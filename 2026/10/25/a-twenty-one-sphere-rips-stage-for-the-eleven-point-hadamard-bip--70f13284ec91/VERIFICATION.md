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

# Reproducible verification

Run `python3 verify_biplane11.py CERTIFICATE.json` using Python 3. No third-party libraries are needed. The checker recomputes the unique cyclic incidence description, design pair counts, diameter at most three, all 4,776 scale-two faces, the 55 actual elementary collapses from the 11-facet block complex to its two-dimensional core, the 45 triangle-relator elimination steps proving its fundamental group trivial, binary homology ranks at scale two, and orientation-signed Lefschetz numbers for all 11 cyclic translations.

The certificate uses integer bitmasks for block-complex faces; an integer bitmask records which point labels occur. The stored pair lists are replayed against a freshly generated complex and checked for the free-face condition at every step. A triangle eliminates an edge only when its other two edges are already trivial in the chosen spanning-tree presentation. The checker asserts the full two-pass elimination, not just a final count.

Expected markers: `BIPLANE11_DESIGN_VERIFIED 11 5 2`, `BIPLANE11_DOWKER_COLLAPSES_AND_PI1_VERIFIED 55 45 [30, 15]`, `BIPLANE11_RIPS2_MOD2_HOMOLOGY_VERIFIED 4776`, and `BIPLANE11_CYCLIC_LEFSCHETZ_VERIFIED [-21, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`.

The binary chain calculation is finite corroboration, while the free-face and group-presentation certificates support the exact integer homotopy argument. The general homotopy-pushout argument is proved symbolically, not verified by a finite enumeration. No claims concern independent audit or broader families.
