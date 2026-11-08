---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

A vertex of T_n=L(K_n) is an edge uv of K_n. Its induced degree for selected base edges H is deg_H(u)+deg_H(v)-2, so the dissociation condition forces all components to be isolated vertices, K2s, or P3s (a degree-2 vertex cannot meet another degree-2 vertex). Exactly maximal selections either cover [n] by K2/P3 or have one isolated base vertex and all remaining P3. Exponential labeled-block enumeration yields D EGF exp(x+zx^2/2+z^2x^3/2) and M EGF exp(zx^2/2+z^2x^3/2)+x exp(z^2x^3/2). The support of M is every degree ceil(n/2)..floor(2n/3) and singleton exactly n=2,3,4,5,7. Strict log-concavity follows from decreasing adjacent full-partition coefficient ratios; the n=3q+1 corrected last ratio remains smaller than its predecessor for q>=5, while q<=4 has at most two coefficients. Independently checked each graph subset at n2..6 by original adjacency/maximality definitions; examined supplied verifier for larger-n size-truncated enumeration and distinguished finite corroboration from proof.

## originality

PASS

Best-of-knowledge originality after direct claim/implication comparison with published same-object and general methods. Known ingredients, exact overlaps, and inaccessible/plausible priority alternatives are explicitly retained; unsuccessful search alone is not novelty proof.

## value

PASS

This establishes two complete exact labeled enumerators and the entire inclusion-maximal size spectrum for the natural triangular/Johnson( n,2) graph family. An explicit exceptional one-unused-vertex class, strict coefficient log-concavity, and the isolated n7 well-covered case are useful combinatorial facts beyond the known scalar dissociation maximum; the exponential formula is elementary but the classification is not merely a substitution into a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
