# Sharp weighted distortion of conservative nodal positivity scaling

## Finding
For any finite positive quadrature with at least two nodes, the standard cell-mean-anchored linear scaling positivity limiter can require an exactly quantifiable factor more correction than the smallest conservative, nodally nonnegative correction measured in the quadrature-weighted Euclidean norm. The sharp factor depends **only on the two smallest quadrature weights**, not on the other nodes or the data:
\[
\boxed{\sup_{\bar u>0,\,\min_i u_i<0}
\frac{\|u-L(u)\|_w}{\operatorname{dist}_w(u,\mathcal K_{\bar u})}
=\sqrt{\frac{(1-w_{(1)})(1-w_{(2)})}{w_{(1)}w_{(2)}}}.}
\]
For \(N\)-point Legendre--Gauss--Lobatto (LGL) quadrature on an interval, normalized to total weight one, the sharp factor is \(N(N-1)-1\). In particular it grows quadratically with the number of nodal degrees of freedom. With equal quadrature weights it is \(N-1\).

## Assumptions and scope
Fix an integer \(N\ge2\), weights \(w_i>0\) with \(\sum_{i=1}^Nw_i=1\), and any \(u\in\mathbb R^N\) whose weighted mean \(m=\sum_iw_i u_i\) is strictly positive and whose minimum \(u_*\) is negative. Define
\[
\|z\|_w^2=\sum_iw_i z_i^2,\qquad
\mathcal K_m=\{z\in[0,\infty)^N:\sum_iw_i z_i=m\}.
\]
The radial Zhang--Shu-type nodal correction and the optimal positivity-and-mean-preserving correction are
\[
L(u)=m\mathbf1+\theta(u-m\mathbf1),\quad
\theta=\frac{m}{m-u_*},\qquad
P(u)=\mathop{\arg\min}_{z\in\mathcal K_m}\|u-z\|_w.
\]
The minimizer \(P(u)\) exists uniquely by strict convexity, and the denominator in the displayed ratio is positive because \(u\notin\mathcal K_m\). The word *optimal* refers only to this nodal metric and to conservation of the one weighted mean, not to additional entropy inequalities, higher-dimensional physical admissibility, or positivity throughout a cell.

The theorem is homogeneous in the data, so no normalization of \(m\) is required. Sort the weights increasingly, with multiplicity, as \(w_{(1)}\le w_{(2)}\le\cdots\le w_{(N)}\). The displayed constant is the exact supremum for every fixed ordered weight vector, including repeated weights and \(N=2\).

## Proof
**Universal upper bound.** Choose any index \(i\) at which \(u_i=u_*=-a\), \(a>0\). Put
\[
p=\frac{u+a\mathbf1}{m+a}.
\]
Then \(p_i=0\), all coordinates of \(p\) are nonnegative, \(\sum_kw_kp_k=1\), and the radial output is exactly \(L(u)=mp\). Since \(u=(m+a)p-a\mathbf1\), its correction is \(u-L(u)=a(p-\mathbf1)\); consequently
\[
\|u-L(u)\|_w^2=a^2\left(\sum_kw_kp_k^2-1\right).
\]
Let \(j\ne i\) minimize \(w_j\) among all indices other than \(i\). Set \(q_k=w_kp_k\) for \(k\ne i\). These numbers are nonnegative and sum to one. Therefore
\[
\sum_kw_kp_k^2=\sum_{k\ne i}\frac{q_k^2}{w_k}
\le\frac1{w_j}\sum_{k\ne i}q_k^2\le\frac1{w_j}.
\]
Thus \(\|u-L(u)\|_w^2\le a^2(1-w_j)/w_j\).

Conversely, take any feasible \(z\in\mathcal K_m\), and write \(h=z-u\). We have \(h_i\ge a\) and \(\sum_kw_kh_k=0\). The weighted Cauchy--Schwarz inequality gives
\[
\sum_{k\ne i}w_kh_k^2\ge
\frac{\bigl(\sum_{k\ne i}w_kh_k\bigr)^2}{1-w_i}
=\frac{w_i^2h_i^2}{1-w_i},
\]
whence
\[
\|z-u\|_w^2\ge\frac{w_i}{1-w_i}h_i^2
\ge\frac{w_i}{1-w_i}a^2.
\]
Taking the minimum over \(z\) and dividing yields
\[
\frac{\|u-L(u)\|_w^2}{\|u-P(u)\|_w^2}
\le\frac{(1-w_i)(1-w_j)}{w_iw_j}.
\]
The function \(w\mapsto(1-w)/w\) decreases on \((0,1)\), so among all possible distinct \(i,j\) the right side is maximized by the two smallest weights.

**Sharpness, including multiplicities.** Select distinct indices \(i,j\) with weights \(w_{(1)},w_{(2)}\). For each sufficiently small \(\varepsilon>0\), set \(m=1\) and
\[
u_i=-\varepsilon,\qquad u_k=\sqrt\varepsilon\quad(k\notin\{i,j\}),\qquad
u_j=\frac{1+w_i\varepsilon-\sqrt\varepsilon(1-w_i-w_j)}{w_j}.
\]
The mean is exactly one; precisely coordinate \(i\) is negative once \(\varepsilon\) is small. The weighted nearest feasible point sets coordinate \(i\) to zero and shifts every other coordinate down by the same amount \(w_i\varepsilon/(1-w_i)\). Indeed, this shift preserves weighted mean, all other shifted coordinates remain strictly positive for sufficiently small \(\varepsilon\), and it satisfies the first-order optimality conditions for weighted orthogonal projection. Its exact squared correction cost is
\[
\|u-P(u)\|_w^2=\frac{w_i}{1-w_i}\varepsilon^2.
\]
For radial scaling, \(p=(u+\varepsilon\mathbf1)/(1+\varepsilon)\) converges to the vector with coordinate \(j\) equal to \(1/w_j\) and every other coordinate zero. Hence
\[
\lim_{\varepsilon\downarrow0}\frac{\|u-L(u)\|_w^2}{\varepsilon^2}
=\frac{1-w_j}{w_j}.
\]
Together these give the claimed sharp supremum. For \(N=2\), the feasible set is a line segment and every violating radial correction is itself the nearest feasible correction; the sharp ratio is identically one.

**LGL specialization.** For an \(N\)-node Legendre--Gauss--Lobatto formula with unit total weight, the positive weights at nodes \(x_i\) are
\[
w_i=\frac1{N(N-1)P_{N-1}(x_i)^2},
\]
where \(P_{N-1}\) denotes the ordinary Legendre polynomial. The two endpoints have \(|P_{N-1}|=1\), and \(|P_{N-1}(x)|\le1\) on \([-1,1]\), so the two endpoint weights are the two smallest: \(w_{(1)}=w_{(2)}=1/[N(N-1)]\). Substitution into the sharp formula gives \(N(N-1)-1\). Because LGL quadrature integrates every degree-\(N-1\) interpolating polynomial exactly, the weighted mean is also its actual cell average in that natural polynomial subspace.

## Verification
The included file `verify.py` evaluates the weighted simplex projection using exact rational arithmetic and checks the sharp inequality across 2,100 reproducible weighted nodal vectors, including a near-sharp explicit family. The independent LGL quadrature check covers node counts \(2\) through \(10\). The program was also extracted from this package and re-executed. These tests check algebra and implementation only; the universal theorem is proved by the upper-bound and sharpness arguments above.

## Relationship to prior work
The positivity- and entropy-stable DG scheme of Liu, Guo, Jiang and Sun (2026) and the EPO framework of Wu (2026) employ mean-anchored convex scaling and establish entropy/admissibility properties. Neither of those properties by itself specifies the **optimal weighted-distance distortion** of radial positivity scaling. The latter is a separately posed comparison of nodal positivity interventions.

Fu, Cheng and Shu (2026, §§3.3.1--3.3.3) discuss both optimization-based nodal correction and linear scaling. They explicitly note that scaling may cause stronger damping than a projection or redistribution method. The theorem here quantifies an exact, universal, *sharp* worst-case weighted-norm ratio and its LGL degree dependence. Their particular quadratic program acts on a weighted nodal vector with the ordinary norm; it should not be identified with the quadrature-weighted projection \(P\) used here.

Earlier work by Laiu and Hauck (2018/2019) compares positivity limiters and gives consistency error estimates. Its full manuscript could not be definitively checked in this assessment; more specialized prior coverage remains a bibliographic risk. No priority claim is made against inaccessible portions of that source.

## Limitations
The theorem is finite-dimensional and static. It treats scalar nodal nonnegativity at a chosen quadrature rule, preserves one weighted mean, and compares correction costs in the quadrature-weighted Euclidean metric. It does **not** show that the optimal nodal projection preserves discrete entropy inequalities, other invariants, high-order consistency of a full time-stepping scheme, or pointwise positivity between interpolation nodes. No bounded-error prediction for an evolved PDE is inferred from the static factor. Sharpness uses nodal configurations approaching a boundary; it need not be attained by a strictly one-negative-component vector.

## References
1. Y. Liu, W. Guo, Y. Jiang, and Z. Sun, *A limiter-based approach to construct high-order fully-discrete entropy stable explicit DG schemes for hyperbolic conservation laws*, arXiv:2603.27478 (first posted 2026-03-29), https://arxiv.org/abs/2603.27478.
2. K. Wu, *EPO: A Unified Framework for Entropy Stability, Positivity, and Oscillation Suppression*, arXiv:2604.00301 (2026), https://arxiv.org/abs/2604.00301.
3. J. Fu, J. Cheng, and C.-W. Shu, *High order positivity-preserving filtered PN methods for the gray model of thermal radiative transfer equations* (2026), Brown University manuscript, https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2026/04/High-order-positivity-preserving-filtered-PN-methods.pdf.
4. M. P. Laiu and C. D. Hauck, *Positivity Limiters for Filtered Spectral Approximations of Linear Kinetic Transport Equations*, Journal of Scientific Computing 78 (2019), 918--950, doi:10.1007/s10915-018-0790-y; public manuscript https://www.osti.gov/servlets/purl/1810030 (access intermittent).
