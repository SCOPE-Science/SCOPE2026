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

# Verification and reproducibility

Run `python3 check_dodeca_sections.py` from the directory containing the included standalone file. It requires Python 3.10+ and the standard library only. The checked finite certificate explicitly constructs twenty scaled regular-dodecahedron vertices in \(\mathbb Z[\sqrt5]^3\), classifies thirty edges by the exact minimum squared distance \(24-8\sqrt5\), verifies ten antipodal axis pairs and all forty-five nonconcurrent great-circle intersection pairs, and generates the complete ninety-two sign-chamber masks. Every chamber's section side count, spherical corner count and exact algebraic interior-angle multiset is checked. Girard's spherical excess and an independent edge-crossing mean provide checks of the resulting probabilities.

Expected last line begins `CHECKS PASS`. Exact sign tests and all integer comparisons use pairs of integers as algebraic numbers; approximate trigonometric evaluation checks decimal presentation only. The argument about every spherical chamber having a pairwise circle corner proves the finite search is exhaustive. The script makes no unbounded enumeration or statistical-to-infinite inference. Exceptional normals on the original ten great circles are excluded as a measure-zero set. The proof has not been independently audited.
