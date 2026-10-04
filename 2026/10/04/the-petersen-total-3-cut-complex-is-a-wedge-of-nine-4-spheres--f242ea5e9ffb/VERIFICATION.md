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

Run `python3 verify_petersen_total_cut.py` with Python 3.

The verifier performs these checks from scratch:

1. Reconstructs the Petersen graph from the displayed 15-edge presentation.
2. Enumerates all independent \(3\)-subsets and confirms there are exactly \(30\).
3. Forms their complements and closes under inclusion, obtaining exactly \(790\) nonempty faces and face vector \((10,45,120,210,240,135,30)\).
4. Rebuilds the sequential element matching with pivots \(0,1,\ldots,9\), checks every matched pair is a Hasse cover, and checks no face is used twice.
5. Orients all \(3510\) Hasse covers in Forman fashion and uses a complete topological-sort test to verify acyclicity.
6. Confirms the unmatched cells consist of one \(0\)-simplex and nine \(4\)-simplices.
7. Separately computes simplicial homology over \(\mathbb F_2\), obtaining Betti vector \((1,0,0,0,9,0,0)\).

The successful terminal marker is `PETERSEN_TOTAL_3_CUT_VERIFY_OK`.

The finite computation proves only the stated Petersen \(k=3\) case. The homotopy conclusion additionally uses the standard theorem of discrete Morse theory that an acyclic matching yields a homotopy-equivalent CW complex with one cell per critical simplex.
