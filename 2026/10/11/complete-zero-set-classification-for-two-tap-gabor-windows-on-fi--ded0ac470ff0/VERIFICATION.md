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

# Verification of the finite-group zero-set classification

The universal proof in RESULT.md uses finite abelian character duality, multiplicative telescoping on cycles, and an explicit construction avoiding finitely many forbidden ratios. No finite sample extrapolation is used.

The standalone `verify_zero_patterns.py` uses the Python 3 standard library. It represents roots of unity by fractional turns and complex amplitudes by exact fractional scales. It enumerates every labeled pattern for cyclic groups of orders 2–5, checks exact counts for all these cases, constructs coefficients for every admissible pattern, tests selected cyclic instances up to order 7 against direct Fourier slices, and independently tests noncyclic product groups. It checks the local counting identity for cycle orders 2–23.

Command: `python3 verify_zero_patterns.py`

Observed output: `VERIFY_OK cyclic_labeled_cases=139968 cyclic_direct_DFT=5061 exhaustive_cardinality_cases=40 product_group_direct_DFT=403 exact_root_cosets=PASS holonomy=PASS pattern_count=PASS`

Computations validate these finite instances only. The assumption that the signal is nowhere zero cannot be dropped without a separate analysis. No independent audit has been performed.
