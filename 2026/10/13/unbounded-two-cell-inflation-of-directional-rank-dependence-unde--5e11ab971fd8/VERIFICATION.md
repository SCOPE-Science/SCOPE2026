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

For the exact polynomial family, algebraic differentiation checks the density and conditional CDF. Integration gives the exact original coefficient, and a separate two-cell conditional calculation gives the approximant coefficient; the proof in `RESULT.md` handles all positive integers and the asymptotic limit by dominated convergence.

The standalone `checkerboard_inflation_check.py` uses only the Python standard library. Run `python3 checkerboard_inflation_check.py`. It passed exact rational binomial and factorial integral comparisons for indices 1–16, exact four-cell mass computations, and independent piecewise-linear conditional CDF integration. It verified the strict transition at index six and printed the exact ratio there.

The computation is finite and does not establish the asymptotic limit by itself. The class remains SI/PQD but is not density-TP\(_2\). The lead paper's finite counterexample to the unqualified lower inequality is prior art; only the unbounded multiplicative mechanism and its uniformly positive polynomial implementation are assessed here. Independent audit has not been performed.
