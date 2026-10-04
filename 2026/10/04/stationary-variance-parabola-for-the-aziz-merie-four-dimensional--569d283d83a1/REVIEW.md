# Review of Stationary variance parabola for the Aziz–Merie four-dimensional flow

## Correctness
PASS. The proof uses only invariant-measure generator identities that are valid on compact support, followed by exact algebra. The endpoint cases are handled separately: the lower endpoint collapses the invariant support to the origin, while the upper endpoint would force a nonzero fixed-sign \(x\) and hence unbounded monotone drift in \(w\), contradicting compactness. The symbolic checker independently replays every Lie derivative and the exact rational source-parameter constants.

## Originality
PASS. Full-text inspection of the introducing 2020 article and the 2021 same-system circuit paper did not locate a stationary moment identity, invariant-measure variance law, or the strict mean-square bound. Equation- and alias-based searches returned closest results for other flows, including Rössler, Rabinovich–Fabrikant, and Halvorsen systems. Those results demonstrate related techniques but do not imply this vector-field-specific chain or coefficients. Residual risk remains that an equivalent derivation exists in poorly indexed literature.

## Value
PASS. The variance parabola is a global statistical constraint applying to every compact stationary regime of the flow. Its strict endpoint analysis distinguishes the equilibrium measure from any nontrivial recurrence and supplies an exact benchmark for simulations or circuit realizations. The statement does not rely on a single numerical orbit.

## Closest literature and limitations
The closest retrieved literature contains invariant-measure moment laws for other classical flows, not this one. The theorem is necessary rather than existential: it does not prove that a nontrivial invariant measure exists, is unique, is ergodic, or is chaotic, and it does not describe the full attractor. Extension beyond compact support would require separate integrability hypotheses.

Same-model review: passed. Independent audit: not yet performed.
