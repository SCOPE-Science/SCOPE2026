# Scientific review

## Correctness — PASS

All genuine two-cycles of the real map reduce exactly and reversibly to the scalar level equation \(G_B(u)=A\) in the stated range. Strict logarithmic concavity controls all roots, and the nonzero forcing derivative makes the unique maximum a fold. Explicit Jacobian multiplication and elementary inequalities certify one saddle and one sink for \(1<B\le9/8\); the asymptotic coefficient is obtained by a regular perturbation of a nondegenerate normalized maximum. `python3 verify.py` passed 2,526 finite consistency assertions; the infinite quantifiers are established analytically, not by sampling.

## Originality — PASS, with priority uncertainty

The full readable 2023 source establishes a fixed-point-free cosine–quadratic memristor map and numerically investigates its dynamics, especially for higher gains, but does not enumerate all primitive two-cycles in the weak-gain regime or prove the threshold and 3/2 onset law. The closest mathematical-record search results are about different rational, cubic and conservative plane maps and do not specialize to the present recurrence. Bao et al.'s earlier discrete memristor model has a nonempty fixed line and a different update law. Searches were compared by mathematical implication rather than labels, but unindexed equivalent statements remain possible.

## Mathematical value — PASS

A map designed to have no equilibria first can possess stable recurrent motion through period two. This result gives a complete root-level phase diagram for that naturally motivated first possible period, an explicit saddle–sink coexistence regime, and a singular opening exponent as the quadratic memristance gain passes its critical value. It provides qualitative and quantitative information not accessible from fixed-point absence or a finite bifurcation diagram.

## Boundaries

The complete period-two count stops at \(B=4/3\); stability types are proved on \(1<B\le9/8\), with no assertion of sharpness. Longer cycles, global basins, invariant chaotic sets and verified literature priority are outside the proof.

Self-review: passed. Independent audit: not yet performed.
