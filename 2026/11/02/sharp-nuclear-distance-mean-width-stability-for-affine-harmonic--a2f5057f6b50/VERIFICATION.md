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

# Verification of the sharp affine mean-width theorem

The proof in RESULT.md establishes the all-dimensional inequality and its complete equality class directly. The essential steps are (i) exact support function and singular-value reduction, (ii) nuclear distance by singular-value perturbation, (iii) superadditivity of a strictly convex scalar deficit, (iv) a sharp chord inequality for the one-coordinate contraction, and (v) evaluation of the Beta law of a uniform sphere coordinate. For any input matrix singular values \(s_j\in[0,1]\), all inequalities hold pointwise in almost every sphere direction; no finite grid is substituted for this proof.

An optional fully standalone standard-library CHECKER.py can be run as `python CHECKER.py`. It checks the dimension-three and dimension-four beta evaluations, deterministic grids for the critical scalar inequalities, the global strict inequality at test anisotropies, and the codimension-one equality case using a deterministic sphere quadrature. All such finite checks are supplementary only. The results make no assertion about general nonlinear harmonic maps.

Independent mathematical audit has not been performed.
