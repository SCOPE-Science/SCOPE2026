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

# Reproduction checks

The included `verify_cyclic_spectrum.py` uses only the Python standard library and can be executed with `python3 verify_cyclic_spectrum.py`. It compares two mathematically distinct constructions: enumerating the actual partial rotations and composing powers on their domains, versus forming the weighted cyclic-run transition matrices with integer-polynomial entries. For each \(2\le n\le10\), it checks every rank coefficient for every cumulative bound \(1\le t\le n\), every upper-half exact-index rank coefficient, and the summed divisor formula for the number of nilpotents.

The independently computed nilpotent totals for \(n=2,3,4,5,6,7,8,9,10\) are respectively \(3,13,37,121,247,757,1545,3745,8171\). At \(n=6\), the separate nilpotency-index counts are \(1,90,108,24,12,12\). The verifier prints `VERIFY_OK` after all checks. Finite enumeration is not evidence of an all-size theorem by itself; the result's proof supplies the uniform combinatorial argument and logarithmic bounds.

No outside certificate or independent scientific audit has been obtained. Scope excludes arbitrary partial permutations and centered extreme-value limits.
