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
For
\[
n,d\ge1,
\]
the checker evaluates
\[
D(n,d)=\frac{(nd)!}{d!(n!)^d}
\]
and
\[
E(n,d)=\binom{n+d}{d}.
\]

It independently reconstructs the top intersection coefficient
\[
\frac{(nd)!}{(n!)^d}
\]
and verifies that division by the generic map degree \(d!\) gives \(D(n,d)\).

For every tested interior pair it checks the exact identities
\[
\frac{R(n,d+1)}{R(n,d)}
=
\frac{\prod_{j=1}^{n}(nd+j)}{n!(n+d+1)}
\]
and
\[
\frac{R(n+1,d)}{R(n,d)}
=
\frac{\prod_{j=1}^{d}(nd+j)}
{(n+1)^{d-1}(n+d+1)}.
\]

It also verifies the full below/equal/above classification on the finite grid
\[
1\le n,d\le60.
\]

Finite checks are regression evidence only. The proof for all parameters is the finite-map intersection calculation, the symmetric-power Euler identity, and the symbolic monotonicity argument.
