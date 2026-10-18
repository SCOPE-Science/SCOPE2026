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

Graph-state character orthogonality gives entropy bits equal to F2 rank of crossing adjacency. For crossing subgraph of a path (forest), unique matching minor proves rank equals maximum matching size. Greedy path matching recurrence s_i=1[a_i≠a_{i+1}](1-s_{i-1}) is exact and yields four-state transfer w(z)T(z,t)^(n-1)1. Independent direct F2 Gaussian elimination on all 2^n cuts for n=4,6,8,10,12 agrees with transfer histogram and endpoints; n=12 gives (2,28,152,358,320,64). Analytically verified characteristic cubic λ[λ^3-(1+z)λ²+z(1-2t)λ+tz(z+1)] and logarithmic Hessian diag(1/4,2/27) at (1,1). Complement symmetry fixes half-population saddle, strict primitive Perron modulus separation away z=1 yields conditional quasi-powers with mean n/3+O(1), var 2n/27+O(1) and CLT. Perfect rank demands each disjoint matched pair cross, 2^m assignments; rank-one only two balanced step cuts when m>=2.

## originality

PASS

The 2006 Facchi–Florio–Pascazio paper covers the identical balanced cluster-state participation statistic, including n=12 histogram, so novelty does not attach to introducing or numerically measuring the observable. A full reading finds finite graphs but no exact all-length transfer/gap/CLT. Contiguous-cut circuit results of 2026 concern different sampling. The all-even-size exact law and Gaussian limit survive best-of-knowledge comparison.

## value

PASS

Exact all-size distribution, sharp exponentially rare maximum-rank balanced partitions, and extensive Gaussian typical entanglement address a motivated statistic already studied in published path-cluster physics, and distinguish disconnected balanced cuts from one-edge contiguous area-law cuts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
