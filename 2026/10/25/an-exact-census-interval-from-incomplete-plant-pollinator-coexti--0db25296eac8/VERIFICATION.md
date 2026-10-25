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

# Reproduction

Run `python verify.py` with Python 3, with the script and `verification_certificate.json` placed in the same directory. The script uses integer and exact-rational arithmetic and prints one canonical JSON object. Its output is byte-for-byte identical to the certificate's content after removing its final newline.

Checks include exact inverse subset transforms, complete feasible census intervals with adjacent excluded integers, direct enumeration of small OR-mixture probability laws, explicit parity witnesses for three through nine plants, and the three-census example. The certificate is from an actual execution of the distributed script.

The exhaustive cases are finite; the universal mathematical proof is in `RESULT.md`. The bibliography is same-document literature comparison rather than independent validation. No independent audit has been performed.
