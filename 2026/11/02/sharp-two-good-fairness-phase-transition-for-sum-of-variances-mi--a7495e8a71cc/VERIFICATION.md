---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The full feasible polytope can be verified directly. Adding the two proportionality surpluses gives (b−a)(d−c)≥0, so put h=d−c≥0. The separate constraints are y h≤f−e≤x h, where x=1−2a>y=1−2b>0. Thus p decomposes as 2c S + 2e Q plus a nonnegative residual supported on D,F with F/D ratio in [y,x]; the residual splits between H1 and H2 (and vanishes if h=0). This proves the four-vertex hull and supplies the corrected intermediate identity for the imprecise adding/subtracting sentence in RESULT.md line 22; it does not change the Finding. Direct variance evaluation gives Φ(Q)>Φ(S), Φ(H1)>Φ(H2)=Φ(R), and 4(Φ(R)−Φ(S))=g_x(y). The law of total variance adds a strictly positive between-mean term for any nontrivial mixture of the two tied candidates, whose first mean utilities differ. End signs g_x(0)<0<g_x(x) and strict concavity give one interior crossing. The two one-good-each allocations are EFX; in F, agent 1 has utility zero, fails EF1 and falls below its positive MMS. The exact witness values are 17/100 and 13/80 with t=5/6. These arguments apply on the stated open chamber, not its boundary. The frozen verifier and recorded 330 finite exact-rational checks were inspected, not executed; the universal conclusion is analytic.

## originality

PASS

The strongest prior source already gives the same failure mechanism and a unique R optimizer at a specific point in exactly this chamber. No originality is credited for existence of failure, that support mechanism, or reducing variance minimization to extreme points. The supported distinct result is the necessary-and-sufficient phase classification of all parameter pairs in the open chamber, including the single crossover and exact tie with no optimal mixtures.

## value

PASS

The minimal setting in which the proposed fairness objective was known to fail lacked a boundary identifying when the objective actually loses ex-post fairness. The classification determines both sides and distinguishes coexistence of two optima from an optimal interpolation at equality. This is a motivated exact gap in understanding the objective, not a new numerical witness or a claim for larger allocation problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
