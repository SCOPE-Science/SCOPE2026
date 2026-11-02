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

## Self-contained reproducibility

Run `python verify_markov_length.py` with Python 3. No downloaded data or third-party packages are needed. The verifier enumerates all \(2^n\) binary host strings for each \(n=1,\ldots,10\), independently computes all distinct scattered subsequences and their length histogram, weights by exact stationary Markov probabilities, and compares with coefficients extracted from the rational generating function. Exact `fractions.Fraction` arithmetic prevents floating-point ambiguity. Test switch probabilities: \(0,1/4,1/2,3/4,1\).

Actual output: `VERIFY_OK switch_parameters=5 n_range=1..10 enumerated_host_words=10230 checked_length_coefficients=275 fair_iid_and_constant_boundaries=TRUE`.

## What is and is not verified

The finite test checks all subsequence-length coefficients in the sampled domain and both constant and fair-i.i.d. sanity cases. The infinite identity follows from the deterministic append-symbol bijection, stationarity/complement symmetry, and exact matrix inversion as proved in RESULT.md, not from extrapolating enumerated hosts. The claim is about expectation, not variance, concentration, or almost-sure growth. Scientific review of this result is not an independent audit.
