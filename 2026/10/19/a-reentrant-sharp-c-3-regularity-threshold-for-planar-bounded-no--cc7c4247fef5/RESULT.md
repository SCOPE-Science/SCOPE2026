# A reentrant sharp \(C^3\)-regularity threshold for planar bounded-noise attractors

## Finding

Consider the planar uncertain linear recurrence \(z_{j+1}=Lz_j+\xi_j\), where \(L=\operatorname{diag}(a,b)\), \(0<b<a<1\), and every disturbance \(\xi_j\) ranges over the entire closed Euclidean disk \(\varepsilon D\), with \(\varepsilon>0\). Denote by \(K\) the unique nonempty compact set satisfying \(K=LK+\varepsilon D\). Then \(\partial K\) is always a regular \(C^2\) closed curve, and

\[
\boxed{\partial K\in C^3\quad\Longleftrightarrow\quad 0<b<a^3\;\;\text{or}\;\;a^{3/2}<b<a.}
\]

In the entire closed intermediate band \(a^3\le b\le a^{3/2}\), \(\partial K\) is not \(C^3\) precisely at the two vertical-normal points, and is real-analytic at every other point. Here \(C^k\) means the existence of a regular \(C^k\) local arclength chart, not smoothness of its possibly singular inverse Gauss map.

There is also a sharp change of curvature at the vertical-normal points:

\[
\kappa_{\mathrm{vertical}}=
\begin{cases}
0,&b\le a^2,\\
(1-a^2/b)/\varepsilon,&b>a^2,
\end{cases}
\qquad
\kappa_{\mathrm{horizontal}}=(1-b^2/a)/\varepsilon.
\]

Thus changing only the smaller contraction factor \(b\), while keeping \(a\) fixed, first destroys and then restores \(C^3\) regularity. These statements apply to all permitted real parameters, including the three equality thresholds.

## Assumptions and scope

The disturbance support is exactly \(\varepsilon D\); no fixed realization, distributional density, or probabilistic independence is required for the invariant-set calculation. The map \(L\) is diagonal with positive eigenvalues and \(0<b<a<1\); rotations, nonnormal matrices, nonspherical disturbances, and higher dimensions are not covered. The set is taken in the Euclidean plane and its boundary regularity is in the embedded-curve sense. Since \(a<1\), the set-valued map \(S\mapsto LS+\varepsilon D\) is a Hausdorff contraction on nonempty compact sets and therefore has exactly one global attracting fixed set. Its explicit expression is the convergent Minkowski series

\[
K=\varepsilon\sum_{n=0}^{\infty}\operatorname{diag}(a^n,b^n)D.
\]

## Proof

**1. Support functions and curvature radii.** Write an outward normal as \(\nu(\theta)=(\cos\theta,\sin\theta)\) and its counterclockwise unit tangent as \(\tau(\theta)=(-\sin\theta,\cos\theta)\). The support function of the \(n\)-th ellipsoidal summand is

\[
h_n(\theta)=\varepsilon\sqrt{a^{2n}\cos^2\theta+b^{2n}\sin^2\theta}.
\]

The unique support point \(x_n(\theta)\) of that ellipsoid satisfies \(x_n'(\theta)=\rho_n(\theta)\tau(\theta)\), where direct differentiation of \(h_n\) yields the positive radius

\[
\rho_n(\theta)=h_n+h_n''=
\frac{\varepsilon a^{2n}b^{2n}}{(a^{2n}\cos^2\theta+b^{2n}\sin^2\theta)^{3/2}}.
\]

The series of support points \(x(\theta)=\sum_{n\ge0}x_n(\theta)\) converges uniformly because \(\|x_n\|\le\varepsilon a^n\). It parametrizes \(\partial K\) by outward normal: every summand has a unique supporting point and the support face of their infinite Minkowski sum remains a singleton. Set \(\rho(\theta)=\sum_{n\ge0}\rho_n(\theta)\), allowing the value \(+\infty\) at isolated angles. For each \(n\), \(\int_0^{2\pi}\rho_n(\theta)\,d\theta\) is the ellipsoid perimeter, bounded by \(2\pi\varepsilon a^n\). Hence \(\rho\) is integrable and Tonelli's theorem gives, on any oriented normal-angle interval,

\[
x(\theta)-x(\theta_0)=\int_{\theta_0}^{\theta}\rho(u)\tau(u)\,du.
\]

Define signed arclength \(s(\theta)=\int_{\theta_0}^{\theta}\rho(u)\,du\). Since the density is positive and integrable, \(s\) is strictly increasing and continuous, including where \(\rho\) diverges. The composition \(X(s)=x(\theta(s))\) is a regular \(C^1\) arclength chart with \(X'(s)=\tau(\theta(s))\). This holds at singular normal angles by averaging the continuous tangent \(\tau\) against the positive measure \(\rho(u)du\).

**2. The only potentially singular normal angles.** Away from \(\theta=\pi/2\pmod\pi\), the radii and all their derivatives converge locally and geometrically; indeed the \(n\)-th radius is controlled by a multiple of \((b^2/a)^n\). Local complex extension or uniform derivative estimates make the sum real-analytic and strictly positive. Thus \(X\) is analytic there. Near a vertical normal write \(t=\theta-\pi/2\), \(r=a/b>1\), and \(q=a^2/b>0\). An exact calculation gives

\[
\rho(t)=\varepsilon\sum_{n=0}^{\infty}q^n
\left(1+(r^{2n}-1)\sin^2t\right)^{-3/2}.
\tag{1}
\]

This function is even in \(t\), and the two vertical points have identical local regularity. For \(t\ne0\) sufficiently small, choose \(N=\lfloor\log_r(1/|t|)\rfloor\). Separating the sums at \(N\) and using \(q/r^3=b^2/a<1\) yields constants \(c,C>0\), depending only on the fixed parameters, such that

\[
c\sum_{n=0}^{N}q^n\le\rho(t)\le C\sum_{n=0}^{N}q^n.
\tag{2}
\]

The upper bound uses a geometric tail: for \(n>N\), \(\rho_n(t)\le C\varepsilon q^n(r^n|t|)^{-3}\), whose total is at most \(Cq^N\). The lower bound uses \(r^n|t|\le1\) on \(n\le N\). In particular, \(\rho(t)\to\infty\) exactly when \(q\ge1\), or equivalently \(b\le a^2\); if \(q<1\), \(\rho(0)=\varepsilon/(1-q)\). At the horizontal normals the same computation gives \(\rho=\varepsilon/(1-b^2/a)\).

**3. Every boundary is \(C^2\).** At a vertical angle with \(q<1\), continuity of the positive density \(\rho\) follows by dominated convergence. At \(q\ge1\), equation (2) implies \(s(t)/t\to\infty\), hence the inverse angle \(\theta(s)\) has derivative zero at the corresponding arclength point. Elsewhere \(\theta'(s)=1/\rho(\theta(s))\). These derivatives extend continuously across both vertical points (at zero they are assigned zero when \(q\ge1\)). Consequently \(X'(s)=\tau(\theta(s))\) has a continuous derivative, proving \(X\in C^2\). The curvature of this arclength chart is exactly \(\kappa(s)=\theta'(s)=1/\rho(\theta(s))\), including the limiting convention \(1/\infty=0\). This also proves both curvature formulas in the claim.

**4. A necessary and sufficient \(C^3\) test.** Since \(X''(s)=\kappa(s)(-\nu(\theta(s)))\), a regular \(C^2\) arclength curve is \(C^3\) precisely when \(\kappa(s)\) is continuously differentiable. Both \(\rho(t)\) and the curvature \(\kappa(s)\) are even around a vertical point. Therefore any derivative of \(\kappa\) at that point must vanish. We now split into three cases.

*Case \(q<1\), equivalent to \(b>a^2\).* Here \(s(t)\sim\rho(0)t\). Uniform differentiation of (1) is valid when \(qr=a^3/b^2<1\): optimizing each term over \(t\) gives \(\sup_t|\rho_n'(t)|\le C\varepsilon q^nr^n\), a summable majorant. Thus \(\rho\in C^1\), and hence \(\kappa\in C^1\), whenever \(b>a^{3/2}\). Conversely, if \(qr\ge1\), the single term indexed by \(N\) shows

\[
\rho(0)-\rho(t)\ge c q^N,
\qquad
\frac{\rho(0)-\rho(t)}{|s(t)|}\ge c(qr)^N.
\]

The constants are positive for all sufficiently small \(t\). This bound does not tend to zero, even in the equality case \(qr=1\). Since \(\kappa(s)-\kappa(0)\) is positive and comparable to \(\rho(0)-\rho(t)\), the even curvature cannot be differentiable at the vertical point. Thus precisely \(a^2<b\le a^{3/2}\) fails this test.

*Case \(q=1\), equivalent to \(b=a^2\).* Equation (2) gives \(\rho(t)\asymp\log(1/|t|)\) and \(s(t)\asymp t\log(1/|t|)\). Consequently \(\kappa(s)/|s|\asymp[|t|\log^2(1/|t|)]^{-1}\to\infty\), so the even curvature is not differentiable at the vertical point.

*Case \(q>1\), equivalent to \(b<a^2\).* Put \(\alpha=\log(1/a)/\log(a/b)\in(0,1)\). Equation (2) implies \(\rho(t)\asymp|t|^{\alpha-1}\), \(s(t)\asymp\operatorname{sgn}(t)|t|^{\alpha}\), and \(\kappa(s(t))\asymp|t|^{1-\alpha}\). Thus

\[
\frac{\kappa(s(t))}{|s(t)|}\asymp |t|^{1-2\alpha}.
\]

If \(\alpha\ge1/2\), this does not tend to zero, contradicting differentiability of the even curvature. Since \(\alpha\ge1/2\) is equivalent to \(b\ge a^3\), this covers \(a^3\le b<a^2\). If instead \(\alpha<1/2\), then differentiation of (1) away from zero and the per-summand bound \(|\rho_n'(t)|\le C\rho_n(t)/|t|\) imply

\[
\left|\frac{d\kappa}{ds}\right|
=\frac{|\rho'(t)|}{\rho(t)^3}
\le\frac{C}{|t|\rho(t)^2}
\le C|t|^{1-2\alpha}\longrightarrow0.
\]

The same asymptotic shows \(\kappa(s)/s\to0\); therefore the curvature derivative exists at the vertical point, equals zero, and is continuous there. This holds precisely when \(0<b<a^3\).

Combining the cases proves the claimed complete \(C^3\) phase diagram, including both equality boundaries. Every step uses an infinite-series argument, not numerical extrapolation.

## Verification

The included \(\texttt{verify.py}\) is a standalone Python 3 program using only the standard library. It directly checks the curvature-radius formula against centered finite differences of the support function, checks positive finite radii and the exact axis bounds, and numerically checks the perimeter majorant for representative \(a,b\) pairs on both sides of each predicted \(C^3\) phase. Its numerical checks are supplementary; the statements for all real parameters and infinitely many summands are proved above by uniform bounds, Tonelli's theorem, and asymptotic estimates.

## Relationship to prior work

Lamb, Rasmussen and Tey (2023, arXiv:2310.03437v1) prove uniqueness, strict convexity and \(C^1\) boundary smoothness for contracting linear maps with bounded spherical noise, give a normal-map series, and explicitly identify precise smoothness as open (Section 5). The present work uses that geometric setting but supplies a sharper \(C^2\)/\(C^3\) classification for the diagonal two-dimensional subfamily.

Tey's 2022 thesis, Chapter 4.2, treats diagonal maps, gives axis intercepts and establishes non-ellipticity and strict convexity; its Chapter 5 develops curvature mapping for other systems. The inspected parts do not state this eigenvalue phase diagram. Kourliouros et al. (2023, arXiv:2303.01895) prove a conditional persistence theorem assuming \(C^2\) and normal hyperbolicity, rather than establishing the present \(C^2\) property or characterizing its third-derivative failure. Ruan and Chirikjian (2021, arXiv:2012.15461v2) provide parametric formulas for finite Minkowski sums of positively curved bodies. Such formulas provide the finite-sum starting point but do not settle regularity of the infinite Hausdorff limit; positivity of curvature in finite sums does not imply its positivity in this limit.

## Limitations

Only strictly positive diagonal contractions with ordered distinct entries and disk disturbances are classified. The proof does not establish \(C^4\) or higher-regularity phase diagrams, nonlinear persistence, random-measure smoothness, or analogous thresholds for general nonnormal matrices. Literature search and accessible-source comparison cannot prove historical priority exhaustively; an antecedent stated in other terminology may exist. The result is a mathematical statement with an internal proof and supplementary finite tests, not independently audited publication-level certification.

## References

1. J. S. W. Lamb, M. Rasmussen and W. H. Tey, *Attractors of linear maps with bounded noise* (2023), arXiv:2310.03437v1, https://arxiv.org/html/2310.03437v1.
2. W. H. Tey, *On Minimal Invariant Sets of Certain Set-Valued Dynamical Systems: A Boundary Map Approach* (PhD thesis, 2022), Chapter 4.2 and Chapter 5, https://www.researchgate.net/publication/366016533_On_Minimal_Invariant_Sets_of_Certain_Set-Valued_Dynamical_Systems_-_A_Boundary_Map_Approach.
3. K. Kourliouros et al., *Persistence of Minimal Invariant Sets for Certain Set-Valued Dynamical Systems: A Boundary Mapping Approach* (2023), arXiv:2303.01895, https://arxiv.org/abs/2303.01895.
4. S. Ruan and G. S. Chirikjian, *Closed-Form Minkowski Sums of Convex Bodies with Smooth Positively Curved Boundaries* (2021), arXiv:2012.15461v2, https://arxiv.org/html/2012.15461v2.
