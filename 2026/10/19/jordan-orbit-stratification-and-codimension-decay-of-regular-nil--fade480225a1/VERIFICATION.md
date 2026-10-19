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

Run `python3 checker.py` with Python 3.9 or later; only the standard library is required. This enumerates the whole restricted-range matrix semigroup for nine parameters with \(q\in\{2,3\}\), \(r\le3\), and \(c\le2\), and checks nilpotent counts, partition multiplicities, actual Jordan types and ranks. For \(q=2,r=2,c=1\), it also enumerates every potential inner inverse and checks \(TUT=T\) directly for all \(64\) transformations. A successful execution prints `VERIFY_OK`.

The checker is finite and does not establish the infinite-field statement. The accompanying mathematical proof uses block regularity, shear conjugation, standard nilpotent Jordan centralizers and an elementary fiber count. The full text sources on restricted-range semigroup regularity and maximal regular subsemigroups are cited in the result. No external independent scientific audit has been performed.
