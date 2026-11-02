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

# Verification record

The proof uses an exact three-class Markov reduction, strict convexity of the mean and a regenerative rare-target argument. The standalone `checker.py` uses independent full vertex-state rational linear systems, not the derived three-class equations, to verify the mean and generating function, and independently propagates vertex-level distributions for the initial ten hitting-time probabilities. It also compares examples of nonisomorphic regular cores, boundary and interior optimization cases, and large-parameter formulas.

Run using Python 3 (standard library only): `python checker.py`. The reviewed execution returned `PASS 5247 exact comparison and analytic-limit assertions`.

Finite-state checking is supplementary. The general topology-invariance proof depends on exact regularity, the unique optimizer on strict convexity, and the limit on independent regenerative trials with uniformly bounded failure-duration variance. No independent audit has been performed. The result does not verify any claim of global historical uniqueness.
