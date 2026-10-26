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

# Analytical and computational verification

The mathematical proof is in `RESULT.md`, and `verify.py` is a self-contained Python standard-library program for finite supplementary checks. Reproduce from a directory containing the three files with `python verify.py`; compare its printed assertions with `verification_output.txt`.

The program exhaustively enumerates categorical uniform prefixes of lengths five and seven under three nested thresholds, and verifies the implied geometric increment factorization exactly using rational arithmetic. It checks the logarithm of the geometric generating function against the sum of independent Poisson jump intensities for several thresholds. It numerically integrates the Mittag–Leffler survival identity from the primary source at four decreasing shape parameters and three fixed logarithmic thresholds, and uses a seeded positive-stable representation for a finite Monte Carlo sanity check of the Brownian one-block hitting probability.

The recorded output contains 154 passed finite exact, floating-point, and simulated assertions. These checks do not prove the infinite-prefix limit, process convergence, uniqueness of an earlier literature result, convergence of prelimit moments, or independent mathematical validation. The weak-limit and independent-increment statements depend on the complete symbolic argument and identified established identities.
