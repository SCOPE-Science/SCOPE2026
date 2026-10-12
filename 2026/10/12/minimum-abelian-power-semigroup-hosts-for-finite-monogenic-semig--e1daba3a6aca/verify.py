"""Self-contained finite checks for a theorem on powers of subsets of finite abelian groups.
Run: python3 check_monogenic.py. Finite tests supplement, not replace, the proof.
"""
from itertools import product, combinations
from math import prod


def profiles(limit):
    profiles_ = [(1,)]
    def rec(start, seq, size):
        for d in range(max(2,start), limit//size+1):
            if seq and d % seq[-1] != 0:
                continue
            entry = tuple(seq)+(d,)
            profiles_.append(entry)
            rec(d, entry, size*d)
    rec(1, (), 1)
    return profiles_


def inspect_group(dims):
    elems = list(product(*(range(d) for d in dims)))
    n = len(elems)
    ix = {e:i for i,e in enumerate(elems)}
    zero = ix[(0,)*len(dims)]
    assert zero == 0
    table = [[ix[tuple((x+y)%d for x,y,d in zip(a,b,dims))]
              for b in elems] for a in elems]
    neg = [ix[tuple((-x)%d for x,d in zip(e,dims))] for e in elems]

    def mul(A,B):
        bits = 0
        for a in range(n):
            if (A>>a)&1:
                for b in range(n):
                    if (B>>b)&1:
                        bits |= 1<<table[a][b]
        return bits

    def index_period(A):
        seen = {A:1}
        power, k = A, 1
        while True:
            power=mul(power,A)
            k+=1
            if power in seen:
                return seen[power], k-seen[power]
            seen[power]=k
            assert k<=n*n+2

    def ord_elem(a):
        cur=0
        for k in range(1,n+1):
            cur=table[cur][a]
            if cur==zero:
                return k
        raise AssertionError

    def pair_structure(A,mu,lam):
        if A.bit_count()!=2:
            return False
        a,b=(i for i in range(n) if (A>>i)&1)
        difference=table[b][neg[a]]
        h_order=ord_elem(difference)
        if h_order!=mu+1:
            return False
        H={0}
        cur=0
        for k in range(1,h_order):
            cur=table[cur][difference]
            H.add(cur)
        assert len(H)==h_order
        cur=0
        for k in range(1,n//h_order+1):
            cur=table[cur][a]
            if cur in H:
                return k==lam
        return False

    outcomes = set()
    tests = 0
    extremizers=0
    for A in range(1,1<<n):
        mu,lam=index_period(A)
        tests+=1
        outcomes.add((mu,lam))
        if mu==1:
            minimum = lam
        else:
            minimum = (mu+1)*lam
        assert n>=minimum, (dims,A,mu,lam,minimum)
        if n==minimum:
            extremizers+=1
            if mu==1:
                assert A.bit_count()==1 and ord_elem(next(i for i in range(n) if (A>>i)&1))==lam
            else:
                assert pair_structure(A,mu,lam), (dims,A,mu,lam)
    return tests,outcomes,extremizers


def explicit_witness(mu,lam):
    dims = (lam,) if mu==1 else (mu+1,lam)
    elems=list(product(*(range(d) for d in dims)))
    a=(1%lam,) if mu==1 else (0,1%lam)
    b=None if mu==1 else (1,1%lam)
    A={a} if mu==1 else {a,b}
    B=A.copy()
    seen={frozenset(B):1}
    k=1
    while True:
        B={tuple((x+y)%d for x,y,d in zip(t,s,dims)) for t in B for s in A}
        k+=1
        fb=frozenset(B)
        if fb in seen:
            assert (seen[fb],k-seen[fb])==(mu,lam), (dims,mu,lam)
            return
        seen[fb]=k
        assert k<=mu+lam+2


def main():
    pairs={}
    total=0
    extremizers=0
    profs=profiles(12)
    for dims in profs:
        tests,outcomes,ext=inspect_group(dims)
        total+=tests
        extremizers+=ext
        for mu,lam in outcomes:
            pairs.setdefault((mu,lam),prod(dims))
            pairs[(mu,lam)] = min(pairs[(mu,lam)],prod(dims))
    for (mu,lam),minimum in pairs.items():
        expected=lam if mu==1 else (mu+1)*lam
        assert minimum==expected,(mu,lam,minimum,expected)
    # Every theoretically possible pair below 12 appears with the optimal host.
    for mu in range(1,13):
        for lam in range(1,13):
            minimum=lam if mu==1 else (mu+1)*lam
            if minimum<=12:
                assert pairs[(mu,lam)]==minimum,(mu,lam,pairs.get((mu,lam)))
    for mu in range(1,14):
        for lam in range(1,11):
            explicit_witness(mu,lam)
    print(f'GROUP_PROFILES={len(profs)} NONEMPTY_SUBSETS={total} OPTIMAL_SUBSETS={extremizers}')
    print(f'OBSERVED_INDEX_PERIOD_PAIRS={len(pairs)} EXPLICIT_WITNESSES={13*10}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
