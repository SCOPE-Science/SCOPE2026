"""Exact rational finite-state diagnostics for a nonuniform coupon-refresh process."""
from fractions import Fraction as F
from itertools import combinations


def subset_formula(w, p):
    q = 1 - p
    if q <= 0 or any(x <= 0 for x in w) or sum(w) != 1:
        raise ValueError('Positive probability weights summing to one, p<1, required')
    r = p / q
    val = F(0)
    for k in range(1, len(w) + 1):
        for inds in combinations(range(len(w)), k):
            val += (r**k - (-1)**k) / sum((w[i] for i in inds), F(0))
    return val


def formula_laplace(w, p, s):
    r = p / (1-p)
    a = F(1, 1) / s
    b = F(1, 1) / s
    for k in range(1, len(w)+1):
        for inds in combinations(range(len(w)), k):
            denom = s + sum((w[i] for i in inds), F(0))
            a += (-1)**k / denom
            b += r**k / denom
    return a/b


def solve(A, b):
    a = [list(row)+[b[i]] for i, row in enumerate(A)]
    n = len(b)
    for c in range(n):
        ix = next((i for i in range(c,n) if a[i][c]), None)
        if ix is None: raise ValueError('Singular test system')
        a[c],a[ix] = a[ix],a[c]
        pivot = a[c][c]
        a[c] = [z/pivot for z in a[c]]
        for i in range(n):
            if i != c and a[i][c]:
                t = a[i][c]
                a[i] = [x-t*y for x,y in zip(a[i],a[c])]
    return [row[n] for row in a]


def discrete_markov(w,p,z=None):
    n=len(w); target=(1<<n)-1; states=list(range(target))
    matrix=[[F(int(i==j)) for j in states] for i in states]
    rhs=[F(1) if z is None else F(0) for _ in states]
    scalar = F(1) if z is None else z
    for mask in states:
        for i,weight in enumerate(w):
            for nxt,pr in ((mask|(1<<i),weight*(1-p)),(mask&~(1<<i),weight*p)):
                if nxt == target:
                    if z is not None: rhs[mask]+=z*pr
                else:
                    matrix[mask][nxt]-=scalar*pr
    return solve(matrix,rhs)[0]


def test():
    cases = [
        ([F(1)],F(1,4)),
        ([F(1,2),F(1,2)],F(1,2)),
        ([F(1,5),F(4,5)],F(2,5)),
        ([F(1,2),F(1,3),F(1,6)],F(1,3)),
        ([F(1,10),F(1,5),F(3,10),F(2,5)],F(1,4)),
        ([F(1,5)]*5,F(1,5)),
        ([F(1,2),F(1,3),F(1,6)],F(0))]
    ncheck=0
    for w,p in cases:
        expected=subset_formula(w,p)
        direct=discrete_markov(w,p)
        assert expected==direct,(w,p,expected,direct)
        ncheck+=1
        if len(w)<=4:
            for z in (F(1,3),F(3,5),F(4,5)):
                s=(1-z)/z
                a=formula_laplace(w,p,s)
                b=discrete_markov(w,p,z)
                assert a==b,(w,p,z,a,b)
                ncheck+=1
    assert subset_formula([F(1,5),F(4,5)],F(2,5))==F(355,36)
    assert subset_formula([F(1,2),F(1,2)],F(2,5))==F(55,9)
    ncheck+=2
    for n in range(2,11):
        unif=[F(1,n)]*n
        for p in (F(0),F(1,5),F(1,2),F(4,5)):
            u=subset_formula(unif,p)
            for smallnum in range(1,n):
                vals=[F(smallnum,n*n)]+[F(n*n-smallnum,n*n*(n-1))]*(n-1)
                assert subset_formula(vals,p)>u
                ncheck+=1
    print('PASS:',ncheck,'exact rational checks; full matrix mean/PGF, sample strict minimizers.')
if __name__ == '__main__': test()
