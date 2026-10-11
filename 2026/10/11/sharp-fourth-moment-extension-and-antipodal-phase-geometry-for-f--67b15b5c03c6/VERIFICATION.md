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

Run the included script in Python 3 using `python3 checker.py`; no third-party package or network is needed. For prime fields of orders \(5,7,11,13,17\) and quadratic extensions of orders \(25,49\), it checks that the only nontrivial two-sum fiber is the antipodal fiber, recomputes every convolution fiber using ordered pairs, compares it with the closed quadratic identity, tests the sharp bound on deterministic randomized complex inputs, and reconstructs paired-phase extremizers. Three field sizes also have direct evaluations of the original Fourier extension to check the factor of \(q^{-1}\). The recorded script result is `PASS 1588 checks; direct Fourier checks for q=5,7,25`.

The unrestricted proof instead uses field algebra, exact orthogonality and the explicit sum-of-squares deficit identity. These finite tests do not establish the theorem for every finite field. There is no independent mathematical audit, and no machine-formalized proof or external certification is asserted.
