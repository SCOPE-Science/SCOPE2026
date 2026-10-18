---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The actual Neunhäuserer recursion product MGF at n=3 yields, up to translation and p<->1-p, weighted iid Bernoulli sum B1+d1B2+d2B3 with positive integer d1,d2. Sorting weights to {1,u,v} (1<=u<=v), only equal-weight or largest=sum of other two subset-sum collisions occur, i.e. u=1, v=u, or v=u+1. These exhaust exactly five entropy expressions: 3h, 3h-3s log3, 3h-2s log2, (3-s)h, (3-s)h-2s log2, s=p(1-p). Independently built all eight subset configurations for 78 weight types 1<=u<=11,u<=v<=12 and four biases, all matched their predicted formula. Analytic strict curvature follows h=-1/s, s<=1/4, h<=log2, (2p-1)log((1-p)/p)<=0, and G<=-11+2log2 with G=(3-s)h. Thus all h3 strictly concave on (0,1), symmetric and unique maximum at 1/2. Numeric checks do not supply the infinite-weight proof; the collision argument does.

## originality

PASS

The full six-page Neunhäuserer arXiv:2609.05546v2 (Sept 22 2026) was read, including Proposition 2.2 product MGF, Conjecture 3.1, Proposition 3.1 proving only two extremal regimes, and empirical Section 4. Its n=3 partial-overlap case is not proven there, and the author explicitly says no general proof is known outside these regimes. The full relevant beginning of Li arXiv:2609.01529v2 was read: all weighted-sum theorems take independent Bernoulli(1/2), varying entropy order, not common bias p. Classical Shepp–Olkin covers unweighted sum, not arbitrary additive-collision three-weight patterns. No matching published general p 3-weight theorem found by targeted searches.

## value

PASS

The source posed a concrete entropy concavity conjecture; n=3 is the first possible genuinely partially overlapping stage. Proving all positive integer weight patterns uniformly and classifying exactly five collision geometries settles an intrinsically motivated open first layer, not just an arbitrary numerical example. The result can support work on recursive Bernoulli convolutions and biased weighted-sum entropies; the n>=4 conjecture remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
