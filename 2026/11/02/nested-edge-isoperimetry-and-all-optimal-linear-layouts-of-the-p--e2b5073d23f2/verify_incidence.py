"""Independent incidence-model validation by direct edge-cut counting.

Run: python verify_incidence.py (Python 3.8+, standard library only).
"""
N=18
TRIPLES=((0,1,2),(3,4,5),(6,7,8),(0,4,6),(3,1,6),
         (0,5,7),(3,2,7),(1,5,8),(4,2,8))
# Maps 18-cycle LCF vertex number to point/line incidence number.
ISO=(0,9,2,17,4,12,6,13,1,16,8,11,7,15,3,10,5,14)
PROFILE=(0,3,4,5,6,7,6,7,8,7,8,7,6,7,6,5,4,3,0)
COUNTS=(1,18,27,54,126,324,18,108,540,54,540,108,18,324,126,54,27,18,1)
TARGET=31850496

def verify():
    edges=sorted((v,9+j) for j,trip in enumerate(TRIPLES) for v in trip)
    assert len(edges)==27 and len(set(edges))==27
    assert sorted(ISO)==list(range(N))
    lcf={(min(i,(i+1)%N),max(i,(i+1)%N)) for i in range(N)}
    for i,d in enumerate((5,7,-7,7,-7,-5)*3):
        j=(i+d)%N
        lcf.add((min(i,j),max(i,j)))
    transform={tuple(sorted((ISO[u],ISO[v]))) for u,v in lcf}
    assert transform==set(edges)
    sz=[0]*(1<<N)
    b=[0]*(1<<N)
    mins=[99]*(N+1)
    counts=[0]*(N+1)
    # This implementation deliberately does NOT use the incremental
    # boundary recurrence: count crossing edges directly for each set.
    for mask in range(1<<N):
        k=mask.bit_count()
        bd=sum(((mask>>u)^(mask>>v))&1 for u,v in edges)
        sz[mask]=k
        b[mask]=bd
        if bd<mins[k]:mins[k]=bd;counts[k]=1
        elif bd==mins[k]:counts[k]+=1
    assert mins==list(PROFILE)
    assert counts==list(COUNTS)
    prefix=0
    cutseq=[0]
    for u in ISO:
        prefix|=1<<u
        cutseq.append(b[prefix])
    assert cutseq==list(PROFILE)
    # Alternative forward DP: extend only through minimizing subsets.
    paths=[0]*(1<<N)
    paths[0]=1
    for mask in range(1<<N):
        if not paths[mask]:continue
        assert b[mask]==mins[sz[mask]]
        available=((1<<N)-1)^mask
        while available:
            bit=available&-available
            available^=bit
            after=mask|bit
            if b[after]==mins[sz[after]]:paths[after]+=paths[mask]
    assert paths[-1]==TARGET
    assert sum(cutseq)==99 and max(cutseq)==8
    print('INCIDENCE_DIRECT_CUT_EXHAUSTIVE_PASS', len(edges),2**N,mins,counts)
    print('INDEPENDENT_LAYOUT_AND_COUNT_PASS',TARGET,'minimum_linear_arrangement=99','cutwidth=8')

if __name__=='__main__':
    verify()
