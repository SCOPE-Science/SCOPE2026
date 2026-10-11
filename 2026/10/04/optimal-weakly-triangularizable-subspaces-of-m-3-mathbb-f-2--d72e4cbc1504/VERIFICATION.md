---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The finite classification was independently replayed from the definition. Exactly 352 of the 512 binary 3-by-3 matrices have split characteristic polynomial. Enumerating every reduced-row-echelon basis gives all 788035 six-dimensional subspaces and finds exactly 35 in which all 64 matrices are triangularizable; enumerating all 43435 seven-dimensional subspaces finds none. A separate exact conjugation replay over all 168 elements of \(\mathrm{GL}_3(\mathbb F_2)\) partitions those 35 spaces into orbits of sizes \(21,7,7\), matching the three displayed representatives. This establishes both maximality and exhaustive similarity classification independently of the saved certificate.

## originality

PASS

Originality passes. The complete open HTML of the 2026 characteristic-two paper was inspected. It explicitly identifies classification of optimal weakly triangularizable spaces as a remaining problem and says the methods for larger perfect characteristic-two fields fail for the field of two elements and require a different approach. The known dimension formula already covers \((\mathbb F_2,n=3)\) because the previously possible exception was only fields with cardinality strictly less than \(n-1\), but the larger-field structural classification does not cover this binary case. Fresh Resultary search found only the audited classification and adjacent binary matrix-space problems, not a prior 35-space/three-orbit theorem.

## value

PASS

The result addresses the smallest binary case specifically left outside the available structural methods. A complete classification of all optimal spaces, including exact conjugacy orbits, is a natural finite boundary for an active matrix-space problem and distinguishes whether exceptional binary similarity types appear.

The dated certificate retains the supplied scientific assessment, sources and limitations.
