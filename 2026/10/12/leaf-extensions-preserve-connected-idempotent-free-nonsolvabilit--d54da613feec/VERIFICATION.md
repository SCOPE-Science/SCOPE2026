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

The leaf-extension theorem is proved symbolically in `RESULT.md`; it is not inferred from computation. In particular, the proof checks idempotent coordinates, annihilator coordinates, graph connectivity, and termwise inclusion of derived series for arbitrary numbers of attached leaves.

The finite program `verify.py` is only a regression check for the explicit Hu--Wen corollary. It verifies the displayed multiplication identities, nonzero natural-basis squares, graph connectivity, expected derived-space ranks, and exhaustive absence of nonzero idempotents in selected small prime fields and dimensions.

A successful run ends with `CHECK_OK`. Finite checks are not used as evidence for the infinite quantifiers.
