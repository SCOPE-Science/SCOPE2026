from collections import Counter
from math import ceil, log2


def cycle_union(parts):
    n=sum(parts)
    A=[set() for _ in range(n)]
    off=0
    for m in parts:
        for i in range(m):
            u=off+i; v=off+(i+1)%m
            A[u].add(v); A[v].add(u)
        off+=m
    return A


def canonicalize_pair(mats):
    vals=[]
    for M in mats:
        for row in M: vals.extend(row)
    ids={s:i for i,s in enumerate(sorted(set(vals),key=repr))}
    return [[[ids[x] for x in row] for row in M] for M in mats]


def joint_wl_first_differences(parts_a,parts_b,max_rounds=10):
    Gs=[cycle_union(parts_a),cycle_union(parts_b)]
    init=[]
    for A in Gs:
        n=len(A); M=[[None]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                M[x][y]=(x==y, y in A[x])
        init.append(M)
    colors=canonicalize_pair(init)
    full_first=diag_first=None
    for r in range(max_rounds+1):
        h=[Counter(c for row in C for c in row) for C in colors]
        d=[Counter(C[i][i] for i in range(len(C))) for C in colors]
        if full_first is None and h[0]!=h[1]: full_first=r
        if diag_first is None and d[0]!=d[1]: diag_first=r
        if full_first is not None and diag_first is not None:
            return full_first,diag_first
        if r==max_rounds: break
        sigm=[]
        for gi,A in enumerate(Gs):
            n=len(A); old=colors[gi]; M=[[None]*n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    mult=Counter((old[z][y],old[x][z]) for z in range(n))
                    M[x][y]=(old[x][y],tuple(sorted(mult.items())))
            sigm.append(M)
        colors=canonicalize_pair(sigm)
    return full_first,diag_first


def partitions(n,last=3):
    if n==0:
        yield ()
        return
    for a in range(last,n+1):
        rem=n-a
        if rem==0:
            yield (a,)
        elif rem>=a:
            for q in partitions(rem,a):
                yield (a,)+q


def clog2(m): return (m-1).bit_length()


def predicted_depth(n):
    if n<=5: return 2
    return 1+clog2(n//2)


def main():
    checked=0
    for n in range(6,21):
        for p in partitions(n):
            if len(p)<2: continue
            ff,dd=joint_wl_first_differences((n,),p,8)
            s=clog2(min(p))
            assert ff==s-1,(n,p,ff,s-1)
            assert dd==s,(n,p,dd,s)
            # Lemma 4.3 then gives pairwise C^3 counting depth s+1.
            checked+=1
    # hardest balanced witness and resulting defining-depth formula
    for n in range(6,41):
        p=(n//2,n-n//2)
        ff,dd=joint_wl_first_differences((n,),p,8)
        q=clog2(n//2)
        assert dd==q,(n,p,dd,q)
        assert predicted_depth(n)==q+1
    # small cycles: order + degree 2 defines C_n for n<6 at depth 2.
    for n in range(3,6): assert predicted_depth(n)==2
    print(f'VERIFY_OK partitions={checked} exhaustive_n=6..20 balanced_n=6..40 formula_small=3..5')

if __name__=='__main__': main()
