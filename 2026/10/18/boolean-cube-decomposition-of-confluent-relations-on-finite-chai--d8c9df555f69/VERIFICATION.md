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

# Reproduction and proof boundaries

For the accompanying `verify.py`, execute `python3 verify.py` in the directory containing that file. It uses only the Python standard library. The program directly checks the quantified forward and backward confluence conditions, computes independent row/column profiles for each Boolean matrix on the ten stated rectangular shapes, and compares full arrow-count polynomials with the profile-fiber formula. The shapes together contain exactly 74,650 Boolean matrices. The same implementation uses the profile formula to obtain the six stated square counts.

For an independently coded finite check, compile `verify_exhaustive.cpp` with `c++ -std=c++17 -O3 verify_exhaustive.cpp -o verify_exhaustive` and execute `./verify_exhaustive`. It counts all binary square relations through five worlds, including all \(2^{25}\) relations at size five, and verifies the first five closed-form sums. Both source programs were replayed successfully for this finding.

The programs confirm finite instances, not the unbounded quantifiers. General correctness depends on the written direct proof: (i) maximal witnesses characterize FC and BC, (ii) the two incidence inequalities characterize feasible profile pairs, (iii) independently selectable nonextremal entries give Boolean intervals, and (iv) the bottom-right edge forces the sharp sparsity and free-dimension bounds. No independent audit has been performed.
