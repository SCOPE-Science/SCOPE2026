from itertools import combinations
from math import comb


def parts(n, lo=1):
    if n==0:
        yield ()
        return
    for a in range(lo,n+1):
        for rest in parts(n-a,a):
            yield (a,)+rest


def vertices(profile):
    part=[]
    for i,n in enumerate(profile): part += [i]*n
    return part


def literal(profile,k,mask):
    part=vertices(profile); N=len(part)
    S=[(mask>>v)&1 for v in range(N)]
    for v in range(N):
        i=part[v]
        ns=sum(S[u] for u in range(N) if part[u]!=i)
        if ns<k: return False
        if not S[v]:
            nc=sum(1-S[u] for u in range(N) if part[u]!=i)
            if nc<k: return False
    return True


def criterion(profile,k,mask):
    part=vertices(profile); N=len(part)
    s=sum((mask>>v)&1 for v in range(N))
    si=[0]*len(profile)
    for v,i in enumerate(part): si[i]+= (mask>>v)&1
    for i,n in enumerate(profile):
        if s-si[i] < k: return False
        if si[i] < n and (N-s)-(n-si[i]) < k: return False
    return True


def formula_counts(profile,k):
    N=sum(profile)
    out=[0]*(N+1)
    for s in range(N+1):
        # multiply polynomials in y, only exponent needed
        poly=[1]+[0]*N
        for n in profile:
            allowed=[]
            lo=max(0, s+n-N+k)
            hi=min(n-1, s-k)
            if lo<=hi:
                allowed.extend(range(lo,hi+1))
            if n<=s-k:
                allowed.append(n)
            q=[0]*(N+1)
            for j in allowed:
                q[j]=comb(n,j)
            r=[0]*(N+1)
            for a,ca in enumerate(poly):
                if not ca: continue
                for b,cb in enumerate(q):
                    if cb and a+b<=N: r[a+b]+=ca*cb
            poly=r
        out[s]=poly[s]
    return out

profiles=0; parameter_checks=0; subset_checks=0; valid_sets=0; coefficient_checks=0; minimum_checks=0
for N in range(2,10):
    for p in parts(N):
        if len(p)<2: continue
        profiles+=1
        delta=N-max(p)
        for k in range(1,delta+1):
            parameter_checks+=1
            brute=[0]*(N+1)
            for mask in range(1<<N):
                subset_checks+=1
                a=literal(p,k,mask)
                b=criterion(p,k,mask)
                if a!=b:
                    raise SystemExit(f'criterion mismatch p={p} k={k} mask={mask} literal={a} criterion={b}')
                if a:
                    valid_sets+=1
                    brute[mask.bit_count()]+=1
            form=formula_counts(p,k)
            if brute!=form:
                raise SystemExit(f'coefficient mismatch p={p} k={k}\nbrute={brute}\nform={form}')
            coefficient_checks += N+1
            # gamma from least nonzero coefficient agrees with brute minimum
            bm=next((i for i,c in enumerate(brute) if c),None)
            fm=next((i for i,c in enumerate(form) if c),None)
            if bm!=fm: raise SystemExit('minimum mismatch')
            minimum_checks+=1
print(f'VERIFY_OK profiles={profiles} parameter_checks={parameter_checks} subset_checks={subset_checks} valid_sets={valid_sets} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=9')
