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

The proof relies on four reproducible reductions: (1) direct bracket-based automorphism normal form; (2) exact principal-unit multiplication and scaling; (3) norm surjectivity and fixed-unit splitting for multipliers whose order divides \(q-1\); and (4) Burnside's lemma and Frobenius power equations in characteristic \(p\). No step relies on classification software, a timeout, or incomplete infinite enumeration.

Run `python3 verify_cyclic_leibniz.py` in a standard Python 3 environment. It directly enumerates automorphisms represented by scalar multipliers and truncated-unit coefficient tuples, composes group elements, computes each exact element order, and obtains the number of classes by counting commuting pairs divided by group order. No external dependencies are required. The finite-field model of size four uses \(\mathbb F_2[x]/(x^2+x+1)\).

Actual successful checks include \((q,n)=(2,2),(2,3),(2,5),(3,2),(3,3),(3,4),(4,3),(4,4),(5,2),(5,3),(5,4)\). The result text is `CYCLIC_LEIBNIZ_CENSUS_OK` after all order distributions and class counts match. These finite computations do not prove the universal theorem; the symbolic group and norm proof does.

No separate reviewer or independent mathematical validation has been performed. Absolute literature priority remains open, especially for broader theorems concerning principal-unit semidirect products.
