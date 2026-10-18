---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the printed Fu-Xu-Xiao vector field J0=[[0,alpha,0,0],[-10,0,1,0],[0,0,0,1],[0,1,0,0]], independent symbolic expansion gives det(lambda I-J0)=lambda(lambda^3+10 alpha lambda-1). For alpha>0 this cubic has one positive real root and a conjugate pair with real part -r/2; zero is simple. The exact normalized left/right eigenvectors ell=(1,0,0,-alpha), v=(1,0,10,0) give ell^T v=1, ell^T J0=0, J0v=0. Direct Hessian evaluation B(v,v)=(20p,-20,2,0) and projection yield center coefficient (1/2)ell^TB(v,v)=10p. At p=1/5 this is 2, giving xi(t)~-1/(2t) on the negative attracting local center branch. The result is local, not a statement about a distant attractor.

## originality

PASS

Source-specific checks of the exact vector field, eigenvalues, correction/erratum notices and center-manifold aliases, plus five independently queried Resultary mathematical records, found no earlier statement of this specific zero factor plus its nonlinear center drift. The primary article claims a contradictory nonzero four-eigenvalue spectrum at the origin.

## value

PASS

Correcting a published local spectral classification changes the equilibrium from purportedly hyperbolic to a one-center saddle, and the explicit nonzero quadratic coefficient identifies one-sided slow dynamics; this is motivated local structure, not a mere formatting/normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
