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
# Reproducibility record

From the package root run `python3 verify.py` using Python 3.10+ with `sympy`. The checker constructs the folded-five-cube graph directly; 16 neighborhoods generate exactly 352 faces, with face vector (16,80,160,80,16). Every rational simplicial boundary is built with increasing-vertex signs; all three consecutive chain-boundary compositions are zero and exact rational ranks are (15,65,64,16). The resulting reduced rational Betti vector has its sole entry of 31 in degree two.

The group action is evaluated on every 5-coordinate permutation and every quotient translation: 120 x 16 = 1920 affine elements. The program computes the signed fixed-face Hopf trace for every element. Exact Fourier projections verify that the translation-character multiplicities are 6 for the zero weight, 1 for each of ten weight-two labels, and 3 for each of five weight-four labels. All 120 elements of the whole coordinate-permutation group are checked against the character of the second exterior power of its standard representation on the zero-weight space. The weight-two stabilizer's 12 elements and weight-four stabilizer's 24 elements are checked against their displayed exact sign/standard characters. Conjugation transports these checks to every other weight label.

Expected terminal lines:

`VERIFY_OK 16_VERTICES 352_FACES BOUNDARY_RANKS_15_65_64_16`

`AFFINE_AUTOMORPHISMS_1920 HOMOLOGY_31 IRREDUCIBLES_6_10_15`

The finite checker uses exact integers and SymPy rational ranks. The separate irreducibility conclusion uses standard rational finite-group representation theory. No integral decomposition, formal verification, or independent external validation is asserted.
