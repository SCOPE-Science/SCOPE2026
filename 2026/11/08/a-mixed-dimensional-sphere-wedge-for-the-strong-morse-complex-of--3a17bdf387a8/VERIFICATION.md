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

# Reproducible mathematical verification

The standalone Python 3 script `verify.py` uses only the standard library. Invoke `python3 verify.py`; its recorded output is embedded in `verify_output.txt`.

It exhaustively visits all 720 vertex permutations, constructs the downward closure of the resulting strong gradients, verifies 91 distinct generators and 36 maximal faces, and checks the complete face vector \((14,57,58,10)\). A deterministic coordinate-toggle procedure provides 66 matched incidences and leaves one vertex, one edge and five triangles. The directed Hasse graph is explicitly checked to be acyclic on all 139 faces and 328 incidences.

Signed chain reductions then cancel the 66 pairs with integer unit pivots. The resulting seven-cell differential is exactly zero, establishing the degree-zero attachments in the discrete-Morse CW model. The final assertion of the verifier is `ALL_VERIFY_OK`.

These exact checks prove the stated **finite** homotopy classification using the standard discrete-Morse CW theorem. They do not furnish a formula for larger theta graphs, a general graph classification or independent external validation.
