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

# Reproducibility and finite checks

Run `python verify.py` with Python 3 and a compatible NumPy installation (version constraint in `requirements.txt`). The checker builds the four-by-four pair-creation contact unitary and two-qubit pre-reset density matrices, forms partial transpose as an independent matrix reshape/permutation, and compares its negative eigenvalues with the closed-form formula. It tests many thermal probabilities and contact strengths and verifies strict-positive-contact indices.

To avoid relying solely on the derived single-parameter population formula, the checker also starts at the exact maximally mixed target and **iterates a fresh thermal ancillary pair, full unitary conjugation, and an explicit partial trace**, for 55 contacts at each of 20 parameter combinations. These iterates agree with the analytic trajectory and the independently diagonalized partial transpose. The run completed **9,301 finite assertions**. Near-zero floating-point eigenvalues are handled by tolerance; exact threshold equality is proved analytically, not certified by floating point.

The program tests the sharp bath probability boundary and computes the unique optimizing scalar root by bisection. For cold-bath probabilities \(0.01\), \(0.002\), \(0.0005\), and \(0.0001\), it prints candidate horizons \(22\), \(114\), \(462\), and \(2318\) at the theoretically specified scaling.

# Proof-versus-computation boundary

The finite checks do not prove the integer formula for all inputs, the global supremum over continuum contact strengths, the unique asymptotic optimizer, or the infinite-horizon zero-temperature boundary. Those statements follow from the explicit matrix reduction, strict PPT inequality, and uniform asymptotic bound proved in `RESULT.md`. No independent audit or external mathematical validation has been performed.
