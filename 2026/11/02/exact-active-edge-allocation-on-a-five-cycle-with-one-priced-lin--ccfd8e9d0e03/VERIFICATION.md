---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For ordinary combinatorial weighted Laplacian C5, objective lambda_2 with positive linear budget, 0<q<16 and B>0, positive homogeneity reduces optimization to minimizing cost for lambda_2>=1. Reflection-even and odd two-dimensional characteristic polynomials give b=(2a-1)/(5a-3), t=(2a-1)^2/(5a^2-6a+2) and both low eigenvalues exactly 1. The exact sixth-degree Bernstein coefficients are all negative on z=5a-3 in [0,1], proving Q(a) strictly decreasing on (sqrt(2/5),4/5) from 16 to 0. Remaining eigenvalues lie above 1. Positive dual weights alpha,beta multiply squared edge differences of normalized unit even and odd eigenvectors to equal the individual edge prices, so any independent nonnegative conductances with gap>=1 cost>=C=alpha+beta. Equality makes both eigenvectors eigenvalue-one eigenvectors; their five vertex equations force all conductances individually, proving uniqueness even without imposed symmetry. Independently checked the exact q=25/16 instance a=.7,b=.8,t=.64,C=4 and Laplacian low double eigenvalue=1. The bundled verify.py symbolic identities, Bernstein representation and 1500 random comparisons were read; random comparisons alone do not prove globality. Endpoint q=0,16 excluded.

## originality

PASS

PASS, qualified. Sun/Boyd/Xiao/Diaconis (SIAM Review 2006) Section 5.3 already formulates the same continuous-time SDP and dual and handles equal-price cycles plus dimension-two duality for general cycles; screening at q=16 is not claimed novel. It does not provide this exact one-priced five-cycle allocation for all subcritical q with uniqueness against asymmetric designs. The 2004 fastest mixing chain paper concerns discrete-time SLEM. Specialist Fiedler 1993 remains an uninspected possible predecessor.

## value

PASS

This supplies a sharp globally unique conductance design with continuously variable edge price, exact algebraic inverse and active-edge/edge-screening transition. Spectral-gap allocation is a natural convex graph optimization problem, and the concrete nontrivial price law plus unrestricted symmetry-breaking exclusion improves on equal-price cycles or SDP solvability, providing usable explicit network-design data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
