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
Run `python3 verify_paley37.py paley37_integral_certificate.json` with a standard Python 3 interpreter. The code re-enumerates all cliques in the 37-vertex quadratic-residue graph, reconstructs signed integer boundaries, replays every unimodular pivot, compares the full residual matrices against the JSON certificate, checks the 555 compositions of successive boundaries, and computes all 666 affine Lefschetz characters. The recorded `paley37_verification_output.txt` ends with `VERIFICATION SUCCESS`.

The verified face numbers are 37 vertices, 333 edges, 888 triangles and 555 tetrahedra, with no higher simplices. The second boundary has 297 unit factors and zero residual, while the third has 554 unit factors and one residual column with 37 entries of each sign of 26. The only nonzero reduced integral homology is degree two, \(\mathbb Z^{36}\oplus\mathbb Z/26\mathbb Z\). The rational affine character has multiplicities 1, 36 and 629 for respective traces 36, -1 and 0.

The reported checks are complete for this finite input, but do not show a homotopy decomposition, a fundamental-group presentation or equivariant integral torsion behavior. They do not constitute independent external audit.
