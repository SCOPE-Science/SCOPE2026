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

# Reproducible finite checks
Run `python3 verify.py` using the Python 3 standard library. The program enumerates admissible interval-row relations through dual size eight, compares the full tense-space condition against every binary relation through dual size four, and separately tests the reduced negative-tense axioms (including the two adjunction inequalities and compatibility inequalities) for all antitone unary operator pairs through dual size five. Expected output concludes in `VERIFY_OK`. The unrestricted conclusion comes from the written combinatorial proof, not finite exhaustion.
