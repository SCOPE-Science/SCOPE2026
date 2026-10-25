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

# Verification of the degree-one \(\Gamma\)-comparison

The general argument is an exact integer-chain calculation. Its two nontrivial directions are: (i) every cubical two-boundary becomes the boundary of two simplicial triangles on opposite stars; (ii) the cube patterns \((a,b,a,a)\) and \((a,b,c,b)\) realize respectively each reversal and each simplicial triangle boundary. The proof does not require the finite experiments.

The executable `gamma_compare_verify.py` uses the vertex-image definition of singular \(\Gamma\)-cubes and directly enumerates each admissible two-cube. It checks these identities over signed integral oriented edges across 65 hypergraph instances, including 60 reproducibly seeded cases. This exercises 25,427 admissible cubes and 502 associated edges. For the stated six-vertex projective-plane example, the script checks every vertex link, every edge incidence, the Euler characteristic, the chain relation, and the exact Smith diagonal of the integral boundary matrices.

Reproduction command: `python3 gamma_compare_verify.py`. The Python program uses SymPy for Smith normal form; the checked environment used Python 3.13.5 and SymPy 1.14.0. Exact expected stdout is embedded in `verification.log`.

Scientific limits: this verifier tests finitely many instances and one integral torsion example, not every possible hypergraph or higher-degree homology. The universal statement is supported by the symbolic proof in `RESULT.md`. No independent mathematical audit was performed.
