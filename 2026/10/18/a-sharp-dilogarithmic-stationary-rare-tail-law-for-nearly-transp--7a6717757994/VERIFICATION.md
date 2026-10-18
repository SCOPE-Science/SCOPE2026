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

# Verification of the sharp rare-tail formula

Run the standard-library standalone check using `python3 checker.py`. It verifies generator and cumulant moment identities by exact rational arithmetic, the dilogarithm and saddlepoint identities numerically, the order-one Euler–Maclaurin logarithmic-product correction at several parameter values, and the exact rational Fourier-modulus inequality used for the tilted local limit. Checks verify finite exact identities and numerical consistency but **do not by themselves certify** the infinite limiting probability ratio.

The decisive analytic steps appear in `RESULT.md`: the stationary Laplace perpetuity and its product transform; an Euler–Maclaurin estimate uniform with required derivatives on fixed compact tilt regions; an explicit Fourier product estimate that yields convergence of tilted density functions uniformly; and dominated convergence for the exponentially weighted tail integral. The conclusion is pointwise in fixed \(y>0\). No independent external scientific audit has been performed.
