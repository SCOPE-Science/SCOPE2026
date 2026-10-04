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

The checker implements the two source conditions literally on the chain
\[
C_n=\{0,\ldots,n-1\}.
\]

For every relation through
\[
n=4,
\]
it tests downward confluence
\[
x\le x'Ry'
\Longrightarrow
\exists y\,(xRy\le y')
\]
and forward confluence
\[
x'\ge xRy
\Longrightarrow
\exists y'\,(x'Ry'\ge y).
\]

It separately computes each row minimum with empty sentinel \(n\) and each row maximum with empty sentinel \(-1\), and verifies that the direct predicates are respectively equivalent to monotonicity of these endpoint sequences.

It then checks the simultaneous normal form: either the relation is empty, or every row is nonempty and both finite endpoint sequences are nondecreasing.

Direct relation-level counts are
\[
2,\ 7,\ 80,\ 2855
\]
for \(n=1,2,3,4\).

An independent weighted dynamic program evaluates the endpoint formula. Its state set is
\[
\{(m,M):0\le m\le M<n\},
\]
with row weight
\[
2^{\max(M-m-1,0)}.
\]
It sums weights over nondecreasing state sequences of length \(n\), then adds the empty relation. The first six values are
\[
2,\ 7,\ 80,\ 2855,\ 374660,\ 195589841.
\]

The first four formula counts agree exactly with direct enumeration. The script also evaluates further terms as a consistency check.

The script prints `VERIFY_OK`.

## Limits

Finite enumeration corroborates the proof but is not used to infer the arbitrary-\(n\) theorem. The general result follows from the endpoint-witness argument. No claim is made for non-chain intuitionistic orders.
