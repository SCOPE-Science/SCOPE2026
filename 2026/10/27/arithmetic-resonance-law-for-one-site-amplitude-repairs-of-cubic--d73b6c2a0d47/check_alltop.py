"""Standalone numerical cross-checks of an exact cubic-chirp ambiguity theorem.

The theorem is established analytically by a quadratic Gauss-sum identity;
these finite computations check formulas and exceptional cases only.
"""
import cmath
import math


def legendre(x,p):
    s=pow(x%p,(p-1)//2,p)
    assert s in (1,p-1)
    return 1 if s==1 else -1


def predicted(p,t,a,b):
    z=cmath.exp(2j*math.pi/p)
    if a==0:
        return complex(p-1+t*t if b==0 else t*t-1)
    mod=lambda x:x%p
    A=mod(3*a)
    B=mod(3*a*a+b)
    C=mod(B*B*pow(4*A,-1,p))
    eps=1 if p%4==1 else 1j
    return z**mod(a**3)*(eps*legendre(A,p)*math.sqrt(p)*z**(-C)+(t-1)*(1+z**mod(-a*b)))


def direct(p,t,a,b):
    z=cmath.exp(2j*math.pi/p)
    g=lambda j:complex(t) if j%p==0 else z**((j%p)**3%p)
    return sum(g(j+a)*g(j).conjugate()*z**(b*j%p) for j in range(p))


def exceptional_amplitudes(p):
    if p%4==3:
        return []
    result=[]
    for a in range(1,p):
        chi=legendre(3*a,p)
        for b in range(p):
            if (b*b+9*pow(a,4,p))%p:
                continue
            h=(a*b*pow(2,-1,p))%p
            S=2*math.cos(2*math.pi*h/p)
            assert abs(S)>1e-10
            if chi*S<0:
                t=1-chi*math.sqrt(p)/S
                assert t>1
                result.append((a,b,t))
    return result


def main():
    primes=(5,7,11,13,17,19,23,29,31,37)
    tests=0
    for p in primes:
        for t in (0,0.5,1,1.125,2.5):
            for a in range(p):
                for b in range(p):
                    d=direct(p,t,a,b)
                    f=predicted(p,t,a,b)
                    assert abs(d-f)<2e-9, (p,t,a,b,d,f)
                    tests+=1
        ex=exceptional_amplitudes(p)
        if p%4==3:
            assert ex==[]
        for a,b,t in ex:
            assert abs(direct(p,t,a,b)) < 2e-9, (p,a,b,t)
    assert not exceptional_amplitudes(5)
    assert not exceptional_amplitudes(13)
    e17=exceptional_amplitudes(17)
    assert len(e17)==8
    t17=1+math.sqrt(17)/(2*math.cos(math.pi/17))
    assert any(a==3 and b==6 and abs(t-t17)<1e-11 for a,b,t in e17)
    assert abs(direct(17,t17,3,6))<1e-10
    print('PASS',tests,'direct-versus-Gauss checks; p=5,13 no exceptional amplitudes; p=17 has',len(e17),'resonant cells')
    print('p=17 example t=',repr(t17))

if __name__=='__main__':main()
