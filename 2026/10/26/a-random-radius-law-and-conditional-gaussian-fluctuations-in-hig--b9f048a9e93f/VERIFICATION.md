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

# Verification and limits

The standalone `verify.py` uses exact rational beta-moment recursions, independent simulated uniform-sphere directions, and a dimension-dependent radial error comparison. Run it with `python verify.py`. The supplied execution yielded `PASS 123 assertions` using its fixed random seed. The mathematical argument is the proof in `RESULT.md`; numerical finite-dimensional tests cannot certify convergence in dimension.

Exact identities independently evaluated include the mean and variance of the Poisson–Dirichlet Simpson statistic, the expected fourth power sum, finite-dimensional radius and coordinate fourth moments, and the excess-kurtosis sign threshold. The simulation truncates the stick-breaking sequence and allocates the remainder to the final simulated mass. Consequently the simulated process approximates, rather than exactly samples, the full infinite-past model. The theorem explicitly assumes independent uniform spherical reorientations, fixed positive rates and no additional thermal forcing.

No independent scientific validation has been performed.
