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

The unit ball is the symmetric edge polytope: normalized differences along arbitrary shortest paths are averages of unit-edge differences. The graph is connected, so these differences span the dimension-(2n-1) zero-sum space. In the polar modulo constants the tight-edge incidence rank is 2n minus the number of spanning tight components, counting isolated vertices. A polar vertex has a tight spanning tree, yielding integrality after normalization. A constant row would force every matching edge tight, then force the other clique constant, leaving disjoint matching edges. Hence each row takes exactly two consecutive values and the relative offset is -1, 0 or 1. The within-row tight graphs are connected; the rows need a tight matching edge. At offset zero the row words are nonconstant and distinct, and either outer offset has three allowed column types with both endpoints required. This yields (2^n-2)(2^n-3)+2(3^n-2^(n+1)+1). For n>=3 the only cliques of size n are the two rows; preserving their matching gives exactly the stated graph group. At offset zero its action with sign identifies the two pairs of occupation numbers independently. If both mismatch occupations are positive the match occupations are arbitrary; if exactly one mismatch is positive both match occupations must be positive. At outer offsets the joint action identifies the offsets and exchanges the two positive endpoint occupations. For G(z)=z^2/((1-z)(1-z^2)), the three orbit contributions have generating functions G(z)/((1-z)(1-z^2)), zG(z)/(1-z), and G(z)/(1-z). Their sum gives the claimed rational function; extracting even and odd coefficients yields the two given cubics and the leading n^3/24. The coefficient at n=2 is only an extension. Separate rooted-potential connectivity and group enumeration (independent_enum.py) matched facets for n=3 through 7 and orbits for n=3 through 5; the frozen verify.py was inspected, not executed. Neither finite enumeration covers all n or any larger group of isometries.

## originality

PASS

The tight-edge potential criterion and the Hamming metric interpretation are established. The checked general and nearby exact enumerations do not provide the all-n facet and orbit formulas for two matched cliques or their occupation-number classification. The scoped group, graph, metric, and polarity are essential to the comparison.

## value

PASS

The two-row rook graph is a natural family of Hamming transportation metrics. The structural classification gives exact facet data in arbitrary dimension for that family, plus canonical descriptions up to the specified symmetries. The contrast between exponentially many facets and cubically many orbit types is a consequence of the explicit classification, not a numerically observed pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
