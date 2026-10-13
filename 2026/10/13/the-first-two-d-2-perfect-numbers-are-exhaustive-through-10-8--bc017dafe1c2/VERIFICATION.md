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

The finite theorem is checked by the standalone `verify.cpp`.

The published formula for the second Schemmel totient gives
\[
L_2(n)=0
\]
for even \(n\), while for odd \(n=pu\) with least prime divisor \(p\),
\[
L_2(n)=
\begin{cases}
pL_2(u),&p\mid u,\\
(p-2)L_2(u),&p\nmid u.
\end{cases}
\]

A deterministic linear sieve computes every least prime divisor through
\[
10^8.
\]
The code checks the independent sieve sanity value
\[
\pi(10^8)=5761455.
\]

Because
\[
0\le L_2(n)<n\qquad(n>1),
\]
the exact recurrence
\[
D_2(n)=L_2(n)+D_2(L_2(n))
\]
can be evaluated in increasing order with integer arithmetic.

The verifier examines every integer
\[
2\le n\le10^8
\]
and rejects unless the complete fixed-point set is
\[
\{37147,53290831\}.
\]

Fresh replay from the finalized package:
`VERIFY_OK cutoff=100000000 fixed_points=37147,53290831 pi_count=5761455 max_D2=284911615 argmax_D2=97556803`.

The `max_D2` and `argmax_D2` fields are diagnostics only. No claim is made about values above the stated cutoff.
