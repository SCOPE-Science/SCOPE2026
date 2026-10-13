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
# Verification

`verify_book_power.py` independently implements the graph and the standard power-domination dynamics. For each \(2\le n\le7\), it exhausts all \(2^{2n+2}\) subsets, compares simulation against the theorem's structural criterion, compares every cardinality coefficient with the closed polynomial, checks the total \(3\cdot4^n+(n+3)3^{n-1}\), and checks the minimum singleton count.

The finite replay is not used to infer the theorem for larger \(n\). The infinite claim is justified by the proof's two cases and the permanent-stall argument when at least two pages are untouched. The verifier has no external dependencies beyond the Python standard library.
