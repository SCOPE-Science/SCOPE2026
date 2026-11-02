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
# Verification notes

The proof is an all-real-parameter argument. Its exhaustive analytic part is the table of sixteen choices of the final omitted vertex and its image; it supplies a universal lower bound for any permitted order. The two explicit compatible retraction systems provide matching upper bounds. The metric edge-test argument remains valid when the special edge is longer than the shortest route through the other four edges.

`verify_pentagon.py` checks the distance formulas, the explicit maps, the sixteen witnesses, and, at several rational inputs, enumerates every candidate ordering and all compatible prefix retractions. Run `python verify_pentagon.py` from the directory containing this file. Expected output: `PENTAGON_RATIONAL_CHECK_OK`.

Finite testing alone is not a proof of the continuously parameterized theorem. No external or independent audit was performed. The argument does not address arbitrary linear Schauder bases.
