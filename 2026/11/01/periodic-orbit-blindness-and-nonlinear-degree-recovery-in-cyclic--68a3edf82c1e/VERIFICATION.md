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

# Verification and limits

The proof is self-contained in `RESULT.md`; the Python checker is supplementary. Run `python checks/verify.py` in an environment with Python 3 and SymPy. The program was executed on the embedded source and returned six `PASS` lines. It checks exactly \(499\) scalar root-count examples, \(25\) polynomial-composition identities, the diagonal three-step reduction for degrees \((2,3,4)\), \(768\) multiplier identities, \(270\) moment-indexing checks and positive-lag vanishing in the selected degree and lag range. The proof separately establishes these statements for **all** integer degree triples at least two, every positive iterate and arbitrary polynomial-mode indices.

No finite calculation establishes an infinite-time claim merely by testing, and no computation is presented as independent validation. The theorem does not cover noninteger map parameters or the behavior of numerical finite-precision simulations. Source comparison included the accessible mathematical text of the principal one-dimensional correlation paper and the relevant public portions of the original three-dimensional map paper; unexamined publisher-hosted portions are a residual priority risk.
