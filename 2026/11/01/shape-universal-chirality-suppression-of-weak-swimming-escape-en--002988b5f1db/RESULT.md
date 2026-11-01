# Shape-universal chirality suppression of weak-swimming escape enhancement

## Finding

For a chiral active Brownian particle in any bounded, connected, fully absorbing, planar \(C^2\) domain, started uniformly in position and orientation, the weak-swimming reduction in mean exit time is a strictly completely monotone function of the **squared chirality**. The exact reduction is a positive Dirichlet spectral Stieltjes transform. This conclusion does not require rotational diffusivity to be positive, and it does not require a circular or reflection-symmetric domain.

**Theorem.** Let \(G\subset\mathbb R^2\) be bounded, connected and \(C^2\), and let \(D>0\), \(D_R\ge0\), \(\Omega\in\mathbb R\). Consider the Markov process up to its first spatial exit \(\tau_G\):
\[
 dX_t=v(\cos\Phi_t,\sin\Phi_t)\,dt+\sqrt{2D}\,dB_t,
 \qquad d\Phi_t=\Omega\,dt+\sqrt{2D_R}\,dW_t \pmod{2\pi},
\]
where \(B,W\) are independent Brownian motions, \(X_0\) is uniform on \(G\), and \(\Phi_0\) is independent and uniform on the circle. Write \(M_G(v,\Omega)=\mathbb E\tau_G\). Let \(u_0\) be the unique Dirichlet solution of
\[
 -D\Delta u_0=1\quad\text{in }G,\qquad u_0=0\quad\text{on }\partial G.
\]
For any real orthonormal basis of Dirichlet Laplacian eigenfunctions \((\psi_j)_{j\ge1}\), with \(-\Delta\psi_j=\lambda_j\psi_j\), define
\[
 a_j=D\lambda_j+D_R,\qquad
 B_{j,k}=\int_G\psi_j(x)\,\partial_k u_0(x)\,dx\quad(k=1,2).
\]
Then, as \(v\to0\) for each fixed \(\Omega\),
\[
 M_G(v,\Omega)=\frac1{|G|}\int_Gu_0(x)\,dx-v^2\chi_G(\Omega)+O(v^4),
\]
where
\[
 \boxed{\displaystyle
 \chi_G(\Omega)=\frac1{2|G|}\sum_{j=1}^{\infty}
 \bigl(B_{j,1}^2+B_{j,2}^2\bigr)
 \frac{a_j}{a_j^2+\Omega^2}.}
\]
The series is absolutely convergent, independent of eigenbasis choice within degenerate eigenspaces, and strictly positive. With \(s=\Omega^2\), for every integer \(k\ge0\) and every \(s\ge0\),
\[
 \boxed{\displaystyle
 (-1)^k\frac{d^k}{ds^k}\chi_G(\sqrt s)
 =\frac{k!}{2|G|}\sum_{j\ge1}
 \frac{(B_{j,1}^2+B_{j,2}^2)a_j}{(a_j^2+s)^{k+1}}>0.}
\]
Consequently \(\chi_G\) is even, strictly decreases with \(|\Omega|\), and tends to zero as \(|\Omega|\to\infty\). The unscaled mean has the independent, nonperturbative bound
\[
 M_G(v,\Omega)<M_G(0,\Omega)
 \quad\text{for every }v\ne0,\;\Omega\in\mathbb R.
\]
The latter follows from a generic antisymmetric-drift energy comparison and is included for context; the **new focus** is the explicit all-domain chirality Stieltjes law and its strict complete-monotonicity hierarchy.

The theorem is not a claim that \(M_G(v,\Omega)\) is monotone in chirality for arbitrary nonzero \(v\). It is a statement about the exact coefficient of \(v^2\) at \(v=0\).

## Assumptions and scope

The entire spatial boundary is absorbing, without reflecting or partially reactive segments. Angular evolution is independent of position and starts in its Haar stationary distribution. Rotational diffusivity may be zero; positive translational diffusivity is essential. The uniform spatial initialization is essential for the energy identity and the coefficient's sign. A \(C^2\) boundary is assumed for standard Dirichlet regularity; the spectral formula also suggests weak-domain extensions, but they are not asserted here.

The orientation-averaged exit time for a prescribed starting position need not satisfy the same sign or chirality ordering. The error \(O(v^4)\) is for fixed \(G,D,D_R,\Omega\); uniformity as \(|\Omega|\to\infty\), as \(D\downarrow0\), or over degenerating domains is not asserted.

## Proof

**1. Backward equation and solvability.** Use the normalized real \(L^2\) pairing
\[
 \langle f,g\rangle=\frac1{2\pi|G|}\int_G\int_0^{2\pi}f(x,\phi)g(x,\phi)\,d\phi\,dx.
\]
Write \(e(\phi)=(\cos\phi,\sin\phi)\), \(\mathcal B=e(\phi)\cdot\nabla_x\), and
\[
 \mathcal A_0=-D\Delta_x-D_R\partial_\phi^2-\Omega\partial_\phi,
 \qquad\mathcal A_v=\mathcal A_0-v\mathcal B.
\]
The mean exit function \(U_v(x,\phi)=\mathbb E_{x,\phi}\tau_G\) satisfies
\(\mathcal A_v U_v=1\) with zero trace on \(\partial G\) and periodic angular boundary conditions. Dirichlet coercivity in \(x\) gives invertibility for every real \(v\), including \(D_R=0\).

The drift \(\mathcal B\) is skew in this pairing because it is spatially divergence-free and functions have zero Dirichlet trace; \(-\Omega\partial_\phi\) is skew by periodicity. Thus
\[
 \langle U_v,\mathcal A_v U_v\rangle
 =D\|\nabla_x U_v\|_2^2+D_R\|\partial_\phi U_v\|_2^2.
\]
For the unperturbed problem, \(U_0(x,\phi)=u_0(x)\), independent of \(\phi\) and of the angular parameters. The adjoint likewise satisfies \((\mathcal A_0^*)^{-1}1=u_0\).

**2. Justification of the swimming expansion.** Let \(\lambda_1>0\) be the first spatial Dirichlet eigenvalue. If \(u=\mathcal A_0^{-1}f\), the skew terms disappear in the real energy pairing, so
\[
 D\|\nabla_x u\|_2^2\le \|f\|_2\|u\|_2,
 \qquad\|u\|_2\le\frac{\|f\|_2}{D\lambda_1}.
\]
It follows that \(\|\mathcal B\mathcal A_0^{-1}\|_{2\to2}\le 1/(D\sqrt{\lambda_1})\). Therefore the resolvent expansion of \(\mathcal A_v^{-1}=\mathcal A_0^{-1}(I-v\mathcal B\mathcal A_0^{-1})^{-1}\) converges in operator norm for \(|v|<D\sqrt{\lambda_1}\). Shifting the angle by \(\pi\) leaves \(\mathcal A_0\), the uniform measure and the constant source invariant and changes \(\mathcal B\) to \(-\mathcal B\). Hence \(M_G(v,\Omega)\) is an even analytic function of \(v\) near zero, so the remainder after the quadratic term is \(O(v^4)\).

**3. Exact negative second variation.** Set
\[
 F=\mathcal B u_0=\cos\phi\,\partial_1u_0+\sin\phi\,\partial_2u_0.
\]
The quadratic coefficient in the normalized volume-angle mean is
\[
 \begin{aligned}
 [v^2]M_G(v,\Omega)
 &=\langle1,\mathcal A_0^{-1}\mathcal B\mathcal A_0^{-1}\mathcal B u_0\rangle\\
 &=\langle u_0,\mathcal B\mathcal A_0^{-1}F\rangle\\
 &=-\langle F,\mathcal A_0^{-1}F\rangle.
 \end{aligned}
\]
The first equality uses the resolvent expansion, the second the adjoint unperturbed equation, and the third the skewness of \(\mathcal B\). The real quadratic form is nonnegative despite the angular operator being non-self-adjoint, as its antisymmetric contribution cancels.

**4. Spectral evaluation and complete monotonicity.** Expand each component of \(\nabla u_0\) in the real Dirichlet eigenbasis. Only the first orientation harmonics \(\cos\phi\) and \(\sin\phi\) occur. On their two-dimensional span, \(\mathcal A_0\) acts at spatial eigenvalue \(\lambda_j\) as a matrix with symmetric diagonal \(a_j\) and skew off-diagonal parts \(\pm\Omega\). Its inverse has symmetric part
\[
 \frac{a_j}{a_j^2+\Omega^2}\,I_2.
\]
Orthogonality of the two angular harmonics gives their normalized squared norm \(1/2\), yielding the boxed spectral expression. Parseval gives
\(\sum_j(B_{j,1}^2+B_{j,2}^2)=\|\nabla u_0\|_{L^2(G)}^2<\infty\), and \(a_j\ge D\lambda_1+D_R>0\). These facts justify the series, basis invariance, termwise derivatives for every \(s\ge0\), and the limit as \(s\to\infty\). Since \(-D\Delta u_0=1\), the gradient cannot vanish identically. Hence at least one spectral weight is positive, making every displayed alternating derivative **strictly** positive.

**5. Nonperturbative bound.** For any \(v\), use \(\mathcal A_vU_v=1\), \(-D\Delta u_0=1\), integration by parts, and Cauchy–Schwarz:
\[
 \begin{aligned}
 M_G(v,\Omega)
 &=D\|\nabla_x U_v\|_2^2+D_R\|\partial_\phi U_v\|_2^2\\
 &=D\langle\nabla_x u_0,\nabla_x U_v\rangle\\
 &\le\sqrt{M_G(0,\Omega)\,M_G(v,\Omega)}.
 \end{aligned}
\]
Thus \(M_G(v,\Omega)\le M_G(0,\Omega)\). Equality would force \(U_v=c u_0\) (up to constants eliminated by Dirichlet trace), and the mean identity forces \(c=1\). The equation for \(U_v=u_0\) would then demand \(v e(\phi)\cdot\nabla u_0=0\) for almost every angle, which is impossible for \(v\ne0\). Hence the inequality is strict. This classical antisymmetric-drift argument is not used to infer the more specialized chirality derivative hierarchy.

**6. Two normalization tests.** For a one-dimensional absorbing interval \((-L,L)\) with a planar heading but only the horizontal component of the propulsion used, the identical first-harmonic argument gives
\[
 \chi_{(-L,L)}(\Omega)=\frac{L^2}{D^2\pi^2}\sum_{n=1}^\infty
 \frac{D(n\pi/L)^2+D_R}{n^2\bigl([D(n\pi/L)^2+D_R]^2+\Omega^2\bigr)}.
\]
At \(D_R=\Omega=0\), the sum is \(L^4/(90D^3)\). Independently, expanding the constant-velocity exit equation for a fixed orientation gives the second-order pointwise term
\[
 U_2(x,\phi)=-\frac{(L^2-x^2)^2\cos^2\phi}{24D^3},
\]
whose uniform spatial-angular average is indeed \(-L^4/(90D^3)\). The interval is a dimensional-reduction check, not a two-dimensional smooth-domain hypothesis.

For a fully absorbing disk of radius \(R\) with \(D_R=\Omega=0\), one has \(u_0(x)=(R^2-|x|^2)/(4D)\). Solving the first-order Dirichlet equation for the linear spatial coordinate yields
\[
 \mathcal A_0^{-1}F=-\frac{(e(\phi)\cdot x)(R^2-|x|^2)}{16D^2},
 \qquad\chi_{\mathrm{disk}}(0)=\frac{R^4}{384D^3}.
\]
This independent polynomial calculation checks the factors \(1/2\), \(|G|^{-1}\), and the power of the diffusivity in the general formula; it is not claimed as a new standalone disk theorem.

## Verification

Run `python verify.py` in an environment with NumPy and SciPy. The program performs deterministic computations of the interval Dirichlet series and its alternating derivatives, checks the independent disk polynomial integral, and solves a discrete backward equation with periodic angular coordinates at four pairs of angular diffusivity and chirality. It verifies convergence of the quadratic finite-swimming response, equality under swimming-direction reversal, and the strict finite-parameter mean speedup. A complete replay produced `PASS: 126 deterministic checks`.

The discrete grid and truncated series do **not** prove the infinite-domain/parameter statements. The proof is the preceding resolvent, orthogonality, and positivity argument.

## Relationship to prior work

Iyaniwura, Qiu and Peng (2026, arXiv:2605.23095v1) formulate chiral active Brownian mean first-passage problems in absorbing intervals and partially absorbing disks; they establish a high-chirality interval boundary layer and numerical chirality effects for prescribed starts. Their high-chirality asymptotics and orientation-specific behaviors are not new here. They do not state the general fully absorbing, uniformly initialized, weak-swimming Dirichlet spectral Stieltjes law or the strict all-order hierarchy in squared chirality.

Iyaniwura and Peng (2025, arXiv:2506.15813v1) derive an achiral mean-exit PDE and a first-order weak-activity field for disks, annuli, and ellipses. Their source explicitly observes that the orientation-average correction starts at quadratic order; it does not compute this coefficient as a general-domain chiral Stieltjes transform. Their joint work on splitting probabilities (2026, arXiv:2603.13621v2) gives a quadratic weak-activity correction for **which exit is reached**, not for the **total mean exit time**; distinct boundary-value data prevent either statement from implying the other directly.

Baouche, Le Goff, Kurzthaler and Franosch (2025, arXiv:2503.05401v1) compute second-order perturbative **hitting-time distributions** for an achiral particle approaching an unbounded half-space wall, for which the mean hitting time diverges. Di Trapani, Franosch and Caraglio (2023, arXiv:2306.12702) give a spectral perturbation scheme for an achiral particle in an absorbing disk, which may already imply the special case \(\Omega=0\) in that geometry. Neither source contains the all-domain chiral complete-monotonicity statement.

Iyer, Novikov, Ryzhik and Zlatoš (2010, DOI:10.1137/090776895) investigate exit times with incompressible advection. This provides context for generic drift-energy comparisons; it does not by itself state the frequency-resolved first-orientation-harmonic response derived here. The spectral proof uses established PDE and operator theory, and novelty is claimed for the mathematically motivated combination and strict chirality law, not for those standard tools.

## Limitations

No claim is made for reflecting walls, partial absorption, spatially varying angular dynamics, degenerate translational diffusion, nonuniform initial distributions, or general monotonicity of mean time at finite nonzero swimming speed as chirality changes. Even for this fully absorbing setting, a truncated numerical spectral sum cannot establish the infinite series without Parseval and coercivity. External publication-priority coverage beyond the specified inspected primary literature remains a residual risk. No independent mathematical audit has been conducted.

## References

1. S. A. Iyaniwura, M. Qiu and Z. Peng, *Mean first passage time of chiral active Brownian particles* (2026), arXiv:2605.23095v1, https://arxiv.org/html/2605.23095v1.
2. S. A. Iyaniwura and Z. Peng, *Mean first passage time of active Brownian particles in two dimensions* (2025), arXiv:2506.15813v1, https://arxiv.org/html/2506.15813v1.
3. S. A. Iyaniwura and Z. Peng, *Splitting probabilities of confined chiral active Brownian particles* (2026), arXiv:2603.13621v2, https://arxiv.org/html/2603.13621v2.
4. Y. Baouche, M. Le Goff, C. Kurzthaler and T. Franosch, *First-passage-time statistics of active Brownian particles: A perturbative approach* (2025), arXiv:2503.05401v1, https://arxiv.org/html/2503.05401v1.
5. F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian particles in a circular disk with an absorbing boundary* (2023), arXiv:2306.12702, https://arxiv.org/abs/2306.12702.
6. G. Iyer, A. Novikov, L. Ryzhik and A. Zlatoš, *Exit Times of Diffusions with Incompressible Drift*, SIAM J. Math. Anal. 42 (2010), DOI:10.1137/090776895, https://doi.org/10.1137/090776895.
