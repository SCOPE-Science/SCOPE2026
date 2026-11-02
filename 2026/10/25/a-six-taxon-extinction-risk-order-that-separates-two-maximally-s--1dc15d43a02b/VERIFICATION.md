---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every nonroot internal clade v, extinction loss of its incoming unit edge occurs with probability q^{s(v)} independently and θq+(1−θ)q^{s(v)} in the common-shock mixture; the n leaves contribute no excess, yielding Δ_T=θ[(n−2)q−Σ_nonrootinternal q^{s(v)}]. Six-leaf unlabeled root splits 1+5,2+4,3+3 enumerate 3+2+1=6 shapes with nonroot clade-size multisets {2,3,4,5}, {2,2,4,5}, {2,2,3,5}, {2,2,3,4}, {2,2,3,3}, {2,2,2,4}. Adjacent polynomial gaps are q²(1−q), q³(1−q), q⁴(1−q), q³(1−q), q²(1−q)², strictly positive; hence the Δ order. E/F both have depths 2,2,3,3,3,3, and their local F gap is q²(1−q)²; all ancestor clade sizes stay constant under a depth-preserving graft. For 4 and 5 tips the stated most balanced root splits are strict optimizers. Separate independent exact small-shape enumeration checked all six clade vectors/depths and symbolic gaps. The universal result follows from factorization and linearity, not finitely sampled probabilities.

## originality

PASS

Previously established correlated-extinction mean loss (Faller–Steel) and the two six-tip Sackin minimizers (Fischer) are acknowledged; their mathematical results do not alone compare the six precise catastrophe-mixture clade polynomials or establish the E-to-F globally depth-preserving graft. The contribution is the strict, all-q six-shape loss order and local improvement; novelty is best-of-knowledge, not an exhaustive priority guarantee.

## value

PASS

Phylogenetic diversity loss and Sackin depth balance are natural ecology/tree-shape invariants. The explicit strict separation of equal-depth minimum-Sackin trees proves that balancing alone does not determine catastrophe excess loss; the graft extends a six-tip witness to arbitrary tree size without changing any leaf-depth vector. This is a motivated structural counterexample rather than an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
