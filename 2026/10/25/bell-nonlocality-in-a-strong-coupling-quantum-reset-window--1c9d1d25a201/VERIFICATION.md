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
# Verification record

Run `python verify_standalone.py` with NumPy. The script evaluates the reset-state spectral integral using independently diagonalized Hamiltonians and compares the resulting nine Pauli correlations to the stated rational form at 400 deterministic pseudorandom parameter points. It also checks the explicit finite-coupling witness at seven couplings, 15 near-asymptotic settings, two reset extremes at six couplings, Hermiticity, trace normalization and state positivity.

Observed result: PASS. In particular, the numerical maximal CHSH values at \(lpha=2,3,10,100\) and \(R=(2lpha)^{-1}\) are approximately \(2.104408784710,2.168647483419,2.229256240838,2.235999040443\), respectively. The analytic scaled limit at \(s=1/2\) is \(\sqrt5\).

Universality, strict inequalities, and uniqueness of the **scaled** optimizer follow algebraically from RESULT.md, not from the finite sample. The exact finite-coupling Bell phase boundary and independent scientific verification are not established.
