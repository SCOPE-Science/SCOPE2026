"""Exact enumeration of pencils of smooth plane cubics over GF(2).

Requires Python 3 and SymPy. No third-party data files are used.
"""
import itertools
from collections import Counter
import sympy as sp

X, Y, Z = sp.symbols('X Y Z')
SYMS = (X, Y, Z)
MON = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
F2POINTS = [(0,0,1),(0,1,0),(0,1,1),(1,0,0),
            (1,0,1),(1,1,0),(1,1,1)]

def polynomial(mask):
    return sum(((mask >> k) & 1)*X**i*Y**j*Z**l
               for k,(i,j,l) in enumerate(MON))

def smooth_groebner(mask):
    f=polynomial(mask)
    gradient=[sp.diff(f,t) for t in SYMS]
    for t in SYMS:
        rem=[s for s in SYMS if s!=t]
        g=sp.groebner([v.subs(t,1) for v in gradient],*rem,
                      modulus=2,order='lex')
        if not (len(g.polys)==1 and g.polys[0].as_expr()==1):
            return False
    return True

def eval_f(mask,p):
    a,b,c=p
    return sum(((mask >> k)&1)*(a**i)*(b**j)*(c**l)
               for k,(i,j,l) in enumerate(MON)) % 2

def npoints(mask):
    return sum(eval_f(mask,p)==0 for p in F2POINTS)

def base_rational(triple):
    return sum(eval_f(triple[0],p)==0 and eval_f(triple[1],p)==0
               for p in F2POINTS)

def poly_mul(a,b):
    o={}
    for m,v in a.items():
        for n,w in b.items():
            if v and w:
                k=tuple(m[i]+n[i] for i in range(3))
                o[k]=o.get(k,0)^1
    return {k:v for k,v in o.items() if v}

def linear(row):
    return {tuple(int(i==j) for i in range(3)):1
            for j,v in enumerate(row) if v}

def matrices_and_actions():
    for bits in range(512):
        rows=[tuple((bits >> (3*i+j))&1 for j in range(3))
              for i in range(3)]
        imgs={tuple(sum(rows[i][j]*v[j] for j in range(3))%2
               for i in range(3))
              for v in itertools.product(range(2),repeat=3)}
        if len(imgs)!=8: continue
        L=[linear(row) for row in rows]
        actions=[]
        for e in MON:
            P={(0,0,0):1}
            for ind,degree in enumerate(e):
                for _ in range(degree):P=poly_mul(P,L[ind])
            actions.append(sum(v << MON.index(k) for k,v in P.items()))
        yield actions

def transform(mask,actions):
    result=0
    for k in range(10):
        if (mask>>k)&1: result ^=actions[k]
    return result

def base_reduced(triple):
    f,g=map(polynomial,triple[:2])
    for t in SYMS:
        rem=[s for s in SYMS if s!=t]
        ff=sp.expand(f.subs(t,1));gg=sp.expand(g.subs(t,1))
        jac=sp.diff(ff,rem[0])*sp.diff(gg,rem[1])-sp.diff(ff,rem[1])*sp.diff(gg,rem[0])
        h=sp.groebner([ff,gg,jac],*rem,modulus=2,order='lex')
        if not (len(h.polys)==1 and h.polys[0].as_expr()==1): return False
    return True

def main():
    smooth={F for F in range(1,1024) if smooth_groebner(F)}
    print("smooth",len(smooth))
    triples={tuple(sorted((a,b,a^b))) for a in smooth for b in smooth
             if a<b and (a^b) in smooth}
    print("triples",len(triples))
    actions=list(matrices_and_actions())
    assert len(actions)==168
    remain=set(triples)
    orbits=[]
    while remain:
        P=min(remain)
        orb={tuple(sorted(transform(F,A) for F in P)) for A in actions}
        assert orb <= remain or orb.isdisjoint(remain)==False
        assert orb <= triples
        remain.difference_update(orb)
        orbits.append((P,len(orb),base_rational(P),
                       tuple(sorted(npoints(F) for F in P)),base_reduced(P)))
    orbits.sort()
    print("number_orbits",len(orbits))
    
    
    
    print('nonzero ternary cubics = 1023')
    print('geometrically smooth cubics =',len(smooth))
    print('all-smooth rational pencils =',len(triples))
    print('PGL_3(F2) order =',len(actions))
    print('projective pencil orbits =',len(orbits))
    print('representatives (three polynomial masks), orbit size, rational base, rational member point counts, reduced base:')
    for row in orbits:print(*row)
    print('total reduced-base pencils =',sum(sz for _,sz,_,_,r in orbits if r))
    print('total nonreduced-base pencils =',sum(sz for _,sz,_,_,r in orbits if not r))
    print('mass by rational base and member counts:')
    tab=Counter((base_rational(P),tuple(sorted(npoints(F) for F in P))) for P in triples)
    for k,v in sorted(tab.items()):print(k,v)

if __name__=='__main__':main()
