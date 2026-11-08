# Independent mathematical audit

## correctness

PASS

For every prime p, alpha>=1, n>=0, let n+1=p^r m with p∤m and R=m mod p^alpha (least positive residue). Kummer gives p-valuation of binomial(n,k) as number of base-p borrows. Since the last r digits of n are all p-1, the good/bad indicator in row n repeats the indicator of row m-1 in blocks p^r, so maximal run scales by p^r. For reduced N=m-1, its low alpha digits encode R-1. The initial R entries 0..R-1 incur fewer than alpha borrows, as do terminal R by symmetry. For any interval [K,K+R] inside row N, take Z=Q*floor(K/Q)+digitwise_max(K mod Q,R) for Q=p^alpha. Each extra digit added is bounded by its R digit so K<=Z<=K+R<=N, and subtracting Z from N forces borrow in every one of the first alpha digits. Hence no run >R, proving exact L=p^r R=(n+1) mod p^(r+alpha). Independent exact integer tests for p=2,3,5,7, alpha=1..3, n=0..160 (1,932 rows) corroborated maximal runs; the explicit all-parameter Kummer certificate, not finite enumeration, proves universality.

## originality

PASS

Best-of-knowledge PASS: classical Kummer pointwise valuation and Fine/Rowland/Spiegelhofer–Wallner survivor counts do not determine ordered maximum consecutive runs. The new digitwise universal covering lemma supplies the added result.

## value

PASS

Maximum uninterrupted stretches of binomial coefficients nondivisible by prime powers are natural structural invariants of modular Pascal rows, different from the classically enumerated number of survivors. The all-p/all-alpha sharp residue formula, endpoint witnesses and explicit divisibility witness for each longer interval answer a meaningful extremal digit-combinatorics question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
