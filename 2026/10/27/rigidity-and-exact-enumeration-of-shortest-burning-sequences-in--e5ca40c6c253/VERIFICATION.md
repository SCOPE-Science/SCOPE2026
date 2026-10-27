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

The proof is an exact all-dimensional binary linear-algebra argument. The files `verify_pg.py` and `verify_output.txt` record a standalone exhaustive recurrence over all legal synchronous source choices on orders \(7\) and \(15\): the total numbers of valid optimal sequences are \(504\) and \(141120\). The published earlier tables agree on these two cases. The verifier separately replays an explicit minimum sequence for orders \(7,15,31,63\), including exact round-end size profiles and a redundant last source. The product formula was also evaluated with arbitrary-precision integers for dimensions \(3\) through \(7\). This finite evidence does not establish the infinite statement; see the span and induction proof in `RESULT.md`. The complete MSc-thesis PDF was not accessible for historical priority checking; no independent scientific audit is claimed.
