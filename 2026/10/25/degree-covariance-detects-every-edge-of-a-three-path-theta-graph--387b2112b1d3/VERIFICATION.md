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

# Finite exact verification

Run `python verify.py` using Python 3 without external dependencies. The program constructs each theta graph for all 216 ordered length triples from `{2,3,4,5,6,7}^3`; enumerates all candidates for deleting two edges, independently checks connectivity, computes exact rational moments and degree covariances directly from actual spanning trees, verifies the distinct-edge deletion kernel, verifies the two adjacent-edge closed forms, tests strict negativity for every nonedge, classifies nonnegative adjacent entries and sharp zero cases, and checks covariance row sums. It reports `VERIFY_OK 216 parameter triples; 35865 exact checks`.

The finite range is not a proof of the unrestricted theorem. The all-parameter argument in `RESULT.md` follows from the two-edge deletion bijection, the exact covariance kernel, and elementary positivity inequalities. No independent mathematical audit or external formal certification has been conducted.
