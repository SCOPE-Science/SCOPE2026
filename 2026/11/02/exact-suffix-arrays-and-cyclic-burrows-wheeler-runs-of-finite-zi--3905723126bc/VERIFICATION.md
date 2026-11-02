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

# Reproduction and scope

Run `python3 checker.py` from the extracted package. The checker independently constructs literal finite Zimin words, compares brute-force suffix sorting to the stated recursive permutation for ranks \(1\) through \(11\), and compares brute-force cyclic rotation sorting to suffix sorting and the claimed transform for ranks \(1\) through \(9\). It verifies the primary index and exact run counts, including the merging exception at rank \(2\). All these finite tests passed.

The proof of the statements for **all** ranks is the induction in `RESULT.md`; the finite checker alone cannot certify infinitely many ranks. The code uses no third-party packages. Independent mathematical auditing is not represented by these tests and has not been performed.
