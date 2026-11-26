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

On the orthogonal complement of constants the unfailed spectral bottom is 2, and the surviving Laplacian is positive definite because cube edge connectivity is d≥3. Conjugating the downdate by (L−sI)^(-1/2) shows that it is positive definite exactly while the top eigenvalue of the two-incidence-vector resolvent K(s) is below 1. K increases strictly and its top eigenvalue diverges at 2 from the first Walsh level; this identifies the first and smallest surviving positive eigenvalue. Tensoring the one-bit kernel gives the common diagonal A. Parallel edges differing in k base bits have cross integrand 2 exp(−(2−s)t)a^(d−1−k)b^k, with strict maximum at k=1. For different directions each active coordinate contributes one signed exp(−2t) factor, so the absolute cross term is bounded by V with all other factors chosen diagonal. At the unit level ρ of F=A+P, substitution u=exp(−2t) gives the normalized density u^(α−1)((1+u)/2)^k, k=d−2, α=1−ρ/2. Under it P−V=(1−2E[u])/2. Integration by parts gives E[u]<2(1−α)/k<1/2 for k≥4. The d=3,4,5 direct rational checks give respectively (F,P−V)=(20/21,2/231),(14/15,1/35),(2980/3289,7230/141427), at s=1/2,1,7/5. These were recomputed independently by evaluating M_i=2^(−k)∑_j binom(k,j)/(α+j+i) for i=0,1 using exact fractions, then taking (M_0,(M_0−2M_1)/2). The normalized mean decreases as s increases, because its derivative is −Cov(u,log u)/2, so the strict comparison holds at the larger unit-level s. Thus every nonsquare pair crosses later. Counting both opposite-side choices in each square gives d(d−1)2^(d−2). Expanding F gives the claimed equation and ρ_3; F decreases strictly with d and the terms of index j≥1 at the root sum to O(1/d) by the binomial-integral bound. This proves monotonicity and the stated asymptotic without relying on the supplied finite tests.

## originality

PASS

The inspected works give context on consensus rates, cut robustness or different spectral and resistance objectives, but not the strict worst-pair orbit for the unit-weight combinatorial gap, its root equation and dimension dependence. The most directly titled adjacency-radius source was not accessible in full; the verdict does not treat that access failure as evidence of noncoverage.

## value

PASS

The binary cube and its consensus rate give a natural fault experiment, and the comparison identifies the worst geometry rather than just proving that two failures leave a connected graph. The strict orbit separation, exact minimum and dimension law together provide a benchmark for resilience analysis in a canonical network, including a counterpoint to adjacency-based intuitions from other two-failure objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
