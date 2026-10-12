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

From the package directory run `python3 verify.py` with Python 3 and no third-party dependencies. On the inspected package the program printed `PASS: 728 exact rational comparisons; infinite-horizon bounds proved analytically.` It directly executes each two-component gradient step, enumerates the two possible order choices through eight epochs using exact rational Markov transition probabilities, and compares first and second moments to the derived finite-horizon expression for three rational stepsizes, two signed noise amplitudes, two initial states, and five stationary order correlations. Additional rational tests cover endpoint sharpness, two switching signs, and five members of the unbounded-gap family.

The code does **not** check infinitely many times or all stationary processes. Those assertions are established by absolute convergence, Herglotz spectral representation, spectral extremizers, and a symbolic limit in `RESULT.md`. The algorithm's sampling marginal, exact arithmetic, and stability condition are essential to the claim. No external or independent verification has been performed.
