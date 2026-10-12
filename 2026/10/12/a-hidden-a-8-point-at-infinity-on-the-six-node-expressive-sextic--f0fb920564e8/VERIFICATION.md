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
The accompanying `verification/verify.py` uses exact rational polynomial arithmetic. It checks the degree-six homogeneous parametrization, confirms that its only point over \(L_\infty\) is \([1:0:0]\), reproduces the difference-resultant factorization from Example 8.4, and verifies the local valuation identity
\[
\operatorname{ord}_s(Y/X)=2,
\qquad
\operatorname{ord}_s\bigl(Z/X+8(Y/X)^3\bigr)=9.
\]
The second order is established from the exact factorization of \(ZX^2+8Y^3\), not from floating-point series fitting.

The checker also verifies \(p_a=10\), \(6\cdot1+4=10\), \(\mu(A_8)=8\), \((\overline C\cdot L_\infty)_p=6\), and the \(L_\infty\)-polar value \(8+6-1=13\).

The source's independent mathematical ingredient used here is its proof that the affine self-intersections are six simple hyperbolic nodes. The checker reproduces the displayed resultant but does not attempt to replace that transversality proof with numerical root approximations. The analytic implication “multiplicity-two unibranch with Puiseux pair \((2,9)\) is \(A_8\)” is standard characteristic-zero plane-branch theory and is explained in `RESULT.md`.
