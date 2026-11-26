---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed the moment using H=A_theta* A_theta. Writing s2=xy+yz+zx and s3=xyz, tr H=t^2+u^2, the second elementary symmetric function of H is t^2u^2+(t^2-u^2)^2 s2, and det H=(t^6+u^6+2t^3u^3 cos(6 theta))s3, by the two directed-cycle terms in det A_theta. Newton's identity gives the claimed phase polynomial, whose maximum is achieved at theta=0 including zero coefficients. For sorted x>=y>=z, cubic Schur's gap is (x-y)^2(x+y-z)+z(x-z)(y-z); its zeros are exactly the uniform and equal two-edge profiles. Combining Schur with s2<=1/3 proves the minimum and strict equality regimes on either side of E/D=9/4. The D=0 case instead gives all and only boundary profiles. E/D=(1-q)^2/(1-2q) away from the center, strictly increasing for 0<q<1/2, and elementary bisection is not needed: the quadratic root and direct evaluation give t*=0.359741911255301. Endpoints and reflection t↔1−t are included. RESULT.md, VERIFICATION.md and the supplied checker were inspected; the checker was not executed, and finite grid checks are not used to justify the continuum claim.

## originality

PASS

The inspected papers give the same functional or an equivalent block formulation and general inequalities; the closest indexed cycle results give a phase formula or different Schatten-fourth minima. None inspected establishes the exact normalized three-cycle minimum with the claimed support transition and complete equality sets. The pass is for that classification, not for the functional, Schur's inequality, or exclusive ownership of the harmonic formula.

## value

PASS

The directed triangle is a natural first test for nonzero winding at Schatten order six. At fixed Hilbert–Schmidt energy the exact threshold distinguishes a uniform supported cycle from a broken path, resolves coexistence at the transition, and reveals the larger equality family at symmetry. This is a useful extremal benchmark that general upper bounds and fourth-moment path results cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
