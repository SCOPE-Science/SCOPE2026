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

# Verification and reproducibility

The included `verify.py` is standalone standard-library Python. It exhaustively tests both directions of the proposed exclusion for unordered \(2\le a<b\le5000\), independently checks the numerator criterion at all prime pairs not exceeding \(5000\), and compares the multiplicative \(n\mathcal H(n)\) identity with the original rational sum for all \(1\le n\le600\). The nontrivial positive example \(\mathcal H(614341)=486361\) and the \(\Phi_4\) contrast are also checked.

The logical verification is the four-step Vieta descent in RESULT.md, which uses no unproved computational lemma. Exact finite tests alone do not prove an unrestricted universal claim. Earlier source priority and the general problem for nonsquarefree \(n\) are not resolved. No independent mathematical audit has been performed.
