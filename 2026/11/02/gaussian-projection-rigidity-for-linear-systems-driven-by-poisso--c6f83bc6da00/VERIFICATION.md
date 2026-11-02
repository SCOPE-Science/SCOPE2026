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

# Mathematical verification

The `RESULT.md` proof establishes the full all-parameter network theorem. The standalone `verify.py` uses Python 3 with SymPy and can be executed using `python verify.py` from the extracted package directory.

The checker constructs stationary moment recurrences from the resetting diffusion generator for a scalar linear filter and symbolically verifies its second moment, fourth cumulant, normalized excess kurtosis and exact unit-parameter moment values. It further verifies strict transfer-function positivity at all sites for 5 finite chain sizes (`2`, `3`, `4`, `5`, `8`), 3 positive rational parameter quadruples, and both boundary inputs: 132 individual strictly positive rational transfer entries. It reports `PASS` only if every identity and positivity assertion holds.

These symbolic and finite chain checks are reproducibility evidence and examples, not an exhaustive proof over all dimensions or parameter values. General correctness rests on conditional variance, Poisson clock insertion, and M-matrix arguments in `RESULT.md`. Publication-priority and independent scientific audits have not been performed.
