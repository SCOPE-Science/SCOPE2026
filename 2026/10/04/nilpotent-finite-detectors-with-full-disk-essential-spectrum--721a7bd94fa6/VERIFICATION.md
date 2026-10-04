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
# Verification

The following checks were completed for the stated claim.

1. **Ambient algebra.** Corollary 10.7 of arXiv:2609.32330v1 applies to \(F_n=M_n(\mathbb C)\) with their operator norms and yields an isometric unital Calkin-algebra realization of the countable \(\ell_\infty\)-product.
2. **Spectrum.** The coordinatewise inverse formula was reconstructed for all four regimes \(\lambda=0\), \(0<|\lambda|<1\), \(|\lambda|=1\), and \(|\lambda|>1\). The first three fail invertibility globally through singularity or unbounded inverse norms; the last has the uniform bound \(1/(|\lambda|-1)\).
3. **Polynomial norm.** Each finite shift is a compression of the unilateral shift, giving the upper bound. Finite-support vectors give the reverse inequality after taking sufficiently large matrix sizes. Hence the polynomial norm is exactly the disk supremum norm.
4. **Finite detectors.** The first \(r\) shifts have common nilpotency exponent \(r\), so every polynomial has singleton spectrum \(\{p(0)\}\) at that stage.
5. **Global polynomial spectrum.** Banach-algebra spectral mapping applied to the Calkin class gives \(p(\overline{\mathbb D})\).

The argument is exact and symbolic; no numerical approximation, finite search, or external certificate is needed. The realization theorem is the only non-elementary premise. The checked literature does not establish priority, and an equivalent classical finite-section formulation under different terminology remains possible.
