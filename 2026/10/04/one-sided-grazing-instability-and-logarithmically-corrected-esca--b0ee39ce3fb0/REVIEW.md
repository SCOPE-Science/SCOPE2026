# Same-model review

## Correctness
PASS. Under the stated sign assumptions and boundary equality, the source return map has \(R(A)=0\), while the explicit upper and lower flight times are both positive. The boundary orbit reaches the lower threshold tangentially at \((0,-\mu)\). Signed distance reduces the return map exactly to
\[
u^+=\sqrt{u(u+2\rho)}.
\]
This recurrence is strictly expansive for every \(u>0\), and its exact increment yields
\[
u_n=\rho n-\frac{\rho}{2}\log n+C+o(1).
\]
The proof is analytic and does not extrapolate from finite computation.

## Originality
PASS. The motivating paper explicitly removes \(R(x^*)=0\) from its differentiable stability argument and says the singular boundary requires separate analysis. Its later qualitative statement that visible-fold cycles are repulsive does not provide the singular normal form or an escape rate. Focused indexed-literature searches for the source, boundary equality, exact recurrence, grazing aliases, and logarithmic escape found no implication-equivalent record. Full text of the closest classical square-root-map paper was inspected; it develops generic grazing square-root bifurcation structure but does not contain this model-specific recurrence or the \(-\rho\log n/2\) correction.

The closest literature is the Nordmark/square-root grazing-map theory, especially doi:10.1088/0951-7715/23/2/012 and doi:10.1137/120884286. Those works make the square-root singularity itself expected, so the novelty claim is limited to the exact boundary reduction and sharp long-iterate escape law.

## Value
PASS. The parameter equality is a natural bifurcation boundary where the source says its usual derivative criterion fails. Determining the actual one-sided dynamics there closes a specific gap in the phase portrait, and the logarithmically corrected linear escape rate quantifies the singular instability rather than merely relabeling it.

## Limitations and residual risk
The theorem is confined to the affine model, the returning branch, and the exact singular equality. It does not prove robustness of the logarithmic correction under smoothing, nonlinear perturbations, or noise. An equivalent recurrence calculation could be hidden in unindexed nonsmooth-dynamics literature, although targeted exact-form and alias searches did not find one.

Same-model review: passed. Independent audit: not yet performed.
