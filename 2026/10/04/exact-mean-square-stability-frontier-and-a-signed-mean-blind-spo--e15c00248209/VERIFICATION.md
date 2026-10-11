---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For one coordinate, the Bernoulli row choice closes the exact covariance recursion on (q,r,s) with the displayed 3x3 matrix T. Independent symbolic expansion reproduced the cubic coefficients and the factorization of the first Jury quantity. After substituting c=1-beta and u=cM, an independent exact Bernstein conversion reproduced all 49 degree-(6,6) coefficients of the third Jury quantity with minimum exactly 3/16, while the second condition is manifestly positive. Under the first inequality the determinant condition is strictly inside the unit disk. The source initialization has nonzero projection on the unit/unstable real mode, so equality is marginal and supercritical parameters do not converge in mean square. The beta=0 signed-mean 2x2 Jury test gives M<1, while mean-square requires M<1/sqrt(2); the M=1 algebra yields beta>(5-sqrt(17))/2.

## originality

PASS

Originality passes. The defining KGSM paper was inspected in full, including visual inspection of the algorithm and limitations/open-question pages: its proved observable is signed directional expectation, and it explicitly asks for a critical momentum region and convergence of expected absolute or Euclidean error. It does not contain the exact three-dimensional covariance recursion or the audited Schur boundary. The broader heavy-ball source treats a different unsmoothed recurrence and gives sufficient L2 rates, not this necessity-and-sufficiency KGSM frontier.

## value

PASS

The defining paper explicitly asks for critical momentum and stronger unsigned/Euclidean convergence. The orthonormal two-row system is the natural geometry-free baseline, and the exact blind spot demonstrates why signed expectation is insufficient. The result therefore resolves a motivated mathematical boundary, not an arbitrary toy calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
