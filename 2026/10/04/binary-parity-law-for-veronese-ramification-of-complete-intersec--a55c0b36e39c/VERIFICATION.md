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
The proof has four exact ingredients.

First, \(k<\min_i d_i\) implies that the complete-intersection ideal has no nonzero degree-\(k\) form, so the restricted series has
\[
M=\binom{N+k}{k}
\]
sections and line-bundle degree \(kD\).

Second, the Wronskian of a base-point-free series of projective dimension \(M-1\) lies in
\[
L^{\otimes M}\otimes K_C^{\otimes M(M-1)/2},
\]
giving degree
\[
M\bigl(kD+(M-1)(g-1)\bigr).
\]

Third, complete-intersection adjunction gives
\[
2g-2=D(S-N-1).
\]

Fourth, Kummer--Lucas parity gives
\[
\binom{N+k}{k}\equiv1\pmod2
\]
exactly when the binary addition of \(N\) and \(k\) has no carry, equivalently \(N\mathbin{\&}k=0\).

The bundled checker verifies the resulting formulas on a bounded family and separately verifies the binomial/bitwise equivalence on a substantially larger range. Those finite checks are regression evidence only.

Limits: characteristic zero, smooth complete intersections, and \(1\le k<\min_i d_i\). The real conclusion guarantees existence but not simplicity or a count of distinct real ramification points.
