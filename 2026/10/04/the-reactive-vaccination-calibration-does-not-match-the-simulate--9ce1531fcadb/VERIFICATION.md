---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The primary article's counterfactual susceptible equation contains the term \(-\nu_a\mathrm{VE}_aS_a\), while the supplementary calibration uses \(-\nu_a(S_a-S_{\infty,a})\). Solving the two scalar ODEs gives different maps from rate to endpoint. A fresh high-precision replay gives supplement rates 0.006581243690... and 0.008461585371..., but the multiplicative half-rate is 0.004968796993.... Inserting the supplement rates into the multiplicative law gives endpoints 0.1317635673... and 0.0675748848..., not 0.165 and 0.11.

## originality

PASS

The contribution is a source-specific reconciliation check across the article, supplement and released implementation. Targeted Resultary and web searches found no published erratum or prior statement of this exact calibration mismatch. General vaccination ODEs do not imply that this study used two incompatible calibration laws.

## value

PASS

The disputed calibration is used to interpret reactive-vaccination intensities in a current outbreak model. Distinguishing a positive-asymptote relaxation law from the actually simulated multiplicative vaccine-removal law changes the claimed mapping between daily rate and susceptible reduction, so the correction has substantive modelling value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
