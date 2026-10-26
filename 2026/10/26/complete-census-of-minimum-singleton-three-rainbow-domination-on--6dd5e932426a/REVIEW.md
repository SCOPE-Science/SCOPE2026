# Scientific review of the prism minimum-function census

## Correctness — PASS

The proof applies to every integer \(n\ge3\). Cubic neighborhoods force the uncolored vertices to form an independent set and permit at most one uncolored vertex per rung. For deficits of zero, one, or two, the uncolored support is exhausted by its empty rungs and alternating runs. A directly derived \(3\times3\) two-terminal color kernel counts the precise positive colorings of each run, including length one and length two. The analysis separately treats adjacent holes, nonadjacent holes, odd circumference, and even circumference. Matrices are multiplied only where endpoint-color constraints require them, and every pair of holes is counted once in the final formulas. Small graph cases are included rather than extrapolated. The complete minimum-number formula follows by locating the first positive coefficient, without relying on an external minimum-weight theorem.

Exact direct graph enumeration and an independently implemented constraint-graph color counter match the displayed coefficients in all tested orders. These finite computations are checks, not the infinite argument.

## Originality — PASS, subject to bibliographic uncertainty

The closest primary source is Lange, arXiv:2610.06906v1, Theorem 19 and its proof. It gives the **minimum weight** in the identical singleton model on the identical graph family, but no number of optimal functions, and does not determine the next two coefficients of the weight distribution. Its Theorem 7 describes the equality structure for regular graphs, not the full near-extremal color multiplicities. Those earlier results alone cannot imply the formulas at weights \(n+1\) and \(n+2\), and the present combinatorial run-kernel argument supplies the missing count.

Žerovnik's 2026 cylindrical-graph study provides bounds and constructive examples rather than the same coefficient formulas in its accessible sections. A 2026 exact prism-dominion article instead enumerates **ordinary dominating sets** and has a modulo-four, not modulo-six, classification. Related Roman domination on complete-clique prisms concerns different labels and a different graph. A targeted search of scholarly indexing and public mathematical-result records found no equivalent formula. This does not establish publication priority; the complete Žerovnik PDF could not be checked, and unindexed results remain a risk.

## Mathematical value — PASS

The new formulas resolve an intrinsically motivated refinement of a recently determined minimum parameter: how many named-color configurations attain the optimum, for every circumference. The theorem provides a full extremal classification and additionally determines the two adjacent weight layers for all circumferences. It distinguishes three growth regimes—constant, linear, and quadratic—via a transparent finite local kernel. These are cardinalities of naturally defined optimizing objects, not arbitrary graph indices or merely small finite tables.

## Limitations and relationships

Weights above \(n+2\) are not covered; the classical multicolor-per-vertex rainbow model is not covered. Literature comparisons are best-knowledge, not an independent bibliographic or mathematical audit. No claim of independent mathematical validation is made.

Self-review: passed. Independent audit: not yet performed.
