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

The theorem uses the explicit real symmetric matrix and forcing sequence given in RESULT.md. Those formulas suffice to reconstruct every step for all admissible arm-length tuples. An accompanying standalone Python program `verify.py` reconstructs distances rather than assuming the proposed matrix's support, then verifies the off-diagonal matrix pattern, complete integer nullspace witnesses, linear independence on first-coordinate blocks, and every individual unique-neighbor force.

Command: `python3 verify.py`

Observed output: `VERIFY_OK heterogeneous_cases=48 explicit_null_vectors=300 verified_forces=516 exhaustive_cases=5`

The program tested 48 parameter tuples, checked 300 explicit kernel vectors and 516 forcing moves, and exhaustively ruled out smaller forcing sets in five small instances. This is reproducibility evidence, not an exhaustive check of infinitely many arm lengths or powers. The published graph-power upper bound and traditional maximum-nullity/zero-forcing inequality are acknowledged as prior mathematical inputs. An independent mathematical audit has not been performed.
