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

# Reproducible checks

Run `python3 verify_medvedev.py` in the extracted file directory with standard Python 3; no external dependencies are required. The checker independently enumerates every set-theoretic map between all worlds of the full nonempty powerset frames for all nine pairs \(1\le n,m\le3\). At each source world, it computes the image of all accessible worlds and compares it with the accessible worlds of the image, which is exactly the conjunction of forth and back. It compares the complete set of passing world maps against maps induced by all functions on underlying sets and checks the Stirling-number onto count.

A replay from the packaged checker reports `VERIFY_OK all_maps_checked= 826113 all_p_morphisms= 56`. Expected morphism counts for source sizes \(n=1,2,3\), by target sizes \(m=1,2,3\), are respectively \((1,2,3)\), \((1,4,9)\), and \((1,8,27)\). Onto counts are \((1,0,0)\), \((1,2,0)\), and \((1,6,6)\). The checker matches all entries.

These finite checks do not establish the theorem for arbitrary size or infinite sets. That scope is proved by the singleton-image, back-lifting, and inverse-image-intersection arguments in RESULT.md. No independent external audit or certification has been performed.
