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

# Verification details

The all-dimensional argument is the algebraic proof in RESULT.md. The accompanying standard-library script `verify.py` was executed from its actual local source file before packaging. It enumerated derangements for n=2,...,7, checked the signed double sum exactly against \(n\,n!\), checked exact `Fraction` moment formulas and boundary/interior amplification, and checked the occurrence of both signs in derangement matrices exactly from n=4 onward. All tests passed. The key rank-two determinant identity was also independently expanded symbolically with exact arithmetic for n=2,...,5. These are finite corroborations only. The proof covers every n>=2; the first unsigned moment and full law are not established. No independent audit has taken place.
