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

# Verification and reproducibility

Run `python verify.py` in an environment with NumPy. The script independently builds the full Lindblad superoperator for stars with 2, 3 and 5 leaves and compares its Perron eigenvalue and two concurrences to a separately assembled permutation-reduced generator. It also checks the asymptotic coefficients at \(m=1000\) for three parameter triples. Positive eigenvalues of all stationary densities in the finite samples are checked.

The analytical proof is in `RESULT.md`: positivity-improving jump paths give a unique stationary conditional state, permutation symmetry gives the exact reduced generator, and an analytic implicit-function argument at inverse degree zero proves the full asymptotic claims. Finite numerical tests are sanity checks only. No external independent audit is claimed.
