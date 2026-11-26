---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The Caputo integral equation and continuity at the initial state force y(t)=K+F(K)t^α/Γ(α+1)+o(t^α), including α=1. In the publisher PDF, Eq. (5.8) and its definitions of the zeroth products support the frozen comparison. Eq. (5.9) changes the symptomatic loss and recovery input, giving first-coefficient residuals φ_s(K₃−K₄) and ρ_h(K₅−K₆). Eq. (5.10) repeats the symptomatic loss error and uses the exposed instead of susceptible state in the natural mortality term of the susceptible equation; it also swaps the incidence pairings in both rows. The sign of the susceptible residual in the frozen proof is correct. These differences are nonzero as polynomial identities; the non-incidence differences alone suffice. Transfer balance requires consistent pairings but does not distinguish a simultaneous swap; the intended labels are established separately by Table 1 and (5.8). Section 6 explicitly attributes its approximations to (5.10), but this does not establish what the unavailable implementation computed. VERIFICATION.md and verify.py were inspected, not executed; the script checks the transcribed expressions, not their provenance or any trajectory. The analytic first-term comparison is decisive.

## originality

PASS

The distinct claim is the specific first-coefficient failure of Eqs. (5.9)–(5.10) in DOI 10.3934/math.2022877, not the Caputo first-term test or the compartmental model. No equivalent diagnosis was found in the inspected material.

## value

PASS

A leading-order inconsistency in the recurrence explicitly cited as the basis of the numerical figures is a concrete reproducibility defect. It rules out correcting the discrepancy simply by taking more terms of the same formal series, without drawing conclusions about epidemiological predictions or unavailable code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
