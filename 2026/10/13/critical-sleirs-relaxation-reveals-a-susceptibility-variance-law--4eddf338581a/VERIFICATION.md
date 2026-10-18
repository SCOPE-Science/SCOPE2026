---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At Ak=delta+mu, the displayed full five-compartment ODE has a nonnegative logarithmic Lyapunov function. Independent SymPy differentiation verified exactly Vdot=-mu(S-rho)^2/S-mu(L-(1-rho))^2/L+sigma R[1-rho^2/S-(1-rho)^2/L] (critical terms cancel). Cauchy Schwarz plus simplex forces Vdot<=0, and LaSalle yields DFE attraction. An irreducible infected 2x2 Metzler matrix has simple 0 mode (1,h) and stable complement, giving I/E->h, stable scalar filters yield R/E and both signed susceptible deviations. The positive inverse infected weight derivative converges to K/H; hence tE->1/K and all component 1/t and cumulative log limits. Exact symbolic fraction check for rho=1/2, other rates=1, alpha=5/3,beta=1 yields A=4/3,B=17/9,G=1/4,H=4/3,K=45/16. Fresh ODE integration to t=100000 agrees with all five leading coefficients within 0.006% relative error, not proof of all initial states.

## originality

PASS

The closed-threshold disease-free stability is already strongly suggested/covered in broader multi-susceptibility works and MUST NOT be credited independently. The full five-component critical asymptotic with exact transmission-contrast variance K(delta) for the Pan–Tang R0=1 boundary was not implied by inspected statements. Resultary already has same-model subcritical risk-composition contraction; this covers strictly R0<1 but not the critical coefficient.

## value

PASS

The critical t^-1 vector and explicit susceptibility-variance law quantify critical slowing and infection burden at identical R0=1; treating α,β risk heterogeneity separately rather than averaging is motivated by the model and gives a nontrivial sensitivity coefficient. The older global stability threshold is credited, not claimed valuable by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
