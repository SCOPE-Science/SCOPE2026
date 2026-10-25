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

The general proof is given in RESULT.md. The reproducibility script checks the characteristic-five instance only:

- the derivative of \(t^5+t^2+t\) over \(\mathbf F_5\) has its only root at \(t=2\), where the polynomial is nonzero, so the form is squarefree;
- the local expansions give critical orders \(m=2\) and \(m=3\);
- the numerical semigroups \(\langle2,5\rangle\) and \(\langle3,5\rangle\) have respectively \(2\) and \(4\) gaps;
- the delta sum \(2+4=6\) equals the arithmetic genus of a plane quintic.

These finite checks do not prove the universal theorem. The general proof uses the Jacobian criterion, the degree \(p-2\) of the critical divisor, the local monomial normal form, and the plane-curve genus formula. Independent audit and independent validation have not been performed.
