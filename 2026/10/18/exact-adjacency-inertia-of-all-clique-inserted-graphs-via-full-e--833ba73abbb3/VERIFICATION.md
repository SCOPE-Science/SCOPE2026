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

# Reproducibility

The package contains `verify.py`, a standalone Python 3 standard-library verifier, and `verification_output.txt` containing its expected stdout. Execute `python3 verify.py` from the directory containing the files. The verifier constructs adjacency matrices directly from edge-subdivided graphs and computes their inertia by rational congruence elimination without floating-point eigenvalues.

It exhausts **all connected labelled graphs with 2 through 5 vertices**, comprising \(1+4+38+728=771\) graphs, then checks 126 extra structured connected graphs. All 897 formula comparisons passed. This computation was run before packaging and its output was recorded; successful finite enumeration is not asserted to prove an infinite theorem. The proof in `RESULT.md` establishes the unlimited graph-order claim via the incidence/saddle-point reduction, including the exact boundaries \(m=n-1\), \(m=n\), and \(m=n+1\).

# Known limits

This result is confined to finite connected simple graphs subdivided at every original edge once. The older full-spectrum formulas for regular clique-inserted graphs are not new. Independent audit and exhaustive bibliographic-priority verification have not been performed; one earlier publisher full text was not materially accessible.
