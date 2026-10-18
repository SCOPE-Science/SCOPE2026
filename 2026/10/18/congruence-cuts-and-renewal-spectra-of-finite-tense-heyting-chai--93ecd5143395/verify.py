"""Exact small-chain checks for tense Heyting congruence decomposition.
Python 3.10+, standard library only; no network or external packages.
"""
from collections import Counter
from itertools import combinations_with_replacement


def right_adjoint_maps(m):
    # Finite-chain right adjoints preserving least and greatest elements.
    yield from ((0,) + middle + (m,)
                for middle in combinations_with_replacement(range(m + 1), m - 1))


def left_adjoint(g):
    return tuple(next(i for i, y in enumerate(g) if y >= j)
                 for j in range(len(g)))


def small_test(g, h):
    p, f = left_adjoint(g), left_adjoint(h)
    return all(g[i] <= f[i] and h[i] <= p[i] for i in range(len(g)))


def heyting(x, y, m):
    return m if x <= y else y


def full_axioms(g, h):
    m = len(g) - 1
    p, f = left_adjoint(g), left_adjoint(h)
    if g[0] != 0 or h[0] != 0 or g[m] != m or h[m] != m:
        return False
    for x in range(m+1):
        for y in range(m+1):
            if (p[x] <= y) != (x <= g[y]): return False
            if (f[x] <= y) != (x <= h[y]): return False
            if min(g[x], f[y]) > f[min(x,y)]: return False
            if min(h[x], p[y]) > p[min(x,y)]: return False
            if g[max(x,y)] > max(g[x], f[y]): return False
            if h[max(x,y)] > max(h[x], p[y]): return False
            v=heyting(x,y,m)
            if g[v] > heyting(g[x],g[y],m):return False
            if h[v] > heyting(h[x],h[y],m):return False
            if g[v] > heyting(f[x],f[y],m):return False
            if h[v] > heyting(p[x],p[y],m):return False
    return True


def partitions(n):
    # Every partition as a restricted growth tuple.
    if n == 1:
        yield (0,)
    else:
        for q in partitions(n-1):
            for k in range(max(q)+2):
                yield q + (k,)


def preserves(part, maps):
    n=len(part)
    for f in maps:
        for i in range(n):
            for j in range(i+1,n):
                if part[i]==part[j] and part[f(i)] != part[f(j)]:
                    return False
    return True


def direct_congruence_cut_count(g, h, parts):
    m=len(g)-1;p,f=left_adjoint(g),left_adjoint(h)
    maps=[g.__getitem__,h.__getitem__,p.__getitem__,f.__getitem__,
          lambda x:x]  # binary signature is checked below
    c=0
    for q in parts:
        ops=maps[:]
        # All unary polynomial sections of each basic binary operation.
        for a in range(m+1):
            ops.extend([lambda x,a=a:min(x,a),lambda x,a=a:max(x,a),
                        lambda x,a=a:heyting(x,a,m),lambda x,a=a:heyting(a,x,m)])
        if preserves(q,ops):c+=1
    return c


def run():
    B={0:1}; hist={}; checked=0; checked_direct=0
    for m in range(1,7):
        maps=list(right_adjoint_maps(m)); distribution=Counter()
        cutsets=Counter(); all_satisfy=0
        for g in maps:
            for h in maps:
                a=small_test(g,h)
                if m<=4:
                    assert a==full_axioms(g,h), (m,g,h)
                if not a: continue
                all_satisfy+=1
                cuts=frozenset(k for k in range(1,m) if g[k]==h[k]==k)
                distribution[len(cuts)]+=1
                cutsets[cuts]+=1
                if m<=4:
                    c=direct_congruence_cut_count(g,h,list(partitions(m+1)))
                    assert c==len(cuts)+2, (m,g,h,c,cuts)
                    checked_direct+=1
        B[m]=all_satisfy;hist[m]=distribution
        for mask in range(1<<(m-1)):
            K=frozenset(j+1 for j in range(m-1) if mask>>j&1)
            boundaries=[0]+sorted(K)+[m]
            expected=1
            for a,b in zip(boundaries,boundaries[1:]):
                expected*=B[b-a]
            got=sum(v for s,v in cutsets.items() if K.issubset(s))
            assert got==expected,(m,K,got,expected)
        print('m',m,'B',B[m],'cuts',dict(sorted(distribution.items())))
    I={0:0}
    for m in range(1,7):
        I[m]=B[m]-sum(I[j]*B[m-j] for j in range(1,m))
        assert I[m]==hist[m][0]
        # Complete renewal coefficient check via compositions.
        def split_sum(n,r):
            if r==1:return I[n] if n>0 else 0
            return sum(I[j]*split_sum(n-j,r-1) for j in range(1,n))
        for r in range(1,m+1):assert split_sum(m,r)==hist[m][r-1]
    print('INDECOMPOSABLE',I)
    print('VERIFY_OK all_axiom_cases_m_le_4',sum(len(list(right_adjoint_maps(m)))**2 for m in range(1,5)),
          'direct_congruence_algebras',checked_direct,'cut_subset_checks',sum(2**(m-1) for m in range(1,7)))

if __name__=='__main__':run()
