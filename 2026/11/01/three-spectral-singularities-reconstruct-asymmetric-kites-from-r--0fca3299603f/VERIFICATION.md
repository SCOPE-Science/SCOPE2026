---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For vertices (±r,0),(0,−pr),(0,qr), r>0, 0<p<=q, projection support yields w/r=2cos θ (θ<α=atan(1/q)), cosθ+qsinθ=Rcos(θ−τ) (α<θ<β=atan(1/p)), and (p+q)sinθ (θ>β) under Haar θ∈[0,π/2]. The analytic change of variables supplies exact density f(w)=(2/π)∑ inverse-sqrt branch multiplicities; no atoms. In 1<q<sqrt3 and 0<p<sqrt(1+q²)−q, interior middle maximum exists and three distinct upper-cutoff divergences z1=r(p+q)<z2=r√(1+q²)<z3=2r have multiplicities 1,2,1 and limiting coefficients 2/π,4/π,2/π. Algebraic inverse r=z3/2, q=√((z2/r)²−1),p=z1/r−q is smooth away from boundaries. Independently checked switch ordering, the three singular heights and limiting amplitudes for p=1/4,q=3/2,r=1.7 at two offsets. Numerical checks corroborate but the branchwise proof covers all parameters.

## originality

PASS

Qualified PASS for full kite forward density/phase diagram and exact inverse reconstruction in ordered three-peak subregion; first-two-moment width optimization and symmetric polygon distribution-inverses cover distinct statements.

## value

PASS

A canonical low-parameter asymmetric convex body is uniquely recoverable from unlabelled projection statistics on an explicit open domain; singular locations identify geometry without directional labels and show precise phase boundaries where identifiability mechanisms fail. Exact law and inverse have direct geometric-statistical meaning beyond a toy evaluation of a known width formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
