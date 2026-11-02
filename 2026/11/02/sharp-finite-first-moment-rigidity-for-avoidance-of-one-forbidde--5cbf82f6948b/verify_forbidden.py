#!/usr/bin/env python3
"""Exact checks for the finite-jet rigidity of one-factor avoidance.
Uses only the Python standard library; all counts are integers.
"""
from collections import defaultdict
from itertools import product


def add(P,Q):
    R=P.copy()
    for k,v in Q.items(): R[k]=R.get(k,0)+v
    return {k:v for k,v in R.items() if v}


def shift(P,a):
    return {k+a:v for k,v in P.items()}


def scale(P,m):
    return {k:v*m for k,v in P.items() if v*m}


def direct_spectrum(pattern, q, mark, N):
    m=len(pattern); zero={0:1}; states=[{} for _ in range(m)]; states[0]=zero
    records=[]
    for n in range(N+1):
        tot={}
        for P in states: tot=add(tot,P)
        records.append(tot)
        nxt=[{} for _ in range(m)]
        for i,P in enumerate(states):
            if not P: continue
            for a in range(q):
                candidate=pattern[:i]+(a,)
                if candidate[-m:]==pattern: continue
                j=max(k for k in range(m) if k==0 or candidate[-k:]==pattern[:k])
                nxt[j]=add(nxt[j],shift(P,int(a==mark)))
        states=nxt
    return records


def correlation_terms(pattern,mark):
    m=len(pattern)
    terms={0:{0:1}}
    for d in range(1,m):
        if pattern[:m-d]==pattern[d:]:
            suffix=pattern[m-d:]
            terms[d]={sum(a==mark for a in suffix):1}
    return terms


def cluster_spectrum(pattern,q,mark,N):
    m=len(pattern); h=sum(a==mark for a in pattern)
    C=correlation_terms(pattern,mark)
    # Denominator D=(1-z(q-1+y))*C + z^m*y^h
    D={}
    for d,P in C.items():
        D[d]=add(D.get(d,{}),P)
        D[d+1]=add(D.get(d+1,{}),scale(P,-(q-1)))
        D[d+1]=add(D.get(d+1,{}),scale(shift(P,1),-1))
    D[m]=add(D.get(m,{}),{h:1})
    assert D[0]=={0:1}
    out=[]
    for n in range(N+1):
        P=C.get(n,{}).copy()
        for d,Q in D.items():
            if d==0 or d>n: continue
            for a,c in Q.items():
                P=add(P,scale(shift(out[n-d],a),-c))
        assert all(v>=0 for v in P.values())
        out.append(P)
    return out


def first_stats(hists):
    return tuple((sum(p.values()),sum(k*c for k,c in p.items())) for p in hists)


def main():
    total=0; cohorts=[]
    for q,mmax,N in [(2,8,19),(3,4,14)]:
        for m in range(1,mmax+1):
            mapping={}
            for pattern in product(range(q),repeat=m):
                a=direct_spectrum(pattern,q,1,N)
                b=cluster_spectrum(pattern,q,1,N)
                assert a==b,(q,pattern)
                key=first_stats(a)[:2*m]
                if key in mapping: assert mapping[key]==a,(q,m,pattern)
                else: mapping[key]=a
                total+=1
            cohorts.append((q,m,q**m,len(mapping)))
    print('all exact recurrence vs independent KMP DP comparisons PASS:',total)
    print('jet grouping, no false identification through tested N: PASS')
    print('cohorts: q,m,patterns,first-jet classes:',cohorts)
    for m in range(4,11):
        w=tuple(map(int,'011'+'0'*(m-3)))
        v=tuple(map(int,'1'+'0'*(m-2)+'1'))
        A=direct_spectrum(w,2,1,2*m+1)
        B=direct_spectrum(v,2,1,2*m+1)
        assert all(sum(x.values())==sum(y.values()) for x,y in zip(A,B))
        assert first_stats(A)[:2*m-1]==first_stats(B)[:2*m-1]
        assert first_stats(A)[2*m-1][1]-first_stats(B)[2*m-1][1]==1
        assert correlation_terms(w,1)=={0:{0:1},m-1:{2:1}}
        assert correlation_terms(v,1)=={0:{0:1},m-1:{1:1}}
        print('sharp m=',m,'first difference n=',2*m-1,'moment gap=+1')
    w=(0,1,1,0);v=(1,0,0,1)
    A=direct_spectrum(w,2,1,7)[7]
    B=direct_spectrum(v,2,1,7)[7]
    print('length seven spectra for 0110 / 1001:', sorted(A.items()), sorted(B.items()))
    # The single-forbidden-factor hypothesis is essential: two forbidden pairs.
    def several_forbidden_spectrum(forbidden,q,N):
        out=[]
        for n in range(N+1):
            spectrum={}
            for word in product(range(q),repeat=n):
                if any(word[i:i+len(p)]==p for p in forbidden for i in range(n-len(p)+1)):
                    continue
                t=sum(x==1 for x in word)
                spectrum[t]=spectrum.get(t,0)+1
            out.append(spectrum)
        return out
    X=several_forbidden_spectrum(((0,0),(1,1)),2,12)
    Y=several_forbidden_spectrum(((0,1),(1,0)),2,12)
    assert first_stats(X)==first_stats(Y)
    assert X[2]=={1:2} and Y[2]=={0:1,2:1}
    print('multiple-forbidden boundary: equal N and M through n=12; at n=2 spectra 2y versus 1+y^2: PASS')
    # Direct brute force is distinct from the suffix-automaton count and cluster recurrence.
    checks=0
    for q,mmax,nmax in [(2,5,9),(3,3,7)]:
        for m in range(1,mmax+1):
            for pattern in product(range(q),repeat=m):
                expected=direct_spectrum(pattern,q,1,nmax)
                for n in range(nmax+1):
                    brute={}
                    for word in product(range(q),repeat=n):
                        if any(word[i:i+m]==pattern for i in range(n-m+1)):
                            continue
                        k=sum(a==1 for a in word)
                        brute[k]=brute.get(k,0)+1
                    assert brute==expected[n]
                    checks+=1
    print('independent brute-force word-enumeration histograms PASS:',checks)
    print('ALL CHECKS PASSED')

if __name__=='__main__': main()
