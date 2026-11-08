---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For every q,n>=2, the earliest greedy embedding makes each distinct deletion descendant correspond to one canonical pair. Writing S=#nonzero adjacent differences, K=#zero-runs, E=#ABA inversions yields B=binom(S+1,2)+K-E, including n=2 constant input. Nonzero increments in each run have q-1 first choices; succeeding nonzero increments have one reversal and q-2 nonreversal choices. Counting alternating runs proves the stated polynomial, with negative powers canceled by B>=1. Independent Bernoulli change indicators and binomial reversal flags yield the exact mean and variance. I independently reconstructed this enumerator and compared it to actual distinct descendants and to the alternate fully equivalent formula in record 0, for 21 exhaustive (q,n) cases, and symbolically verified both given variance formulas agree; these finite checks support the written all-parameter proof.

## originality

PASS

PASS, best of knowledge with explicit risks. This package was committed at 2026-11-02T03:34:52Z, earlier than the equivalent record 0 at 03:34:54Z; the other assigned package is covered here and is not a prior independent theorem. The Resultary corpus contains an exact binary variance only, and Li–Wang–Fu provide q-ary per-word extrema, not a full all-source distribution. The 2008 Mercier paper is relevant but inaccessible beyond its abstract; it may have more relevant formulae than can be verified. Checked sources did not establish a full all-q,n distribution predating this result; absence of hits is not proof of priority.

## value

PASS

A full parameterized all-q,n distribution of distinct two-deletion descendants is a natural and independently useful finite-block synchronization channel invariant. It yields every probability, tail and moment, not just fixed-word bounds or pre-known binary variance. The distinct run-and-reversal enumeration provides a meaningful structural derivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
