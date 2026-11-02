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

# Reproducibility and limits
Run `python checks/verify.py` from the unpacked finding directory. Only the Python standard library is needed. The checker enumerates all fixed-point-free permutations of sizes 2 through 8 and calculates exact Ewens-weighted cycle moments for parameters \(\theta=1/2,1,2\). It then compares against two independently computed recurrences and the cycle-marking identities. It checks monotonicity and the one-crossing sign pattern through size 450 and samples convergence of the transition fraction.

In the completed local run, 5,658 exact assertions passed and 51,024 weighted derangement cases were counted across the three parameter values. The mathematical proof, not finite enumeration or a numerical phase probe, establishes the all-size statement and limiting profile. No independent audit or external certification is asserted.
