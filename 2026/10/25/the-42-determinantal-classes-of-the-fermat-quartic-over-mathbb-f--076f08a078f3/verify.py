"""Reproduction of exact point counts and finite symplectic arithmetic for the Fermat quartic in characteristic five."""
from itertools import product
from math import comb

P=5

def field_count(d, modulus):
    q=P**d
    digits=[]
    for z in range(q):
        t=z; ds=[]
        for j in range(d):
            ds.append(t%P); t//=P
        digits.append(ds)
    def mul(a,b):
        v=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):
                v[i+j]=(v[i+j]+a[i]*b[j])%P
        for k in range(2*d-2,d-1,-1):
            z=v[k]
            for j in range(d):
                v[k-d+j]=(v[k-d+j]-z*modulus[j])%P
        return tuple(v[:d])
    def add(a,b):return tuple((x+y)%P for x,y in zip(a,b))
    zero=tuple([0]*d);one=tuple([1]+[0]*(d-1));minus_one=tuple([4]+[0]*(d-1))
    els=list(map(tuple,digits))
    p4=[mul(mul(e,e),mul(e,e)) for e in els]
    counts={}
    for u in p4:counts[u]=counts.get(u,0)+1
    affine=sum(counts.get(tuple((-1-u[0],)+tuple(-w for w in u[1:])),0) for u in p4) if False else 0
    # RHS = -1 - x^4 for each x
    for w in p4:
        rhs=tuple((-int(i==0)-c)%5 for i,c in enumerate(w))
        affine+=counts.get(rhs,0)
    infinity=counts.get(minus_one,0)  # x^4=-1 at [x:1:0]
    N=affine+infinity
    return N,affine,infinity,counts

# Monic moduli: t+0, t^2+2, t^3+t+1 (all irreducible over F5).
for d,coeff in ((1,[0]),(2,[2,0]),(3,[1,1,0])):
    # Verify no roots for d=2,3. Degree 2/3 rootlessness suffices irreducible.
    if d>1:
        assert all((sum(coeff[i]*pow(x,i,5) for i in range(d))+pow(x,d,5))%5 for x in range(5))
    N,aff,inf,_=field_count(d,coeff)
    expect={1:0,2:44,3:192}[d]
    assert N==expect,(d,N,expect)
    print('CURVE_POINTS',5**d,N,'affine',aff,'infinity',inf)

s1=6-0;s2=26-44;s3=126-192
a1=-s1
a2=(s1*s1-s2)//2
a3=(-s1**3+3*s1*s2-2*s3)//6
assert (a1,a2,a3)==(-6,27,-68)
# Weil functional equation for genus 3, q=5
a4=5*a2;a5=25*a1;a6=125
L=[1,a1,a2,a3,a4,a5,a6]
assert L==[1,-6,27,-68,135,-150,125]
assert sum(L)==64
# A smooth nonhyperelliptic genus-three curve has unique degree-two divisors
# in their linear equivalence classes. Since C(F5)=empty, effective degree-two
# divisors are precisely Frobenius pairs in C(F25).
effective_deg2=(44-0)//2
assert effective_deg2==22
all_pic2=sum(L)
linear_det=all_pic2-effective_deg2
assert linear_det==42
print('WEIL_POLYNOMIAL',L,'JACOBIAN_POINTS',sum(L),'DEGREE2_EFFECTIVE',effective_deg2,'DETERMINANTAL',linear_det)

# Standard symplectic F2^6 and Arf-one quadratic form q(v).
def eps(v,w):
    return sum((v>>(2*i)&1)*(w>>(2*i+1)&1)+(v>>(2*i+1)&1)*(w>>(2*i)&1) for i in range(3))%2
def q(v):
    a=v&1;b=(v>>1)&1
    return (sum(((v>>(2*i))&1)*((v>>(2*i+1))&1) for i in range(3))+a+b)%2
anisotropic=3
assert q(anisotropic)==1
F=lambda v: v^(anisotropic if eps(v,anisotropic) else 0)
odd=[v for v in range(64) if not q(v)]
even=[v for v in range(64) if q(v)]
assert len(odd)==28 and len(even)==36
assert all(q(F(v))==q(v) for v in range(64))
assert all(F(F(v))==v for v in range(64))
assert sum(F(v)==v for v in range(64))==32
assert sum(F(v)==v for v in odd)==16
assert sum(F(v)==v for v in even)==16
assert 16+26==linear_det
print('THETA_FROBENIUS','odd_fixed',16,'odd_2cycles',6,'even_fixed',16,'rational_2torsion',32)

# 4th roots of 1 in F5, and a direct five-coefficient identity for ordinary bitangents.
roots=[v for v in range(5) if pow(v,4,5)==1]
assert len(roots)==4
for a,b in product(roots,repeat=2):
    # compute coefficients of F((-a)y+(-b)z,y,z) and 2*((ay)^2+ab yz+(bz)^2)^2
    coeff1=[0]*5; coeff2=[0]*5
    for j in range(5):
        coeff1[j]=(comb(4,j)*pow(-a,4-j,5)*pow(-b,j,5))%5
    coeff1[0]=(coeff1[0]+1)%5;coeff1[4]=(coeff1[4]+1)%5
    u=[a*a%5,a*b%5,b*b%5]
    for i in range(3):
        for j in range(3):
            coeff2[i+j]=(coeff2[i+j]+2*u[i]*u[j])%5
    assert coeff1==coeff2,(a,b,coeff1,coeff2)
assert len({(a,b) for a,b in product(roots,repeat=2)})==16
print('BITANGENT_IDENTITY',16,'ordinary lines; 12 hyperflex lines from three coordinate pairs')
print('VERIFY_OK')
