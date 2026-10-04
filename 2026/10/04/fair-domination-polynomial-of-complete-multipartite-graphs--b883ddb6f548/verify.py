#!/usr/bin/env python3
from math import comb

def profiles(max_order=9):
    out=[]
    def rec(rem, lo, cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for v in range(lo, rem+1):
            rec(rem-v, v, cur+[v])
    for n in range(2, max_order+1):
        rec(n, 1, [])
    return out

def part_counts(ns, mask):
    out=[]
    off=0
    for n in ns:
        out.append(sum((mask >> (off+j)) & 1 for j in range(n)))
        off += n
    return out

def literal_fair(ns, mask):
    N=sum(ns)
    full=(1 << N)-1
    if mask==full:
        return True
    if mask==0:
        return False
    d=mask.bit_count()
    counts=part_counts(ns, mask)
    outside=[]
    for i,n in enumerate(ns):
        if counts[i] < n:
            outside.extend([d-counts[i]] * (n-counts[i]))
    return bool(outside) and outside[0] > 0 and all(v==outside[0] for v in outside)

def criterion(ns, mask):
    N=sum(ns)
    full=(1 << N)-1
    if mask==full:
        return True
    if mask==0:
        return False
    counts=part_counts(ns, mask)
    nonfull=[counts[i] for i,n in enumerate(ns) if counts[i] < n]
    if not nonfull or len(set(nonfull)) != 1:
        return False
    t=nonfull[0]
    return sum(counts)-t > 0

def poly_formula(ns):
    N=sum(ns)
    L=max(ns)
    coeff=[0]*(N+1)
    for t in range(L):
        cur=[0]*(N+1)
        cur[0]=1
        for n in ns:
            if n <= t:
                factors=[(n,1)]
            else:
                factors=[(n,1),(t,comb(n,t))]
            nxt=[0]*(N+1)
            for a,ca in enumerate(cur):
                if ca:
                    for b,cb in factors:
                        nxt[a+b] += ca*cb
            cur=nxt
        coeff=[a+b for a,b in zip(coeff,cur)]
    coeff[N] -= L-1
    coeff[0] -= 1
    return coeff

def main():
    ps=profiles(9)
    subset_checks=0
    fair_sets=0
    coefficient_checks=0
    minimum_checks=0
    for ns in ps:
        N=sum(ns)
        brute=[0]*(N+1)
        for mask in range(1 << N):
            a=literal_fair(ns, mask)
            b=criterion(ns, mask)
            assert a==b, (ns,mask,a,b)
            if a:
                brute[mask.bit_count()] += 1
                fair_sets += 1
            subset_checks += 1
        formula=poly_formula(ns)
        assert brute==formula, (ns,brute,formula)
        coefficient_checks += N+1
        fd=next(i for i,c in enumerate(brute) if c)
        assert fd==min(len(ns),min(ns)), (ns,fd)
        minimum_checks += 1
    print(f"VERIFY_OK profiles={len(ps)} subset_checks={subset_checks} fair_sets={fair_sets} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=9")

if __name__=='__main__':
    main()
