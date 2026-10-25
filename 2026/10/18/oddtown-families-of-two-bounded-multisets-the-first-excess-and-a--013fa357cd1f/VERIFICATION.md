---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The domain is 0,1,2 multiplicities; parity is of total coordinate sum and pairwise multiset intersection sum min(x_i,y_i), excluding diagonal pairs. Initial-segment embedding Φ(x) subset [n]x[2] preserves sums and pairwise min-intersections and gives F_2-orthogonal odd self-pair vectors, hence universal upper O2(n)<=2n, not n. Independent direct graph enumeration over all odd vectors (3^n-1)/2 with every increasing clique visited exactly once recomputed counts: n1 [1,1,0], n2 [1,4,2,0], n3 [1,13,30,14,0], n4 [1,40,332,744,450,72,8,0], n5 [1,121,3300,27020,73200,68874,24640,3040,0], proving exact maxima (1,2,3,6,7) with the forbidden next-size zero. The displayed 10 six-coordinate odd words have all 45 min-intersections even; disjoint-support union gives 10q+r when n=6q+r, so liminf O2(n)/n >=5/3. Independently checked enumerator and source verify.py predicate agree; finite n<=5 count is exhaustively proved, not extrapolated.

## originality

PASS

Best-of-knowledge contribution is odd-self-cardinality bounded-multiset case (minimum intersections), exact first cutoff n<=5, and 10-word six-coordinate block, not Oddtown linear independence or Eventown. Closely matching multiset Eventown paper was read in full and self-parity is opposite, so it does not imply this odd-member family result.

## value

PASS

Multiplicities two are the first natural relaxation of classical odd-cardinality set systems. The first failure of old n-bound occurs at the meaningful smallest dimension four, and a verified reusable six-coordinate family guarantees asymptotic linear growth at least 5n/3 while the known universal 2n upper remains separated. The exact initial profile and amplifier are natural combinatorial extremal facts even without a complete n>=6 census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
