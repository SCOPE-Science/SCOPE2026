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

# Verification record

The proof applies to all positive integer values of the repunit parameter. It derives exact zero-count bounds from base-four carry cases, establishes the endpoint-letter restrictions, and classifies all possible reduced Parikh vectors using substitution and reversal closure. The global logarithmic upper bound follows from a general finite-digit carry argument. No numerical test is used as an infinite proof.

Run `python3 check.py` from the directory containing the accompanying files. The script uses only Python's standard library. It independently produces the fixed point by substitution, compares it to the explicit valuation formula on a length-131072 prefix, evaluates the complete spectra for seven positive parameter values, checks the attainable zero-count intervals against alternating digit sums, and performs literal run reductions at 14000 starting positions across those lengths. The exact observed counts were 2, 4, 6, 8, 10, 12, 14; `check_output.txt` records the run.

Finite-prefix tests do not independently settle the unbounded claim, do not verify originality, and do not constitute an external audit. Source accessibility and residual scientific limitations are discussed in the accompanying scientific review.
