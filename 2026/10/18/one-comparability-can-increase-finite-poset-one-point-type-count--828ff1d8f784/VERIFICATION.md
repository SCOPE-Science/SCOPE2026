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

Run `python3 verify.py` from the same directory. The checker derives transitive closures for posets and all possible one-point extensions rather than relying on the proof's closed-form counting. It independently verifies all comparison instances through four old vertices, canonicalizes increasing pairs, reports all six classes, and checks the infinite-family identities on all \(1\le a,b\le4\). The exact software is included. Successful finite checking does not establish the universal formulas, which are proved symbolically in `RESULT.md`.

The inspected source for the one-point-extension downset/filter construction is Dolinka–Mašulović, Lemma 4.3, *Proceedings of the Edinburgh Mathematical Society* 55 (2012), p. 648. The related 2026 public mathematical record's complete `RESULT.md` was read for implication coverage. Pretzel (1980) was available only via abstract; its full text was not inspected. No external independent audit has been performed.
