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
# Verification of the complete-graph relaxation theorem

The proved range is \(n\ge3\), \(J>0\), and \(\gamma>0\). The required algebraic checks are the three invariant-block identities, the cubic determinant, the off-block eigenspace count, the real-root quadratic discriminant, and the factorization at the claimed maximizer; these are written out in `RESULT.md`.

The standalone numerical replay uses Python 3.10 or newer and NumPy. Run `python verify.py`. It independently constructs \(n^2\times n^2\) Lindblad matrices from the master equation, compares every eigenvalue with the cubic-plus-degenerate spectral prediction for six sizes and multiple parameter regimes, and checks both the proposed spectral upper bound and its sharp attainment.

The recorded run passed 264 numerical checks with maximum absolute eigenvalue discrepancy \(3.935\times10^{-13}\). These checks cover only \(3\le n\le8\), two hopping strengths and seven positive noise ratios. Finite experiments do not prove infinitely many dimensions, uniqueness or global optimality: those follow from the discriminant and exact factorization proof. All models assume equal all-to-all hopping and spatially uniform site dephasing. No independent audit has been performed.
