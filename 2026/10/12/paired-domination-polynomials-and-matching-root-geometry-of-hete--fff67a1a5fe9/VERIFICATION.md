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

# Reproducibility checks

`verify.py` uses only Python 3 standard-library modules. The actual executable content embedded beside this document was run from its package source path before inclusion; the captured standard output is embedded in `VERIFIER_OUTPUT.txt`.

It independently enumerates every candidate selected set of each explicitly constructed decorated graph; it checks domination and the existence of a perfect matching with separate routines, then compares the resulting coefficient array against a sum over base vertex supports. Exact families: every labeled base graph of orders one through four with each private-leaf multiplicity in \(\{1,2\}\), and every labeled base graph of order five with one private leaf per vertex. Further deterministic examples at orders five and six with heterogeneous attachments are **sampled**, not exhaustive. The program tests the cycle support-vs-matching multiplicity boundary and the path matching coefficients through nine base vertices.

The weighted Heilmann–Lieb root conclusion is established in the mathematical proof using the cited theorem, not certified by finite floating-point root computations. Computations alone cannot establish the universal formula, novelty, or value; independent external scientific validation is not performed.
