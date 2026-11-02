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

# Reproducibility of the single-sink prime-torus theorem

The supplied `verify_prime_tori.py` uses NumPy's real-symmetric eigendecomposition on the full site Hilbert space; it does not reconstruct amplitudes via the cyclotomic proof. For every distinct numerical eigenvalue it sums the corresponding exact finite-dimensional eigenspace projection numerically and evaluates the rank-one sink's bright-state overlap. It then independently compares each site against the stated closed-form theorem.

Run `python verify_prime_tori.py` from the directory containing the file. The recorded output in `verification_output.txt` was reproduced by executing that exact packaged script. The checker covers 24 prime/coupling cases and 1,448 starting sites with a maximum discrepancy less than \(10^{-13}\). It also checks bright dimensions and that the sum of capture probabilities equals the active dimension.

The analytic proof and the cyclotomic field intersection cover all eligible primes and rational positive coupling ratios, including primes and couplings not directly tested. Finite computation is a check of the implementation and formulas, not a substitute for those infinite-family arguments. Finite-time absorption rates, environmental noise, arbitrary irrational couplings, and composite cycle orders are unproved here.
