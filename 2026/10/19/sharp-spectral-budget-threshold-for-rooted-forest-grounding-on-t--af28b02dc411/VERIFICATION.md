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

The proof in `RESULT.md` is analytic for all connected, simple, vertex-transitive cores of order at least three. It establishes positive definiteness, strict global concavity, automorphism-induced symmetry, an exact Schur determinant, monotonicity and endpoint signs of the spectral threshold, and the sharp complete-core extremum.

Replay the included standalone numerical and symbolic checks with `python verify_corona.py` (requires NumPy, SciPy, SymPy). The direct run returned `VERIFY_OK 1216`. Finite matrix and numerical optimization checks do not certify all graphs and budgets, and the stated theorem does not depend on their exhaustiveness. The exact symbolic checks independently evaluate the clique and four-cycle threshold expressions.

Limits: no independent audit has been performed; no statement is made for unequal vertex prices or arbitrary non-vertex-transitive cores. A possibly unindexed equivalent theorem has not been excluded by a universal literature search.
