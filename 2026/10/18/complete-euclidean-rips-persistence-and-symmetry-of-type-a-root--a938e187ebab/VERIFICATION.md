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

# Verification procedure

The complete calculation is supported by `verify_a_root_rips.py`, which uses the Python standard library only. Run `python3 verify_a_root_rips.py`; it should end with `VERIFY_OK`. The script computes exact integer squared distances and enumerates first- and second-scale simplices for \(n=4,5,6\). For \(n=4,5\), ranks of the full simplicial boundary matrices over two distinct prime fields give the predicted Betti dimensions. For \(n=5\), all 240 group elements are tested against signed Lefschetz characters on the actual simplicial complexes. The penultimate stage is checked symbolically as an antipodal-pair join, so enumerating its exponentially many faces is unnecessary.

The proof that these results hold integrally for every \(n\ge5\) is **not computational extrapolation**: it is the exact nerve of a bipartite graph, a homotopy equivalence proved by contractible poset fibers, an explicit \(\ell^1\)-sphere model, and a cross-polytope join. The equivariant version follows by fixed-subgroup fiber contractibility and determinant computations. The file does not certify arbitrary other root systems, quotients, or unknown prior literature.
