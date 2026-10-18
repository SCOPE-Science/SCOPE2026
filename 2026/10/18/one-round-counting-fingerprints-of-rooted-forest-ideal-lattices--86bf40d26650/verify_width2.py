#!/usr/bin/env python3
"""Standalone finite checks for one-round counting fingerprints of rooted-forest ideal lattices."""
from collections import Counter, defaultdict

def types(n):
    yield ('chain',n)
    for a in range(1,n//2+1):
        yield ('parallel',a,n-a)
    for s in range(1,n-1):
        for a in range(1,(n-s)//2+1):
            b=n-s-a
            if a<=b:
                yield ('fork',s,a,b)

def parents(t):
    kind=t[0]
    if kind=='chain':return [-1]+list(range(t[1]-1))
    if kind=='parallel':
        a,b=t[1:]
        return [-1]+list(range(a-1))+[-1]+list(range(a,a+b-1))
    s,a,b=t[1:]
    # stem of s nodes, then two separate chains hanging from its last node
    return [-1]+list(range(s-1))+[s-1]+list(range(s,s+a-1))+[s-1]+list(range(s+a,s+a+b-1))

def brute(t):
    par=parents(t);n=len(par)
    children=[[] for _ in par]
    for i,p in enumerate(par):
        if p>=0:children[p].append(i)
    f=Counter()
    for mask in range(1<<n):
        if any(p>=0 and ((mask>>i)&1) and not((mask>>p)&1) for i,p in enumerate(par)):continue
        lower=sum(bool((mask>>i)&1) and all(not((mask>>j)&1) for j in children[i]) for i in range(n))
        upper=sum(not((mask>>i)&1) and (p<0 or ((mask>>p)&1)) for i,p in enumerate(par))
        f[lower,upper]+=1
    return +f

def analytic(t):
    kind=t[0];f=Counter()
    if kind=='chain':
        f.update({(1,0):1,(0,1):1});f[1,1]+=t[1]-1
    elif kind=='parallel':
        a,b=t[1:]
        f.update({(2,0):1,(1,1):2,(0,2):1})
        f[2,1]+=a+b-2;f[1,2]+=a+b-2;f[2,2]+=(a-1)*(b-1)
    else:
        s,a,b=t[1:]
        f.update({(2,0):1,(0,1):1})
        f[1,1]+=s+1
        f[2,1]+=a+b-2;f[1,2]+=a+b-1;f[2,2]+=(a-1)*(b-1)
    return +f

def norm(f):return tuple(sorted((k,v) for k,v in f.items() if v))

def verification():
    checked=0;first_u=None;first_conn=None;all_pair_distinct=True
    for n in range(1,16):
        uni=defaultdict(list);pairs=defaultdict(list)
        for t in types(n):
            f=brute(t);ff=analytic(t)
            assert norm(f)==norm(ff),(n,t,norm(f),norm(ff))
            pairs[norm(f)].append(t)
            uni[norm(Counter({(0,b):sum(v for (a,c),v in f.items() if c==b) for b in {b for (a,b) in f}}))].append(t)
            checked+=1
        assert all(len(z)==1 for z in pairs.values()),(n,'paired collision')
        coll=[v for v in uni.values() if len(v)>1]
        if coll and first_u is None:first_u=(n,coll[0])
        for v in coll:
            cc=[x for x in v if x[0]=='fork']
            if len(cc)>1 and first_conn is None:first_conn=(n,cc)
        # exact univariate fibre formula
        formula=defaultdict(int)
        for a in range(1,n//2+1):formula[a*(n-a)]+=1
        for s in range(1,n-1):
            for a in range(1,(n-s)//2+1):
                b=n-s-a
                if a<=b: formula[a*b]+=1
        assert sorted(list(formula.values())+[1])==sorted(map(len,uni.values())),(n,formula,{k:len(v) for k,v in uni.items()})
        if n in (4,5,6,8,12,15):print('n',n,'types',sum(map(len,uni.values())),'1side_profiles',len(uni),'paired_profiles',len(pairs),'collision_groups',len(coll))
    assert first_u[0]==5,first_u
    assert first_conn[0]==6,first_conn
    print('first_all_collision',first_u)
    print('first_connected_collision',first_conn)
    print('verified_types',checked,'max_n',15)
    # Odd factor parameterization for s=1 cross-type collisions, all k,r <= 15.
    cases=0
    for k in range(1,16):
        for r in range(k,16):
            a=k*(r+1);b=r*(k+1);c=k*r;d=(k+1)*(r+1)
            n=a+b+1
            assert n==c+d
            assert (2*k+1)*(2*r+1)==2*n-1
            assert norm(analytic(('fork',1,a,b)))!=norm(analytic(('parallel',c,d)))
            Bu=lambda t:tuple(sorted((j,sum(v for (i,j2),v in analytic(t).items() if j2==j)) for j in {j for (i,j) in analytic(t)}))
            assert Bu(('fork',1,a,b))==Bu(('parallel',c,d))
            cases+=1
    print('odd_factor_pairs_checked',cases)
    print('VERIFY_OK')
if __name__=='__main__':verification()
