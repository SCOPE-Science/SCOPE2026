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

The algebraic argument uses the unique primitive relation in the unsigned incidence matrix of the dumbbell graph, the elementary critical sets of disjoint-support monomials, squarefree Veronese monomial syzygies, and Serre's normality criterion. See `RESULT.md` for precise assumptions and proof.

Run `python3 check.py` with a standard Python 3 interpreter. The checker constructs the edge lattice relation afresh, tests every coordinate zero/nonzero support in seven parameter triples, compares finite Hilbert-function coefficients against the claimed formulas, and calculates exact rational Hessian ranks. It terminates with `VERIFY_OK` when all assertions pass.

These finite checks do not establish arbitrary-parameter or positive-characteristic statements. No full nonreduced Jacobian scheme, conductor, or nongeneric local models are verified or claimed.
