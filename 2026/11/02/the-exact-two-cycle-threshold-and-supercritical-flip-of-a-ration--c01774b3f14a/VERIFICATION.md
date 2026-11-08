---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

On [0,1] f_r(x)=sin(pi x)/(1+rx) has fixed 0 (derivative pi) and exactly one positive fixed point by monotonic sin(pi x)/x and 1/(1+rx). Its multiplier crosses -1 at c=acos(-1/pi)/pi, r*=(sin(pi c)-c)/c². For any distinct two-cycle x<y, equality H(x)=H(y) for H(t)=t+sin(pi t), strict concavity and midpoint m(d)=acos[-d/sin(pi d)]/pi reduce full problem to scalar F(d,r). Its proved strict negative derivative for 0<=r<=r* and strictly negative endpoint at the boundary produce exactly one root below r*, none at/above. Even Taylor expansion yields d~sqrt((r*-r)/C), C>0, and critical flip normal form gives return multiplier 1-4k(r*-r)+O((r*-r)^1.5), k>0. Independent high precision values at representative parameters and near r* checked r*~0.94810546376 and asymptotic multipliers. Sampling was not used for exhaustive root count.

## originality

PASS

Best-of-knowledge qualified: Zhu et al (2023) introduce exactly the normalized family, derive the positive fixed point and sufficient instability criterion and provide numerical dynamics. The claim here is the distinct all-positive-parameter count of unordered primitive 2-cycles and supercritical normal-form coefficients. Indexed original primary mathematical sections inspected show no implication of this global exhaustive count. A direct complete publisher document was rate limited, so historical coverage outside available sections remains a genuine risk.

## value

PASS

An all-parameter exact census of primitive period-two orbits, including zero-at-threshold boundary and a nondegenerate square-root flip and local stability, is the natural first periodic-orbit classification for a previously introduced nonlinear interval map. It sharpens earlier numerical/threshold diagnostics without claiming higher-period/global behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
