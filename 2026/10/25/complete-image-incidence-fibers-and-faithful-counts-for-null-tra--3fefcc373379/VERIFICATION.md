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

# Reproduction and limits

Run `python3 verify.py` in the extracted package directory, with Python 3 standard library. The verifier constructs every total map fixing the distinguished point, independently tests all pairwise products, computes each exact image-incidence cell vector, and tests every profile against the analytical integer formula. It also compares the number of pairs with all semigroup images distinct against the signed-Stirling inversion.

Exhaustive parameters: \((n,m)=(0,1),(1,1),(2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3),(3,3)\).

Selected exact outputs: \((n,m)=(4,2)\): total \(553\), faithful \(432\), occupied profile vectors \(10\). \((n,m)=(3,3)\): total \(226\), faithful \(18\), occupied profile vectors \(14\). Finite checks do not establish the unrestricted theorem, whose proof is in `RESULT.md`.

A successful run ends with `VERIFY_OK_NULL_TRANSFORMATION_IMAGE_INCIDENCE`. Independent validation was not performed.
