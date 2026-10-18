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

# Reproducible verification

Run `python verify.py` with a standard Python 3 interpreter. The script does not need nonstandard packages or network access.

It verifies the 24 transition inequalities and 12 terminal inequalities using exact rational arithmetic; it checks the rank-threshold identity and finite bound exhaustively for all permutations of \(2\) through \(9\) ranks (409112 configurations); and it independently computes subset dynamic-programming minima for \(2\le n\le16\), checking 131053 nonempty subset states against the claimed inequality. It also integrates the piecewise-affine support profile exactly and verifies \(13/24\).

All runs of this verification program completed without assertion failures. The unlimited-sample theorem is proved in `RESULT.md` by the explicit finite-state certificate and telescoping argument. Finite enumeration alone would not prove the claim. The sharpness of the asymptotic constant as the *attainable* minimum remains unproved.
