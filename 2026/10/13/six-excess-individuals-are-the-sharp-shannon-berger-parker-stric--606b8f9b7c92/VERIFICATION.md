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
For fixed total
\[
N,
\]
define
\[
Q(n)=\prod_i n_i^{n_i}
\]
and
\[
M(n)=\max_i n_i.
\]

Then Shannon entropy satisfies
\[
H=\log N-\frac1N\log Q(n),
\]
while order-\(\infty\) Hill diversity is
\[
{}^{\infty}D=\frac{N}{M(n)}.
\]

Thus both rankings reduce to exact integer comparisons.

The embedded `verify_shannon_berger_parker_boundary.py` checks profiles through excess
\[
r=6,
\]
verifies weak-order agreement through \(r=3\), the unique first tie split at \(r=4\), absence of strict reversal through \(r=5\), and the complete first strict layer at \(r=6\).

The verifier also reconstructs abundance profiles from partitions of the excess \(r\). Once richness satisfies
\[
k\ge r,
\]
larger richness only pads profiles with baseline ones, which change neither \(Q\) nor \(M\). This makes the finite check exhaustive for every
\[
k\ge3.
\]

Run:

`python3 verify_shannon_berger_parker_boundary.py`

The first output line must be:

`VERIFY_OK`

All classification comparisons use exact integers.
