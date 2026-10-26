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

# Reproduction and boundaries

The self-contained `check.py` enumerates every \(n+3\)-parameter centralizer matrix for each tested finite field and compares the directly computed \(X^2=0\) condition and Gaussian-elimination rank to the theorem's coefficients and total count. Run: `python check.py`.

The executed checks passed for \(\mathbb F_2\) with \(3\le n\le8\), \(\mathbb F_3\) with \(3\le n\le6\), \(\mathbb F_4\) with \(3\le n\le5\), and \(\mathbb F_5\) with \(n=3\). Output ended with `HOOK_SQUARE_ZERO_RANK_OK 14 exhaustive fields/dimensions`.

No experiment verifies the algebraic arguments for infinitely many dimensions or prime powers. The proof explicitly derives square-zero coordinates, valuation bounds, rank filtration, component geometry and singular loci. The theorem concerns reduced varieties, not raw square-zero schemes, and independent mathematical audit has not been performed.
