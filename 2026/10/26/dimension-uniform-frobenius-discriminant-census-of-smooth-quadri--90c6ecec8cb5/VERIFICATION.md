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

# Reproducible exact finite checks

Run the two independent programs directly from this package in an environment with Python 3 and a C++17 compiler:

```sh
python3 check_pencils.py
g++ -std=c++17 -O2 -o check_quadric4 check_quadric4.cpp
./check_quadric4
```

The concatenated standard output of these programs appears in `expected_counts.txt`, separated by one blank line. Both were executed directly from the material in the package and matched these outputs.

The first program enumerates all finite ternary conic pencils over \(\mathbf F_3\) and \(\mathbf F_5\), checking each of the \(q+1\) rational members; it also directly enumerates root-free squarefree degree-four monic polynomials over \(\mathbf F_3,\mathbf F_5,\mathbf F_7\). The independent C++17 program enumerates the full set of four-by-four symmetric ternary matrices for each of the two Witt types of invertible first matrices, without using the first program's polynomial enumeration, and compares with a direct count of nonsingular first matrices. It produces exactly \(509,483,520\) ordered valid pairs and, after dividing by \(|\mathrm{GL}_2(\mathbf F_3)|=48\), the formula's \(10,614,240\) pencils.

All computations are finite checks only. In particular, polynomial enumeration for degrees three and four is not evidence for all \(n\). The uniform conclusion is instead proved by the geometric smoothness–discriminant equivalence and the étale trace-form count in `RESULT.md`. No proof assistant or external human validation is claimed. Published-priority reservations appear in `REVIEW.md`.
