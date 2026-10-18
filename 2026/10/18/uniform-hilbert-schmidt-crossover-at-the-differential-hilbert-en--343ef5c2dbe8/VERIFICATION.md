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

# Verification of the crossover theorem

The proof derives all infinite-parameter limits from uniform gamma-ratio, beta-integral and row/column comparison estimates; no computational exhaustion of infinitely many parameters is claimed.

The included `verify.py` computes exact finite-section matrix entries from independently evaluated weighted monomial norms and checks the square-sum equals the Frobenius norm, positivity of relevant entries, the first two coefficients, growth under increasing cutoffs and monotonicity under increasing target weight. It also reports measured finite-cutoff logarithmic slopes against the analytic limiting coefficients.

Actual run: `python verify.py`. The checks passed for \(\alpha=-3/4,-1/2,-1/5\), matrix sizes \(64,128,256,512\), and weights shifted by \(\delta=0,0.01,0.06\). The finite slopes remain below the predicted coefficients at these modest matrix sizes; this does not contradict the asymptotic formula and is not used as its proof. Reproducibility requires Python, NumPy and SciPy.

Limits: no independent audit, computer-assisted infinite proof, full singular-value distribution or uniformity at the parameter boundaries is asserted.
