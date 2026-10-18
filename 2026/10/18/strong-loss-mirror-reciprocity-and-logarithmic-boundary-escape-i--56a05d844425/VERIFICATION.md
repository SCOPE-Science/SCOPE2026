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

# Reproducible checks and limits

The analytic proof in `RESULT.md` establishes the all-parameter result by a fixed-dimensional spectral decomposition, positive dissipative modal rates, and a separately justified harmonic-number Riemann limit. The attached `verify_loss.py` is a finite corroboration script requiring Python, NumPy and SciPy. Execute `python verify_loss.py` to reconstruct the Hermitian hopping blocks and the non-Hermitian evolution, compute integrated site-loss probabilities using a continuous Lyapunov equation, compare them with two independent representations of the limiting distribution, and test mirror reciprocity for nonsymmetric positive profiles.

At the recorded test parameters, the program covers 29 small-size configurations, with a largest discrepancy below \(9\times10^{-16}\) between the two strong-loss formulas, a largest weighted mirror error below \(2\times10^{-16}\), and a largest finite-versus-asymptotic discrepancy at loss scale 1500 of approximately 0.001397. For chain lengths 60, 120, 500 and 1200, the endpoint ratio is numerically the chain length, while \(\pi_1\log N\) approaches an integral coefficient approximately 0.737503087043 for the indicated hopping strengths.

Finite tests neither establish an infinite-dimensional identity nor prove the uniqueness of a result in the literature. The large-loss and large-size limits are sequential, with no uniform error bound for arbitrary simultaneous growth. Independent scientific audit and independent external validation have not been performed.
