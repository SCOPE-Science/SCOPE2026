"""Exact-rational checks for the hyperflower cluster-contraction and critical-equilibrium theorem.

Usage: python CHECKER.py
No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import product

def tri(z):
    k=z//2
    r=z-2*k
    return r if r<=1 else 2-r

def tent(z,mu):
    return mu*min(z,1-z)/2

def delta(fx,c,t,l):
    k=c+t-1
    C=sum(fx[:c],F(0))
    d=[F(0)]*(c+t*l)
    q=[]
    for j in range(l):
        P=sum(fx[c+j*t:c+(j+1)*t],F(0))
        q.append(C-P)
    for i in range(c):
        d[i]=sum(q,F(0))/(l*k)
    for j in range(l):
        for v in range(t):d[c+j*t+v]=-q[j]/k
    return d

def step(x,c,t,l,mu,eps):
    fx=[tent(v,mu) for v in x]
    dx=delta(fx,c,t,l)
    return [tri(a-eps*b) for a,b in zip(fx,dx)]

def blocks(c,t,l):
    return [list(range(c))]+[list(range(c+j*t,c+(j+1)*t)) for j in range(l)]

def diameter(x,c,t,l):
    return max((max(x[i] for i in block)-min(x[i] for i in block) for block in blocks(c,t,l)),default=F(0))

def check():
    assertions=0
    # Independent incidence-matrix expansion of the Laplacian.
    for c,t,l in product((1,2,3),(1,2,3),(1,2,3)):
        for r in range(4):
            n=c+t*l
            x=[F((3*i+2*r+1)%13,16) for i in range(n)]
            got=delta(x,c,t,l)
            B=[]
            for j in range(l):
                B.append([F(1) if i<c else (F(-1) if c+j*t<=i<c+(j+1)*t else F(0)) for i in range(n)])
            D=[l*(c+t-1)]*c+[c+t-1]*(t*l)
            by_incidence=[sum((B[j][i]*sum((B[j][k]*x[k] for k in range(n)),F(0)) for j in range(l)),F(0))/D[i] for i in range(n)]
            assert got==by_incidence
            assertions+=n
            for mu,eps in product((F(1,2),F(9,5),F(2)),(F(-23,5),F(0),F(3),F(27,4))):
                a=step(x,c,t,l,mu,eps)
                assert all(F(0)<=y<=F(1) for y in a); assertions+=n
                assert diameter(a,c,t,l)<=mu/2*diameter(x,c,t,l); assertions+=1
                y=x
                for _ in range(4):
                    z=step(y,c,t,l,mu,eps)
                    assert diameter(z,c,t,l)<=mu/2*diameter(y,c,t,l)
                    assertions+=1
                    y=z
    # Sharp rate: uncoupled tent map acts linearly on the lower half.
    for mu in (F(1,3),F(1),F(9,5)):
        x=[F(0),F(1,4),F(0),F(0),F(0),F(0)] # c=2,t=2,l=2
        d=diameter(x,2,2,2)
        for n in range(12):
            assert diameter(x,2,2,2)==d*(mu/2)**n
            assertions+=1
            x=step(x,2,2,2,mu,F(0))
    # At mu=2 the kernel polytope has non-cluster fixed states.
    for c,t,l in product((1,2,3),(1,2,3),(1,2,3)):
        a=F(t,4*(c+t)); b=F(c,4*(c+t))
        v=[a]*c+[b]*(t*l)
        assert all(z==0 for z in delta(v,c,t,l)); assertions+=1
        for eps in (F(-17),F(0),F(1),F(11,2)):
            assert step(v,c,t,l,F(2),eps)==v
            assertions+=1
        if c>=2:
            h=min(a,F(1,16))
            v[0]+=h;v[1]-=h
        elif t>=2:
            h=min(b,F(1,16))
            v[c]+=h;v[c+1]-=h
        else:
            continue
        assert diameter(v,c,t,l)>0
        assert all(z==0 for z in delta(v,c,t,l));assertions+=2
        assert step(v,c,t,l,F(2),F(5))==v; assertions+=1
    # Above the boundary, disconnected scalar fixed points remain at zero coupling.
    for mu in (F(5,2),F(3),F(4)):
        a=mu/(mu+2)
        assert tent(a,mu)==a and tent(F(0),mu)==0
        x=[F(0),a,F(0),F(0)]
        assert step(x,2,2,1,mu,F(0))==x
        assert diameter(x,2,2,1)>0
        assertions+=4
    print('Exact rational assertions passed:',assertions)

if __name__=='__main__': check()
