# Exact certificate window for the Chen--Zhang conformal correction

## Finding

Fix a rank-two lattice \(\Lambda\subset\mathbb R^2\) and
\[
0<\varepsilon\le\frac14.
\]
Let \(g_\varepsilon\) be the connection metric on \(S^2\times(\mathbb R^2/\Lambda)\) introduced by Chen and Zhang. For a new parameter \(\tau>0\), define
\[
u_{\varepsilon,\tau}(z)
=
1+\frac{\tau\varepsilon^4}{1+\varepsilon^2}z^2,
\qquad
\widehat g_{\varepsilon,\tau}
=
u_{\varepsilon,\tau}^2g_\varepsilon.
\]
Write
\[
a_\varepsilon=\frac{\varepsilon^4}{1+\varepsilon^2}.
\]

The Chen--Zhang curvature estimate together with their conformal identity certifies
\[
k_{\widehat g_{\varepsilon,\tau}}>0
\]
at every point precisely for
\[
\boxed{
\tau_-(\varepsilon)<\tau<\tau_+(\varepsilon),
}
\]
where
\[
\boxed{
\tau_-(\varepsilon)
=
\frac{\varepsilon^2(1+\varepsilon^2)}
{4(1+\varepsilon^2)-\varepsilon^6},
\qquad
\tau_+(\varepsilon)
=
\frac{1-4\varepsilon^2}{8}.
}
\]

Here "precisely" refers to positivity of this explicit lower-bound certificate, not to the unknown maximal parameter range on which the actual metric may have positive biorthogonal curvature.

More quantitatively, throughout the interval,
\[
\boxed{
k_{\widehat g_{\varepsilon,\tau}}
\ge
\frac{\varepsilon^4}{(1+a_\varepsilon\tau)^2}
\min\!\left\{
\frac18-\tau-\frac{\varepsilon^2}{2},
\frac{2\tau}{1+a_\varepsilon\tau}-\frac{\varepsilon^2}{2}
\right\}.
}
\]
This uniform certified lower bound has a unique maximizing conformal coefficient
\[
\boxed{
\tau_*(\varepsilon)
=
\frac{2}
{24-a_\varepsilon+\sqrt{(24-a_\varepsilon)^2+32a_\varepsilon}}.
}
\]
As \(\varepsilon\to0\),
\[
\boxed{
\tau_*(\varepsilon)
=
\frac1{24}
+
\frac{\varepsilon^4}{864}
+
O(\varepsilon^6).
}
\]

Thus the coefficient \(1/24\) used by Chen and Zhang is asymptotically optimal for their lower-bound mechanism, while for every fixed positive \(\varepsilon\) the certificate-optimal coefficient is slightly larger.

## Assumptions and scope

Chen and Zhang define
\[
k_g(p)=\min_{\sigma\subset T_pM}K_g^\perp(\sigma)
\]
and prove that their connection metric satisfies
\[
k_{g_\varepsilon}
\ge
\varepsilon^4\frac{1-z^2}{8}
-
\frac{\varepsilon^6}{2}
\]
for every rank-two lattice and every
\[
0<\varepsilon\le\frac14.
\]

For a conformal change
\[
\widehat g=u^2g,
\]
their conformal formula reduces the positivity problem to a lower bound for
\[
k_g-\frac{\Delta_g u}{2u}.
\]
For functions depending only on the sphere variable, they also compute
\[
\Delta_{g_\varepsilon}z^2
=
(1+\varepsilon^2)(2-6z^2).
\]

The result below uses exactly these published estimates. It does not replace the source's curvature estimate by an equality. Consequently, failure of the certificate outside the displayed interval does not prove failure of positive biorthogonal curvature.

## Proof

Put
\[
e=\varepsilon^2,
\qquad
a=a_\varepsilon=\frac{\varepsilon^4}{1+\varepsilon^2},
\qquad
s=z^2\in[0,1].
\]
Then
\[
u_{\varepsilon,\tau}=1+a\tau s.
\]
The exact Laplacian formula gives
\[
\frac{\Delta_{g_\varepsilon}u_{\varepsilon,\tau}}
{2u_{\varepsilon,\tau}}
=
\varepsilon^4
\frac{\tau(1-3s)}{1+a\tau s}.
\]
Combining this with the source's lower bound for \(k_{g_\varepsilon}\) yields
\[
k_{g_\varepsilon}
-
\frac{\Delta_{g_\varepsilon}u_{\varepsilon,\tau}}
{2u_{\varepsilon,\tau}}
\ge
\varepsilon^4 B_{\varepsilon,\tau}(s),
\]
where
\[
B_{\varepsilon,\tau}(s)
=
\frac{1-s}{8}
-
\frac{\tau(1-3s)}{1+a\tau s}
-
\frac{e}{2}.
\]

Differentiate with respect to \(s\):
\[
B_{\varepsilon,\tau}'(s)
=
-\frac18
+
\frac{\tau(3+a\tau)}
{(1+a\tau s)^2},
\]
and
\[
B_{\varepsilon,\tau}''(s)
=
-\frac{2a\tau^2(3+a\tau)}
{(1+a\tau s)^3}
<0.
\]
Thus \(B_{\varepsilon,\tau}\) is strictly concave on \([0,1]\). Its minimum is therefore attained at an endpoint. The endpoint values are
\[
B_{\varepsilon,\tau}(0)
=
\frac18-\tau-\frac e2,
\]
and
\[
B_{\varepsilon,\tau}(1)
=
\frac{2\tau}{1+a\tau}-\frac e2.
\]

The first endpoint is positive exactly when
\[
\tau<\frac{1-4e}{8}
=
\tau_+(\varepsilon).
\]
The second is positive exactly when
\[
4\tau>e(1+a\tau),
\]
or
\[
\tau>
\frac{e}{4-ea}
=
\frac{\varepsilon^2(1+\varepsilon^2)}
{4(1+\varepsilon^2)-\varepsilon^6}
=
\tau_-(\varepsilon).
\]
This proves the exact certificate interval.

The interval is nonempty throughout the source range. Indeed, the source coefficient
\[
\tau=\frac1{24}
\]
lies inside it. At this value,
\[
B_{\varepsilon,1/24}(0)
=
\frac1{12}-\frac e2
\ge
\frac5{96}>0,
\]
while, because \(a/24<1\),
\[
B_{\varepsilon,1/24}(1)
=
\frac{1}{12(1+a/24)}-\frac e2
>
\frac1{24}-\frac1{32}
=
\frac1{96}>0.
\]

The conformal factor satisfies
\[
1\le u_{\varepsilon,\tau}\le1+a\tau.
\]
Hence the conformal curvature identity gives
\[
k_{\widehat g_{\varepsilon,\tau}}
\ge
\frac{\varepsilon^4}{(1+a\tau)^2}
m_\varepsilon(\tau),
\]
where
\[
m_\varepsilon(\tau)
=
\min\!\left\{
\frac18-\tau-\frac e2,
\frac{2\tau}{1+a\tau}-\frac e2
\right\}.
\]

It remains to optimize this certified lower bound. The two terms inside the minimum are equal exactly when
\[
1+(a-24)\tau-8a\tau^2=0.
\]
There is one positive root:
\[
\tau_*
=
\frac{2}{24-a+\sqrt{(24-a)^2+32a}}.
\]

Below \(\tau_*\), the second endpoint controls the minimum. Differentiating
\[
\frac{\frac{2\tau}{1+a\tau}-\frac e2}{(1+a\tau)^2}
\]
gives numerator
\[
2+ae+a^2e\tau-4a\tau.
\]
In the full source range,
\[
0<e\le\frac1{16},
\qquad
0<a<\frac1{256},
\qquad
0<\tau<\frac18,
\]
so this numerator is strictly positive. Above \(\tau_*\), the first endpoint controls the minimum; its numerator decreases with \(\tau\) while the positive denominator increases. Therefore the certified lower bound increases strictly up to \(\tau_*\) and decreases strictly afterwards.

Finally, expansion in the small parameter \(a\) gives
\[
\tau_*
=
\frac1{24}
+
\frac{a}{864}
+
O(a^2).
\]
Since
\[
a
=
\frac{\varepsilon^4}{1+\varepsilon^2}
=
\varepsilon^4+O(\varepsilon^6),
\]
we obtain
\[
\tau_*(\varepsilon)
=
\frac1{24}
+
\frac{\varepsilon^4}{864}
+
O(\varepsilon^6).
\]

## Verification

The bundled symbolic checker differentiates \(B_{\varepsilon,\tau}\) exactly, verifies its endpoint formulas and strict concavity, checks the algebraic equivalence of the endpoint inequalities with the two stated parameter bounds, and verifies that the displayed closed form for \(\tau_*\) solves the endpoint-crossing equation.

It also differentiates the two branches of the uniform lower-bound expression and verifies the series
\[
\tau_*
=
\frac1{24}
+
\frac{a}{864}
+
\frac{a^2}{62208}
+
O(a^3).
\]

The argument is analytic for every
\[
0<\varepsilon\le\frac14.
\]
Finite numerical sampling is not used to establish positivity, the interval, or optimality.

## Relationship to prior work

Chen and Zhang construct the connection metric \(g_\varepsilon\), prove the curvature estimate used above, and choose
\[
u_\varepsilon
=
1+\frac{\varepsilon^4 z^2}{24(1+\varepsilon^2)}.
\]
They explain that the \(z^2\) correction is dictated by the leading curvature term and that the factor \(1+\varepsilon^2\) compensates for the horizontal contribution to the Laplacian. Their full proof treats the single coefficient \(1/24\).

The result here keeps the same geometrically natural quadratic correction but exposes its coefficient as a free parameter. Strict concavity in \(z^2\) reduces the resulting global curvature certificate to two endpoint inequalities, producing an exact open parameter window and a unique coefficient optimizing the resulting uniform lower bound.

Pigazzini studies positive biorthogonal curvature on \(S^2\times T^2\) through an affine connection with torsion. That is a different curvature problem from the Levi--Civita Riemannian construction considered here. Bettiol's earlier conformal-deformation construction concerns \(S^2\times S^2\), not the torus product and not this parameterized connection-metric family.

Targeted searches using the source identifier, the quadratic conformal factor, the coefficient \(1/24\), parameter-window terminology, and certificate optimization did not locate a prior statement of this interval or optimizer.

## Limitations

The interval
\[
(\tau_-(\varepsilon),\tau_+(\varepsilon))
\]
is exact for the lower-bound certificate obtained from Chen and Zhang's Theorem 1.1 and conformal identity. It is not claimed to be the exact set of \(\tau\) for which the true biorthogonal curvature of \(\widehat g_{\varepsilon,\tau}\) is positive.

Likewise, \(\tau_*(\varepsilon)\) maximizes the explicit uniform lower bound derived here, not necessarily the true minimum biorthogonal curvature of the metric.

The statement is restricted to
\[
0<\varepsilon\le\frac14
\quad\text{and}\quad
\tau>0.
\]
No classification for negative conformal coefficients or larger \(\varepsilon\) is asserted.

## References

1. Zhiqi Chen and Hui Zhang, *Positive biorthogonal curvature on \(S^2\times T^2\)*, arXiv:2609.08119v1, first submitted 8 September 2026.
2. Alexander Pigazzini, *Positive Biorthogonal Curvature on \(S^2\times T^2\): An open problem no more?*, arXiv:2502.11914, first submitted 17 February 2025.
3. Renato G. Bettiol, *Positive biorthogonal curvature on \(S^2\times S^2\)*, Proceedings of the American Mathematical Society 142 (2014), 4341--4353.
