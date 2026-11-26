# Independent mathematical audit

## correctness

PASS

Straub's Jacobsthal lemma gives the valuation bound for the ratio with a=p^(r−1), b=j and 1≤j<a. Writing s=v_p(j), both j and a−j have valuation s, so for p≥5 the ratio differs from 1 by a multiple of p^(r+2+2s). Lucas gives v_p(binomial(a,j))=r−1−s; the difference of the cubes is divisible by p^(4r−1−s), at least p^(3r+1) since s≤r−2. Endpoints cancel and at r=1 they comprise the entire divisible-index sum. For p∤k, Lucas gives binomial(p^r−1,k−1)≡(−1)^(k−1) (base-p digit parity); the normalized cubic terms contribute (−1)^(k−1)/k³. For k=ap+b the alternating sum over the odd number p^(r−1) of block signs is 1. The full reciprocal cube sum is zero modulo p, so the alternating sum is −1/4 times the half-range sum. The p-integral Bernoulli polynomial power sum with m=p−3 gives [B_m(1/2)−B_m]/m; since 2^(1−m)≡8, that is −2B_m. This yields the asserted B_(p−3)/2 and the divisibility and exact-valuation dichotomy, including the p=5 boundary.

## originality

PASS

Credit Straub for cubic prime-power divisibility and Aeran Kim for the exact r=1 Bernoulli digit, which the frozen comparison should acknowledge. The supported distinct claim is the uniform first digit of the successive differences at precision p^(3r+1), extending the prime-index case to every tower step. An overlapping indexed theorem gives the weaker fixed modulus p^4 for each term relative to 2. Neither of those statements nor their combination with cubic divisibility determines the first digit at r≥2.

## value

PASS

This measures sharpness of a classical prime-power supercongruence rather than testing an arbitrary modulus: the first possible nonzero digit is the same at every height, and the p^(3r) bound is exact simultaneously for every height at all non-Wolstenholme primes. At a Wolstenholme prime the improvement occurs at every height. The relation of the exception to a classical Bernoulli invariant is a usable uniform arithmetic distinction and is not obtained from the fixed p^4 prime-power residue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
