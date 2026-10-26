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

# Verification and scope

Run `python verify.py` with Python 3 and the standard library; NumPy is optional, enabling additional full-superoperator diagonalizations. In the performed check, 69 exact-rational finite-\(n\) rate configurations through \(n=8\) reproduced the minimal rank-two prefix; 67 finite dimensions verified the exact rate-rectangle maximum. For \(n=1,2,3\), independently assembled Lindblad matrix eigenvalues agreed with the triangular formula to numerical precision. Gaussian-window finite-size diagnostics also matched the predicted trend. The analytic proof in RESULT.md establishes all integer dimensions and the asymptotic limit; neither the finite enumeration nor numerical diagonalization is an exhaustive proof. The model assumes positive rates, retained multiplicities, and excludes parameter tie lines.

The verification included no independent scientific audit; these checks reproduce calculations and do not establish literature-wide priority.
