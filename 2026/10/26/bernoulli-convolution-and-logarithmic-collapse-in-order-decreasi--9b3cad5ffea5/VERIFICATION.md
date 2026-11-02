---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The binary-increment normal form f(1)=1 and f(i+1)-f(i) in {0,1} is a bijection for all n. For independent F,G the active jumps of G address pairwise distinct outer increments U_1,...,U_{G(n)-1}; conditioning on G then averaging over independent V_i factors the joint generating polynomial as ∏(1-pq+pq t_i). Thus the FULL output increment vector is iid Bernoulli(pq), not merely its rank. Induction gives all k factors and exact map fiber multiplicity (2^k-1)^(n-r). The absorbing map has all bits zero, giving exact hitting/TV laws and the lattice-window binomial-Poisson cutoff. n=1 and p,q=0 or1 are explicitly accounted for. Fresh independent actual-map composition checks: 36 parameter/fiber tests for n<=6 and k<=4; these do not establish the general statement.

## originality

PASS

One-element rank and monoid cardinality are established earlier; the full product measure convolution, every labeled ordered factor fiber and logarithmic absorbing cutoff require the new distinct-index argument. No inspected source asserts an equivalent all-k law. Strongest caveat: inaccessible original 1990/1992 Higgins works on random transformation products may contain specializations; they were not treated as proven NOT_COVERING.

## value

PASS

This resolves a natural multiplicative probabilistic problem on an entire noncommutative transformation-monoid family: it determines the full product law and exact fibers, hitting-time distribution and sharp mixing scale, not merely a textbook binomial fact for one map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
