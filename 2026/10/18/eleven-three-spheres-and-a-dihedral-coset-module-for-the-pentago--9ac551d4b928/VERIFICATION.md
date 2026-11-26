---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For induced components of size at most two, the exact face test is that every selected vertex has at most one selected neighbor. This gave the face vector (10,45,90,75,10). Reconstructing the successive toggles gave the 109 certificate pairs and the 12 stated critical faces; independent depth-first traversal found the directed cover graph acyclic on all 230 nonempty faces and 710 arrows. Forman’s CW conclusion gives one zero-cell and exactly eleven three-cells with constant attaching maps, proving the homotopy conclusion, not just a Betti count. The only five-cycles are the layers: a five-cycle using rungs must use two, since the layer changes are even and rungs cannot be consecutive; three horizontal steps of ±1 cannot close modulo five. Thus an automorphism preserves or swaps the layers and acts by the same dihedral permutation on both since it preserves the rung matching. I evaluated all twenty Lefschetz numbers independently by summing over admissible nonempty unions of vertex cycles; a union of j cycles contributes (−1)^(j−1) after the orientation sign. From L(g)=1−χ₃(g), the values are 11 at identity, 3 at the five layer-swapped reflections, and 1 elsewhere. The fixed-coset formula gives 10, 2 and 0 respectively for G/⟨ts⟩; rational characters determine the semisimple rational modules, so the decomposition and its two invariant dimensions follow. Replay: python3 -B /workspace/branches/independent-checks/record3.py. This verifies a rational module, not an integral group-lattice decomposition or equivariant wedge.

## originality

PASS

Best of current knowledge: neither the integral homotopy type nor the rational action is covered by the inspected claims. There is genuine overlap with later circular-ladder enumerations at n=5, but it is at the level of face numbers and reduced Euler characteristic, not the full topology or representation.

## value

PASS

For an elementary nonchordal circular ladder, allowing isolated edges in the selected face changes ordinary independence topology substantially. The integral homotopy type resolves what the previously compared scalar invariants cannot, and the coset summand identifies how concrete layer/reflection symmetries act, rather than reporting rank alone. The example supplies useful exact data for comparisons within higher independence of ladder graphs and for their symmetry actions, without asserting a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
