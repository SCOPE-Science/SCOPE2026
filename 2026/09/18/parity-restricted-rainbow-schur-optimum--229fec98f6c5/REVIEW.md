# Review: parity-restricted optimality for rainbow Schur triples

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** For even \(n=2m\), the rainbow count in the stated coloring class reduces exactly to
\[
2\bigl(a(m-a)+\operatorname{cut}_{H_m}(A)\bigr),
\]
where \(H_m\) has edges \(\{i,j\}\) exactly when \(i<j\) and \(i+j\le m+1\). The two terms correspond respectively to Schur triples with exactly one odd summand and with two odd summands. The correspondence was checked in both directions, including ordered-pair multiplicity and the condition \(i+j\le m+1\).

The fixed-cardinality cut function has the exact two-step recursion recorded in RESULT.md because vertex 1 is universal, vertex \(m\) is adjacent only to 1, and deleting both leaves \(H_{m-2}\). Substitution of the piecewise quadratic comparison function into this recursion gives Bellman residual of magnitude at most \(1/2\); the only transition is one integer wide around \(a=m/3\), and all three residue classes of \(m\bmod3\) are listed explicitly. Induction therefore gives the uniform \(O(m)\) error bound. The remaining optimization is a direct quadratic calculation with unique maximizers \(5/11\) and \(6/11\) and value \(9/22\).

The lower construction is independently recounted by a direct lattice-area count, so the conclusion does not depend on assuming optimality of the motivating construction. Exact rational computations in `artifacts/verify.py` compare the recursion to brute force on small graphs, test the Bellman residual and error inequalities through \(m=1000\), and confirm finite extrema converging to \(9/22\). These computations support, but are not substitutes for, the general proof.

## Originality

**PASS, to the best of our knowledge.** Hegde--Kumar--Pratibha, arXiv:2609.18474 (submitted 16 September 2026), was inspected through its full arXiv HTML rendering. It proves unrestricted asymptotic bounds \(9/22\) and \(8/15\), gives the parity-and-interval lower construction, and explicitly asks whether the unrestricted optimum is \(9/22\). It does not state optimality under the broader condition that all evens have one color and all odds use the other two arbitrarily.

Searches covered exact and synonymous formulations involving rainbow Schur triples, \(9/22\), the \(4/11\) and \(10/11\) breakpoints, parity colorings, monochromatic evens, odd/even restrictions, anti-Ramsey Schur problems, threshold graphs, and maximum cuts. The Parczyk--Spiegel 2026 paper was also checked at its journal abstract/bibliographic level; its lower bound is the earlier \(0.4\) construction and it predates the \(9/22\) result. No source located gives the fixed-cardinality threshold-graph reduction, the piecewise asymptotic cut profile, or the resulting parity-restricted \(9/22\) theorem.

The motivating arXiv preprint is extremely recent, so an unindexed contemporaneous follow-up remains a genuine residual originality risk. No highly matching inaccessible paper was identified whose unseen contents specifically threaten the claim.

## Value

**PASS.** The current unrestricted problem has a substantial gap between \(9/22\) and \(8/15\). This result rules out an entire natural and very large class of potential improvements: arbitrary rearrangements of the two odd colors cannot beat \(9/22\) if the evens remain monochromatic in the third color. The exact reduction also supplies a reusable threshold-graph optimization framework and a stability constraint on near-extremal color balances. It is therefore more than an optimization of the original two-breakpoint ansatz while remaining a precise partial advance rather than a claim to solve the unrestricted problem.
