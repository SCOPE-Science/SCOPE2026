from itertools import product, combinations
from math import comb


def deletion_ball(word):
    return {word[:i] + word[i+1:] for i in range(len(word))}


def is_canonical_type_a_pair(x, y):
    assert len(x) == len(y)
    diffs = [i for i,(a,b) in enumerate(zip(x,y)) if a != b]
    if len(diffs) < 2:
        return False
    i,j = diffs[0], diffs[-1]
    # Outside the first/last differing interval the words must agree.
    if x[:i] != y[:i] or x[j+1:] != y[j+1:]:
        return False
    # They must differ at every position of the interval.
    if any(x[k] == y[k] for k in range(i,j+1)):
        return False
    # The two interval words must be opposite-phase alternations on two symbols.
    a,b = x[i], y[i]
    if a == b:
        return False
    for t,k in enumerate(range(i,j+1)):
        ex = a if t % 2 == 0 else b
        ey = b if t % 2 == 0 else a
        if x[k] != ex or y[k] != ey:
            return False
    return True


def closed_edges(q,n):
    assert q >= 2 and n >= 2
    num = q * (1 - n * q**(n-1) + (n-1) * q**n)
    den = 2 * (q-1)
    assert num % den == 0
    return num // den


def sum_edges(q,n):
    return comb(q,2) * sum((n-L+1)*q**(n-L) for L in range(2,n+1))


def direct_counts(q,n):
    alphabet = tuple(range(q))
    words = list(product(alphabet, repeat=n))
    count2 = 0
    countcanon = 0
    mismatch=[]
    for x,y in combinations(words,2):
        inter = deletion_ball(x) & deletion_ball(y)
        two = len(inter)==2
        canon = is_canonical_type_a_pair(x,y) or is_canonical_type_a_pair(y,x)
        if two:
            count2 += 1
        if canon:
            countcanon += 1
        if two != canon and len(mismatch) < 5:
            mismatch.append((x,y,len(inter),canon))
        if len(inter) > 2:
            raise AssertionError((q,n,x,y,len(inter)))
    if mismatch:
        raise AssertionError((q,n,mismatch))
    return count2,countcanon


def main():
    cases=[]
    cases += [(2,n) for n in range(2,10)]
    cases += [(3,n) for n in range(2,7)]
    cases += [(4,n) for n in range(2,6)]
    cases += [(5,n) for n in range(2,5)]
    for q,n in cases:
        s=sum_edges(q,n)
        c=closed_edges(q,n)
        assert s==c,(q,n,s,c)
        d,k=direct_counts(q,n)
        assert d==k==c,(q,n,d,k,c)
        avg_num=2*c
        print(f'q={q} n={n} edges={c} avg_degree={avg_num}/{q**n}')
    # Binary recurrence and first values.
    vals=[closed_edges(2,n) for n in range(2,11)]
    assert vals == [1,5,17,49,129,321,769,1793,4097]
    for n in range(2,10):
        assert closed_edges(2,n+1)-closed_edges(2,n) == n*2**(n-1)
    print('binary_edges_n2_to_n10=' + ','.join(map(str,vals)))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
