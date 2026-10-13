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

The universal algebraic identity and its inverse coordinate transformation are written in `RESULT.md`; they are the proof, not the finite tests. Run `python3 checker.py` using Python 3.8 or later; no third-party dependencies are needed. The retained `checker_output.txt` gives the exact observed result: 42 integer specializations of the permanent expansion identity for \(3\le n\le8\), and six nonzero complementary-matrix determinant checks.

The all-size statement is established by the Laplace-type permanent expansion and by specializing all remaining matrix entries to one; an enumeration through eight does not certify all positive integers. Rank and Jacobian-scheme claims follow from the invertible change of coordinates on the principal open. No claim is made beyond that open, and no independent audit has taken place.
