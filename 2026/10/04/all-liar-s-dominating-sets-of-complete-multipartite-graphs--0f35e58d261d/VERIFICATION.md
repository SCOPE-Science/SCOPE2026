---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Direct neighborhood reconstruction gives \(N[v]=(V\setminus V_i)\cup\{v\}\). Different-part pairs force only \(s\ge3\); same-part pairs reduce to outside-part counts \(q_i\ge3,2,1\) according to two/one/zero omitted vertices. When \(n_i<s\) these inequalities are automatic, while when \(n_i\ge s\) they are equivalent to \(s_i\le s-3\). The generating function and minimum criterion are then exact bounded-composition counting. An independent exhaustive check over all ordered part profiles of total order 3 through 8 and all 43,176 vertex subsets matched the criterion exactly.

## originality

PASS

Fresh comparison found substantial partial prior coverage: Canoy–Balandra's join theorem already classifies liar-dominating sets whenever a complete multipartite graph is expressed as a join of two nontrivial connected factors. It does not, under its stated hypotheses, cover all arbitrary part profiles (notably general tripartite decompositions), nor does it state the unified capacity enumerator and minimum-set count. Resultary found no earlier theorem completing those remaining cases. Best-of-knowledge originality therefore survives, but only for the genuinely uncovered arbitrary-part/unified-enumerator content.

## value

PASS

Despite partial prior join coverage, the surviving content is a compact all-part-size classification and exact enumerator that includes cases not covered by the connected-factor join theorem and upgrades scalar information to all feasible sets. This is a natural structural refinement of an established fault-tolerant domination invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
