"""Standalone small-prime verification of full-support evolution algebra symmetry counts.

Run: python evolution_fullsupport_checker.py
Counts full-support structure matrices directly rather than using orbit assignments.
"""
from itertools import product


def invertible(flat, n, p):
    a = [list(flat[i*n:(i+1)*n]) for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col] % p), None)
        if pivot is None:
            return False
        a[col], a[pivot] = a[pivot], a[col]
        u = pow(a[col][col], -1, p)
        for j in range(col, n):
            a[col][j] = (a[col][j]*u) % p
        for i in range(col+1, n):
            v = a[i][col]
            for j in range(col, n):
                a[i][j] = (a[i][j]-v*a[col][j]) % p
    return True


def is_automorphism(flat, n, p, perm, scales):
    for i in range(n):
        for j in range(n):
            if (flat[perm[i]*n+perm[j]] * scales[i]**2 - flat[i*n+j]*scales[j]) % p:
                return False
    return True


def run_case(p, n):
    assert p in (3, 5)
    qminus = p-1
    tau = list(range(n)); tau[0],tau[1]=tau[1],tau[0]
    expected = qminus**(n*n-2*n+3)
    trans_count = trans_inv = invertible_count = duplicates = 0
    cases = 0
    for mat in product(range(1, p), repeat=n*n):
        cases += 1
        good = invertible(mat, n, p)
        invertible_count += good
        found = 0
        for t in range(1, p):
            scales=[1]*n
            scales[0]=t
            scales[1]=pow(t,-1,p)
            found += is_automorphism(mat,n,p,tau,scales)
        duplicates += found > 1
        trans_count += found > 0
        trans_inv += (found>0) and good
    assert cases == (p-1)**(n*n)
    assert trans_count == expected, (p,n,trans_count,expected)
    assert duplicates == 0
    assert 0 < trans_inv <= trans_count
    assert invertible_count > 0
    print(f'q={p} n={n} tested={cases} invertible={invertible_count} '
          f'swap_automorphisms={trans_count} swap_invertible={trans_inv} '
          f'duplicate_scales={duplicates} expected={expected}')
    return cases



def permutation_orbit_checks():
    from itertools import permutations
    tested=0
    for n in (5, 6, 7):
        for sigma in permutations(range(n)):
            k=sum(i != sigma[i] for i in range(n))
            if k == 0:
                continue
            seen=set(); orbits=0
            for i in range(n):
                for j in range(n):
                    if (i,j) in seen:
                        continue
                    orbits += 1
                    a,b=i,j
                    while (a,b) not in seen:
                        seen.add((a,b))
                        a,b=sigma[a],sigma[b]
            deficit=n*n-orbits
            if k == 2:
                assert deficit == 2*n-2
            else:
                assert deficit-k >= (2*n-2 if n == 5 else 2*n-1), (n,sigma,k,deficit)
            tested += 1
    print(f'PERMUTATION_ORBIT_DEFICIT_CHECKS_PASSED permutations={tested}')


def main():
    total=0
    for q,n in ((3,3),(3,4),(5,3)):
        total+=run_case(q,n)
    permutation_orbit_checks()
    print('EVOLUTION_FULLSUPPORT_AUTOMORPHISM_CHECKS_PASSED total_matrices='+str(total))


if __name__=='__main__':
    main()
