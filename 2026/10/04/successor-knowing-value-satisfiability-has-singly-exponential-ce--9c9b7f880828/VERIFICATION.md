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

Let \(n\) be the written formula length.

The source finite-model construction uses the subformula closure under one negation and modal depth. The elementary syntax bounds are
\[
|\Sigma|\le2n,
\qquad
D\le n.
\]
A conservative substitution into the source estimate yields
\[
N_n=(4n)^{n+1}.
\]

The source standard-model decision proof bounds relevant constant values by
\[
(|C_\varphi||W|+1)(B+1).
\]
For explicit successor syntax,
\[
|C_\varphi|\le n,
\qquad
B\le n,
\]
so
\[
U_n=(nN_n+1)(n+1)
\]
is sufficient.

The certificate representation uses at most \(n\) agent equivalence relations, at most \(n\) proposition valuations, and at most \(n\) constant valuations on \(N_n\) worlds. Its bit length is bounded by
\[
O(nN_n^2+nN_n\log U_n)
=
2^{O(n\log n)}.
\]

Direct checking of equivalence relations and bottom-up formula semantics takes a polynomial in \(n\) and \(N_n\); a naive knowing-value check over pairs of accessible worlds is still bounded by \(O(nN_n^3)\). Hence verification stays within
\[
2^{O(n\log n)}.
\]

## Limits

This verification establishes an upper class only. It does not prove NEXPTIME-hardness or optimality, and it does not cover succinctly coded successor exponents or public-announcement reduction size.
