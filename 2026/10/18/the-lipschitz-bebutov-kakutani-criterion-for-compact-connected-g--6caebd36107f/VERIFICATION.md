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

## Verification of the claim

**Analytic checks.** The correlation identity uses left Haar substitution; its Lipschitz bound uses only right invariance. The Fourier sign/order is fixed by \(\widehat f(\pi)=\int f(g)\pi(g)\,dm(g)\), which yields \(\widehat{f*g}=\widehat f\widehat g\) and \(\widehat{u*u^*}=\widehat u\widehat u^*\). Concentration of normalized Lipschitz bumps at the identity gives \(\widehat u_n(\pi)\to I\) separately for each irreducible \(\pi\). Strict positivity of each block follows from positive summands, not from a claimed uniform gap. Injectivity uses Peter–Weyl completeness.

**Independent finite algebra diagnostic.** Run `python3 examples/check_convolution.py` with standard Python. Exact fractions test cyclic order five and nonabelian symmetric order six: both convolution matrices have nonzero determinants, with exact normalization, shift equivariance, and Lipschitz inequalities. This does not prove the general theorem; the infinite-group assertions are established analytically in RESULT.md.

**Boundary check.** The fixed-point criterion uses connectedness only to invoke the classical Jaworski–Chen continuous-shift theorem. The convolution filter itself works for every compact metrizable group. No inference is made from a merely Borel embedding to a continuous embedding.

**Limits.** Not checked by an independent party. A general compact-group harmonic-analysis text could already imply the smoother as an unstated lemma; claims about uniqueness in the full literature are not made.
