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

For the original Hilbert-space theorem, take a one-point measure space and
\[
K=I,\qquad
\Lambda_\ast=\sqrt A\,I,\qquad
L=tI,\qquad
a_\ast=-\frac{\sqrt A}{t},
\qquad t>1.
\]
Then
\[
\|\Lambda_\ast x\|^2=A\|K^*x\|^2,
\]
so the original family is \(A\)-tight. The printed perturbation hypothesis holds because
\[
|a_\ast|^2
=
\frac{A}{t^2}
<
\frac{A}{t}
=
\frac{A}{\|L\|}.
\]
But
\[
\Lambda_\ast+a_\ast LK^*=0.
\]
Thus the conclusion fails exactly.

The proof defines
\[
R=\|L\|^2\|a\|_2^2.
\]
Its lower estimate is
\[
\|R_\Gamma x\|
\ge
(\sqrt A-\sqrt R)\|K^*x\|.
\]
A positive lower bound therefore requires
\[
R<A,
\]
equivalently
\[
\|a\|_2^2<\frac{A}{\|L\|^2}.
\]
At equality, the scalar example cancels exactly.

The later Hilbert-\(C^*\)-module theorem has the identical algebraic structure, with
\[
R=\|Q\|^2\|c\|_2^2.
\]
Its scalar Hilbert-\(\mathbb C\)-module specialization is the same counterexample. For the general module repair, the perturbed adjointable analysis operator is bounded below whenever
\[
\|Q\|\|c\|_2<\sqrt A.
\]
Then its positive Gram operator is invertible and supplies the required module-order lower frame bound.

The primary theorem pages and the later generalization theorem pages were inspected in the actual full-text sources. No numerical experiment, finite enumeration, or approximate certificate is used.
