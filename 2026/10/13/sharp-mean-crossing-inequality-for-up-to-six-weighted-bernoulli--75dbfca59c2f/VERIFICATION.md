---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With q=1-p and a weight w_i>=p, success of coordinate i suffices. If w_i<=1-p, failure of i and success of all other positive-weight coordinates also wins and is disjoint and positive; if w_i>1-p, i is necessary too. Otherwise pad to six coordinates, all <p, forcing p>1/6. Complements show that all sets of size at least four win, that all pairs win for p<=1/5, and that all triples win for p<=1/4. In the intermediate range two disjoint losing pairs are impossible (total mass strictly below 4p<=1); an intersecting edge family on six vertices has at most five edges, so at least ten pairs win. In the last range every perfect matching hits a winning edge (three losing pairs would have mass <3p<=1), yielding k>=5 since 15 matchings meet each edge three times. The complement of each losing triple is a winning-pair triangle since its total is >1-p>=2p and all weights are <p. The independent exact graph check exhausts 32768 graphs and gives t<=2k-8; extra edges above k=5 contribute a nonnegative difference bounded below by (k-5)p^2 q^3(1-3p). Exact Bernstein coefficients certify each of the three reduced probability bounds minus p strictly positive on the full closed subinterval, with minimum coefficients 4505/46656, 196/3125 and 21/4096 respectively. These are polynomial positivity certificates, not sampling. The argument handles endpoints, repeated or zero weights and the non-strict event; p=0 is a separate trivial case, not part of the equality criterion.

## originality

PASS

Pass for the sharp six-weight subfamily across the full continuous parameter range, including equality. The range is already the conjectured universal range, its endpoint p=1/3 is known for arbitrary length, and the explicit five-weight indexed overlap must be credited. The six-weight regime and its all-small-weight strictness are not covered by those results. A later or same-date index label alone decides neither priority nor overlap.

## value

PASS

This settles a natural finite-support subcase of an explicit probability conjecture through the full continuous p interval, not just a grid or the known isolated endpoint. The six-weight matching and triangle argument explains why the light-weight case is strictly above the lower bound and thereby gives a sharp equality locus for the whole subfamily.

The dated certificate retains the supplied scientific assessment, sources and limitations.
