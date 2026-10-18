#!/usr/bin/env python3
"""Direct finite-group convolution and fourth-moment checks for the two-axis theorem.
Run: python3 verify_axes.py. Python 3 standard library only.
The checks are finite corroboration of the unrestricted algebraic argument.
"""
import cmath
import itertools
import math
import random


def elements(moduli):
    return list(itertools.product(*(range(m) for m in moduli)))


def add(x, y, m):
    return tuple((a+b) % d for a, b, d in zip(x, y, m))


def neg(x, m):
    return tuple((-a) % d for a, d in zip(x, m))


def char(x, k, m):
    return cmath.exp(2j*math.pi*sum(a*b/d for a,b,d in zip(x,k,m)))


def compute(moduli, f):
    A=elements(moduli); z=tuple(0 for _ in moduli); N=len(A)
    S=[(z,z)]+[(x,z) for x in A if x!=z]+[(z,x) for x in A if x!=z]
    assert len(f)==len(S)
    vals=dict(zip(S,f)); a=vals[(z,z)]
    g={x:vals[(x,z)] if x!=z else a for x in A}
    h={x:vals[(z,x)] if x!=z else a for x in A}
    mass=sum(abs(w)**2 for w in f)
    C={(x,y):0j for x in A for y in A}
    for t,ft in vals.items():
        for u,fu in vals.items():
            C[(add(t[0],u[0],moduli),add(t[1],u[1],moduli))]+=ft*fu
    Q=sum(abs(w)**2 for w in C.values())
    def pieces(w):
        G=sum(abs(w[x])**2 for x in A if x!=z)
        B=sum(w[x]*w[neg(x,moduli)] for x in A if x!=z)
        R=sum(abs(w[x])**2*abs(w[neg(x,moduli)])**2 for x in A if x!=z)
        D=0.
        for s in A:
            if s==z: continue
            prods=[w[t]*w[add(s,neg(t,moduli),moduli)] for t in A]
            D+=N*sum(abs(p)**2 for p in prods)-abs(sum(prods))**2
        return G,B,R,D
    G,Bg,Rg,Dg=pieces(g); H,Bh,Rh,Dh=pieces(h)
    l=abs(a)**2; b=abs(Bg); c=abs(Bh)
    theta=2*N-6-2/(N-1)
    terms=[Dg,Dh,N*(Rg-b*b/(N-1)),N*(Rh-c*c/(N-1)),
           ((N-1)*l-b-c)**2/(N-1),theta*b*c,
           (2*N-4)*(G*H-b*c),
           (l+b+c)**2-abs(a*a+Bg+Bh)**2]
    lhs=N*mass**2-Q
    assert abs(lhs-sum(terms))<=1e-7*max(1,abs(lhs),abs(sum(terms))), (moduli,lhs,terms)
    if N>=4:
        assert all(t>=-1e-7*max(1,mass**2) for t in terms), (moduli,terms)
        assert lhs>=-1e-7*max(1,mass**2),(moduli,lhs)
    return Q,mass,terms,S


def check():
    rng=random.Random(208034)
    tested=0
    for m in ((3,),(4,),(5,),(6,),(7,),(2,2),(2,4),(3,3)):
        A=elements(m);N=len(A); z=tuple(0 for _ in m)
        S=[(z,z)]+[(x,z) for x in A if x!=z]+[(z,x) for x in A if x!=z]
        for _ in range(65):
            f=[complex(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in S]
            Q,M,terms,_=compute(m,f)
            tested+=1
        if N>=4:
            for axis in (0,1):
                for dual in A[:min(3,N)]:
                    f=[char(p[axis],dual,m) if p[1-axis]==z else 0j for p in S]
                    Q,M,terms,_=compute(m,f)
                    assert abs(Q-N*M*M)<1e-7*(1+N*M*M)
                    assert max(abs(t) for t in terms)<1e-7*(1+N*M*M)
                    tested+=1
            # Fourier normalization checked independently, without using Plancherel identity.
            duals=elements(m)
            f=[(2+3j)*char(p[0],duals[0],m) if p[1]==z else 0j for p in S]
            Q,M,_,_=compute(m,f)
            E4=sum(abs(sum(ft*char(p[0],k,m)*char(p[1],h,m) for ft,p in zip(f,S))/len(S))**4
                   for k in duals for h in duals)
            ratio=E4/(M/len(S))**2
            assert abs(ratio-N**3/(2*N-1)**2)<1e-7*max(1,ratio)
    # The order-three case is deliberately excluded from the stated inequality.
    f=[1.186+0j]+[1+0j]*4
    Q,M,_,_=compute((3,),f)
    assert Q/M**2>3.10
    print(f'VERIFY_OK groups=8 complex_inputs={tested} exact_deficit_identity=PASS axes_extremizers=PASS fourier_normalization=PASS exceptional_order_three=PASS')


if __name__=='__main__':
    check()
