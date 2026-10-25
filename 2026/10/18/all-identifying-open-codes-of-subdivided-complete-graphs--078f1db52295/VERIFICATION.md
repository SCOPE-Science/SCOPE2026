---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For every n>=3, actual S(K_n) bipartition signatures separate into incident selected edges at each original vertex and selected original endpoints at each subdivision vertex. The latter are distinct nonempty exactly when at most one original vertex is omitted. The former are distinct nonempty exactly when the selected-edge graph has no K1 or isolated K2 component. This gives the iff classification. Labelled connected-component exponential formula removes sizes 1 and 2, producing P_n=(n z^(n-1)+z^n)A_n. If c components all have >=3 vertices, |F|>=n-c>=ceil(2n/3), with equality iff c=floor(n/3) and each component is a tree. Cayley labelled tree counts on size 3,4,5 component profiles yield all minimizers. Separate independent enumeration of actual open-code signatures gives (n,total,min,multiplicity)=(3,16,4,9),(4,190,6,64),(5,4368,8,625). Tests corroborate but do not prove the infinite n statement.

## originality

PASS

Best-of-knowledge statement-level comparison identifies no prior theorem implying the final claim at its actual hypotheses; known overlap and residual bibliographic risks are recorded, not erased.

## value

PASS

A natural infinite incidence-graph family receives the entire identifying-open-code size polynomial, an exact minimum and full forest/class multiplicity, beyond generic domination bounds. The structural signature reduction and complete enumerator are useful precise invariants, not isolated tiny cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
