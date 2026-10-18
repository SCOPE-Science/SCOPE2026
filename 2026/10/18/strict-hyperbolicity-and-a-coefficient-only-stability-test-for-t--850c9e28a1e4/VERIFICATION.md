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

# Mathematical verification

The exact coefficient calculations and the sample event-driven first-return integration can be reproduced by running `python check.py`. The script asserts all six source-example offset inequalities using exact fractions, and verifies the explicit expression for the sample multiplier. If NumPy/SciPy are available, it integrates each affine segment and compares a centered return derivative against the formula. A numerical tolerance validates the demonstration only; it cannot certify the theorem across arbitrary real coefficients.

The proof is self-contained within the stated four-crossing, transverse, isolated itinerary. Conservation of each quadratic Hamiltonian and the first-hit section derivative establish the return multiplier. The exceptional cases of equal central offsets are handled by local continuation of genuine transverse sections and hence cannot be isolated. The coefficient-only strict inequality is a mathematical consequence of an exact factorization and four normal-velocity signs.

No claim is made about a larger class of itineraries, infinite enumeration, or independent certification. The closest two-zone hyperbolicity theorem and three-zone cycle-count papers are distinguished in the result's literature comparison. External audit has not been performed.
