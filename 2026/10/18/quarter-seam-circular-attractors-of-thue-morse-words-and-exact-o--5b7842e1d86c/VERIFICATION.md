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

The executable `verify.py` requires only Python 3 standard library. Run it from the directory containing the file; the deterministic stdout is recorded in `verification_output.txt`. For every order from two through eight, it enumerates all circular factors of lengths from one through the word length, constructs exact cyclic coverage masks, removes constraints that contain a smaller mask, and recursively enumerates all transversals up to the proved minimum size. Its complete branching argument is given in `RESULT.md`. At orders seven and eight, it compares the entire enumerated optimizer set, not merely its count, against the stated five boundary families. The independent length-thirteen linear factor count in the order-six word supplies the finite input for the general mathematical lower bound.

No computation proves the count of optimal sets at orders greater than eight; that count is not asserted. The all-orders minimum and all-orders sixteen-family construction have separate symbolic proofs. The output file is a recorded same-environment replay, not an independent audit.
