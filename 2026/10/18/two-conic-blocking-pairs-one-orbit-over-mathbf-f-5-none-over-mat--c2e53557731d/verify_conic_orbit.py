"""Independent fixed-conic orbit and 5-field incidence cross-check.

Run: python verify_conic_orbit.py.
"""
from itertools import product
from verify_conic_census import normalized_vectors,quadratic,smooth

q=5
points=list(normalized_vectors(q,3))
loc={p:i for i,p in enumerate(points)}
lines=[sum(1<<i for i,(x,y,z) in enumerate(points) if (a*x+b*y+c*z)%q==0) for a,b,c in points]

def pmask(v):
    return sum(1<<i for i,p in enumerate(points) if quadratic(v,p,q)==0)

C0=pmask((0,0,1,4,0,0))
missing=[lm for lm in lines if lm&C0==0]
partners=set()
for v in normalized_vectors(q,6):
    if not smooth(v,q):continue
    pm=pmask(v)
    if all(pm&lm for lm in missing):partners.add(pm)
assert len(partners)==12

# All projective transformations induced by binary linear changes of
# homogeneous coordinates on the standard Veronese conic xz-y^2=0.
permutations=set()
for a,b,c,d in product(range(q),repeat=4):
    if (a*d-b*c)%q==0:continue
    perm=[]
    for x,y,z in points:
        X=(a*a*x+2*a*b*y+b*b*z)%q
        Y=(a*c*x+(a*d+b*c)*y+b*d*z)%q
        Z=(c*c*x+2*c*d*y+d*d*z)%q
        for v in (X,Y,Z):
            if v:inv=pow(v,-1,q);break
        perm.append(loc[(X*inv%q,Y*inv%q,Z*inv%q)])
    permutations.add(tuple(perm))
assert len(permutations)==120

def apply(pm,permutation):
    ret=0
    for index,transformed in enumerate(permutation):
        if pm>>index&1:ret|=1<<transformed
    return ret
assert all(apply(C0,p)==C0 for p in permutations)
image={apply(next(iter(partners)),p) for p in permutations}
assert image==partners
line_spectrum=set()
for pm in partners:
    union=pm|C0
    line_spectrum.add(tuple(sum(int((union & lm).bit_count()==j) for lm in lines) for j in range(7)))
    assert (pm&C0).bit_count()==1 and union.bit_count()==11
assert line_spectrum=={(0,11,10,5,5,0,0)}
# |PGL_3(F5)| = 372000, hence one unordered pair orbit, stabilizer 20.
assert (5**3-1)*(5**3-5)*(5**3-25)//(5-1)==372000
assert 372000//(3100*12//2)==20
print('PGL2(F5) order:',len(permutations))
print('fixed-conic partner orbit:',len(image))
print('unique line-intersection profile:',next(iter(line_spectrum)))
print('global unordered pair orbit size:',3100*len(partners)//2)
print('unordered pair stabilizer:',20)
print('PASS')
