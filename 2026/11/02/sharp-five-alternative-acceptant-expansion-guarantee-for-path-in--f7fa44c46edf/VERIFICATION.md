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

# Reproducible exact verification

Run `python3 verification/verify.py`. The verifier uses only exact integers and Python's standard library. It checks every generated choice function against the full path-independence identity and checks every source against every admissible acceptant target. Expected five-alternative lines include `QUOTA 3 SOURCE 56140 ACCEPTANT 80 UNCOVERED 0` and `QUOTA 4 SOURCE 59385 ACCEPTANT 5 UNCOVERED 0`, followed by `SIX_WITNESS_NO_EXPANSION 4` and `VERIFICATION_OK`.

The completeness argument uses the established Aizerman–Malishevski maximizer-collecting theorem; without that theorem, computational generation would certify only the generated subclass. The six-alternative witness is an independently verified instance of a previously published type of obstruction, not a new priority claim. No inference about arbitrary larger numbers of alternatives is made, and no independent validation has been performed.
