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

Run `python verify_matching_fixed.py` from the directory containing the standalone script. It uses only standard-library Python and independently enumerates all faces of the symmetric-orbit complex for \(n=2,3,4\), evaluates all \(\mathbb F_2\) simplicial boundary ranks by bit elimination, and verifies reduced homology concentrated in degrees \(0,2,5\), each of rank one. A separate face-level signed Lefschetz enumeration exhausts original matching faces for the same values of \(n\), testing the identity, row transposition, column transposition, transpose, and a composite, and checks the character signs.

Verified output:

```
fixed 2 (3, 4, {0: 1})
character 2 [1, -1, -1, 1, -1]
fixed 3 (6, 44, {2: 1})
character 3 [1, 1, 1, -1, -1]
fixed 4 (10, 808, {5: 1})
character 4 [1, -1, -1, -1, 1]
MATCHING_FIXED_SPHERES_AND_CHARACTERS_VERIFIED
```

These computations are finite checks only. Infinite correctness rests on the proof's simplex-orbit identification, nerve lemma, integral combinatorial Alexander duality and Hurewicz/Whitehead argument. No independent mathematical audit is asserted.
