# Projective orbit classification of bidegree-(3,3) forms over F2.
from itertools import product
from collections import Counter,defaultdict
from pathlib import Path
from sympy import symbols,Poly,groebner

basis=list(product((0,1),repeat=4))
G=[]
for a,b,c,d in product(range(2),repeat=4):
    if (a*d+b*c)%2==1:G.append((a,b,c,d))
assert len(G)==6

def polymul(P,Q):
    R={}
    for k,v in P.items():
        for l,w in Q.items():R[k+l]=R.get(k+l,0) ^ (v&w)
    return {k:v for k,v in R.items() if v}

def powlinear(a,b,n):
    P={0:1}
    for _ in range(n):P=polymul(P,{0:b,1:a} if a and b else ({1:1} if a else ({0:1} if b else {})))
    return P

def trans3(g):
    a,b,c,d=g
    return [sum((1<<k) for k,v in polymul(powlinear(a,b,i),powlinear(c,d,3-i)).items() if v) for i in range(4)]
T={g:trans3(g) for g in G}
assert all(len(set(T[g]))==4 for g in G)
maps=[]
for g,h,z in product(G,G,range(2)):
    basis_map=[]
    for i in range(4):
        for j in range(4):
            v=0
            for k in range(4):
                for l in range(4):
                    if (T[g][i]>>k&1) and (T[h][j]>>l&1):
                        v^=1 << ((l*4+k) if z else (k*4+l))
            basis_map.append(v)
    lut0,lut1=[0]*256,[0]*256
    for idx in range(256):
        for bit in range(8):
            if idx>>bit&1:lut0[idx]^=basis_map[bit];lut1[idx]^=basis_map[bit+8]
    maps.append((lut0,lut1))
assert len(maps)==72

def mapmask(mask,m):return m[0][mask&255]^m[1][mask>>8]
S=set(map(int,Path('candidates.txt').read_text().split()))
assert len(S)==16020
orig=len(S)
orbits=[]
while S:
    r=min(S)
    orb=set(mapmask(r,m) for m in maps)
    assert orb<=S
    orbits.append((r,len(orb)))
    S.difference_update(orb)
print('ORBIT_COUNT',len(orbits),'ORBIT_SIZE_COUNTS',dict(sorted(Counter(n for _,n in orbits).items())))
assert sum(n for _,n in orbits)==orig
Path('orbit_reps.txt').write_text(''.join(f'{r} {n}\n' for r,n in orbits))

x,y=symbols('x y')
def chart_eq(mask,ix,iy):
    f=0
    for i in range(4):
        for j in range(4):
            if mask>>(i*4+j)&1:f+=x**(3-i if ix else i)*y**(3-j if iy else j)
    return Poly(f,x,y,modulus=2).as_expr()

fails=[]
for count,(r,n) in enumerate(orbits,1):
    for ix,iy in product(range(2),repeat=2):
        f=chart_eq(r,ix,iy)
        J=groebner([f,f.diff(x),f.diff(y)],x,y,order='grevlex',modulus=2)
        if not J.is_zero_dimensional and J.polys and not any(p.total_degree()==0 and p.LC()%2 for p in J.polys):
            fails.append((r,n,ix,iy,str(J)))
        # unit ideal iff reduced Groebner basis contains 1.
        elif not any(p.total_degree()==0 and p.LC()%2 for p in J.polys):
            fails.append((r,n,ix,iy,str(J)))
    if count%50==0:print('POSITIVE_CHECKS',count,flush=True)
print('UNIT_IDEAL_FAILURES',len(fails),fails[:2])
assert not fails
print('VERIFIED',len(orbits),'positive orbits with all four charts')
