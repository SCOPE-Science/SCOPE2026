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

# Verification instructions and limits

Run `python3 verify.py` (Python 3 standard library). The expected final output is exactly:

`VERIFY_OK exhaustive_tuples=69904 matrix_checks=165 even_lengths=12`

The checker computes the actual power of the cyclic neighbor-sum operator on tuples over integers modulo four. A direct row/column diagonalization routine determines exact image cardinalities for all powers up to two beyond the predicted nilpotence time at the even lengths 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24 and 32. Exhaustive iteration directly classifies all starting tuples at lengths 2, 4, 6, 8, totaling 69,904 tuples, using periodic vectors obtained by iteration. This verifies agreement with the predicted frequency formula at those finite instances.

The calculations are not independent scientific certification and cannot prove the infinite assertion. The complete proof is the CRT and explicit ideal-filtration argument in `RESULT.md`. The theorem's originality is assessed against inspected papers, with residual bibliographic risks stated in `REVIEW.md`.
