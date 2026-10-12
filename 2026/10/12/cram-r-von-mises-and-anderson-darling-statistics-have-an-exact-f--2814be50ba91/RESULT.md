# Cramér–von Mises and Anderson–Darling statistics have an exact finite-sample covariance

## Finding

Let \(X_1,\ldots,X_n\) be iid from a fully specified continuous distribution \(F_0\), with \(n\ge1\). Define
\[
W_n^2
=
n\int_{-\infty}^{\infty}
\bigl(F_n(x)-F_0(x)\bigr)^2\,dF_0(x)
\]
and
\[
A_n^2
=
n\int_{-\infty}^{\infty}
\frac{\bigl(F_n(x)-F_0(x)\bigr)^2}
{F_0(x)(1-F_0(x))}\,dF_0(x).
\]

Then
\[
\boxed{
\operatorname{Cov}(W_n^2,A_n^2)
=
\frac{2n-1}{18n}.
}
\tag{1}
\]

The exact marginal variances are
\[
\boxed{
\operatorname{Var}(W_n^2)
=
\frac{4n-3}{180n}
}
\tag{2}
\]
and
\[
\boxed{
\operatorname{Var}(A_n^2)
=
\frac{
10-6n+(2n-3)\pi^2/3
}{n}.
}
\tag{3}
\]

Consequently,
\[
\boxed{
\operatorname{Corr}(W_n^2,A_n^2)
=
\frac{
\sqrt5(2n-1)
}{
3\sqrt{
(4n-3)
\left(
10-6n+(2n-3)\pi^2/3
\right)
}
}.
}
\tag{4}
\]

In particular,
\[
\operatorname{Cov}(W_n^2,A_n^2)\longrightarrow\frac19
\tag{5}
\]
and
\[
\boxed{
\operatorname{Corr}(W_n^2,A_n^2)
\longrightarrow
\frac{\sqrt5}
{3\sqrt{2\pi^2/3-6}}
=
0.9789229548\ldots.
}
\tag{6}
\]

Thus the two classical quadratic EDF tests remain extremely strongly correlated under the simple null, even asymptotically, despite their very different tail weighting.

## Assumptions and scope

The null distribution \(F_0\) is fully specified and continuous. By the probability integral transform, the result is distribution-free, so the proof may take \(U_i=F_0(X_i)\) iid uniform on \((0,1)\).

The formulas concern the unmodified one-sample statistics written above. Parameter estimation, finite-sample corrections used in software, censoring, and composite nulls change the empirical-process covariance and are outside the claim.

The endpoint singularity of the Anderson–Darling weight is harmless here because the centered empirical-process summands vanish at the corresponding endpoint.

## Proof

Put
\[
Z_u(t)=\mathbf1\{u\le t\}-t,
\qquad
K(s,t)=\mathbb E[Z_U(s)Z_U(t)]=\min(s,t)-st,
\]
for \(U\sim\operatorname{Unif}(0,1)\). For a nonnegative weight \(w\), define
\[
Q_w
=
\int_0^1
w(t)
\left(
\frac1{\sqrt n}\sum_{i=1}^n Z_{U_i}(t)
\right)^2dt.
\]
Then \(W_n^2=Q_1\) and \(A_n^2=Q_a\) with
\[
a(t)=\frac1{t(1-t)}.
\]

Write
\[
h_w(u,v)=\int_0^1w(t)Z_u(t)Z_v(t)\,dt,
\qquad
q_w(u)=h_w(u,u).
\]
Because
\[
\mathbb E[h_w(U,V)\mid U]=0
\]
for independent uniforms \(U,V\), diagonal and off-diagonal parts are orthogonal in the Hoeffding decomposition. For two weights \(w,v\),
\[
\operatorname{Cov}(Q_w,Q_v)
=
\frac1n\operatorname{Cov}(q_w(U),q_v(U))
+
\frac{2(n-1)}n
\iint_{[0,1]^2}
w(s)v(t)K(s,t)^2\,ds\,dt.
\tag{7}
\]

For the Cramér–von Mises weight,
\[
q_1(u)
=
\int_0^u t^2dt+\int_u^1(1-t)^2dt
=
u^2-u+\frac13.
\tag{8}
\]
For the Anderson–Darling weight,
\[
q_a(u)
=
\int_0^u\frac{t}{1-t}\,dt
+
\int_u^1\frac{1-t}{t}\,dt
=
-1-\log(u(1-u)).
\tag{9}
\]

Elementary integrals now give
\[
\mathbb E q_1(U)=\frac16,
\qquad
\mathbb E q_a(U)=1,
\tag{10}
\]
\[
\operatorname{Var}(q_1(U))=\frac1{180},
\tag{11}
\]
\[
\operatorname{Cov}(q_1(U),q_a(U))=\frac1{18},
\tag{12}
\]
and
\[
\operatorname{Var}(q_a(U))
=
4-\frac{\pi^2}{3}.
\tag{13}
\]

For the off-diagonal terms, symmetry across \(s=t\) and
\[
K(s,t)=s(1-t),\qquad 0<s<t<1,
\]
yield
\[
\iint K(s,t)^2\,ds\,dt=\frac1{90},
\tag{14}
\]
\[
\iint
\frac{K(s,t)^2}{t(1-t)}\,ds\,dt
=
\frac1{18},
\tag{15}
\]
and
\[
\iint
\frac{K(s,t)^2}
{s(1-s)t(1-t)}
\,ds\,dt
=
\frac{\pi^2}{3}-3.
\tag{16}
\]

Substituting (12) and (15) into (7) gives
\[
\operatorname{Cov}(W_n^2,A_n^2)
=
\frac1{18n}
+
\frac{n-1}{9n}
=
\frac{2n-1}{18n},
\]
proving (1).

Using (11), (14) in (7) with both weights equal to \(1\) gives (2). Using (13), (16) with both weights equal to \(a\) gives (3). Equation (4) follows by standardization. Equations (5)--(6) follow directly by taking \(n\to\infty\).

## Verification

The accompanying deterministic checker independently evaluates all six one- and two-dimensional integrals that enter the Hoeffding decomposition at high precision.

It then reconstructs covariance and both variances from the decomposition for every \(1\le n\le100\), compares them with the three closed forms, and checks the stated limiting correlation numerically at large \(n\).

These computations are supplementary. The proof for arbitrary \(n\) is the exact decomposition (7) together with the elementary integral identities (8)--(16).

## Relationship to prior work

Laio treats Cramér–von Mises and Anderson–Darling statistics side by side, develops their marginal moments from empirical-process covariance kernels, and discusses small-sample corrections and composite-null applications. In the inspected full article, the moments are computed separately for the two statistics; no joint covariance or correlation between them is stated.

Hwang and Kuriki develop a unified modern theory of generalized Anderson–Darling, Cramér–von Mises, and Watson statistics. Their full manuscript gives covariance kernels and separate Karhunen–Loève eigenstructures for these families, with primary MSC \(62G10\) and \(62E20\). Targeted inspection found no cross-statistic finite-sample covariance formula.

The accepted result instead uses the shared empirical-process summands before diagonalization. This exposes the finite-\(n\) non-Gaussian diagonal correction and shows that the cross-covariance is already a simple rational function of sample size.

## Limitations

The formula is for a fully specified continuous null. Estimated parameters change the limiting covariance kernel and generally destroy the distribution-free finite-sample identity.

No claim is made about joint tail probabilities, optimal combinations of the two tests, or power under alternatives.

Weighted Cramér–von Mises statistics have a large literature. A generic joint-moment identity for two arbitrary weights may imply the calculation after specialization even though no explicit Cramér–von Mises/Anderson–Darling covariance formula was located.

## References

1. F. Laio, “Cramer–von Mises and Anderson–Darling goodness of fit tests for extreme value distributions with unknown parameters,” *Water Resources Research* 40 (2004), DOI 10.1029/2004WR003204, first published 2004-09-28.
2. H.-K. Hwang and S. Kuriki, “Integrated empirical measures and generalizations of classical goodness-of-fit statistics,” arXiv:2404.06040, first public version 2024-04-09; *Electronic Journal of Statistics* 19 (2025), DOI 10.1214/25-EJS2386.
