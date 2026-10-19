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

# Verification of exact finite classification

Run the standalone scripts from the same directory:
```
cc -std=c99 -O3 -Wall -Wextra verify_dsr.c -o verify_dsr
./verify_dsr
python3 verify_orbit.py
```
The complete enumerator visits every bitmask at each indicated order; the bit corresponding to ordered pair \((i,j)\) with \(i<j\) is one exactly when \(i\) defeats \(j\). All arithmetic is integral and bounded, and the source checks tie-handling and the exact counts:
```
n=2 total=2 noncontainment=0 disjoint=0
n=3 total=8 noncontainment=0 disjoint=0
n=4 total=64 noncontainment=0 disjoint=0
n=5 total=1024 noncontainment=0 disjoint=0
n=6 total=32768 noncontainment=0 disjoint=0
n=7 total=2097152 noncontainment=5040 disjoint=0
witness_mask=1324 copeland: 3 3 2 2 2 5 4 dsr: 6 3 2 4 5 14 14 first_noncontainment_mask=1324
VERIFY_OK
```
The independent Python orbit computation prints:
```
witness_copeland: [3, 3, 2, 2, 2, 5, 4] witness_dsr: [6, 3, 2, 4, 5, 14, 14]
seven_vertex_label_orbit: 5040 automorphism_order: 1
VERIFY_OK
```
The Python program then independently checks every tournament with two through six vertices (respectively 2, 8, 64, 1,024, and 32,768 cases), finding zero noncontainment instances, using a separate Boolean-adjacency score implementation.

The mathematical bridge from the printed finite census to the theorem is the exact equivalence of the scoring code to Hou's specified 2024 Algorithm 2 and the permutation-equivariance of both rules. The bitmask enumeration is exhaustive within the finite scope, but code may contain undetected errors; there is no independent audit or claim for larger tournaments.
