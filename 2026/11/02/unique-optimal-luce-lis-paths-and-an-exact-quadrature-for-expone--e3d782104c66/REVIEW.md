# Self-review

## Correctness — PASS

The new claim specifies the full admissible class, fixed \(\beta\ge0\), and the original \(2\sqrt n\) probabilistic normalization. The bounded variable \(y=1-e^{-e^{-\beta t}u}\) converts the functional to \(\int\sqrt b\) with BV identity \(dy=(b-\beta g(y))dt+d\nu\), where \(\nu\ge0\) is singular. The root \(C_\beta\) exists and is unique by the strict shooting integral. Along the constructed curve, \(p'=\beta pg'\) and both square-root and \(g\) tangent inequalities reduce every competitor's deficit to three nonpositive boundary/singular terms. Equality implies the same ODE and thus the identical curve. The endpoint expansions follow by the implicit-function theorem and a direct inequality. The 249 passing numerical assertions test calculations but do not substitute for the argument. A priori reliance on the underlying established probabilistic LIS variational theorem is explicit.

## Originality — PASS with historical qualification

Borga–Dubach (arXiv:2610.30382v1, full HTML, §3.4) give the variational principle and expressly say existence, uniqueness, and a plausible maximizing formula are unresolved; they do not calculate an exact value for exponential weights. Their bound for the same \(f_\beta\) is not equivalent to an optimizer or upper bound. Borga–Chatterjee–Diaconis (arXiv:2509.07729) obtain Luce permuton and statistical limits but not the solved variational problem. Deuschel–Zeitouni (arXiv:math/9803035) address generic i.i.d. increasing subsequences and large deviations, not this specialized calibration. Semantic mathematical-record searches for Luce optimal paths, exponential-weight LIS constants and quadrature found no equivalent theorem; checked earlier claims also lacked one. An unlocated abstract optimal-control result may overlap with the method, and independent publication priority remains unverified.

## Mathematical value — PASS

This resolves a natural concrete subcase of a problem explicitly stated open in a recent primary paper. It identifies the optimizer uniquely **within the original unrestricted class**, computes the actual LIS constant with a scalar integral, and gives sharp small- and large-parameter information for naturally arising Mallows-like exponential weights. Its importance does not depend on claiming a general-weight solution or finite-LIS geodesic concentration.

## Boundaries and residual risks

The proof is rigorous only for fixed exponential weights with nonnegative exponent. The global calibration and BV singular-measure term must both be retained; solving only Euler–Lagrange equations would not establish global uniqueness. The primary recent manuscript was inspected in full through its lawful open HTML rendering. Other historical variational-optimal-control frameworks may share ingredients and deserve specialist priority review.

Self-review: passed. Independent audit: not yet performed.
