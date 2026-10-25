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

The structural proof in `RESULT.md` establishes, by topological induction on the attack-dependency digraph, uniqueness of any complete or stable extension, then proves support-closure is necessary and sufficient. No finite experiment is used to justify a universal quantifier.

`checker.py` uses direct subset enumeration and independently evaluates closed attackers, so it does not reuse the proof's candidate evaluation for its semantic oracle. Run `python3 checker.py`. A successful run prints `ALL_CHECKS_OK 34455` (34,455 diagnostic assertions or case-pair comparisons as counted by the script). Fixed-order exhaustive tests reach three arguments; seeded randomly sampled collective-rule tests cover two through six arguments, including empty support bodies. The two boundary examples are explicitly tested.

The checks do not exhaust all large frameworks or establish originality. They do not claim independent mathematical audit. Primary literature comparisons are reported in `REVIEW.md` and `AUDIT.json`. The result requires an acyclic attack-dependency digraph, nonempty attack tails and explicitly listed rule bodies.
