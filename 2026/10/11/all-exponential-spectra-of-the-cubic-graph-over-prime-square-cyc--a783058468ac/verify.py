#!/usr/bin/env python3
"""Exact finite arithmetic checks for cubic graph Fourier spectra over prime-square rings."""
from itertools import product
from math import comb


def primes_under(n):
    return [p for p in range(5,n) if all(p%d for d in range(2,int(p**0.5)+1))]


def zero_mod_p(u,v,p):
    if u%p==0 and v%p==0:
        return False
    seen={(u*x+v*x**3)%p for x in range(p)}
    return len(seen)==p


def predict_zero(u,v,p):
    mod=p*p
    u%=mod;v%=mod
    if u%p==v%p==0:
        return zero_mod_p(u//p,v//p,p)
    if v%p==0:
        return u%p!=0
    if u%p==0:
        return False
    s=(-u*pow(3*v,-1,p))%p
    return pow(s,(p-1)//2,p)==p-1


def exact_zero_using_cyclotomic_histogram(u,v,p):
    """Q(z)=sum_z c[z]z^z zero in Q[z]/Phi_{p^2} iff c[r+jp] constant in j."""
    n=p*p
    c=[0]*n
    for x in range(n): c[(u*x+v*x*x*x)%n]+=1
    return all(c[r]==c[r+j*p] for r in range(p) for j in range(1,p))


def slopes(p):
    return {0}|{s for s in range(1,p) if pow((-3*s)%p,(p-1)//2,p)==p-1}


def verify():
    assert primes_under(14)==[5,7,11,13]
    prime_cases=0
    for p in primes_under(14):
        for u,v in product(range(p),repeat=2):
            predicted=(v==0 and u!=0) or (u==0 and v!=0 and p%3==2)
            assert zero_mod_p(u,v,p)==predicted,(p,u,v)
            prime_cases+=1

    exact_cases=0
    for p in primes_under(14):
        n=p*p
        expected=n*(p-1)+n*(p-1)**2//2+(p-1)*(1+(p%3==2))
        observed=0
        for u in range(n):
            for v in range(n):
                exact=exact_zero_using_cyclotomic_histogram(u,v,p)
                pred=predict_zero(u,v,p)
                assert exact==pred,(p,u,v,exact,pred)
                observed+=exact
                exact_cases+=1
        assert observed==expected,(p,observed,expected)
        assert len(slopes(p))==(p+1)//2

    graph_checks=0
    for p in [5,7]:
        good=[]
        allowed=slopes(p)
        for vals in product(range(p),repeat=p):
            okay=all(((vals[j]-vals[i])*pow(j-i,-1,p))%p in allowed for i in range(p) for j in range(i+1,p))
            if okay:
                good.append(vals)
                assert len({(vals[j]-vals[0])*pow(j,-1,p)%p for j in range(1,p)})==1
            graph_checks+=1
        assert len(good)==p*len(allowed),(p,len(good))

    # Independent exact Fourier-orthogonality proof-of-concept for sample complete spectra.
    sample_spectra=0
    for p in [5,7,11]:
        n=p*p; chosen=sorted(slopes(p))
        for slope in chosen:
            for b in [0,1]:
                frequencies=[]
                for residue in range(p):
                    redv=(slope*residue+b)%p
                    lift=(2*residue+1)%p
                    orient=1 if (p%3==2 and residue%2==1) else 0
                    if orient==0:
                        frequencies.extend((residue+p*j,redv+p*lift) for j in range(p))
                    else:
                        frequencies.extend((residue+p*lift,redv+p*j) for j in range(p))
                assert len(frequencies)==n and len(set(frequencies))==n
                for i in range(n):
                    for j in range(i+1,n):
                        u=(frequencies[i][0]-frequencies[j][0])%n
                        v=(frequencies[i][1]-frequencies[j][1])%n
                        assert predict_zero(u,v,p),(p,slope,b,i,j)
                sample_spectra+=1
    print('VERIFY_OK prime_cases=%d exact_cyclotomic_mod_p2_cases=%d graph_functions=%d constructed_spectra=%d zero_formula=PASS residue_direction_rigidity=PASS' % (prime_cases,exact_cases,graph_checks,sample_spectra))


if __name__=='__main__':verify()
