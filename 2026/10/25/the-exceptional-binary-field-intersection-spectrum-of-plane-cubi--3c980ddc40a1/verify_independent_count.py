"""Independent counting by restriction-pattern classes and divisor incidence.

Usage: python verify_independent_count.py
Requires Python 3 and SymPy. Counts unordered pairs and doubles at the end.
"""
from collections import Counter,defaultdict
from itertools import combinations
from sympy import symbols, Poly
x,y,z=symbols('x y z')
C=[x**3,x**2*y,x**2*z,x*y**2,x*y*z,x*z**2,y**3,y**2*z,y*z**2,z**3]
Q=[x**2,x*y,x*z,y**2,y*z,z**2]
L=[x,y,z]
EXP={tuple(Poly(t,x,y,z).monoms()[0]):i for i,t in enumerate(C)}
P=[(int(i&4>0),int(i&2>0),int(i&1>0)) for i in range(1,8)]

def vector(poly):
    poly=Poly(poly,x,y,z,modulus=2)
    return sum(1<<EXP[mon] for mon,coeff in poly.terms() if int(coeff)%2)

def form(polyterms,mask):
    return sum(t for j,t in enumerate(polyterms) if mask>>j&1)

def zero_pattern(mask):
    p=Poly(form(C,mask),x,y,z,modulus=2)
    out=0
    for i,(a,b,c) in enumerate(P):
        if p.eval({x:a,y:b,z:c})==0:out |= 1<<i
    return out

def main():
    zvals=[0]+[zero_pattern(j) for j in range(1,1024)]
    classcount=Counter(zvals[1:])
    allpairs=Counter()
    for a,n in classcount.items():
        allpairs[a.bit_count()] += n*(n-1)//2
        for b,m in classcount.items():
            if a<b:allpairs[(a&b).bit_count()] += n*m
    pairs=set()
    for line in range(1,8):
        cands={vector(form(L,line)*form(Q,q)) for q in range(1,64)}
        assert len(cands)==63
        pairs.update(combinations(sorted(cands),2))
    for q in range(1,64):
        cands={vector(form(Q,q)*form(L,l)) for l in range(1,8)}
        assert len(cands)==7
        pairs.update(combinations(sorted(cands),2))
    assert len(pairs)==13965
    excluded=Counter((zvals[a]&zvals[b]).bit_count() for a,b in pairs)
    coprime=allpairs-excluded
    assert coprime=={0:69972,1:163191,2:162918,3:85554,4:23604,5:3339,6:210}
    # Sample multivariate polynomial gcds validate independently that divisor
    # incidence detects common components, both on shared and coprime pairs.
    forms=[None]+[Poly(form(C,i),x,y,z,modulus=2) for i in range(1,1024)]
    import random
    rng=random.Random(1)
    for a,b in rng.sample(sorted(pairs),500):
        assert forms[a].gcd(forms[b]).total_degree()>0
    checked=0
    while checked<500:
        a=rng.randrange(1,1024);b=rng.randrange(1,1024)
        if a>=b or (a,b) in pairs:continue
        assert forms[a].gcd(forms[b]).total_degree()==0
        checked+=1
    print('restriction patterns',len(classcount))
    print('all distinct unordered pairs',dict(sorted(allpairs.items())))
    print('shared-component unordered pairs',dict(sorted(excluded.items())))
    print('coprime ordered intersection counts',dict(sorted((k,2*v) for k,v in coprime.items())))
    print('SymPy gcd sample check: 500 shared, 500 coprime')
    print('PASS')
if __name__=='__main__':main()
