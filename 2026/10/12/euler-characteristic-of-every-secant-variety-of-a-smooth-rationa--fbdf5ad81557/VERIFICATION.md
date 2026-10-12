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
The checker verifies three independent pieces of the proof.

First, for binary monomials of every degree
\[
1\le d\le18,
\]
it constructs the relevant catalecticant matrix and computes its rank by exact rational Gaussian elimination. The rank agrees with
\[
\min\{j,d-j\}+1
\]
for every
\[
0\le j\le d.
\]

Second, it checks the finite-difference identities
\[
\sum_{h=0}^{q}(-1)^{q-h}\binom qh h^a=0
\]
for
\[
0\le a<q
\]
and the leading identity
\[
\sum_{h=0}^{q}(-1)^{q-h}\binom qh h^q=q!
\]
through
\[
q=12.
\]

Third, for deterministic scroll types with
\[
2\le k\le5
\]
and splitting degrees at most \(9\), it enumerates all coordinate monomials and verifies that the number whose exact border-rank threshold is at most \(r\) equals
\[
\sum_i\min\{d_i+1,2r\}
\]
at every tested secant level.

Finite checks are regression evidence only. The all-parameter theorem is proved symbolically in `RESULT.md`.
