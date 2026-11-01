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

# Reproducibility and limits

Run `python3 checker.py` with Python 3.10 or later; no external packages are required. The script performs 48 exact rational verifications of the symbolic spectral-derivative numerator against the stated polynomial, 600 seeded random numerical comparisons between generator/moment resolvents and independently decomposed promoter spectra on directed cycles of lengths two through six, 240 explicit three- and four-state harmonic checks, and four threshold tests. It prints 892 successful comparisons, largest observed relative spectral discrepancy below \(2\times10^{-14}\), and the sample peak at \(0.7779563871383612\).

The infinite parameter range and the unique spectral root are proved in RESULT.md by the strict increase of an explicit real polynomial on the nonnegative axis; the finite checker cannot prove such quantified statements. A spectral peak is not a deterministic oscillatory orbit or an experimental signal-to-noise guarantee. Historical novelty is qualified by the primary-literature comparisons in REVIEW.md and AUDIT.json. Independent validation has not been performed.
