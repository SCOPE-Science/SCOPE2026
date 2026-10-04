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

The proof was checked symbolically from the primary source factorization. In particular, the negative-endpoint crossing was re-expanded as \((1-\beta)^2=n(n+\beta)\), giving \(\beta=1+n/2-\sqrt{n(4+5n)}/2\) in \((0,1]\), and the positive crossing reproduces \(1-\sqrt p\). Direct root evaluation confirms the endpoint formulas for \(0<\beta<2\).

The bundled `verify_sign_aware_dgt.py` checks: (i) direct polynomial roots against the closed endpoint radii; (ii) branch-intersection identities; (iii) dense minimization over a grid of \((p,n)\) values; and (iv) the negative-only two-agent example. The numerical checks support the algebra but do not replace it.

Unproved/out-of-scope limits: heterogeneous curvatures, directed or time-varying mixing, vector-valued noncommuting Hessians, and uncoordinated steps. Literature originality remains subject to the explicit access risks recorded in `AUDIT.json` and `REVIEW.md`.
