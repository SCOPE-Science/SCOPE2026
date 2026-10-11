# Review of Universal extremal rigidity for monotone weighted Fock Korenblum radii

## Correctness

PASS. The source's non-increasing-weight proof uses the law of \(\max(T,m_1)\) in the moment-duality theorem. If the endpoint norms are equal, every inequality in that ordered moment chain is equality. Because the measure has positive continuous mass on an interval immediately above its mean, the nonnegative Schwarz--Pick coefficient defect vanishes on an interval. The defect is analytic after multiplication by the radius variable, so it vanishes identically.

Equality in the resulting circle estimate forces equality in Schwarz--Pick and hence a degree-one Möbius quotient. Entire cancellation gives
\[
g=(z+\overline a\,\eta R_W)h,
\qquad
f=(az+\eta R_W)h.
\]
The exact norm difference is
\[
(1-|a|^2)
\sum_{j\ge0}|c_j|^2
(m_{j+1}-R_W^2m_j).
\]
The zeroth term vanishes, while every higher term is strictly positive by
\[
m_{j+1}-m_1m_j
=
\operatorname{Cov}(T,T^j)>0.
\]
Thus \(h\) must be constant. The converse pair is checked by a direct pointwise identity and the defining moment relation.

## Originality

PASS. The 2026 primary source explicitly gives all equality pairs for the standard Gaussian Fock space. Its separate theorem for every non-increasing radial weight determines the sharp radius and admissibility, but does not state a complete equality classification for those weights.

Earlier weighted-Fock papers of Wee and Le focus on upper bounds obtained from probe pairs. The source itself describes its new theorem as making those upper bounds sharp in the Hilbert case. A targeted published-finding search over equality, extremal-pair, Möbius, and weighted-Fock formulations found no implication-equivalent classification.

The principal residual risk is that the equality propagation may have been observed in an unpublished note or under a different extremal-pair terminology not surfaced by the searches.

## Value

PASS. Once an optimal domination radius is known, classifying all equality pairs is the natural next extremal problem. The result shows a strong universality phenomenon: changing the entire monotone radial weight changes only the radius, not the geometry of equality.

This is more than the existence of a sharp probe pair. It rules out every nonlinear extremizer throughout a broad family that includes stretched-exponential and decreasing gamma-type Fock weights, providing a reusable rigidity statement for later stability and perturbation questions.

Same-model review: passed. Independent audit: not yet performed.
