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

Execute the included \(\texttt{verify.py}\) with Python 3 and no third-party dependencies. The checker enumerates distinct **contiguous** palindromic factors by expanding independently around each character and each gap, then compares their count to the exact formula for all five-tuples with run lengths from one to five (3,125 tuples). It independently checks all 625 four-run tuples in the same range, enumerates all five-run positive compositions for lengths 5–26, compares every defect-histogram cell to rational generating-function coefficients, compares exact first moments, and checks maximum-defect thresholds. The expected last line is \(\texttt{VERIFY_OK}\).

The infinite-domain statements are established by the written factor classification, positive-composition generating-function identities, root-of-unity singularity analysis, and explicit witnesses. Finite checks are cross-checks rather than a substitute for these arguments. The originality evidence is incomplete outside the inspected literature. No independent audit has been performed.
