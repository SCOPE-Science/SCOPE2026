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
# Verification of the area-spectrum theorem

The proof establishes the following checks for every permitted parameter, rather than inferring universal results from examples: (i) the derivative dominance yields positive Jacobian and global injectivity; (ii) the normalized Schur quotient is analytic and vanishes at the origin; (iii) Schwarz's lemma bounds the coanalytic derivative by the analytic shift; (iv) Parseval supplies the nonnegative coefficient weights in the lower area remainder; (v) equality gives exactly the quadratic shears; (vi) positive-real-part coefficient estimates give the already-known upper area formula; (vii) two admitted families continuously and explicitly fill the entire claimed range, including the total-area limit.

For additional reproducibility run `python3 verify_area_spectrum.py` with Python 3. It verifies 120 algebraic normalizations and comparisons for rational parameters and compares the analytic extremal family to independent Taylor truncations. The computations provide consistency checks only. The cited 2016 and 2013 articles could not be completely inspected and unindexed equivalent results remain an originality risk.
