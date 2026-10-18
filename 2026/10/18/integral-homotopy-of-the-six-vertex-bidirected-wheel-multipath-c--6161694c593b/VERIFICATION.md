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

# Verification and reproducibility

All three programs below are embedded in the same directory and use only the Python standard library. Re-run from that directory with a recent Python 3 installation:

`python3 verify_wheel_homology.py`

`python3 verify_wheel_cup.py`

`python3 direct_gf2_check.py`

The exhaustive face model has 871 augmented faces, 2910 incidences, 408 matched pairs, and 55 critical nonempty simplices (12 of dimension two, 33 of dimension three, 10 of dimension four). The empty face is paired with a vertex. The integer three-to-two Morse differential has ten unit invariant factors and the four-to-three Morse differential is zero. The separate direct modular simplicial-boundary calculation confirms the ranks but does not itself establish integral torsion-freeness.

The attaching-map program verifies the two pulled-back integral degree-two cocycles on all 310 three-simplices. It constructs ten integer four-cycles, each containing six original four-simplices, and checks their complete simplicial boundaries vanish. All forty ordered integral cup-product evaluations are zero. The vanishing of these quadratic invariants, combined with the torsion-free Hilton–Milnor third-homotopy group of a two-sphere wedge and the zero three-sphere cellular degrees, proves that the remaining four-cell attaching maps are nullhomotopic.

The programs certify exactly the stated six-vertex instance and do not establish larger-wheel homotopy classifications or resolve publication priority. External independent mathematical validation remains unperformed.
