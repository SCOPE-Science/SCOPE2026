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

The bundled `verify.py` uses only the Python standard library and exact rational arithmetic. It reconstructs the characteristic polynomials of the two printed equilibria from \(\lambda I-J\), checks the right and left zero eigenvectors at the origin, and evaluates the Hessian contraction giving the center coefficient.

Expected terminal output:

`VERIFY_OK`

For the accepted claim, the exact checks are \(\chi_0(\lambda)=\lambda^4+(10/7)\lambda^2-\lambda\), \(J_0v=0\), \(\ell^TJ_0=0\), \(\ell^Tv=1\), and \(\tfrac12\ell^TB(v,v)=2\). The sign classification of the nonzero spectrum is analytic: \(g'(\lambda)=3\lambda^2+10\alpha>0\) for \(\alpha>0\), with \(g(0)<0<g(1)\).

The verification is local to the printed autonomous vector field. It does not numerically reproduce the article's global attractor, controller, or circuit simulation.
