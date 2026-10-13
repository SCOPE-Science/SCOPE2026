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

The arbitrary finite-region claim is analytic. For a subset indicator \(t\), direct parity counting gives \(B_Rt=\mathbf1_{dT\cap R}\); therefore the contributing subsets are exactly \(\ker B_R\). Rank-nullity then gives exactly \(2^{\dim\ker B_R}\) contributing subsets. The source-defined two-term condition leaves either only \(0\), or exactly \(0\) and \(\mathbf1\), which is equivalent to the two kernel cases stated in the finding.

`artifacts/verify.py` performs exact \(\mathbb F_2\) row reduction and exhaustive subset enumeration for a suite of small matrices, including the degree-three witness. It asserts equality between enumerated survivor count and \(2^{\text{nullity}}\), and separately checks the two-case criterion. These tests are corroborative only; they are not an exhaustive proof over arbitrary region size.

The downstream Dobrushin-Shlosman conclusion is not rederived by the checker. It is invoked only under the unchanged assumptions of Theorem 2.6 in the cited source. No independent audit or external validation has been performed.
