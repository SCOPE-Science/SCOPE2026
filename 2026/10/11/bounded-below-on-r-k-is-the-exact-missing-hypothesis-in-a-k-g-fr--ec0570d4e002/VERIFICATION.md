---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

In Li--Leng--Huang Theorem 5 the displayed implication incorrectly turns the operator norm upper bound ||Tx||<=||T|| ||x|| into a lower estimate. On H=R^2 choose K=I, Lambda1=I, T=diag(1,0); all printed hypotheses hold, but e2 witnesses lower-frame inequality failure. Sufficiency of a positive lower bound m for T on Range(K*) follows from sum_i||Lambda_i T f||^2 >=A||K*T f||^2=A||T K*f||^2>=A m^2||K*f||^2, with upper B||T||^2||f||^2. Necessity for universal preservation follows by taking the valid single-operator K-g-frame Lambda1=K*: its composed lower bound is exactly a lower bound for T on the range. If T=0 or K=0, the formal composed upper constant B||T||^2 may be zero; choose any positive larger Bprime, leaving the exact lower equivalence unchanged. No closed-range assumption required.

## originality

PASS

The exact counterexample and necessary/sufficient universal repair were compared against the original erroneous full-text Theorem 5 and a later full-text isometry-preservation theorem. The latter covers an isometry as a strict sufficient special case but not the precise range-bounded-below iff. The universal necessity via Lambda1=K* is explicit; no indexed erratum was verified, an honest remaining priority risk.

## value

PASS

A false general operator construction theorem corrupts lower-frame estimates. A concrete rank-one projection kills the claim even in a Parseval setting, while the exact iff identifies when *every* K-g-frame is preserved and supplies quantitative bounds. This is a motivated correction with reusable criterion, not merely an obvious normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
