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
# Direct computational verification

The standalone file `verify_hyperoctahedral.cpp` implements signed permutations as signed images of the positive coordinates; a direct multiplication computes product signed permutations. The program enumerates every signed permutation of degree one through six and constructs one representative of each exact signed-cycle conjugacy type. For each representative it enumerates **all** choices of the second group element, computes the complete atomic diagram on the identity and both chosen elements (including both product orders), and stores the set of possible diagrams. It separately checks the signed-cycle square-root criterion by brute force, across all cycle types through degree six.

Build and run, in the same directory:

```sh
g++ -O3 -std=c++17 verify_hyperoctahedral.cpp -o verify_hyperoctahedral
./verify_hyperoctahedral
```

The exact recorded output is embedded as `verify_hyperoctahedral.out`. It reports pointed-profile counts \(2,4,6,7,8,8\) at degrees \(1,2,3,4,5,6\), exact identity between the full sets for degrees five and six, and eight categories determined solely by element order class and square existence from degree five onward. It ends in `VERIFY_OK`.

**Limits:** Finite enumeration through degree six alone cannot establish the theorem for arbitrary \(n\). The infinite classification depends on the generic involution and three-cycle constructions, the square-root decomposition lemma, and the four distinguishing rank-two sentences proved in `RESULT.md`. No independent formal or external scientific audit was performed.
