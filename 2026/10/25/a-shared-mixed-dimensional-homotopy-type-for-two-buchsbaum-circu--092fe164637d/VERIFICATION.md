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

The package's `verify.py` is standalone and requires Python 3 standard library only. Run `python3 verify.py` and compare the output to `VERIFIER_OUTPUT.txt`. Each case enumerates all bit masks, checks every face, validates each matched Hasse edge, checks a complete topological sort of all arrows, and reduces the integral signed 49-by-64 presentation via exact unimodular row and column operations. The graph nonisomorphism check uses an independent common-neighbor edge histogram. These are exact finite checks and, together with the stated discrete Morse and attaching-degree arguments, prove the specified two-case homotopy theorem. No numerical approximation or finite-to-infinite extrapolation is involved. Independent audit has not been performed.
