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
The proof is self-contained. The three critical checks are: (i) each normalized norm error lies in \([0,2\rho_X(h)]\), uniformly in unit inputs; (ii) finite-exponent power means have the same differential \((u+v)/2\) at \((1,1)\) and bounded Hessian for \(h\le1/4\); (iii) swapping unit inputs negates the norming-functional defect, so the infimum and supremum coefficients are the opposite signs of the same \(\kappa_X\). Symmetric norming-functionals generate a bilinear form whose diagonal is the norm squared.

The explicit \(\ell_4^2\) witness uses \((1/2)^4+15/16=1\) and \(j(y)(x)=(1/2)^3\); it checks only strict non-Hilbertness, not an optimal coefficient. The exact Hilbert maximum-mean formula supplies a separate excluded-endpoint counterexample. No symbolic or numerical package is necessary for the theorem, and no independent audit has been performed.
