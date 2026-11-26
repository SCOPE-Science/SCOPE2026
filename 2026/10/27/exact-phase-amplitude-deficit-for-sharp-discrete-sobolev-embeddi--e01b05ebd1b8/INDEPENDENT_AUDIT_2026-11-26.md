# Independent mathematical audit

## correctness

PASS

Zero extension makes the full rectangular difference matrix injective (its first d rows are unit lower triangular), and Vandermonde gives the stated Gram entries. Conjugating by alternating signs gives the binomial path matrix. For a complementary cofactor with one source and one sink removed, match the remaining endpoints in increasing order. The relative offsets r_k-c_k are identically zero except for one block on which they are all +1 or all -1; in particular both signs never occur in the same cofactor. The specified schedule with a common first α-1 steps and up to two final advances cannot exchange paths: offsets that differ by one change the neighboring gap only once, and the source and sink gaps are both positive. No other endpoint permutation can be disjoint in this monotone time-position graph. Hence the path determinant is strictly positive; the two Cramer signs cancel after conjugation. For an independent constant check let v_j=binom(j+α-1,α) binom(d+α-j,α), interpreted as a polynomial of j. It has zeros on the two length-α exterior stencil layers and leading coefficient (-1)^α/(α!)², so Qv is the constant vector binom(2α,α) times one by the centered 2α-th difference. Summing v by Vandermonde gives binom(d+2α,2α+1). For s chosen as in the claim, s* a=||a||_1 and q>0; the energy projection coefficient onto Gs is u/q. Subtracting the projection yields qE-u², while C²-q is exactly the positive-weight pairwise phase energy. Equality forces a common phase and an exact projection, and the positive vector G1 shows the converse including zero. For a nonzero input the complete-graph sum is d²-|sum s|² and the distance to a common phase is 2(d-|sum s|), which proves the stated bound for every choice of phases at zero entries.

## originality

PASS

The sharp constant and a Landau extremizer are prior, and finite Toeplitz inverse formulas already cover the matrix as a special case. Neither is credited as new. The dated later Resultary record 3240556c60ce is a separate, mathematically equivalent statement of the central identity, not merely a similar title. Its available Nov. 1 catalogue provenance is later than the frozen Oct. 27 record and supplies no evidence that the equivalent formula predates the frozen result. The available earlier primary statements do not furnish the exact phase-sensitive deficit or its phase-stability conclusion. The pass is limited to that refinement and does not certify priority or independent discovery relative to the later match.

## value

PASS

At the known sharp endpoint the inequality alone does not measure how a complex sequence fails to attain equality. The exact weighted phase energy and the orthogonal energy residual distinguish phase misalignment from failure to lie on the phase-conditioned representer, for all support lengths and difference orders. Positivity makes the former a genuine full-coordinate rigidity test and produces an explicit all-input phase estimate, including arbitrary phases at zero coordinates. This is useful structure for near-extremizers, beyond computing the constant or just checking the published extremizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
