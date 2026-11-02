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

# Verification of the mathematical claim

The standard-library-only script `VERIFY.py` was executed directly for the included package. It reported **688 assertions passed**. It checks exact rational stationary solutions for \(n=1,\ldots,8\) at three rational deletion probabilities, their full-state probabilities, all the subset moment identities, count-distribution inclusion-exclusion, transition row sums and stationary equations, and the known first marginal. It additionally compares finite critical-loss products against the sharp prefactor approximation using composite Simpson quadrature at five fixed \(c\)-values and five increasing \(n\)-values.

Numerical sample: \(I(0.2)\approx0.190988803905\), \(I(1)\approx0.836727862260\), \(I(3)\approx2.114651415653\). The corresponding \(A(c)\) values are approximately \(0.973239499201\), \(0.595917718227\), and \(0.032259161645\), respectively.

The finite test domain does **not** certify all integers, all \(p\), or the limiting theorem. Those conclusions are proven by the exact stationary subset recurrence, its positive product solution, uniform smooth Euler–Maclaurin expansion for each fixed \(c\), and a stationary-coupling/mixing sandwich for the mean first hit. The coefficient \(A(c)\) is the stationary-state probability prefactor, *not* a proven hitting-time prefactor. No independent audit or external certification has been performed.

Reproduce from the extracted folder by running `python3 VERIFY.py`; no downloaded papers or third-party Python modules are required.
