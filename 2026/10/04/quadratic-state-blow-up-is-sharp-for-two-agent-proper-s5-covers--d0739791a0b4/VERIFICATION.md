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

The lower-bound proof is symbolic.

For each agent \(i\), bounded-morphism back onto a universal target relation implies that every \(S_i\)-equivalence class maps onto all \(m\) target worlds. Therefore every source class has at least \(m\) states.

In a proper two-agent S5 frame, every \(S_1\)-class and \(S_2\)-class intersect in at most one point. Hence one \(S_1\)-class of size at least \(m\) meets at least \(m\) distinct \(S_2\)-classes, each of size at least \(m\), forcing at least \(m^2\) source states.

The bundled `verify.py` reconstructs the matching Bjorndahl--Sink cover for
\[
1\le m\le20.
\]
It verifies both equivalence relations, properness, surjectivity, and both bounded-morphism clauses for first-coordinate projection.

The script also checks that each source equivalence class has exactly \(m\) points and maps bijectively to the target, so the construction attains the lower bound with equality.

The script prints `VERIFY_OK`.

## Limits

The computation corroborates the equality construction. The arbitrary-\(m\) lower bound is not inferred from finite enumeration; it follows from the class-size and properness argument. The theorem does not cover non-S5 source frames or higher-agent minimum-cover problems.
