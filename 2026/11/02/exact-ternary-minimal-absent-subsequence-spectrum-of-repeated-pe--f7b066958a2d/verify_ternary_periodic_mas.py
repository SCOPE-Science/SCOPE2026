#!/usr/bin/env python3
"""Reproducible combinatorial checks for minimal absent subsequences of (012)^m.
Requires only Python's standard library. Finite checks are not proofs of the infinite identities.
"""
from collections import defaultdict, Counter
from itertools import product

def is_subsequence(target, host):
    it = iter(host)
    return all(any(c == want for c in it) for want in target)

def descent_count(word):
    return sum(a >= b for a,b in zip(word, word[1:]))

def local_mas(word, m):
    if len(word) < 2 or descent_count(word) != m:
        return False
    if word[0] < word[1] or word[-2] < word[-1]:
        return False
    return all((a >= b) + (b >= c) - (a >= c) == 1
               for a,b,c in zip(word,word[1:],word[2:]))

def direct_mas(word, host):
    return (not is_subsequence(word,host) and
            all(is_subsequence(word[:i]+word[i+1:],host)
                for i in range(len(word))))

def brute(q,m):
    host=tuple(range(q))*m
    profile=Counter()
    tested=0
    for length in range(1, min(q*m+1,2*m)+1):
        for word in product(range(q), repeat=length):
            left=local_mas(word,m)
            right=direct_mas(word,host)
            assert left==right,(q,m,word,left,right)
            tested+=1
            if left:profile[length]+=1
    return tested, dict(sorted(profile.items()))

def transfer_profile(q,K):
    """Coefficients of the exact finite-state transfer expression."""
    states=defaultdict(int)
    for a in range(q):
        for b in range(q):
            if a>=b:states[(1,2,a,b)]+=1
    out=defaultdict(int)
    for length in range(2,2*K+1):
        nextstates=defaultdict(int)
        for (k,l,a,b),multiplicity in states.items():
            if l!=length:continue
            if b<=a and k<=K:
                out[(k,l)]+=multiplicity
            if l==2*K: continue
            for c in range(q):
                if (int(a>=b)+int(b>=c)-int(a>=c))!=1:continue
                nk=k+int(b>=c)
                if nk<=K: nextstates[(nk,l+1,b,c)]+=multiplicity
        states=nextstates
    return out

# D(t,z) F(t,z)=N(t,z), with t marking host repetitions and z length.
DEN={(0,0):1,(1,1):-3,(2,2):3,(2,3):-1,
     (3,3):-1,(3,4):-3,(4,5):3,(4,6):-1,
     (5,7):-3,(6,9):1}
NUM={(1,2):6,(2,3):-8,(2,4):6,(3,4):3,
     (3,5):6,(3,6):1,(4,6):-9,(4,7):6,
     (5,8):9,(5,9):-1,(6,10):-3}

def rational_check(profile,K):
    tested=0
    for k in range(K+1):
        for l in range(2*K+1):
            product_coefficient=sum(d*profile.get((k-dk,l-dl),0)
                      for (dk,dl),d in DEN.items())
            assert product_coefficient==NUM.get((k,l),0),(k,l,product_coefficient,NUM.get((k,l),0))
            tested+=1
    return tested

def main():
    direct_cases=0;direct_targets=0;total_mas=0
    for q,lo,hi in ((2,1,7),(3,1,5)):
        for m in range(lo,hi+1):
            target_count, profile=brute(q,m)
            d=transfer_profile(q,m)
            assert profile=={l:n for (k,l),n in d.items() if k==m}
            direct_cases+=1;direct_targets+=target_count;total_mas+=sum(profile.values())
    # Matrix enumeration (q=3) versus polynomial identity to larger orders.
    K=22
    table=transfer_profile(3,K)
    identities=rational_check(table,K)
    expected={1:6,2:16,3:46,4:127,5:349,6:960,7:2640,8:7264}
    for k,v in expected.items():
        assert sum(n for (i,l),n in table.items() if i==k)==v,(k,v)
    print('VERIFY_OK direct_parameter_cases=%s literal_targets=%s tested_MAS=%s '%(direct_cases,direct_targets,total_mas)+
          'rational_coefficients=%s ternary_prefix=%s'%(identities,','.join(map(str,expected.values()))))

# The exact rational identity can also be checked independently of enumeration:
# for polynomials D,N and vector P from ternary_mas_algebra_certificate.json,
# check (I-M)P=D w and vP=N as identities in Z[t,z].
def verify_polynomial_certificate(path=None):
    import json
    from pathlib import Path
    if path is None:
        path=Path(__file__).with_name('ternary_mas_algebra_certificate.json')
    c=json.loads(Path(path).read_text(encoding='utf-8'))
    states=[tuple(x) for x in c['state_order']]
    assert states==[(a,b) for a in range(3) for b in range(3)]
    def unpack(xs):return {(a,b):n for a,b,n in xs if n}
    def plus(A,B):
        v=dict(A)
        for xy,n in B.items():v[xy]=v.get(xy,0)+n
        return {xy:n for xy,n in v.items() if n}
    def scale(A,n):return {xy:n*v for xy,v in A.items() if n*v}
    def shift(A,k,l):return {(x+k,y+l):n for (x,y),n in A.items()}
    D=unpack(c['denominator_terms']);N=unpack(c['numerator_terms'])
    P=[unpack(xs) for xs in c['adjugate_vector_terms']]
    for i,(a,b) in enumerate(states):
        v=P[i]
        for cc in range(3):
            if int(a>=b)+int(b>=cc)-int(a>=cc)!=1: continue
            j=states.index((b,cc))
            v=plus(v,scale(shift(P[j],int(b>=cc),1),-1))
        assert v==(D if a>=b else {}),(a,b,'matrix_identity')
    numerator={}
    for i,(a,b) in enumerate(states):
        if a>=b:numerator=plus(numerator,shift(P[i],1,2))
    assert numerator==N,'numerator_identity'
    return len(P), sum(len(x) for x in P)

if __name__=="__main__":
    main()
    states, terms=verify_polynomial_certificate()
    print("ALGEBRA_CERT_OK states=%d polynomial_terms=%d"%(states,terms))
