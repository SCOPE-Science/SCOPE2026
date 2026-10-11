# Exact Eisenman quotient on polydisc–ball product models

## Finding

Let
\[
k,m\ge1,
\qquad
d=k+m,
\]
and consider the product domain
\[
\Omega_{k,m}
=
\Delta^k\times\mathbb B^m
\subset\mathbb C^d,
\]
where \(\Delta\) is the unit disk and \(\mathbb B^m\) is the Euclidean unit ball.

With the standard Carathéodory–Eisenman and Kobayashi–Eisenman normalizations,
\[
c_\Omega(0)
=
\sup
\left\{
|\det F'(0)|^2:
F\in\mathcal O(\Omega,\mathbb B^d),
\ F(0)=0
\right\},
\]
and
\[
k_\Omega(0)
=
\inf
\left\{
|\det G'(0)|^{-2}:
G\in\mathcal O(\mathbb B^d,\Omega),
\ G(0)=0
\right\},
\]
the exact values at the origin are
\[
k_{\Omega_{k,m}}(0)=1
\]
and
\[
c_{\Omega_{k,m}}(0)
=
q_{\Omega_{k,m}}(0)
=
\frac{m^m}{(k+m)^{k+m}},
\]
where
\[
q_\Omega=\frac{c_\Omega}{k_\Omega}.
\]

The Carathéodory extremum is attained by the explicit linear map
\[
L(z,w)
=
\frac1{\sqrt{k+m}}
\bigl(
z_1,\ldots,z_k,\sqrt m\,w
\bigr).
\]

For the product model appearing in the recent localization analysis,
\[
\Delta\times\mathbb B^n,
\]
this gives
\[
q_{\Delta\times\mathbb B^n}(0)
=
\frac{n^n}{(n+1)^{n+1}}
\sim
\frac1{en}.
\]
More generally, for every fixed
\[
k\ge1,
\]
\[
q_{\Omega_{k,m}}(0)
\sim
e^{-k}m^{-k}
\qquad
(m\to\infty).
\]

## Assumptions and scope

The result concerns the origin of the balanced product domain
\[
\Delta^k\times\mathbb B^m.
\]
No boundary regularity hypothesis is involved.

The normalization is exactly the one used in the cited 2026 localization paper: determinants are squared in the Carathéodory–Eisenman definition and inverse-squared in the Kobayashi–Eisenman definition.

The theorem is stated for
\[
k,m\ge1.
\]
At the limiting pure-product endpoints, the familiar values are recovered separately: the unit ball has quotient invariant \(1\), while the unit polydisc in complex dimension \(d\) has quotient invariant \(d^{-d}\).

The claim is an exact finite-dimensional model computation. It does not assert a new boundary limit for a general domain and does not replace the localization or scaling arguments of the source paper.

## Proof

Write a point of
\[
\mathbb C^d
\]
as
\[
(z,w)\in\mathbb C^k\times\mathbb C^m.
\]
The Minkowski functional of
\[
\Omega_{k,m}
\]
is
\[
p(z,w)
=
\max
\left\{
\|z\|_\infty,\|w\|_2
\right\}.
\]

Let
\[
F:\Omega_{k,m}\longrightarrow\mathbb B^d
\]
be holomorphic with
\[
F(0)=0,
\]
and put
\[
A=F'(0).
\]
The one-variable Schwarz lemma applied on every complex line through the origin gives
\[
\|A(z,w)\|_2
\le
p(z,w).
\]
Thus \(A\) is a contraction from the product norm
\[
\max\{\|\cdot\|_\infty,\|\cdot\|_2\}
\]
to the Euclidean norm.

Write
\[
A=
[u_1\ \cdots\ u_k\ B],
\]
where
\[
u_j\in\mathbb C^d
\]
and
\[
B:\mathbb C^m\to\mathbb C^d.
\]
Fix a unit vector
\[
v\in\mathbb C^m.
\]
For arbitrary unimodular scalars
\[
\varepsilon_1,\ldots,\varepsilon_k,\eta,
\]
the vector
\[
(\varepsilon_1,\ldots,\varepsilon_k,\eta v)
\]
has product norm \(1\), so
\[
\left\|
\sum_{j=1}^k\varepsilon_j u_j+\eta Bv
\right\|_2^2
\le1.
\]
Averaging over independent uniform phases annihilates all cross terms and yields
\[
\sum_{j=1}^k\|u_j\|_2^2+\|Bv\|_2^2
\le1.
\]
Put
\[
t_j=\|u_j\|_2^2,
\qquad
s=\sum_{j=1}^k t_j.
\]
Since the preceding inequality holds for every unit \(v\),
\[
\|B\|_{\mathrm{op}}^2
\le
1-s.
\]

Hadamard's determinant inequality, applied to the first \(k\) columns and to any orthonormal basis of the last \(m\) coordinates, gives
\[
|\det A|^2
\le
\left(\prod_{j=1}^k t_j\right)
\|B\|_{\mathrm{op}}^{2m}.
\]
Hence
\[
|\det A|^2
\le
\left(\prod_{j=1}^k t_j\right)
(1-s)^m.
\]
For fixed \(s\), the arithmetic–geometric mean inequality gives
\[
\prod_{j=1}^k t_j
\le
\left(\frac{s}{k}\right)^k.
\]
Therefore
\[
|\det A|^2
\le
\left(\frac{s}{k}\right)^k
(1-s)^m.
\]
The right-hand side has its unique maximum on
\[
0\le s\le1
\]
at
\[
s=\frac{k}{k+m}.
\]
Its maximum value is
\[
\frac{m^m}{(k+m)^{k+m}}.
\]
Thus
\[
c_{\Omega_{k,m}}(0)
\le
\frac{m^m}{(k+m)^{k+m}}.
\]

For the reverse inequality, define
\[
L(z,w)
=
\frac1{\sqrt{k+m}}
\bigl(
z_1,\ldots,z_k,\sqrt m\,w
\bigr).
\]
If
\[
(z,w)\in\Omega_{k,m},
\]
then
\[
\|L(z,w)\|_2^2
=
\frac{
\sum_{j=1}^k|z_j|^2
+
m\|w\|_2^2
}{
k+m
}
<1.
\]
Hence
\[
L:\Omega_{k,m}\to\mathbb B^d.
\]
Moreover,
\[
|\det L|^2
=
(k+m)^{-k}
\left(\frac{m}{k+m}\right)^m
=
\frac{m^m}{(k+m)^{k+m}}.
\]
This proves the exact Carathéodory–Eisenman value.

For the Kobayashi–Eisenman volume element, the inclusions
\[
\mathbb B^d
\subset
\Delta^k\times\mathbb B^m
\subset
\Delta^d
\]
and monotonicity give
\[
k_{\mathbb B^d}(0)
\ge
k_{\Omega_{k,m}}(0)
\ge
k_{\Delta^d}(0).
\]
Both endpoint values equal \(1\), so
\[
k_{\Omega_{k,m}}(0)=1.
\]
Therefore
\[
q_{\Omega_{k,m}}(0)
=
c_{\Omega_{k,m}}(0).
\]

Finally, with
\[
k=1,\qquad m=n,
\]
\[
\frac{n^n}{(n+1)^{n+1}}
=
\frac1{n+1}
\left(1-\frac1{n+1}\right)^n
\sim
\frac1{en}.
\]
For fixed \(k\),
\[
\frac{m^m}{(m+k)^{m+k}}
=
m^{-k}
\left(1+\frac{k}{m}\right)^{-(m+k)}
\sim
e^{-k}m^{-k}.
\]

## Verification

The determinant optimization is finite-dimensional and exact.

The contraction estimate for
\[
F'(0)
\]
comes from restricting \(F\) to complex lines in the balanced source domain. The phase average is an identity, not a probabilistic approximation: all mixed inner products have zero average.

The determinant bound uses only Hadamard's inequality, the operator-norm estimate for the ball block, and the arithmetic–geometric mean inequality. Equality is realized by the displayed block-diagonal linear map, so no gap remains between the upper and lower bounds.

The Kobayashi–Eisenman value uses only domain inclusions and the exact unit-ball and unit-polydisc values. No numerical experiment or finite search is used to establish the theorem.

## Relationship to prior work

Jaiswal and Kar study strong localization of the Kobayashi–Eisenman volume element and quotient invariant. In their model calculations they prove
\[
q_{\Delta^d}(0)=d^{-d}
\]
and
\[
k_{\Delta\times\mathbb B^n}(0)=1.
\]
The latter product is the scaling model used in their exponentially flat boundary analysis. The inspected full text does not compute
\[
c_{\Delta\times\mathbb B^n}(0)
\]
or its quotient invariant.

The present calculation fills that model constant and, at no extra conceptual cost, gives the full mixed family
\[
\Delta^k\times\mathbb B^m.
\]
The resulting determinant problem is different from the pure-polydisc computation: the disk columns and Euclidean ball block share one contraction budget, and the exact optimum occurs when those budgets are split in the proportions
\[
k:(m).
\]

Kar's earlier work gives dimension-dependent upper and lower estimates for Eisenman volume elements and quotient invariants on convex and \(\mathbb C\)-convex domains. Those general estimates provide broader context but do not supply the exact mixed-product value derived here.

## Limitations

The theorem computes the invariant only at the origin. Homogeneity of the individual factors can be used to transport the value to other points, but an explicit all-point formula is not part of the claim.

The result does not establish a new quotient-invariant boundary asymptotic for exponentially flat domains. It supplies the exact intrinsic constant of the product model only.

The literature comparison included the full recent model paper, the relevant general convex-domain comparison literature, exact-formula searches, and semantic searches. Classical literature on invariant volume elements is extensive, so an older equivalent product-domain computation under different notation remains a residual risk.

## References

1. R. S. Jaiswal and D. Kar, *Strong Localization of the Kobayashi–Eisenman Volume Element and Its Boundary Asymptotics*, arXiv:2606.01773v1, first posted 1 June 2026.
2. D. Kar, *Geometric estimates and comparability of Eisenman volume elements with the Bergman kernel on \((\mathbb C\)-)convex domains*, Bulletin des Sciences Mathématiques 195 (2024), 103467, DOI: 10.1016/j.bulsci.2024.103467.
3. C. Carathéodory, *Über die Abbildungen, die durch Systeme von analytischen Funktionen von mehreren Veränderlichen erzeugt werden*, Mathematische Zeitschrift 34 (1932), 758–792, DOI: 10.1007/BF01180619.
