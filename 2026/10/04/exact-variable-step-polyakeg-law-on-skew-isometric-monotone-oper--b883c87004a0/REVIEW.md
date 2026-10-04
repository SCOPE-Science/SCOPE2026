# Same-model review

## Correctness

PASS. The proof uses only the defining PolyakEG formulas and the identities \(J^T=-J\), \(J^TJ=I\), hence \(J^2=-I\). The projection step-size, update matrix, norm factor, critical-condition ratio, finite product, and the square-summability criterion are all derived explicitly. The only infinite-step implication is reduced to the elementary two-sided comparison between \(\log(1+u)\) and \(u\) on a bounded interval.

The bundled exact-rational checker verifies representative canonical-block instances and a multi-step product. Those computations are supporting checks; the quantified proof is algebraic and does not rely on finite experimentation.

## Originality

PASS. The primary 2026 PolyakEG paper was inspected in full. It defines the update and gives generic sublinear best-iterate residual bounds for merely monotone problems, with linear convergence derived under strong monotonicity. Its introduction uses a planar rotation as the canonical example of rotational difficulty, but no exact PolyakEG trajectory law, product formula, or square-summability criterion was found.

The known projection correction predates the paper. Publisher material for Solodov--Svaiter and a bibliographic/abstract record for Tseng's linear-convergence work were checked as broader prior coverage. Those sources establish general projection-method convergence principles, not the exact variable-step formula claimed here.

The two closest published-finding corpus records were inspected in full. One solves a degree-two minimax problem for unequal-step classical extragradient on normal strongly monotone systems; the other optimizes a reflected forward-backward recurrence on skew rotations. Their update maps and implications are different and do not subsume this claim.

Residual risk: specialized older linear-operator literature may contain an equivalent formula, and full theorem-level text of every historical projection-method paper was not available.

## Value

PASS. The skew-isometry class is the natural higher-dimensional form of the planar rotation used throughout monotone root-finding as the canonical non-gradient mode. The finding gives a complete exact trajectory law at this non-strongly-monotone boundary and identifies the sharp variable-step convergence threshold. It also distinguishes nonsummable from square-nonsummable decay schedules, which is directly relevant to adaptive and decreasing-step designs.

The result is not presented as a worst-case theorem for all monotone operators, nor as a replacement for the general source theorem. Its value is a sharp structural benchmark that exposes behavior hidden by the generic \(O(1/K)\) best-iterate estimate.

Same-model review: passed. Independent audit: not yet performed.
