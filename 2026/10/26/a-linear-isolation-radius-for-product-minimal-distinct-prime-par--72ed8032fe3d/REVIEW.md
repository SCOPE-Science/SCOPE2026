# Independent mathematical audit

## correctness

PASS

Let A≠empty be product-minimal at sum s, M=product A, H=ceil(5M/2). For any candidate B with sum s+q and product ≤qM, write k=|B|, b=max B, u=sum(B\{b}), R=product(B\{b}). Since b≥(s+q)/k, R≤qM/b<kM. Independently verified the universal auxiliary inequality k*u/R≤5/2 for k≥2: k=2 gives 2, k=3 max at (2,3) gives 5/2; for k≥4 first-prime extremizers and F_m=(m+1)S_m/P_m, F_3=4/3 with F_{m+1}/F_m<1, close all larger cases. Thus u<5M/2, and with s≤M, |b-q|=|s-u|<5M/2≤H; isolation forces b=q. Product-minimality and unique prime factorization force B=A∪{q}; k=1 also follows with u=0. Independent combinations of first 12 primes through k=7 verified the sharp auxiliary maximum 5/2 as supplemental finite check only.

## originality

PASS

Campbell arXiv:2610.19534 Lemma 2 obtains product-minimality preservation after adjoining a prime isolated in width 4M²; the reviewed proof replaces the product-based estimate by a sum bound giving width ceil(5M/2), linear in M. Campbell Lemma 6 features an 11M gap for a DIFFERENT complementary max-product construction, so it does not itself establish the same equal-sum product-minimal extension. The new inequality strengthens a natural proof ingredient rather than repeating the published theorem with a renamed constant.

## value

PASS

Replacing the quadratic isolation width by a universal linear radius in the central distinct-prime product-minimization extension lemma is a mathematically motivated sharp-order improvement in an existing construction; no claim of an effective least prime or optimal 5/2 coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
