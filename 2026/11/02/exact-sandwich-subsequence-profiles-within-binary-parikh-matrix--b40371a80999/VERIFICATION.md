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

# Reproducibility and verification

Run `python check.py` in a directory containing `check.py`; only the Python standard library is required. The expected saved stdout is `check_output.txt`.

The script directly enumerates binary words from position choices for each \(2\le A\le7\), \(0\le B\le7\), independently computes the internal \(b\)-count and scattered \(ab\)-count, and compares the resulting joint coefficients against the generating expression computed using a separate Gaussian-binomial recurrence. It also checks the Gaussian-binomial marginal and all conditional support sets, and tests the subsequence threshold by direct greedy subsequence matching.

Observed passing coverage: 48 parameter pairs, 12,825 enumerated words, 2,995 nonzero joint coefficients, 804 support spectra, and 4,640 direct pattern tests. The reported figures and representative histograms come from the included execution output, not from an unexecuted planned test. All computations are integer-exact. The parameter range is finite; arbitrary-parameter correctness rests on the proof in `RESULT.md`, specifically gap uniqueness and the interval overlap inequality.

Scientific limits: no assertion is made for arbitrary multi-run patterns, ternary Parikh matrices, or global priority. The complete texts of some directly relevant references were not available. Independent audit: not performed.
