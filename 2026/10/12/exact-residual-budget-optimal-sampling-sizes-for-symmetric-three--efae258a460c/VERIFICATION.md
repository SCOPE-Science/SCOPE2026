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
# Reproducibility and mathematical limits

Run `python verify.py` after installing `requirements.txt` (SymPy). The code verifies the two exact elimination resultants, the root counts on their intended intervals using exact Sturm arithmetic, the three squared-norm transition characteristic polynomials, the key inequality factorizations, 15 exact-rational finite-time squared-error expectations from direct subset enumeration, and five sample-size diagnostics. The checks passed when packaged.

The proof in RESULT.md, not numerical sampling, establishes the infinite-horizon rates, the continuity-region classification, and the strict optimality and equality cases. Generic starting error is required for the stated root rate; the result makes no assertion for arbitrary start vectors parallel to one of the rows. The nominal residual-evaluation budget ignores projection overhead and reuse of computed residuals. Independent external review or validation has not occurred.
