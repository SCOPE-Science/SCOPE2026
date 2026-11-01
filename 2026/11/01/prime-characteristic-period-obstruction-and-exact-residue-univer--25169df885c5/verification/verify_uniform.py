"""Exhaustive residue-matrix test of the uniform p-adic period obstruction."""
from itertools import product
from math import lcm


def verify(p, max_r):
    modulus = p
    for d in range(1,p):
        modulus = lcm(modulus,p**d-1)
    # The graph's part-size residues define a matrix of order r,
    # independently of the actual positive sizes of the parts.
    patterns = 0
    states = 0
    max_tail = 0
    max_period = 0
    for r in range(2,max_r+1):
        for a in product(range(p), repeat=r):
            patterns += 1
            for x in product(range(p), repeat=r):
                seen = {}
                y = x
                while y not in seen:
                    seen[y] = len(seen)
                    total = sum(a[i]*y[i] for i in range(r)) % p
                    y = tuple((total-a[i]*y[i])%p for i in range(r))
                tail = seen[y]
                period = len(seen)-tail
                if tail > p+1 or modulus % period != 0:
                    raise AssertionError((p,r,a,x,tail,period,modulus))
                if period%(p*p) == 0:
                    raise AssertionError("square of characteristic divides a period")
                states += 1
                max_tail = max(max_tail,tail)
                max_period = max(max_period,period)
    print(f"UNIFORM_PERIOD_VERIFY_OK p={p} patterns={patterns} states={states} "
          f"maximum_observed_tail={max_tail} maximum_observed_period={max_period} "
          f"universal_period_divisor={modulus}")


if __name__ == '__main__':
    verify(3,5)
    verify(5,4)
