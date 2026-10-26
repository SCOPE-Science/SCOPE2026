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

Run `python3 verify.py` using the Python 3 standard library only. It prints the monomial generators of the first three determinantal ideals, confirms all fourth-order minors vanish, checks ranks of all \(49\) parameter pairs over \(\mathbb F_7\), and ends with `VERIFY_OK`.

The coefficient matrix is reconstructed from binomial expansion of the defining Artin–Schreier polynomial and the universal Cartier residue criterion. Polynomial arithmetic is performed exactly in \(\mathbb F_7[x,a,b]\) and \(\mathbb F_7[a,b]\). The generator-ideal checks enumerate every finite minor and verify both ideal containment and a nonzero unit-multiple witness for each monomial generator; they are symbolic calculations, not a bounded search for geometric curves. The independent prime-field specialization loop verifies ranks as a separate consistency check but does not substitute for the proof over algebraic closures.

The projective smooth normalization, the regular-differential basis, and the interpretation via Serre duality and the relative Hasse–Witt map are established mathematically in the proof. The computation does not independently classify isomorphisms between parameters, global moduli scheme structures, or Ekedahl–Oort types. No independent audit has been performed.
