# Exact Lipschitz phase diagram of metric projection onto the constant-vector line in real \(\ell_p^n\)
## Finding
Let \(n\ge2\) be an integer, \(1<p<\infty\), and \(I_n=\operatorname{span}\{(1,\ldots,1)\}\subset\ell_p^n(\mathbb R)\). For \(x\in\mathbb R^n\), let \(m_p(x)\) be the unique minimizer of \(\sum_{i=1}^n|x_i-t|^p\) over real \(t\), and write \(P_{n,p}(x)=m_p(x)(1,\ldots,1)\) for the metric projection onto \(I_n\). Then its sharp global Lipschitz constant in the ambient \(\ell_p^n\) norm is
\[
\operatorname{Lip}(P_{n,p})=
\begin{cases}
1,&n=2,\quad 1<p<\infty,\\
n^{1/p},&n\ge3,\quad1<p<2,\\
1,&n\ge3,\quad p=2,\\
(n/2)^{1/p},&n\ge3,\quad2<p<\infty.
\end{cases}
\]
For every fixed \(n\ge3\), the sharp constant is discontinuous at the Hilbert exponent:
\[
\lim_{p\uparrow2}\operatorname{Lip}(P_{n,p})=\sqrt n,
\qquad \operatorname{Lip}(P_{n,2})=1,
\qquad \lim_{p\downarrow2}\operatorname{Lip}(P_{n,p})=\sqrt{n/2}.
\]
In the subquadratic range the sharp constant is witnessed by infinitesimal perturbations of a point with exactly one vanishing residual, and in the superquadratic range it is witnessed by infinitesimal perturbations of the configuration \((1,-1,0,\ldots,0)\). No finite-pair attainment assertion is made.

## Assumptions and scope
All vector spaces and scalars are real. Fix an integer \(n\ge2\) and \(1<p<\infty\). Give \(\mathbb R^n\) the standard \(\ell_p\) norm
\[
\|x\|_p=\left(\sum_{i=1}^n|x_i|^p\right)^{1/p}.
\]
The line of constant vectors is \(I_n=\{t\mathbf1_n:t\in\mathbb R\}\) with \(\mathbf1_n=(1,\ldots,1)\). Strict convexity makes the metric projection
\[
P_{n,p}(x)=m_p(x)\mathbf1_n,
\qquad
m_p(x)=\operatorname*{argmin}_{t\in\mathbb R}\sum_{i=1}^n|x_i-t|^p
\]
well defined. We use the global Lipschitz constant
\[
\operatorname{Lip}(P_{n,p})=
\sup_{x\ne y}\frac{\|P_{n,p}(x)-P_{n,p}(y)\|_p}{\|x-y\|_p}.
\]
No claim is made for complex scalars, for infinite-dimensional non-atomic \(L_p\) spaces, or for projections onto arbitrary subspaces.

## Proof
**Existence, monotonicity, and the universal bound.** Set
\[
\phi_p(s)=\operatorname{sgn}(s)|s|^{p-1},
\qquad \phi_p(0)=0.
\]
Since \(\phi_p\) is continuous and strictly increasing, the strictly convex objective has exactly one critical point, satisfying
\[
\sum_{i=1}^n\phi_p(m_p(x)-x_i)=0.
\tag{1}
\]
Equation (1) implies translation covariance and coordinatewise monotonicity:
\[
m_p(x+c\mathbf1_n)=m_p(x)+c,
\qquad
x_i\le y_i\ (1\le i\le n)\Longrightarrow m_p(x)\le m_p(y).
\]
Indeed, shifting each coordinate up weakly shifts the left side of (1) down at every fixed trial value, so its unique zero cannot move down. Consequently,
\[
|m_p(x)-m_p(y)|\le\|x-y\|_\infty.
\]
Therefore, for all \(1<p<\infty\),
\[
\|P_{n,p}(x)-P_{n,p}(y)\|_p
=n^{1/p}|m_p(x)-m_p(y)|
\le n^{1/p}\|x-y\|_p.
\tag{2}
\]

**Two coordinates and the Hilbert exponent.** If \(n=2\), the symmetry of the strictly convex objective gives
\[
m_p(x)=\frac{x_1+x_2}{2}
\]
for every \(p>1\). This is a linear projection of operator norm exactly one by Hölder's inequality, with equality on constant vectors. If \(p=2\), for every \(n\) the minimizer is the arithmetic mean \(n^{-1}\sum_i x_i\), so \(P_{n,2}\) is the orthogonal projection and has operator norm one.

**Subquadratic sharpness, \(n\ge3\) and \(1<p<2\).** Put
\[
a=(n-2)^{1/(p-1)},
\qquad
x^0=(0,\underbrace{1,\ldots,1}_{n-2\text{ entries}},-a).
\]
Equation (1) gives \(m_p(x^0)=0\), because the nonzero residual powers cancel:
\[
-(n-2)+a^{p-1}=0.
\]
For \(\varepsilon>0\), set \(x^\varepsilon=x^0+\varepsilon e_1\) and \(m_\varepsilon=m_p(x^\varepsilon)\). Monotonicity and translation covariance give \(0\le m_\varepsilon\le\varepsilon\). The root equation becomes
\[
(\varepsilon-m_\varepsilon)^{p-1}=g(m_\varepsilon),
\quad
g(t)=(n-2)\phi_p(t-1)+\phi_p(t+a).
\]
Here \(g(0)=0\) and, since its arguments stay nonzero near zero, \(g\) has a bounded derivative there. Thus for small \(\varepsilon\) one has \(0\le g(m_\varepsilon)\le C\varepsilon\), with a finite constant depending only on \(n,p\). It follows that
\[
0\le\varepsilon-m_\varepsilon\le
C^{1/(p-1)}\varepsilon^{1/(p-1)}=o(\varepsilon),
\]
because \(1/(p-1)>1\). Hence \(m_\varepsilon/\varepsilon\to1\) and
\[
\lim_{\varepsilon\downarrow0}
\frac{\|P_{n,p}(x^\varepsilon)-P_{n,p}(x^0)\|_p}
{\|x^\varepsilon-x^0\|_p}=n^{1/p}.
\]
Together with (2), this proves the sharp subquadratic branch. This is a limiting perturbation; the proof does not assert a maximizing separated pair.

**Superquadratic upper bound, \(n\ge3\) and \(p>2\).** For \(x\notin I_n\) set \(r_i=x_i-m_p(x)\). Since \(p>2\), the implicit function theorem applied to (1) shows that \(m_p\) is differentiable outside \(I_n\), with
\[
Dm_p(x)[h]=\sum_{i=1}^n w_i h_i,
\qquad
w_i=\frac{|r_i|^{p-2}}{\sum_{j=1}^n|r_j|^{p-2}}.
\tag{3}
\]
The residual equation is \(\sum_i\operatorname{sgn}(r_i)|r_i|^{p-1}=0\). For each \(i\), the triangle inequality yields
\[
|r_i|^{p-1}\le\sum_{j\ne i}|r_j|^{p-1}.
\]
Write \(s=(p-2)/(p-1)\in(0,1)\). Concavity/subadditivity of the power \(t^s\) gives
\[
|r_i|^{p-2}\le\left(\sum_{j\ne i}|r_j|^{p-1}\right)^s
\le\sum_{j\ne i}|r_j|^{p-2}.
\]
Thus every weight in (3) satisfies \(0\le w_i\le1/2\), while \(\sum_iw_i=1\). With conjugate exponent \(q=p/(p-1)\),
\[
\|w\|_q^q=\sum_iw_i^q
\le (1/2)^{q-1}\sum_iw_i=2^{1-q},
\qquad
\|w\|_q\le2^{-1/p}.
\]
Hölder's inequality applied to (3) therefore gives
\[
\|DP_{n,p}(x)\|_{\ell_p\to\ell_p}
=n^{1/p}\|w\|_q\le(n/2)^{1/p}.
\tag{4}
\]
The bound passes from derivatives to all pairs by integrating along line segments disjoint from the diagonal \(I_n\). A segment not entirely within \(I_n\) intersects it in at most one point; split at that point and apply continuity of \(P_{n,p}\). On a segment inside \(I_n\), the map is the identity and has Lipschitz constant one, which is at most \((n/2)^{1/p}\) since \(n\ge2\). Therefore the global Lipschitz constant is at most \((n/2)^{1/p}\).

**Superquadratic sharpness.** At the point
\[
x^0=(1,-1,0,\ldots,0),
\]
we have \(m_p(x^0)=0\), and the weights (3) are \((1/2,1/2,0,\ldots,0)\). For the tangent perturbation \(h=(1,1,0,\ldots,0)\),
\[
\frac{\|DP_{n,p}(x^0)[h]\|_p}{\|h\|_p}
=\frac{n^{1/p}}{2^{1/p}}=(n/2)^{1/p}.
\]
This exactly matches the global upper bound. The claimed piecewise formula now follows, including the one-sided limits at \(p=2\).

## Verification
The analytic proof covers every integer \(n\ge2\) and every real exponent \(1<p<\infty\); no finite experiment is used to infer a universal bound. The upper bounds follow from either coordinatewise monotonicity or the exact derivative weights, and sharpness follows from explicit one-parameter perturbations.

A reproducible derivative check for the superquadratic configuration uses \(r=(1,-1,0,\ldots,0)\), so \(w=(1/2,1/2,0,\ldots,0)\). For any \(n\ge3\), the derivative ratio along \(h=(1,1,0,\ldots,0)\) is exactly \((n/2)^{1/p}\). The subquadratic test uses the displayed \(x^0\) and the implicit scalar equation to obtain the exact limit \(m_\varepsilon/\varepsilon\to1\), rather than extrapolation from numerical data.

## Relationship to prior work
Berens, Finzel, Li, and Xu proved uniform Lipschitz continuity of best \(\ell_p\)-approximations onto a fixed finite-dimensional linear subspace, uniformly over the exponent, in their foundational 1997 paper. That result proves existence of finite constants but does not display the sharp constant for the one-dimensional all-ones subspace or the discontinuous exponent profile.

Finzel and Li extended uniform Lipschitz continuity to polyhedral approximation sets in 1998. Its abstract concerns existence of a uniform bound, not a sharp formula for this metric projection. Its complete primary text was unavailable in the checked routes, and possible undiscovered coverage is a residual originality risk.

Borodin, Druzhinin, and Chesnokova (2017), Theorem 2 and its proof, specifically consider the diagonal line \(I_n=\operatorname{span}\{(1,\ldots,1)\}\) and establish the estimate
\[
K(I_n)\le 2^{1/q}(n-1)^{1/p}+1,
\]
where \(q\) is conjugate to \(p\), in the context of an asymptotically best choice of one-dimensional subspace. Their complete article does not determine an exact sharp formula. The result here gives the exact value in all dimensions and exponents and explains a singularity at the Hilbert exponent.

Kapoor and Mathur (1983) determine the maximum *metric projection bound* over arbitrary subspaces of the two-dimensional \(\ell_p\) space, in connection with radial retraction. That distinct supremum does not determine the Lipschitz constant of the specific diagonal-line projection in dimensions \(n\ge3\), and their exact \(p=4\) value is not claimed here.

## Limitations
Only real scalar \(\ell_p^n\) spaces with \(1<p<\infty\) are treated. The constants measure the global Lipschitz behavior of the metric projection onto the **single fixed line** of constant vectors, not the worst metric projection over all subspaces. The lower bounds use infinitesimal perturbations and do not imply a finite pair of distinct points actually attains the supremum. Discontinuity refers to the sharp constant as \(p\) varies with dimension fixed, not discontinuity of each metric projection in its input \(x\).

## References
1. H. Berens, M. Finzel, W. Li, and Y. Xu, “Hoffman's Error Bounds and Uniform Lipschitz Continuity of Best \(\ell_p\)-Approximations,” *Journal of Mathematical Analysis and Applications* 213 (1997), 183–201. DOI 10.1006/jmaa.1997.5521.
2. M. Finzel and W. Li, “Uniform Lipschitz Continuity of Best \(\ell_p\)-Approximations by Polyhedral Sets,” *Journal of Mathematical Analysis and Applications* 228 (1998), 112–118. DOI 10.1006/jmaa.1998.6120.
3. P. A. Borodin, Yu. Yu. Druzhinin, and K. V. Chesnokova, “Finite-Dimensional Subspaces of \(L_p\) with Lipschitz Metric Projection,” *Mathematical Notes* 102 (2017), 465–474. DOI 10.1134/S0001434617090188.
4. O. P. Kapoor and S. B. Mathur, “Metric Projection Bound and the Lipschitz Constant of the Radial Retraction,” *Journal of Approximation Theory* 38 (1983), 66–70. DOI 10.1016/0021-9045(83)90142-9.
