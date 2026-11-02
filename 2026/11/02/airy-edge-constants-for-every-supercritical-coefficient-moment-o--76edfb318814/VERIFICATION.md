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

# Verification notes
The exact identities and estimates needed for the finding are established in the proof: positive Poisson-phase curvature sums, the two uniform fold normal forms, and bulk and exterior bounds with integrable moment tails at every fixed exponent above four. The control exponent for the interior is \(1-p/4<0\), which fails to vanish at the critical \(p=4\); thus no unsupported critical extension is asserted.

A standalone deterministic script, \(\texttt{check.py}\), computes the two-root exact curvature and velocity identities with rational arithmetic, compares the cubic coefficients to centered numerical second derivatives of the phase velocity, verifies selected Airy-edge coefficient ratios with an FFT for moderate powers, and checks that the sixth-moment normalization is in the predicted range and increases toward its predicted constant for tested sizes. It requires NumPy and SciPy. Numerical finite-size results do not prove the asymptotic statement or historical priority.

The self-review is passed for the stated claim; an independent audit and independent validation have not been performed.
