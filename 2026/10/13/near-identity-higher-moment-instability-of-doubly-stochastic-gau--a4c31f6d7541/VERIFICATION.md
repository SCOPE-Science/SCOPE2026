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
# Reproducibility

Execute `python3 verify.py` using Python 3.9 or later; no third-party packages are needed. The script uses `fractions.Fraction` and `itertools.product` to construct all ordered entry updates and their exact probabilities. It checks the matrix identity for conditional squared-error contraction, the rational factors \(323/404\) and \(6561/6464\), 360 nonzero rational directions for second and fourth moments, and 18 exhaustively enumerated expectations across three starts and six horizons.

The replayed script prints `VERIFY_OK: 360 rational-direction tests, 18 exact finite-horizon expectations, quadratic matrix identity`.

The script checks finite mathematical consequences only. The proof of the assertion for all real orders \(p>2\), all horizons, and all nonzero starting states is the analytical power-mean/singular-value argument in `RESULT.md`; the almost-sure conclusion follows from a summable second-moment tail bound. No independent verification has been performed.
