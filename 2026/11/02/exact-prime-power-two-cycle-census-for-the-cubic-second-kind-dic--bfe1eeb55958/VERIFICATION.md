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

With t=x², the quotient (F(F(x))−x)/x is t(t−2)³−2(t−2)−1=(t−3)(t−1)³. Therefore whenever x²−1 is a unit, second-iterate fixedness already implies fixedness. At an odd prime the first-displacement factor is a unit on either sign class, and the second-displacement valuation there is 3v_p(x∓1), including p=3. At 2, F is the identity modulo 2; for odd x the first-displacement valuation is 1 and the second is 1+3v_2(x²−1). The minimum latter valuation is 10, attained at x=3. For k≥11 exactly one of x±1 has valuation 1, so the stated condition is precisely x≡±1 modulo 2^(ceil((k−1)/3)−1). Counting the two disjoint balls and dividing by two gives the stated cycle counts. The proof is universal; the package's reported exact finite run is corroboration, not a run observed for this review.

## originality

PASS

The checked literature and catalog entries do not establish the corresponding all-level least-period-two census for iteration of the fixed second-kind cubic. The finding is accepted on the exact residue sets and the sharp dyadic cutoff, not on novelty of polynomial factorization or valuation methods.

## value

PASS

The least nontrivial orbit statistic for a standard second-kind Dickson polynomial is a natural finite-quotient invariant. This calculation locates every such orbit point in two explicit lifting balls and explains the unusually late dyadic branching at exponent eleven through a triple displacement zero. That sharp cutoff and the exact residue sets are useful for a functional-graph census even though the proof is elementary and does not cover higher periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
