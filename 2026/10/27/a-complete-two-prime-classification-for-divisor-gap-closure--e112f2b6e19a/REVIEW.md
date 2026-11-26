# Independent mathematical audit

## correctness

PASS

With exactly two prime factors, an odd n fails at its first gap (least prime minus 1). For n=2^a p^b, the pure powers of two neighboring p are consecutive to it wherever they exist: the next p-multiple is at least 2p, above the least power of two exceeding p. Each such gap is odd and smaller than p and hence must equal 1. If p lies above the last pure power this forces p=2^a+1, with separated p-layers and all gaps equal to divisors. If there is an upper neighbor as well, both gaps can be 1 only for 2,3,4. Primality of 2^a+1 forces a to be a power of two by the odd-power factorization. For p=3,a≤4 the induction at 3^b preserves the earlier prefix and reduces the whole new suffix to 3^(b−2) times the divisors at least 9 in 2^a·9: j≤b−3 cannot reach 3^b since 2^a≤16<27. The predecessor is 2·3^(b−1) for a≤2 and 8·3^(b−2) for a≥3, making the bridge valid; the four base/suffix rows check by subtraction. For b=1 each binary shell has entries 2^h and 3·2^(h−1) before the final 3·2^a. For b=2,a≥3 the three contributions in complete shells come from 1,9,3 times powers of two, and the four stated remaining tail values account for all top-end exponent choices. Their connecting gaps are divisors, with a=1,2 already covered. When a≥5,b≥3, j∈{0,1,2,3} gives no 2^i3^j in (27,32), and j>3 is too large; gap 5 fails independently of exponents. Independent replay: python3 /workspace/review-evidence/check_frozen_math.py 4 used a divisor sieve, not a parametrized exponent list, to check all 21,062 two-prime-support integers up to 60,000 (including odd cases); 57 qualified, all as predicted. The unbounded proof is independent of both this and the frozen finite script.

## originality

PASS

The divisor-gap predicate, equivalent zero-test and known unit-exponent subfamilies are already documented and should not be claimed. The distinct contribution supported by the checked sources is the unbounded exactly-two-prime classification, including the separate sharp ternary boundaries and necessity of the precise Fermat-prime relation in the other branch.

## value

PASS

A complete classification on the natural exactly-two-prime slice of a documented arithmetic property yields a uniform obstruction and a sharp exponent boundary, and ties the nonternary branch to Fermat primes. This supersedes finite membership checks on a substantial slice without asserting any result about the infinitude of Fermat primes or support size three and larger.

The dated certificate retains the supplied scientific assessment, sources and limitations.
