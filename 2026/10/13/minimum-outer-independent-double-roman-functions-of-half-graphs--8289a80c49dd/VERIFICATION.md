---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Definitions: label 0 needs neighboring 3 or two distinct 2s; label 1 needs neighbor 2 or 3; zero set independent. Thus D={f>0} vertex cover; n disjoint diagonal matching edges give |D|>=n. Weight decomposes |D|+e, e=|V2|+2|V3|. Zeros on both sides require excess >=2 in each side (hence e>=4). All zeros on one side yield e>=n if |D|=n; if |D|=n+1 they force e>=3, and if |D|>=n+2 e>=2 (n>=4), giving lower bound n+4. At equality support size n corresponds to complement of maximal independent staircases S_t={b_1..b_t}∪{a_{t+1}..a_n}; leaves b1 and an when zero force labels 3 at a1 and bn, giving n−1 interior F_t. Support n+1 forces exactly endpoint choices F0/Fn; support n+2 cannot achieve equality. Source lists complete finite exception H2 four minima and H3 eight. Independent full 4^(2n) label enumeration n=2..5 confirmed exact weights/counts (5,4),(7,8),(8,5),(9,6). Analytic proof supplies arbitrary n; minor indexed tuple notation was decoded correctly.

## originality

PASS

Best-of-knowledge PASS for complete half-graph OIDR function classification and optimizer multiplicity; known general bounds and complete-bipartite n+4 branch neither include sparse nested half graphs nor determine every optimal labelling.

## value

PASS

Half graphs are a standard chain/Ferrers graph test family with nested neighborhoods; exact OIDR domination and all optimum function counts are natural combinatorial invariants. The leaf-forced n+1 staircase classification for all n>=4 and exceptional H2/H3 minima provide a nontrivial full structural and finite-boundary result beyond coincidentally matching K_nn scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
