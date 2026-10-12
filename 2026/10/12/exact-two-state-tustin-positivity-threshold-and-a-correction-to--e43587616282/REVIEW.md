# Self-review

## Correctness
PASS. For Hurwitz Metzler \(A\), the matrix \(I-hA/2\) is a nonsingular \(M\)-matrix and
\[
T_h=2\left(I-\frac h2A\right)^{-1}-I.
\]
Thus only diagonal entries can obstruct positivity. In two states, exact inversion reduces positivity to two quadratic inequalities whose conjunction is
\[
\alpha^2-|a-d|\alpha-(ad-bc)\ge0.
\]
Solving this inequality gives the displayed sharp \(h_\star\). The exact diagonal counterexample satisfies the published determinant-only condition but has a negative Tustin diagonal entry.

The embedded exact-rational verifier reproduces the counterexample, the coupled threshold example, and the resolvent identity.

## Originality
PASS. The 2010 source contains the correct two-state matrix formula but then asserts an insufficient determinant-only condition. It does not state the corrected iff threshold or the unbounded coupling-dependent improvement over its later safe bound. The 2012 follow-up retains a correct conservative general condition and, in the inspected full text, does not give the exact two-state correction. General Cayley-transform literature inspected supplies algebraic context without the control-discretization threshold.

Targeted semantic and literature searches using Tustin, Cayley, first-order diagonal Padé, Metzler positivity, determinant tests, and resolvent-diagonal terminology found no implication-equivalent corrected theorem. Residual risk remains that older matrix-positive literature uses another parametrization.

## Value
PASS. Positive-system simulation needs both stability and nonnegative state propagation. The exact threshold directly improves sampling-time selection, corrects a false local sufficiency statement in foundational Padé-positive-systems work, and shows that the retained conservative diagonal bound can lose an arbitrarily large factor when positive coupling is strong.

## Closest literature and limitations
The closest direct source is the 2010 Zappavigna--Colaneri--Kirkland--Shorten paper; the closest later treatment is their 2012 article. The closed form is two-dimensional. In higher dimensions the exact resolvent-diagonal criterion is proved, but no scalar entry formula is claimed. Higher Padé orders and nonlinear or time-varying positive systems are outside scope.

Self-review: passed. Independent audit: not yet performed.
