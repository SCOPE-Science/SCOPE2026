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

The proof is the symbolic \(\mathbb F_2\) rank reduction and count in `RESULT.md`. Run `python verify.py` using Python 3.10 or later; no third-party packages are needed.

The verifier reports `VERIFY_OK` after: comparing all translated cubic derivatives' direct matrix ranks against an independent at-most-four-group reduction through \(n=11\); checking the exact binomial rank multiplicities and all-size closed order-two moments for \(4\le n\le30\); and reconstructing the order-two Pauli--Liouville moment through independent Boolean Walsh transforms for \(4\le n\le8\). The finite tests corroborate but do not prove the theorem for arbitrary \(n\). No external or independent audit has been performed.
