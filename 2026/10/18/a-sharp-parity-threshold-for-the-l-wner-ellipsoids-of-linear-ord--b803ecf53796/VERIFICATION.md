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

# Verification summary

Run `python3 CHECKER.py` with SymPy installed. The checker uses exact rational arithmetic to enumerate all 24, 120 and 720 rank permutations for n=4,5,6; filters by parity; constructs the signed comparison covariance and theoretical parity corrections; verifies spectral/projector identities, strictly positive covariance, exact determinants and the squared contact equality for every allowed vertex.

Observed success included the exact squared enclosing-volume ratios 64/125 for n=4 and n=5 and 1 for n=6. This is not an exhaustive infinite-dimensional computation. The all-order step instead follows from the involution swapping two labels outside the at-most-four-label support of a covariance entry; the AM–GM argument certifies the resulting ellipsoids without numeric optimization. No external independent audit was performed.
