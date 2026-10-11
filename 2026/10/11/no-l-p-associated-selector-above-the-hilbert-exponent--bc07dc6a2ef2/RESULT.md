# No \(L_p\)-associated selector above the Hilbert exponent
## Finding
Let \(d\ge2\) and
\[
2<p<\infty.
\]
For convex bodies in \(\mathbb R^d\), define the support-function metric
\[
\rho_p(A,B)
=
\left(
\int_{S^{d-1}}
|h_A(u)-h_B(u)|^p\,d\mu(u)
\right)^{1/p},
\]
where \(\mu\) is normalized spherical measure.

There is no selector
\[
s:\mathcal K_0^d\longrightarrow\mathbb R^d
\]
which is equivariant under Euclidean isometries and associated with \(\rho_p\): whenever an isometric copy \(f(A)\) is \(\rho_p\)-nearest to \(B\), one cannot have
\[
s(f(A))=s(B)
\]
for every pair \(A,B\). Consequently no such selector exists on the larger family \(\mathcal K^d\) either.

The obstruction can be witnessed by one smooth strictly convex body. Write
\[
x=u_1,
\]
and define on \(S^{d-1}\)
\[
H_2(u)=x^2-\frac1d,
\qquad
H_3(u)=x^3-\frac{3x}{d+2}.
\]
For every sufficiently small nonzero \(\varepsilon\),
\[
h_\varepsilon(u)
=
1+\varepsilon\bigl(H_2(u)+H_3(u)\bigr)
\]
is the support function of a smooth strictly convex body \(X_\varepsilon\).

If \(x_R\) is the unique translation minimizing the \(\rho_p\)-distance from a radius-\(R\) ball to \(X_\varepsilon\), then
\[
x_R
=
-\frac{6(p-2)(d-1)}{(d+2)^2(d+4)}
\frac{\varepsilon^2}{R}\,e_1
+
O(R^{-2}).
\]
The leading coefficient is nonzero for every \(d\ge2\), \(p>2\), and \(\varepsilon\ne0\). Hence the nearest translated ball has a radius-dependent center.

This gives a negative answer, for every \(d\ge2\) and every finite \(p>2\), to the selector question posed as Problem 13 in the 2009 Banach Center Open Problem Session.

## Assumptions and scope
The family \(\mathcal K_0^d\) consists of compact convex subsets of \(\mathbb R^d\) with nonempty interior, and \(\mathcal K^d\) denotes the family of all nonempty compact convex subsets.

Multiplying the spherical measure in the definition of \(\rho_p\) by a positive constant does not change nearest isometric copies. We therefore use normalized spherical probability measure \(\mu\).

A selector is required to choose a point of each convex body and to satisfy Euclidean equivariance
\[
s(gK)=g(s(K))
\]
for every Euclidean isometry \(g\). Association with the metric means that every optimal isometric copy satisfies the displayed selector identity.

The theorem covers finite
\[
2<p<\infty.
\]
It does not add a new statement for the Hausdorff endpoint, where nonexistence was already known in the motivating literature. The case \(p=2\) is genuinely different: the Steiner point is an associated selector.

## Proof
We use a perturbation of the Euclidean ball whose first spherical harmonic vanishes but whose squared support function has a nonzero first moment.

Let
\[
H_2(u)=u_1^2-\frac1d,
\qquad
H_3(u)=u_1^3-\frac{3u_1}{d+2}.
\]
These are restrictions of homogeneous harmonic polynomials of degrees \(2\) and \(3\), respectively. Put
\[
f=H_2+H_3,
\qquad
h_\varepsilon=1+\varepsilon f.
\]

For a \(C^2\) function \(h\) on the sphere, strict positivity of
\[
\nabla_S^2 h+h\,g_S
\]
is the standard support-function criterion for a smooth strictly convex body. At \(\varepsilon=0\) this tensor is \(g_S\). Since
\[
\nabla_S^2 f+f\,g_S
\]
is continuous on the compact sphere, there is \(\varepsilon_d>0\) such that
\[
0<|\varepsilon|<\varepsilon_d
\]
makes \(h_\varepsilon\) the support function of a smooth strictly convex body \(X_\varepsilon\).

The first support moment vanishes. Indeed, reflection in any coordinate \(u_j\) for \(j>1\) kills the corresponding component. For the first component, the standard spherical moments are
\[
\mathbb E[u_1^2]=\frac1d,
\qquad
\mathbb E[u_1^4]=\frac{3}{d(d+2)}.
\]
Hence
\[
\mathbb E[u_1H_2]=0
\]
by parity and
\[
\mathbb E[u_1H_3]
=
\frac{3}{d(d+2)}
-
\frac3{d+2}\frac1d
=
0.
\]
Therefore
\[
\int_{S^{d-1}}u\,h_\varepsilon(u)\,d\mu(u)=0,
\]
so the Steiner point of \(X_\varepsilon\) is the origin.

The second support moment does not vanish. Using also
\[
\mathbb E[u_1^6]
=
\frac{15}{d(d+2)(d+4)},
\]
one obtains
\[
\begin{aligned}
\mathbb E[u_1H_2H_3]
&=
\mathbb E\left[
u_1^6
-
\left(\frac1d+\frac3{d+2}\right)u_1^4
+
\frac{3}{d(d+2)}u_1^2
\right]\\
&=
\frac{6(d-1)}
{d(d+2)^2(d+4)}.
\end{aligned}
\]
Parity eliminates the \(H_2^2\) and \(H_3^2\) contributions to the first component, while coordinate reflections eliminate all other vector components. Consequently
\[
M_\varepsilon
:=
\int_{S^{d-1}}
u\,h_\varepsilon(u)^2\,d\mu(u)
=
\frac{12(d-1)}
{d(d+2)^2(d+4)}
\varepsilon^2 e_1.
\tag{1}
\]

Now fix a radius \(R>0\). Any Euclidean isometric image of the ball \(RB^d\) is a translate
\[
RB^d+x,
\]
because rotations do not change the ball. Its support function is
\[
R+x\cdot u.
\]
Thus the \(p\)-th power of its distance to \(X_\varepsilon\) is
\[
\Phi_R(x)
=
\int_{S^{d-1}}
\left|R+x\cdot u-h_\varepsilon(u)\right|^p\,d\mu(u).
\tag{2}
\]
For \(p>1\), \(\Phi_R\) is coercive and strictly convex in \(x\): scalar strict convexity of
\[
r\longmapsto |r|^p
\]
is strict on a positive-measure set of directions whenever two translation vectors differ. Hence \(\Phi_R\) has a unique minimizer, denoted \(x_R\).

Set
\[
\delta=\frac1R.
\]
Near \((x,\delta)=(0,0)\), the quantity
\[
1+\delta(x\cdot u-h_\varepsilon(u))
\]
is positive. Define
\[
F(x,\delta)
=
\int_{S^{d-1}}
u\,
\frac{
\left(1+\delta(x\cdot u-h_\varepsilon(u))\right)^{p-1}-1
}{\delta}
\,d\mu(u),
\]
with the removable singularity at \(\delta=0\) filled by continuity.

Because
\[
\int u\,d\mu=0,
\]
the equation
\[
F(x,\delta)=0
\]
for positive small \(\delta\) is exactly the first-order condition for (2). At \((0,0)\),
\[
F(0,0)=0
\]
and
\[
D_xF(0,0)
=
\frac{p-1}{d}I.
\]
Therefore the implicit function theorem gives a unique smooth root
\[
x=x(\delta)
\]
near \(0\).

Differentiating in \(\delta\) gives
\[
\partial_\delta F(0,0)
=
\frac{(p-1)(p-2)}2
M_\varepsilon.
\]
Hence
\[
\begin{aligned}
x'(0)
&=
-\left(D_xF(0,0)\right)^{-1}
\partial_\delta F(0,0)\\
&=
-\frac{d(p-2)}2 M_\varepsilon\\
&=
-\frac{6(p-2)(d-1)}
{(d+2)^2(d+4)}
\varepsilon^2 e_1.
\end{aligned}
\tag{3}
\]
Strict convexity makes this local critical point the unique global minimizer. Equations (2)--(3) therefore imply
\[
x_R
=
-\frac{6(p-2)(d-1)}
{(d+2)^2(d+4)}
\frac{\varepsilon^2}{R}e_1
+
O(R^{-2}).
\tag{4}
\]
In particular,
\[
x_R\ne0
\]
for all sufficiently large finite \(R\), while
\[
x_R\longrightarrow0.
\]

Suppose an associated Euclidean-equivariant selector \(s\) existed. Rotational equivariance forces
\[
s(RB^d)=0,
\]
and translation equivariance then gives
\[
s(RB^d+x_R)=x_R.
\]
Because \(RB^d+x_R\) is the unique nearest isometric copy of \(RB^d\) to \(X_\varepsilon\), association with \(\rho_p\) forces
\[
s(X_\varepsilon)=x_R
\]
for every sufficiently large \(R\).

Letting \(R\to\infty\) would give
\[
s(X_\varepsilon)=0.
\]
But (4) says
\[
x_R\ne0
\]
for all sufficiently large finite \(R\), contradicting
\[
s(X_\varepsilon)=x_R.
\]
Thus no associated equivariant selector exists on \(\mathcal K_0^d\). A selector on \(\mathcal K^d\) would restrict to one on \(\mathcal K_0^d\), so none exists there either.

## Verification
The supplied `verify.py` uses exact symbolic arithmetic to check the spherical-moment calculation, the first-harmonic cancellation, the nonzero vector in (1), and the coefficient in (3)--(4).

It also specializes the construction to \(d=2\), where
\[
H_2(\theta)=\frac12\cos(2\theta),
\qquad
H_3(\theta)=\frac14\cos(3\theta),
\]
and verifies the explicit curvature density
\[
h_\varepsilon+h_\varepsilon''
=
1-\frac32\varepsilon\cos(2\theta)-2\varepsilon\cos(3\theta).
\]
Thus, for example,
\[
|\varepsilon|<\frac27
\]
already gives strict convexity in the planar witness family.

The checker is not used to infer the universal nonexistence theorem from samples. Coercivity, strict convexity, the implicit-function argument, and the selector contradiction are analytic.

## Relationship to prior work
Herburt and Moszyńska define the \(L_p\) support-function metrics and optimal Euclidean isometries. Their 2009 paper recalls Arnold's \(p=2\) theorem, where the Steiner points of an optimal copy and target coincide, and proves that no associated Euclidean-equivariant selector exists for the Hausdorff metric.

The Open Problem Session in the same volume then asks specifically whether an associated Euclidean-equivariant selector exists for
\[
p>2.
\]
The present theorem gives a negative answer for every finite \(p>2\) and every dimension \(d\ge2\).

Later work by Bogdewicz, Herburt, and Moszyńska studies quotient metrics on convex-body hyperspaces, while Moszyńska and Saorín Gómez introduce another Euclidean-equivariant selector, the kernel center. The inspected statements do not claim association of that selector with \(\rho_p\), nor do they settle the \(p>2\) optimal-isometry problem.

The mechanism here is also statement-level distinct from the earlier Hausdorff obstruction. It uses the radius dependence of the unique \(L_p\)-optimal translation of large Euclidean balls. The factor
\[
p-2
\]
in (3) explains why this obstruction vanishes exactly at the Hilbert exponent, consistent with the known \(p=2\) Steiner-point theorem.

Targeted searches for the problem wording, \(\rho_p\)-associated selectors, optimal \(L_p\) translations of balls, and equivalent support-function formulations did not locate a published resolution.

## Limitations
The theorem treats finite
\[
p>2.
\]
It does not provide a new proof of the already known Hausdorff-metric endpoint.

No quantitative lower bound on the failure of a hypothetical selector is asserted beyond the explicit large-radius drift in (4).

The perturbation size required for strict convexity is left existential in general dimension, although the planar family has the explicit sufficient condition
\[
|\varepsilon|<\frac27.
\]

Historical indexing is incomplete. An unindexed later resolution of the 2009 problem remains a residual originality risk.

## References
1. I. Herburt and M. Moszyńska, *Optimal isometries for a pair of compact convex subsets of \(\mathbb R^n\)*, Banach Center Publications 84 (2009), 111--120. DOI: 10.4064/bc84-0-7.
2. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 13. Volume ISBN: 978-83-86806-03-4.
3. A. Bogdewicz, I. Herburt, and M. Moszyńska, *Quotient metrics with applications in convex geometry*, Beiträge zur Algebra und Geometrie 53 (2012), 379--397. DOI: 10.1007/s13366-011-0082-2.
4. M. Moszyńska and E. Saorín Gómez, *On the kernel center of a convex body*, Beiträge zur Algebra und Geometrie 55 (2014), 595--602. DOI: 10.1007/s13366-013-0176-0.
