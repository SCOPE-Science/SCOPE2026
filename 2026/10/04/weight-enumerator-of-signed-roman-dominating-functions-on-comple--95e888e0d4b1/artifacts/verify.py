from itertools import product
from collections import Counter
from math import factorial

MAX_ORDER=9

def partitions(n, lo=1):
    if n==0:
        yield ()
        return
    for x in range(lo,n+1):
        for rest in partitions(n-x,x):
            yield (x,)+rest

def offsets(parts):
    out=[]; a=0
    for n in parts:
        out.append(range(a,a+n)); a+=n
    return out

def literal(parts, vals):
    inds=offsets(parts)
    N=sum(parts)
    W=sum(vals)
    for I in inds:
        sig=sum(vals[v] for v in I)
        outside=W-sig
        for v in I:
            if outside+vals[v] < 1:
                return False
            if vals[v]==-1:
                if not any(vals[u]==2 for J in inds if J is not I for u in J):
                    # `is not` works here because ranges are distinct objects, but avoid ambiguity below
                    pass
    # explicit Roman condition
    part_of=[]
    for i,I in enumerate(inds):
        for v in I: part_of.append(i)
    for v,x in enumerate(vals):
        if x==-1:
            i=part_of[v]
            if not any(vals[u]==2 and part_of[u]!=i for u in range(N)):
                return False
    return True

def criterion(parts, vals):
    inds=offsets(parts)
    W=sum(vals)
    C=sum(x==2 for x in vals)
    for I in inds:
        arr=[vals[v] for v in I]
        sig=sum(arr)
        mu=min(arr)
        a=sum(x==-1 for x in arr)
        c=sum(x==2 for x in arr)
        if W-sig+mu < 1:
            return False
        if a>0 and C-c < 1:
            return False
    return True

def multinom(n,a,b,c):
    return factorial(n)//(factorial(a)*factorial(b)*factorial(c))

def aggregate(parts):
    states=[]
    for n in parts:
        st=[]
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                sig=-a+b+2*c
                mu=-1 if a else (1 if b else 2)
                st.append((a,b,c,sig,mu,multinom(n,a,b,c)))
        states.append(st)
    ans=Counter()
    for combo in product(*states):
        W=sum(z[3] for z in combo); C=sum(z[2] for z in combo)
        ok=True; mult=1
        for a,b,c,sig,mu,m in combo:
            if W-sig+mu<1 or (a>0 and C-c<1):
                ok=False; break
            mult*=m
        if ok: ans[W]+=mult
    return ans

profiles=labelings=valid=criterion_checks=coefficient_checks=0
for N in range(2,MAX_ORDER+1):
    for parts in partitions(N):
        if len(parts)<2: continue
        profiles+=1
        brute=Counter()
        for vals in product((-1,1,2), repeat=N):
            labelings+=1
            a=literal(parts,vals)
            b=criterion(parts,vals)
            criterion_checks+=1
            if a!=b:
                raise AssertionError((parts,vals,a,b))
            if a:
                valid+=1; brute[sum(vals)]+=1
        agg=aggregate(parts)
        keys=set(brute)|set(agg)
        for w in keys:
            coefficient_checks+=1
            if brute[w]!=agg[w]:
                raise AssertionError((parts,w,brute[w],agg[w]))
print(f'VERIFY_OK profiles={profiles} labelings={labelings} valid_functions={valid} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} max_order={MAX_ORDER}')
