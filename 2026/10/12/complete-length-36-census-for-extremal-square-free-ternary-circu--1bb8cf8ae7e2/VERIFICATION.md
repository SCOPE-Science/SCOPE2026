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

Compile and run `verify.cpp` beside `certificate.json`:

`c++ -O3 -std=c++17 verify.cpp -o verify && ./verify`

The verifier reconstructs every ternary square-free linear word through length \(37\) by exact suffix-square tests. It independently checks circular square-freeness at lengths \(36\) and \(37\).

Extremality at length \(36\) is then tested twice. Engine A asks whether any insertion belongs to the completely enumerated length-\(37\) circular-square-free language. Engine B directly tests every one-letter insertion for circular square-freeness. The two exact sets must coincide.

Finally the verifier canonicalizes rotations, confirms \(15\) circular classes, and recomputes the action of all six alphabet permutations together with reversal, obtaining three orbits of sizes \(6,6,3\).

The computation is finite and exhaustive. It proves only the length-\(36\) equality classification stated here. Independent audit has not been performed.
