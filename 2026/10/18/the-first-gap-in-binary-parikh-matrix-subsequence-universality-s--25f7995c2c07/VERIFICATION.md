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

# Reproducible mathematical checks

Run `python3 verify.py` with Python 3.9+ and no third-party dependencies, in a directory also containing `verification_output.txt`. The program directly tests all binary subsequences (not just arches), counts all 511 words through length eight, and groups them into 255 Parikh-matrix fibers. It also implements an independent bounded-partition recurrence for the exceptional fiber, verifies the only gap and all eight example words, and checks four adjacent class witnesses. A successful run prints exactly the enclosed `verification_output.txt` content.

The exhaustive program verifies a finite cutoff. The proof of its sufficiency lies in the separate arch and all-length-two-factor lemmas in `RESULT.md`. The package does not claim any checked statement at larger total lengths, nor any independent external validation.
