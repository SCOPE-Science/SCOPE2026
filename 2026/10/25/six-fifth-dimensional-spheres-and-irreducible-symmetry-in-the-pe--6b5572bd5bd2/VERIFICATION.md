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

# Reproduction of the mathematical checks

Run `python3 VERIFY.py` in the directory containing this file. The program depends only on the Python 3 standard library, takes no input, and exits with a nonzero status if any asserted check fails. Its actual recorded standard output is embedded as `VERIFY_OUTPUT.txt`.

The two complete enumerations agree on all \(2^{10}\) vertex masks. `VERIFY.py` constructs the ordinary nonempty face poset, performs the stated deterministic pivot matching, enumerates every cover relation, and checks the entire directed graph for acyclicity by topological sorting. Critical cells are a single vertex and six five-cells, proving the integral wedge-of-spheres homotopy type by discrete Morse theory. No finite homology experiment is substituted for an infinite or general-case theorem.

The mod-two simplicial chain-boundary ranks are independently recomputed from all faces of the original complex as a consistency check, not as an integral torsion certificate. The complete \(\mathfrak S_5\) group action is checked elementwise by label permutations. The representation proof uses the already established concentration of integral homology, the signed simplicial Lefschetz formula, and an independent exterior-square character formula; all \(120\) traces agree. A character inner product check gives irreducibility. Nothing here asserts a computation for other graphs, an integral representation classification, independent audit, or certification outside the stated checks.
