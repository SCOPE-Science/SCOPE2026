"""Exact finite-field checks of Fourier fourth moments on Gold graphs."""
from math import gcd
from itertools import product
import random

POLY={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def mul(x,y,m):
    poly=POLY[m]; out=0
    while y:
        if y&1: out ^= x
        y>>=1; x <<= 1
        if x & (1<<m): x ^= poly
    return out

def power(a,n,m):
    z=1
    while n:
        if n&1: z=mul(z,a,m)
        a=mul(a,a,m); n>>=1
    return z

def absolute_trace(a,m):
    t=a; v=a
    for _ in range(1,m):
        v=mul(v,v,m); t ^= v
    assert t in (0,1)
    return t

def quadratic_signs(m,d):
    n=m//d; q=1<<m; s=1<<d
    sub=[u for u in range(q) if power(u,s,m)==u]
    assert len(sub)==s
    basis=[power(2,j,m) for j in range(n)]
    coord={}
    for vec in product(sub,repeat=n):
        x=0
        for u,z in zip(vec,basis):x ^= mul(u,z,m)
        coord[x]=vec
    assert len(coord)==q
    result={}
    for x,vec in coord.items():
        vv=mul(vec[0],vec[1],m)
        # trace from the subfield F_{2^d} to F_2
        t=vv; w=vv
        for _ in range(1,d):w=mul(w,w,m);t^=w
        assert t in (0,1)
        result[x]=1 if t==0 else -1
    return result

def energy(m,k,eps):
    q=1<<m
    P=[power(x,(1<<k)+1,m) for x in range(q)]
    coeff={}
    for x in range(q):
        for y in range(q):
            key=(x^y,P[x]^P[y]);coeff[key]=coeff.get(key,0)+eps[x]*eps[y]
    return sum(abs(v)**2 for v in coeff.values())

def fibers(m,k):
    q=1<<m; P=[power(x,(1<<k)+1,m) for x in range(q)]
    dd={}
    for a in range(1,q):
        his={}
        for x in range(q):
            b=P[x]^P[x^a]
            his[b]=his.get(b,0)+1
        dd[a]=list(his.values())
    return dd

cases=0; nonlinear=0; nonopt=0;direct=0
for m in range(1,7):
    q=1<<m
    for k in range(1,m+1):
        d=gcd(m,k);s=1<<d
        rows=fibers(m,k)
        assert all(len(row)==q//s and all(v==s for v in row) for row in rows.values())
        target=q*q+s*(q*q-q)
        one={x:1 for x in range(q)}
        assert energy(m,k,one)==target
        lin={x:(-1 if absolute_trace(x,m) else 1) for x in range(q)}
        assert energy(m,k,lin)==target
        if d==1:
            rnd=random.Random(330+m*17+k)
            eps={x:rnd.choice([-1,1]) for x in range(q)}
            assert energy(m,k,eps)==target
        if d>=2 and m//d>=2:
            eps=quadratic_signs(m,d)
            assert energy(m,k,eps)==target
            nonlinear+=1
            assert any(eps[x^y]!=eps[x]*eps[y] for x in range(q) for y in range(q))
        if d>=2 and q>4:
            eps={x:1 for x in range(q)};eps[0]=-1
            assert energy(m,k,eps)<target
            nonopt+=1
        cases+=1

# Actual Fourier transform direct for one nontrivial sample (normalization check).
for m,k in [(2,1),(3,1),(4,2),(5,2)]:
    q=1<<m; eps={x:1 for x in range(q)}
    P=[power(x,(1<<k)+1,m) for x in range(q)]
    e=0
    for a in range(q):
        for b in range(q):
            w=sum(eps[x]*(1 if not absolute_trace(mul(a,x,m)^mul(b,P[x],m),m) else -1) for x in range(q))
            e+=w**4
    assert e==q*q*energy(m,k,eps)
    direct+=1
print(f'VERIFY_OK exact_Gold_cases={cases} nonaffine_quadratic_extremizer_cases={nonlinear} nonextremizer_tests={nonopt} Fourier_orthogonality_checks={direct}')
