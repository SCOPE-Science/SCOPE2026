# Self-review

## Correctness
**PASS.** For fixed \(0<p<1/2\), the entropy derivative \(L=\log((1-p)/p)\) is nonzero, so the implicit boundary \(h(t_R)=R\) is locally invertible. Expanding \(h(p)-h(p-u)\) and \(D(p-u\|p)\), reverting the first series, and substituting gives the stated cubic expansion of the phase-uniform converse. Independently, differentiating the channel-aware variational objective at \(s=0\) gives curvature \(-p(1-p)L^2\) and third derivative \(p(1-p)(1-2p)L^3\); the interior maximizer therefore has the claimed local expansion. The cubic difference reduces exactly to a positive coefficient. No finite experiment is used to establish the asymptotic theorem.

## Originality
**PASS.** The anchor paper states and proves a strict separation in its rotated-qubit example, but the inspected statement/proof does not give the order at which the gap opens near capacity. Focused searches by source identifier, formula, capacity-deficit, near-capacity, cubic, Petz/sandwiched, and moderate-deviation aliases found no implication-equivalent result. The closest broader works establish the channel-aware error exponent and the shared quadratic dispersion scale; neither supplies this cubic difference. The principal residual risk is a newly posted or differently phrased third-order note not yet indexed.

## Value
**PASS.** The result identifies the first asymptotic scale on which the source's reliability loss becomes visible. Because both exponents agree through quadratic order, standard moderate-deviation analysis cannot detect the penalty; the explicit cubic coefficient quantifies the first separation. This is a structurally motivated refinement of the source's main phenomenon rather than a routine parameter substitution.

## Closest literature and limitations
The primary anchor is arXiv:2610.01941v1. The closest broader channel-aware exponent result inspected is arXiv:2507.06232v4, and the closest near-capacity asymptotic result inspected is arXiv:1701.03114v3. The claim is local for fixed \(p\), does not cover endpoint-uniformity, low rates, or arbitrary noncommuting channel families, and does not assert an all-channel third-order invariant.

Self-review: passed. Independent audit: not yet performed.
