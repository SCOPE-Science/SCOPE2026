"""Independent finite checks for crown-graph forts and forcing (stdlib only)."""
from itertools import combinations
from math import comb, floor
from functools import lru_cache

def crown_adj(n):
    return [sum(1 << (n+j) for j in range(n) if i != j) for i in range(n)] + [sum(1 << i for i in range(n) if i != j) for j in range(n)]

def is_fort(mask, adj):
    if mask == 0:
        return False
    return all(((nbr & mask).bit_count() != 1) for i,nbr in enumerate(adj) if not (mask>>i)&1)

def predicted_forts(n):
    def mask_a(s): return sum(1 << i for i in s)
    def mask_b(s): return sum(1 << (n+i) for i in s)
    ans=set()
    for tri in combinations(range(n),3):
        ans.add(mask_a(tri));ans.add(mask_b(tri))
    for pair in combinations(range(n),2):
        ans.add(mask_a(pair)|mask_b(pair))
    return ans

def actual_min_forts(n):
    adj=crown_adj(n)
    k=2*n; total=1<<k
    forts=bytearray(total)
    proper=bytearray(total)
    output=set()
    for mask in range(1,total):
        forts[mask]=is_fort(mask,adj)
        # Every nonempty proper subset of mask appears inside an immediate deletion.
        v=mask
        while v:
            lsb=v&-v; v-=lsb
            sub=mask^lsb
            if forts[sub] or proper[sub]:
                proper[mask]=1;break
        if forts[mask] and not proper[mask]: output.add(mask)
    return output

def will_force(blue,adj):
    n=len(adj); full=(1<<n)-1
    while True:
        progressed=False
        for i in range(n):
            if (blue>>i)&1:
                white_n=adj[i] & (~blue & full)
                if white_n and white_n.bit_count()==1:
                    blue|=white_n;progressed=True;break
        if not progressed: return blue==full

def min_zero_sets(n):
    adj=crown_adj(n)
    target=2*n-4
    expected=set()
    for aa in combinations(range(n),2):
        for bb in combinations(range(n),2):
            if aa!=bb:
                white=sum(1<<i for i in aa)+sum(1<<(n+j) for j in bb)
                expected.add(((1<<(2*n))-1)^white)
    # Every smaller initial set has an all-left or all-right 3-white fort.
    by_size=[0]*(2*n+1)
    predicted_by_size=[0]*(2*n+1)
    for a in range(3):
        for b in range(3):
            predicted_by_size[2*n-a-b]+=comb(n,a)*comb(n,b)
    predicted_by_size[2*n-4]-=comb(n,2)
    for mask in range(1<<(2*n)):
        result=will_force(mask,adj)
        if result: by_size[mask.bit_count()]+=1
        if mask.bit_count()<target:
            assert not result, (n,mask,'unexpected smaller zero forcing set')
        elif mask.bit_count()==target:
            assert result==(mask in expected),(n,mask,'min-set mismatch')
    assert len(expected)==comb(n,2)*(comb(n,2)-1)
    assert by_size==predicted_by_size,(n,by_size,predicted_by_size)
    return len(expected)

def fort_packing(n):
    forts=tuple(sorted(actual_min_forts(n)))
    at=[[] for _ in range(2*n)]
    for f in forts:
        for i in range(2*n):
            if (f>>i)&1:at[i].append(f)
    @lru_cache(None)
    def recurse(mask):
        if not mask:return 0
        first=mask&-mask
        i=first.bit_length()-1
        best=recurse(mask^first)
        for f in at[i]:
            if f&mask==f:
                best=max(best,1+recurse(mask^f))
        return best
    return recurse((1<<(2*n))-1)


def test():
    for n in range(3,9):
        actual=actual_min_forts(n); pred=predicted_forts(n)
        assert actual==pred,(n,len(actual),len(pred),actual^pred)
        assert len(actual)==2*comb(n,3)+comb(n,2)
        print('FULL_SUBSET_MINIMALITY_OK',n,len(actual))
    for n in range(3,8):
        print('DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK',n,min_zero_sets(n))
    for n in range(3,8):
        v=fort_packing(n)
        assert v==2*n//3,(n,v)
        print('EXACT_FORT_PACKING_DP_OK',n,v)
    try:
        import scipy.optimize as so
        for n in range(3,8):
            patterns=predicted_forts(n)
            matrix=[[int((p>>i)&1)*-1 for i in range(2*n)] for p in patterns]
            result=so.linprog([1]*(2*n),A_ub=matrix,b_ub=[-1]*len(matrix),bounds=(0,None),method='highs')
            assert result.success
            assert abs(result.fun-2*n/3)<1e-7
            print('INDEPENDENT_FRACTIONAL_LP_OK',n,round(result.fun,8))
    except ImportError:
        print('LP_SOLVER_UNAVAILABLE_EXACT_AVERAGING_PROOF_SUPPLIES_VALUE')
    print('VERIFY_OK')

if __name__=='__main__': test()
