---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Verified the finite K_(r+1)-free extension/type correspondence using Henson Theorem 2.3 and Conant Section 3. A unary neighborhood is valid iff it misses a part. For adjacent x,y a forbidden common K_(r-1) occurs precisely for the unique part i missed by both and common neighbors in all other parts, giving the disjoint B correction. Factoring U=2^N s(1+O_r(s)) and B=4^N sum p_i^2(1+O_r((3/4)^min n)) gives uniform collision asymptotic. Cauchy-Schwarz and discreteness of powers 2^{-n_i} give balanced equality. Fresh independent finite checks used 63 r=2..4 size vectors N<=7; not an infinite proof.

## originality

PASS

Best-of-knowledge after statement-level comparison: Equivalent forms are finite labeled K_(r+1)-free two-vertex extension diagrams and common (r-1)-clique obstructions; Henson/Conant ensure realization but neither states the product correction or sharp r-parametric collision law. The universal finite K_(r+1)-free graph extension property is broader in permissible parameter graphs, but establishes realizability rather than enumeration. A prior exact one-type counting result determines U, not the adjacent two-type correction B.

## value

PASS

Maximal complete multipartite parameter graphs sit at the natural clique-forbidden boundary. The result supplies the full orientation-refined ordered two-type spectrum and isolates the unique common-clique obstruction; its uniform collision law explains how relative part sizes control adjacency even when absolute sizes diverge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
