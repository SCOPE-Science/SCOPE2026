---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The event complement is the product of two independent site failures 1-r(1-t^m)(1-t^f) and 1-r(1-t^(n-m))(1-t^(n-f)). At fixed m+f, strict convexity of t^x (0<t<1) uniquely favors |m-f|≤1 simultaneously at both habitats. Any odd habitat total gives failure L_odd=(1-r sqrt(ab))(1-r sqrt(cd)) with L_odd>sqrt(L_j L_(j+1))≥min(L_j,L_(j+1)), since (1-r sqrt(uv))²−(1-ru)(1-rv)=r(sqrt u−sqrt v)². Thus all optima are paired (m=f=j). For paired allocations, failure F(t^j)F(t^(n-j)) is a strict concave quadratic in S=t^j+t^(n-j) for 0<r<1; global minima on discrete monotonic S_j occur only at j=0 or floor(n/2). At r=1 the failure is strictly decreasing in S and concentration wins. Sign Δ_n=r(a+b-c-rab) gives exact comparison and ties; for n=2k the reduced quadratic bracket has one root z*(r) in (0,1), p*=1-z*^(1/k) and p*~-log(z*)/k. Exact independent Fraction checks across n=1..8 and nine (p,r) pairs confirmed extremizers. Excludes p=0,1/r=0 extra ties; viability is one-step survivor mate feasibility, not demographic persistence.

## originality

PASS

Grevstad (1999; later 2011 analysis) formulates an aggregation-versus-release-number tradeoff under stochastic environmental and Allee effects, but not this exact two-site independent Bernoulli suitability/sex-count one-step optimization. Jerde–Bampfylde–Lewis (2009) studies hierarchical sexual-establishment probability, fertilization and later dynamics rather than complete two-site known-sex allocation. Their abstract was read, but full paper could not be retrieved (author-hosted PDF 403, institutional access disconnected). The inaccessible plausible source is explicitly a risk, not a reason to assert noncoverage. No stronger inspected theorem implies the exact all-or-nearly-even global optimality or threshold; best-of-knowledge PASS.

## value

PASS

The model captures a real competing mathematical mechanism: same-site two-sex survival favors co-location while independent site suitability rewards redundancy. A proof that all uneven partitions lose and a unique sharp even-budget transition gives a complete and reusable finite optimization classification; practical field efficacy is not asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
