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

The crucial quantifiers were checked, including the empty simplex and cones. If K fails r-conicity, a subcomplex A on <=r vertices lies in no closed star; for every v some face sigma in A cannot be extended by v, so its vertex set is totally dominating. Conversely for a dominating S of size <=r, faces sigma_v witnessing each vertex generate a subcomplex A on <=r vertices contained in no star. Thus K r-conic iff gamma(K)>r, for all integers r>=-1. K is cone iff no totally dominating set exists, proving infinity case. For disjoint joins, a witness face alpha union beta for v in K fails join membership iff alpha union {v} fails in K, since beta is a valid L face; hence total domination holds exactly when both component sets totally dominate. Minimize cardinalities, covering cone/infinity cases. The provided verify.py correctly enumerates all 126 small nonempty labeled complexes and 144 joins, which corroborate but do not prove the general theorem.

## originality

PASS

Aharoni–Berger (2006) states simplicial total domination via non-extendable faces; Barmak (2021) separately defines r-conicity through closed stars and proves only a lower join bound. The full texts checked provide the two ingredients separately, but not their identity or exact join additivity of maximal conicity; Farber appendix likewise restates conicity without the dual parameter. This is a short derivation once definitions are juxtaposed; novelty is bounded to the explicit cross-parameter formula and joins, not new connectivity bounds.

## value

PASS

This is an exact dictionary between independently used topology and combinatorial domination invariants. Its nontrivial mathematical purpose is to transfer conicity estimates to an existing total-domination parameter and upgrade Barmak's general one-sided join estimate to an equality for the maximal conicity index, including cones. Although the proof is short, the universal join structure and reusable equivalence are motivated, not an arbitrary renamed finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
