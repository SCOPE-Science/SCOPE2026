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
For a positive-integer abundance profile of total \(N\), define
\[
Q=\prod_i n_i^{n_i}
\]
and
\[
F=\prod_i n_i!.
\]

Then
\[
H_S=\log N-\frac1N\log Q
\]
and
\[
H_B=\frac{\log(N!)-\log F}{N}.
\]

At fixed \(N\), both diversity rankings therefore reduce to exact integer comparisons.

The embedded `verify_shannon_brillouin_boundary.py` generates every integer partition for
\[
1\le N\le8
\]
and independently cross-checks the partition counts
\[
1,2,3,5,7,11,15,22.
\]

It verifies complete weak-order agreement through \(N=6\), the unique Brillouin tie split by Shannon at \(N=7\), and exactly two strict reversals at \(N=8\).

Run:

`python3 verify_shannon_brillouin_boundary.py`

The first output line must be:

`VERIFY_OK`

All classification comparisons use exact integers; logarithms are needed only to translate the invariant inequalities back into index differences.
