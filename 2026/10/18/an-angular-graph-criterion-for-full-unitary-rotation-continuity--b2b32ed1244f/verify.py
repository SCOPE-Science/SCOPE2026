#!/usr/bin/env python3
"""Finite checks of normalized bosonic transfer weights and angular geometry."""
import cmath
import math

def verify_basis_transfer():
    checks = 0
    for m in range(1, 31):
        for k in range(m):
            # J_12 sends (k,m-k) to (k+1,m-k-1).
            direct = (m-k) * math.sqrt(
                math.factorial(k+1)*math.factorial(m-k-1)
                / (math.factorial(k)*math.factorial(m-k))
            )
            target = math.sqrt((k+1)*(m-k))
            assert math.isclose(direct, target, rel_tol=1e-12, abs_tol=1e-12)
            checks += 1
    return checks

def verify_angles():
    checks = 0
    for m in range(1, 601):
        for k in range(m):
            edge = 1 / math.sqrt((k+1)*(m-k))
            increment = 2 * (math.asin(math.sqrt((k+1)/m))
                             - math.asin(math.sqrt(k/m)))
            assert edge <= increment + 1e-10
            assert increment <= math.pi*edge + 1e-10
            checks += 1
    return checks

def verify_separation():
    nums = []
    for m in (10000, 40000, 160000, 640000):
        k = m // 2
        h = int(math.pi * math.sqrt(m))
        dist = sum(1 / math.sqrt((j+1)*(m-j)) for j in range(k,k+h))
        oscillation = abs(cmath.exp(1j*h/math.sqrt(m)) - 1)
        assert dist < 20 / math.sqrt(m)
        assert oscillation > 1.99
        nums.append((dist, oscillation))
    assert all(nums[i][0] > nums[i+1][0] for i in range(len(nums)-1))
    for m in (100, 10000, 1000000):
        rho = math.sqrt(m+1)-math.sqrt(m)
        assert rho < 1 / math.sqrt(m)
        assert abs((-1)**m-(-1)**(m+1)) == 2
    return len(nums) + 3

def main():
    a=verify_basis_transfer()
    b=verify_angles()
    c=verify_separation()
    print("FOCK_FULL_UNITARY_ANGULAR_GRAPH_FINITE_IDENTITIES_OK "
          f"transfers={a} angular_edges={b} separation_checks={c}")

if __name__ == "__main__":
    main()
