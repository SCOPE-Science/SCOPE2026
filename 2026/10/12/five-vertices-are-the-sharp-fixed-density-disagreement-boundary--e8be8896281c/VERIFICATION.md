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
For a connected simple graph with order
\[
n
\]
and size
\[
m,
\]
Freeman degree centralization is
\[
C_F
=
\frac{n d_{\max}-2m}{(n-1)(n-2)}.
\]

At fixed
\[
n
\]
and
\[
m,
\]
its ordering is therefore exactly the ordering by maximum degree.

Degree Gini is
\[
G_d
=
\frac{\sum_{i<j}|d_i-d_j|}{2nm},
\]
so at fixed order and size its ordering is exactly the ordering by pairwise degree spread.

The embedded `verify_freeman_gini_boundary.py` enumerates every labeled simple graph on
\[
2\le n\le5,
\]
filters for connectivity, and canonically quotients by all vertex relabelings.

It recovers connected unlabeled graph counts
\[
1,\ 2,\ 6,\ 21
\]
and checks every pair of isomorphism classes with common order and common size.

Exactly one strict reversal exists through five vertices. It occurs at
\[
n=5,\qquad m=6
\]
between degree multisets
\[
(2,2,2,2,4)
\]
and
\[
(1,2,3,3,3).
\]

For the first sequence,
\[
C_F=\frac23,
\qquad
G_d=\frac2{15}.
\]

For the second,
\[
C_F=\frac14,
\qquad
G_d=\frac16.
\]

Run:

`python3 verify_freeman_gini_boundary.py`

The first output line must be:

`VERIFY_OK`

The lower bound and first-layer uniqueness are finite exhaustive statements, so the complete graph census is a proof rather than an extrapolation.
