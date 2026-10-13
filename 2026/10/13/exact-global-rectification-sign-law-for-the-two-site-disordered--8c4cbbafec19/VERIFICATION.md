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

# Reproducibility

Execute `python3 verify.py` with a standard Python 3 interpreter. No third-party dependencies, files, internet access, or randomness are needed. The script constructs all four configurations explicitly, forms the continuous-time Markov generator from the stated transition rates, replaces one balance equation by normalization, and solves it over exact fractions. It independently obtains stationary current from \(a\pi(10)-b\pi(01)\).

The executable checks both analytical rational identities, denominator positivity, the sign of current and the reversal asymmetry for all combinations of four rational rate values per parameter and five reservoir values per side: 1,600 stationary chains. The displayed output is:

`CHECK_OK stationary_chain_cases 1600 nonzero_rectification_cases 960 example_current 36/173 example_reverse -44/237`

Mathematical completeness comes from the algebraic identities and positive-sum decompositions in `RESULT.md`; finite rational samples are not an exhaustive proof over real parameters. No independent audit is represented by these calculations.
