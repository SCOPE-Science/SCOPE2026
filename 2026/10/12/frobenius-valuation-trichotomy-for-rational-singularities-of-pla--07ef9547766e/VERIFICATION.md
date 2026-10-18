---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed affine partial derivatives f_x=1+a^r(k-b), f_y=a^{r+1}-b^r and rational-point parametrization t=b/a; no infinity singularity from line derivative. Frobenius translation produces zero coefficients below degree min(s,q)+1; for s<q tangent slope roots of z^{s+1}-z+t^{-N} are squarefree; for s>q U^q V-U V^q gives q+1 rational directions; at s=q derivative of P_h,lambda has unique repeated-root candidate and condition h²+lambda(h+1)=0. Independently factored mod 5 exceptional witness (p,q,r,t)=(5,5,5,3) as one simple plus one 5-fold tangent, and mod 3 (3,3,3,1) as one 4-fold tangent; distinguishes repeated tangent from unknown analytic branch number. Only rational singular points are classified.

## originality

PASS

Best-of-knowledge new local singularity trichotomy for exactly the curve family of Asgarli–Ghioca, expressly retaining their rational singular-point first-derivative classification. The read primary 2023 paper gives a rational singularity exclusion test but does not in the inspected treatment derive these all-p-dividing-r tangent cone orders and collision patterns.

## value

PASS

Multiplicities, tangent directions and normalization-branch splitting at rational singularities are fundamental local invariants of plane-filling curves. The sharp valuation boundary s=q and degenerate critical tangent pattern clarify a natural open parameter regime, rather than an arbitrary finite-field example or cosmetic derivative calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
