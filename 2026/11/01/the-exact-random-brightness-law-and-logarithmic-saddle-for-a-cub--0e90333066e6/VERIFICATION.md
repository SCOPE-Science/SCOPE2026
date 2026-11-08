---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For 0<|epsilon|<=1/4 the support curvature tensor I+epsilon(∇²_S P+P I) is positive by the explicit Hessian norm and cubic bound, with width two by oddness. Published exact directional area b=pi-(pi epsilon²/4) product(1-n_i²) gives normalized Y=product(1-U_i²), independent of epsilon. Haar spherical coordinates S=|Z| uniform[0,1], Phi uniform imply Y=A(S)+B(S) sin²(2Phi) with A=s²(1-s²) and B=(1-s²)³/4; arcsine conditioning yields claimed entire CDF and differentiated density. The maximum T(s)=A+B occurs at s=1/sqrt(3), giving support [0,8/27]. On the sphere there are 6 quadratic minima, 8 diagonal maxima, and 12 nondegenerate saddles at 1/4 with local form 1/4+w²/4-alpha²; the coarea delta integral contributes 1/(2pi) log(1/|y-1/4|) per saddle, hence 6/pi total. Cap-area expansions yield endpoint slopes 3/2 and 9/2. Independent exact Dirichlet moments give 4/21,128/3003 and variance400/63063. Numerical checks are secondary, not the all-directions proof.

## originality

PASS

Known full directional brightness profile of precisely this cubic body was read and credited; it does not evaluate the Haar pushforward law, critical-density singularity, endpoint mass expansions or statistical moments. The published zonal cubic distribution has different harmonic/object and no twelve-saddle transition. General brightness/coarea work does not directly imply the exact evaluated special law. Best-of-knowledge originality concerns the computed distribution of a natural known directional function, with residual alternative-terminology priority risk.

## value

PASS

The natural random-direction brightness observable of a concrete smooth constant-width body has an exact distribution with a nontrivial saddle-driven interior logarithmic singularity. The singularity coefficient, endpoint densities and exact moments distinguish the tetrahedral cubic from previously solved zonal cubic; these are specific potentially reusable invariants of projection statistics, not a cosmetic parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
