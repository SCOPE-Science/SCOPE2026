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

# Verification

The result concerns the scalar Zak transform in the precise Fourier and lattice conventions of `RESULT.md`. Run `python checker.py` with dependencies in `requirements.txt` to reproduce the exact polynomial identities and three sampled Poisson checks.

The checker tests the identity between the rational Zak expression and the cleared cubic, the special values at \(z=1\) and \(z=-1\), the coefficient obstruction for any conjugate unimodular pair, and the factors at \(\xi=0\) and \(\xi=1/2\). These are finite algebraic identities and do not constitute an exhaustive numerical search.

For the infinite claim, the proof uses the real nature of the cubic coefficients, the necessary coefficient identity for conjugate unit roots, strict positivity of the remaining factors for all \(0<q<1\), and a strict inequality ruling out the residual quadratic's unit-circle roots. All boundary cases are explicit. Verification does not establish independent historical priority or settle the Gabor frame-set classification.
