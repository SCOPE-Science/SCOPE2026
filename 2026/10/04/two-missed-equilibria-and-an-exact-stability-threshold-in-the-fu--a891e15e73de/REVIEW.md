# Review of Two missed equilibria and an exact stability threshold in the Fu–Cheng–Liu hyperchaotic flow

## Correctness
PASS. The equilibrium equations are solved exhaustively. The two off-origin branches satisfy the vector field identically, the origin spectrum is factored exactly, and the two branch characteristic polynomials are derived from the Jacobian. The Routh first-column signs give the exact unstable dimensions on \(0<d\le30\). The crossing value \(d_H\) is the smaller positive root of the exact Hurwitz determinant, and direct factorization at \(d_H\) isolates one simple imaginary pair while leaving the other two eigenvalues in the open left half-plane.

The proof does not infer infinite-dimensional or global behavior from finite computation. The symbolic checker is supplementary; the mathematical argument states the interval signs and the exceptional Routh denominator explicitly.

## Originality
PASS. The motivating Scientific Reports article states that the flow has a sole equilibrium at the origin and later labels \(27<d\le30\) as stable at that origin. The checked full text does not list the two off-origin equilibria, the stable interval for \(E_{-1}\), or the exact threshold \(d_H\). Exact DOI/title/equation/parameter searches and published-finding corpus searches did not locate a same-system correction or a stronger result that implies the accepted claim. The nearest published-finding corpus records concern other vector fields and therefore do not subsume this statement.

Residual risk remains that an unindexed note or thesis independently contains the same calculation. Standard Routh–Hurwitz theory is not claimed as novel.

## Value
PASS. The source presents the claimed single equilibrium as a defining structural feature and uses equilibrium stability in its dynamical interpretation and feedback-control discussion. Completing the equilibrium set changes that structure materially: a stable off-origin equilibrium exists for \(0<d<d_H\), so any other attractor in that interval cannot be globally attracting, and the source's asserted stable-origin regime is impossible because the origin always has eigenvalue \(12\). The exact threshold is a natural local invariant of the published parameter family rather than an arbitrary numerical slice.

The result does not establish a nonlinear Hopf branch, global attractor structure, or encryption performance.

Same-model review: passed. Independent audit: not yet performed.
