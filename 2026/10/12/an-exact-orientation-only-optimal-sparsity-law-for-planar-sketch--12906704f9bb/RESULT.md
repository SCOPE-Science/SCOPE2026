# An exact orientation-only optimal sparsity law for planar sketch-and-project

## Finding

Let \(A\in\mathbb R^{2\times2}\) be invertible with singular values \(\sigma_1>\sigma_2>0\). Let a leading **right** singular vector be \((\cos\theta,\sin\theta)\). Consider the Euclidean sketch-and-project solver for the consistent square system \(A^\top x=b\), with a fresh independent nonzero sketch vector \(s\in\mathbb R^2\) at each step. With probability \(1-t\), choose \(s\) uniformly from the four signed coordinate vectors \(\{\pm e_1,\pm e_2\}\); with probability \(t\), choose it uniformly from the four full sign vectors \(\{(\pm1,\pm1)\}\). Here \(0\le t\le1\).

Define
\[
\kappa=\frac{\sigma_1}{\sigma_2},\qquad
r=\frac{\kappa^2-1}{\kappa^2+1},\qquad
u=\sin(2\theta),\qquad v=\cos(2\theta),\qquad
D=(1-r^2v^2)(1-r^2u^2).
\]
Writing \(P_s=(As)(As)^\top/\|As\|_2^2\), the largest uniform expected-squared-error contraction coefficient is **exactly**
\[
\boxed{\rho(t)=\lambda_{\min}(\mathbb E P_s)
=\frac12\left[1-\frac{r}{\sqrt D}
\sqrt{u^2v^2+(1-r^2)(t-u^2)^2}\right].}
\]
Consequently, its **unique** maximizing mixture and the corresponding conditioned Bernoulli-sign entry density are
\[
\boxed{t_*=\sin^2(2\theta),\qquad
p_*=\frac{2\sin^2(2\theta)}{1+\sin^2(2\theta)}.}
\]
The optimum depends on the leading right-singular-vector orientation, **not** on the distinct singular values. Whenever \(0<\sin^2(2\theta)<1\), it strictly improves the sharp per-step uniform guarantee over both pure coordinate and pure dense-sign sketching.

Specifically, with \(x_*\) the unique exact solution and arbitrary deterministic \(x_0\),
\[
\mathbb E\|x_j-x_*\|_2^2\le(1-\rho(t))^j\|x_0-x_*\|_2^2
\qquad(j=0,1,2,\ldots).
\]
No larger \(\rho(t)\) can satisfy this inequality for every initial error and every \(j\), because equality is attainable at \(j=1\).

## Assumptions and scope

The matrix \(A\) is fixed and real, square and invertible; \(\kappa>1\) ensures uniqueness of \(t_*\). The vector \(b\) is consistent automatically because \(A^\top\) is invertible. The sketch distribution is fixed over iterations, with independent draws and exact Euclidean projections. The leading singular vector is understood up to sign. The coordinate/dense-sign mixture has a literal Bernoulli construction: retain each of two independent fair signs with probability \(p>0\), independently, and condition on at least one being retained. Then \(t=p/(2-p)\) and \(p=2t/(1+t)\). The \(p=0\) endpoint means its one-sparse limit, with a uniform coordinate chosen directly. The conditional expected number of nonzero entries is \(1+t\).

If \(\kappa=1\), every nonzero sketch generates isotropic average projector \(\mathbb E P_s=I/2\), so every \(t\) is optimal and uniqueness is not claimed.

## Proof

**1. Projector identity and exact sharp coefficient.** The update is
\[
x_{j+1}=x_j-\frac{As_j\,s_j^\top(A^\top x_j-b)}{s_j^\top A^\top A s_j}.
\]
For \(e_j=x_j-x_*\), this is \(e_{j+1}=(I-P_{s_j})e_j\). As \(P_{s_j}\) is an orthogonal rank-one projector,
\[
\mathbb E[\|e_{j+1}\|_2^2\mid e_j]
=\|e_j\|_2^2-e_j^\top\mathbb E[P_s]e_j
\le(1-\lambda_{\min}(\mathbb E P_s))\|e_j\|_2^2.
\]
Independence yields the claimed bound by induction. For \(j=1\), an initial error along a minimum-eigenvalue eigenvector realizes equality, establishing sharpness of its uniform coefficient.

**2. Orthogonal-pair projector calculation.** Scaling and left orthogonal transformations preserve eigenvalues of \(\mathbb E P_s\). Choose singular coordinates so that \(A\) acts like \(\operatorname{diag}(\kappa,1)R_\theta^\top\), where \(R_\theta\) is a plane rotation. For a pair of equiprobable perpendicular sketch directions making angles \(\psi\) and \(\psi+\pi/2\) with the first right singular direction, let \(M_\psi\) be the average rank-one projector onto their transformed directions. Every \(M_\psi\) has trace one, and direct division by the two squared transformed norms yields
\[
\begin{pmatrix}(M_\psi)_{11}-(M_\psi)_{22}\\2(M_\psi)_{12}\end{pmatrix}
=\frac{r}{1-r^2\cos^2(2\psi)}
\begin{pmatrix}\sin^2(2\psi)\\-\sqrt{1-r^2}\,\sin(2\psi)\cos(2\psi)\end{pmatrix}.
\]
For any trace-one symmetric \(2\times2\) matrix with this two-component vector \(w\), its two eigenvalues are \((1\pm\|w\|_2)/2\).

**3. Completion of the square.** Put \(u=\sin(2\theta)\), \(v=\cos(2\theta)\), \(a=1-r^2v^2\), and \(d=1-r^2u^2\). The uniform coordinate pair has \(\psi=-\theta\); the full sign pair has \(\psi=\pi/4-\theta\). Thus their respective trace-one projector vectors are
\[
w_0=\frac r a\begin{pmatrix}u^2\\\sqrt{1-r^2}\,uv\end{pmatrix},\qquad
w_1=\frac r d\begin{pmatrix}v^2\\-\sqrt{1-r^2}\,uv\end{pmatrix}.
\]
For mixture probability \(t\), the mean projector vector is \(w(t)=(1-t)w_0+tw_1\). Using \(u^2+v^2=1\) and expanding the two squares gives the exact identity
\[
\boxed{\|w(t)\|_2^2
=\frac{r^2}{ad}\left[u^2v^2+(1-r^2)(t-u^2)^2\right].}
\]
Both denominators are positive. As \(0<r<1\), the right-hand side has a unique minimum at \(t=u^2\in[0,1]\). Taking the square root and using the trace-one eigenvalue formula proves the claimed \(\rho(t)\) and unique optimizer, including endpoints. The conditioned Bernoulli relation proves the density formula. Neither maximizing value \(t_*\) nor \(p_*\) contains \(\kappa\).

**4. An exact mixed-design witness.** At \(\kappa=2\) and \(\theta=\pi/8\), one has \(r=3/5\), \(u^2=v^2=1/2\), and \(t_*=1/2\) (equivalently \(p_*=2/3\)). The sharp rate is
\[
\rho(1/2)=\frac{13}{41}
>\rho(0)=\rho(1)=\frac12\left(1-\frac3{\sqrt{41}}\right).
\]
Both extreme designs are therefore strictly inferior for this natural planar linear-system family.

## Verification

The standalone `verify.py` uses standard-library exact rational arithmetic to compute all four rank-one projectors directly from \(As\), their mixtures, the trace-one eigenvalue discriminant, and the completed-square identity. It checks twelve rational singular-vector directions, four singular-value ratios, and eight mixture values per pair: **1,152 exact-rational identities**. Run with `python3 verify.py`; the analytic proof above, not the finite checks, establishes the assertion for every admissible real parameter.

## Relationship to prior work

Gower and Richtárik [1] establish the sketch-and-project framework, the expected-projector contraction, and in Section 5.1 a general semidefinite program for optimizing probabilities over any finite family of sketches. Thus the existence of a convex probability optimization is **not** new. That general program does not state the present closed-form optimizer along the nonlinear Bernoulli-sign density family. Dereziński, Liang, Liao, and Mahoney [2] analyze expected projections for Gaussian and Rademacher sketches using quantitative surrogates. Dereziński and Rebrova [3] supply sharp general spectral bounds, explicit discussion of sparse and full sign sketches, and experiments on sparsification; their Section 3.3 focuses on LESS-type sketch distributions and bounds rather than optimizing a conditioned Bernoulli sign density on a planar instance. The present result is an exact, narrowly specified distribution-optimization law, not a replacement for those general bounds.

## Limitations

This is a planar theorem for one sketched equation per iteration and a specific two-support-size sign-mixture family. The optimal mixing parameter requires the singular-vector orientation, which may be expensive to know. The result optimizes the mathematically sharp *uniform expected-squared-error contraction coefficient*, not an instance-specific asymptotic error exponent, total computational cost, or the best law among all possible sketch distributions. No higher-dimensional or nonlinear extension follows merely by this calculation. Priority may be affected by unindexed elementary two-dimensional calculations. Independent validation remains to be performed.

## References

[1] R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (first posted 10 June 2015), https://arxiv.org/abs/1506.03296 .

[2] M. Dereziński, F. Liang, Z. Liao, and M. W. Mahoney, *Precise Expressions for Random Projections: Low-rank Approximation and Randomized Newton*, arXiv:2006.10653 (first posted 18 June 2020; corrected v3 available), https://arxiv.org/abs/2006.10653 .

[3] M. Dereziński and E. Rebrova, *Sharp Analysis of Sketch-and-Project Methods via a Connection to Randomized Singular Value Decomposition*, arXiv:2208.09585 (first posted 20 August 2022), https://arxiv.org/abs/2208.09585 .
