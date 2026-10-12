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

Execute `python3 verify.py` with Python 3 standard library. The adjacent `verification_output.txt` records the actual run. The verifier enumerates every vertex ordering on 11 finite double-star profiles and checks the complete probability law, then checks 20,100 rational parameter profiles and the predicted minimizer at every order from 3 through 200. Each check operates from exact fractions; none relies on floating-point thresholds. The full quantification for all integer parameters is established in `RESULT.md`, not by finite tests. The standalone program does not validate literature originality or any external certification.
