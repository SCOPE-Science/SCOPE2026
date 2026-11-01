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

# Verification of the stated theorem

The proof gives a compact-equivalence reduction, an exact coprime-graph description of the limiting cross-product, and a calculation in the Calkin algebra. It separately proves the finite/infinite cokernel alternatives and the closed/nonclosed range alternatives. These are analytic arguments valid for all the quantified Hilbert spaces, not conclusions from finite sampling.

Run `python3 verify.py` using a Python 3 standard-library interpreter. This verifies exact moment-normalization formulas for nonnegative integral weights; it also checks finite monomial Gram identities for multiple powers and indices, the arithmetic path identities, the finite-path Chebyshev roots, and selected large-index coefficient limits. In the delivered environment it reported `PASS 27276 finite deterministic assertions`.

The script does not numerically certify essential spectra, Fredholmness, infinite multiplicity, or inaccessible source noncoverage. Publication priority remains uncertain and no independent audit was performed.
