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
The included `verify.py` is a self-contained exhaustive checker using Python 3.11+ and SymPy. It enumerates all 23,624 simplicial faces of the ordinary cube-graph Morse complex, constructs the deterministic face-poset matching, verifies acyclicity using a topological sort over all 23,625 augmented faces and 124,200 cover relations, computes the signed 50-by-185 Morse boundary matrix, and independently checks exact rational rank, Smith normal form and a 46-by-46 determinant-one minor. It passes only after the computed reduced integral homology ranks are 4 and 139, with no torsion. This proof does not rely on floating-point calculations or truncation.

Run `python verify.py`. The captured output is in `verification_output.txt`. Run `python crosscheck.py` to repeat the independent undirected-edge enumeration and mod-two top-dimensional elimination; its captured output appears in `crosscheck_output.txt`. The checks were executed for the exact included program bytes. The homotopy conclusion uses the fact that the associated CW structure contains only one vertex, 50 five-cells, and 185 six-cells, and \(\pi_5(\bigvee^{50}S^5)\cong\mathbb Z^{50}\).

Limitations: Independent mathematical validation is not performed, and the inaccessible 2020 directed-forest Cayley-graph thesis remains an originality risk. The calculation is finite and makes no claim concerning other cube dimensions.
