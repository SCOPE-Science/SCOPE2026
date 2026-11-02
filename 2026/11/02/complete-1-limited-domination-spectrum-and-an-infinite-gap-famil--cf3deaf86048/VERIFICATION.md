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

# Reproducibility and limits

Execute `python3 verify.py` from the unpacked research bundle. The program uses Python 3 and no third-party dependencies. It enumerates the ten recurrent state pairs, forms each weighted transition with the two explicit neighbour inequalities, and performs a **full polynomial determinant computation**, not numerical interpolation. It checks equality with the displayed factorization as integer polynomials in two indeterminates.

For \(n=3,\ldots,8\), it independently enumerates every graph vertex subset using the full adjacency definition, verifies the conditions of \(1\)-limited domination, and compares every size count to closed-walk transfer enumeration; this visits \(87{,}360\) candidate subsets in total. For \(n=3,\ldots,40\), it computes the cyclic-word transfer polynomial and checks the minimum, first three coefficients, and top-cardinality boundary conditions.

Expected exact completion line:

`VERIFY_OK determinant_monomials=16 exhaustive_assignments=87360 n=3..8 min_nearmin_profiles=3..40`

The proof for all lengths uses the trace bijection, an exact finite determinant identity and formal algebraic root expansions. Small-instance exhaustive tests do not in themselves establish unbounded-length claims. No external independent audit, formal proof assistant or historical novelty certification is claimed.
