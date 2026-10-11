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
The target source was read in full at arXiv:2102.05255v1, including the range characterization and Theorem 3.8 with its proof. The source-level counterexample was checked symbolically in the two-dimensional Hilbert reduction of a standard 2-inner-product space. The original frame energy equals \(\|K^*x\|^2\) exactly. After the positive transform, every atom is parallel to \((2,1)\), while \(x=(1,-2)\) has zero transformed analysis coefficients and nonzero \(K^*x\).

The false proof step was also checked directly: with \(S_F=P_{e_1}\) and \(S=I+U\), the matrix \(S S_F S-S_F\) has determinant \(-1\), so it is not positive.

For the repair, the synthesis operator of the transformed family is \(SV\). The standard characterization gives the fixed-frame condition \(R(K)\subseteq R(SV)\). Universal preservation is sufficient under \(R(K)\subseteq S R(K)\) and necessary by testing the Parseval \(K\)-frame \((Ke_i)\). Douglas factorization yields the exact positive multiplier \(\eta(S,K)\). No computation beyond these exact identities is used.

Limit: one plausible 2021 construction paper was accessible only by abstract in the checked route, so an unindexed or inaccessible prior correction remains a residual originality risk.
