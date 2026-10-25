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

Run `python check.py` with a standard SymPy installation. It rederives the six-cone transform, exact hexagonal invariant, differentiated Fourier numerator, positivity-certificate factorization and discriminant, and the square-norm Fourier obstruction at \(\eta^2=10\). Direct numerical comparisons at four wave vectors supplement the exact identities. The paper's sign proof handles every real frequency by the two cases \(0\le Q\le21\) and \(Q\ge21\), not by finite sampling. The claimed separation requires no randomized computation or inaccessible file. There has been no independent audit.
