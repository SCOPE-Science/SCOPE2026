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

The finite theorem is verified by the standalone program `verify.cpp`, compiled from the embedded source with a C++17 compiler. Its execution enumerates all \(65,536\) subsets of \(Q_4\); all \(8,122\) feasible layer masks and \(65,966,884\) ordered layer pairs for \(Q_5\); and the full coordinate-flip/permutation orbits of each optimum. The two-layer predicate is shown equivalent to the original graph condition in `RESULT.md`, and the checker rechecks every minimum candidate directly on the 32-vertex graph.

Command:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
```

Actual output:

```text
Q4_EXHAUSTIVE 8 428 SUBSETS_CHECKED 65536
Q5_EXHAUSTIVE 16 1830 ADMISSIBLE_LAYERS 8122 ORDERED_PAIRS 65966884
Q4_SIX_AUTOMORPHISM_ORBITS 8:255 12:4080 24:7128 96:975 96:2022 192:987
Q5_SIX_AUTOMORPHISM_ORBITS 10:65535 20:16776960 120:63960000 240:1044735 480:4193340 960:1045455
VERIFY_OK
```

All computations are exact finite integer tests. The program enumerates every candidate under a proved equivalence; it does not rely on random testing, a timeout, a numerical floating-point threshold, or extrapolation. The proof of the two-layer equivalence and of full-group generation remains part of the human-readable reasoning. No independent audit has been performed.
