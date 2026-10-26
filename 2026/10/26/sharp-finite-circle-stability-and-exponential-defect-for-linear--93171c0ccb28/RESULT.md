# Sharp finite-circle stability and exponential defect for linear spline projection

## Finding

Let \(n\ge3\) be an integer. On the circle \(\mathbb T=\mathbb R/\mathbb Z\) take the \(n\) equally spaced nodes \(j/n\), and let \(V_n\) be the space of continuous functions affine on every intervening arc. Let \(P_n:L^2(\mathbb T)\to V_n\) be orthogonal projection with respect to Lebesgue measure; use its continuous finite-rank kernel to regard it also as an operator \(L^\infty(\mathbb T)\to L^\infty(\mathbb T)\).

Put
\[
q=2-\sqrt3,\qquad u=-q,\qquad
 g_{n,j}=\frac{u^j+u^{n-j}}{2\sqrt3\,(1-u^n)},\quad 0\le j\le n,
\]
with cyclic indexing \(g_{n,n}=g_{n,0}\). Define the elementary function
\[
H(a,b)=
\begin{cases}
 (|a|+|b|)/2,&ab\ge0,\\[2pt]
 (a^2+b^2)/(2(|a|+|b|)),&ab<0.
\end{cases}
\]
Then the **sharp operator norm** is exactly
\[
\boxed{\Lambda_n:=\|P_n\|_{L^\infty\to L^\infty}
=6\sum_{j=0}^{n-1}H(g_{n,j},g_{n,j+1}).}
\]
The formula is computable in \(O(n)\) arithmetic operations from \(q\). It gives, for instance,
\[
\Lambda_3=\frac{16}{9},\quad
\Lambda_4=\frac{17}{9},\quad
\Lambda_5=\frac{257}{132},\quad
\Lambda_6=\frac{2923}{1485}.
\]

For all \(n\ge3\) the finite-circle constant satisfies \(1<\Lambda_n<2\). More precisely, putting \(m=\lfloor n/2\rfloor\) and
\[
c_*=\frac{3(7q-1)}{32\sqrt3}>0,
\]
one has the **uniform two-sided finite-size defect bound**
\[
\boxed{c_*q^m\le 2-\Lambda_n\le4q^m.}
\]
In particular the geometric rate is exact:
\[
\boxed{\lim_{n\to\infty}(2-\Lambda_n)^{1/n}
=\sqrt{2-\sqrt3}.}
\]
The supremum in the operator norm is attained in \(L^\infty\) by choosing the sign of the projection kernel at any fixed knot (arbitrary values at its zeros). The maximizing output locations include all knots. No assertion is made about uniqueness of those locations.

## Assumptions and scope

All functions are real-valued (the same upper norm holds for complex inputs). The measure on the circle is normalized Lebesgue measure, arcs have common length \(1/n\), and the spline space has periodic continuity. The integer restriction \(n\ge3\) avoids the degenerate two-node cycle convention. The sharpness statement uses all measurable inputs of essential supremum at most one; the supremum over continuous inputs has the same value by continuous approximation to a bounded sign function in the kernel integral.

This is an exact finite-dimensional uniform-mesh theorem, not an arbitrary-knot estimate and not a theorem about nonperiodic intervals or multivariate splines. Its primary mathematical setting is spline approximation (MSC2020 41A15).

## Proof

**1. Normal equations and the inverse Gram row.** Write \(\phi_j\) for the periodic nodal hat, so \(\phi_j(k/n)=\delta_{jk}\). Its Gram matrix is \(G=(6n)^{-1}A\), where \(A=4I+S+S^{-1}\), with \(S\) the cyclic shift on \(n\) coordinates. Indeed, each diagonal overlap is \(2/(3n)\), and each adjacent overlap is \(1/(6n)\). The formula also applies when \(n=3\): each pair of distinct hats meets along exactly one short arc. The matrix is strictly positive definite, since
\[
 z^*Az=\sum_{j=0}^{n-1}\bigl(4|z_j|^2+2\operatorname{Re}(\overline{z_j}z_{j+1})\bigr)\ge2\sum_j|z_j|^2.
\]
On the infinite integer lattice, \(A_\infty=4I+S+S^{-1}\) has inverse Green coefficients \(h_j=u^{|j|}/(2\sqrt3)\). They satisfy \(4h_j+h_{j-1}+h_{j+1}=\mathbf1_{j=0}\), because \(u^2+4u+1=0\). Periodizing this absolutely summable sequence produces the inverse row on the circle,
\[
 g_{n,j}=\sum_{\ell\in\mathbb Z}h_{j+\ell n}
 =\frac{u^j+u^{n-j}}{2\sqrt3(1-u^n)}
\quad(0\le j\le n).
\]

**2. The exact norm and its attainment.** The evaluation kernel at knot zero is
\[
 K_n(0,y)=6n\sum_{j=0}^{n-1}g_{n,j}\phi_j(y).
\]
Put \(s=ny\), so on the normalized \(j\)-th arc this kernel is \(6n[(1-t)g_{n,j}+t g_{n,j+1}]\) with \(t=s-j\in[0,1]\). The elementary identity
\[
 \int_0^1|(1-t)a+tb|\,dt=H(a,b)
\]
therefore gives the displayed exact norm formula for evaluation at a knot. At every interior point of an arc, the evaluation kernel is the same convex combination of the two endpoint kernels; convexity of its \(L^1\) norm shows that no interior output location has larger sensitivity. Translation invariance makes the nodal norm the same at every knot. Choosing \(f(y)=\operatorname{sgn}K_n(0,y)\) realizes equality in the integral. Since constants are preserved, \(\Lambda_n\ge1\), and the negative part of the nodal kernel (visible from the alternating inverse row) has positive measure, giving \(\Lambda_n>1\).

**3. Strict upper bound and a sharp-rate upper defect estimate.** Work in unit mesh coordinates on \(\mathbb R\). The nonperiodic nodal kernel is the piecewise-linear function
\[
 k(j+t)=6[(1-t)h_j+t h_{j+1}],\quad j\in\mathbb Z,\;0\le t\le1.
\]
For \(j\ge0\), its cellwise absolute integral equals
\[
 \frac{6}{2\sqrt3}q^j\frac{1+q^2}{2(1+q)}.
\]
Both half-lines contribute equally. Summing the geometric series and using \((1+q^2)/(1-q^2)=2/\sqrt3\) yields
\[
 \int_{\mathbb R}|k(x)|\,dx=2,
 \qquad\int_{|x|\ge m}|k(x)|\,dx=2q^m
 \quad(m\in\mathbb N).
\]
The periodic knot kernel in unit coordinates is the absolutely convergent periodization \(K_n^*(x)=\sum_{\ell\in\mathbb Z}k(x+\ell n)\). Hence \(\Lambda_n=\int_0^n|K_n^*(x)|\,dx\le2\). Choosing the central fundamental domain \([-n/2,n/2]\), the reverse triangle inequality gives
\[
 \Lambda_n\ge\int_{-n/2}^{n/2}|k|-
 \int_{-n/2}^{n/2}\sum_{\ell\ne0}|k(x+\ell n)|\,dx
 \ge2-2\int_{|x|\ge n/2}|k(x)|\,dx
 \ge2-4q^m.
\]

**4. A quantitative strictness witness and the sharp exponent.** For every \(x\), write
\[
 D_n(x)=\sum_{\ell\in\mathbb Z}|k(x+\ell n)|-
 \left|\sum_{\ell\in\mathbb Z}k(x+\ell n)\right|.
\]
It is periodic, nonnegative, and \(\int_0^nD_n=2-\Lambda_n\). If two terms have opposite signs, then \(D_n(x)\) is at least twice their smaller absolute value; all other terms can only increase the total positive or negative mass.

For \(n=2m\), choose \(x=m+t\) with \(3/8\le t\le5/8\). The two contributions \(k(x)\) and \(k(x-n)\), after multiplying by the common sign \((-1)^m\), are respectively
\[
 \frac6{2\sqrt3}q^m[(1-t)-qt],
 \qquad
 \frac6{2\sqrt3}q^m[(1-t)-t/q].
\]
They have opposite signs throughout the indicated interval. Both absolute values are at least \(\frac6{2\sqrt3}q^m(3-5q)/8\); integrating yields
\[
 2-\Lambda_{2m}\ge \frac{3(3-5q)}{16\sqrt3}q^m.
\]

For \(n=2m+1\), take \(x=m+t\), \(0\le t\le1/8\). The corresponding two terms, after the same common sign, are
\[
 \frac6{2\sqrt3}q^m[(1-t)-qt],
 \qquad
 \frac6{2\sqrt3}q^m[-q(1-t)+t].
\]
Their signs are opposite because \(q>1/7\). The smaller absolute value is at least \(\frac6{2\sqrt3}q^m(7q-1)/8\). Thus
\[
 2-\Lambda_{2m+1}\ge\frac{3(7q-1)}{32\sqrt3}q^m.
\]
The even-case coefficient is larger than the latter constant, so the announced uniform lower bound follows. It proves \(\Lambda_n<2\). Taking \(n\)-th roots between the two fixed positive multiples of \(q^{\lfloor n/2\rfloor}\) proves the sharp geometric rate.

## Verification

The standalone `check.py` recomputes the finite inverse Gram rows by exact-rational Gauss–Jordan elimination for each \(3\le n\le28\), checks the cyclic inverse equations and reflection symmetry, compares the result to the closed-form inverse row at high precision, evaluates the exact piecewise kernel integral, tests the two-sided defect inequalities, verifies parity-dependent adjacent signs, and matches the four listed small-\(n\) fractions. It makes 1,722 assertions and passes. This finite replay is supplementary; all quantifiers and the limiting rate are proved in the preceding four steps.

## Relationship to prior work

General spline orthoprojection theory provides mesh-independent \(L^\infty\) stability estimates, and Passenbrunner establishes uniform boundedness for periodic splines with arbitrary knots. The present theorem treats the strict finite-size improvement and optimal exponential convergence rate on *uniform finite circles*, using an explicit inverse circulant Gram matrix and cancellation between periodized Green kernels. A uniform bi-infinite piecewise-affine spline projector has endpoint norm exactly \(2\), but this equality alone does not determine the finite-circle defect or its optimal rate.

The literature review distinguished endpoint operator norms from Hilbert-space contraction, cyclic Fourier multipliers, and nonperiodic arbitrary-knot bounds. The finite periodic formula and the geometric lower bound are not stated in the primary works inspected. This is a bounded literature comparison, not a historical priority guarantee.

## Limitations

The theorem gives neither an exact closed elementary expression without the finite sum for arbitrary \(n\), nor the leading parity-dependent multiplicative constants in the exponential defect; it proves their two-sided nonzero envelopes. It does not classify every maximizing output point, nor assert monotonicity of \(\Lambda_n\) in \(n\). It does not apply to graded meshes. Earlier equivalent computations might exist in older periodic B-spline or circulant-matrix literature; independent bibliographic checking remains necessary.

## References

- Alexander Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first public version 2004-08-30. For the classical arbitrary-knot linear-spline stability constant and its history.
- Peter Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first public version 2006-11-19. For the dimensional distinction in maximum-norm stability and the nodal mass-matrix framework.
- Markus Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720, first public version 2016-08-24. For arbitrary-knot periodic orthoprojection boundedness and localization arguments.
