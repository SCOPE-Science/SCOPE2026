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

Run `python3 checker.py` with a standard Python 3 interpreter. The program enumerates every one of the 256 sign assignments, independently evaluates the sum- and difference-frequency Fourier contractions at sampling orders three, four and five, and confirms their equality with exact integers. It evaluates the unaliased integer-lattice sums, verifies the analytical n>=5 no-aliasing premise over the entire binary domain, and exhaustively partitions all sign arrays into symmetry orbits. Its assertions reproduce the moment histograms and the two-orbit minimum classification reported in RESULT.md.

No computation checks unrestricted complex coefficients, general masks, or unbounded Fourier supports. The identity for all orders above five follows analytically from the range of lattice pair sums, not numerical sampling. Independent external audit: not performed.
