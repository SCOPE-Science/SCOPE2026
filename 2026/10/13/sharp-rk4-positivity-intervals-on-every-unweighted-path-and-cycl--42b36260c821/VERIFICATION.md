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

For R(z)=1+z+z²/2+z³/6+z⁴/24, the claimed matrix is T_G(h)=R(−hL_G). Taylor integral remainder gives R(−x)>0 for x>=0, hence all diagonal entries stay positive. Four-step walk locality reduces every path/cycle distance-one and -two entry to seven cubics/five quadratics; their Bernstein coefficients on [0,2/3] are positive. The enumerated distance-three coefficients vanish at 2/3,4/7,1/2 for large enough paths/cycles and become strictly negative thereafter. P2,P3,C3,C4,C5 have an explicitly checked unique positive cubic root with other off-diagonal entries nonnegative globally. Independent exact rational matrix-power enumeration of paths and cycles through n=12 corroborated every exceptional and stable cutoff; the infinite classification follows from walk locality, not those tests.

## originality

PASS

PASS best-of-knowledge: complete necessary-and-sufficient endpoints for every unweighted finite path and cycle under classical RK4, including nonmonotone cycle sizes, extend beyond general SSP positivity-radius and unrelated numerical schemes. Fekete–Ketcheson–Lóczi Section6.2 handles a periodic heat stencil via two-stage methods, not this exact 4-stage classification.

## value

PASS

Sharp timestep regions for a standard fourth-order integrator on fundamental diffusion graphs matter for positivity preservation. The complete family threshold and genuine cycle-size nonmonotonicity (C5>C4, C7>C6) distinguish the exact result from generic sufficient SSP guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
