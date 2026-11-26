---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The connected graph's incidence vectors span the (q+1)-dimensional zero-sum hyperplane with its actual Euclidean metric. Under the cited Steiner normalization the zonotope wedge-sum formula gives the sum of Gram volumes of k-generator subsets. Cycles have dependent columns; forests have independent columns by leaf deletion. For each nontrivial tree on s vertices, deleting any one row from its oriented incidence matrix gives a determinant of absolute value one, by leaf elimination rooted at the omitted vertex. Cauchy–Binet gives Gram determinant s, and disjoint components multiply, with isolated vertices contributing one. If the hubs join, exactly one selected right vertex has both edges, since two such vertices form a cycle and none separates the hubs. The active right vertices number k-1; choosing them, the connector and the other attachments gives binom(q,k-1)(k-1)2^(k-2), each with Gram volume sqrt(k+1). If the hubs separate, k right vertices each select one edge; with j on the first hub, the two star sizes j+1 and k-j+1 give the D summand. This proves both formulas and k=0,1,q+1, and removing the weights gives uniform odds k(k-1)/(4(q-k+1)). For the weighted odds the separating average is H_k=E[sqrt((X+1)(k-X+1))] for X binomial(k,1/2). The weak law plus the bounded arithmetic-mean upper bound after division by k give H_k/k tending to 1/2. Thus weighted odds are asymptotic to k^(3/2)/(2(q-k+1)) along growing interior ranks. At k/q^(2/3) tending to finite positive t this is t^(3/2)/2, and odds conversion gives the claimed limit; below scale it tends to zero (including bounded-rank subsequences), and above scale it diverges since q-k+1<=q. The top rank has probability one. The exact unweighted ratio similarly gives its sqrt(q) scale and both outer limits. Independent replay `python3 /workspace/audit_recompute.py 3` reproduced the exact component-size radicand partition of 10383 forests through q=7 and compared 258 incidence Gram determinants by integer permutation expansion through q=4. These finite computations corroborate the formula but do not establish the infinite limits.

## originality

PASS

The distinct finding is the sharp rank-conditioned connectivity profile with Euclidean Gram-volume weights and the shift relative to the uniform fixed-rank benchmark. The universal wedge sum, spanning-tree top volume, and known component enumeration are not separately credited. The exact split exposes how the two classes are reweighted and supports the asymptotic result; the closest inspected statements do not supply that rank-dependent geometric comparison.

## value

PASS

The geometric effect is more than an exact decomposition of a known intrinsic volume: the square-root Gram weights shift the exponent of a natural connectivity event from 1/2 to 2/3 for the same graph family and fixed-rank conditioning. The limiting profiles quantify that shift and the exact split explains it by a single large component versus two roughly balanced stars. The conclusion is specific to the stated Euclidean weighting and K_{2,q}, not a proposed universal zonotope threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
