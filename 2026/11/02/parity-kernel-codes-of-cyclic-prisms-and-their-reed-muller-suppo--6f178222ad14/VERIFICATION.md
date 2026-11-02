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

# Reproducibility

Run `python3 verify.py` with the Python 3 standard library. The code independently constructs all closed neighborhoods of \(C_n\square K_2\), performs exact bitwise Gaussian elimination over \(\mathbb F_2\), and compares every predicted kernel word and weight for \(3\le n\le64\). It independently examines every vertex subset for \(3\le n\le9\), verifies the eight affine evaluation columns of \(\operatorname{RM}(1,3)\) on the four-cycle prism, and enumerates subspaces to check all generalized Hamming weights for \(3\le n\le24\).

Successful execution prints `VERIFY_OK`, with coverage details. These tests are finite and are not proofs for all cycle lengths; the infinite proof is the exact four-period reduction and its code equivalence in `RESULT.md`. No independent external audit or certification is claimed.
