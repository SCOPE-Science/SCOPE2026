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

Execute `python3 checker.py` with Python 3.10 or later; the standard library is sufficient. The checker independently builds the perfect-matching facets for the prism and the predicted facets indexed by base matchings. It compares every face and then constructs the signed orientation of the complete augmented face-poset Hasse diagram, performing a full directed-cycle test. It also computes all reduced mod-two Betti numbers using exact bit-vector Gaussian elimination.

Verified: all 613 labeled even-cycle-free simple graphs on one to five vertices, including 28 cases with a perfect matching; 92,400 augmented faces and 260,989 directed incidences. Seven additional named graphs with up to seven base vertices, and the forbidden boundary case \(C_4\), were tested. The boundary has reduced mod-two first Betti number four. The full captured output appears in `CHECKS.txt`. These finite checks are not a proof for arbitrary \(n\); the uniform acyclicity and uniqueness arguments in `RESULT.md` establish the theorem.

The primary literature comparison covered the complete accessible text of arXiv:2209.02803, arXiv:2407.05809 and arXiv:2608.30601v2. The present theorem includes already-known path and odd-cycle consequences, and this overlap is identified in the result and review. No independent audit or external certification has been performed.
