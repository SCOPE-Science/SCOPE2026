---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For v in blade B_i the closed neighborhood is {c} union B_i, so signed dominance is exactly e+S_i>=1; for e=+1 this yields S_i>=0, and for e=-1 S_i>=2. Center inequality is automatic for r>=2. Independent binomial choices per blade give the two-term weight polynomial, with Q_1=0 as a correct boundary case; minima are 1+o in + branch and -1+2r+o in - branch, with latter strictly larger if feasible. Independently brute-forced original vertexwise neighborhood sums for 35 heterogeneous size tuples comprising 4856 sign labelings; all exact coefficient maps and minimum counts match.

## originality

PASS

Dutch-windmill forcing and scalar minimum results were published for homogeneous size-two blades; this special case is explicitly not claimed new. The reviewed 2020 Mycielski result concerns signed domination on a different enlarged graph, not the original heterogeneous windmill. Signed Roman/minus domination on complete multipartite graphs is a different invariant and graph class. Full heterogeneous all-weight signed-domination generating polynomials and optimal-labeling counts were not found in relevant Resultary and literature, with a material access risk for the 2007 full text.

## value

PASS

An entire exact weight enumerator and full minimum-family description for arbitrary unequal clique sizes constitutes a natural, reusable signed-domination invariant of a graph family whose homogeneous special case was already studied. It answers more than minimum weight: counts all feasible signed labelings by weight, displays parity dependence and central-label rigidity, potentially usable for signed forcing/extremal questions. The proof is elementary but the complete heterogeneous all-weight invariant, not a renaming of the known homogeneous scalar, is the motivated result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
