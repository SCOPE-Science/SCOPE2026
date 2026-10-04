# Review

## Correctness

PASS. With a constant gradient and frozen orthogonal basis, the SOAP first and second moments converge to the constant signal and its coordinatewise square. The stationary update is therefore exactly the entrywise map \(z\mapsto z/(|z|+\varepsilon)\) in that basis. For the canonical \(45^\circ\) family, the update has the symmetric form with eigenvalues \(p+r\) and \(p-r\), giving the exact condition-number law. The fresh-basis spectrum and general angle threshold follow by direct diagonalization and rotation.

Risk: this is a stationary-gradient spectral statement, not a nonlinear convergence theorem.

## Originality

PASS. The defining SOAP paper reports worse behavior with infrequent eigenbasis recomputation, and a later large-scale study directly attributes loss spikes and divergence to stale preconditioner statistics. The inspected full texts do not state the stationary rank-one limit, the exact \(\kappa+(\kappa^2-1)/(2\varepsilon)\) law, or the half-saturation angle. Focused published-record searches found no implication-equivalent SOAP theorem.

Residual risk: an equivalent short derivation may exist in unindexed implementation notes.

## Value

PASS. The exact law concerns two defining SOAP design choices: eigenbasis freshness and Adam's epsilon floor. It shows that their interaction is singular rather than perturbatively small and quantifies the angular scale at which a stale off-diagonal coordinate becomes order one. This gives a concrete spectral mechanism aligned with independently reported stale-preconditioner instability without overclaiming global causation.

Same-model review: passed. Independent audit: not yet performed.
