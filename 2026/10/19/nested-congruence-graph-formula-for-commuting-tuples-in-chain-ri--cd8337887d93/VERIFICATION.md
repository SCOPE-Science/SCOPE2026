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

# Reproducibility and boundary checks

Run `python verify.py` from the same directory using Python 3 and its standard library. The checker constructs ring addition and multiplication for both \(\mathbb Z/p^L\mathbb Z\) and truncated polynomial rings \(\mathbb F_p[\varepsilon]/(\varepsilon^L)\). It multiplies quiver-algebra elements using diagonal idempotents and arrows, independently determines commuting pairs, then counts compatible ordered tuples by exhaustive traversal of the literal adjacency relation. It evaluates the nested-subgraph expression separately and checks equality in twelve cases: both ring types at residue order two and lengths two and three, two parallel arrows, a three-vertex path, reversed orientation, a loop, arities one through three, and integer residue order three.

Observed final marker: `VERIFY_OK_NESTED_CHAIN_QUIVER`. Representative verified counts: for one arrow over either length-two ring of residue order two, \(C_2=1408\) and \(C_3=25600\); for a two-edge path over those rings, \(C_2=123904\); for one arrow over length-three rings, \(C_2=47104\). An independent exhaustive calculation for the integer chain ring of order nine gives \(C_2=76545\).

Exhaustion covers only these finite configurations. It does not establish the statement for unbounded quivers, tuple arity, or chain length; the written proof handles those quantifiers. Only commutative chain rings are claimed. There has been no independent mathematical audit.
