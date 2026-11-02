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

The proof in `RESULT.md` is a finite-field linear-algebra argument valid for every prime power. The standalone `verify.py` and `verify_nilpotent.py` are independent computational tests: it represents traceless matrices by three coordinates, builds the Lie bracket directly, computes the linear span of the input matrices and their brackets by finite-field row reduction, and tests generation without using eigenline classification or the proposed probabilities as its predicate.

The two checkers exhaustively tested every prescribed first matrix and all additional tuples for \(q=2,3,4,5,7\), \(k=1\), plus \(q=2,3\), \(k=2\). It independently supplies arithmetic for the extension field \(\mathbb F_4\). The exact counts for each type appear in `verify.log` and `verify_nilpotent.log`, concluding `VERIFY_OK` and `NIL_VERIFY_OK`.

Finite tests are not exhaustive over all prime powers or tuple lengths; the symbolic Borel-classification and Heisenberg-quotient arguments supply the unrestricted proof. No independent audit or external certification has been undertaken.
