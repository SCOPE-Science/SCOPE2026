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

Run `python3 verify.py` from the extracted directory containing this file and `verify.py`. No third-party libraries are required.

The verifier builds closed-neighborhood matrices directly from Hamming distance one, checks nilpotence/involution at ranks 2, 3, 4, exhaustively lists all nonzero dual words at those ranks, enumerates disjoint helper-set packings for representative systematic and parity positions, and checks exact localities. It also validates the explicit rank-four triple and independently computes the minimum codeword weight at ranks 2 through 5.

Successful execution ends with `VERIFY_OK`. This computation checks the indicated finite ranks only. The all-rank repair-availability claims and upper bound use the mathematical proof in RESULT.md. The original graph-code construction and its earlier literature are credited there. No independent external scientific audit is recorded.
