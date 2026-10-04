---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The primary publisher full text was checked at the controlled state system, the Gâteaux first-variation system, the adjoint system, and the stated optimal-control characterization. The delayed vector-incidence term was transcribed directly before differentiation.

The proof uses two exact steps. First, ordinary product differentiation of
\[
(1-u_2(t))\beta_{hv}e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau)
\]
gives the stated first variation. Second, substituting \(s=t+\tau\) in the costate pairing converts delayed state variations into advanced costate coefficients with \(u_2(t+\tau)\), current state values, and the unchanged factor \(e^{-\mu_v\tau}\).

The packaged `verifier.py` implements a small formal polynomial ring over exact rational coefficients. It expands a perturbed product with a formal \(\varepsilon\), extracts the coefficient of \(\varepsilon\), and checks identity with the corrected variation. This is a symbolic replay of the algebraic step and uses no floating-point approximation.

Limits: only delay-generated terms are verified. No numerical optimal-control trajectory is claimed, and no conclusion is drawn about a corrected existence or uniqueness theorem.
