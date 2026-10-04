from itertools import combinations
from math import comb

MAX_ORDER=10


def profiles(total, minimum=1):
    # nondecreasing compositions, at least 2 parts
    def rec(rem, lo, cur):
        if rem==0:
            if len(cur)>=2:
                yield tuple(cur)
            return
        for x in range(lo, rem+1):
            cur.append(x)
            yield from rec(rem-x, x, cur)
            cur.pop()
    yield from rec(total, minimum, [])


def build(parts):
    cls=[]
    for i,n in enumerate(parts): cls += [i]*n
    N=len(cls)
    adj=[[False]*N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if u!=v and cls[u]!=cls[v]: adj[u][v]=True
    return cls,adj


def literal(mask, parts, cls, adj):
    N=len(cls)
    S=[v for v in range(N) if mask>>v&1]
    Sin=set(S)
    for v in range(N):
        if v not in Sin and sum(adj[v][u] for u in S)<2:
            return False
    Nset={v for u in S for v in range(N) if adj[u][v]}
    for v in Nset:
        if not any(adj[v][u] for u in Nset):
            return False
    return True


def criterion(mask, parts, cls):
    N=len(cls); r=len(parts)
    s=mask.bit_count()
    if s<2: return False
    ss=[0]*r
    for v in range(N):
        if mask>>v&1: ss[cls[v]]+=1
    if any(ss[i]<parts[i] and s-ss[i]<2 for i in range(r)):
        return False
    if r==2 and sum(x>0 for x in ss)<2:
        return False
    return True


def formula_coeff(parts, s):
    dp=[0]*(s+1); dp[0]=1
    for n in parts:
        nd=[0]*(s+1)
        opts=[]
        lim=min(n-1,s-2)
        if lim>=0:
            opts += [(j,comb(n,j)) for j in range(lim+1)]
        if n<=s: opts.append((n,1))
        for a,ca in enumerate(dp):
            if not ca: continue
            for j,cj in opts:
                if a+j<=s: nd[a+j]+=ca*cj
        dp=nd
    ans=dp[s]
    if len(parts)==2:
        ans -= sum(1 for n in parts if n==s)
    return ans


def gamma_formula(parts):
    N=sum(parts); r=len(parts); m=min(parts)
    if r==2:
        if m==1: return N
        if m==2: return 3
        return 4
    if any(n==2 for n in parts) or sum(n==1 for n in parts)>=2:
        return 2
    return 3

pcount=subsets=critchecks=coeffchecks=gchecks=valid=0
for N in range(2,MAX_ORDER+1):
  for parts in profiles(N):
    pcount+=1
    cls,adj=build(parts)
    brute=[0]*(N+1)
    for mask in range(1<<N):
        subsets+=1
        a=literal(mask,parts,cls,adj)
        b=criterion(mask,parts,cls)
        critchecks+=1
        if a!=b:
            raise SystemExit(f'criterion mismatch parts={parts} mask={mask} literal={a} criterion={b}')
        if a:
            brute[mask.bit_count()]+=1; valid+=1
    for s in range(2,N+1):
        f=formula_coeff(parts,s); coeffchecks+=1
        if f!=brute[s]:
            raise SystemExit(f'coeff mismatch parts={parts} s={s} formula={f} brute={brute[s]}')
    g=min(i for i,c in enumerate(brute) if c)
    gf=gamma_formula(parts); gchecks+=1
    if g!=gf:
        raise SystemExit(f'gamma mismatch parts={parts} brute={g} formula={gf}')
print(f'VERIFY_OK profiles={pcount} subset_checks={subsets} criterion_checks={critchecks} valid_sets={valid} coefficient_checks={coeffchecks} gamma_checks={gchecks} max_order={MAX_ORDER}')
