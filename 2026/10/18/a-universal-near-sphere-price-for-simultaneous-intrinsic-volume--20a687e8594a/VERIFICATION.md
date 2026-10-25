---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For d>=3 the individual curvature-weighted random-inscribed-polytope leading errors have functionals I_j(rho)=integral kappa^(1/(d-1)) H_(d-j) rho^(-2/(d-1)) dS. Holder with beta=(d-1)/(d+1) gives individual M_j and density G^beta/int G^beta for every simplex mixture G=sum lambda_j w_j/M_j. Concavity and directional KKT at simplex maximum prove exact global inf-density/max-objective=minimax=max-simplex F and uniqueness of common optimal density. Q=1 forces coincident endpoint densities kappa^[d/(d+1)] and kappa^[1/(d+1)], hence constant Gauss curvature and a sphere. Uniform second-order expansion of individually normalized v_j cancels all unknown individual second-order terms; first-order curvature coefficients r_j=(d-j+1)/(d-1), endpoint range one, and Popoviciu give max variance 1/4. Coefficient Var(h)/(4(d+1)), equal endpoint mixture for nonconstant h, density correction (h-mean)/2. For spheroid Gauss derivative (d+1)u1^2-2, fourth moments produce (d^2-1)/[2d^2(d+2)]. All asymptotics concern leading N^(-2/(d-1)) errors; no finite-N minimax interchange. Original exact rational checks independently reproduced d=3,4,6,9 spherical coefficients.

## originality

PASS

Hoehner Theorems 3.1 and 3.4 give precisely the known curvature error inputs/individual densities and qualitative rigidity, respectively. They do not state the finite-dimensional worst-relative-loss minimax dual or its universal sharp quadratic second variation for one common density. Previously published Hellinger gap is a different distance between endpoint optimizers, not an exact multiobjective worst-regret optimum. Best-of-knowledge original incremental quantitative theorem.

## value

PASS

The precise cost of forcing one boundary sampling density to approximate ALL intrinsic-volume errors is a natural optimization problem raised by single-density rigidity; exact global dual, sharp second-order deficit, and endpoint-only local active weights quantify a nontrivial loss and boundary stability, not a parameter renaming or numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
