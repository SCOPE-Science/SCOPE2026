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

Execute `python checker.py` using Python 3. The script uses only the standard library and `fractions.Fraction`, solves an independent finite-boundary tridiagonal hitting system via rational Gaussian elimination, and checks eight parameter choices across all \(1\le m\le14\): **112 exact equality comparisons**. In the observed run it printed `PASS 112 exact rational comparisons`. It also prints the first five tail values at four parameters. The script's exact-arithmetic comparisons verify the displayed rational formula at those finite points, not the general proof or the infinite-depth limits.

Analytically check the proof via the shell launch distribution \(q\) at depth one and \(p2^{-j-1}\) for every depth \(j\ge0\), the finite Dirichlet recurrence \(h_j=ph_{j-1}+qh_{j+1}\), and the geometric sum in equation (1) of `RESULT.md`. The parameter-limit arguments in `RESULT.md` separately address the removable singularities \(p=1/2\), \(p=2/3\), and the deterministic endpoint \(p=1\). High-precision finite-parameter crossover calculations were performed for several increasing depths; such calculations support the formulas but cannot certify their limiting values.

No independent scientific audit has yet been conducted.
