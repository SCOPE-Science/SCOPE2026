"""Exact complete Pappus graph edge-boundary and nested-layout enumeration.

Run: python verify_lcf.py  (Python 3.8+, standard library only).
"""
N=18
OFFSETS=(5,7,-7,7,-7,-5)*3
PROFILE=(0,3,4,5,6,7,6,7,8,7,8,7,6,7,6,5,4,3,0)
COUNTS=(1,18,27,54,126,324,18,108,540,54,540,108,18,324,126,54,27,18,1)
TARGET=31850496

def edges():
    a={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    for i,d in enumerate(OFFSETS):
        a.add(tuple(sorted((i,(i+d)%N))))
    return sorted(a)

def verify():
    ee=edges()
    assert len(ee)==27
    adjacency=[0]*N
    for u,v in ee:
        adjacency[u]|=1<<v
        adjacency[v]|=1<<u
    assert all(row.bit_count()==3 for row in adjacency)
    full=1<<N
    boundary=[0]*full
    size=[0]*full
    minima=[99]*(N+1)
    multiplicities=[0]*(N+1)
    for m in range(full):
        if m:
            x=m&-m
            v=x.bit_length()-1
            p=m^x
            size[m]=size[p]+1
            boundary[m]=boundary[p]+3-2*(adjacency[v]&p).bit_count()
        k=size[m]
        if boundary[m]<minima[k]:
            minima[k]=boundary[m]
            multiplicities[k]=1
        elif boundary[m]==minima[k]:
            multiplicities[k]+=1
    assert minima==list(PROFILE), (minima,PROFILE)
    assert multiplicities==list(COUNTS), (multiplicities, COUNTS)
    # Count all chains of edge-isoperimetric minimizers; these are
    # exactly the optimal minimum-linear-arrangement vertex orders.
    chains=[0]*full
    chains[0]=1
    for m in range(1,full):
        if boundary[m]!=PROFILE[size[m]]:
            continue
        sub=m
        while sub:
            bit=sub&-sub
            sub^=bit
            chains[m]+=chains[m^bit]
    assert chains[-1]==TARGET,chains[-1]
    # All initial Hamiltonian-cycle prefixes saturate boundary minima.
    for k in range(N+1):
        assert boundary[(1<<k)-1]==PROFILE[k]
    assert sum(PROFILE)==99 and max(PROFILE)==8
    print('LCF_EXHAUSTIVE_PROFILE_PASS',len(ee),full,minima,multiplicities)
    print('NESTED_ORDER_CERTIFICATE_PASS',TARGET,'min_linear_arrangement=99','cutwidth=8')

if __name__=='__main__':
    verify()
