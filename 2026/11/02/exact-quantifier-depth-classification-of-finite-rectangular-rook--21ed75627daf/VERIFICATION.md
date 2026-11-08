---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The actual RESULT.md identifies alpha(R_mn)=m and omega(R_mn)=n, so existential independent/clique tests I_k,C_k of quantifier rank k<=q prove necessity. For sufficiency Duplicator preserves separately the equality pattern of chosen row coordinates and column coordinates, choosing previously paired values on repetitions or fresh ones otherwise. In at most q moves, both sides with size >=q never exhaust fresh values, while any smaller side is equal to its match; the induced selected-vertex map preserves equality and adjacency. This is an unrestricted q-round EF proof, not a finite-test extrapolation. The class predicates use I_a,C_b and negated I_(a+1),C_(b+1) only when truncations are <q. This yields exactly binomial(q,2) classes, sharp q^2 minimum representative for class (q,q), and minimal distinguishing rank. Independent explicit clique/independent enumeration confirmed small m,n<=4.

## originality

PASS

A complete exact bounded-quantifier-depth classification of the graph-reduct rectangular rook family was not identified in inspected graph-definability and homogeneity sources. The proof uses standard EF games, but the exact two-threshold normal form and sharp rank/cutoff are family-specific conclusions not automatically provided by the general EF theorem.

## value

PASS

The family K_m square K_n is a canonical line graph of K_{m,n}. The result exactly classifies how finite first-order logic loses size information, supplies optimal distinguishing quantifier rank, and constructs optimal bounded-depth representatives. This is a natural full classification with reusable model-theoretic invariants, not an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
