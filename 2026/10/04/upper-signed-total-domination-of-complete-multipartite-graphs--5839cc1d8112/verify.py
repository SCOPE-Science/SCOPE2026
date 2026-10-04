#!/usr/bin/env python3
from itertools import combinations

MAX_ORDER = 10
FULL_LOWER_ORDER = 7


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def vertex_parts(ns):
    out=[]
    for i,n in enumerate(ns): out += [i]*n
    return out


def is_stdf(bits, ns, vp):
    N=len(vp)
    vals=[1 if (bits>>v)&1 else -1 for v in range(N)]
    part_sum=[0]*len(ns)
    for v,x in enumerate(vals): part_sum[vp[v]] += x
    W=sum(vals)
    return all(W-part_sum[i] >= 1 for i in range(len(ns)))


def is_minimal_single(bits, ns, vp):
    if not is_stdf(bits,ns,vp): return False
    N=len(vp)
    for v in range(N):
        if (bits>>v)&1 and is_stdf(bits ^ (1<<v), ns, vp):
            return False
    return True


def is_minimal_full(bits, ns, vp):
    if not is_stdf(bits,ns,vp): return False
    sub=(bits-1)&bits
    while sub:
        if is_stdf(sub,ns,vp): return False
        sub=(sub-1)&bits
    if bits and is_stdf(0,ns,vp): return False
    return True


def structural(bits, ns, vp):
    N=len(vp); r=len(ns)
    vals=[1 if (bits>>v)&1 else -1 for v in range(N)]
    sigma=[0]*r; has_plus=[False]*r
    for v,x in enumerate(vals):
        sigma[vp[v]] += x
        if x==1: has_plus[vp[v]]=True
    W=sum(vals)
    eps=[1 if (N-n)%2 else 2 for n in ns]
    T=[W-sigma[i] for i in range(r)]
    if any(T[i] < eps[i] for i in range(r)): return False
    Q={i for i in range(r) if T[i]==eps[i]}
    return all(any(i!=j for i in Q) for j in range(r) if has_plus[j])


def formula(ns):
    N=sum(ns); eps=[1 if (N-n)%2 else 2 for n in ns]
    best=None
    for i,j in combinations(range(len(ns)),2):
        M=N-ns[i]-ns[j]
        b=min(ns[i]+eps[i], ns[j]+eps[j], M+eps[i]+eps[j])
        best=b if best is None or b>best else best
    return best

profiles=0
labelings=0
minimal=0
full_lower_checks=0
formula_checks=0
construction_targets=0
for N in range(2,MAX_ORDER+1):
    for ns in partitions(N):
        if len(ns)<2: continue
        profiles += 1
        vp=vertex_parts(ns)
        weights=[]
        tight_attained=set()
        for bits in range(1<<N):
            labelings += 1
            m1=is_minimal_single(bits,ns,vp)
            st=structural(bits,ns,vp)
            if m1 != st:
                raise AssertionError(("structural",ns,bits,m1,st))
            if N<=FULL_LOWER_ORDER and is_stdf(bits,ns,vp):
                mf=is_minimal_full(bits,ns,vp)
                full_lower_checks += 1
                if mf != m1:
                    raise AssertionError(("full-minimal",ns,bits,mf,m1))
            if m1:
                minimal += 1
                w=2*bits.bit_count()-N
                weights.append(w)
                vals=[1 if (bits>>v)&1 else -1 for v in range(N)]
                sig=[0]*len(ns)
                for v,x in enumerate(vals): sig[vp[v]] += x
                eps_now=[1 if (N-n)%2 else 2 for n in ns]
                Q=[i for i in range(len(ns)) if w-sig[i]==eps_now[i]]
                for a,b in combinations(Q,2):
                    tight_attained.add((a,b,w))
        brute=max(weights)
        pred=formula(ns)
        formula_checks += 1
        if brute != pred:
            raise AssertionError(("formula",ns,brute,pred))
        # For every pair, verify that its bottleneck target is attained by a minimal STDF.
        eps=[1 if (N-n)%2 else 2 for n in ns]
        minimal_weights=set(weights)
        for i,j in combinations(range(len(ns)),2):
            M=N-ns[i]-ns[j]
            target=min(ns[i]+eps[i],ns[j]+eps[j],M+eps[i]+eps[j])
            construction_targets += 1
            if (i,j,target) not in tight_attained:
                raise AssertionError(("pair-target",ns,i,j,target))
print(f"VERIFY_OK profiles={profiles} labelings={labelings} minimal_functions={minimal} full_lower_checks={full_lower_checks} formula_checks={formula_checks} pair_targets={construction_targets} max_order={MAX_ORDER}")
