---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each prime p and integer alpha≥1, the digit-borrow matrix T_d(U,V)=((d+1)U+dV,z((p-1-d)U+(p-d)V)) mod z^alpha represents counts of k≤n with p-adic binomial valuation <alpha via Kummer. State space Q[z]/z^alpha ⊕ zQ[z]/z^alpha has dimension 2alpha−1, giving upper kernel-rank bound. The prefixes 0^r yield state differences (0,(p−1)p^{r−1}z^r), 1≤r<alpha, then a p−1 digit maps (0,z^r) to ((p−1)z^r,z^{r+1}), spanning each first-component monomial. Observability: repeated p−1 digit suffixes have y_h−p y_{h−1}=(p−1)sum_{j=1}^{alpha−h}V_j; these nested sums kill V coefficients. Prefixing one zero then p−1 suffixes yields nested sums of U_j, and U(1)=0 removes the last coefficient. Thus every state is reachable, none nonzero is unobservable; rank equals 2alpha−1 and is the minimal rational linear representation dimension, including alpha=1. Fresh independent exact binomial coefficient counts and rational kernel-rank minors for p=2,3 and alpha=1,2,3 matched 1,3,5; finite samples not used to establish universal algebraic minimality.

## originality

PASS

Best-of-knowledge original scientific contribution confined to the exact theorem beyond explicitly acknowledged prior partial coverage. Meaningful searched aliases, broader-result implications, primary source materials, and access limits are documented below.

## value

PASS

This is a natural exact state-complexity invariant for prime-power divisibility statistics in Pascal rows, and explicitly resolves the rank 2alpha−1 question formulated by Rowland in 2010. The reachability/observability lower bound is not furnished by the previously known polynomial transfer and is mathematically nontrivial and reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
