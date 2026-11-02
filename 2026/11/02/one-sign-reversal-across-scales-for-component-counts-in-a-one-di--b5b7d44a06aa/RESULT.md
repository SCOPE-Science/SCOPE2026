# One sign reversal across scales for component counts in a one-dimensional random geometric graph

## Finding
Let \(n\geq3\) points be independent and uniform on \([0,1]\). For \(0<t<1\), let \(K_n(t)\) be the number of components in the graph connecting pairs at distance at most \(t\). For all \(0<r\leq s<1\),
\[
\operatorname{Cov}(K_n(r),K_n(s))=(n-1)(1-s)^n\big[1-(n-1)(1-r)^n\big]+(n-1)(n-2)(1-r-s)_+^n,
\]
where \(x_+=\max\{x,0\}\). Set \(r_0(n)=1-(n-1)^{-1/n}\).

If \(r>r_0(n)\), the covariance is strictly positive at every \(s\in[r,1)\). If \(r=r_0(n)\), it is strictly positive for \(r\leq s<1-r\) and exactly zero for \(1-r\leq s<1\). If \(0<r<r_0(n)\), there is **exactly one** root \(s_*(n,r)\in(r,1-r)\): the covariance is positive for \(r\leq s<s_*\), zero at \(s_*\), and negative for \(s_*<s<1\). The root is explicit:
\[
u=\left(\frac{(n-1)(1-r)^n-1}{n-2}\right)^{1/n},\qquad s_*(n,r)=1-\frac{r}{1-u}.
\]
For example, the covariance at \(n=3\), \(r=2/25\), and \(s=7/10\) is \(-17192/1953125\), despite the pointwise monotonicity \(K_n(s)\leq K_n(r)\).

At sparse radii \(r_n=c/n\), \(s_n=d/n\) with fixed \(0<c\leq d\),
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n(c/n),K_n(d/n))}{n}=e^{-d}\big[1-e^{-c}(1+cd)\big].
\]
The asymptotic sign changes at \(d_*(c)=(e^c-1)/c>c\), and the finite exact crossing satisfies \(n s_*(n,c/n)\to d_*(c)\). Also \(r_0(n)\sim (\log n)/n\).

## Assumptions and scope
The sample size is fixed, not Poisson distributed; all positions are i.i.d. uniform on the closed unit interval, with ties of probability zero. The graph is an ordinary undirected Euclidean-radius graph on this interval, not a circle and not an independent-edge Erdős–Rényi graph. The strict sign classification holds for every integer \(n\geq3\) and real thresholds \(0<r\leq s<1\). At equality with either displayed threshold the stated zero cases are included. The sparse limit assumes fixed \(c,d\) independent of \(n\) and applies to sufficiently large \(n\) so that the radii lie below one.

## Proof
Write the order statistics as \(X_{(1)}<\dots<X_{(n)}\), and define all \(n+1\) spacings, including the two outer spacings. The full spacing vector is uniform on the standard \(n\)-simplex, equivalently Dirichlet with all \(n+1\) parameters equal to one. Its \(n-1\) internal coordinates \(D_i=X_{(i+1)}-X_{(i)}\) determine graph components by
\[
K_n(t)=1+\sum_{i=1}^{n-1}{\bf1}\{D_i>t\}.
\]
Uniform-simplex volume translation gives, for any distinct spacing coordinates and nonnegative \(a,b\),
\[
\Pr(D_i>a)=(1-a)_+^n,\qquad
\Pr(D_i>a,D_j>b)=(1-a-b)_+^n.
\]
For \(r\leq s\), the same coordinate contributes \(\Pr(D_i>r,D_i>s)=(1-s)^n\). Therefore the diagonal terms of the covariance sum contribute \((n-1)[(1-s)^n-(1-r)^n(1-s)^n]\), and distinct-coordinate terms contribute \((n-1)(n-2)[(1-r-s)_+^n-(1-r)^n(1-s)^n]\). Collecting terms yields the claimed exact identity.

Divide the identity by the strictly positive factor \((n-1)(1-s)^n\). Its sign becomes the sign of
\[
B_{n,r}(s)=1-(n-1)(1-r)^n+(n-2)\left(\frac{(1-r-s)_+}{1-s}\right)^n.
\]
For \(s<1-r\), the ratio equals \(1-r/(1-s)\), strictly decreasing in \(s\); it is zero for \(s\geq1-r\). At \(s=r\), \(B_{n,r}(r)>0\) because it represents \(\operatorname{Var}(K_n(r))\) divided by a strictly positive factor. This variance is strictly positive: for every \(0<r<1\), positive-probability configurations exhibit one connected cluster, and others exhibit two clusters separated by more than \(r\). At \(s\geq1-r\) the sign is that of \(1-(n-1)(1-r)^n\). This expression vanishes precisely at \(r=r_0(n)\); moreover \(r_0(n)<1/2\). Strict decrease until \(1-r\) establishes the three sign regimes and uniqueness. Solving \(B_{n,r}(s)=0\) yields the displayed \(u\) and \(s_*\).

For sparse scales, use \((1-z/n)^n=e^{-z}[1-z^2/(2n)+O(n^{-2})]\) for fixed \(z\). In the independent-coordinate covariance form, the diagonal contribution per \(n\) tends to \(e^{-d}(1-e^{-c})\), while the distinct-coordinate term per \(n\) tends to \(-cd e^{-(c+d)}\). Adding proves the limiting formula. Its sign changes at \(d=(e^c-1)/c\). The latter exceeds \(c\) because \(e^c>1+c^2\) for every \(c>0\). Since the finite normalized sign function is strictly decreasing on its nonconstant interval, and its value at \(d/n\) tends to a strictly positive or negative limit on either side of \(d_*(c)\), its unique crossing satisfies \(ns_*(n,c/n)\to d_*(c)\). Finally \(r_0(n)=1-\exp[-\log(n-1)/n]\sim\log n/n\).

## Verification
The standalone standard-library program `verify.py` replays the exact simplex event-pair expression against the collected covariance identity for many rational parameters; tests the sign and normalized monotonicity, checks the negative rational example, and compares fixed sparse-scale values with the proved limit. The actual verification run returned `VERIFY_OK exact_or_asymptotic_assertions=21421`. These finite computations are checks, not a replacement for the uniform-in-parameters proof above.

## Relationship to prior work
Decreusefond and Ferraz examine the distribution of the number of components in one-dimensional **Poisson** random geometric graphs at a fixed radius, including one-radius moments; their source does not derive a fixed-number-of-points covariance across two radii or its one-switch classification. Classical empirical-process work on uniform spacings, including Einmahl and van Zuijlen, provides relevant background for large-sample threshold counts and could imply part of the sparse-limit covariance. The finite-sample all-radius sign regimes and exact zero curve are the assessed contribution; standard Dirichlet marginal and pairwise survival formulas are not claimed as new.

## Limitations
The proof treats the unit interval, uniform sampling, fixed sample size, and pairwise covariance of component counts. It does not assert a full joint distribution, analogous classifications for other sampling densities, higher-dimensional geometric graphs, or independent historical priority. Related uniform-spacing empirical-process literature might contain equivalent finite-threshold formulas or their implications; that historical possibility has not been eliminated by exhaustive full-text inspection.

## References
1. L. Decreusefond and E. Ferraz, *On the One Dimensional Poisson Random Geometric Graph*, arXiv:1008.5140, first public version 2010-08-30; *Journal of Probability and Statistics* (2011), DOI:10.1155/2011/350382.
2. J. H. J. Einmahl and M. C. A. van Zuijlen, *Glivenko-Cantelli-type theorems for weighted empirical distribution functions based on uniform spacings*, *Statistics & Probability Letters* **13** (1992), 411–419, DOI:10.1016/0167-7152(92)90116-M.
