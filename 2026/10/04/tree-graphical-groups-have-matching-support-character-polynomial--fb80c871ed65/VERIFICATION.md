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

For any weighted forest with nonzero edge weights over any field, leaf v adjacent to u yields a nonzero 2x2 alternating block via congruence, leaving F minus {u,v}; rank therefore recurses by +2. A maximum matching can be chosen using uv, so nu(F) recurses by +1; rank=2nu(F) follows independently of weight values and char. Support S occurs in exactly (q-1)^|S| edge labels. For odd q the O'Brien–Voll orbit/character degree conversion gives ch(T,i;q)=q^(n-2i)[z^i] sum_S(q-1)^|S|z^nu(S). Root DP state mu-mu0 in {0,1} correctly yields P0=prod(P0_child+q P1_child) and P1=z(q^k prod(P0_child+P1_child)-P0). The tree DP and rank lemma constitute all-size proofs; packaged finite q=3,5 example code is only regression evidence.

## originality

PASS

Rossmann explicitly formulates polynomial character-enumeration for graphical groups and records path/complete/edgeless cases; Section 7 on trees concerns conjugacy classes, not this full tree character-degree distribution. General orbit formula alone leaves alternating rank strata unevaluated. The forest-specific support-matching polynomial with rooted recursion is not provided by inspected primary results or nearby Resultary coning/cycle results.

## value

PASS

Graphical groups are a natural open-ended enumerative family posed explicitly by Rossmann. The support-matching identity solves all trees, beyond paths, and the local two-state recurrence computes every character multiplicity without enumerating q^(n-1) edge labels. This is an extensible structural and algorithmic answer to an explicit question, not a tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
