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

# Verification of mixed length-two duplication spheres

The source word consists of \(n\ge2\) letters from a finite alphabet of size \(q\ge2\). The exact-one mixed descendant set includes both ordinary-copy and reversed-copy duplications of an adjacent length-two factor. The key identity subtracts one for each distinct \(abba\) factor because it creates a cross-type duplicate output.

The standalone `verify.py` constructs each output as a complete literal tuple and compares `len(set(tandem_outputs + palindromic_outputs))` with the formula from the proof for every source in the fixed exhaustive ranges. It separately checks the collision criterion for each site whose adjacent symbols differ, validates that these palindromic outputs are pairwise distinct, confirms exact maxima and extremizer counts, and checks the mean by counting all source words. Executed directly from the supplied file path, the checker prints:

`MIXED_PAL_TANDEM_LENGTH2_PASS q=2..5 nmax=12,9,7,6 words=79073 nonconstant_pal_sites=355650`

Run `python3 verify.py` with Python 3; only its standard library is used. The finite tests cover alphabet sizes two through five and the listed finite lengths. For **all** finite alphabet sizes and all source lengths, validity depends on the proof, not on finite enumeration. No theorem about capacity, optimal codes, or multiple errors is implied. No independent external mathematical audit was performed.
