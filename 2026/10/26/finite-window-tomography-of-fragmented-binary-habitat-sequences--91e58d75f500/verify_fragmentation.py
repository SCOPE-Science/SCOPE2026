#!/usr/bin/env python3
"""Exact finite-state checks for binary spatial patch-count tomography.
Only finite verification; general identities are proved separately.
"""
from fractions import Fraction as F
from itertools import product
import json


def probability(bits, t, a, b):
    w = t if bits[0] == 0 else 1-t
    for u,v in zip(bits, bits[1:]):
        w *= ((1-a) if v==0 else a) if u==0 else (b if v==0 else (1-b))
    return w


def run_count(bits):
    return sum(v == 1 and (i == 0 or bits[i-1] == 0)
               for i,v in enumerate(bits))


def law(n,t,a,b):
    ans=[F(0)]*(n//2+2)
    for bits in product((0,1),repeat=n):
        ans[run_count(bits)] += probability(bits,t,a,b)
    assert sum(ans)==1
    return ans


def pgf_matrix(n,t,a,b):
    # Polynomials represented by coefficient lists, with z marking each newly begun run.
    v0=[t]; v1=[F(0),1-t]
    for _ in range(n-1):
        next0=[F(0)]*max(len(v0),len(v1))
        for i,w in enumerate(v0): next0[i]+=(1-a)*w
        for i,w in enumerate(v1): next0[i]+=b*w
        next1=[F(0)]*(max(len(v0)+1,len(v1)))
        for i,w in enumerate(v0): next1[i+1]+=a*w
        for i,w in enumerate(v1): next1[i]+=(1-b)*w
        v0,v1=next0,next1
    out=[F(0)]*max(len(v0),len(v1))
    for i,w in enumerate(v0):out[i]+=w
    for i,w in enumerate(v1):out[i]+=w
    return out


def trim(v):
    while v and v[-1]==0:v=v[:-1]
    return v


def verify_all():
    sample_pairs=[(F(i,j),F(k,l)) for j in range(2,7) for i in range(1,j)
                  for l in range(2,7) for k in range(1,l)]
    chains=0; laws=0; patterns=0; stationed=0
    for a,b in sample_pairs:
        for t in (F(1,5),F(1,3),F(1,2),F(2,3),F(4,5), b/(a+b)):
            chains+=1
            x=law(3,t,a,b)[0]
            y=law(3,t,a,b)[2]
            z=law(4,t,a,b)[0]
            assert x==t*(1-a)**2
            assert z==t*(1-a)**3
            assert y==(1-t)*b*a
            assert x>z>0 and x**3<z**2
            assert y < (1-x**3/z**2)*(1-z/x)
            ta=x**3/z**2
            aa=1-z/x
            bb=y/((1-ta)*aa)
            assert (ta,aa,bb)==(t,a,b)
            assert (y*z*z==x*(x-z)**2)==(t*a==(1-t)*b)
            if t*a==(1-t)*b:
                stationed+=1
                # Rational square-roots are known from identities x=t(1-a)^2, y=t*a^2.
                u2=t*(1-a); v2=t*a # u2,v2 stand for sqrt(t)*sqrt(x),sqrt(t)*sqrt(y)
                assert x==(t*(1-a))**2/t
                assert y==(t*a)**2/t
                assert (t*(1-a)+t*a)==t
            for n in range(1,9):
                L=law(n,t,a,b)
                P=pgf_matrix(n,t,a,b)
                assert trim(L)==trim(P), (n,t,a,b,L,P)
                laws+=1
                patterns+=2**n
    # Two different stationary chains can share the two-site component-count law.
    w=F(1,4)
    t1=F(1,3); t2=F(2,5)
    q1=t1-w; q2=t2-w
    s1=(q1/t1,q1/(1-t1))
    s2=(q2/t2,q2/(1-t2))
    assert s1!=s2 and law(2,t1,*s1)==law(2,t2,*s2)
    # Examples for stationarity and nonstationarity.
    stationary=(F(2,3),F(1,4),F(1,2))
    arbitrary=(F(1,3),F(1,4),F(1,2))
    res={
        'status':'PASS',
        'exact_arithmetic':'fractions.Fraction, no floating point',
        'parameter_triples':chains,
        'stationary_parameter_triples':stationed,
        'sequence_length_range':[1,8],
        'exact_distribution_and_transfer_matrix_comparisons':laws,
        'pattern_probabilities_summed_across_distributions':patterns,
        'nonidentifiable_two_site_witness':{'zero_patch_probability':str(w),'first':list(map(str,(t1,*s1))),'second':list(map(str,(t2,*s2)))},
        'stationary_example':{'parameters':list(map(str,stationary)), 'R3':list(map(str,law(3,*stationary))), 'R4_zero':str(law(4,*stationary)[0])},
        'nonstationary_example':{'parameters':list(map(str,arbitrary)), 'R3':list(map(str,law(3,*arbitrary))), 'R4_zero':str(law(4,*arbitrary)[0])},
        'scope':'Finite exact checks only; they do not prove general identifiability, sufficiency or necessity.'
    }
    return res


if __name__=='__main__':
    print(json.dumps(verify_all(),sort_keys=True,indent=2))
