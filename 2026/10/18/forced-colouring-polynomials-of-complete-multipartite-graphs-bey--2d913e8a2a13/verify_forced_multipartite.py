#!/usr/bin/env python3
"""Reproducible finite checks for forced-colouring enumerator of multipartite graphs.
Only the mathematical forcing rule, not an external published result, is encoded.
"""
import itertools, math


def stirling(n,k):
    if not 0 <= k <= n: return 0
    row=[0]*(k+1);row[0]=1
    for _ in range(n):
        new=[0]*(k+1)
        for j in range(1,k+1):new[j]=j*row[j]+row[j-1]
        row=new
    return row[k]


def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r


def A(n):
    return [0]+[math.comb(n,j) for j in range(1,n+1)]


def theory(sizes,lam):
    N=sum(sizes);r=len(sizes)
    coeff=[0]*(N+1)
    for t in itertools.product(*(range(1,min(n,lam)+1) for n in sizes)):
        if sum(t)>lam:continue
        fac=math.factorial(lam)//math.factorial(lam-sum(t))
        for n,ti in zip(sizes,t):fac*=stirling(n,ti)
        if fac==0:continue
        if sum(t)<=lam:
            coeff[N]+=fac
        if sum(t)!=lam:continue
        M=[i for i in range(r) if t[i]==1]
        if not M:continue
        # subtract one all-seeded coloring per full colouring
        coeff[N]-=fac
        baseline=[1]
        for i in M:baseline=mul(baseline,A(sizes[i]))
        subtotal=baseline
        for i in M:
            z=[1]
            for j in M:
                if j!=i:z=mul(z,A(sizes[j]))
            # polynomial add
            if len(subtotal)<len(z):subtotal += [0]*(len(z)-len(subtotal))
            for j,v in enumerate(z):subtotal[j]+=v
        pref=[0]*sum(sizes[i] for i in range(r) if t[i]>=2)
        for j,v in enumerate(subtotal):coeff[len(pref)+j]+=fac*v
    return coeff


def brute(sizes,lam):
    N=sum(sizes);part=[i for i,n in enumerate(sizes) for _ in range(n)]
    neigh=[[w for w in range(N) if part[w]!=part[v]] for v in range(N)]
    counts=[0]*(N+1)
    for partial in itertools.product(range(-1,lam), repeat=N):
        c=list(partial)
        if any(c[v]>=0 and c[w]>=0 and c[v]==c[w] for v in range(N) for w in neigh[v]):
            continue
        for _ in range(N):
            changed=False
            for v in range(N):
                if c[v]!=-1:continue
                colors={c[w] for w in neigh[v] if c[w]>=0}
                if len(colors)==lam-1:
                    missing=list(set(range(lam))-colors)
                    if len(missing)!=1:raise AssertionError('bad forced color')
                    c[v]=missing[0];changed=True
                    break
            if not changed:break
        if -1 not in c and all(c[v]!=c[w] for v in range(N) for w in neigh[v]):
            counts[N-partial.count(-1)]+=1
    return counts


def lower_bound_seed(sizes,lam):
    N=sum(sizes);r=len(sizes);k=lam-r
    if k<0:return None
    if k==0:return r-1
    best=N
    for mask in range(1<<r):
        H=[i for i in range(r) if mask>>i&1]
        if len(H)==r:continue
        cap=sum(sizes[i]-1 for i in H)
        if len(H)<=k<=cap:
            best=min(best,r-1+cap)
    return best


def run():
    profiles = [(1,1),(1,2),(1,3),(2,2),(2,3),(1,1,1),(1,1,2),(1,2,2),(2,2,2),(1,1,1,2),(1,1,2,2),(1,2,3),(2,2,3),(1,1,1,1),(1,2,2,2)]
    checked=0; nonzero=0
    for sizes in profiles:
        N=sum(sizes)
        for lam in range(len(sizes), min(N+2,7)):
            if (lam+1)**N>350000:continue
            theory_co=theory(sizes,lam)
            brute_co=brute(sizes,lam)
            if theory_co!=brute_co:
                raise AssertionError((sizes,lam,theory_co,brute_co))
            computed=min((j for j,n in enumerate(brute_co) if n),default=None)
            expected=lower_bound_seed(sizes,lam)
            if computed!=expected:raise AssertionError(('min seed',sizes,lam,computed,expected))
            checked+=1
            nonzero+=sum(brute_co)
    print('VERIFICATION_OK', 'profiles=',len(profiles),'parameter_cases=',checked,'admissible_seed_assignments=',nonzero)
    for s,l in [((2,3),3),((2,3),4),((1,2,3),4),((2,2,3),4),((1,1,2,2),5)]:
        print('example',s,l, theory(s,l), 'minseed=',lower_bound_seed(s,l))
if __name__=='__main__':run()
