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

The proof has two exact components.

For the frame bound, a bounded morphism onto \(K_r^{\mathrm r}\) is exactly a partition into \(r\) dominating fibers. Complementary pairs give \(2^{n-1}\) dominating blocks. The Hall argument on complement-pair tokens proves that no domatic partition of any induced subframe can have more blocks.

For logical strictness, set
\[
r_n=2^{n-1}+1.
\]
The Jankov--Fine formula of \(K_{r_n}^{\mathrm r}\) is frame-valid throughout the \(n\)-atom compatibility frame family. At stage \(n+1\), complement blocks give a bounded morphism onto \(K_{r_n}^{\mathrm r}\). Coordinate variables with
\[
v(q_i)=[n+1]\setminus\{i\}
\]
make the propositional formula
\[
\theta_A=
\bigwedge_{i\in A}\neg q_i
\wedge
\bigwedge_{i\notin A}q_i
\]
true exactly at state \(A\). Hence arbitrary bounded-morphism fibers are definable and the corresponding substitution instance of the characteristic formula fails.

The bundled `verify.py` exhaustively computes the maximum domatic number over every induced subgraph for \(n\le3\), verifies complement-pair domatic partitions through \(n=8\), and checks exact-state coordinate coding and the quotient construction at further finite sizes. It prints `VERIFY_OK`.

## Limits

The computation is corroborative. The arbitrary-\(n\) theorem follows from the Hall and Jankov--Fine arguments, not finite extrapolation. No optimal formula-size claim is made.
