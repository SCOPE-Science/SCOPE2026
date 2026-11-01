#!/usr/bin/env python3
"""Exact GF(2) rank and first-entry counts for GP(n,3); no third-party modules."""

def neighbors(n):
    if n < 7: raise ValueError('need n >=7')
    ns=[set() for _ in range(2*n)]
    def edge(u,v):
        ns[u].add(v);ns[v].add(u)
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,i+n)
        edge(i+n,((i+3)%n)+n)
    assert all(len(x)==3 for x in ns)
    return ns

def step(state,mask):
    z=0
    for i,m in enumerate(mask):
        if (state&m).bit_count() & 1: z |= 1<<i
    return z

def rank(vectors):
    pivot={}
    for x in vectors:
        while x:
            b=x.bit_length()-1
            if b not in pivot:
                pivot[b]=x
                break
            x^=pivot[b]
    return len(pivot)

def test(n,verbose=False):
    ns=neighbors(n)
    mask=[sum(1<<j for j in x) for x in ns]
    size=2*n
    current=[1<<j for j in range(size)]
    e=n&-n
    val=e if n%5==0 else 0
    limit=(val+1)//2 if val else 0
    ranks=[]
    for t in range(0,max(3,limit+2)):
        rk=rank(current)
        ranks.append(rk)
        expected=size - 4*min(2*t,val) if val else size
        assert rk == expected,(n,t,rk,expected)
        current=[step(y,mask) for y in current]
    identity_shift=[(1<<i)^mask[i] for i in range(size)]
    fix_dim=size-rank(identity_shift)
    want_fix=min(4,n & -n)+(4 if n%5==0 else 0)
    assert fix_dim==want_fix,(n,fix_dim,want_fix)
    if verbose:
        print('n=',n,'v2n_factor=',e,'nil_e=',val,'ranks=',ranks,
              'periodic=',f'2^{size-4*val}', 'T=',limit,'fixed=',f'2^{fix_dim}')
    return ranks

if __name__ == '__main__':
    for n in range(7,121):
        test(n,n in [7,8,9,10,15,20,25,30,40,50,60,80,100,120])
    print('RANK_PROFILE_OK all n 7..120')
