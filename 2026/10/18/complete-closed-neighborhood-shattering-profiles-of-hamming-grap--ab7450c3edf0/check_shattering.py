"""Independent finite enumeration of closed-neighborhood shattering in Hamming graphs.
No third-party dependencies. Python 3.9+.
"""
from itertools import product, combinations
from math import comb


def predicted(q, d):
    n = q ** d
    if d == 1:
        return (1, 0, 0, 0)
    singles = n
    pairs = 0 if (d, q) == (2, 2) else n * (d*(q-1) + comb(d,2)*(q-1)**2) // 2
    if d == 2:
        triples = n*(q-1)**2*(q-2) if q >= 4 else 0
    else:
        triples = n*(comb(1+d*(q-1),3) - d*comb(q,3))
    return 1, singles, pairs, triples


def brute_counts(q, d, include_four=True):
    vertices = list(product(range(q), repeat=d))
    m = len(vertices)
    centers = []
    for c in vertices:
        centers.append(sum(1 << i for i,x in enumerate(vertices)
                           if sum(a!=b for a,b in zip(x,c)) <= 1))
    result = [1]
    for k in (1,2,3,4):
        if k == 4 and not include_four:
            break
        cnum=0
        for subset in combinations(range(m), k):
            patterns = set()
            for mask in centers:
                p=0
                for j,i in enumerate(subset):
                    if mask >> i & 1:
                        p |= 1 << j
                patterns.add(p)
                if len(patterns) == (1<<k):
                    cnum+=1
                    break
        result.append(cnum)
    return result


def main():
    cases = [(2,1),(3,1),(2,2),(3,2),(4,2),(5,2),(6,2),
             (2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]
    total_triples=0
    for q,d in cases:
        expect=predicted(q,d)
        checkfour=(q**d<=32)
        observed=brute_counts(q,d,include_four=checkfour)
        assert tuple(observed[:4]) == expect, (q,d,expect,observed)
        if checkfour and len(observed)==5:
            assert observed[4]==0,(q,d,observed)
        total_triples += expect[3]
        print('CASE',q,d,'observed',observed,'expected',expect,
              'four_exhaustive',checkfour,'PASS')
    print('VERIFY_OK cases',len(cases),'total_shattered_triples',total_triples,
          'all_coefficients=PASS four_set_upper_boundary=PASS')

if __name__ == '__main__':
    main()
