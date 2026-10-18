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

Run `python3 verify.py` and confirm `VERIFY_OK`. The checker validates the eight-state-pair closure, reconstructs the coded Rudin–Shapiro prefix, enumerates all length-\(2^m\) windows from each exact two-tile image for \(4\le m\le16\), and asserts all thirteen claimed counts. The independent direct-index parity comparison is performed at the first seven specified scales. Canonical sorted-profile hashes can be compared with `certificates.json`. The exhaustive infinite-factor reduction is proved in `RESULT.md`; this verification checks finite cases only. No independent audit has been performed.
