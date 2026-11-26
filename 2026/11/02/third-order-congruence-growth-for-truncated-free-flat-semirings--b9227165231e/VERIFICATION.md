---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Flat addition forces any class with two distinct words to merge into the zero class; multiplicative ideals containing zero give the converse, with their nonzero parts exactly the contiguous-factor upsets. For F of size m at length k-1, each length-k word is forced iff its prefix or suffix of length k-1 is in F: this covers also any word forced by a chosen shorter factor. Thus the forced count is the union of incoming and outgoing arcs, 2nm-e(F). No shorter word can be in an ideal with m<=2 for k>=3, since its length-(k-2) extension has at least 2n-1 distinct one-letter extensions (left/right sets intersect in at most one). Singletons get a factor 2 on exactly the n constant vertices. For two vertices, there is at most one arc per ordered pair. Two distinct constants cannot be adjacent, and a nonconstant neighbor of a constant has exactly one incidence direction because k-1>=2. Among nonconstant vertices two arcs require a reciprocal pair, forcing alternating distinct letters and giving one pair per unordered alphabet pair. Thus the two-arc counts are binom(n,2), 2n(n-1), and binom(n,2) in the three disjoint classes. Total arc incidence summed over unordered pairs is 2n(N-1), so 2^e=1+e+binom(e,2) gives Q_k exactly. Every admissible shorter word must be a factor of some member of F and each vertex has at most c_k proper nonempty factors, hence w(F)<=2^(c_k m). Using e(F)<=min(m^2,nm) yields O_k(N^3 2^-6n) for m=3 and O_k(N^4 2^-8n) for m=4, then a geometric tail with ratio N 2^(c_k-3n/2) for 5<=m<=n/2 and one with ratio N 2^(c_k-n) for m>n/2. Both tails are absorbed for fixed k. At k=2, m letters in the ideal leave (n-m)^2 independent top words, giving the exact sum and the same tail argument with N=n,c_k=0,e(F)=m^2. The probability statement follows by dividing the positive nonempty-lower-layer contribution by the total. A distinct top-down enumeration of uncollapsed factor-closed sets reproduced counts 21, 567, 390 and 130315 for (n,k)=(2,2),(3,2),(2,3),(2,4).

## originality

PASS

The congruence–ideal correspondence and the family itself are established, and the k=2 relation count is an elementary consequence. The distinct contribution is the exact de Bruijn-layer count and resulting second overlap coefficient with fixed-k remainder for k>=3. The strongest accessible flat-semiring, free-semigroup-growth and finite-poset enumeration sources inspected do not give that bounded-factor result or a theorem that fixes its coefficient without the graph-specific comparisons.

## value

PASS

The truncation family is natural in flat-semiring theory. The first nontrivial correction beyond independently selecting maximal words detects interactions between collapsed words. The exact coefficient classifies those interactions by loop, incidence and period-two behavior, and the remainder shows that more complicated zero classes do not contribute at that scale for any fixed truncation. This is an informative enumeration of the congruence structure, not only a table of small totals or the elementary k=2 sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
