# Review

## Correctness

PASS. The growth coupling gives exact update identities for leaf count and total path length. Conditioning on the uniformly selected parent turns its depth into \(P_n/n\), its leaf indicator into \(L_n/n\), and their product into \(Q_n/n\). The two covariance terms involving the old tree cancel exactly.

The remaining auxiliary expectation \(q_n=\mathbb E Q_n\) satisfies a closed first-order recurrence. Solving it gives \(q_n=\frac n2H_{n-1}-\frac{n-2}{4}\), and substitution makes the covariance decrement exactly \(-1/4\) at every step. The base case is deterministic.

The packaged checker independently enumerates every recursive tree through \(n=10\) and verifies all displayed finite identities with rational arithmetic.

## Originality

PASS, with a residual risk from older recursive-tree literature. Dobrow--Fill treat total path length, Zhang treats leaf count, and the full Leckey--Neininger manuscript treats both leaves and internal path length in the same broader Hoppe-tree paper. In that full manuscript the two quantities are analyzed in separate sections, and targeted searches found no covariance or joint-law statement.

Lundblad--Wagner's work treats path length together with the sum of leaf depths, which is the auxiliary bridge used here, but its stated result compares average depths rather than leaf abundance against total path length.

## Value

PASS. Leaf count is a canonical fringe-size statistic, while total path length is the canonical recursive-tree search cost. Their interaction is mathematically motivated and algorithmically interpretable.

The identity is stronger than a sign calculation: every growth step contributes the same \(-1/4\) covariance increment. The exact linear-projection slope tends to \(-3\), quantifying how leaf-rich fluctuations align with reduced global search cost even though standardized correlation tends to zero.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK sizes=9 trees=409113 first_moment_checks=27 covariance_checks=9 leaf_variance_checks=8 slope_checks=8`.
