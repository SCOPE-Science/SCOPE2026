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

# Reproduction and verification

Compile the supplied `verify.c` as follows:

```sh
cc -O2 -std=c99 -Wall -Wextra verify.c -o verify
./verify
```

This program uses solely the standard C library. It evaluates the integer adjugate formula for the exact orthogonal cycle-projection norm. For each vertex count \(2\) through \(6\) it processes every bit mask of possible edges, checks connectedness and checks all single missing-edge insertions. It does not use floating point or assume any graph catalogue is complete. The observed labelled-connected graph counts are \(1,4,38,728,26704\); the numbers of insertions are \(0,3,84,3140,186360\). There were zero cycle-projection norm decreases in all \(189587\) tested insertions.

For the explicit seven-vertex witness, exact grounded Laplacian determinants are \(153\) before addition and \(243\) after addition. The checked cut-projection norms were \(\frac{284}{153}\) and \(\frac{16}{9}\); the cycle-projection norms were \(\frac{313}{153}\) and \(\frac{55}{27}\). The printed final success line confirms the exact strict difference \(\frac4{459}\). The correct mathematical inference is an exhaustive finite threshold, **not** a general infinite-graph monotonicity statement.

An additional symbolic exact-rational cross-check, using separately constructed incidence matrices with SymPy and all 142 connected unlabelled NetworkX Graph Atlas representatives on at most six vertices, passed all 821 edge insertions. This cross-check is ancillary; the shipped C program is self-contained and verifies the full labelled domain.

The computation confirms mathematical statements under the specified conventions; it is not an independent mathematical audit or an external certification.
