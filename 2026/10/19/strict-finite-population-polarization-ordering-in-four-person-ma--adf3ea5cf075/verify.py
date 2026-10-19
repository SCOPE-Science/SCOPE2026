"""Exact independent verification for the finite-state polarization theorem.

Usage: python3 verify.py
Python standard library only. All comparisons use fractions.Fraction.
"""
from fractions import Fraction as F
from math import factorial, comb

def falling(a, j):
    if a < j: return 0
    z=1
    for b in range(j): z*=a-b
    return z

def rates(n, k, p, mode):
    den=falling(n,4)
    u=F(4*(n-k)*falling(k,3),den)
    v=F(4*k*falling(n-k,3),den)
    if mode == 'independence':
        return (1-p)*u + p*F(2*(n-k),n), (1-p)*v + p*F(2*k,n)
    if mode == 'anticonformity':
        return (1-p)*u + p*F(falling(n-k,4),den), (1-p)*v + p*F(falling(k,4),den)
    raise ValueError(mode)

def stationary(n,p,mode):
    weights=[F(1)]
    for k in range(n):
        up=rates(n,k,p,mode)[0]
        down=rates(n,k+1,p,mode)[1]
        assert up > 0 and down > 0
        weights.append(weights[-1]*up/down)
    Z=sum(weights)
    return [w/Z for w in weights]

def radius(n,pi):
    out={}
    for k,mass in enumerate(pi):
        d=abs(2*k-n)
        out[d]=out.get(d,F(0))+mass
    return sorted(out.items())

def right_ratios(n,p,mode):
    r=[]
    for k in range((n+1)//2,n):
        num=rates(n,k,p,mode)[0]
        den=rates(n,k+1,p,mode)[1]
        r.append(num/den)
    return r

def run():
    ps=[F(1,25),F(1,10),F(1,4),F(1,3),F(1,2),F(2,3),F(9,10),F(24,25)]
    checks=0; ntest=0; singleton=0
    for mode in ('independence','anticonformity'):
        for n in range(6,31):
            for p in ps:
                pi=stationary(n,p,mode)
                assert sum(pi)==1
                for k in range(n+1):
                    assert pi[k]==pi[n-k]
                    checks+=1
                for k in range(n):
                    up=rates(n,k,p,mode)[0]
                    down=rates(n,k+1,p,mode)[1]
                    assert pi[k]*up==pi[k+1]*down
                    checks+=1
                ntest+=1
            for i in range(len(ps)-1):
                lo, hi=ps[i:i+2]
                rlo, rhi=right_ratios(n,lo,mode),right_ratios(n,hi,mode)
                for a,b in zip(rlo,rhi):
                    assert a>b, (mode,n,lo,hi,a,b)
                    checks+=1
                dlo=radius(n,stationary(n,lo,mode))
                dhi=radius(n,stationary(n,hi,mode))
                assert [a for a,b in dlo]==[a for a,b in dhi]
                for j in range(1,len(dlo)):
                    tail_lo=sum(x[1] for x in dlo[j:]); tail_hi=sum(x[1] for x in dhi[j:])
                    assert tail_lo>tail_hi, (mode,n,lo,hi,j,tail_lo,tail_hi)
                    checks+=1
                # The ratios of radial masses decrease strictly with p.
                for j in range(1,len(dlo)):
                    assert dlo[j][1]/dlo[j-1][1] > dhi[j][1]/dhi[j-1][1]
                    checks+=1
        if mode=='independence':
            for n in range(6,31):
                pi=stationary(n,F(1),mode)
                assert all(pi[k]==F(comb(n,k),2**n) for k in range(n+1))
                checks+=n+1
    # Exact small-population boundary for the anticonformist chain.
    for n in (4,5):
        cut=n//2
        assert rates(n,cut,F(1,2),'anticonformity')[0]==0
        if n==4:
            assert rates(n,cut,F(1,2),'anticonformity')[1]==0
        else:
            assert rates(n,cut+1,F(1,2),'anticonformity')[1]==0
        checks+=2
    print(f'PASS: {checks} exact identities/strict comparisons; {ntest} stationary distributions')
    for mode in ('independence','anticonformity'):
        for p in (F(1,4),F(1,2)):
            pi=stationary(6,p,mode)
            val=sum(pi[k] for k in range(7) if abs(2*k-6)>=4)
            print(mode, 'N=6,p=',p,'P(D>=4)=',val)

if __name__=='__main__': run()
