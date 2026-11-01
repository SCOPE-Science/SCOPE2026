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

# Verification

`CHECK.py` is standalone and requires Python 3 with `sympy`. Run `python CHECK.py` from the same directory as the six documents. It confirms the exact equivalent multiplier formula, the total-mass equation, the product factorization, the fixed-face degeneracy at \(\alpha=1\), 72 admissible exact-rational normalized-product comparisons and 60 strict edge-drift comparisons. A passing process prints `PASS` and exits with status zero.

The proof's infinite statements are not certified by enumeration. Their decisive steps are the positive-factor AM–GM inequality, stationarity of the bounded mass and product observables, edge restriction/invariance, and the subsequence contradiction for nonzero limiting normalized product. The checked code has no dependency on private files, previous records or external network access.

No independent mathematical audit has been performed.
