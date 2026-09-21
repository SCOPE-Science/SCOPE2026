# Rank-three mechanism obstruction and a correction to Bao's Example 6.3

## Statement

Let \(K=\mathbb{Q}(\omega)\), where \(\omega^3=1\) and \(\omega\ne1\). For
\[
E_0:\quad y^2=x^3+At^6+Bt^3+C
\]
with the auxiliary curves \(E_1,E_2,E_3\) and ranks \(r_i=\operatorname{rk}_{\mathbb Z}E_i(\mathbb Q(t))\) defined as in Bao [1], assume Bao's Theorem 1.3.

### Theorem 1 (rank-three mechanism obstruction)

If the nondegenerate rank-one case for \(E_2\) in Bao's Theorem 1.3(c)(i) holds—namely, exactly one of \(\sqrt A,\sqrt C\) lies in \(K\)—then
\[
\operatorname{rk}_{\mathbb Z}E_0(\mathbb Q(t))\le 2.
\]
Consequently a rank-three surface in Bao's family can occur only through one of the following mechanisms:

1. \((r_1,r_2,r_3)=(1,1,1)\), with the \(E_2\)-rank-one contribution necessarily coming from Theorem 1.3(c)(ii), where both \(\sqrt A\) and \(\sqrt C\) lie in \(K\); or
2. \((r_1,r_2,r_3)=(1,2,0)\) or \((0,2,1)\).

In particular, a rank-three example with \((r_1,r_2,r_3)=(1,1,1)\) and the \(E_2\) contribution coming from Theorem 1.3(c)(i) is impossible.

### Theorem 2 (the family printed in Example 6.3 has rank two)

For every integer \(n\ge1\), put
\[
d=32n^3-1,\qquad m=\frac3d,\qquad
A=16n^6,\qquad B=1+3m,\qquad C=16m^3.
\]
Then
\[
(r_1,r_2,r_3)=(1,1,0),\qquad
\boxed{\operatorname{rk}_{\mathbb Z}E_0(\mathbb Q(t))=2}.
\]
Thus the squarefreeness hypothesis on \(32n^3-1\) in Bao's Example 6.3 is not needed for the actual rank calculation: the displayed family has rank two for every \(n\ge1\), rather than rank three for the stated squarefree subfamily.

Two explicit independent sections spanning a finite-index subgroup of \(E_0(\mathbb Q(t))\) are
\[
P_n=\left(\frac{1-m}{4n^2},\;4n^3t^3+\frac{1+3m}{8n^3}\right)
\]
and
\[
Q_n=\left(2t+\frac{16m^2}{t^2},\;-4n^3t^3-12m-\frac{64m^3}{t^3}\right).
\]

## Proof

Bao's Theorem 1.3 gives
\[
r_0=r_1+r_2+r_3,
\]
with \(r_1,r_3\le1\) and \(r_2\le2\). In the nondegenerate rank-one case 1.3(c)(i), exactly one of \(\sqrt A,\sqrt C\) lies in \(K\). But Theorem 1.3(b) requires \(\sqrt A\in K\) for \(r_1=1\), while Theorem 1.3(d) requires \(\sqrt C\in K\) for \(r_3=1\). Hence at least one of \(r_1,r_3\) is zero, so
\[
r_0=r_1+1+r_3\le2.
\]
This proves Theorem 1. Degenerate rank-one cases for \(E_2\) cannot yield rank three either: \(A=0\) forces \(r_1=0\), \(C=0\) forces \(r_3=0\), and \(B^2-4AC=0\) forces both outer rank conditions to fail. Therefore the listed rank-three mechanisms are exhaustive, using Bao's bound \(r_0\le3\) (Proposition 6.1).

Now specialize to Theorem 2. Since \(d\ge31\), we have \(0<m<1\). We first show that \(m\) is never a rational square. If \(m=(a/b)^2\) in lowest terms, then
\[
3b^2=d a^2.
\]
Coprimality forces \(a^2\mid3\), hence \(a=1\) and \(d=3b^2\). But \(d=32n^3-1\equiv7\pmod8\), whereas \(3b^2\pmod8\) can only be \(0,3,4\), a contradiction. Because \(m>0\), this also implies \(\sqrt m\notin K\): if \((a+b\sqrt{-3})^2=m\in\mathbb Q_{>0}\), then \(ab=0\); the case \(b=0\) makes \(m\) a rational square, while \(a=0\) makes it nonpositive.

Thus
\[
\sqrt A=4n^3\in\mathbb Q,\qquad
\sqrt C=4m\sqrt m\notin K.
\]
The identities
\[
32n^3m=3+m,
\]
\[
B^2-4AC=(1-m)^3
\]
and
\[
2\sqrt A\sqrt C-B=(\sqrt m-1)^3,
\qquad
-2\sqrt A\sqrt C-B=(-1-\sqrt m)^3
\]
show that Bao's Theorem 1.3(c)(i) applies, so \(r_2=1\). Moreover,
\[
\frac{B^2-4AC}{4A}
=\left(\frac{1-m}{4n^2}\right)^3,
\]
so Theorem 1.3(b) gives \(r_1=1\). Although
\[
\frac{B^2-4AC}{4C}
=\left(\frac{1-m}{4m}\right)^3,
\]
Theorem 1.3(d) also requires \(\sqrt C\in K\), which fails. Therefore \(r_3=0\), and Theorem 1.3(a) gives \(r_0=2\).

The first displayed section \(P_n\) is the section supplied by Bao's Theorem 1.4(b) for \(E_1\), transported to \(E_0\) via Theorem 1.4(a). For \(E_2\), take the two geometric sections with cube roots \(\sqrt m-1\) and \(-1-\sqrt m\). Their group sum is
\[
(2t+16m^2,\,-4n^3t^2-12mt-64m^3),
\]
which is rational; transporting it to \(E_0\) gives \(Q_n\). The direct-sum decomposition in Theorem 1.4(a) makes the two transported non-torsion components independent and finite-index spanning.

## Relation to the literature

Bao's paper states Theorem 1.3 with the rank criteria above and Proposition 6.1 with the global bound \(\operatorname{rk}E_0(\mathbb Q(t))\le3\). Its Example 6.2 realizes rank three through Theorem 1.3(c)(ii), while Example 6.4 realizes the \((1,2,0)\) mechanism. Example 6.3 explicitly claims a third mechanism: \((1,1,1)\) with the \(E_2\) contribution coming from 1.3(c)(i). However, the same example states \(\sqrt C\notin K\), while Theorem 1.3(d) requires \(\sqrt C\in K\) for \(r_3=1\). The final inference in Example 6.3 checks that \((B^2-4AC)/(4C)\) is a cube but omits this square-root condition [1].

The low-degree criterion underlying Theorem 1.3(b),(d) is traced in Bao to Bremner's 1991 classification [2], and Bao also gives a derivation of the required quadratic criterion in Proposition 3.6. No change to Bao's general rank formula is asserted here; the correction is to the mechanism classification implicit in Section 6 and to Example 6.3.

## Reproducibility

`artifacts/verify.py` symbolically checks the identities used in Theorem 2 and verifies directly that both displayed sections satisfy the defining equation of \(E_0\). It also records the modulo-8 obstruction to \(m\) being a rational square. The script uses exact symbolic arithmetic in SymPy.

## Limitations

The correction is derived from Bao's Theorem 1.3 as stated and from its low-degree criteria; it is not an independent reproof of the full rank formula. The source preprint is very recent and may subsequently be revised. Originality is therefore asserted only to the best of our knowledge. Searches for the arXiv identifier, Example 6.3, its parameter family, and equivalent rank-two/rank-three formulations found no prior correction or follow-up. Bremner's original article was identified bibliographically, but its full text was not independently inspected; Bao reproduces the relevant criterion and proof in Proposition 3.6, which substantially reduces the resulting correctness risk.

## References

1. Z. Bao, *A formula for the rank over \(\mathbb Q(t)\) of the elliptic curve \(y^2=x^3+At^6+Bt^3+C\)*, arXiv:2609.16349v1 (2026). https://arxiv.org/abs/2609.16349
2. A. Bremner, *Some simple elliptic surfaces of genus zero*, Manuscripta Math. 73 (1991), 5--37. https://doi.org/10.1007/BF02567626
