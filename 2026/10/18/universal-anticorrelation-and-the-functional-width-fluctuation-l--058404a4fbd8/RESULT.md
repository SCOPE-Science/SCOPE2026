# Universal anticorrelation and the functional width-fluctuation limit for regular polygons

## Finding
Let \(P_n\) be a regular Euclidean polygon with \(n\ge3\) vertices and circumradius \(R>0\). For an angle \(\theta\), let \(w_n(\theta)\) be its Euclidean width in direction \((\cos\theta,\sin\theta)\), and let \(\Theta\) be uniform on \([0,2\pi)\). Define
\[
 q_n=\begin{cases}\pi/n&n\text{ even},\\\pi/(2n)&n\text{ odd},\end{cases}\qquad
 A_n=\begin{cases}2R&n\text{ even},\\2R\cos q_n&n\text{ odd}.\end{cases}
\]
The mean is \(\mu_n=A_n\sin(q_n)/q_n\). The variance is \(\sigma_n^2=A_n^2\bigl(\frac12+\frac{\sin(2q_n)}{4q_n}-(\sin q_n/q_n)^2\bigr)>0\). For arbitrary angular lag \(\phi\), let \(r=\min_{k\in\mathbb Z}|\phi-2kq_n|\in[0,q_n]\). Then the *exact* two-angle covariance is
\[
 \operatorname{Cov}(w_n(\Theta),w_n(\Theta+\phi))=A_n^2\bigl(C_{q_n}(r)-(\sin q_n/q_n)^2\bigr),
\]
where
\[
 C_q(r)=\frac{(2q-r)\cos r+r\cos(2q-r)+\sin(2q-r)+\sin r}{4q}.
\]
For each fixed \(n\), this covariance is strictly decreasing in \(r\in[0,q_n]\), with one zero and a strictly negative minimum at \(r=q_n\).

More substantially, consider the centered, variance-one *entire angular process* on the fixed circle \(\mathbb R/2\mathbb Z\):
\[
 Z_n(x)=\frac{w_n(\Theta+q_n x)-\mu_n}{\sigma_n}.
\]
Let \(U\) be uniform on \([-1,1]\), and set \(d_2(t)=\min_{k\in\mathbb Z}|t-2k|\in[0,1]\). There is a coupling in which
\[
 \sup_{x\in\mathbb R/2\mathbb Z}\left|Z_n(x)-\frac{\sqrt{45}}{2}\left(\frac13-d_2(U+x)^2\right)\right|=O(q_n^2),
\]
where the implied constant is absolute for all sufficiently large \(n\), and the bound holds for every outcome, not just in probability. In particular, the process converges in the uniform topology to the indicated non-Gaussian process. Its correlation function at normalized offset \(z\in[0,1]\) is
\[
 \rho(z)=1-\frac{15}{8}z^2(2-z)^2,
\]
and the finite-\(n\) correlations converge uniformly to it with error \(O(q_n^2)\). The half-cell correlation tends to \(-7/8\), and the unique correlation zero at normalized offset \(z_n\in(0,1)\) tends to \(1-\sqrt{1-\sqrt{8/15}}\). The one-point limiting law is supported on \([-\sqrt5,\sqrt5/2]\) and has skewness \(-2\sqrt5/7\).

The previously known equality of standardized width functions for odd \(m\ge3\) and the regular \(2m\)-gon follows from Akiyama and Kamae's Theorems 3--4. It is historical context, not an original claim here.

## Assumptions and scope
All widths are classical Euclidean support widths, \(w_K(\theta)=h_K(\theta)+h_K(\theta+\pi)\). The randomization is a **single uniform initial angle**, followed by deterministic offsets, not independent directions at each offset. The previously known exact parity correspondence is only for odd \(m\ge3\). The new result concerns the functional scaling limit, universal lag correlation and negative correlation minimum.

We use the convention that a polygon has positive circumradius and nonempty interior. The asymptotic error is for the natural cell size \(q_n\); keeping an unscaled physical offset fixed as \(n\to\infty\) is a different limit.

## Proof
**1. Reduction to one periodic cosine arc.** Place a vertex at polar angle zero. The support function in direction \(\theta\) is \(R\) times the cosine of the angular distance to the nearest vertex. For even \(n\), the opposite vertex exists, so \(w_n(\theta)=2R\cos d(\theta)\), where \(d(\theta)\) is the distance modulo \(2\pi/n\) to the nearest vertex direction and takes values in \([0,\pi/n]\). For odd \(n\), if \(0\le\theta\le\pi/n\), the two extreme vertices give
\[
 w_n(\theta)=R\cos\theta+R\cos(\pi/n-\theta)=2R\cos(\pi/(2n))\cos(\theta-\pi/(2n)).
\]
Reflection and rotation extend this expression periodically with period \(\pi/n\). Thus in both parities, after a deterministic phase shift,
\[
 w_n(\theta)=A_n\cos\bigl(q_n d_2((\theta-\theta_*)/q_n)\bigr).
\]
A uniformly random \(\Theta\) induces a uniform phase \(U\) on \([-1,1]\). This proves the claimed exact distributional representation of the *whole* rescaled process as \(A_n\cos(q_n d_2(U+x))\).

**2. Exact two-angle covariance.** With \(q=q_n\), write \(f_q(t)=\cos t\) for \(-q\le t\le q\), extended with period \(2q\). Its expectation is \(s_q=\sin q/q\). By periodicity and reflection it suffices to evaluate \(r\in[0,q]\). Partitioning the overlap at \(q-r\) gives
\[
 C_q(r)=\frac1{2q}\left(\int_{-q}^{q-r}\cos t\cos(t+r)\,dt+\int_{q-r}^q\cos t\cos(t+r-2q)\,dt\right).
\]
Elementary product-to-sum integration yields exactly the displayed \(C_q(r)\). In particular \(C_q(0)=1/2+\sin(2q)/(4q)\), proving the mean and variance formulas and the exact covariance.

**3. Strict anticorrelation and unique crossing.** Differentiation simplifies to
\[
 C_q'(r)=\frac{r\sin(2q-r)-(2q-r)\sin r}{4q}
 =\frac{r(2q-r)}{4q}\left(\frac{\sin(2q-r)}{2q-r}-\frac{\sin r}{r}\right)<0
\]
for \(0<r<q\), because \(\sin t/t\) is strictly decreasing on \((0,\pi)\) and \(0<r<2q-r\le\pi/2\). The variance at lag zero is positive since the cosine arc is nonconstant. The lag-covariance integral over one full period vanishes, because the mean-centered autocorrelation integrates to zero. Strict monotonicity over half a period therefore forces the value at \(q\) to be negative and yields exactly one zero in \((0,q)\).

**4. Functional scaling limit and sharp limiting correlation.** Let \(d=d_2(U+x)\in[0,1]\). Uniformly in both \(x\) and \(U\),
\[
 \cos(qd)-\sin q/q =\frac{q^2}{2}(1/3-d^2)+O(q^4),
\]
while direct Taylor expansion of the exact variance yields
\[
 C_q(0)-s_q^2=q^4/45-q^6/315+O(q^8).
\]
Taking the square root, dividing, and bounding the remainders uniformly proves the sup-norm coupling with error \(O(q^2)\). This also proves uniform convergence of all bounded continuous functionals and fixed finite-dimensional moments of the process; it is stronger than convergence in distribution. Expanding the explicit covariance uniformly for \(0\le z\le1\) yields
\[
 C_q(zq)-s_q^2=q^4\left(1/45-z^2(2-z)^2/24\right)+O(q^6).
\]
Division by \(q^4/45+O(q^6)\) gives the universal quartic correlation with a uniform \(O(q^2)\) error. Strict monotonicity makes the finite-\(n\) zero unique. The limiting quartic has a unique zero in \((0,1)\), obtained by solving \(z(2-z)=\sqrt{8/15}\), so convergence of the zeros follows. At \(z=1\) the quartic is \(-7/8\). The limiting marginal is the affine image of \(U^2\), where \(U\) is uniform on \([-1,1]\); its endpoints and skewness follow from \(\mathbb E U^{2j}=1/(2j+1)\) for \(j=1,2,3\).



## Verification
The standalone standard-library program `verify.py` reconstructs projected widths directly from the vertices of regular polygons, without calling the proof's periodic cosine representation. It computes means and two-angle covariances by deterministic numerical quadrature for \(n\in\{3,4,5,6,7,8,11,12,17\}\) at five fractional lags per polygon (45 cases). Its observed maximum absolute mean discrepancy is below \(4\cdot10^{-9}\), and the maximum covariance discrepancy is below \(3\cdot10^{-9}\). Its assertion thresholds are \(3\cdot10^{-7}\). The full theorem, monotonicity, and functional limit are proved analytically, not inferred from these finite checks.

## Relationship to prior work
Akiyama and Kamae, *Width deviation of convex polygons* (arXiv:2201.06736v1, 18 January 2022), introduce random directional width, calculate its mean and second moment, and give a piecewise trigonometric representation. Their Theorem 1 explicitly gives a two-edge expectation kernel, so suitable rotation and summation **already imply** a lag-covariance *computational procedure* for any polygon. Their Theorems 3--4 also give the exact underlying width-function identity for odd regular polygons and double-sided regular polygons, hence the parity pairing of processes is **already covered**. Neither of those computations is represented as original here. Their exact width functions determine the finite joint angular laws in principle, but the paper does not state the **normalized functional scaling limit**, its uniform-in-angle quadratic coupling, its non-Gaussian limit, or the sharp half-cell anticorrelation law. The present finding isolates this stronger, two-point-and-process-level geometric structure and computes its sharp limiting constants. Related work on one-point width distributions and discrete directional Cauchy quadrature addresses different statistical objects; it does not supply the process limit here.

## Limitations
This result is for regular **Euclidean** polygons; the full process law need not survive affine deformation or arbitrary irregular polygons. The result concerns the *same* random initial angle for the entire angular field, not independent directions. The limiting process is periodic and strongly dependent, so no central limit theorem is claimed. The finite covariance formula can be obtained in principle from the earlier projected-edge kernel, and the odd-to-double-even pairing follows from the earlier exact pre-edge width function; neither is represented as novel. Originality and value here concern the full functional limit and the sharp angle-lag anticorrelation law. An unindexed prior derivation of these finer facts is a residual literature risk, and no external independent audit has been conducted.

## References
1. Shigeki Akiyama and Teturo Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1 (public 2022-01-18), https://arxiv.org/abs/2201.06736; full text https://arxiv.org/pdf/2201.06736; journal DOI 10.1007/s00454-023-00545-6. Specifically Introduction, Theorems 1, 3, 4, and the regular polygon deviation.
2. Relevant published mathematical-record comparators: *Inverse classification of projection-width distributions for tangential symmetric polygons* (one-angle width laws), and *Sharp positive N-direction Cauchy quadrature and angular rigidity* (finite deterministic direction sampling). Neither record claims a continuous angular stochastic-process limit.
