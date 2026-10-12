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
# Verification

The accompanying `artifacts/verify.cpp` performs an exhaustive finite check for \(0\le n\le6\).

It uses one ternary state for every unordered pair of labels: incomparable, forward, or backward. A state is accepted exactly when the induced strict relation is transitive. This independently recovers the classical labeled partial-order counts
\[
1,1,3,19,219,4231,130023.
\]

For each accepted upper order \(Q\), a coordinatewise zeta transform counts accepted lower orders \(P\subseteq Q\). Summing these counts produces
\[
1,1,5,79,3221,301831,60305525.
\]

The program then computes Stirling numbers of the second kind by recurrence and verifies the repeated-coordinate transform
\[
b_n=\sum_{k=0}^n {n\brace k}a_k,
\]
obtaining
\[
1,1,6,95,3731,336092,65049621.
\]

The captured output ends with `VERIFY_OK`.

This computation checks the finite census and the transform. It does not independently re-prove Lipparini's Fraïssé-limit theorem or independently audit the literature-originality assessment.
