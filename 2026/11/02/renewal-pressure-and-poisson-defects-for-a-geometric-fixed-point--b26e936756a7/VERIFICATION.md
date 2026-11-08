---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read complete frozen RESULT.md blob cdf5533... . For cylinder [1 0^(r-1) 1], summed return energy E_r=(1-θ^r)/(1-θ), independent of later symbols. Renewal root Σ exp(-βE_r-rP)=1 and entropy/KL vs iid qβ imply uniqueness and m finite. Separate geometric tail B/(e^P−1) from summable Δ_r; bound tail after r=3 by β θ^r e^-βE3/(1−θ), obtaining correct two activation corrections because 1/(1−θ)>1+θ. Intensity m^-1~B and Palm-to-stationary excess waiting-time argument yields Exp(1) waits and independent Poisson arrival spacings. Independently calculated nine high-precision renewal root cases with normalization and activation ratios.

## originality

PASS

Compared implication of broad Dini-potential nonfreezing (Jiang–Li–Sun 2026) and double-well zero-temp results: neither known statement gives this particular exact geometric return law/pressure correction/Poisson limit. Closest full text was inaccessible; explicit historical risk retained without claiming it lacks a hidden stronger theorem.

## value

PASS

Determines an exact natural low-temperature thermodynamic activation barrier and corrections, and the stationary rare-defect point-process law, for a concrete Lipschitz distance-to-fixed-point observable; these quantitative results are not automatic from the positivity of pressure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
