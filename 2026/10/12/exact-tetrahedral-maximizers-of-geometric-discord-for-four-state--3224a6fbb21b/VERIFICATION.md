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

Using traceless diagonal 4x4 operator completeness in the qubit-register Hilbert–Schmidt discord formula, the classical-register centering terms cancel and G=(1/4)sum_a r_a r_a^T. For four unit Bloch vectors tr(G)=1, so lambda_max(G)>=1/3 and D_G<=(1/8)(1-1/3)=1/12. Equality RR^T=4I/3 implies I-(3/4)R^TR=ss^T/4 with s_a in ±1, so all maximizers are signed regular tetrahedra; this handles the continuous Bloch optimization. The two QRAC Walsh vectors have norm squared (16-(w·s)^2)/3<=16/3; measurement optimization gives P_av<=1/2+1/(2sqrt(3)), attained at unflipped tetrahedron; this is below optimal 1/2+1/(2sqrt(2)). Independently replayed exact rational Gram and sixteen sign choices; sign enumeration only after proof reduces all continuous maximizers.

## originality

PASS

Yao et al 2012 prove a general 1/12 eigenvalue bound and numerically approximate its sharpness; Appendix A does not provide exact four-state equality classification or the optimal QRAC ceiling restricted to that equality class. Mančinska–Storgaard analyze QRAC Bloch success geometry, without the quantum discord maximization. General unit-norm tight-frame classification alone does not itself identify which QRAC geometric-discord states maximize and their exact incompatible success ceiling without combining the discord identity and Walsh formula. Semantic Resultary searches found related discord/QRAC but no dominating same-claim theorem.

## value

PASS

Closes an explicit analytic gap left as numeric simulation in a standard two-to-one QRAC–discord toy model: determines entire continuous maximizer locus and a strict operational tradeoff with best coding success, rather than merely a bound or one tetrahedral example. The natural four pure encodings and geometric discord were independently motivated by prior analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
