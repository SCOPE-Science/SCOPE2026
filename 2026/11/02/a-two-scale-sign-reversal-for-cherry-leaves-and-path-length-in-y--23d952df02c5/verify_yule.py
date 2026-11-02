"""Exact finite checks for two-scale cherry/depth identities in leaf-splitting trees.

This standalone program uses only the Python 3 standard library.
It is a consistency check, not a replacement for the all-size proof.
"""
from fractions import Fraction
from math import factorial

assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)


def leaves(tree):
    if tree is None:
        return 1
    return leaves(tree[0]) + leaves(tree[1])


def split_at(tree, index):
    if tree is None:
        check(index == 0, 'nonzero index for leaf')
        return (None, None)
    k = leaves(tree[0])
    if index < k:
        return (split_at(tree[0], index), tree[1])
    return (tree[0], split_at(tree[1], index - k))


def measures(tree, depth=0):
    """Returns (leaves, Sackin, cherries, cherry-tip-depth sum)."""
    if tree is None:
        return (1, depth, 0, 0)
    left, right = tree
    a, s1, c1, q1 = measures(left, depth + 1)
    b, s2, c2, q2 = measures(right, depth + 1)
    if left is None and right is None:
        return (2, s1 + s2, 1, 2 * (depth + 1))
    return (a + b, s1 + s2, c1 + c2, q1 + q2)


def h(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def expected(n):
    s = 2 * n * (h(n) - 1)
    c = Fraction(n, 3)
    q = Fraction(2, 3) * s + Fraction(2 * n, 9)
    cov = -Fraction((n - 3) * (n + 2), 9 * (n - 1))
    cs = cov + c * s
    return c, s, q, cs, cov


def descendants(tree):
    return [split_at(tree, i) for i in range(leaves(tree))]


if __name__ == '__main__':
    # Exact all-history enumeration for every size from 2 through 9.
    sums = {}
    counts = {}
    def explore(tree):
        n, s, c, q = measures(tree)
        counts[n] = counts.get(n, 0) + 1
        a = sums.setdefault(n, [0, 0, 0, 0])
        a[0] += c
        a[1] += s
        a[2] += q
        a[3] += c*s
        if n < 9:
            for i in range(n):
                explore(split_at(tree, i))

    explore((None, None))
    for n in range(2, 10):
        check(counts[n] == factorial(n-1), ('history-count', n))
        moments = [Fraction(u, counts[n]) for u in sums[n]]
        if n >= 3:
            c, s, q, cs, cov = expected(n)
            for name, actual, predicted in zip(('C', 'S', 'Q', 'CS'), moments, (c,s,q,cs)):
                check(actual == predicted, ('enumeration', n, name, actual, predicted))
            check(moments[3] - moments[0]*moments[1] == cov, ('covariance',n))
            check(q/Fraction(n) - Fraction(2,3)*(s/n) == Fraction(2,9), ('local',n))
        else:
            check(moments == [1,2,2,2], ('initial',n,moments))

    # Independently test single-step conditional increment identities on all
    # histories with at most 7 leaves. This directly checks the key lemma.
    sample_count = 0
    def test_transitions(tree):
        global sample_count
        n,s,c,q = measures(tree)
        children = descendants(tree)
        child_stats = [measures(u) for u in children]
        actual = [sum(z[j] for z in child_stats) for j in (1,2,3)]
        cbar = Fraction(n-2, n)*c+1
        sbar = Fraction(n+1, n)*s+2
        qbar = Fraction(n-2,n)*q+Fraction(2,n)*s+2
        for label,lhs,rhs in zip(('c','s','q'),(Fraction(actual[1],n),Fraction(actual[0],n),Fraction(actual[2],n)),(cbar,sbar,qbar)):
            check(lhs == rhs, ('transition',n,label,lhs,rhs))
        csbar = Fraction(n-1,n)*c*s+Fraction(n+1,n)*s+(2-Fraction(4,n))*c-Fraction(q,n)+2
        actual_cs=Fraction(sum(z[1]*z[2] for z in child_stats), n)
        check(actual_cs==csbar,('transition-cs',n,actual_cs,csbar))
        sample_count+=1
        if n < 7:
            for child in children:
                test_transitions(child)
    test_transitions((None,None))

    # All-size rational recurrence substitution, for a non-exhaustive range.
    for n in range(3, 1001):
        c,s,q,cs,cov=expected(n)
        cn,sn,qn,csn,covn=expected(n+1)
        check(cn==Fraction(n-2,n)*c+1,('rec-c',n))
        check(sn==Fraction(n+1,n)*s+2,('rec-s',n))
        check(qn==Fraction(n-2,n)*q+Fraction(2,n)*s+2,('rec-q',n))
        check(csn==Fraction(n-1,n)*cs+Fraction(n+1,n)*s+(2-Fraction(4,n))*c-q/n+2,('rec-cs',n))
        check(covn==Fraction(n-1,n)*cov-Fraction(2,9),('rec-cov',n))

    print(f'PASS: {assertions} exact assertions; {sum(counts.values())} growth histories; {sample_count} independent transition cases.')
