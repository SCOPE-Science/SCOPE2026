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

# Verification scope
Run `python verify.py` with the Python standard library. The recorded execution returned `PASS 224 exact rational stationary and ballot checks; 12 periodic boundary-layer comparisons` with no assertion failures. The finite identities test the stationary product-generator balance independently from the first-passage dynamic programming recurrence, and test the homogeneous recurrence against a separate ballot-path enumeration. Periodic arrays of rates \((1)\), \((1,3)\), and \((1,2,4)\) were compared at site index 900 against the proposed asymptotic formula for four separations; all twelve absolute discrepancies were below 0.023.

These computations verify finite instances and implementation consistency; they do **not** certify the general theorem or the functional central limit argument. The general proof, including positivity, bounded-period invariance principles, and Brownian hitting, appears in `RESULT.md`. Exact moment identities require independent Poisson input and gates and strictly positive rates. The asymptotic result requires a fixed bounded positive period and positive limiting normalized separation.
