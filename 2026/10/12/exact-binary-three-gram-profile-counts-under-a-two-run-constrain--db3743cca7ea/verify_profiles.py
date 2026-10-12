#!/usr/bin/env python3
"""Exact, standard-library verification of the binary 3-gram profile formula.

Run: python3 verify_profiles.py
This program does not replace the all-length mathematical proof in RESULT.md.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

EDGES = ('001','010','011','100','101','110')
VERTICES = ('00','01','10','11')
POLY = (1,6,8,5,4,2)

def expected(M):
    """Coefficients of P/[(1-z^2)(1-z^3)(1-z^4)]."""
    v=[0]*(M+1)
    for i,p in enumerate(POLY):
        if i<=M:v[i]+=p
    for period in (2,3,4):
        for k in range(period,M+1):v[k]+=v[k-period]
    return v

def all_paths(M):
    """Independent DP: enumerate every possible edge-multiplicity profile of paths."""
    paths={(v,(0,)*6) for v in VERTICES}
    out=[{prof for v,prof in paths}]
    for m in range(1,M+1):
        nxt=set()
        for vertex,prof in paths:
            for i,e in enumerate(EDGES):
                if e[:2]!=vertex:continue
                new=list(prof);new[i]+=1
                nxt.add((e[-2:],tuple(new)))
        paths=nxt
        out.append({prof for v,prof in paths})
    return out

def all_balance(M):
    """Parametrization by possible start/end imbalance, independent of DP."""
    result=[]
    for m in range(M+1):
        seen=set()
        for s in VERTICES:
            for t in VERTICES:
                delta=[int(v==s)-int(v==t) for v in VERTICES]
                for a in range(m+1):
                    for c in range(m+1):
                        v=m-a-3*c+delta[0]+delta[1]-delta[3]
                        if v<0 or v%2:continue
                        b=v//2;d=a-delta[0];e=b+c-a-delta[1];f=c+delta[3]
                        if min(b,d,e,f)>=0:
                            profile=(a,b,c,d,e,f)
                            if sum(profile)==m:seen.add(profile)
        result.append(seen)
    return result

def direct_words(max_m):
    """A third implementation: enumerate actual constrained binary strings."""
    out=[]
    for m in range(max_m+1):
        st=set()
        for bits in product('01',repeat=m+2):
            w=''.join(bits)
            if '000' in w or '111' in w:continue
            ct=Counter(w[i:i+3] for i in range(m))
            st.add(tuple(ct[e] for e in EDGES))
        out.append(st)
    return out

def main():
    M=72
    pred=expected(M)
    walks=all_paths(M)
    assert [len(x) for x in walks]==pred, 'generating-function coefficients versus direct path DP'
    gamma24=(24,77,56,9,56,77,24,41,56,45,56,41)
    assert pred==[(13*m*m+54*m+gamma24[m%12])//24 for m in range(M+1)], 'period-twelve polynomial'
    assert all((13*m*m+54*m+gamma24[m%12])%24==0 for m in range(M+1))
    bal=all_balance(40)
    assert bal==walks[:41], 'degree balance parametrization versus edge-walk DP'
    brute=direct_words(15)
    assert brute==walks[:16], 'literal words versus graph paths'
    print('VERIFY_OK', 'max_m',M, 'direct_strings_through_n',17,
          'balance_through_m',40,'first_16',pred[:16],
          'at_m72',pred[72])
if __name__=='__main__':main()
