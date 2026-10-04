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

The symbolic proof establishes the theorem for every connected complete multipartite graph with at least two parts. The packaged `verify.py` performs an independent finite consistency check through order \(9\).

It enumerates all nondecreasing multipartite profiles with at least two parts, then all \({0,1,2}\)-labelings. For each labeling it compares the literal independent Roman definition with the claimed one-part criterion. It also compares every weight coefficient with the closed formula, checks the minimum weight and the number of minimum functions, and reconstructs every profile from the polynomial.

Replay command: `python verify.py`

Expected output: `VERIFY_OK profiles=87 labelings=748341 valid_functions=2316 coefficient_checks=1369 min_checks=87 reconstruction_checks=87 max_order=9`

The finite census is not used as an infinite proof. It is a boundary and implementation check for the symbolic argument.
