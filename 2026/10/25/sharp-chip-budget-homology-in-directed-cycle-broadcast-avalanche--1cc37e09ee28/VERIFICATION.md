---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. At initial parallel firing the outdegree-k source distributes exactly one grain per disjoint directed cycle, never receives grains and never fires again. Induction gives exactly one grain at cycle index (t-1) mod n_i at every t>=1. Pairwise gcd(n_i,n_j)=g by coprime quotients; the generalized Chinese remainder theorem makes a tuple reachable iff all indices have common residue modulo g. Thus the exact complex is an isolated initial broadcaster plus g mutually vertex-disjoint joins D_{m1}*...*D_{mk}; their integral homotopy is wedges of prod(m_i-1) spheres of degree k-1 and reduced H0 rank g, free all higher groups. Every finite directed positive-outdegree configuration with k conserved grains fires at most k vertices at once, giving upper dimension k-1; the construction attains it for all k>=2. Independently simulated complete support periods for six parameter tuples and matched every CRT support. Top integral assertion relies on mathematical join decomposition rather than tested field ranks.

## originality

PASS

PASS qualified: Foundational Riihimäki–Smith avalanche homology work and closest published related SCOPE residue construction are genuine prior context, but their accessible statements do not imply the present broadcaster plus k independent cycles / CRT join family. Foundational full text was inaccessible this run; best-of-knowledge with specific risk, not a blanket noncoverage assertion.

## value

PASS

PASS. For the new avalanche homology of directed sandpiles, the complete exact homotopy type is a natural infinite arithmetic family. The model establishes the maximum achievable nonzero homological dimension for every positive chip budget and exposes gcd-controlled disconnected join topology, not simply a degree count on a fixed tiny graph. It does not classify general avalanches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
