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

Run `python3 verify.py` with a Python 3 standard-library interpreter. There are no external input files, random seeds or installation requirements. The script builds all \(inom{L-1}{6}\) normalized eight-point integer sets at each \(7\le L\le16\), discards nonprimitive sets, and computes all restricted fourfold sums in two exact ways. It asserts the minimum at all ten diameters and the exact equality list at the first failing diameter.

The script was executed and returned `VERIFY_OK`. At diameter sixteen it counted 5005 normalized candidates, 4998 primitive candidates, minimum 25 and exactly three extremizers. The finite exhaustive enumeration is complete for the stated range; it does not prove claims for larger diameters, an unbounded set-size parameter or additional independent validation.
