---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Split disjunction entailment sufficiency follows directly from a perfect matching of individual FD implications. Necessity uses Hall obstruction for a 2x2 bipartite graph. If one source implies no target, an F3 pair-coordinate grid team satisfying that source has each target maximum FD-subteam size <=|T|/3. Otherwise both sources only imply the same target: disjoint tagged grids give target maxima <=|T|/2 and <=|T|/3, so no two-target cover exists. This handles nontrivial FD consequents outside determinants including empty determinants. Independent exact density calculations validated 97 sampled nonmatching cases on three attributes. Infinite-domain equivalence follows from the general finite witness construction, not the random tests.

## originality

PASS

Best-of-knowledge noncovering after explicit comparison to the strongest identified literature and indexed records, with residual priority risks retained.

## value

PASS

A complete natural single-premise fragment of the previously posed disjunctive functional-dependency implication problem admits a surprisingly simple polynomial matching criterion. The Hall obstruction is converted into finite counterteams with quantitative density margins, a nonroutine logical structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
