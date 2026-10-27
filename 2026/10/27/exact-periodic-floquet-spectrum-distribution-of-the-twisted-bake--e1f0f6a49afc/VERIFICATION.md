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

# Mathematical verification
The complete derivation is in `RESULT.md`, including the exact signed-cycle factors, the attainable weak compositions, the stars-and-bars multiplicity and the sharp ratio extremizers.

Execute `python check_partition_spectra.py` using Python's standard library. The program independently enumerates all binary words at dimensions \(2\le M\le6\) and return lengths \(1\le n\le8\), constructs the exact integer iterate Jacobians, computes characteristic polynomials with an exact matrix algorithm, and compares observed frequencies to the closed formulas. It also verifies that the spectral-class count equals the integer-partition count and total frequency equals \(\binom nk\).

The actual execution output was `CHECK_OK 2510 exact Jacobian characteristic-polynomial comparisons, 180 exact spectral-frequency distributions`.

These finite checks do not certify the all-dimensional theorem or historical novelty. Those rely respectively on the self-contained general proof plus the cited published coding theorem, and on the stated source/claim comparisons. No independent audit has been performed.
