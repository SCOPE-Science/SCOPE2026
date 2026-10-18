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

# Reproduction and mathematical limits

The included `verification.py` executes under ordinary Python 3 using only the standard-library `fractions` and `math.factorial` modules. Run `python3 verification.py`. All inequalities are computed using exact rational Taylor polynomials and rigorous absolute remainder bounds; no floating-point tolerance is used to determine a sign. The displayed decimals are outward-rounded summaries of rational endpoints.

Expected certificates:

- `r=4/5, concentrated: extinction [-0.000243134545, -0.000243134544]`
- `r=4/5, dispersed: growth [0.000086879311, 0.000086879312]`
- `r=2, concentrated: growth [0.009281781678, 0.009281781679]`
- `r=2, dispersed: extinction [-0.012615180095, -0.012615180094]`
- `CERTIFIED: four strict viability signs, common second moment, fourth-moment difference.`

The program confirms the boundary-pole condition implicitly assumed by the viability test only through the known analytic inequality on the chosen domain; the report's proof separately establishes the spectral criterion. The checker establishes **only the four strict numerical inequalities**, the moment equalities and the positive fourth-moment difference. Existence and uniqueness of the leading spectral root, convex-order transfer, all-width crossover, and implicit fourth-moment critical-width law are established analytically in `RESULT.md`, not by finite computation. Independent external scientific audit has not been performed.
