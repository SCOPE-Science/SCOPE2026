# Sixth-order endpoint law on the degenerate Minkowski-period boundary
## Finding
Let \(q>p\), put
\[
d=q-p,
\]
and let \(\Theta(p,q,r)\) be the period integral associated with the planar isotropic \(L_p\) dual Minkowski equation
\[
u^{1-p}\bigl((u')^2+u^2\bigr)^{(q-2)/2}(u''+u)=1,
\qquad u>0.
\]
Assume that the parameters lie on the degenerate boundary
\[
A(p,q):=p^2-pq+q^2+3p-3q=0.
\]
Then \(0<d\le4\), and as \(r\downarrow1\),
\[
\boxed{
\Theta(p,q,r)
=
\frac{\pi}{\sqrt d}
+
\frac{\pi d^{5/2}(d-4)(d-1)^2}{368640}(\log r)^6
+o\!\left((\log r)^6\right).
}
\]
Because \(\log r\sim r-1\), equivalently
\[
\boxed{
\Theta(p,q,r)
=
\frac{\pi}{\sqrt d}
-
\frac{\pi d^{5/2}(4-d)(d-1)^2}{368640}(r-1)^6
+o\!\left((r-1)^6\right).
}
\]

At every nonexceptional point of this boundary, the displayed sixth-order coefficient is strictly negative. Hence the first nonzero departure from the small-amplitude endpoint value is of order six, even though the known quadratic coefficient vanishes.

The coefficient vanishes exactly when
\[
d=1
\quad\text{or}\quad
d=4.
\]
On the boundary \(A=0\), these are precisely the three parameter points
\[
(1,2),\qquad (-2,-1),\qquad (-2,2).
\]
The primary source records that at these three points the period is in fact constant, so the vanishing of the sixth-order coefficient matches the exact exceptional families.

## Assumptions and scope
The period \(\Theta(p,q,r)\) is the angle between a neighboring minimum and maximum of a nonconstant positive solution, with amplitude ratio
\[
r=\frac{u_+}{u_-}>1.
\]
The recent source proves that away from the three exceptional points the period is strictly decreasing in \(r\) exactly when
\[
A(p,q)\le0.
\]
It also recalls the previously known endpoint expansion
\[
\Theta(p,q,r)
=
\frac{\pi}{\sqrt{q-p}}
+
\frac{\pi A(p,q)}{96\sqrt{q-p}}(r-1)^2
+o\!\left((r-1)^2\right).
\]
The present claim addresses the boundary \(A=0\), where that quadratic test is silent.

Write
\[
s=p+q.
\]
A direct change of variables gives
\[
4A=3d^2-12d+s^2.
\]
Thus \(A=0\) is equivalent to
\[
s^2=3d(4-d),
\]
which immediately implies \(0<d\le4\).

The proof is local near \(r=1\). The source derives its \(E\)-representation globally in the cross-sign sector and transports the remaining regions by duality. Locally, the analytic construction below only uses that \(d=q-p>0\), so the denominator appearing in \(U'\) is positive in a neighborhood of the expansion point.

## Proof
The source introduces
\[
U'(y)=\frac{e^y-1}{qe^y-p},
\qquad
U(0)=0,
\]
and two local inverse branches of \(U(y)=x\), denoted \(y_L(x)<0<y_R(x)\). Their width is
\[
W(x)=y_R(x)-y_L(x).
\]
The new parameter \(E\) satisfies
\[
W(E)=d\log r,
\]
and the period has the convolution form
\[
\Theta(E)
=
\frac1d\int_0^E
\frac{W'(x)}{\sqrt{e^{2(E-x)}-1}}\,dx.
\]

Since
\[
U''(0)=\frac1d>0,
\]
the inverse branches have convergent Puiseux expansions. Put \(t=\sqrt{x}\) and choose the analytic branch \(y(t)\) with positive linear coefficient satisfying
\[
U(y(t))=t^2.
\]
Then
\[
y_R(x)=y(\sqrt{x}),
\qquad
y_L(x)=y(-\sqrt{x}).
\]
Exact series reversion gives
\[
\begin{aligned}
y(t)={}&
\sqrt{2d}\,t
+\frac{s}{3}t^2
+\frac{\sqrt2(3d^2+s^2)}{72\sqrt d}t^3\\
&+\left(\frac{ds}{60}-\frac{s^3}{540d}\right)t^4
+\frac{\sqrt2(3d^2+s^2)^2}{17280d^{3/2}}t^5
+O(t^6),
\end{aligned}
\]
and the seventh-order odd coefficient is
\[
[t^7]y(t)
=
-\frac{\sqrt2\left(2025d^6+7209d^4s^2-477d^2s^4+139s^6\right)}{43545600d^{5/2}}.
\]
Only odd coefficients survive in \(W\). Consequently
\[
W'(x)
=a_1x^{-1/2}+3a_3x^{1/2}+5a_5x^{3/2}+7a_7x^{5/2}+O(x^{7/2}),
\]
where the \(a_j\) are the corresponding coefficients above.

The kernel has the local expansion
\[
\frac1{\sqrt{e^{2z}-1}}
=
\frac1{\sqrt2}z^{-1/2}
-\frac1{2\sqrt2}z^{1/2}
+\frac1{24\sqrt2}z^{3/2}
+\frac1{48\sqrt2}z^{5/2}
+O(z^{7/2}).
\]
Termwise convolution is justified by the convergent local Puiseux expansions. Using
\[
\int_0^E x^{\alpha-1}(E-x)^{\beta-1}\,dx
=
E^{\alpha+\beta-1}B(\alpha,\beta),
\]
one obtains
\[
\Theta(E)
=
\frac{\pi}{\sqrt d}
+c_1E+c_2E^2+c_3E^3+O(E^4),
\]
with
\[
c_1
=
\frac{\pi(3d^2-12d+s^2)}{48d^{3/2}},
\]
\[
c_2
=
\frac{\pi(3d^2-12d+s^2)^2}{9216d^{5/2}}.
\]
On the boundary \(A=0\), substitution of
\[
s^2=12d-3d^2
\]
annihilates both coefficients and simplifies the cubic coefficient to
\[
\boxed{
c_3
=
\frac{\pi(d-4)(d-1)^2}{720\sqrt d}.
}
\]

It remains to return from \(E\) to \(r\). From the leading odd term in the inverse expansion,
\[
W(E)
=
2\sqrt{2dE}+O(E^{3/2}).
\]
Since \(W(E)=d\log r\),
\[
E
=
\frac d8(\log r)^2
+O\!\left((\log r)^4\right).
\]
Therefore
\[
E^3
=
\frac{d^3}{512}(\log r)^6
+o\!\left((\log r)^6\right).
\]
Combining this with the boundary value of \(c_3\) gives
\[
\Theta(p,q,r)-\frac{\pi}{\sqrt d}
=
\frac{\pi d^{5/2}(d-4)(d-1)^2}{368640}(\log r)^6
+o\!\left((\log r)^6\right),
\]
as claimed.

As a consistency check, away from \(A=0\), composing the linear \(E\)-coefficient with
\[
E\sim\frac d8(\log r)^2
\]
recovers exactly the published quadratic coefficient
\[
\frac{\pi A}{96\sqrt d}.
\]

## Verification
The bundled symbolic checker reconstructs the Taylor series of \(U\) directly from
\[
U'(y)=\frac{e^y-1}{qe^y-p},
\]
performs the Puiseux-series reversion through the seventh odd coefficient, expands the convolution kernel, and evaluates all beta integrals symbolically.

It verifies independently that
\[
c_1=\frac{\pi A}{12d^{3/2}},
\qquad
c_2=\frac{\pi A^2}{576d^{5/2}},
\]
and that after imposing \(A=0\),
\[
c_3=\frac{\pi(d-4)(d-1)^2}{720\sqrt d}.
\]
It also verifies the final conversion coefficient
\[
\frac{c_3d^3}{512}
=
\frac{\pi d^{5/2}(d-4)(d-1)^2}{368640}.
\]
No finite sampling is used to infer the asymptotic law.

## Relationship to prior work
Li and Wan obtained the endpoint limit and the quadratic expansion of the same period integral. Their Corollary 4.3 gives the \((r-1)^2\) term proportional to
\[
A(p,q)=p^2-pq+q^2+3p-3q.
\]
Thus their stated expansion becomes inconclusive exactly on \(A=0\).

Tao's recent paper introduces the \(E\)-convolution representation used here and proves that, apart from three explicit exceptional parameter points, \(\Theta\) is strictly decreasing in \(r\) if and only if \(A\le0\). The inspected full text uses Li--Wan's quadratic asymptotic for necessity but does not give a higher-order endpoint coefficient on the degenerate boundary.

The sixth-order coefficient above supplies that missing local quantitative mechanism. Its zero set is exactly the three exceptional constant-period points recorded in the recent classification.

Targeted searches for the source identifier, the boundary polynomial, sixth-order endpoint asymptotics, and the exact denominator \(368640\) did not locate a covering statement.

## Limitations
The result concerns the local small-amplitude regime \(r\downarrow1\). It does not replace the global monotonicity theorem of the source.

The coefficient classifies the first local departure only on the codimension-one boundary \(A=0\). Off that boundary, the published quadratic term is already nonzero in general.

The primary recent preprint does not display an MSC line. The mathematical ownership used here is \(52A10\): the same planar isotropic \(L_p\) dual Minkowski problem is classified under primary code \(52A10\) in Li--Wan's arXiv record, and both sources formulate the unknown as the support function of a planar convex body.

## References
1. Guanyu Tao, *The exact number of nonconstant positive solutions to the planar isotropic \(L_p\) dual Minkowski problem*, arXiv:2609.39636v1, first submitted 30 September 2026.
2. Haizhong Li and Yao Wan, *Classification of solutions for the planar isotropic \(L_p\) dual Minkowski problem*, J. Reine Angew. Math. 834 (2026), 27--56; arXiv:2209.14630v2.
