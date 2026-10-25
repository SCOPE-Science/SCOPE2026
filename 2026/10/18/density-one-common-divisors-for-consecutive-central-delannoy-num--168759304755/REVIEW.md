# Independent mathematical audit

## correctness

PASS

The Delannoy formula D_n=Σ_k binom(n,k)^2 2^k obeys Lucas digit factorization modulo any odd prime p, including zero padding. End digits D_0≡D_{p−1}≡1, while the Legendre recurrence (j+1)D_{j+1}=3(2j+1)D_j−jD_{j−1} rules out adjacent zero digits 1≤j≤p−2. Adding 1 changes trailing (p−1) digits to zero and one first changed digit; adjacent roots impossible, so both D_n and D_{n+1} vanish iff an unchanged higher digit lies in Z_p. Unique position r of first non-(p−1) digit gives exception count E_p(L)=1+(p−1)Σ_{h=0}^{L−1}(p−z_p)^h exactly. For p≡3 mod4, m=(p−1)/2 odd and the Deuring-type binomial polynomial H_m(X)=Σ binom(m,j)^2 X^j solves a mod-p ODE invariant under X↦1−X; uniqueness by initial coefficient gives H_m(1−X)=−H_m(X), and H_m(−1)=0 by paired terms, so H_m(2)=D_m≡0. Thus z_p≥1; exceptional counts O_p(N^{log_p(p−z_p)}) at arbitrary N have density zero, and choosing arbitrarily large primes 3 mod4 proves gcd(D_n,D_{n+1})→∞ in natural density. Independent direct binomial Delannoy evaluation and prime-base digit simulation tested primes 3,5,7,11,13,19 and complete blocks up to 50,000, agreeing with all formulas. Finite checks support, not replace, proofs of infinite density.

## originality

PASS

Best-of-knowledge mathematical-implication comparison: evaluated exact final statement against identified source claims, known ingredients and search aliases; where full primary texts are inaccessible only their actually inspected portions are assessed, and priority risks are stated, not hidden. The identified available sources do not establish a covering statement of the full final claim.

## value

PASS

It is a strong concrete arithmetic property of a classical combinatorial sequence: successive central Delannoy terms share arbitrarily large divisors for almost all indices, despite sharp local root restrictions. The exact exceptional set cardinality and fractal exponent for each prime are natural local statistics, connecting Lucas factorizations with additive carries and a polynomial symmetry. Neither a single finite gcd table nor routine rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
