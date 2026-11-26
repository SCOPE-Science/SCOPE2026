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

A full map with increments 0 or 1 has contiguous image. Idempotence forces that image to be fixed; monotonicity forces clipping outside it. Two intersecting clips compose to the clip on the intersection, while disjoint clips compose in opposite orders to different constants. The singleton interval in a point-star forces maximality, and every commuting family has nonempty intersection. For a particular product interval [u,v] with k=v−u+1, the left and right endpoint choices are independent because u≤v. The separate maximum/minimum constraints give Δ_m(u)Δ_m(n−v+1); each commuting tuple has exactly one product interval. Summing first over endpoints and then ranks gives t^k[A_m(t)/(1−t)^m]² for a fixed rank and zt/(1−zt) as the rank-summing factor. With z=1, A_m(1)=m! gives C_n=(m!)² n^(2m)/(2m)!+O_m(n^(2m−1)) and the probability follows from |E_n|=n(n+1)/2. Since the counts depend only on n−k, summing ranks k≥r is exactly C_(n−r+1), giving the repaired conditional tail ratio and the limit (1−x)^(2m) at 0<x<1. Normalization and empty endpoints then give the stated Beta law, also for m=1; n=1 gives one tuple for every m. The asymptotic fixes m. Independently enumerated sorted maps with adjacent increment ≤1, tested idempotence and literal composition, and matched every product rank in 20 configurations (67,028 tuples). The original script was read, not executed; it has a larger finite grid and also tests the structural lemmas.

## originality

PASS

The repaired contribution is the product-rank enumeration for ordered tuples of every arity in this exact contraction class, and its exact conditional-rank distribution; the interval normal form, commuting-clamp test, point-stars, known pair totals, and standard Beta spacing distribution are not separate novelty claims. The closest broader product-rank series counts pairs in the larger unrestricted monotone monoid, without tracking the statistic that singles out contractions.

## value

PASS

The count records the size of the shared fixed image, not just whether two maps commute. It solves that exact finite distribution for every tuple length in a natural finite-chain monoid, separates the common-product statistic from the known centralizer law, and determines the conditional probability of retaining any desired image fraction. Utility rests on the whole finite rank distribution, not on the already known pair totals or the standard Beta family alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
