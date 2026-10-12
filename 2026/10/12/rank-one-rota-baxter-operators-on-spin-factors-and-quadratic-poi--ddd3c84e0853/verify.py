#!/usr/bin/env python3
"""Independent finite-field checks for rank-one weight-zero Rota--Baxter maps on spin factors.
Run: python3 verify.py; only prime fields are checked; general theorem uses proof.
"""
from itertools import product


def mul(x,y,d,p):
    n=len(d)
    return ((x[0]*y[0]+sum(d[i]*x[i+1]*y[i+1] for i in range(n)))%p,)+tuple((x[0]*y[i+1]+y[0]*x[i+1])%p for i in range(n))

def add(x,y,p): return tuple((a+b)%p for a,b in zip(x,y))
def dot(x,y,p): return sum(a*b for a,b in zip(x,y))%p

def check_R(c,f,d,p):
    N=len(c)
    basis=[tuple(int(j==i) for j in range(N)) for i in range(N)]
    R=lambda x:tuple(dot(f,x,p)*v%p for v in c)
    for i in range(N):
        for j in range(i,N):
            x,y=basis[i],basis[j]
            lhs=mul(R(x),R(y),d,p)
            rhs=R(add(mul(R(x),y,d,p),mul(x,R(y),d,p),p))
            if lhs!=rhs:return False
    return True

def normalized(v,p):
    a=next(x for x in v if x)
    inv=pow(a,-1,p)
    return tuple((z*inv)%p for z in v)

def predict(p,d):
    n=len(d); N=n+1
    def chi(x):
        x%=p
        return 0 if x==0 else (1 if pow(x,(p-1)//2,p)==1 else -1)
    P=(p**n-1)//(p-1)
    if n%2:
        Delta=(-1)**((n+3)//2)
        for x in d:Delta*=x
        P+=chi(Delta)*p**((n-1)//2)
    return P*(p**(n-1)-1),P

def test(p,d):
    n=len(d);N=n+1
    allvec=list(product(range(p), repeat=N))
    lines={normalized(v,p) for v in allvec if any(v)}
    allf=[v for v in allvec if any(v)]
    expected,points=predict(p,d)
    assert points==sum(1 for c in lines if (sum(di*u*u for di,u in zip(d,c[1:]))-c[0]**2)%p==0)
    verified=0;spec=0
    for c in lines:
        zeroform=(sum(di*u*u for di,u in zip(d,c[1:]))-c[0]**2)%p==0
        for f in allf:
            good=check_R(c,f,d,p)
            predicted=zeroform and f[0]==0 and dot(c[1:],f[1:],p)==0
            if good!=predicted:
                raise AssertionError((p,d,c,f,good,predicted))
            verified+=int(good)
            spec+=int(predicted)
    assert verified==expected==spec,(p,d,verified,expected)
    print('field',p,'diagonal',d,'rank_one',verified,'projective_quadric',points,'tested_rank_one',len(lines)*len(allf))

if __name__=='__main__':
    for p,d in [(3,[1,1]),(5,[1,2]),(7,[1,1]),(3,[1,1,1]),(3,[1,1,2]),(5,[1,1,1]),(5,[1,1,2]),(3,[1,1,1,1])]:
        test(p,d)
    print('VERIFY_OK')
