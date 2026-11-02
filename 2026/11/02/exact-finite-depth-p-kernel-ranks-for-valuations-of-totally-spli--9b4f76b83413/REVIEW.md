# Review of exact finite-depth \(p\)-kernel rank theorem

## Correctness — PASS
For each \(j\), only the \(d\) residue branches containing Hensel roots give variable subsequences; other branches are constant, and depth two provides the constant-one sequence. A rational affine map sending one algebraic root of an irreducible polynomial to another must permute all conjugates; a positive power of \(p\) cannot act with finite order unless the multiplier is one. The resulting tail roots and original roots are pairwise distinct. Approximating each root independently by nonnegative integers forces linear independence of all \(de+2\) generators. The proof explicitly handles depths \(0\), \(1\), and \(e\ge2\) and contains no finite-to-infinite inference. The standalone finite checker corroborates the ranks for degrees two and three.

## Originality — PASS, qualified
Bell (2007), Theorem 1.2 and Proposition 3.2, already proves non-\(p\)-regularity from irrational \(p\)-adic roots and explicitly mentions \(\nu_5(n^2+1)\). Medina–Moll–Rowland (2015), Theorem 2.1, gives periodicity/unboundedness rather than finite-depth rank. Shu–Yao (2011) and Sobolewski (2023) give broader regularity classifications. The checked portions do not contain the exact cumulative depthwise rank \(de+2\) or the degree-slope result. The distinguishing claim is the all-depth exact finite-dimensional invariant and its explicit independent generating family, not nonregularity itself. Related historical records about Hensel roots, but not valuation-kernel dimensions, were found. It remains possible that an unlocated paper or unstated specialization of Bell's construction obtains this formula.

## Mathematical value — PASS
The rank of the span of kernel subsequences at bounded digital depth is a natural quantitative invariant of nonregularity. A qualitative infinite-rank theorem does not determine its finite-depth rate. The finding identifies the rate *exactly*, for a degree-\(d\) family with arbitrary totally split good primes, rather than reporting a single small example. It supplies explicit bases and identifies the arithmetic reason that distinct digit tails never collide, allowing level-by-level comparison of computational resources for sequences with different algebraic degrees. This is a structural quantitative refinement, not a new proof of Bell's original qualitative result.

## Residual risks and boundaries
The independent audit is not performed. The originality assessment is relative to accessed primary documents, accessible historical claims, and published indexed records, not a universal uniqueness certificate. Ramified or reducible cases are unproved. The finite-field sample-rank script is corroboration only.

Self-review: passed. Independent audit: not yet performed.
