#!/usr/bin/env python3
from itertools import combinations
from math import comb

MAX_ORDER = 9

def compositions(n, r):
    if r == 1:
        if n >= 1:
            yield (n,)
        return
    for first in range(1, n-r+2):
        for tail in compositions(n-first, r-1):
            yield (first,) + tail

def parts(ns):
    out=[]; k=0
    for n in ns:
        out.append(list(range(k,k+n)))
        k += n
    return out

def literal_liar(ns, mask):
    ps=parts(ns); N=sum(ns)
    pidx=[None]*N
    psets=[]
    for i,P in enumerate(ps):
        Pset=set(P); psets.append(Pset)
        for v in P: pidx[v]=i
    S={v for v in range(N) if (mask>>v)&1}
    V=set(range(N))
    def closed(v):
        return (V-psets[pidx[v]]) | {v}
    for v in range(N):
        if len(closed(v) & S) < 2:
            return False
    for u in range(N):
        Nu=closed(u)
        for v in range(u+1,N):
            if len((Nu | closed(v)) & S) < 3:
                return False
    return True

def capacity_liar(ns, mask):
    ps=parts(ns); s=mask.bit_count()
    if s < 3:
        return False
    for n,P in zip(ns,ps):
        si=sum((mask>>v)&1 for v in P)
        cap=n if n < s else s-3
        if si > cap:
            return False
    return True

def predicted_coeffs(ns):
    N=sum(ns); coeff=[0]*(N+1)
    for s in range(3,N+1):
        dp=[0]*(s+1); dp[0]=1
        for n in ns:
            cap=n if n < s else s-3
            nd=[0]*(s+1)
            for a,val in enumerate(dp):
                if not val: continue
                for j in range(0,min(cap,n,s-a)+1):
                    nd[a+j] += val*comb(n,j)
            dp=nd
        coeff[s]=dp[s]
    return coeff

def predicted_gamma(ns):
    N=sum(ns)
    for s in range(3,N+1):
        if sum(n if n < s else s-3 for n in ns) >= s:
            return s
    raise AssertionError('no feasible size')

def main():
    profiles=subset_checks=coefficient_checks=gamma_checks=0
    for N in range(3,MAX_ORDER+1):
        for r in range(2,N+1):
            for ns in compositions(N,r):
                profiles += 1
                actual=[0]*(N+1)
                for mask in range(1<<N):
                    a=literal_liar(ns,mask)
                    b=capacity_liar(ns,mask)
                    subset_checks += 1
                    if a != b:
                        raise AssertionError(('criterion mismatch',ns,mask,a,b))
                    if a:
                        actual[mask.bit_count()] += 1
                pred=predicted_coeffs(ns)
                for s in range(N+1):
                    coefficient_checks += 1
                    if actual[s] != pred[s]:
                        raise AssertionError(('coefficient mismatch',ns,s,actual[s],pred[s]))
                g=min(s for s,c in enumerate(actual) if c)
                pg=predicted_gamma(ns)
                gamma_checks += 1
                if g != pg:
                    raise AssertionError(('gamma mismatch',ns,g,pg))
    print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} coefficient_checks={coefficient_checks} gamma_checks={gamma_checks} max_order={MAX_ORDER}')

if __name__ == '__main__':
    main()
