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

The companion `artifacts/verify.py` uses only the Python standard library and checks the finite combinatorial bridges in three different ways.

First, it enumerates all subsets of forward pairs \((i,j)\) with \(i<j\), retains exactly the transitive strict relations, and recovers the naturally labeled poset counts
\[
1,1,2,7,40,357,4824
\]
for sizes zero through six. These agree with the published initial row of A006455.

Second, independently of that representation, for every \(n\le5\) it enumerates all ternary orientations of unordered pairs, retains the strict partial orders, and counts every linear extension by brute-force permutations. It recovers the classical labeled-poset counts
\[
1,1,3,19,219,4231
\]
and verifies
\[
\sum_{P\in\mathcal P_n} e(P)=n!\,s_n.
\]
The resulting injective profile through six points is
\[
1,1,4,42,960,42840,3473280.
\]

Third, it computes Stirling numbers of the second kind by recurrence and independently enumerates equality partitions as restricted-growth strings. These two equality-pattern counters agree, and both give the all-tuple profile
\[
1,1,5,55,1241,53551,4182185
\]
through six coordinates.

The replay ends with `VERIFY_OK`.

The script verifies finite enumeration and the two exact transforms. It does not reproduce the model-theoretic proof of ultrahomogeneity of the Fraïssé limit, nor the classical Kleitman–Rothschild asymptotic; those are external mathematical inputs cited in the result.
