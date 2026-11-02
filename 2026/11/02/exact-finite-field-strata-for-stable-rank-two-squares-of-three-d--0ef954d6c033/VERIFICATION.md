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

# Reproducibility record

The accompanying `verify.cpp` enumerates the original labeled multiplication tables. Compile it with `g++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify 2`, `./verify 3`, `./verify 4`, and `./verify 5`. Each previously yielded `VERIFY_OK` after evaluating all \(q^9\) matrices and classifying the two-dimensional stable-square instances, with no hard-coded observed counts.

Observed \((\text{rank two},\text{stable},\text{split},\text{double},\text{irreducible})\): \(q=2\): \((294,186,162,18,6)\); \(q=3\): \((8112,6384,5040,768,576)\); \(q=4\): \((79380,68580,50760,8100,9720)\); \(q=5\): \((461280,418080,295200,46080,76800)\).

The code treats \(\mathbb F_4\) as \(\mathbb F_2[z]/(z^2+z+1)\). Its classification directly examines products and natural orthogonality, then compares counts to the formula. It does not establish the statement for arbitrarily large \(q\); that extension is supplied by the projective-plane argument in the mathematical proof. No independent audit has been performed.
