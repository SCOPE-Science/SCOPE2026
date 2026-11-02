"""Independent finite checks for acyclic orientations of K_{2,n}.

Use: python verify.py (Python >=3.10, standard library only).
"""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def rank(u,a,b):
    if u+a+b==0:return 0
    options=[]
    if u:options.append(1+min(rank(u-1,a+1,b),rank(u-1,a,b+1)))
    if a:options.append(1+min(rank(u,a-1,b),u+a-1))
    if b:options.append(1+min(rank(u,a,b-1),u+b-1))
    return max(options)

def closed(u,a,b):
    return max(u+a,u+b,(3*u+a+b+1)//2)

for u in range(30):
    for a in range(30):
        for b in range(30):
            assert rank(u,a,b)==closed(u,a,b),(u,a,b)
print('THREE_STATE_RANK_FORMULA_PASS',30**3)


def brute(n):
    # Two mixed local orientations cannot coexist across columns.
    columns=set()
    for mixed in (1,2):
        for t in product((0,3,mixed),repeat=n):
            state=sum(((v&1)<<(2*i))|(((v>>1)&1)<<(2*i+1)) for i,v in enumerate(t))
            columns.add(state)
    columns=sorted(columns)
    assert len(columns)==2*3**n-2**n
    tests=[sum(1<<i for i,c in enumerate(columns) if (c>>q)&1) for q in range(2*n)]
    allstates=(1<<len(columns))-1
    @lru_cache(None)
    def ld(S):
        if S.bit_count()==1:return 0
        best=0
        for test in tests:
            yes=S&test;no=S^yes
            if yes and no:
                if min(yes.bit_count(),no.bit_count())<1<<best:continue
                best=max(best,1+min(ld(yes),ld(no)))
        return best
    return len(columns),ld(allstates),ld.cache_info().currsize

out=[]
for n in range(1,8):
    size,d,states=brute(n)
    assert d==(3*n+1)//2
    out.append((n,size,d,states))
print('EXACT_BRUTE_LITTLESTONE_K2N_PASS',out)
print('ACyclic_BIPARTITE_ALL_CHECKS_PASS')
