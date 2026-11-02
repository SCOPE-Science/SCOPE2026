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

# Verification record

`verify.cpp` is the exact all-structure enumerator for dimension two; it uses full finite-field multiplication tables and checks every invertible matrix against the original algebra homomorphism equations, including the mixed product. Compile and execute in C++17; the expected final line is `VERIFY_OK`. The observed rows are:

| Field | All labeled structures | Exactly three automorphisms | Perfect among these |
| --- | ---: | ---: | ---: |
| \(\mathbb F_2\) | 16 | 0 | 0 |
| \(\mathbb F_3\) | 81 | 0 | 0 |
| \(\mathbb F_4\) | 256 | 30 | 6 |
| \(\mathbb F_5\) | 625 | 0 | 0 |
| \(\mathbb F_7\) | 2401 | 24 | 24 |
| \(\mathbb F_8\) | 4096 | 0 | 0 |
| \(\mathbb F_9\) | 6561 | 0 | 0 |

`verify3.cpp` independently checks the explicit dimension-three candidates using **all invertible matrices**, not just monomial matrices. It reports \(3\) automorphisms among respectively \(168,11232,1488000\) invertible matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and concludes `VERIFY3_OK`.

Run in a directory containing these standalone source files:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify2 && ./verify2
g++ -O3 -std=c++17 verify3.cpp -o verify3 && ./verify3
```

Computational limits: the checks do not exhaust all fields, all three-dimensional structure matrices, or all algebra dimensions. The symbolic proof handles arbitrary fields. The group-of-points convention differs from claims about the affine group scheme; no external independent mathematical audit has occurred.
