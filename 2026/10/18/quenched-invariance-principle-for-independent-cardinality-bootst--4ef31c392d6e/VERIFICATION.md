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
# Reproducibility and scope

Run `python verify_quenched.py` using the Python standard library. This performs **finite exact diagnostics only**: parity count for Lucas's theorem, geometric dyadic digit sum identities, heterogeneous Bernoulli expectation factorization, and the conditional one-step covariance identity for fixed coefficient arrays.

The general theorem is established analytically by the five-step proof in `RESULT.md`, including the conditional strong law, the geometric-occupation argument, Fubini's disintegration and the multivariate martingale functional central limit theorem. Finite enumeration does not certify almost-sure limits and is not presented as doing so.

The mathematical claims were checked for coefficient-index boundary conditions \(n\ge1\), the fixed multiplier \(\zeta_0=1\), the exponent parity convention, uniform ellipticity, the time and cardinality independence needed for conditional independence, and the distinction between annealed and quenched laws. The cross-variation proof is joint almost sure and therefore implies conditional almost sure for almost all environments; it does not assert a uniform-in-environment limit.

The 2026 motivating preprint was read at the relevant formal setting, Theorem 2, Proposition 7, Proposition 8, Corollary 9 and the post-corollary remark, and compared by mathematical implication. This is a self-review, not independent certification.
