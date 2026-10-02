# Independent mathematical audit

## correctness

PASS

The rank-transfer proof reconstructs directly. For a nonzero computation-code word a=uG, choosing a B-basis alpha_1,...,alpha_r of the B-span of its coordinates expresses every reused leakage g_j(a_i c_j) as a B-linear combination of the r base-share leakages g_j(alpha_l c_j). Feeding the product decoder the one-dimensional family (u_1 c,...,u_K c) therefore recovers a nonzero scalar multiple of c_0 from at most r B-symbols per share. For the systematic one-output code, rank one is exactly a nontrivial B-relation among the coefficient classes mu_i+B in F/B; independence excludes rank one and a generator row supplies rank two. The K>=m, quadratic-extension, and LFSR consequences follow from dimension and scalar-invariance of B-span. The finite verifier is only corroborative and is not used as the infinite proof.

## originality

PASS

The motivating Aoutouf--Augot paper proves the identical-leakage collapse for simple addition and reports simulations for weighted relations and LFSRs, but its complete v1 does not state the minimum-row-subfield-rank transfer theorem or the quotient-space classification. The earlier 18 September SCOPE stabilizer-field result covers computations whose entire coefficient matrix descends to the leakage stabilizer field, not the more general obstruction obtained from a single low-rank computation-code word. A very close column-subfield-rank SCOPE theorem was published later on 19 September; repository chronology places the audited record at 03:27:56 UTC and that later record at 17:29:57 UTC, so it is not prior coverage.

## value

PASS

The result isolates a natural computation-code invariant that turns a product-code leakage attack into a quantitative base-code repair obstruction and gives a sharp one-output classification. It explains the simple-addition and LFSR boundary in one mechanism and rules out apparent weighted-relation gains in entire extension-degree regimes. This is a motivated structural boundary, not a parameter renaming or finite lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
