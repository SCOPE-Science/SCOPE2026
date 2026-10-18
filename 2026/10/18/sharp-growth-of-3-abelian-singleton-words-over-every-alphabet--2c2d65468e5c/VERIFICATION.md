---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Checks performed

A standalone Python 3 verifier `verify.py` builds the claimed necklace-cycle ordering for alphabets of sizes 2 through 7 and checks every class, shared-symbol connector, minimal length and forward-distance sum. For sizes 2 through 4 it independently performs a multiplicity-aware finite Euler-trail search at four parameter vectors per alphabet and checks that there is exactly one possible word for each triple-factor multiset and its fixed initial pair. All binary strings of lengths 8 through 15 were separately enumerated and grouped by complete length-three signatures and initial pairs; every constructed binary family member of those lengths has multiplicity one. The extracted checker produced `ALL_CHECKS_PASS`.

Exact length generating-function coefficients were also independently computed from stars-and-bars as coefficients of `(1-z)^{-q}(1-z^2)^{-binom(q,2)}` at the baseline lengths for `q=2,3,4,5`.

## Boundaries and unproved extensions

Finite checks are not proofs for arbitrary alphabet size or length; the graph-theoretic forced-trail proof covers that full quantifier range, and the matching upper bound is cited from the published original work. No claim is made about exact total singleton numbers, the total leading constant, other values of the equivalence factor length, or independent validation.
