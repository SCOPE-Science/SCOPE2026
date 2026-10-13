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

The complete proof, hypotheses and implications are in `RESULT.md`. The standalone `verify.py` script uses NumPy, SciPy and SymPy versions governed by `requirements.txt`. Run with `python verify.py` in this directory. The observed output after unpacking the checked source files was:

`VERIFY_OK graph_numeric=28 exact_cyclotomic=28 asymmetry_rational=28 detector_rank_cases=24 long_time_cases=4`

The script enumerates Möbius ladders for \(3\le m\le30\), checks each Hamiltonian eigenvalue against the analytic Fourier spectrum, tests exact eigenvalue coincidence using remainders modulo the integer cyclotomic polynomial \(\Phi_{2m}\), verifies the two predicted exact time averages as rational numbers, and compares both one- and two-absorber spectral detector ranks for \(3\le m\le14\). Four matrix-exponential no-jump tests for \(m=3,4\) also match limiting survival probabilities. This tests only those finite sizes; the all-size proof uses the Conway–Jones 1976 classification, Fourier decomposition and dissipativity. No experiment by itself proves that other rational cosine collisions cannot occur.

This report records self-review only. No independent audit or external validation is claimed.
