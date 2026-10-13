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
At a fixed census total \(N\),
\[
H=\log N-\frac1N\log\left(\prod_i n_i^{n_i}\right)
\]
and
\[
C_2=\frac{\sum_i n_i^2}{N^2}.
\]

Thus exact equality of Shannon and Simpson summaries is checked using the integer invariants
\[
Q=\prod_i n_i^{n_i},
\qquad
M_2=\sum_i n_i^2.
\]

The embedded `verify_hill_joint_identifiability.py` generates all integer partitions through
\[
N=30
\]
and independently cross-checks each partition count by dynamic programming.

It checks
\[
28628
\]
profiles in total.

It verifies:
\[
(H,C_2)\text{ is injective for }N\le23,
\]
exactly two collision classes at \(N=24\),
\[
(S,H,C_2)\text{ is injective for }N\le29,
\]
and exactly one collision class at \(N=30\).

Run:

`python3 verify_hill_joint_identifiability.py`

The first output line must be:

`VERIFY_OK`

All classification comparisons use exact integers.
