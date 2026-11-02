"""Exact checks for the finite homocyclic subgroup-polynomial theorem.

Two independently structured implementations of Delsarte's sum:
(1) enumerate conjugate partitions and reverse their polynomials;
(2) propagate Gaussian factors by a top-down transfer recurrence.
No external dependencies. This is finite verification, not an infinite proof.
"""
from functools import lru_cache
from itertools import combinations_with_replacement


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return tuple(out)


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b): out[i+j] += v*w
    return tuple(out)


@lru_cache(None)
def gaussian(n, k):
    if k < 0 or k > n: return (0,)
    if k in (0, n): return (1,)
    left = gaussian(n - 1, k)
    right = (0,) * (n - k) + gaussian(n - 1, k - 1)
    return add(left, right)


def del_sarte_polynomial(r, a):
    """Full subgroup polynomial in increasing powers of p."""
    total = (0,)
    for asc in combinations_with_replacement(range(r + 1), a):
        heights = tuple(reversed(asc))
        next_heights = heights[1:] + (0,)
        summand = (1,)
        shift = 0
        for h, nxt in zip(heights, next_heights):
            shift += nxt * (r - h)
            summand = multiply(summand, gaussian(r - nxt, h - nxt))
        total = add(total, (0,) * shift + summand)
    return total


def reversed_transfer(r, a):
    """Independent transfer in the coefficient-of-codegree variable t."""
    s = r // 2
    successor_states = {0: (1,)}
    for _ in range(a):
        new_states = {}
        for successor, poly in successor_states.items():
            for h in range(successor, r + 1):
                defect = (h-s)*(h-(r-s))
                edge_poly = multiply(poly, gaussian(r-successor,h-successor))
                term = (0,) * defect + edge_poly
                new_states[h] = add(new_states.get(h, (0,)), term)
        successor_states = new_states
    total=(0,)
    for polynomial in successor_states.values():
        total=add(total,polynomial)
    return total


def coeff(poly, k):
    return poly[k] if k < len(poly) else 0


def xi_even_coefficients(s, max_degree):
    """Published limiting block series: Gaussian(2s,s;t) prod_{j<=s}(1-t^j)^(-2)."""
    result=gaussian(2*s,s)
    for j in range(1,s+1):
        factor=[0]*(max_degree+1)
        for m in range(max_degree//j+1): factor[j*m]=m+1
        result=multiply(result,tuple(factor))[:max_degree+1]
    return result


def main():
    total_tests=0
    for r in range(2, 9):
        vals=[]
        for a in range(1, 8):
            direct=del_sarte_polynomial(r,a)
            reverse=reversed_transfer(r,a)
            expected_degree=a*(r//2)*(r-r//2)
            assert len(direct)-1 == expected_degree, (r,a,'degree')
            assert tuple(reversed(direct)) == reverse, (r,a,'independent transfer')
            assert all(v>=0 for v in direct)
            vals.append(reverse)
            total_tests+=1
            if r%2==0:
                assert coeff(reverse,0)==1
                assert coeff(reverse,1)==3
            else:
                assert coeff(reverse,0)==a+1
                assert coeff(reverse,1)==2*a
        for k in range(7):
            if r%2==0:
                seen=[coeff(vals[a-1],k) for a in range(k+1,8)]
                assert len(set(seen))==1, (r,k,'even stability',seen)
            else:
                # Eventual affine dependence: second finite difference zero.
                seen=[coeff(vals[a-1],k) for a in range(k+2,8)]
                assert all(seen[i+2]-2*seen[i+1]+seen[i]==0 for i in range(len(seen)-2)), (r,k,'odd affine',seen)
    sharp_tests=0
    for s in range(1,5):
        for a in range(1,8):
            finite=reversed_transfer(2*s,a)
            limiting=xi_even_coefficients(s,a+1)
            assert all(coeff(finite,k)==coeff(limiting,k) for k in range(a+1)), (s,a,'sharp congruence')
            assert coeff(limiting,a+1)-coeff(finite,a+1)==2*a+3, (s,a,'first mismatch')
            sharp_tests+=1
    for r in (2,3,4,5,6):
        print(f'rank {r}: reversed top coefficients for exponents 1,2,3,4')
        for a in range(1,5):
            print(f'  exponent={a}: {reversed_transfer(r,a)[:min(7,a*(r//2)*(r-r//2)+1)]}')
    print(f'Independent exact polynomial checks: {total_tests}')
    print(f'Sharp limiting-series boundary checks: {sharp_tests}')
    print('VERIFY_OK')

if __name__=='__main__':main()
