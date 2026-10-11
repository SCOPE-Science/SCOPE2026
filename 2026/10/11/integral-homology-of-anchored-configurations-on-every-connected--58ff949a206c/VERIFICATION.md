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

# Verification and reproducibility

The core certificate is the proof in `RESULT.md`: a homotopy equivalence of pointed graphs relative to all anchor vertices, followed by an integral direct-sum decomposition of cellular chains into shifted tree-anchored complexes. The published tree homotopy theorem supplies the necessary integral free homology groups, including the cases of one anchor and exactly as many particles as anchors. No computer calculation is used to infer infinite torsion-freeness.

For an independent finite **mod-two** check, run `python3 verify_anchored.py` with Python 3. The script constructs all cubical cells of each finite test graph, builds each boundary matrix by enumerating oriented edge endpoints, computes ranks by exact bit-vector elimination over \(\mathbb F_2\), then compares its Betti vector to the theorem's closed formulas. The actual output ends with `VERIFY_OK 14 exact cubical boundary-rank comparisons`. The graph family includes small trees, cycles, a cycle with a tail, a wedge of two triangles, and the complete graph on four vertices; special tests cover one anchor and \(n=r\).

The finite computations do **not** test every graph or every number of particles, do not certify any integral Smith normal form, and are not a proof that no torsion exists. The infinite proof is the integral chain splitting and the cited theorem for trees. No independent audit or external validation has been performed.
