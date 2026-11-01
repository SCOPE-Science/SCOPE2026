#!/usr/bin/env python3
"""Independent finite checks for heterogeneous self-inclusion in XOR networks.

The update is recomputed directly from all pairwise neighbor contributions,
not from the determinant or Jordan formulas used in the proof.
"""
from collections import Counter
from itertools import product


def update_binary(x, a, b):
    n=a+b
    bits=[(x>>i)&1 for i in range(n)]
    out=0
    for i in range(n):
        t=0
        for j in range(n):
            if (i!=j) or (i>=a):
                t ^= bits[j]
        out |= t<<i
    return out


def update_field(x,a,b,q):
    n=a+b
    out=[0]*n
    for i in range(n):
        for j in range(n):
            if i!=j or i>=a:
                out[i] ^= x[j]  # addition over fields of characteristic 2
    return tuple(out)


def ranks(B):
    B=list(B);n=len(B);z=0
    for i in range(n):
        p=next((k for k in range(z,n) if (B[k]>>i)&1),None)
        if p is None: continue
        B[z],B[p]=B[p],B[z]
        for k in range(n):
            if k!=z and (B[k]>>i)&1:
                B[k]^=B[z]
        z+=1
    return z


def apply(B,x):
    ans=0
    for i,row in enumerate(B):
        if (row & x).bit_count()%2:ans|=1<<i
    return ans


def mat_mult(B,C):
    n=len(B)
    cols=[sum(((C[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
    return [sum((((B[i]&cols[j]).bit_count()%2)<<j) for j in range(n)) for i in range(n)]


def mat_add(B,C):return [b^c for b,c in zip(B,C)]


def form(a,b):
    c=a%2;d=b%2
    if (c,d)==(1,1):return {'zero':[1]*(b-1),'one':[1]*(a-1),'irreducible':[2],'order':3}
    if (c,d)==(1,0):return {'zero':[3]+[1]*(b-2),'one':[1]*(a-1),'irreducible':[],'order':1}
    if (c,d)==(0,1):return {'zero':[1]*(b-1),'one':[3]+[1]*(a-2),'irreducible':[],'order':4}
    return {'zero':[2]+[1]*(b-2),'one':[2]+[1]*(a-2),'irreducible':[],'order':2}


def expected(a,b,q):
    f=form(a,b)
    zero=f['zero']; invdim=sum(f['one'])+sum(f['irreducible'])
    entry=[q**(invdim+sum(min(t,j) for j in zero)) for t in range(4)]
    fixed={}
    if a%2 and b%2:
        fixed={1:q**(a-1),2:q**(a-1),3:q**(a+1),4:q**(a-1)}
    elif a%2 and not b%2:
        fixed={1:q**(a-1),2:q**(a-1),3:q**(a-1),4:q**(a-1)}
    elif not a%2 and b%2:
        fixed={1:q**(a-1),2:q**a,3:q**(a-1),4:q**(a+1)}
    else:
        fixed={1:q**(a-1),2:q**a,3:q**(a-1),4:q**a}
    cycles=Counter({1:fixed[1]})
    for d in (2,3,4):
        if d==2:cycles[d]=(fixed[2]-fixed[1])//2
        if d==3:cycles[d]=(fixed[3]-fixed[1])//3
        if d==4:cycles[d]=(fixed[4]-fixed[2])//4
    return f,entry, fixed, cycles


def cycle_data(F,x):
    seen={};states=[];y=x
    while y not in seen:
        seen[y]=len(states);states.append(y);y=F(y)
        if len(states)>100000:raise AssertionError('unanticipated long orbit')
    return seen[y],len(states)-seen[y]


def main():
    matrix_cases=0
    assertions=0
    for a,b in product(range(2,15),repeat=2):
        n=a+b
        B=[sum((1 if (i!=j or i>=a) else 0)<<j for j in range(n)) for i in range(n)]
        Id=[1<<i for i in range(n)]
        f,entry,fixed,cycles=expected(a,b,2)
        zero=f['zero'];one=f['one'];other=f['irreducible']
        assert sum(zero)+sum(one)+sum(other)==n
        # Nonzero eigenparts are invertible; rank-power deficits come only from zero Jordan blocks.
        P=Id
        for t in range(5):
            target=n-sum(min(t,j) for j in zero)
            assert ranks(P)==target,(a,b,t,'zero kernel')
            assertions+=1;P=mat_mult(P,B)
        # Same invariant-block computation for the eigenvalue 1.
        Q=Id; C=mat_add(B,Id)
        for t in range(5):
            target=n-sum(min(t,j) for j in one)
            assert ranks(Q)==target,(a,b,t,'one kernel')
            assertions+=1;Q=mat_mult(Q,C)
        # Fitting projection: no transient remains after max(zero); this is actual matrix equality.
        t=max(zero)
        P=Id
        for _ in range(t):P=mat_mult(P,B)
        P2=P
        for _ in range(f['order']):P2=mat_mult(P2,B)
        assert P2==P,(a,b,'stabilized cycle power')
        assertions+=1;matrix_cases+=1
    exhaustive_states=0;binary_cases=0
    for a,b in product(range(2,7),repeat=2):
        n=a+b
        if n>11:continue
        f,entry,fixed,cycles=expected(a,b,2)
        T=Counter();orbits=Counter();labelled=Counter();vis=set()
        F=lambda x:update_binary(x,a,b)
        for x in range(1<<n):
            pre,per=cycle_data(F,x)
            T[pre]+=1
            labelled[per]+=int(pre==0)
            if pre==0 and x not in vis:
                z=x;states=[]
                while z not in vis:
                    vis.add(z);states.append(z);z=F(z)
                assert z==x
                orbits[len(states)]+=1
            exhaustive_states+=1
        for t in range(4):
            assert sum(T[s] for s in range(t+1))==entry[t],(a,b,t,'entry')
            assertions+=1
        for d in (1,2,3,4):
            assert orbits[d]==cycles[d],(a,b,d,'orbits')
            assert sum(k*orbits[k] for k in (1,2,3,4) if d%k==0)==fixed[d],(a,b,d,'fixed')
            assertions+=2
        assert sum(T.values())==1<<n
        assertions+=1;binary_cases+=1
    quartic_states=0;quartic_cases=0
    for a,b in product(range(2,5),repeat=2):
        n=a+b
        if n>7:continue
        q=4
        f,entry,fixed,cycles=expected(a,b,q)
        F=lambda x:update_field(x,a,b,q)
        T=Counter();orbits=Counter();vis=set()
        for x in product(range(q),repeat=n):
            pre,per=cycle_data(F,x)
            T[pre]+=1
            if pre==0 and x not in vis:
                y=x
                while y not in vis:
                    vis.add(y);y=F(y)
                assert y==x
                orbits[per]+=1
            quartic_states+=1
        for t in range(4):
            assert sum(T[s] for s in range(t+1))==entry[t]
            assertions+=1
        for d in (1,2,3,4):
            assert orbits[d]==cycles[d],(a,b,d,'GF4 cycles')
            assertions+=1
        quartic_cases+=1
    print('HETEROGENEOUS_COMPLETE_XOR_VERIFY_OK',
          'matrix_pairs=',matrix_cases,'binary_pairs=',binary_cases,
          'binary_states=',exhaustive_states,'GF4_pairs=',quartic_cases,
          'GF4_states=',quartic_states,'assertions=',assertions)

if __name__=='__main__':main()
