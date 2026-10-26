---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and verification

The assertion is an analytic proof and has no numerical premise or external certificate dependency. Check the normalization by direct polar integration:
\[\frac2\pi\int_{|z|<1}|z|^{2m-2}(1-|z|^2)dA=\frac2{m(m+1)}.\]
Expand the pole fractions and use Parseval to obtain the pair potential \(\Phi\). Direct differentiation of its explicit complex-logarithm formula gives the Poisson integral for \(\Phi''\). Since the denominator does not exceed \((1+s)^2\), the uniform curvature floor is \(2\log2-1\), attained at exactly the antipode. For the cyclic \(r\)-arcs check \(\sum_j\sigma_{j,r}=2\pi r\), and for centered pole-angle lifts check \(\sum_{r,j}(d_{j+r}-d_j)^2=2N\sum_j(d_j-\bar d)^2\). These equalities prove the global inequality, the positive remainder, and equality classification. Checking \(N=2\) and an antipodal perturbation proves sharpness.

A direct numerical consistency exercise sampled 500 independent random ordered pole configurations for each \(N\in\{2,3,4,7,13\}\) (fixed random seed 721). It evaluated \(\Phi(t)=2\operatorname{Re}(1+(e^{-it}-1)\log(1-e^{it}))\) away from angular coincidences and used \(\Phi(0)=2\) at coincidences. The sampled minimal normalized ratios were approximately 0.3862944115, 0.4424687212, 0.4672763750, 0.4992361286, 0.5084594684, respectively, all above \(2\log2-1\approx0.3862943611\). For \(N=2\), perturbations by 0.1, 0.01, and 0.001 radians gave ratios approaching the lower bound. These finite observations do not prove the theorem and are not relied upon for global quantifiers.

The endpoint case with colliding poles is justified by the continuity of \(\Phi\) and the integrability of its logarithmic curvature blowup at the angular endpoints. The result does not address unweighted \(L^1\), other power weights, or fixed-\(N\) optimality for \(N>2\).
