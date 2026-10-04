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

For
\[
p_1=p_2=p_3=p,\qquad n=2p,
\]
with \(p\) an odd prime,
\[
P=3p^2,\qquad Q=p,\qquad d_1=d_2=p.
\]
Thus Theorem 29 applies exactly as printed.

Its coloring equations reduce to
\[
p(c-a)\equiv0\pmod{2p},
\qquad
p(c-b)\equiv0\pmod{2p},
\]
so \(a,b,c\) have the same parity. Writing
\[
(a,b,c)=(e+2A,e+2B,e+2C)
\]
identifies the coloring set with \(\mathbb F_2\times\mathbb F_p^3\).

Every endomorphism of \(R_{2p}\) is affine:
\[
x\longmapsto rx+s.
\]
For a nontrivial coloring the vector
\[
(B-A,C-A)\in\mathbb F_p^2\setminus\{0\}
\]
therefore changes only by scalar multiplication. Its projective class is invariant until the coloring collapses to a constant.

There are \(p+1\) projective classes, each containing
\[
2p(p-1)
\]
colorings. Chinese-remainder counting gives exactly two endomorphisms between any ordered pair in one nontrivial block and exactly two from a nontrivial coloring to a prescribed constant coloring. Distinct projective classes have no directed edges between them.

The bundled regression script prints:

`VERIFY_OK primes=5,7,11 p5_actual=10+40+40+40+40+40+40 p5_theorem29=10+40+40+40+120 projective_block_pattern=true`

It constructs the complete coloring sets and affine endomorphism actions for \(p=5,7,11\). The finite replay is not the infinite proof.

The independent-audit channel has not been performed.
