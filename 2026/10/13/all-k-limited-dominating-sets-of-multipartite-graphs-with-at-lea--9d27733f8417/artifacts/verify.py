from itertools import product
from math import comb

def profiles(total):
    out = []
    def rec(rem, last, cur):
        if rem == 0:
            if len(cur) >= 3:
                out.append(tuple(cur))
            return
        for x in range(last, rem + 1):
            cur.append(x)
            rec(rem - x, x, cur)
            cur.pop()
    rec(total, 1, [])
    return out

def graph(profile):
    part_of = []
    for i,n in enumerate(profile):
        part_of += [i]*n
    N=len(part_of)
    adj=[0]*N
    for u in range(N):
        for v in range(N):
            if u != v and part_of[u] != part_of[v]:
                adj[u] |= 1 << v
    return part_of, adj

def dominates(adj, mask):
    full=(1<<len(adj))-1
    covered=mask
    for v in range(len(adj)):
        if (mask>>v)&1:
            covered |= adj[v]
    return covered==full

def direct(profile,k,mask):
    part_of,adj=graph(profile)
    if mask==0 or not dominates(adj,mask):
        return False
    N=len(part_of)
    outside=((1<<N)-1)^mask
    for v in range(N):
        if (mask>>v)&1:
            if (adj[v] & outside).bit_count() > k:
                return False
    return True

def occupancies(profile,mask):
    vals=[]
    start=0
    for n in profile:
        d=0
        for v in range(start,start+n):
            d += (mask>>v)&1
        vals.append(d)
        start+=n
    return vals

def structural(profile,k,mask):
    ds=occupancies(profile,mask)
    S=[i for i,d in enumerate(ds) if d>0]
    N=sum(profile)
    if len(S)==1:
        i=S[0]
        return ds[i]==profile[i] and N-profile[i] <= k
    if len(S)<2:
        return False
    os=[n-d for n,d in zip(profile,ds)]
    q=sum(os)
    return all(q-os[i] <= k for i in S)

def polynomial_formula(profile,k):
    N=sum(profile); r=len(profile)
    coeff=[0]*(N+1)

    # support size one
    for i,n in enumerate(profile):
        if N-n <= k:
            coeff[n] += 1

    # support S of size at least two
    for bits in range(1<<r):
        S=[i for i in range(r) if (bits>>i)&1]
        if len(S)<2:
            continue
        B=sum(profile[j] for j in range(r) if j not in S)
        for ys in product(*[range(profile[i]) for i in S]):
            # y_i is the number omitted from occupied part i, so 0..n_i-1
            if any(B + sum(ys[h] for h in range(len(S)) if h != a) > k
                   for a in range(len(S))):
                continue
            dsize=N-B-sum(ys)
            ways=1
            for a,i in enumerate(S):
                ways *= comb(profile[i], ys[a])
            coeff[dsize] += ways
    return coeff

def support_gamma_formula(profile,k):
    N=sum(profile); r=len(profile)
    candidates=[]

    for i,n in enumerate(profile):
        if N-n <= k:
            candidates.append(n)

    for bits in range(1<<r):
        S=[i for i in range(r) if (bits>>i)&1]
        s=len(S)
        if s<2:
            continue
        B=sum(profile[j] for j in range(r) if j not in S)
        if B>k:
            continue
        K=k-B
        caps=[profile[i]-1 for i in S]
        C=sum(caps)
        cmin=min(caps)
        Y=min(C, K+cmin, (s*K)//(s-1))
        candidates.append(N-B-Y)

    return min(candidates)

profiles_checked=0
subset_checks=0
parameter_cases=0

for N in range(3,10):
    for profile in profiles(N):
        profiles_checked += 1
        Delta=N-min(profile)
        for k in range(1,Delta):
            parameter_cases += 1
            direct_coeff=[0]*(N+1)
            best=N+1
            for mask in range(1<<N):
                subset_checks += 1
                a=direct(profile,k,mask)
                b=structural(profile,k,mask)
                if a != b:
                    raise AssertionError(("structural",profile,k,mask,a,b,occupancies(profile,mask)))
                if a:
                    s=mask.bit_count()
                    direct_coeff[s]+=1
                    best=min(best,s)
            form=polynomial_formula(profile,k)
            if direct_coeff != form:
                raise AssertionError(("polynomial",profile,k,direct_coeff,form))
            gf=support_gamma_formula(profile,k)
            if best != gf:
                raise AssertionError(("gamma",profile,k,best,gf,direct_coeff))

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles_checked}; "
    f"parameter_cases={parameter_cases}; "
    f"subset_checks={subset_checks}; "
    "orders=3..9"
)
