# Phase-lift compression cost for multimode coherent-state tori

## Finding

For a normalized vector \(\psi=\sum_{\mathbf k\in\mathbb N_0^d}c_{\mathbf k}e_{\mathbf k}\) in complex bosonic Fock space, consider its full coordinate phase orbit \(\psi_{\boldsymbol\theta}=U_{\boldsymbol\theta}\psi\) and the corresponding rank-one density-operator orbit \(\rho_{\boldsymbol\theta}=|\psi_{\boldsymbol\theta}\rangle\langle\psi_{\boldsymbol\theta}|\). Kolmogorov widths here always mean **complex-linear** subspaces, with Hilbert norm for vectors and Hilbert--Schmidt norm for operators. Let \(p_{\mathbf k}=|c_{\mathbf k}|^2\), extended by zero from \(\mathbb N_0^d\) to \(\mathbb Z^d\), and let \(q=p*\check p\), where \(\check p_{\mathbf k}=p_{-\mathbf k}\). For every finite integer \(N\ge0\),

\[
 d_N(\{\psi_{\boldsymbol\theta}\})^2=1-\sum_{j=1}^N p_j^\downarrow,
 \qquad d_N(\{\rho_{\boldsymbol\theta}\})^2=1-\sum_{j=1}^N q_j^\downarrow.
\]

The arrows denote decreasing rearrangement with multiplicity over the entire lattice; an empty sum is zero. In particular, \(d_N(\{\rho_{\boldsymbol\theta}\})\ge d_N(\{\psi_{\boldsymbol\theta}\})\) for every normalized vector and every finite \(N\).

For each fixed integer \(d\ge1\), positive anisotropy vector \(\mathbf a=(a_1,\ldots,a_d)\), and intensity scale \(t>0\), specialize to the product coherent vector

\[
 \psi_t=\exp\!\left(-\frac{t^2}{2}\sum_{j=1}^da_j^2\right)
 \sum_{\mathbf k\in\mathbb N_0^d}
 \left(\prod_{j=1}^d\frac{(ta_j)^{k_j}}{\sqrt{k_j!}}\right)e_{\mathbf k}.
\]

Then \(p_t\) is the joint probability mass function of independent Poisson variables with means \(t^2a_j^2\), and \(q_t\) is that of their coordinatewise differences with independent copies (a product of symmetric Skellam laws). In particular, for \(\mathbf l\in\mathbb Z^d\),

\[
 q_t(\mathbf l)=\prod_{j=1}^d e^{-2t^2a_j^2}I_{|l_j|}(2t^2a_j^2),
\]

where \(I_m\) is the ordinary modified Bessel function of the first kind. For every \(t>0\) and finite \(N\ge1\), the above width inequality is **strict**.

Fix a target error \(0<\varepsilon<1\). Define \(N_{\mathrm{vec}}(t,\varepsilon)\) and \(N_{\mathrm{proj}}(t,\varepsilon)\) as the least integers \(N\ge0\) for which the respective widths do not exceed \(\varepsilon\). Let \(R_{d,\varepsilon}>0\) be defined by \(\Pr(\chi_d^2\le R_{d,\varepsilon}^2)=1-\varepsilon^2\), and put \(v_d=\pi^{d/2}/\Gamma(1+d/2)\). As \(t\to\infty\), with \(d,\mathbf a,\varepsilon\) fixed,

\[
 \begin{aligned}
 N_{\mathrm{vec}}(t,\varepsilon)&\sim v_d R_{d,\varepsilon}^{d}
 t^d\prod_{j=1}^d a_j,\\
 N_{\mathrm{proj}}(t,\varepsilon)&\sim v_d R_{d,\varepsilon}^{d}
 (\sqrt2\,t)^d\prod_{j=1}^d a_j,\\
 \frac{N_{\mathrm{proj}}(t,\varepsilon)}{N_{\mathrm{vec}}(t,\varepsilon)}&\longrightarrow 2^{d/2}.
 \end{aligned}
\]

Thus passing from pure-state amplitude vectors to the corresponding phase-invariant rank-one projectors incurs a sharp, dimension-dependent overhead of \(2^{d/2}\) in optimal complex-linear compression capacity for the full \(d\)-torus of independent phases. This is a statement about complex-linear Kolmogorov widths, **not** about minimal physical Hilbert-space dimension, positive reconstructions, nonlinear compression, or real-linear Hermitian-only subspaces.

## Assumptions and scope

The number of modes \(d\) is a fixed positive integer. The oscillator Hilbert space is \(\mathcal H=\ell^2(\mathbb N_0^d;\mathbb C)\) with the standard number basis and \(U_{\boldsymbol\theta}e_{\mathbf k}=e^{i\mathbf k\cdot\boldsymbol\theta}e_{\mathbf k}\) for \(\boldsymbol\theta\in\mathbb T^d\). The operator space is complex \(\mathcal S_2(\mathcal H)\), with \(\|A\|_2^2=\operatorname{tr}(A^*A)\). For any subset \(E\) of the relevant Hilbert space, \(d_N(E)=\inf_{\dim_{\mathbb C}V\le N}\sup_{x\in E}\inf_{v\in V}\|x-v\|\). The general exact formulas require only a normalized vector, no coherent-state assumption. The asymptotic formulas require \(a_j>0\) and fixed \(\varepsilon\in(0,1)\).

## Proof

**1. Exact phase Fourier decompositions.** Write \(\psi_{\boldsymbol\theta}=\sum_{\mathbf k}e^{i\mathbf k\cdot\boldsymbol\theta}v_{\mathbf k}\), with orthogonal \(v_{\mathbf k}=c_{\mathbf k}e_{\mathbf k}\) and \(\|v_{\mathbf k}\|^2=p_{\mathbf k}\). In \(\mathcal S_2\), the projector is the Hilbert--Schmidt-convergent Fourier series

\[
 \rho_{\boldsymbol\theta}=\sum_{\mathbf l\in\mathbb Z^d}e^{i\mathbf l\cdot\boldsymbol\theta}B_{\mathbf l},\quad
 B_{\mathbf l}=\sum_{\mathbf k-\mathbf m=\mathbf l}c_{\mathbf k}\overline{c_{\mathbf m}}|e_{\mathbf k}\rangle\langle e_{\mathbf m}|.
\]

Matrices on distinct diagonals \(\mathbf k-\mathbf m\) are orthogonal in \(\mathcal S_2\), and \(\|B_{\mathbf l}\|_2^2=\sum_{\mathbf k-\mathbf m=\mathbf l}p_{\mathbf k}p_{\mathbf m}=q_{\mathbf l}\). These weights sum to one since all density matrices have Hilbert--Schmidt norm one.

**2. The optimal-uniform-orbit lemma.** Suppose in any complex Hilbert space \(x_{\boldsymbol\theta}=\sum_{\mathbf k}e^{i\mathbf k\cdot\boldsymbol\theta}w_{\mathbf k}\), with mutually orthogonal Fourier coefficient vectors and \(\sum\|w_{\mathbf k}\|^2=1\). For any orthogonal projection \(P\) of rank at most \(N\), normalized Haar averaging and Parseval give

\[
 \int_{\mathbb T^d}\|Px_{\boldsymbol\theta}\|^2\,d\boldsymbol\theta
 =\sum_{\mathbf k}\|Pw_{\mathbf k}\|^2
 =\operatorname{tr}\!\left(P\sum_{\mathbf k}|w_{\mathbf k}\rangle\langle w_{\mathbf k}|\right)
 \le\sum_{j=1}^N\|w\|_{(j)}^2.
\]

The last inequality is the min--max/Ky Fan bound for the positive trace-class covariance operator. Since \(\|x_{\boldsymbol\theta}\|=1\), the supremum of the squared projection error is at least one minus this sum. Choosing \(V\) to be the span of the \(N\) coefficient vectors of largest squared norm makes \(\|Px_{\boldsymbol\theta}\|^2\) identically equal to that sum for *every* phase. This proves the two exact width formulas, including the infinite-support case by monotone convergence.

**3. Convolution makes the phase lift harder.** Extend \(p\) by zero to \(\mathbb Z^d\). For any finite set \(S\) of at most \(N\) lattice points,

\[
 \sum_{\mathbf l\in S}q_{\mathbf l}
 =\sum_{\mathbf m}p_{\mathbf m}\sum_{\mathbf l\in S}p_{\mathbf l+\mathbf m}
 \le\sum_{j=1}^N p_j^\downarrow.
\]

Taking the supremum over \(S\) proves \(q\) is majorized by \(p\) and gives the width comparison. If \(p\) is the full-support product Poisson law with all intensities positive, this inequality is strict for every fixed finite \(S\): as \(\mathbf m\) tends to infinity through the positive orthant, the sum over the shifted finite set \(S+\mathbf m\) tends to zero, whereas the greatest \(N\)-point \(p\)-mass is positive; all mixing weights \(p_{\mathbf m}\) are positive. The top \(N\) points of \(q\) exist because \(q\in\ell^1\) and its entries tend to zero, so strictness persists on optimizing \(S\).

**4. Coherent Fourier spectra.** The coefficient magnitudes of \(\psi_t\) give independent Poisson laws. For each coordinate, the difference of two independent variables with mean \(\mu=t^2a_j^2\) has generating function

\[
 \mathbb E e^{i\xi(Z-Z')}=\exp\{2\mu(\cos\xi-1)\}
 =\sum_{k\in\mathbb Z}e^{-2\mu}I_{|k|}(2\mu)e^{ik\xi}.
\]

Taking products yields the displayed \(q_t\) and the exact decreasing-rearrangement formulas. No unstated special-function identities are needed beyond this convergent generating series.

**5. Multidimensional sharp quantile asymptotics.** Define scale factors \(h_j=t a_j\) for the vector coefficients, and \(h_j=\sqrt2\,t a_j\) for projector coefficients. The corresponding lattice probability mass functions \(\pi_t\) satisfy the uniform local central-limit formula on every bounded rescaled region,

\[
 \left(\prod_jh_j\right)\pi_t(\mathbf k)
 =\phi_d(\mathbf x)+o(1),\qquad
 \phi_d(\mathbf x)=(2\pi)^{-d/2}e^{-|\mathbf x|^2/2},
\]

where \(\mathbf x=((k_j-m_j)/h_j)_j\), with \(m_j=t^2a_j^2\) in the Poisson case and \(m_j=0\) in the difference case. For Poisson variables, Stirling's formula proves this uniformly on compacts. For differences, Fourier inversion of \(\exp\{2t^2a_j^2(\cos\xi-1)\}\) and the substitution \(\xi=u/h_j\) prove it by dominated convergence; the bound \(1-\cos\xi\ge c\xi^2\) on \([-\pi,\pi]\) controls the inversion tails.

The lattice probabilities are tight on the rescaled coordinates by the usual (joint) central limit theorem. Moreover, no remote point can defeat a fixed bounded Gaussian superlevel threshold: each Poisson marginal is unimodal (successive ratio \(\mu/(k+1)\)), and each equal-parameter Skellam marginal is symmetric and strictly decreasing away from zero. For completeness, the latter monotonicity follows by taking \(s_k=e^{-x}I_k(x)\) and \(\delta_k=s_k-s_{k+1}\), \(k\ge0\). The discrete heat equation gives \(\delta_0'=-3\delta_0/2+\delta_1/2\) and \(\delta_k'=(\delta_{k-1}+\delta_{k+1})/2-\delta_k\) for \(k\ge1\), with initial values \((1,0,0,\ldots)\). Its positive irreducible semigroup has \(\delta_k(x)>0\) for every \(x>0\). Thus outside a sufficiently large fixed rescaled box, one marginal is uniformly smaller than the chosen Gaussian threshold by monotonicity and the local limit formula; other marginals have maximum \(O(t^{-1})\). This establishes the needed global separation of high-probability lattice sites.

Fix \(0<\eta<R_{d,\varepsilon}\). Local limits, this separation, and lattice Riemann sums imply that, for sufficiently large \(t\), the set of largest coefficient probabilities that captures \(1-\varepsilon^2\) mass contains essentially all lattice sites of rescaled radius below \(R_{d,\varepsilon}-\eta\) and none beyond \(R_{d,\varepsilon}+\eta\), up to a boundary discrepancy of \(o(t^d)\) sites. This uses the strict radial decay of \(\phi_d\), continuity of Gaussian ball mass, and \(\Pr(|G|\le R_{d,\varepsilon})=1-\varepsilon^2\). Consequently its minimum cardinality \(N\) is squeezed, after division by \(\prod_jh_j\), between \(v_d(R_{d,\varepsilon}-\eta)^d+o(1)\) and \(v_d(R_{d,\varepsilon}+\eta)^d+o(1)\). Letting \(\eta\downarrow0\) yields \(N\sim v_dR_{d,\varepsilon}^d\prod_jh_j\). Substitution of the two scale vectors gives the displayed limits and the exact ratio \(2^{d/2}\).

## Verification

Run `python verify_phase_orbits.py` with Python 3, NumPy, and SciPy. The supplied checker builds finite phase-orbit Gram blocks directly, tests their Fourier-diagonal Hilbert--Schmidt masses, verifies finite majorization and Bessel selection, and evaluates the growing-intensity dimension ratios in one, two, and three modes. It passed 724 finite checks in the stated environment. These finite tests are supplementary; the statements for all dimensions, all amplitudes, and all real \(t>0\) rest on the argument above.

## Relationship to prior work

Mensah's 2026 operator Pego criterion concerns precompactness of Hilbert--Schmidt families; it supplies motivation but not the sharp dimension budget of a specific phase orbit. Arbes--Greif--Urban (2025) analyze optimal-width decompositions using shift-isometric eigenspaces for linear transport; the general orbit-eigenspace method in Step 2 is related and is **not** presented as an independently new universal technique. Drummond--Reid (2016) construct projected coherent phase states, while Mamon (2025/2026) studies the manifold dimension of optical orbits; neither identified source states the asymptotic difference between optimal vector and rank-one Hilbert--Schmidt projection budgets. The Poisson and Skellam formulas, standard majorization under convolution, and multivariate central-limit theorem are also prior mathematical ingredients. The present claimed quantitative object is the exact finite-dimensional phase-lift comparison together with the full anisotropic fixed-error asymptotic and \(2^{d/2}\) overhead.

## Limitations

The approximation subspaces are complex linear. In particular, a best finite-dimensional subspace of \(\mathcal S_2\) need not consist of self-adjoint operators, and this result does not prove a physical compression scheme using positive density operators. The asymptotic is for each fixed number of modes, positive anisotropies, and fixed error threshold, not uniform in dimension, anisotropy approaching zero, or shrinking error. It does not address trace norm, diamond norm, fidelity-based accuracy, nonlinear encoders, general non-Poisson number distributions' dimension asymptotics, or arbitrary phase-space translation families. General group-orbit width results and classical local limit theory may imply parts of this calculation; full publication priority remains open, especially because the motivating 2026 paper's primary full text was inaccessible in the present comparison.

## References

1. Y. Mensah, *The Pego Theorem for the Hilbert--Schmidt Class* (first submitted 2026-08-30), arXiv:2608.29976, https://arxiv.org/abs/2608.29976.
2. F. Arbes, C. Greif, and K. Urban, *The Kolmogorov N-width for linear transport: exact representation and the influence of the data*, Advances in Computational Mathematics 51 (2025), article 13, https://doi.org/10.1007/s10444-025-10224-0.
3. P. D. Drummond and M. D. Reid, *Coherent states in projected Hilbert spaces*, arXiv:1610.01261, https://arxiv.org/html/1610.01261v2.
4. E. Z. Mamon, *Orbit dimensions in linear and Gaussian quantum optics*, arXiv:2506.07995, https://arxiv.org/html/2506.07995v2.
5. J. G. Skellam, *The frequency distribution of the difference between two Poisson variates belonging to different populations*, J. R. Stat. Soc. A 109 (1946), 296; the probability law and generating function are used in their standard classical form.
