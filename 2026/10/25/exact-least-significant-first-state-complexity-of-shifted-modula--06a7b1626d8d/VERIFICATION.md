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

The symbolic proof in `RESULT.md` is the basis for the all-parameter theorem. The finite replay independently constructs automata for sampled parameters, minimizes them by partition refinement, and directly checks evaluated outputs.

Run `python3 checks/verify_shifted_valuations.py`. Compare stdout against `checks/verification_output.txt`. Tests cover 3,200 parameter triples and 204,800 direct outputs. They do not establish the theorem for parameters outside the tested set.

No independent audit has been conducted.
