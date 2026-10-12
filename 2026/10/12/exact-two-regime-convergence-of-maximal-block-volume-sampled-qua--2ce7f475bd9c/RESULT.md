# Exact two-regime convergence of maximal-block volume-sampled quadratic coordinate descent

## Finding
Consider the Gaussian-free volume-sampled coordinate-descent method that at every step exactly minimizes a positive-definite quadratic over all but one coordinate, sampling the updated principal block proportionally to its determinant. Its **exact mean-square convergence factor** is the Perron root of a symmetric matrix built from the Hadamard square of the inverse Hessian. Independently, its trajectories obey a sharp dichotomy: any off-diagonal zero of the inverse Hessian implies almost-sure **finite-step absorption**, while a dense inverse Hessian implies no finite-step absorption from a coordinatewise-nonzero initial point and yields an explicit, generally different, almost-sure exponential rate.

More precisely, let \(H\in\mathbb R^{n\times n}\) be positive definite, \(n\ge2\), \(G=H^{-1}\), \(w_i=G_{ii}\), \(T=\sum_iw_i\), and \(C_{ij}=G_{ij}/\sqrt{w_iw_j}\). Define
\[
K_{ij}=\frac{G_{ij}^{2}}{T\sqrt{w_iw_j}}=\frac{\sqrt{w_iw_j}}{T}C_{ij}^{2},\qquad r=\rho(K).
\]
For any deterministic \(x_0\) with every coordinate nonzero, there is a constant \(c(H,x_0)>0\) such that
\[
\mathbb E\|x_k\|_2^2\sim c(H,x_0)r^{k-1},\qquad 0<r<1.
\]
If some \(G_{ij}=0\) with \(i\ne j\), the iterates reach the exact minimizer \(0\) in finitely many steps almost surely. If every off-diagonal entry of \(G\) is nonzero, no sample path reaches the minimizer in finite time, and almost surely
\[
\lim_{k\to\infty}\frac1k\log\|x_k\|_2=\gamma
=\sum_{i,j=1}^n\frac{w_iw_j}{T^2}\log|C_{ij}|<0.
\]
These statements jointly form one exact convergence law for the maximal proper-block volume sampler.

## Assumptions and scope
The target is \(f(x)=\tfrac12 x^{\mathsf T}Hx\) in exact real arithmetic. At each iteration, an independently sampled omitted coordinate \(I\in\{1,\ldots,n\}\) determines the selected block \(S=\{1,\ldots,n\}\setminus\{I\}\). Sampling probability is proportional to \(\det H_{SS}\), and the block coordinate minimizer is
\[
x^+=x-E_S H_{SS}^{-1}(Hx)_S.
\]
All principal blocks are invertible. All coordinates of deterministic \(x_0\) are assumed nonzero for the statements about non-absorption and the exact asymptotic mean-square coefficient; the mean-square matrix identity itself holds for any \(x_0\). Indices \(k=1,2,\ldots\) count completed updates. The same matrix \(H\) is used throughout, with fresh independent block labels each step.

## Proof
**1. Sampling and exact block update.** Jacobi's complementary-minor identity gives
\[
\det H_{-i,-i}=\det(H)(H^{-1})_{ii}=\det(H)w_i.
\]
Thus the omitted labels are independent with \(p_i=w_i/T>0\). Let \(v_i=G e_i/w_i\). Then \((v_i)_i=1\) and \(H v_i=e_i/w_i\). In particular, \((Hv_i)_j=0\) for all selected coordinates \(j\ne i\). Uniqueness of the block minimizer with fixed coordinate \(x_i\) implies
\[
x^+=x_i v_i.\tag{1}
\]
After the first update the state always lies on one of the explicitly known lines \(\mathbb Rv_i\). If \(s_k=(x_k)_{I_k}\), then
\[
x_k=s_kv_{I_k},\qquad s_{k+1}=s_k\frac{G_{I_{k+1},I_k}}{w_{I_k}}.\tag{2}
\]

**2. Exact second-moment matrix and rate.** Put \(m_k(j)=\mathbb E[s_k^2\mathbf1_{\{I_k=j\}}]\). From (2),
\[
m_1(j)=p_j(x_0)_j^2,\quad m_{k+1}=Qm_k,\quad Q_{ji}=p_j\frac{G_{ji}^2}{w_i^2}.\tag{3}
\]
With \(D=\operatorname{diag}(w_i^{3/2})\), direct multiplication gives \(D^{-1}QD=K\), the matrix in the finding. The Schur product theorem implies \(G\circ G\) is positive definite; hence so is the symmetric matrix \(K=(G\circ G)\) under positive diagonal congruence and scaling. It has nonnegative entries. Moreover, positive definiteness of \(G\) gives \(|C_{ij}|<1\) for \(i\ne j\). Therefore \(0\le K\le uu^{\mathsf T}/T\) entrywise, where \(u_i=\sqrt{w_i}\), with strict off-diagonal inequality, and the positive matrix \(uu^{\mathsf T}/T\) has spectral radius one. Perron monotonicity gives \(0<r=\rho(K)<1\).

By (1) and (3), the exact finite-time formula is
\[
\mathbb E\|x_k\|_2^2=\sum_j\|v_j\|_2^2(Q^{k-1}m_1)_j.\tag{4}
\]
Since \(m_1>0\) and \(\|v_j\|_2^2>0\), both terminal weights in the symmetric representation are strictly positive. Spectral decomposition of the symmetric positive-definite, entrywise-nonnegative matrix \(K\) shows that its top eigenspace contributes a strictly positive coefficient to (4), even if \(K\) is reducible. All other eigenvalues are strictly below \(r\), proving the asserted positive-constant asymptotic.

**3. Exact finite absorption.** If \(G_{ij}=0\) for distinct \(i,j\), occurrence of consecutive omitted labels \((I_t,I_{t+1})=(i,j)\) makes \(s_{t+1}=0\) in (2) and all later iterates zero. Each disjoint pair of labels has probability \(p_ip_j>0\) of equaling \((i,j)\). The probability of avoiding this pair in the first \(m\) disjoint trials is at most \((1-p_ip_j)^m\), so absorption occurs in finite time almost surely. Conversely, when all off-diagonal entries of \(G\) are nonzero, every ratio in (2) is nonzero, including the diagonal ratios. As \((x_0)_{I_1}\ne0\), no finite sequence can annihilate the state.

**4. Almost-sure exponent without absorption.** In the dense-inverse case, (2) and \(G_{ji}/w_i=C_{ji}\sqrt{w_j/w_i}\) give
\[
\log|s_k|=\log|(x_0)_{I_1}|+\sum_{t=1}^{k-1}\log|C_{I_{t+1},I_t}|+\frac12\log\frac{w_{I_k}}{w_{I_1}}.\tag{5}
\]
The bounded endpoint contributions vanish after division by \(k\). The strong law for the finite-state stationary ergodic sequence of adjacent pairs of independent labels gives the limit of the middle sum as \(\sum_{i,j}p_ip_j\log|C_{ij}|\). Since the finitely many \(\|v_i\|\) are bounded above and below away from zero, the same exponent holds for \(\|x_k\|\). At least one strict off-diagonal correlation occurs with positive frequency, hence \(\gamma<0\).

**5. Illustrative exact separation and nontrivial inverse-zero case.** In dimension two take \(G=\begin{psmallmatrix}1&c\\c&1\end{psmallmatrix}\) with \(0<c<1\). Then \(r=(1+c^2)/2\), but the almost-sure factor for squared error is \(\exp(2\gamma)=c\), and \(r-c=(1-c)^2/2>0\). In dimension three, \(G=\begin{psmallmatrix}2&0&1\\0&3&1\\1&1&2\end{psmallmatrix}\) is positive definite, whereas \(H=G^{-1}=\tfrac17\begin{psmallmatrix}5&1&-3\\1&3&-2\\-3&-2&6\end{psmallmatrix}\) has no zero off-diagonal entries. Nevertheless two successive omitted labels \((1,2)\) annihilate the iterate exactly. This isolates inverse-Hessian sparsity rather than Hessian separability as the absorption mechanism.

## Verification
The standalone Python 3 standard-library script `verify.py` reconstructs \(H\), the block minimizers, their weighted covariance recursion, and all finite label histories of lengths up to five for four rational positive-definite examples in dimensions two, three and four. It checks 1,147 exact rational path/norm equalities, the non-diagonal-Hessian inverse-zero example, and exact two-dimensional rate separation. Run `python3 verify.py` (expected terminal output starts `PASS:`). These finite checks test the identities and examples; the spectral, ergodic, and infinite-time statements are proved analytically above and are not inferred from finite enumeration.

## Relationship to prior work
Rodomanov and Kropotov's original volume-sampled block coordinate descent chooses blocks using principal minors and derives objective decrease/convergence guarantees, including a uniform expected contraction theorem. Its algorithm matches (1), but the examined analysis does not give (2)--(5), the Hadamard-square exact mean-square factor, or the inverse-zero finite-absorption criterion. Mutný, Dereziński and Krause analyze determinantal block-coordinate sampling and bounds involving expected inverse submatrices; their general sampling may have varying block size, and the examined results do not imply the present pathwise law. Published work on optimally weighted **single-coordinate** sampling and on **stale** Gauss--Seidel steps treats different updating rules. The precise new contribution here is the jointly exact annealed and quenched dynamics of the natural maximal proper-block determinant sampler, not re-proving its known first-step contraction estimate.

## Limitations
The almost-sure exponent formula applies only when \(G\) is off-diagonally dense, whereas exact finite absorption occurs when some inverse off-diagonal is zero. Initial coordinates all nonzero are essential for non-absorption and the positive mean-square leading coefficient; other starts may exhibit earlier cancellation. This is exact arithmetic for fixed SPD quadratics and \(n-1\)-coordinate block minimization only, not sparse approximate solvers, numerical floating-point termination, nonlinear optimization, arbitrary block sizes, or practical runtime superiority. Originality is based on inspected sources and search comparisons, not a proof that no equivalent derivation exists elsewhere.

## References
1. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587, first posted 2019-04-09, https://arxiv.org/abs/1904.04587 . Algorithm and general convergence theorems inspected.
2. I. Mutný, M. Dereziński and A. Krause, *Convergence Analysis of Block Coordinate Algorithms with Determinantal Sampling*, arXiv:1910.11561, first posted 2019-10-25, https://arxiv.org/abs/1910.11561 . Sampling framework and convergence-bounds analysis inspected.
3. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published mathematical record, 2026-09-20, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995 . Single-coordinate case compared.
4. *Exact delay-distribution law for two-coordinate randomized Gauss-Seidel*, published mathematical record, 2026-09-20, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-stochastic-delay-law-randomized-gauss-seidel--9ae0040f2dac . Different stale-coordinate update analyzed.
