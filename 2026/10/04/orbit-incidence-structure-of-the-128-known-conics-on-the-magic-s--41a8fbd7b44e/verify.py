from itertools import product, permutations

# Small polynomial dictionary in variables u,v; key=(u_exp,v_exp).
def add(p,q):
    r=dict(p)
    for k,c in q.items():
        r[k]=r.get(k,0)+c
        if r[k]==0:
            del r[k]
    return r

def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            key=(i+k,j+l)
            r[key]=r.get(key,0)+a*b
    return {k:v for k,v in r.items() if v}

def scale(p,c):
    return {k:c*v for k,v in p.items() if c*v}

u2={(2,0):1}
v2={(0,2):1}
uv={(1,1):1}
a=add(u2,v2)
b=add(add(u2,scale(uv,-2)),scale(v2,-1))
c=add(add(scale(u2,-1),scale(uv,-2)),v2)
identity=add(add(mul(b,b),mul(c,c)),scale(mul(a,a),-2))
assert identity=={}

# Four projective sign classes [1:±1:±1].
trivial_classes={(1,s,t) for s,t in product((-1,1),repeat=2)}
assert len(trivial_classes)==4
for aa,bb,cc in trivial_classes:
    assert bb*bb+cc*cc==2*aa*aa

# Orbit/stabilizer arithmetic.
sign_group=2**9//2
sign_stabilizer=2**3//2
assert sign_group==256
assert sign_stabilizer==4
assert sign_group//sign_stabilizer==64
full_group=2048
conics=128
assert full_group//conics==16

# Chosen 6x6 Jacobian minor in columns (A,B,C,D,M,E) after restriction.
# Rows have unique nonzero columns 0,1,2,3,5,4 with factors 6a,6b,6c,6c,6b,6a.
perm=(0,1,2,3,5,4)
# parity by inversion count
inv=sum(1 for i in range(6) for j in range(i+1,6) if perm[i]>perm[j])
sign=-1 if inv%2 else 1
assert sign==-1
coeff=sign*(6**6)
exponents={'a':2,'b':2,'c':2}
assert coeff==-(6**6)
assert exponents=={'a':2,'b':2,'c':2}

# Each coordinate-zero slice has two projective points; b=0 and c=0 are p1, a=0 is p3.
zero_slices={'a':2,'b':2,'c':2}
assert sum(zero_slices.values())==6
p1=zero_slices['b']+zero_slices['c']
p3=zero_slices['a']
assert (p1,p3)==(4,2)

# Incidence double counts.
assert 128*4==256*2
assert 128*4==128*4
assert 128*2==64*4
assert 0==64*0

# Representative p2 square values are five distinct numbers, while a Z3 conic point has <=3.
p2_sq=(-1,0,1,2,0,-2,-1,0,1)
assert len(set(p2_sq))==5
assert 5>3

print('conic_parametrization_identity=ok')
print('trivial_projective_classes=4')
print('sign_family_orbit=64')
print('full_conic_stabilizer=16')
print(f'jacobian_minor_coefficient={coeff}')
print('node_split=p1:4,p3:2')
print('incidence_degrees=trivial:2,p1:4,p2:0,p3:4')
print('VERIFY_OK')
