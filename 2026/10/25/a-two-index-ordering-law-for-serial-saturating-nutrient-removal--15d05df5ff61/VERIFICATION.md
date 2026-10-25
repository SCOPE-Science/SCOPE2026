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
# Reproducibility and limits

With Python 3 and the `sympy` dependency listed in `verification/requirements.txt`, run

```bash
python3 verification/check_serial_uptake.py
```

The program verifies the exact symbolic two-stage commutator identity, a complete rational two-stage order switch at incoming concentration one, 10,000 seeded pairwise comparisons over positive parameters, 133 distinct randomly generated rational families with exhaustive permutations at both extreme-input regimes, and an equal-residual-index boundary. It uses exact rational arithmetic for every exhaustive permutation comparison; numerical random tests are checked against a symbolic formula.

The seed is fixed and the program uses only the explicitly bundled code and listed dependency. Tests do not prove behavior for all real parameters or establish historical priority. Those universal mathematical conclusions follow from the analytic proof in `RESULT.md`. The paper reports no experimental validation, noise robustness, or extension to hydraulic routing.
