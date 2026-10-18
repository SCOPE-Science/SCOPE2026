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

# Reproducibility
Run `python3 verify.py` with Python 3 and no third-party packages. The script independently constructs matrix-unit products and exhaustively enumerates every element in five finite-field algebras, tests the equation \(v^2=1\), groups involutions by residue signs and checks the predicted counts. It also checks the predicted unit-plus-involution count at every algebra element.

Cases: \(T_3(\mathbb F_3)\), \(T_2(\mathbb F_5)\), and three 5-dimensional radical-square-zero quiver algebras over \(\mathbb F_3\). Expected counts respectively: \((729,56)\), \((125,12)\), and \((243,32)\) for each of three remaining cases, where the entries are total elements and involutions. The run completed with `VERIFY_OK`.

These are exhaustive **finite** computations only. The uniform statement for all admissible finite-dimensional algebras follows from the conjugation proof, Peirce decomposition, orbit–stabilizer and unit detection in `RESULT.md`. No independent mathematical audit is claimed.
