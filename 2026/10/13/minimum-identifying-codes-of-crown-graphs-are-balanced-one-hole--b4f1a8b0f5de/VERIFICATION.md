---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For i!=j the closed-neighborhood symmetric difference N[a_i] Δ N[a_j] equals P_i ∪ P_j, forcing at most one empty matched pair; hence |C|>=n-1. Equality forces one hole and one code endpoint from each remaining pair. For A-side traces, selected a_i gives {a_i}∪B_Q, unselected a_i gives B_Q\{b_i}, and the hole gives B_Q; symmetric B traces. If either chosen-side count is <2 a zero trace or collision results; for >=2 on each side all 2n traces are nonempty, same-side distinct and cross-side disjoint except impossible singleton cases. Count choose hole n times and orient n-1 occupied indices excluding side counts 0,1,n-2,n-1: n(2^(n-1)-2n). Reconstructed definitions and all n>=5 boundary. Independently enumerated all size n−1 subsets for n=5,6,7,8 with totals 30,120,350,896; finite enumeration corroborates but does not prove all n.

## originality

PASS

Best-of-knowledge PASS only for complete minimum-code structure/multiplicity, not the scalar code number. Closest exact-graph 2020 paper reports scalar identifying-code numbers for matching-deleted bicliques; inaccessible full text is the principal unresolved overlap risk, recorded without negative inference.

## value

PASS

The standard extremal crown family has a known scalar identifying-code minimum, but its ENTIRE optimizer set and exact count are natural additional invariants for classification/symmetry and code-selection questions. The two-per-side obstruction and exceptional n=5 onset distinguish it from the easy lower bound. This is a self-contained all-n structural classification, not a mere known-number recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
