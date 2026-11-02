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

# Reproducible verification

Run `python3 verify_planar.py` with standard Python 3.10 or later. There are no external packages and no network calls. The deterministic script prints `PASS: 849 independent deterministic assertions` on successful completion.

The script independently checks the exact rational quadratic-energy decrease identity for many rational starting states and directions; integrates the Gaussian projective angular density; tests the Cauchy threshold law and analytical angular derivative identity; compares candidate start angles for several thresholds and condition numbers; verifies mean, median, exact batch-confidence ceiling; runs independent seeded Gaussian checks; and compares the large-condition-number law with its predicted square-root critical limit. Every test executed successfully when the complete set of embedded files was assembled.

Rational examples and finite numerical sweeps do not certify the universal theorem for all real parameters. The proof in `RESULT.md` supplies the general angular monotonicity argument, strict covariance minimax and the asymptotic expansions. Its assumptions include Gaussian independent candidate lines and exact one-dimensional minimizations from the **same** initial point. An independent audit is outstanding.
