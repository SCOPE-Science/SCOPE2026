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

The exact source fixed-point equation for the maximal singular cycle becomes G(a,R)=log((1-a)/(1+Ra))+(1+R)a=0 after y_infty=-ba and R=sqrt(u_M/u_m), and the source interval becomes a in (1-1/R,1). Direct differentiation gives G_a=a(R+1)(Ra-R+1)/((a-1)(Ra+1))<0 and G_R=Ra^2/(Ra+1)>0 on that root, hence a'(R)>0. The source fast-flow maximum is Z=Ra-log(1+Ra), so Z is strictly increasing as well. An independent symbolic expansion reproduced a=3/2 delta-3/2 delta^2+27/20 delta^3+O(delta^4) and Z=9/8 delta^2-9/8 delta^3+333/320 delta^4+O(delta^5). The strong-contrast substitution epsilon=1-a gives the exact implicit equation used in the package and the stated exponential first correction. The source pages containing Proposition 3, its fixed-point equation, exit coordinate, and cycle peak were materially read and match the normalized formulas.

## originality

PASS

Borsotti--Kuehn--Sensi prove existence, uniqueness in the relevant interval, stability, and maximal amplitude of the singular cycle and give its exact defining equation and peak. The inspected primary material does not analyze monotonic dependence on the control contrast or derive the weak- and strong-contrast asymptotic laws. Resultary search found the assigned finding as the direct match and no prior equivalent sensitivity theorem. The contribution is therefore bounded to an exact parameter-sensitivity analysis of the published cycle, not to the already-known existence or peak formula.

## value

PASS

Control contrast is the natural design parameter in the source model. The theorem gives exact monotonic response and two sharp asymptotic regimes, distinguishing linear entry/exit growth from quadratic peak growth near equal controls and exponential boundary approach at high contrast. These laws directly refine the source's target-admissibility interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
