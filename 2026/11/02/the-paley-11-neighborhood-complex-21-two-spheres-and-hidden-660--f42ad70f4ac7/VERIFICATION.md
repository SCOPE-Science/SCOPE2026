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

# Reproducibility and boundaries

Run `python3 verify_paley11.py` with Python 3.10 or later. The file uses only the standard library, rebuilds the source complex and finite symmetry group from modular arithmetic, and exits without a success marker if any numerical assertion fails.

The exact checks are: eleven biplane blocks of size five, constant pairwise block intersection two, face vector \((11,55,110,55,11)\), complete \(715\)-incidence discrete-Morse gradient acyclicity after \(110\) pairs, critical-cell counts \(1\) in degree zero and \(21\) in degree two, mod-two boundary ranks \((10,45,44,11)\), exhaustive enumeration of \(660\) full simplicial automorphisms, signed chain-trace calculation on every element, and affine subgroup counts of \(55\) elements.

Terminal marker: `PALEY11_BIPLANE_21S2_FULL660_EQUIVARIANT_CHECKS_OK`.

The integral homotopy result follows from the acyclic matching and the discrete-Morse theorem; the checker does not claim that a mod-two calculation proves an integral theorem. The degree-two character is deduced by Lefschetz after establishing the homotopy type, and its decomposition uses standard finite-group character theory together with published irreducible degrees. Quotient statements use rational transfer after barycentric subdivision. This does not verify integral quotient homology, a rational-to-integral representation lift, or any external independent mathematical audit.
