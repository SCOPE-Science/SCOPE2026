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
For fixed household count
\[
n
\]
and total income
\[
S,
\]
define
\[
Q(x)=\prod_i x_i^{x_i}
\]
and
\[
P(x)=\prod_i x_i.
\]

Theil \(T\) satisfies
\[
T(x)=\frac1S\log Q(x)+\log\left(\frac nS\right),
\]
so its ordering is exactly the ordering of \(Q\).

Mean log deviation satisfies
\[
L(x)=\log\left(\frac Sn\right)-\frac1n\log P(x),
\]
so its ordering is the reverse ordering of \(P\).

The embedded `verify_theil_mld_boundary.py` enumerates every positive integer partition for
\[
2\le n\le S\le11
\]
and checks all
\[
408
\]
unordered within-\((n,S)\) profile pairs.

It finds no weak-order disagreement through
\[
S=10
\]
and exactly three strict reversals at
\[
S=11.
\]

Run:

`python3 verify_theil_mld_boundary.py`

The first output line must be:

`VERIFY_OK`

No floating-point logarithm comparison is used for the cutoff or first-layer classification.
