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

# Reproduction and scope

Run `python3 verify.py` with `certificate.csv` in the same directory. The checker independently constructs order-five cycles using complete five-factor backtracking and using local two-arc Euler-tour orderings, verifies that both lists are identical, and tests the 2,048 canonical cycles with two independent distance implementations. It checks the five-value histogram, all four optimizers and their common complete profile, the symmetry orbit, and the complete CSV certificate. Its successful final line is `VERIFY_OK`.

The finite exhaustive computation is the proof vehicle for the census. It verifies precisely order five; any infinite-order extrapolation remains unproved. All arithmetic in the checker is exact integer arithmetic. The verification here is reproducible computational evidence, not an independent audit or formal verification in an external proof assistant.
