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
Run `python3 verify.py` with the standard library. The script tests a large finite family of arbitrary path, cycle and complete first factors against regular cycles, cliques and one disconnected regular factor; it verifies per-round partition equivalence and exact stable depth on 405 product pairs. It also checks that 80 pairs of connected cylinders and disconnected regular alternatives have equal color histograms. It prints a single `PASS` line on success.

The proof in RESULT.md, not the experiment, establishes the universal quantifiers. The Cartesian-prime automorphism theorem is cited rather than independently recertified. No independent audit has been performed.
