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

# Verification record

The complete all-parameter analytic argument is in `RESULT.md`, Sections 1--7 of its proof. The reproducible companion is `verify_colouring_frame.py`, requiring Python 3 and only the standard library. Execute `python3 verify_colouring_frame.py`. It checks 242 exact rational spatial-block eigensystems and colouring recurrences, direct enumeration of eight small graph/palette instances including 3756 independently assembled full complex Fourier Gram entries, exact rank and threshold identities, and numerical consistency of the proved fixed-dimension asymptotic.

The direct enumerations are finite and do not prove the general claim by themselves. The proof separately establishes the strict rank and frame bounds for every admissible integer parameter. The checker is not external validation or formal certification. No independent audit has been performed.
