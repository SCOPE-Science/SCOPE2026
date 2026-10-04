# Same-model review

## Correctness

PASS. The published Hessian-corrected heavy-ball update was reduced exactly on every eigenvector of an SPD quadratic. The resulting second-order polynomial has necessary-and-sufficient Jury conditions that simplify to the stated modal inequalities and, uniformly over the spectrum, to the single sharp budget \(L(\beta+2\theta)<2(1+\alpha)\). Characteristic-root products and discriminants give the complete modewise optimal-rate law. The matched-curvature parameters make both recurrence coefficients vanish exactly.

The bundled checker independently evaluates these algebraic identities and representative roots. It is supporting evidence only; the proof in `RESULT.md` is the quantified argument.

## Originality

PASS. The recent primary article was inspected at the algorithm, convergence-theorem, and parameter-discussion level, with targeted searches for spectral and quadratic specializations. It defines the same correction but does not state the exact SPD stability budget, the effective-momentum phase diagram, or matched-curvature one-update cancellation.

The foundational gradient-difference Hessian-damping paper was also inspected and uses different inertial recurrences. Targeted published-research database searches for the derived formulas and aliases found no equivalent statement; the closest exact result concerns classical heavy ball without Hessian correction.

Residual risk remains that an elementary equivalent scalar calculation exists in older inertial literature under different notation.

## Value

PASS. Hessian correction is the main added degree of freedom of the source method. The exact quadratic analysis shows that it is literally curvature-dependent momentum cancellation and quantifies its stability price. This explains when correction can remove inertia completely, when it over-corrects into negative effective momentum, and why broad sufficient parameter restrictions can be conservative on quadratic geometry.

Same-model review: passed. Independent audit: not yet performed.
