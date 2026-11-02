#!/usr/bin/env python3
"""Finite checks of a two-noun cardinality-syllogistic small-model theorem.
No claim of exhaustive verification beyond the stated finite ranges.
"""
from itertools import product
from collections import defaultdict

def sgn(x): return (x>0)-(x<0)

def profile(a,b,c,d):
    # Support controls all universal and existential statements on literals.
    # For the cardinality comparisons, preserve pairwise weak order.
    u,v=a-d,b-c
    return (tuple(int(z>0) for z in (a,b,c,d)),
            tuple(sgn(t) for t in (u,v,u+v,u-v)))

def profile_minimal(a,b,c,d):
    u,v=a-d,b-c
    if not u and not v: U,V=0,0
    elif not u: U,V=0,sgn(v)
    elif not v: U,V=sgn(u),0
    elif abs(u)==abs(v): U,V=sgn(u),sgn(v)
    elif abs(u)>abs(v): U,V=2*sgn(u),sgn(v)
    else: U,V=sgn(u),2*sgn(v)
    assert (sgn(U),sgn(V),sgn(U+V),sgn(U-V))==tuple(sgn(t) for t in (u,v,u+v,u-v))
    def pair(s,t,diff):
        if s>0 and t>0:
            return (1+max(diff,0),1+max(-diff,0))
        if s>0:
            assert diff>0
            return diff,0
        if t>0:
            assert diff<0
            return 0,-diff
        assert diff==0
        return 0,0
    A,D=pair(a,d,U)
    B,C=pair(b,c,V)
    return A,B,C,D


def check_raw_sentences(N=10):
    # Compare the derived normal form against the literal truth table of
    # every one of the 4*4*4 syntactically allowed atomic sentences.
    masks=((1,1,0,0),(0,0,1,1),(1,0,1,0),(0,1,0,1))
    by_profile={}
    by_signature={}
    for n in range(1,N+1):
        for a in range(n+1):
            for b in range(n-a+1):
                for c in range(n-a-b+1):
                    d=n-a-b-c
                    cells=(a,b,c,d)
                    literal_sizes=tuple(sum(w*t for w,t in zip(mask,cells)) for mask in masks)
                    signature=[]
                    for i,x in enumerate(masks):
                        for j,y in enumerate(masks):
                            intersection=sum(k*t for k,t in zip((s & t for s,t in zip(x,y)),cells))
                            x_not_y=sum(k*t for k,t in zip((s & (1-t) for s,t in zip(x,y)),cells))
                            signature.extend((x_not_y==0,intersection>0,literal_sizes[i]>=literal_sizes[j],literal_sizes[i]>literal_sizes[j]))
                    signature=tuple(signature)
                    pr=profile(*cells)
                    if pr in by_profile: assert by_profile[pr]==signature
                    else: by_profile[pr]=signature
                    if signature in by_signature: assert by_signature[signature]==pr
                    else: by_signature[signature]=pr
    assert len(by_profile)==len(by_signature)==67
    return len(by_profile)

def check_minimal_profiles(N=30):
    first={}
    cnt=0
    for n in range(1,N+1):
        for a in range(n+1):
            for b in range(n-a+1):
                for c in range(n-a-b+1):
                    d=n-a-b-c
                    c4=(a,b,c,d)
                    p=profile(*c4)
                    small=profile_minimal(*c4)
                    assert profile(*small)==p, (c4,small)
                    assert 1 <= sum(small) <= 7, (c4,small)
                    if p not in first: first[p]=(n,c4)
                    cnt += 1
    assert max(n for n,_ in first.values()) == 7
    return len(first),cnt

def basic(a,b,c,d):
    return (a,b,c,d)
def pgtq(a,b,c,d): return b>c
def qgtqbar(a,b,c,d): return a+c>b+d
def pgtnotp(a,b,c,d): return a+b>c+d
def qgtnotp(a,b,c,d): return a>d
def peqnotp(a,b,c,d): return a+b==c+d
def all_four(a,b,c,d): return all(z>0 for z in (a,b,c,d))
def three(a,b,c,d): return a>0 and b>0 and c>0
def two(a,b,c,d): return a>0 and b>0
def vac(a,b,c,d): return True

def check_spectra(N=28):
    target={
        'T1': lambda a,b,c,d: vac(a,b,c,d),
        'T2': lambda a,b,c,d: two(a,b,c,d),
        'T3': lambda a,b,c,d: three(a,b,c,d),
        'T4': lambda a,b,c,d: all_four(a,b,c,d),
        'T5': lambda a,b,c,d: all_four(a,b,c,d) and pgtnotp(a,b,c,d),
        'T6': lambda a,b,c,d: all_four(a,b,c,d) and pgtq(a,b,c,d) and qgtnotp(a,b,c,d),
        'T7': lambda a,b,c,d: all_four(a,b,c,d) and pgtq(a,b,c,d) and qgtqbar(a,b,c,d),
        'E2': lambda a,b,c,d: peqnotp(a,b,c,d),
        'E4': lambda a,b,c,d: all_four(a,b,c,d) and peqnotp(a,b,c,d),
        'E6': lambda a,b,c,d: all_four(a,b,c,d) and peqnotp(a,b,c,d) and pgtq(a,b,c,d),
    }
    for n in range(1,N+1):
        vals=[]
        for a in range(n+1):
            for b in range(n-a+1):
                for c in range(n-a-b+1):
                    vals.append((a,b,c,n-a-b-c))
        for name,pred in target.items():
            expect=(n>=int(name[1:]) and (name[0]=='T' or n%2==0))
            got=any(pred(*v) for v in vals)
            assert got==expect,(n,name,got,expect)
    return target.keys()

if __name__=='__main__':
    assert check_raw_sentences()==67
    k,num=check_minimal_profiles()
    assert k>0
    names=check_spectra()
    print('ALL_CHECKS_OK')
    print('all 64 raw sentence truth values matched normal form through size 10')
    print('distinct complete two-noun sentence truth profiles:',k)
    print('total 4-cell profiles checked:',num)
    print('witness spectra:',','.join(names))
