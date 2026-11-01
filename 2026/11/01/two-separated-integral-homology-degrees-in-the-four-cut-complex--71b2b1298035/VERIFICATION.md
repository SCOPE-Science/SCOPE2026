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

# Verification of integral four-cut homology

Run `python3 verify.py` with Python 3.9+ and no external packages. The checker enumerates all fifteen graph vertices and all 32768 vertex subsets, generates the 390 disconnected-four-set facet complements, and cross-checks facet closure with a separate complement-predicate evaluation. It checks every one of the 212910 directed cover incidences for matching acyclicity; computes the critical-cell dimensions, signed integral degree-eight Morse boundary, and five explicitly primitive columns; and independently recomputes full simplicial mod-two homology.

Actual checked values: 29654 augmented faces, 14781 Morse pairs, critical counts 5 in dimension seven, 72 in dimension eight and 15 in dimension ten. Five unit columns at indices 2,7,21,39,49 show that degree-eight boundary is surjective onto its five-dimensional integral target. Its kernel is free rank 67. No critical degree-nine cells exist, so degree-ten boundary is zero, giving fifteen free generators. Independent reduced mod-two Betti vector is `(0,0,0,0,0,0,0,0,67,0,15)`.

The attached `verification_output.txt` is the captured successful checker run, ending in `J6_FOUR_CUT_HOMOLOGY_CERTIFICATE_OK`. The program provides a complete finite verification, not an infinite-family theorem or a determination of higher-dimensional attaching maps. It is not independent human audit or certification.
