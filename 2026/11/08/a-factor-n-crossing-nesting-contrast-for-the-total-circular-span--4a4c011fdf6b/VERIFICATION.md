---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The conditional-edge argument correctly separates crossing partners (d−1)(2n−d−1) from nesting partners binom(d−1,2)+(i−1)(2n−j), each divided by 2n−3. Summing over candidate edges of weight min(d−1,2n−d−1), with W=n(n−1)² and explicit U_X,U_N, gives the claimed exact covariances for every integer n≥2. Var(S) uses inclusion probabilities for disjoint and incident edges, while Var(X)=Var(N) follows from pair-count involution. Separate independent exact Fraction enumeration of all matchings for n=2,3,4,5 reproduced (Cov(S,X),Cov(S,N))=(4/9,−2/9),(6/5,−2/5),(96/35,−24/35),(1000/189,−200/189), verifying −n ratio; finite checks do not prove full n-range. The original verify.py and its 2≤n≤7 exhaustive and n≤200 weighted checks were inspected as additional reproducibility, not accepted only from logs.

## originality

PASS

The combined final claim explicitly credits crossing prior work and adds an exact non-implied nesting covariance plus the -n ratio and asymptotic correlated/uncorrelated split. It survives with the bounded weighted-enumerator priority risk. Strong prior coverage of positive crossing covariance and crossing correlation is acknowledged. It does not logically determine negative nesting-span covariance; the involution need not preserve span.

## value

PASS

The same marginal crossing and nesting counts interact radically differently with a natural length functional; an exact negative covariance and n-fold asymmetry quantify a previously hidden geometric dependence. Exact all-n covariance identity and asymptotic vanishing nesting correlation are useful for joint random-chord observables, not a cosmetic substitution of known crossing variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
