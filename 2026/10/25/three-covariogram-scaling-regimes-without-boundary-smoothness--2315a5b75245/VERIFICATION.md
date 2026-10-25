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

# Reproduction and verification

The proof is contained in `RESULT.md`. The new mathematical identity is a pointwise scalar equality for the exact radial smoothing, with the radial differential and surface measure conversion used to transfer it to arbitrary convex bodies.

The standalone `check_square.py` uses SymPy to establish the zero-order, first derivative and second derivative of the scalar gap at zero symbolically, and NumPy midpoint quadrature (200,000 angular nodes) to evaluate the original radial integral for the nonsmooth square \(K=[-1,1]^2\). Run with `python check_square.py` in an environment containing SymPy and NumPy. The checks passed when run on the packaged script before delivery.

Quadrature is finite and is evidence only for the example; correctness of the all-convex-body theorem relies on the mathematical proof and not on these samples. The normal-based integrals and local uniform estimates have not been independently audited. The exact square gauges used are \(H_K(y)=2(|y_1|+|y_2|)\), \(Q_K(y)=4(y_1^2+y_2^2)\), and \(\Phi_K(y)=4[\log\cosh(y_1/2)+\log\cosh(y_2/2)]\).
