"""Reproduce finite character-moment and sharp-deficit checks (Python standard library)."""
import itertools
import math
from fractions import Fraction
from functools import lru_cache

CHECKS = 0

def check(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

@lru_cache(None)
def partitions(n, cap=None):
    if n == 0:
        return ((),)
    if cap is None:
        cap = n
    return tuple((j,) + tail
                 for j in range(min(n, cap), 0, -1)
                 for tail in partitions(n-j, j))

def specht_dimension(shape):
    ans = Fraction(math.factorial(sum(shape)), 1)
    for row, length in enumerate(shape):
        for col in range(length):
            hook = length-col + sum(other > col for other in shape[row+1:])
            ans /= hook
    check(ans.denominator == 1, ('hook-integrality', shape))
    return ans.numerator

@lru_cache(None)
def characters_in_tensor_power(rank, power):
    return {shape+(0,)*(rank-len(shape)): specht_dimension(shape)
            for shape in partitions(power) if len(shape) <= rank}

def schur_moment(rank, r, s):
    if (r-s) % rank:
        return 0
    t = (r-s) // rank
    A = characters_in_tensor_power(rank, r)
    B = characters_in_tensor_power(rank, s)
    return sum(mult * B.get(tuple(v-t for v in shape), 0)
               for shape, mult in A.items())

@lru_cache(None)
def permutations_signed(n):
    result = []
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i+1, n))
        result.append((perm, -1 if inversions % 2 else 1))
    return result

@lru_cache(None)
def compositions(n, k):
    if k == 1:
        return ((n,),)
    return tuple((j,) + tail for j in range(n+1)
                 for tail in compositions(n-j, k-1))

def weyl_torus_moment(rank, r, s):
    """Independent SU(rank) Weyl-denominator constant-term computation.

    Weyl integration on the determinant-one eigenvalue torus takes the
    constant terms of exponents whose N coordinates are all equal.
    """
    if (r-s) % rank:
        return 0
    shift_sum = (r-s)//rank
    factorial = [math.factorial(j) for j in range(max(r,s)+1)]
    s_terms = [(v, math.factorial(s)//math.prod(factorial[x] for x in v))
               for v in compositions(s, rank)]
    total = 0
    for perm, parity in permutations_signed(rank):
        for other, parity2 in permutations_signed(rank):
            shift = [shift_sum - perm[i] + other[i] for i in range(rank)]
            sub = 0
            for v, coefficient in s_terms:
                u = [v[i]+shift[i] for i in range(rank)]
                if min(u) < 0 or max(u) > r:
                    continue
                multinomial = math.factorial(r)//math.prod(factorial[x] for x in u)
                sub += coefficient * multinomial
            total += parity * parity2 * sub
    order = math.factorial(rank)
    check(total % order == 0, ('weyl-integrality', rank, r, s))
    return total//order

def moment_from_representation(rank, a, b):
    out = 0j
    for j in range(4):
        for k in range(4):
            r = 3+j-k
            out += (math.comb(3,j)*math.comb(3,k)
                    * a**j * b**(3-j) * a.conjugate()**k
                    * b.conjugate()**(3-k) * schur_moment(rank,r,6-r))
    check(out.imag == 0, ('real-moment',rank,a,b,out))
    return int(out.real)

def compact_formula(rank, a, b):
    p = int(abs(a)**2)
    q = int(abs(b)**2)
    S = p+q
    w = a*b.conjugate()
    out = 6*S**3+36*S*p*q
    if rank == 3:
        out += 10*int((w**3).real)
    elif rank == 4:
        out += 24*S*int((w**2).real)
    elif rank == 6:
        out += 2*int((w**3).real)
    return out

def four_times_K(rank):
    return {3:65,4:84,6:61}.get(rank, 60)

def four_times_deficit(rank, a, b):
    p = int(abs(a)**2)
    q = int(abs(b)**2)
    S = p+q
    w = a*b.conjugate()
    out = 36*S*(p-q)**2
    if rank == 4:
        out = 60*S*(p-q)**2 + 96*S*(p*q-int((w**2).real))
    elif rank in (3,6):
        m = 5 if rank == 3 else 1
        out += m*S**3 - 8*m*int((w**3).real)
    return out

def main():
    # Representation theory: all moment cases for every rank 3 through 13.
    for n in range(3,14):
        for r in range(7):
            observed = schur_moment(n,r,6-r)
            prescribed = 6 if r==3 else (
                5 if n==3 and r in (0,6) else
                4 if n==4 and r in (1,5) else
                1 if n==6 and r in (0,6) else 0)
            check(observed == prescribed, ('rank-moment',n,r,observed,prescribed))
    # Independent, exact Weyl-torus integral; no Schur functions used.
    for n,r,s,value in ((3,3,3,6),(3,6,0,5),(3,5,1,0),
                        (4,3,3,6),(4,5,1,4),(4,6,0,0),
                        (5,3,3,6),(6,6,0,1)):
        check(weyl_torus_moment(n,r,s)==value, ('weyl-check',n,r,s))
    # Exact Gaussian-integer coefficient test and global sharp deficit.
    gauss = [complex(x,y) for x in range(-2,3) for y in range(-2,3)]
    for n in range(3,14):
        for a in gauss:
            for b in gauss:
                if a == b == 0:
                    continue
                moment = moment_from_representation(n,a,b)
                predicted = compact_formula(n,a,b)
                check(moment == predicted, ('polynomial',n,a,b,moment,predicted))
                S = int(abs(a)**2+abs(b)**2)
                defect = four_times_K(n)*S**3-4*moment
                check(defect == four_times_deficit(n,a,b),
                      ('sharp-deficit',n,a,b,defect))
                check(defect >= 0, ('sharp-inequality',n,a,b))
    for n in range(3,14):
        for a,b,eq in ((1+0j,1+0j,True), (1+0j,-1+0j,n in (4,5,7,8,9,10,11,12,13)),
                       (1+0j,1j,n not in (3,4,6)), (1+0j,2+0j,False)):
            D = four_times_K(n)*int(abs(a)**2+abs(b)**2)**3-4*moment_from_representation(n,a,b)
            check((D==0)==eq, ('equality',n,a,b,eq,D))
    print('OK exact Schur--Weyl moments, independent Weyl-torus integrals,')
    print('sharp constants, global deficit identities, and equality witnesses.')
    print('Assertions passed:', CHECKS)

if __name__=='__main__':
    main()
