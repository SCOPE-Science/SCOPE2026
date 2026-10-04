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
# Verification

The lower bound is proof-based.

For a surjective bounded morphism onto a universal \(m\)-world relation, the back condition forces every source equivalence class to map onto all \(m\) target worlds, so every class has at least \(m\) elements.

For two agents, properness makes every intersection of a first-agent equivalence class with a second-agent equivalence class have size at most one. Hence one first-agent class of size at least \(m\) meets at least \(m\) distinct second-agent classes, each containing at least \(m\) points. Therefore the source has at least \(m^2\) worlds.

Equality forces both partitions to have exactly \(m\) blocks of size \(m\) with singleton cross-intersections. The bounded morphism is then bijective on every block, so its labels form a Latin square.

The bundled `verify.py` constructs cyclic optimal covers for \(1\le m\le12\), checks properness and the bounded-morphism conditions, and exhaustively checks the combinatorial lower-bound obstruction and equality-grid structure for \(m=2,3\).

## Limits

The finite enumeration is corroborative only. The theorem for arbitrary \(m\) follows from the proof. The result is specific to two-agent S5 covers.
