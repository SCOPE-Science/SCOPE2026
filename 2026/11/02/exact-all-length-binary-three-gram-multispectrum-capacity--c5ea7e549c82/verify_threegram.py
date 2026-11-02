#!/usr/bin/env python3
"""Exact rational three-gram multispectrum enumerator, using Euler trails and geometric sums."""
from collections import defaultdict

TAIL=(0,0,1,1,2,2,3,3)
HEAD=(0,1,2,3,0,1,2,3)

def connected(mask):
    par=list(range(4)); active=set()
    def root(x):
        while par[x]!=x:x=par[x]
        return x
    for i in range(8):
        if mask>>i&1:
            a,b=TAIL[i],HEAD[i];active.update((a,b));par[root(a)]=root(b)
    return bool(active) and len({root(x) for x in active})==1

def conditions(seq):
    lb=0; fixed=None
    for mode,v in seq:
        if mode=='eq':
            if fixed is not None and fixed!=v:return None
            fixed=v
        else:lb=max(lb,v)
    if fixed is not None:return ('eq',fixed) if fixed>=lb else None
    return ('ge',lb)

def allowed(s,x):return x==s[1] if s[0]=='eq' else x>=s[1]

def ae_terms(A,E,T,wa,we):
    # list of (multiplier, exponent, denominator factor degrees)
    factors=tuple(w for w,v in ((wa,A),(we,E)) if v[0]=='ge')
    result=[(1,wa*A[1]+we*E[1],factors)]
    for a in range(max(0,T)):
        if allowed(A,a):
            for e in range(max(0,T-a)):
                if allowed(E,e):result.append((-1,wa*a+we*e,()))
    return result

def shift(terms,sign=1,exponent=0,extra=()):
    return [(sign*k,j+exponent,d+extra) for k,j,d in terms]

def formula(mask,d):
    A=conditions((('ge',0),('ge',1) if mask&2 else ('eq',0),('ge',d[0]+1) if mask&16 else ('eq',d[0])))
    C=conditions((('ge',0),('ge',1) if mask&8 else ('eq',0),('ge',1-d[3]) if mask&64 else ('eq',-d[3])))
    E=conditions((('ge',0),('ge',1) if mask&32 else ('eq',0)))
    if None in (A,C,E):return []
    offset=d[1]-d[0]+d[3]
    if mask&4:
        K=d[1]-1
        if C[0]=='eq':out=shift(ae_terms(A,E,C[1]-K,3,2),exponent=offset+C[1])
        else:
            T=C[1]-K
            out=shift(ae_terms(A,E,T,3,2),exponent=offset+C[1],extra=(1,))
            out+=shift(ae_terms(A,E,T,4,3),sign=-1,exponent=offset+K+1,extra=(1,))
    else:
        if C[0]=='eq':
            k=C[1]-d[1]
            out=[(1,3*a+2*(k-a)+offset+C[1],()) for a in range(max(0,k+1)) if allowed(A,a) and allowed(E,k-a)]
        else:out=shift(ae_terms(A,E,C[1]-d[1],4,3),exponent=offset+d[1])
    loops=(bool(mask&1)+bool(mask&128))
    return shift(out,exponent=loops,extra=(1,)*loops)

def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:o[i+j]+=v*w
    return o

def divide_exact(p,d):
    # Divide integer polynomials with constant term 1, exact power-series recurrence
    n=len(p)-len(d)+1
    assert n>0
    q=[0]*n
    for i in range(n):
        q[i]=p[i]-sum(d[j]*q[i-j] for j in range(1,min(i,len(d)-1)+1))
    assert mul(q,d)==p
    return q

def generating_function():
    den=[1]
    for p in (1,1,1,2,3,4):den=mul(den,[1]+[0]*(p-1)+[-1])
    cache={}
    numerator=defaultdict(int)
    support_count=0;term_count=0
    for mask in range(1,256):
        if not connected(mask):continue
        support_has=False
        for src in range(-1,4):
            for dst in ([-1] if src==-1 else [i for i in range(4) if i!=src]):
                delta=[0,0,0,0]
                if src>=0:delta[src]=1;delta[dst]=-1
                ts=formula(mask,delta)
                for k,exp,factors in ts:
                    ff=tuple(sorted(factors))
                    if ff not in cache:
                        div=[1]
                        for p in ff:div=mul(div,[1]+[0]*(p-1)+[-1])
                        cache[ff]=divide_exact(den,div)
                    for j,v in enumerate(cache[ff]):
                        if v:numerator[exp+j]+=k*v
                    term_count+=1;support_has=True
        support_count+=bool(support_has)
    assert all(v==0 for k,v in numerator.items() if k<0),[(k,v) for k,v in numerator.items() if k<0]
    high=max(k for k,v in numerator.items() if v)
    num=[numerator[i] for i in range(high+1)]
    print('supports',support_count,'formal terms',term_count)
    print('num_common',num,'den_common',den)
    # cancel one factor 1-z^2 to match simple reduced form
    while True:
        try:
            num2=divide_exact(num,[1,0,-1]);den2=divide_exact(den,[1,0,-1]);num,den=num2,den2
        except (AssertionError,IndexError):break
    print('num_reduced',num,'den_reduced',den)
    return num,den

def count_all_binary_words(n):
    profiles=set()
    for code in range(1<<n):
        cnt=[0]*8
        for i in range(n-2):
            e=((code>>i)&1)*4+((code>>(i+1))&1)*2+((code>>(i+2))&1)
            cnt[e]+=1
        profiles.add(tuple(cnt))
    return len(profiles)

if __name__=='__main__':
    numerator,denominator=generating_function()
    expected_num=[0,8,-9,7,-3,6,5,-1,2,-5,3]
    expected_den=[1,-3,3,-2,2,0,-2,2,-3,3,-1]
    assert numerator==expected_num,(numerator,expected_num)
    assert denominator==expected_den,(denominator,expected_den)
    counts=[]
    for m in range(100):
        counts.append((numerator[m] if m<len(numerator) else 0)-sum(denominator[j]*counts[m-j] for j in range(1,min(m,len(denominator)-1)+1)))
    for n in range(3,15):
        b=count_all_binary_words(n)
        assert b==counts[n-2],(n,b,counts[n-2])
    print('EXACT_RATIONAL_IDENTITY_OK')
    print('BRUTE_FORCE_BINARY_WORDS_N_3_TO_14_OK')
    print('COUNTS_LENGTHS_3_TO_20',[(n,counts[n-2]) for n in range(3,21)])
