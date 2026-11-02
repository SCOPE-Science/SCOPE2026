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

# Verification of the finite conditional cherry law

Run the supplied standalone Python source with `python verify.py`; it uses only the standard library and prints its exact assertion count. It has been executed after extraction from the assembled scientific package and passed **14,279 exact integer and rational checks**.

The checks compare bivariate coefficient extraction with an independent root-split convolution, enumerate every ordered binary shape through nine internal nodes, verify Catalan normalizations and closed cherry-count coefficients through size 159, and check the stated distribution inequalities, the first incomparable size, all parity cases and maximal-tail ratios through size 99. The proof in `RESULT.md` handles unbounded sizes by algebra and a uniform tree-growth coupling, not by extrapolation from this finite test set.

This verification does not constitute independent scientific validation or priority certification.
