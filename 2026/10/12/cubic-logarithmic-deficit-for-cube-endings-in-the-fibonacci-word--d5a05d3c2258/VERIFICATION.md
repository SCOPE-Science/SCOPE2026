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

Run `python3 verify.py` beside `certificate.json`.

The verifier generates the run-start regular language parametrically and checks its exact cumulative count against
\[
R_L=
\binom{\lfloor L/2\rfloor}{3}
+
2\binom{\lfloor(L-1)/2\rfloor}{3}
+
\binom{\lfloor(L-2)/2\rfloor}{3}
\]
for every \(L\le40\).

It independently generates a Fibonacci-word prefix of length \(2400\). At every position it checks the cube-ending predicate directly by testing all possible cube periods, rather than consulting the regular expression. The starts of the resulting one-runs are compared against canonical Zeckendorf representations matching the published pattern.

Complete zero-runs in the test prefix are checked against the published permitted lengths, and the exact one-run-start counts are checked at Fibonacci cutoffs for \(6\le L\le15\). Every prefix length through \(2400\) is also checked against the proved two-sided deficit bound.

The finite replay tests the bookkeeping and implementation only. The infinite theorem follows from the exact symbolic count and the published run theorems.
