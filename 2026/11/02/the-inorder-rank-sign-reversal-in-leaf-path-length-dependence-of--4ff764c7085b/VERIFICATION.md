---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Checked priority Cartesian tree equivalence, leaf event U_r greater than adjacent sorted-rank priorities, and P_n=∑_{i<j} 1{minimum U_i..U_j occurs at endpoint}. Conditional three-priority beta integrations give the stated one-sided shifts and telescoping B(ℓ)=−1/3+2/[(ℓ+1)(ℓ+2)], yielding exact interior covariance −1/9+2/[3r(r+1)]+2/[3(n-r+1)(n-r+2)]. Endpoint beta integrals yield −(n−2)/(2n); all-n sign and total covariance follow by inequalities and telescoping. Independently reconstructed all BSTs for every insertion order n=2..7 with rational covariances and matched each rank; finite enumeration corroborates the unconditional all-n proof, not a replacement.

## originality

PASS

PASS (qualified): the exact finite-n inorder key-rank covariance and unique near-endpoint positive sign pattern is not implied by the inspected random BST papers. Bóna–Pittel use rank to mean distance from leaves, a different statistic; Chern et al. study global path-length relationships and phase limits. The global covariance follows from the local formula and is not separately claimed as original.

## value

PASS

PASS: An individual inorder rank’s leaf indicator and total path length are natural correlated BST statistics. The exact sign reversal confined to r=2,n−1 for all n≥6 reveals spatial heterogeneity obscured by a negative global covariance and is a useful complete all-size profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
