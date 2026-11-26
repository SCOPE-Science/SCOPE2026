---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The signed coordinate convention places a+it in the units position and it in the next m−1 positions. The fixed-point equations are a(a−1)=mt² and 2a=R_m(B), the latter using t≠0. The imaginary equation is impossible for m=1 by parity and for m≥3 since B²+B+1>2(B−1). At m=2 the two equations are equivalent to a=(B+1)/2 and B²−8t²=1; that equation forces odd B≥3 and ensures both digit bounds. For t>1, multiplication by 3−√8 keeps both integer coefficients positive and gives 0<3t−B<t, preserving norm; t=1 has exactly B=3. This proves all positive solutions are the stated powers, and negative t gives conjugation. The cosh identity then proves the exact count, including equality at a Pell base. An independent exact signed-digit scan over 2≤B≤50, 1≤m≤5 found exactly both signs at B=3 and 17 and no others; replay: python3 /workspace/checks/frozen_review_checks.py gaussian. This is a finite diagnostic, not the proof.

## originality

PASS

The distinct result supported by the comparison is the necessary-and-sufficient all-base classification of this nonreal digit pattern, not the introductory Gaussian map, its known base-3 pair, or the classical Pell solution. No inspected result establishes that classification or renders it a special case of a complete known fixed-point classification.

## value

PASS

A one-digit real part and constant imaginary digits are a natural low-complexity nonreal test family for the Gaussian map. The result determines exactly when this family occurs and how sparse its bases are, rather than extending a table by a few points. The elementary proof and familiar Pell equation do not reduce the mathematical conclusion to a new name for an existing arithmetic sequence: the length obstruction and iff occurrence answer a fixed-point question. The result is not a spectrum of all nonreal fixed points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
