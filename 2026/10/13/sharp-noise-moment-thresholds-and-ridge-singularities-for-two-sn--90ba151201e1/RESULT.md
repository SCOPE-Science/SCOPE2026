# Sharp noise-moment thresholds and ridge singularities for two-snapshot Anderson acceleration

## Finding

**Theorem (two-snapshot Gaussian Anderson moment and ridge law).** Fix an integer \(d\geq1\), a scalar \(|\lambda|<1\), a noise scale \(\sigma>0\), and two distinct deterministic snapshots \(u,v\in\mathbb R^d\). Observe independent noisy evaluations \(F_0=\lambda u+\xi_0\) and \(F_1=\lambda v+\xi_1\), with \(\xi_0,\xi_1\) independent \(N(0,\sigma^2I_d)\). Put \(r_0=F_0-u\), \(r_1=F_1-v\), and \(D=r_1-r_0\). The depth-one, unit-mixing Anderson update with scalar Tikhonov penalty \(\varepsilon\geq0\) is

\[
t_\varepsilon=\underset{t\in\mathbb R}{\operatorname{argmin}}\;\bigl\{\|r_0+tD\|^2+\varepsilon t^2\bigr\},\qquad
X_\varepsilon=F_0+t_\varepsilon(F_1-F_0).
\]

At \(\varepsilon=0\) this is understood wherever \(D\ne0\), an event of probability one. For every real \(q>0\),

\[
\boxed{\;\mathbb E\|X_0\|^q<\infty\quad\Longleftrightarrow\quad q<d.\;}
\]

In particular, although both oracle errors have all finite moments, the accelerated update has infinite mean-square norm in dimensions \(d=1,2\), and finite mean-square norm for every \(d\geq3\). Every \(\varepsilon>0\) restores finiteness of all positive-order moments. Its exact small-penalty mean-square singularity is

\[
\boxed{\;
\mathbb E\|X_\varepsilon\|^2=
\begin{cases}
\displaystyle\frac{\pi}{2}\|\Delta\|^2p_D(0)C_h\,\varepsilon^{-1/2}+o(\varepsilon^{-1/2}),&d=1,\\
\displaystyle\frac{\pi}{2}\|\Delta\|^2p_D(0)C_h\,\log(\sigma^2/\varepsilon)+o(\log(\sigma^2/\varepsilon)),&d=2,\\
\displaystyle\mathbb E\|X_0\|^2+o(1),&d\geq3,
\end{cases}\;}
\]

where \(\Delta=v-u\), \(m=(u+v)/2\), \(C_h=(1-\lambda)^2\|m\|^2+d\sigma^2/2\), and the density of the Gaussian residual difference at the origin is

\[
p_D(0)=(4\pi\sigma^2)^{-d/2}\exp\bigl(-{(1-\lambda)^2\|\Delta\|^2}/{(4\sigma^2)}\bigr)>0.
\]

## Assumptions and scope

The snapshots are fixed **before** drawing the two independent oracle noises. The oracle is the affine contraction \(x\mapsto\lambda x\) with independent additive isotropic Gaussian measurement error at each snapshot. The update uses exactly two distinct snapshots, one residual-difference column, unconstrained scalar affine extrapolation, unit outer mixing, and a ridge penalty on the one scalar mixing coefficient. There is no clipping, restarting, safeguard, or iterate-dependent damping. The penalty is \(\varepsilon t^2\), not a penalty on the two affine weights separately. No assertion is made about snapshots that themselves depend on these same two oracle noises.

All norms are Euclidean. Statements about moments are of \(X_\varepsilon\), not of the deterministic fixed-point map. The zero fixed point is the target, so its squared solution error equals \(\|X_\varepsilon\|^2\).

## Proof

**1. Exact one-column Anderson formula.** For \(\varepsilon>0\), the unique scalar minimizer is

\[
t_\varepsilon=-\frac{\langle r_0,D\rangle}{\|D\|^2+\varepsilon}.
\]

The same formula holds at zero ridge whenever \(D\ne0\). Set \(h=(r_0+r_1)/2\). Since \(r_0=h-D/2\), we obtain

\[
t_\varepsilon=\frac12-\frac{\langle h,D\rangle+\varepsilon/2}{\|D\|^2+\varepsilon}.
\]

Using \(F_1-F_0=\Delta+D\), this gives the **exact update identity**

\[
X_\varepsilon=m+h-\frac{\langle h,D\rangle+\varepsilon/2}{\|D\|^2+\varepsilon}(\Delta+D).
\tag{1}
\]

**2. An independent Gaussian numerator.** The random vectors \(h\) and \(D\) are jointly Gaussian, with means \((\lambda-1)m\) and \((\lambda-1)\Delta\), and respective covariances \(\sigma^2I_d/2\) and \(2\sigma^2I_d\). Their cross-covariance vanishes because the sum and difference of independent equal-covariance Gaussians are uncorrelated. Consequently \(h\) and \(D\) are independent, and \(D\) has a smooth density strictly positive at the origin, equal to the displayed \(p_D(0)\). Also \(\mathbb E\|h\|^2=C_h>0\).

**3. Sharp unregularized moment criterion.** Let \(P_D=DD^{\mathsf T}/\|D\|^2\). At zero ridge, (1) becomes

\[
X_0=m+(I-P_D)h-\Delta\,\frac{\langle h,D\rangle}{\|D\|^2}.
\tag{2}
\]

The first two terms have finite moments of every positive order, since \(\|I-P_D\|\leq1\). The absolute value of the scalar singular term is at most \(\|h\|/\|D\|\). Independence and polar integration give \(\mathbb E\|h\|^q<\infty\) and

\[
\mathbb E\|D\|^{-q}<\infty\quad\Longleftrightarrow\quad\int_0^1r^{d-1-q}\,dr<\infty\quad\Longleftrightarrow\quad q<d.
\]

This proves sufficiency. For necessity, choose a unit direction \(\omega_0\), a compact positive-probability set of \(h\)-values satisfying \(|\langle h,\omega_0\rangle|\geq2c\) for some \(c>0\), and a small spherical cap around \(\omega_0\). Continuity then ensures \(|\langle h,\omega\rangle|\geq c\) uniformly on a smaller cap. For \(D=r\omega\) with sufficiently small \(r\), the last term of (2) has norm at least \(c\|\Delta\|/r\), while the bounded remainder is uniformly bounded on the chosen compact set. By the positive Gaussian density of \(D\) near zero, the \(q\)-th moment is bounded below by a positive multiple of \(\int_0^{r_0}r^{d-1-q}dr\), infinite when \(q\geq d\). This includes the critical logarithmic divergence at \(q=d\).

**4. Regularized moments and their precise small-penalty behavior.** Write

\[
Q_\varepsilon=\frac{\langle h,D\rangle}{\|D\|^2+\varepsilon},\qquad
B_\varepsilon=m+h-Q_\varepsilon D-\frac{\varepsilon}{2}\frac{\Delta+D}{\|D\|^2+\varepsilon};\qquad
X_\varepsilon=B_\varepsilon-\Delta Q_\varepsilon.
\tag{3}
\]

For \(0<\varepsilon\leq1\), \(\|Q_\varepsilon D\|\leq\|h\|\), \(\varepsilon\|D\|/(\|D\|^2+\varepsilon)\leq\sqrt\varepsilon/2\), and \(\varepsilon/(\|D\|^2+\varepsilon)\leq1\). Thus \(B_\varepsilon\) is dominated in every finite \(L^q\) by a constant plus \(2\|h\|\); in particular, \(\sup_{0<\varepsilon\leq1}\mathbb E\|B_\varepsilon\|^2<\infty\). At any fixed positive ridge, \(|Q_\varepsilon|\leq\|h\|/(2\sqrt\varepsilon)\), proving all finite positive moments of \(X_\varepsilon\).

For the second moment, independence gives the exact integral

\[
\mathbb E Q_\varepsilon^2=\int_0^\infty\frac{r^{d+1}}{(r^2+\varepsilon)^2}\left[\int_{\mathbb S^{d-1}}p_D(r\omega)\,\mathbb E(\langle h,\omega\rangle^2)\,d\omega\right]dr.
\tag{4}
\]

Near zero, \(p_D(r\omega)=p_D(0)+O(r)\) uniformly in direction. In one dimension the local leading radial integral is the full-line identity \(\int_{\mathbb R}z^2/(z^2+\varepsilon)^2dz=\pi/(2\sqrt\varepsilon)\). Hence

\[
\mathbb E Q_\varepsilon^2=\frac\pi2p_D(0)C_h\varepsilon^{-1/2}+o(\varepsilon^{-1/2})\qquad(d=1).
\]

In two dimensions, \(\int_{\mathbb S^1}\mathbb E\langle h,\omega\rangle^2\,d\omega=\pi C_h\), while for every fixed small \(R>0\),

\[
\int_0^R\frac{r^3}{(r^2+\varepsilon)^2}dr=\frac12\log(1/\varepsilon)+O_R(1).
\]

It follows that \(\mathbb E Q_\varepsilon^2=(\pi/2)p_D(0)C_h\log(\sigma^2/\varepsilon)+o(\log(\sigma^2/\varepsilon))\) for \(d=2\); the positive reference scale \(\sigma^2\) inside the logarithm changes only a bounded term. The contribution to (4) from \(r\geq R\) is uniformly bounded in both cases. From (3), Cauchy–Schwarz bounds the cross term by \(O((\mathbb E Q_\varepsilon^2)^{1/2})\), while \(\mathbb E\|B_\varepsilon\|^2=O(1)\). Consequently the leading terms in \(\mathbb E\|X_\varepsilon\|^2\) are precisely \(\|\Delta\|^2\mathbb E Q_\varepsilon^2\).

If \(d\geq3\), the integrable majorant \(\|Q_\varepsilon\|^2\leq\|h\|^2/\|D\|^2\) and the bounds on \(B_\varepsilon\) give \(L^2\) convergence \(X_\varepsilon\to X_0\) by dominated convergence. This establishes the third branch and completes the proof.

## Verification

The standalone `verify.py` compares two algebraically independent implementations of (1) on 800 seeded random input/noise vectors across dimensions \(1\) through \(8\) and five ridge values (including zero). Six additional adaptive quadrature comparisons verify the predicted one-dimensional square-root and two-dimensional logarithmic coefficients at three decreasing ridge levels. Run with `python verify.py` in an environment with NumPy and SciPy. These finite checks probe algebra and leading coefficients; the moment threshold and limiting asymptotics are proved in the text, not inferred from numerical sampling or quadrature.

## Relationship to prior work

Anderson mixing and its depth-one least-squares residual projection are classical; no new solver is claimed. Wei, Bao, and Liu (2021) introduced stochastic Anderson mixing with damping and adaptive regularization to control instability in stochastic optimization. The present result isolates its simplest **unsafeguarded** two-snapshot Gaussian oracle mechanism and gives sharp moment and ridge-penalty laws; it neither asserts nor contradicts the stochastic convergence guarantees for their safeguarded method. Shi and collaborators (2019) studied regularization for approximate Anderson evaluations, and Lupo Pasini and Laiu (2022) analyzed inexact Anderson least-squares conditioning; those studies motivate ridge stabilization but their inspected results do not imply the specific Gaussian moment/dimension transition and leading singularity coefficients here. Toth, Kelley, and colleagues (2017) studied inaccurate evaluations; only its abstract was accessible for comparison, so its treatment of closely related randomness is a genuine remaining priority uncertainty.

The fact that a ratio of random variables can have heavy tails is classical. The contribution under consideration is its **specific sharp norm-moment threshold and exact ridge asymptotic coefficients for the vector Anderson update**, with the non-cancelling snapshot displacement explicitly accounted for. No priority or universality is inferred from unsuccessful indexing searches.

## Limitations

The snapshots are fixed independently of the two noises and may not coincide with successive iterates of a stochastic solver. Distinct snapshots and full-rank isotropic Gaussian noise are essential to the stated sharp threshold. The result treats only one depth-one update, a scalar contraction, unconstrained coefficients, and ridge on one scalar; it makes no claims about repeated Anderson cycles, general nonlinear maps, clipping, adaptive regularization, or end-to-end convergence. An accessible full-text comparison to the 2017 inaccurate-evaluation paper remains unavailable; equivalent earlier specialized analysis cannot be excluded. Independent verification by another researcher has not been performed.

## References

1. F. Wei, C. Bao, and Y. Liu, *Stochastic Anderson Mixing for Nonconvex Stochastic Optimization*, arXiv:2110.01543v1, publicly submitted 2021-10-04. https://arxiv.org/abs/2110.01543
2. M. Lupo Pasini and M. P. Laiu, *Anderson acceleration with approximate calculations: applications to scientific computing*, arXiv:2206.03915v1, 2022. https://arxiv.org/abs/2206.03915
3. W. Shi, S. Song, H. Wu, Y.-C. Hsu, C. Wu, and G. Huang, *Regularized Anderson Acceleration for Off-Policy Deep Reinforcement Learning*, arXiv:1909.03245v1, 2019. https://arxiv.org/abs/1909.03245
4. A. Toth, J. A. Ellis, T. Evans, S. Hamilton, C. T. Kelley, R. Pawlowski, and S. Slattery, *Local Improvement Results for Anderson Acceleration with Inaccurate Function Evaluations*, SIAM Journal on Scientific Computing 39(5), S47–S65 (2017), DOI:10.1137/16M1080677 (abstract inspected; full text not accessed).
5. H. F. Walker and P. Ni, *Anderson Acceleration for Fixed-Point Iterations*, SIAM Journal on Numerical Analysis 49 (2011), 1715–1735, DOI:10.1137/10078356X.
