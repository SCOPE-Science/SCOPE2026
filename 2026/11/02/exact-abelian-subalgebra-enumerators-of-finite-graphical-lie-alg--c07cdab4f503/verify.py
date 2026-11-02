"""Independent finite-field enumeration of graph Lie-algebra abelian subspaces.

Usage: python verify.py. Only prime fields are needed for the exhaustive tests;
the mathematical statements apply to arbitrary prime powers.
"""
from itertools import combinations, product
from math import prod


def rank_mod(matrix, p):
    if not matrix:
        return 0
    arr = [list(row) for row in matrix]
    h = len(arr)
    n = len(arr[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, h) if arr[i][c] % p), None)
        if pivot is None:
            continue
        arr[r], arr[pivot] = arr[pivot], arr[r]
        scale = pow(arr[r][c] % p, -1, p)
        arr[r] = [(a * scale) % p for a in arr[r]]
        for i in range(h):
            if i != r and arr[i][c]:
                d = arr[i][c]
                arr[i] = [(a - d * b) % p for a, b in zip(arr[i], arr[r])]
        r += 1
        if r == h:
            break
    return r


def all_rref(n, k, p):
    for pivots in combinations(range(n), k):
        allowed = [(r, c) for r in range(k) for c in range(pivots[r]+1, n) if c not in pivots]
        for choices in product(range(p), repeat=len(allowed)):
            matrix = [[0] * n for _ in range(k)]
            for r, c in enumerate(pivots):
                matrix[r][c] = 1
            for (r, c), a in zip(allowed, choices):
                matrix[r][c] = a
            yield matrix


def abelian_direct(n, edges, p):
    ans = []
    for k in range(n+1):
        count = 0
        for basis in all_rref(n, k, p):
            good = all((basis[i][a]*basis[j][b] - basis[i][b]*basis[j][a]) % p == 0
                       for a,b in edges for i in range(k) for j in range(i+1,k))
            count += good
        ans.append(count)
    return ans


def comps(n, edges, support):
    seen = set()
    support = set(support)
    adj = {a: [] for a in support}
    for a,b in edges:
        if a in support and b in support:
            adj[a].append(b)
            adj[b].append(a)
    out = 0
    for v in support:
        if v in seen:
            continue
        out += 1
        stack = [v]
        seen.add(v)
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return out


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    numer = prod(q**(n-i)-1 for i in range(k))
    denom = prod(q**(k-i)-1 for i in range(k))
    return numer // denom


def gl(k, q):
    return prod(q**k - q**i for i in range(k))


def predicted(n, edges, q):
    comps_list = []
    for mask in range(1<<n):
        S = [i for i in range(n) if mask >> i & 1]
        comps_list.append((len(S), comps(n,edges,S)))
    alpha = max(c for size,c in comps_list)
    max_count = sum((q-1)**(size-alpha) for size,c in comps_list if c==alpha)
    F = [sum((q**j-1)**c*(q-1)**(size-c) for size,c in comps_list)
         for j in range(n+1)]
    counts = []
    for k in range(n+1):
        full = sum(gaussian(k,j,q)*(-1)**(k-j)*q**((k-j)*(k-j-1)//2)*F[j]
                   for j in range(k+1))
        assert full % gl(k,q) == 0
        counts.append(full // gl(k,q))
    assert counts[alpha] == max_count
    assert all(x==0 for x in counts[alpha+1:])
    return counts,alpha,max_count



def abelian_all_direct(n, edges, p):
    """Enumerate every subspace of the full Lie algebra, not just quotients."""
    m=len(edges)
    output=[]
    for d in range(n+m+1):
        count=0
        for basis in all_rref(n+m,d,p):
            if all((basis[i][a]*basis[j][b] - basis[i][b]*basis[j][a]) % p == 0
                   for a,b in edges for i in range(d) for j in range(i+1,d)):
                count+=1
        output.append(count)
    return output


def full_predicted(n,edges,q):
    ranks,alpha,top=predicted(n,edges,q)
    m=len(edges)
    result=[0]*(n+m+1)
    for k,v in enumerate(ranks):
        for t in range(m+1):
            result[k+t]+=v*gaussian(m,t,q)*q**(k*(m-t))
    assert result[m+alpha]==top
    assert not any(result[m+alpha+1:])
    return result

def main():
    checked=0
    for n,p in [(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(3,3),(4,3),(3,5)]:
        possible=list(combinations(range(n),2))
        for mask in range(1<<len(possible)):
            edges=[e for i,e in enumerate(possible) if mask>>i & 1]
            direct=abelian_direct(n,edges,p)
            pred,alpha,m=predicted(n,edges,p)
            assert direct==pred,(n,p,edges,direct,pred)
            assert m==direct[alpha]
            checked+=1
    checked_full=0
    for n,p,max_edges in [(1,2,0),(2,2,1),(3,2,3),(4,2,2),(1,3,0),(2,3,1),(3,3,3)]:
        possible=list(combinations(range(n),2))
        for mask in range(1<<len(possible)):
            edges=[e for i,e in enumerate(possible) if mask>>i & 1]
            if len(edges)>max_edges:
                continue
            actual=abelian_all_direct(n,edges,p)
            expected=full_predicted(n,edges,p)
            assert actual==expected,(n,p,edges,actual,expected)
            checked_full+=1
    print('VERIFY_OK',checked,'quotient graph-field cases and',checked_full,'full-Lie-algebra cases;',
          'independent RREF-bracket enumeration vs connected-support Möbius and Gaussian formulas')
    for n,edges,p in [(4,[(0,1),(1,2),(2,3)],2),(4,[(0,1),(1,2),(2,3)],3),(5,[(i,i+1) for i in range(4)],3)]:
        print('EXAMPLE',n,edges,p,predicted(n,edges,p))


if __name__=='__main__':
    main()
