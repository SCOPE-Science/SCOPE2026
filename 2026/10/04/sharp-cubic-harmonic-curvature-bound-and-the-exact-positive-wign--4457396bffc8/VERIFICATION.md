---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

On a great circle, a harmonic cubic is A cos(3t)+B sin(3t)+C cos(t)+D sin(t), and <Q_q(u)v,v>=p''(0)+p(0)=-8A. The third-frequency amplitude is an exact six-point alternating average and is at most ||q||_infinity, giving the sharp universal factor 8; Re(u1+i u2)^3 attains it. For q_plus, |q_plus|<=a^2 b=(1-b^2)b<=2/(3sqrt(3)), and the displayed orthonormal great circle is exactly a pure third harmonic of that amplitude, so M_plus=16/(3sqrt(3)). Oddness gives both spectral signs, yielding the exact semidefinite and positive-definite epsilon thresholds. Endpoint invariant arithmetic matches the source normalization.

## originality

PASS

Originality passes. Zwierzyński defines q_plus and the support-curvature operator and proves convexity only for sufficiently small perturbations, leaving its operator maximum symbolic. The related SCOPE result solves a different cubic on S2. No checked source gives the universal degree-three bound or the exact q_plus radius.

## value

PASS

The result evaluates a geometric admissibility radius left symbolic in the motivating source and simultaneously supplies a reusable sharp dimension-free operator inequality for every cubic spherical harmonic. It turns a local existence statement into a complete one-parameter convexity classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
