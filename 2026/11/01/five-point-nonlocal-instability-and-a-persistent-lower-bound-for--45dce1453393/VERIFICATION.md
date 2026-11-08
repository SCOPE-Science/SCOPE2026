---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The second-difference rows are independent, every active constraint subset has a strict KKT realization since D is surjective, and on its full-dimensional cell the Euclidean projector Jacobian equals H_A=I−B_Aᵀ(B_AB_Aᵀ)⁻¹B_A. Piecewise-linearity implies the global ℓ∞ two-input norm is max face absolute row sum. Independently enumerated all subsets with exact SymPy rational arithmetic: n=2 1, n=3 4/3, n=4 7/5, n=5 11/7 uniquely at active rows 1 and 3 and output center; n=6 91/57. The 5-site KKT witness is explicit. Block embedding proves monotonicity, and Green matrix inverse of tridiagonal diag 6/offdiag 1 for alternating active rows yields a limiting central row norm 1+1/√2; independently computed m=2,3,5,10,50 convergence to 1.7071067812. This is a constructive liminf, not a sharp unknown limit.

## originality

PASS

Meyer 2008 supplies general cone-projection active-face theory, and Yang–Barber's isotonic regression contraction pertains to first-order monotonicity cone. The convex sequence cone and its Euclidean objective under ℓ∞ perturbation do not preserve those isotonic nonexpansivity conclusions; exact 5-site extremizer and limiting lower obstruction are new relative to inspected statements.

## value

PASS

Pinpoints the first nonlocal separated-curvature amplification beyond adjacent constraints and shows it persists and grows with sample size. The exact natural small-instance instability and explicit asymptotic obstruction explain deterministic robustness limits of convex regression rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
