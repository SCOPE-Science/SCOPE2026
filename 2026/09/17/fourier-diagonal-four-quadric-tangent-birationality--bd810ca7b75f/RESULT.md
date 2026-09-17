# Tangent birationality for a Fourier-diagonal Calabi–Yau intersection of four quadrics

## Statement

Let \(\zeta=e^{2\pi i/8}\), and in \(\mathbb P^7\) with homogeneous coordinates
\([x_0:\cdots:x_7]\) define
\[
X=\bigcap_{m=1}^4 V(Q_m),\qquad
Q_m(x)=\sum_{j=0}^7 \zeta^{mj}x_j^2.
\]
Then \(X\) is a smooth Calabi–Yau threefold, the embedding
\(X\hookrightarrow\mathbb P^7\) is the complete embedding defined by
\(\mathcal O_X(1)\), and its tangent-incidence morphism
\[
q:\mathbb P(J^1(\mathcal O_X(1))^*)\longrightarrow \operatorname{Tan}(X)
\]
is birational. Equivalently,
\[
\tau_{\mathrm{tan}}(X)=1.
\]
Consequently,
\[
\deg\operatorname{Tan}(X)=64.
\]

This gives an explicit symmetric special member of the \(X_{2,2,2,2}\) family
satisfying the tangent-birationality prediction. Kanazawa proves tangent degree
one for a general intersection of four quadrics, while conjecturing it for every
complete Calabi–Yau embedding in ambient dimension at least seven.

## Fourier model

Put \(t_j=\zeta^j\), and let
\[
E(p)=(p(t_0),\ldots,p(t_7)),\qquad
K=E\bigl(\mathbb C[t]_{\le3}\bigr)\subset\mathbb C^8.
\]
The discrete Fourier orthogonality relations give
\[
\sum_{j=0}^7 t_j^m p(t_j)=0
\quad (m=1,2,3,4;\ \deg p\le3).
\]
Both sides define four-dimensional subspaces of \(\mathbb C^8\), hence
\[
x\in X
\quad\Longleftrightarrow\quad
(x_0^2,\ldots,x_7^2)\in K.
\]

The variety has a large visible symmetry group: arbitrary coordinate sign
changes preserve all four equations, and the cyclic coordinate shift preserves
their span. In particular, this is not being presented as a generic choice of
four quadrics.

## Smoothness

Suppose the Jacobian of \(Q_1,\ldots,Q_4\) has rank less than four at a
projective point \(x\in X\). Then there are coefficients \(c_1,\ldots,c_4\),
not all zero, such that
\[
\left(\sum_{m=1}^4 c_m t_j^m\right)x_j=0
\qquad(j=0,\ldots,7).
\]
Writing
\[
p(t)=\sum_{m=1}^4 c_m t^m=t\,r(t),\qquad \deg r\le3,
\]
we see that \(p\) vanishes at at most three of the eighth roots \(t_j\).
Therefore \(x\) has at most three nonzero coordinates.

On the other hand \(x\in X\) gives
\[
(x_0^2,\ldots,x_7^2)=E(f)
\]
for a polynomial \(f\) of degree at most three. Since at least five coordinates
of \(x\) vanish, \(f\) has at least five distinct roots among the \(t_j\), so
\(f=0\), contradicting \(x\ne0\). Thus \(X\) is smooth.

A positive-dimensional complete intersection in projective space is connected;
smoothness then makes \(X\) irreducible. Adjunction gives
\[
K_X\simeq\mathcal O_X(2+2+2+2-8)\simeq\mathcal O_X,
\]
and the standard cohomology of a smooth complete intersection gives
\(H^1(X,\mathcal O_X)=0\). Thus \(X\) is Calabi–Yau. Since its ideal has no
linear forms, \(\mathcal O_X(1)\) gives the complete embedding in \(\mathbb P^7\).

## A tangent point with a singleton reduced fibre

All calculations below can be made in
\[
R=\mathbb Q[t]/(t^8-1),\qquad K_{\mathbb Q}=\langle1,t,t^2,t^3\rangle.
\]
Take
\[
f=-2-t+2t^3,\qquad g=2+t^2.
\]
Both \(f\) and \(g\) are coprime to \(t^8-1\). Choose \(x_j\in\mathbb C^*\) with
\[
x_j^2=f(t_j),
\]
and define
\[
w_j=\frac{g(t_j)}{x_j}.
\]
Because \(E(f)\in K\), the point \([x]\) lies on \(X\). Moreover
\[
(x_jw_j)_{j=0}^7=E(g)\in K,
\]
which is exactly the linearized system for \([w]\in T_xX\).

Now let \([y]\) be any point of the tangent-incidence fibre over \([w]\).
Set
\[
h_j=y_jw_j.
\]
The condition \([w]\in T_yX\) is equivalent to \(h=E(h(t))\in K\), where
\[
h(t)=b_0+b_1t+b_2t^2+b_3t^3.
\]
Since every \(w_j\ne0\),
\[
y_j^2=\frac{h(t_j)^2f(t_j)}{g(t_j)^2}.
\]
Hence \(y\in X\) is equivalent, scheme-theoretically, to
\[
h^2f\in g^2K_{\mathbb Q}\subset R.
\]

An exact elimination of these four quadratic conditions gives the following
homogeneous quadrics in \([b_0:b_1:b_2:b_3]\):
\[
\begin{aligned}
F_1={}&3b_0^2-12b_0b_1-8b_0b_2+4b_0b_3-4b_1^2
      +4b_1b_2+8b_1b_3+4b_2^2-6b_2b_3,\\
F_2={}&11b_0^2+12b_0b_1-24b_0b_2-16b_0b_3-12b_1^2
      -16b_1b_2+8b_1b_3+4b_2^2+16b_2b_3-6b_3^2,\\
F_3={}&b_0^2-b_0b_1-2b_0b_2-8b_0b_3-b_1^2
      -8b_1b_2+2b_2b_3+4b_3^2,\\
F_4={}&3b_0^2+4b_0b_1-2b_0b_2-4b_0b_3-b_1^2
      -4b_1b_2-16b_1b_3-8b_2^2+2b_3^2.
\end{aligned}
\]
On the affine chart \(b_0=1\), their exact lexicographic Gröbner basis is
\[
b_1,\qquad b_2-\frac12,\qquad b_3.
\]
On the hyperplane \(b_0=0\), each of the three standard projective charts
\(b_1=1\), \(b_2=1\), \(b_3=1\) has Gröbner basis containing \(1\).
Therefore the full projective fibre scheme is the single reduced point
\[
[b_0:b_1:b_2:b_3]=[2:0:1:0],
\]
which is precisely \(h=g\) and hence precisely the original point \([x]\).

## From one reduced fibre to generic degree one

We use the following elementary lemma.

**Lemma.** Let \(q:Y\to Z\) be a proper dominant generically finite morphism of
irreducible varieties. If one scheme-theoretic fibre consists of a single
reduced point, then \(\deg q=1\).

**Proof.** The given fibre is finite. Remove from \(Z\) the proper closed image
of the non-quasi-finite locus not meeting that fibre. On a neighbourhood of the
chosen point, proper plus quasi-finite makes \(q\) finite. Write the corresponding
local finite extension as \(A\to B\). Since \(Y\) is irreducible and \(q\) is
dominant, \(B\) is torsion-free over the domain \(A\), and its generic rank is
\(d=\deg q\). The reduced singleton fibre says
\[
\dim_{k} B/\mathfrak m_A B=1.
\]
By Nakayama, \(B\) is generated by one element as an \(A\)-module locally.
After tensoring with \(\operatorname{Frac}(A)\), this forces \(d\le1\).
Dominance gives \(d=1\). \(\square\)

For a smooth nondegenerate threefold in \(\mathbb P^7\), the tangent-incidence
map has six-dimensional source and is generically finite onto the
six-dimensional tangent variety. Applying the lemma to the explicit reduced
singleton fibre above gives
\[
\tau_{\mathrm{tan}}(X)=1.
\]

For a smooth complete intersection \(X_{2,2,2,2}\subset\mathbb P^7\), the
standard tangential Chern-gap calculation gives
\[
\tau_{\mathrm{tan}}(X)\deg\operatorname{Tan}(X)=64.
\]
Thus
\[
\deg\operatorname{Tan}(X)=64.
\]

## Context and originality

Kanazawa's September 2026 preprint formulates tangent birationality
\(\tau_{\mathrm{tan}}=1\) for complete very ample Calabi–Yau threefold embeddings
in \(\mathbb P^N\), \(N\ge7\), and proves it for a **general** complete
intersection of four quadrics in \(\mathbb P^7\). The theorem above instead
certifies a concrete highly symmetric diagonal member by exhibiting one exact
reduced tangent-incidence fibre.

To the best of our knowledge, targeted searches for tangent degree or tangent
birationality of diagonal, cyclic, or Fourier-type intersections of four
quadrics did not locate this explicit example or an equivalent certificate.
Hernandez Gomez–Russo provides the broader framework for tangent degree and
tangent varieties but does not identify this special four-quadric example.

## Limitations

The theorem concerns one explicit member of the \(X_{2,2,2,2}\) family. It does
not prove tangent birationality for every smooth intersection of four quadrics,
nor does it settle Kanazawa's full stable-range conjecture. The motivating
preprint is very recent, so unindexed concurrent work on special members remains
a residual originality risk.

## Reproducibility

`artifacts/verify_fiber.py` performs the exact calculation over
\(\mathbb Q[t]/(t^8-1)\) with SymPy 1.14.0. It checks the two coprimality
conditions, derives the four fibre quadrics, verifies the Gröbner basis on the
\(b_0=1\) chart, and checks all three charts at infinity. The recorded output is
in `artifacts/VERIFICATION.txt`.

## References

1. Atsushi Kanazawa, *Chern bounds and tangent geometry of polarized Calabi-Yau
   threefolds*, arXiv:2609.17513 (2026).
2. Jordi Hernandez Gomez and Francesco Russo, *On the tangent degree and the
   degree of the tangent variety of a projective variety*, arXiv:2605.09437
   (2026).
