# Euclidean tangent obstructions for complex-order spherical maximal operators on rank-one spaces

## Result

Let \(X=G/K\) be a rank-one Riemannian symmetric space of noncompact type, let
\[
d=\dim X=1+m_1+m_2\ge 2,
\]
and let \(\mathcal M_X^\mu f=\sup_{t>0}|M_t^\mu f|\) be the generalized spherical maximal operator introduced by Dakshi--Pusti. We use their analytically continued family in the range
\[
\operatorname{Re}\mu>-\alpha_0-1=-\frac d2,
\qquad
\alpha_0=\frac{d-2}{2}.
\]

### Theorem

If \(1<p<\infty\), \(\mu\in\mathbb C\), and
\[
\|\mathcal M_X^\mu f\|_{L^p(X)}
\le A\|f\|_{L^p(X)}
\]
for all suitable \(f\), then
\[
\boxed{
\operatorname{Re}\mu\ge
\sigma_d(p,p)
=
\max\left\{
-\frac{d-1}{p},
\ \frac1p-\frac{d-1}{2},
\ 1-d+\frac d p
\right\}.
}
\]
Equivalently,
\[
\operatorname{Re}\mu\ge 1-d+\frac d p
\qquad (1<p\le2),
\]
while for \(2\le p<\infty\),
\[
\boxed{
\operatorname{Re}\mu\ge
\max\left\{
\frac1p-\frac{d-1}{2},
-\frac{d-1}{p}
\right\}.
}
\]

For \(p>2\), the latter condition strictly improves the real-parameter necessary condition
\(\mu>1-d+d/p\) proved in Theorem 1.6 of Dakshi--Pusti, because
\[
\left(\frac1p-\frac{d-1}{2}\right)
-\left(1-d+\frac d p\right)
=(d-1)\left(\frac12-\frac1p\right)>0.
\]
It also applies to complex \(\mu\), whereas their necessary theorem is stated for \(\mu\in\mathbb R\).

The two \(p>2\) obstructions cross at
\[
p=\frac{2d}{d-1}.
\]
Thus the first term dominates for \(2<p\le 2d/(d-1)\), and the second for
\(p\ge 2d/(d-1)\).

For real hyperbolic space this reproduces the \(p>2\) necessary boundary of
Chen--Shen--Wang--Yan. The new point is that the same boundary is forced on every
rank-one noncompact symmetric space, including complex, quaternionic and Cayley
hyperbolic cases, and that the argument gives a real-part obstruction for complex
order.

## Tangent-space transfer principle

The theorem follows from a local blow-up statement.

Let
\[
\mathfrak M_t^\mu f(x)
=
\frac1{\Gamma(\mu)}
\int_{|z|\le1}(1-|z|^2)^{\mu-1}f(x-tz)\,dz
\]
denote the Euclidean complex spherical mean, interpreted by analytic continuation,
and put
\[
\mathfrak M_{[1,2]}^\mu f(x)
=
\sup_{1\le t\le2}|\mathfrak M_t^\mu f(x)|.
\]

### Proposition

If \(\mathcal M_X^\mu\) is bounded on \(L^p(X)\), then
\(\mathfrak M_{[1,2]}^\mu\) is bounded on \(L^p(\mathbb R^d)\).

More precisely, after identifying \(T_oX\) with \(\mathbb R^d\) at a fixed origin
\(o\in X\), for every \(f\in C_c^\infty(\mathbb R^d)\),
\[
M_{\varepsilon t}^\mu F_\varepsilon(\exp_o(\varepsilon x))
\longrightarrow
2^{\mu+1}\mathfrak M_t^\mu f(x)
\]
locally, uniformly for \(t\) in finite subsets of \([1,2]\), where
\[
F_\varepsilon(\exp_o(\varepsilon y))=f(y)
\]
inside a fixed normal-coordinate neighborhood and \(F_\varepsilon\) is extended
smoothly by zero.

Consequently, every \(L^p\) obstruction for the Euclidean single-scale maximal
operator is automatically a necessary obstruction for the full rank-one maximal
operator.

## Proof of the transfer proposition

Dakshi--Pusti define, initially for \(\operatorname{Re}\mu>0\),
\[
M_t^\mu F(x)
=
\frac{C(t,\mu)}{\Gamma(\mu)}
\int_{B(x,t)}
F(y)\bigl(\cosh 2t-\cosh 2d(x,y)\bigr)^{\mu-1}\,d\sigma(y),
\]
where
\[
C(t,\mu)
=
\frac{4e^{2\mu t}}
{\sinh^{\,d-2+2\mu}t\,
 \cosh^{\,2\beta_0+2\mu}t}.
\]

Fix compact sets of \(x,y\) in normal coordinates and \(t\in[1,2]\). Standard
normal-coordinate expansions give
\[
d\!\left(\exp_o(\varepsilon x),\exp_o(\varepsilon y)\right)^2
=
\varepsilon^2|x-y|^2+O(\varepsilon^4),
\]
and
\[
d\sigma(\exp_o(\varepsilon y))
=
\varepsilon^d(1+O(\varepsilon^2))\,dy.
\]
Also
\[
C(\varepsilon t,\mu)
=
4\varepsilon^{-(d-2+2\mu)}
t^{-(d-2+2\mu)}(1+o(1)),
\]
while
\[
\cosh(2\varepsilon t)
-\cosh\!\left(2d(\exp_o(\varepsilon x),\exp_o(\varepsilon y))\right)
=
2\varepsilon^2
\bigl(t^2-|x-y|^2+O(\varepsilon^2)\bigr).
\]
Hence, when \(\operatorname{Re}\mu>0\), dominated convergence yields
\[
\begin{aligned}
M_{\varepsilon t}^\mu F_\varepsilon(\exp_o(\varepsilon x))
&\longrightarrow
\frac{2^{\mu+1}}{\Gamma(\mu)}
t^{-(d-2+2\mu)}
\int_{|x-y|<t}
(t^2-|x-y|^2)^{\mu-1}f(y)\,dy\\
&=
2^{\mu+1}\mathfrak M_t^\mu f(x).
\end{aligned}
\]

The same convergence holds throughout the analytically continued range. Indeed,
the one-variable distribution
\[
u_\mu(s)=\frac{s_+^{\mu-1}}{\Gamma(\mu)}
\]
is entire in \(\mu\), with
\[
\partial_s^k u_{\mu+k}=u_\mu.
\]
For a fixed \(\mu\), choose \(k\) with \(\operatorname{Re}(\mu+k)>0\).
The defining functions of the ball boundaries converge smoothly and are
submersions there; integrating by parts \(k\) times reduces the claim to the
positive-real-part case. By uniqueness of analytic continuation, this agrees with
the Dakshi--Pusti multiplier continuation.

Now let \(E\subset[1,2]\) be finite. The assumed maximal inequality gives
\[
\left\|
\max_{t\in E}
|M_{\varepsilon t}^\mu F_\varepsilon|
\right\|_{L^p(X)}
\le A\|F_\varepsilon\|_{L^p(X)}.
\]
After restricting to a normal-coordinate neighborhood containing the Euclidean
output support, changing variables, using Fatou's lemma and cancelling the common
factor \(\varepsilon^{d/p}\), we obtain
\[
|2^{\mu+1}|
\left\|
\max_{t\in E}|\mathfrak M_t^\mu f|
\right\|_{L^p(\mathbb R^d)}
\le A\|f\|_{L^p(\mathbb R^d)}.
\]
Take an increasing sequence of finite subsets dense in \([1,2]\). For
\(f\in C_c^\infty\), \(t\mapsto\mathfrak M_t^\mu f(x)\) is continuous for
\(t>0\), also for analytically continued orders. Monotone convergence therefore
gives the \(L^p\) bound for \(\mathfrak M_{[1,2]}^\mu\).

## Euclidean obstruction

Liu--Shen--Song--Yan proved that if the Euclidean single-scale maximal operator
maps \(L^p(\mathbb R^d)\) to \(L^q(\mathbb R^d)\), then \(q\ge p\) and
\[
\operatorname{Re}\mu\ge
\sigma_d(p,q)
=
\max\left\{
\frac1p-\frac d q,\
\frac{d+1}{2p}-\frac{d-1}{2}\left(\frac1q+1\right),\
\frac d p-d+1
\right\}.
\]
Setting \(q=p\) gives precisely
\[
\sigma_d(p,p)
=
\max\left\{
-\frac{d-1}{p},\
\frac1p-\frac{d-1}{2},\
1-d+\frac d p
\right\}.
\]
For \(p\le2\), the third term dominates. For \(p\ge2\), the third term is no
larger than the second, leaving the two-term maximum stated above.

## Relation to recent work

Dakshi--Pusti's September 2026 preprint extends complex-order spherical maximal
operators from real hyperbolic space to every rank-one noncompact symmetric space.
Their Theorem 1.5 proves the sufficient ranges
\[
\operatorname{Re}\mu>1-d+\frac d p
\quad(1<p\le2),
\qquad
\operatorname{Re}\mu>\frac{2-d}{p}
\quad(2\le p\le\infty),
\]
while Theorem 1.6 gives only the real-parameter necessity
\[
\mu>1-d+\frac d p.
\]
Their Remark 3.7 explicitly identifies the \(p>2\) range as a direction for further
investigation.

For real hyperbolic space, Chen--Shen--Wang--Yan had already found the two
\(p>2\) necessary obstructions
\[
\alpha\ge
\max\left\{
\frac1p-\frac{d-1}{2},
-\frac{d-1}{p}
\right\}.
\]
The tangent-space argument explains why these two obstructions are not specifically
real-hyperbolic: they are Euclidean and therefore survive on every rank-one space.
The root multiplicities \(m_1,m_2\) disappear from the obstruction except through
the total dimension \(d\).

Ghosh--Liu--Rozendaal--Song developed local and variable-coefficient spherical
maximal estimates, including complex Euclidean means and ordinary geodesic spheres
on compact manifolds. Their work supports the general principle that small-scale
spherical maximal behavior is local/Fourier-integral in nature, but it does not
state the present \(L^p\) necessary region for the Dakshi--Pusti complex-order
family on arbitrary rank-one noncompact symmetric spaces.

## Limitations

1. The result is necessary only. For \(p>2\) it narrows, but does not close, the
   gap to the Dakshi--Pusti sufficient condition
   \(\operatorname{Re}\mu>(2-d)/p\).
2. At \(1<p\le2\), the transfer gives the non-strict boundary
   \(\operatorname{Re}\mu\ge1-d+d/p\); Dakshi--Pusti obtain a strict inequality
   for real \(\mu\). No complex endpoint claim is made here.
3. No assertion is made for \(p=\infty\), endpoint weak type, lacunary maximal
   operators, or higher-rank symmetric spaces.
4. The tangent-space transfer mechanism is classical in spirit. The originality
   claim concerns its application to the newly introduced general rank-one family,
   the resulting all-rank-one \(p>2\) necessary boundary, and the complex-order
   real-part obstruction.

## References

1. S. Dakshi and S. Pusti, *Spherical maximal operators on rank one Riemannian
   symmetric spaces of noncompact type*, arXiv:2609.15514 (2026).
   https://arxiv.org/abs/2609.15514
2. N. Liu, M. Shen, L. Song and L. Yan, *\(L^p\to L^q\) Estimates for Stein's
   Spherical Maximal Operators*, Analysis in Theory and Applications 42 (2026),
   90--108; arXiv:2502.09030.
   https://arxiv.org/abs/2502.09030
3. P. Chen, M. Shen, Y. Wang and L. Yan, *The Spherical Maximal Operators on
   Hyperbolic Spaces*, Journal of Geometric Analysis 35 (2025), Paper 373;
   arXiv:2408.02180.
   https://arxiv.org/abs/2408.02180
4. A. Ghosh, N. Liu, J. Rozendaal and L. Song, *Spherical maximal functions and
   Hardy spaces for Fourier integral operators*, Journal of Geometric Analysis
   36 (2026), Paper 250; arXiv:2401.16955.
   https://arxiv.org/abs/2401.16955
