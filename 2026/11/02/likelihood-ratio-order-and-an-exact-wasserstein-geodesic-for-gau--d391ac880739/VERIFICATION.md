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
# Verification notes
The exact theorem and its parameter domain appear in RESULT.md. Using Python 3, run `python3 verify.py` in the directory containing this file and verify.py. The program uses standard-library numerical quadrature and mathematical functions; no external packages or random seeds are required. Its recorded output in verification_output.txt states 347 passed deterministic checks.

The checker corroborates: direct convolution versus the displayed density, direct conditional CDF versus integrated parameter derivative, sampled monotone likelihood ratios and CDFs, and exact mean against numerical integration. The numerical checks sample finitely many parameters, positions, and quadrature intervals. They are not proofs of global likelihood-ratio monotonicity, an endpoint inequality, uniqueness, or optimal transport equality. The decisive proof is the positive truncated-normal second moment, the negative CDF derivative, and the matching coupling/duality bounds in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
