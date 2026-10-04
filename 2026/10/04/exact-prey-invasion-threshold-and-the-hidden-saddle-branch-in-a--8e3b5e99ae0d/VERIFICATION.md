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
The proof is analytic and is based directly on the printed model equations.

Checked analytically:
- cancellation of the interaction terms gives the quadratic ellipse relation;
- for every \(N\in(0,K)\), the ellipse has exactly one positive predator root \(P_+(N)\);
- substitution into the prey equation gives the exact attack-rate graph \(A(N)\);
- \(\lim_{N\downarrow0}A(N)=cr+r/H\), equal to the predator-only prey-invasion threshold;
- the first correction to \(A(N)\) is positive;
- the Jacobian determinant along the small-\(N\) branch is negative to leading order.

Checked computationally by `verify.py`:
- the source reference parameters give \(a_*=0.208\);
- small positive prey values produce \(A(N)>a_*\);
- at \(a=0.8\) there are two positive equilibria satisfying the original equations;
- the smaller-prey equilibrium is a saddle;
- the larger-prey equilibrium is locally asymptotically stable.

The computation does not replace the general proof and is not used to infer an infinite-domain statement.
