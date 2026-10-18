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

Primary PDF equation (2.1) uses beta S(E+A+epsilon V), no population denominator; exposed equation and next-generation R0 are linear in beta Λ/μ. Its Tables 3/4 set Λ=μ N(0) with N(0)=59,310,000, beta=.034/.34, yet print R0=.61/6.11. Let D=1/(p+q+μ)+p/[(p+q+μ)(γ_A+μ)]+qε/[(p+q+μ)(κ+γ_V+μ+δ)]; printed R0=β N0 D, normalized R0=β D. Independent exact rational calculation using all printed parameters gave for beta .034: freq 0.6114991225346483, mass 36268012.95752999; beta .34: freq 6.1149912253464835, mass 362680129.5752999. Initial infectious weighted count yields per susceptible force 8,563,683.19/day versus .1443885/day. Primary model/table screenshots and arithmetic agree. Neither model implementation nor fitted trajectory reproducibility is inferred from missing code.

## originality

PASS

The discovered prior published Resultary finding "A critical-threshold Lyapunov identity closes the waning-immunity SARS-CoV-2 disease-free theorem" (Oct 4, 2026) studies exactly the same printed seven-class equations and R0, but proves a Lyapunov stability endpoint, not a comparison with numerical tables or an incidence-scale correction. General normalized incidence and different epidemic-paper error reports do not supply this DOI-specific arithmetic contradiction; exact source and old theorem were read before concluding no covering implication. Search absence alone is not novelty proof.

## value

PASS

A factor 59,310,000 is an enormous dimensionally significant discrepancy in a calibrated model, changing its R0 from order one to hundreds of millions and its initial force of infection by the same factor. The check is not novel algebra but an independently useful, fully reproducible source-specific correction separating two possible incidence conventions; failure to flag it would mislead quantitative interpretation and published numeric reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
