---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In attack-topological order each head sees only decided predecessors, so the recursion has an order-independent solution K and its attack targets are exactly A minus K. For a complete E, inductively a head rejected by K is attacked by E through the same accepted tail; each tail of an accepted head contains a rejected predecessor, already attacked by E, so E attacks any closed attacker of this head. Completeness forces acceptance. Stability forces the same membership recursion directly. When K is closed, it defends each member by attacking an outsider in each attacking tail; for a rejected head a firing tail T has closed attacker cl_S(T) contained in K, which conflict-freeness prevents K from attacking. This proves all three families are {K} or empty, even with empty or cyclic supports and also for A empty. The algorithm needs only an attack incidence-list topological sort, a head-indexed attack-rule scan, and a scan of the original support rules; no support closure search is needed. A violated rule supplies the claimed witness in the stated linear bound. Independent diagnostics: `python -B /workspace/branches/replay_records_1_3_4_5.py`, section 4, checked direct closed-attacker semantics against the unique attack-only kernel in 131215 bounded cases (empty support family counted in both regimes); the proof is not inferred from this computation.

## originality

PASS

The semantics, closure characterization of defense, support-free kernel, and possibility of nonexistence are established background. No compared source covers the single support-closure criterion for all three classical semantics when only attack dependencies are acyclic and support rules can be arbitrary. The proof depends on a stronger induction (also propagating defeated predecessors), not on restricting all dependencies or switching to a modified defense semantics.

## value

PASS

A natural tractable fragment of collective argumentation is characterized by a condition on attacks alone; supports may still be cyclic. The single linear-time existence test and explicit failure witness replace general closed-attacker/extension searches and isolate the obstruction to complete and grounded existence. The preferred counterexample prevents an overgeneralization to all semantics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
