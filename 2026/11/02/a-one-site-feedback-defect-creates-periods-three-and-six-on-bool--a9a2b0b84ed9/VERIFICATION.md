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

`VERIFY.py` constructs the full binary update matrix from its graph definition, checks the predicted ranks and matrix-power identities in dimensions \(2\) through \(8\), and checks all configurations exhaustively in dimensions \(2\), \(3\), and \(4\). Its separately implemented direct state-transition function agrees with the matrix analysis. The output in `VERIFY_OUTPUT.txt` ends `HYPERCUBE_ONE_SITE_VERIFY_OK`.

The program is finite validation, not an all-dimensions proof. The general theorem follows from the rank and invariant-plane argument in `RESULT.md`. No third-party dependency is required; invoke `python3 VERIFY.py` in a directory containing this file.
