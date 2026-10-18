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

# Reproducibility of the contracted-rotation scaling law

Run `python verify.py` in an environment with Python 3. The checker requires only the standard library, with either SciPy or mpmath available for the diagnostic numerical zeta benchmark.

The program independently reconstructs rational plateau endpoints with exact fractions for \(\lambda\in\{1/2,2/3\}\), verifies their exact equal-width formulas at all reduced fractions with \(2\le q\le12\), checks the standard totient divisor identity for integers through \(1000\), and simulates attracting orbits at plateau midpoints to corroborate the expected rotation numerators. It also numerically sums the full exact mass law over sufficiently many denominators for \(h\in\{0.12,0.06,0.025,0.01\}\) and checks normalization and the convergence trend of its first two rescaled moments.

Observed terminal line:

`VERIFY_OK 90 exact rational tongues; 90 midpoint rotation simulations; 1000 totient-divisor identities; 4 limiting-law mass/moment checks`

These tests are finite checks, not an exhaustive mathematical proof or a check of literature priority. Infinite normalization, the joint weak limit, and convergence of all moments follow analytically from the displayed totient identities, equidistribution estimate, and uniform tail bounds in `RESULT.md`.
