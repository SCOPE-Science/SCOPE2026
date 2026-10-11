---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Prime-exponent vectors turn multiplicative dependence into exact rational linear dependence. Primitive Pluecker coordinates classify the rational two-plane spanned by each independent pair, so a maximal-rank dependent unordered triple is exactly a triangle whose three pair-edges share one plane key. A fresh independent exact replay over all \(2\le a<b<c\le1215\) found \(15\) consecutive triples, \(13\) with maximum at most \(1000\), and exactly the two claimed new triples at \(1215\). The displayed multiplicative identities verify both boundary witnesses and their translates. Maximal rank forces distinct coordinates, so six permutations convert the unordered counts to \(78\) and \(90\).

## originality

PASS

Vukusic--Ziegler's full paper reports exactly \(13\) unordered examples through \(1000\). Shparlinski--Sleiman's complete ten-page preprint defines the same ordered maximal-rank function, records \(M(1000)=78\), proves only an asymptotic upper bound, and explicitly states that even \(M(H)\to\infty\) is unknown. The Benelux pair \((75,1215)\) was already known, so the individual witness coordinates are not wholly new; the surviving claim is the exhaustive first-jump boundary, including exclusion of every competing triple through \(1214\). Resultary searches found no prior post-1000 census.

## value

PASS

The source literature explicitly leaves the growth and occurrence of consecutive maximal-rank triples open. The first jump beyond the standard published census is a natural exact finite invariant, and proving that boundary requires an exhaustive rank-exact search with no relation-exponent cutoff. The result supplies a concrete benchmark for the new asymptotic counting theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
