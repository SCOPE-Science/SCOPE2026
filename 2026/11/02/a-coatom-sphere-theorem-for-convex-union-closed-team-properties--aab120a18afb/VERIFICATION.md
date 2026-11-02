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

# Verification details

`python3 checker.py` tests all families of teams for universe sizes 1 through 4 against both defining closure axioms. It independently generates the same complete weak-ideal lists from the upsets of each maximum team and checks all predicted coatoms, coatom-intersection emptiness conditions, and recursively computed whole-lattice Möbius invariants.

Expected output:
```
n=1 weak_ideals=4 coatoms=2 mobius=1 OK
n=2 weak_ideals=11 coatoms=3 mobius=-1 OK
n=3 weak_ideals=42 coatoms=4 mobius=1 OK
n=4 weak_ideals=283 coatoms=5 mobius=-1 OK
ALL_CHECKS_OK
```

The source is standalone Python with standard-library dependencies only. Brute-force enumeration covers every family for these tested sizes; no enumeration beyond size four is claimed. The general sphere statement follows from the finite nerve lemma and the proof of the coatom-intersection pattern. No independent audit or external proof certification is claimed.
