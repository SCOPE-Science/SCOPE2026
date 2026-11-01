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

# Exact finite verification

The bundled `verify.py` uses the Python standard library only. Run `python3 verify.py` from the package directory and compare its full stdout with `verification_output.txt`. It checks the Clebsch graph via XOR generators and every possible subset of its sixteen vertices, then tests the 2-independence condition exactly. The 2,143 augmented simplices have 2,142 ordinary nonempty faces and 9,280 face-poset incidences. The deterministic ordinary acyclic matching has 1,065 pairs and critical-cell dimensions \(0,3,4\) with multiplicities \(1,5,6\).

A complete topological sort of the signed/reversed Hasse graph establishes acyclicity. Recursive signed algebraic Morse pivot elimination computes the five-by-six integral cellular boundary, with a unimodular five-by-five minor. The proof in `RESULT.md` uses this boundary together with the Hurewicz theorem, not a finite homology inference, to establish \(S^4\). An independent full simplicial boundary rank calculation over \(\mathbb F_2\) gives reduced fourth Betti number one, and face Euler characteristic equals two. Symmetry checks explicitly verify four basis translations, an \(S_5\)-transposition and a five-cycle as automorphisms, then calculate signed fixed-face Lefschetz numbers, determining the integral homology character.

**Limitations:** This is exhaustive only for the fixed 16-vertex graph. The finite checker does not establish scientific priority or a larger-graph theorem. Full group structure and the homotopy interpretation of the integral boundary require the accompanying mathematical proof; sampled automorphism checks alone would not determine a general unrelated group representation.
