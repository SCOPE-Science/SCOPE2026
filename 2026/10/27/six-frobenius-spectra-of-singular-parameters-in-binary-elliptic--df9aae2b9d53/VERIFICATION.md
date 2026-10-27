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

The accompanying sources `enumerate_pencils.py` and `singular_parameters.py` were run in their delivered directory with Python 3 and SymPy. `pencil_catalogue.json` records all enumerated smooth masks, qualifying unordered triples, thirteen projective-orbit representatives, and exact rational-point profiles. `singular_spectra.json` records each representative's irreducible singular-parameter equations, degree multiset and orbit weight. Saved standard outputs permit exact replay comparisons.

Geometric smoothness is determined by exhaustive exact evaluation on all four charts over the degree-four finite extension. The degree-four extension suffices by the derivative-degree lemma in `RESULT.md`. Groebner elimination over \(\mathbf F_2\), followed by irreducible polynomial factorization, determines singular parameter values in the algebraic closure; the independently implemented iterated resultant cross-check agrees for all thirteen representatives. The finite enumerations are exhaustive for the exact scope stated, not experiments over an unbounded domain. Results do not compute Kodaira types, singular-fibre multiplicities, or analogous spectra over larger fields.
