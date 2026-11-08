---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Proof reconstructed: exact flow on each linear saturation region gives return map P and derivative exp(3pi-10.5 E), with E full exterior residence; threshold E*=2pi/7. The frozen center rational brackets and interval verification implementation were inspected; source Hu-Chen Appendix A.3 supplies transverse event order on broad shooting intervals, and new narrower interval inequalities give signs of P(y)-y and E entirely on J1,J2,J3. A fresh independent high-accuracy scipy solve_ivp integration recovered return-displacement signs, approximate E 0.898414,0.8578,1.0023 and multipliers near 0.9915,1.517,0.333, plus central half-period zero at about -0.57902247 with repelling multiplier ~1.004. Antisymmetry Q=-flow(pi), P=Q^2 gives paired orbits and same multipliers; strict inequalities imply local persistence. Numeric integration is corroboration only; the rigorous no-extra-crossing premise is imported from cited primary source and full directed interval proof remains the final certificate. No claim there are exactly seven or no other attractors.

## originality

PASS

Best-of-knowledge independent comparative result: Hu-Chen proves seven isolated periodic orbits; a sign-changing isolated zero can have multiplier exactly one. The new result proves nonunit multipliers for six, four attracting / three repelling including the known central multiplier; it is stronger but not automatic from prior statements. No negative search has been used as a novelty proof; the inaccessible/uninspected historical risk is explicit.

## value

PASS

For a canonical piecewise-linear saturating forced oscillator with known seven isolated cycles, rigorous strict multipliers distinguish four attracting and three repelling cycles and prove robust persistence. Isolation does not imply hyperbolicity; these stability classifications materially strengthen the primary result without claiming a global maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
