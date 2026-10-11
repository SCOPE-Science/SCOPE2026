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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and the standard library; no external files or dependencies are needed. The program independently constructs fixed simplices as partial functions, rejects directed cycles, computes action signs on simplex vertices, constructs the weighted orbit Laplacian and evaluates exact determinants. It checks both sides at enough distinct integers to determine their full polynomial in each finite instance.

Observed execution:

```text
VERIFY_OK: 293 exhaustive graph-automorphism cases through four
VERIFY_OK: complete-graph cycle product, every permutation on 2..6
VERIFY_OK: three six-vertex nontrivial actions with graded traces
```

The first test covers every labeled graph with one through four vertices and every one of its graph automorphisms, not all graphs of arbitrary order. The second test checks all permutation cycle types through order six by iterating over every permutation. The third tests two inequivalent automorphisms of the complete bipartite graph and a cycle half-rotation. Arithmetic uses fractions, not numerical tolerances. These checks test the derivation; the infinite quantified claim is proved symbolically in `RESULT.md`. Chain and homology traces are related only through the alternating Hopf trace identity, so no individual homology character or integral torsion assertion is verified here.
