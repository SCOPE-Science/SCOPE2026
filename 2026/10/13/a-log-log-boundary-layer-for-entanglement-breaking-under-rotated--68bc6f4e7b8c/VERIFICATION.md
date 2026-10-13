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

# Reproducibility and verification

The analytic proof in `RESULT.md` establishes the exact recurrence for all \(n\ge1\), the strict finite/infinite endpoint distinction, and the asymptotic result as \(\theta\downarrow0\) for each fixed \(0<\lambda<1\). None of these infinite-domain assertions is based solely on finite numerical computations.

Run `python verify.py` in a Python environment with `numpy` and `mpmath`. The program verifies the recurrence against direct singular-value decomposition and checks the two-qubit partial-transpose (PPT) separability decision on 128 parameter cases; the equality between PPT and separability for two qubits supplies an independent finite-case diagnostic. It further tests 69 analytically solvable right-angle power cases and 12 high-precision small-angle cases, including the first neglected quadratic correction in the boundary-layer estimate.

Observed output begins:

`VERIFY_OK recurrence_PPT_cases=128 exact_right_angle=69 small_angle_scaling=12`

The cases are selected finite samples, not an exhaustive enumeration. High precision controls cancellation in the small-angle calculations; the infinite-range result relies on analytic spectral perturbation bounds and the qubit entanglement-breaking criterion. The 2026 general eventual-breaking characterization was accessible only as an abstract in the literature comparison, so its specialized implications remain a residual priority risk.
