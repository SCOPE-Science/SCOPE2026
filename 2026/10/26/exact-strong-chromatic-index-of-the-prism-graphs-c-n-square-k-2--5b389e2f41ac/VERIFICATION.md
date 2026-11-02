---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For n≥7 a 6-coloring forces alternating rung colors from a six-edge conflict clique; the four remaining horizontal colors force the swap c(t_{i+2})=c(b_i), c(b_{i+2})=c(t_i), hence nondegenerate period four and 4|n. The n=3,5,6 exceptions follow exhaustive small induced-matching counts (histograms 1,9; 1,15,25; 1,18,57,2). The four-column 6-color pattern and finite 7-/8-color seeds were read from construct.py and checked by a separately implemented every-conflicting-edge-pair verifier for n=3..150. The four-column insertion proof uses repeated matching seam columns and proves all n, not finite extrapolation. Thus index equals 9 at 3, 8 at 5,6, 6 when 4|n, and 7 otherwise.

## originality

PASS

Qualified PASS for complete all-order prism formula. Togni 2007 proves general product bounds and cycle-compatible constructions; Dara–Mishra–Narayanan–Tuza 2022 §5 gives overlapping exact cases and broader bounds, but accessible theorems/table do not directly assert the 7-color bound for all remaining odd prisms with the exceptional 5-case. An equivalent odd-prism classification in other strong-coloring literature remains possible.

## value

PASS

This resolves the exact strong chromatic index of a natural infinite cubic graph family and provides a structural four-periodicity obstruction plus repeatable explicit construction. The 5- and 6-prism finite exceptions are integral to the complete characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
