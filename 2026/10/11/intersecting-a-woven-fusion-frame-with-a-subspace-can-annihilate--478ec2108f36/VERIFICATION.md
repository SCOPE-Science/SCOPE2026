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

Take
\[
H=\mathbb R^2,\qquad X=\{1,2\}
\]
with counting measure and unit weights. Define both source families by
\[
F(1)=G(1)=\operatorname{span}\{e_1\},
\qquad
F(2)=G(2)=\operatorname{span}\{e_2\}.
\]
For every partition of \(X\), choosing either source at either atom changes nothing, so for
\[
h=ae_1+be_2
\]
the weaving energy is
\[
|a|^2+|b|^2=\|h\|^2.
\]
Thus the pair is Parseval woven.

Let
\[
W=\operatorname{span}\{e_1+e_2\}.
\]
Each coordinate axis meets \(W\) only in \(0\). Therefore every intersected analysis projection is zero and every nonzero vector of \(W\) has zero weaving energy.

The erroneous projection identity can be checked directly on
\[
u=\frac{e_1+e_2}{\sqrt2}.
\]
Since \(u\in W\),
\[
P_Wu=u,
\]
and hence
\[
P_{\operatorname{span}\{e_1\}}P_Wu
=
\frac1{\sqrt2}e_1.
\]
But
\[
\operatorname{span}\{e_1\}\cap W=\{0\},
\]
so
\[
P_{\operatorname{span}\{e_1\}\cap W}u=0.
\]

If instead \(P_W\) commutes with each relevant orthogonal projection \(P_V\), then \(P_VP_W\) is the orthogonal projection onto \(V\cap W\). For \(h\in W\),
\[
P_{V\cap W}h=P_Vh,
\]
so every intersected weaving has exactly the original weaving energy on \(W\).

The arXiv and final journal forms of Theorem 2.2 and its proof were inspected directly. The earlier commuting-projection intersection theorem was also inspected in full text and as a rendered PDF page.
