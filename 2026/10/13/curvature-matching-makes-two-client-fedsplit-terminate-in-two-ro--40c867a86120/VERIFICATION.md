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

For two equally weighted scalar strongly convex quadratic clients, the original FedSplit proximal-reflection formula reduces exactly to z1+=r1*z2+(1-r1)*b1 and z2+=r2*z1+(1-r2)*b2, with rj=(1-s*aj)/(1+s*aj). Subtracting the unique affine fixed point yields A=[[0,r1],[r2,0]], A^2=r1*r2*I. For s>0 and aj>0, |rj|<1; at s=1/a1 or 1/a2, A^2=0 for every initial pair, giving exact two-round client-state and averaged primal convergence. Independent rational arithmetic for a1=1,a2=9,b1=-2,b2=1 independently confirmed both choices s=1 and s=1/9 from three distinct common starts; the fixed-point average is 7/10. The geometric-mean rate is strictly positive for unequal curvatures. Checks establish the scalar exact-prox regime only.

## originality

PASS

Pathak and Wainwright (arXiv:2005.05238, algorithm, Proposition 3 and Theorem 1) define the same update and general convergence guarantees; their examined mathematical statement does not identify the two-client cross-reflection nilpotency. General Douglas--Rachford rate/metric-selection papers concern broad convergence bounds; a uniform contraction estimate is not the asserted exact instancewise annihilation. Resultary splitting results found use different algorithms/matrices. The two-client specialization is elementary and a literature not indexed as FedSplit may already contain it; originality is best-of-knowledge rather than priority certification.

## value

PASS

Finite communication termination is a meaningful algorithmic structural boundary in the exact FedSplit method, and the two-round nilpotent setting contrasts with the nonzero geometric-mean-tuned linear factor when a1 != a2. The statement is an exact special-case benchmark, not a claim of practical robust parameter selection or multidimensional finite termination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
