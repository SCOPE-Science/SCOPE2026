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

# Verification of the Petersen induced-support theorem

Run `python3 verify.py` with Python 3.9 or later; it needs no third-party dependencies. It generates the Petersen independence complex from pair labels, enumerates all 1,024 vertex restrictions, and independently computes second mod-two homology from exact binary boundary matrices. All ranks are checked against the integer formula from the proof. The six-vertex support list and the five-classes-one-relation model are checked separately. Signed simplicial Lefschetz traces for all 120 permutations are compared with the claimed character formula.

Expected output starts with `VERIFY_OK PETERSEN_INDEPENDENCE F_VECTOR_10_30_30_5 1024_SUBSETS`, followed by the complete dimension profile and signed symmetry trace histogram. The verifiable face vector is \((10,30,30,5)\) in dimensions zero through three. There are five six-vertex supports with one nonzero second-homology class each, and the full second homology has rank four.

The computations run over \(\mathbb F_2\) and verify the finite claims but do **not** independently certify integral torsion-freeness, primitivity, or injectivity for all finite graphs. Those assertions have an explicit integral proof using the graph-star cover, its nerve, the relative chain complex and the integral four-simplex boundary calculation. No independent external audit has been performed.
