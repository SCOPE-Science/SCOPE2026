---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The Weyl combinatorics give w wprime^{-1}=w0, d=2, fixed torus equations t1=t4 and t2=t3, and d_BHS=26-2+5-1=28. In the actual local chart, Mowlavi’s q=1,(a,b)=(1,2) equation factors as F=(t2+lambda)A with dF_1=s1(dt3-dt4). Together with the two pre-existing torus rows, this raises the t-row rank from 2 to 3; modulo the existing row its class is a unit multiple of d(t1-t2), so the local-model tangent bound drops from 18 to at most 17. The Schubert chart has sole linear rank condition df=-dz41 and tangent dimension 5. BHS’s tangent comparison then adds 10 framing/deformation dimensions, yielding dim T_x X_tri<=27. No equality is claimed.

## originality

PASS

The primary source of the bad-pair equation explicitly leaves strictness of the BHS trianguline tangent upper bound open. The audited record combines that local-model equation with the BHS tangent-dimension bridge and a nonzero Jacobian class to obtain the first-cell strict inequality; no checked source stated that conclusion.

## value

PASS

The result addresses an explicitly stated open strictness question at the first/minimal bad-pair cell and isolates the extra tangent equation responsible for the drop. This is a motivated structural boundary case in the trianguline local-model program, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
