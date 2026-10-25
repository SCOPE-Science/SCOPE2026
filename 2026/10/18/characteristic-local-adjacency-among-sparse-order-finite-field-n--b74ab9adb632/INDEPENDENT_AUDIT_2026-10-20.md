# Independent mathematical audit

## correctness

PASS

Write F_q^×=<g> of order 2^a l. Nonsquare iff exponent k odd, nonprimitive then iff l divides k; these are exactly primitive 2^a-th roots, roots of x^(2^(a-1))+1, all split and squarefree over F_q. Pair count is degree of gcd with the shifted polynomial computed over prime field F_p; irreducible factors are shared exactly over algebraic closure and here all roots already split in F_q. Exact integer resultants for a=1..4 are 1,5,153,1051779953=7²·17⁴·257; modular monic gcd degrees for possible p are (5:1),(3:2,17:1),(7:2,17:4,257:1). Fresh independent symbolic resultant and modular gcd computations reproduced all factors/degrees. The valuations v2(p^f−1) with the primality of (q−1)/2^a eliminate p=3,17 for a3 and p=257 for a4; factorization eliminates p=7 except q=49. The remaining p=5 or 17 families require odd f and prime l; f=1 excluded. The inspected `check.py` also directly computes q49,125,4913 and zero examples, but no infinite assertion relies on those finite fields.

## originality

PASS

The integral shifted-binomial resultants are known in OEIS A255831 and q49 two-pair case was in Cohen. Cohen establishes general positive existence under primitive-density theta<=1/3, while this single-prime case has theta=(l-1)/(2l)>1/3 for l>=5, so the main published bound does not determine the q125/q4913 sparse classes or exact pair counts. The proposed contribution is characteristic-local gcd identity tied to the NSNP condition, modular gcd ranks and all-field sieve at a<=4, not resultant numbers in isolation.

## value

PASS

A sharp natural sparse-multiplicative-order classification of additive adjacency in finite fields turns a difficult general primitive-root density question into a local algebraic congruence computation, identifying genuine exceptional arithmetic families and a universal gcd formula. Finite cutoff a<=4 is the first complete set of low two-adic strata, motivated by manageable resultants rather than arbitrary fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
