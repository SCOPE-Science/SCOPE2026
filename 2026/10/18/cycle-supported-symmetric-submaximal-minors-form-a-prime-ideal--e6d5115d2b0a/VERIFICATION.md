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

The mathematical proof is the four-step argument in `RESULT.md`, with the all-graph radicality and connected-path determinant irreducibility attributed to the open-access primary source `arXiv:2211.07020`. The self-contained script `verify_cycle.py` constructs exact dense-edge corank-two witnesses and, for every two-edge cut in cycle sizes four through eight, checks the two-block kernel and surjectivity of the tangent restriction map. Expected terminal output is `VERIFY_OK`; it was checked in the present package. The script checks only finitely many cases, not the all-size result. No independent audit or outside proof certification was performed.
