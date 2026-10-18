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

Compile and run `verify.cpp` using `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. It enumerates all \(3,628,800\) ten-point permutations with `std::next_permutation`, constructs four quadrant bits by direct pair comparisons, and counts the 16-bit spectra with exactly ten set bits. Expected results: 328 extremizers, 164 of spectrum `0xfce8`, 164 of `0xfea8`, and 46 dihedral orbits comprising ten size-four and 36 size-eight orbits.

Run `python3 verify_independent.py` for a separately implemented enumeration based on extrema of each prefix and suffix. It independently returns the two 164 counts. The analytic argument in `RESULT.md` proves that **no finite size** has more than ten local rank-one types. The enumerations prove the exact count only at size ten, and the witness shows its attainability.

The reproducible checks were completed from these files. The verification is not an independent external audit, which has not been performed.
