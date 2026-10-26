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

The standalone `verify.py` was executed with Python 3 using only the standard library. It passed 210 exact uniform-occupancy factorial-moment identity checks, exact conditional multinomial enumeration through four candidates, and Poisson-tail threshold comparisons for three large occupancy scales and three representative top-class sizes each. The run output is included as `verification_run.txt`. These finite checks are reproducibility tests; they are not a proof of convergence.

The asymptotic claim follows from the written proof's exact occupancy factorial moments, Markov/Chebyshev bounds on the factorial-window classes, the normalization identity \(Q=n+2C\), multinomial-to-independent-Poisson total-variation approximation \(O(m^{12}/n)\), and complementary moderate-deviation bounds ensuring at least one runner-up exceeds every original leader. The finite correction is uniform over \(m!\le n<(m+1)!\). The eventual-winner consequence separately uses the published second-round containment in [1, §1.3]; it was not derived independently here.

No independent audit or external validation has been performed. No numerical rate of asymptotic onset is claimed.
