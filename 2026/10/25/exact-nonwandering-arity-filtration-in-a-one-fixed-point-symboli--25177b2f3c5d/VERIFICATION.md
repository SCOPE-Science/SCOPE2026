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
# Verification

Run `python3 verify.py` with the Python standard library. The verifier independently computes minimum admissible directed-edge covers with an exact bitmask dynamic program for 53 nonempty configurations with \(a,b,c\in\{0,1,2\}\), then checks actual binary shift configurations at a common integer time against local source and target words. It outputs `VERIFY_OK` if all assertions pass. This tests the formula and constructions in a finite range; the full mathematical statement is proved analytically in `RESULT.md`.

The original primary paper was examined in its full publicly readable arXiv form. Older relevant sources were examined to the accessible abstract level only; their inaccessible full text is an originality risk. No external independent audit has been performed.
