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

# Verification of the Gaussian cosine and CG construction

The companion standalone script `verify_cosine.py` requires NumPy, SciPy and mpmath and runs using `python verify_cosine.py`. It checks the two-branch regularized-beta loss distribution against sampled beta energies across matrix ranks and probe numbers; independently evaluates direct matrix-vector cosine calculations; tests Chebyshev-Lobatto polynomial orthogonality in floating point and to 85 decimal digits; runs direct CG iterates for finite diagonal matrices; verifies the two damped-Jacobi sweeps reduce to scalar multiplication on diagonal SPD matrices; and evaluates the shrinking-loss/persistent-energy-error sequence. The actual code was executed successfully with **938 checks**.

These are finite supporting checks. The proof in `RESULT.md`, not simulation, establishes the exact distribution, its limiting regimes, and the existence of arbitrarily slow CG instances. The stated negative example concerns an adversarial RHS and does not establish typical performance or identify a learned model's output. Independent external audit has not been performed.
