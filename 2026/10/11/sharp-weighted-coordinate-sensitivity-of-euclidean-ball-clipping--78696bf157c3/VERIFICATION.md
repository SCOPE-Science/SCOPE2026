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

# Verification and limits

The exact norm identity is proved analytically in RESULT.md. In particular: an exterior Jacobian is a rescaled orthogonal hyperplane projection; its weighted infinity norm is the maximum weighted absolute row sum; Cauchy--Schwarz is saturated by weights-proportional remaining coordinates; a two-by-two eigenvalue gives the maximum; and the transpose-dual identity proves the weighted sum version. The interior identity region and one-dimensional edge case are handled separately.

Reproduce the finite checks by running `python3 verify.py`. The program verifies random weighted Jacobian row and column norms, explicit normals reaching the formula, and finite exterior differences approaching the predicted amplification. These numerical tests do not certify an infinite family of parameters; they are secondary evidence. There is no independent mathematical audit or independent validation.
