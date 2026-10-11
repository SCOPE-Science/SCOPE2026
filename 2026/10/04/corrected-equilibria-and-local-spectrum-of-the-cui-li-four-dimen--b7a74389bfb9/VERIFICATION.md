---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Independent elimination from \(\dot p=0\), \(\dot w=0\), and \(\dot u=0\) gives \(v=-u\), \(w=-u^2/b\), and \(u(-2a+eu^2/b)=0\), yielding exactly the origin and the two stated nonzero branches. Substitution verifies all four stationary equations. Independent symbolic determinant expansion on \(u^2=2ab/e\) matches the claimed quartic exactly. At the source parameters it becomes \(\lambda^4+42\lambda^3-1200\lambda^2+32035\lambda-25800\); exact Routh arithmetic gives \(-82435/42\) and \(519058805/16487\) in the critical first-column entries, hence three sign changes. The primary PDF confirms the source’s erroneous coordinate and polynomial.

## originality

PASS

The introducing source prints a fourth equilibrium coordinate containing \(de-ce-2ad\) and a different nonzero characteristic polynomial. Direct stationarity instead gives \(de-ce-2a\), and no indexed correction was found. Earlier Qi-derived four-dimensional systems use different controller constructions and do not imply the stationary equations of this exact flow. Resultary returned the assigned current record itself as the strongest same-object hit; that self-hit is excluded from prior-art evidence.

## value

PASS

The correction changes the actual nonzero stationary points used in local analysis: at the published parameters the fourth-coordinate magnitude is about 28.912 rather than 260.210. The corrected quartic also determines the exact unstable dimension three. These are structurally important inputs for bifurcation, control, and numerical interpretation around the nonzero states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
