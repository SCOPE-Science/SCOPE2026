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

The proof establishes the congruence classification for all odd starting denominators at least 3. `verify.py` replays four steps of the odd greedy algorithm with exact rational arithmetic, verifies each subtraction is greedy and reconstructs the original fraction. It compares the predicted stopping length for all 10,000 odd denominators 3 through 20,001 and checks the 30 odd residue classes modulo 60. The finite checks are not an infinite certificate; the proof's modular reductions supply the unrestricted argument. Independent audit has not been performed.
