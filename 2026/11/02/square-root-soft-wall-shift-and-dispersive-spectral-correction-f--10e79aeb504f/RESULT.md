# Square-root soft-wall shift and dispersive spectral correction for penalized interval diffusion

## Finding

Let \(a>0\) and \(n>0\). Write \(P_a\) for metric projection onto \([-a,a]\) and consider
\[
dX_t=-n(X_t-P_aX_t)\,dt+\sqrt{2}\,dB_t.
\]
Its invariant probability density is proportional to \(\exp[-n\operatorname{dist}(x,[-a,a])^2/2]\). Let \(0=\lambda_0(n)<\lambda_1(n)<\cdots\) be the eigenvalues of \(-\mathcal L_n\) on the invariant \(L^2\) space, where \(\mathcal L_nf=f''-n(x-P_ax)f'\).

Put
\[
\beta=\sqrt{\pi/2},\qquad d=\beta(\log 2-\pi/6)>0,\qquad
\kappa_j=j\pi/2,\qquad A_n=a+\beta n^{-1/2}.
\]
**Theorem.** For every fixed \(a>0\) and every fixed integer \(j\ge1\),
\[
\boxed{\displaystyle \lambda_j(n)=\frac{\kappa_j^2}{A_n^2}-\frac{2d\kappa_j^4}{A_n^5n^{3/2}}+O_{a,j}(n^{-5/2})\quad(n\to\infty).}
\]
In particular, \(\lambda_1(n)=\pi^2/(4a^2)-\beta\pi^2 n^{-1/2}/(2a^3)+O_a(n^{-1})\). The first correction not explained by enlarging the interval half-width from \(a\) to \(A_n\) is negative and proportional to the fourth power of the mode number. Its coefficient is \(-2d\kappa_j^4/a^5\).

The exact low-eigenvalue equation, valid for all sufficiently large \(n\) depending on \(a,j\), is
\[
\boxed{\displaystyle ak+\arctan\!\left(\frac{\sqrt n}{k}R(k^2/n)\right)=\kappa_j,\quad k=\sqrt{\lambda_j(n)},\quad R(\nu)=\frac{\nu}{\sqrt2}\frac{\Gamma((1-\nu)/2)}{\Gamma(1-\nu/2)}.}
\]
For the root under discussion, \(0<k^2/n<1\). No exact equation for arbitrarily high modes at fixed \(n\) is asserted.

## Assumptions and scope

The state space is the full real line, not the reflected interval. The drift is piecewise linear and continuous at \(\pm a\); the noise coefficient is \(\sqrt2\), not \(1\). The invariant measure is normalized from \(\exp(-V_n)\), where \(V_n(x)=n\operatorname{dist}(x,[-a,a])^2/2\). The low-index limit fixes \(a,j\) and sends \(n\) to infinity. The eigenvalues are those of the **positive** self-adjoint operator \(-\mathcal L_n\), in increasing order, with \(\lambda_0=0\). For a penalty-strength-one diffusion at noise temperature \(T=1/n\), time rescaling divides these eigenvalues by \(n\).

## Proof

**1. Self-adjointness and discrete spectrum.** Since \(\mathcal L_n f=e^{V_n}(e^{-V_n}f')'\), its Dirichlet form is \(\int |f'|^2e^{-V_n}\,dx\), up to normalization. Conjugation by \(e^{-V_n/2}\) gives the Schrödinger operator
\[
-\partial_x^2+\frac14(V_n')^2-\frac12 V_n'',
\]
where the potential is zero on \((-a,a)\) and \(n^2(|x|-a)^2/4-n/2\) outside (in the a.e. sense). Since it grows quadratically at infinity, the resolvent is compact. Standard one-dimensional Sturm oscillation implies that all eigenvalues are simple and the eigenfunction of \(\lambda_j\) has exactly \(j\) zeros. The zero eigenvalue is attained by the constant function.

**2. Exact exterior Dirichlet-to-Neumann ratio.** For an eigenvalue \(\lambda=k^2>0\), the eigenfunction on \((0,a)\) is a multiple of \(\sin(kx)\) for odd parity and \(\cos(kx)\) for even parity. On \(x>a\), set \(z=\sqrt n(x-a)\), \(\nu=k^2/n\). The eigen-equation becomes
\[
u''(z)-zu'(z)+\nu u(z)=0.
\]
(Here \(u\) denotes the eigenfunction in the \(z\) coordinate, while \(\nu\) is the order.) The unique, up to scalar, solution square-integrable against \(e^{-z^2/2}dz\) at infinity is \(u(z)=e^{z^2/4}D_\nu(z)\), where \(D_\nu\) is the parabolic cylinder function. The other independent asymptotic solution grows as \(e^{z^2/2}\) times an algebraic factor, which is not square-integrable. The classical values
\[
D_\nu(0)=\frac{2^{\nu/2}\sqrt\pi}{\Gamma((1-\nu)/2)},\qquad
D_\nu'(0)=-\frac{2^{(\nu+1)/2}\sqrt\pi}{\Gamma(-\nu/2)}
\]
give
\[
\frac{u'(0)}{u(0)}=-\sqrt2\frac{\Gamma((1-\nu)/2)}{\Gamma(-\nu/2)}=R(\nu).
\]
For \(0<\nu<1\), \(D_\nu(0)>0\), \(R(\nu)>0\), and the polynomially growing solution is strictly positive on \([0,\infty)\). One way to justify positivity is to identify its normalized version with the finite exponential moment \(\mathbb E_z e^{\nu\tau_0}\) for the Ornstein–Uhlenbeck diffusion with generator \(\partial_z^2-z\partial_z\) killed upon hitting zero; its first Dirichlet eigenvalue on \((0,\infty)\) is \(1\). Hence the exterior contributes no zero to sufficiently low modes.

**3. Matching and Sturm indexing.** Continuity of the eigenfunction and its first derivative at \(a\) gives \(k\cot(ka)=\sqrt n R(k^2/n)\) for odd eigenfunctions and \(-k\tan(ka)=\sqrt n R(k^2/n)\) for even eigenfunctions. With
\[
\theta_n(k)=\arctan\bigl(\sqrt nR(k^2/n)/k\bigr),
\]
the branch whose even/odd extension has exactly \(j\) zeros on the whole line satisfies \(ak+\theta_n(k)=j\pi/2\) for all sufficiently large \(n\). For fixed \(j\), the implicit-function theorem near \(k=\kappa_j/a\) gives a unique root approaching this value; its interior and exterior nodal counts identify it as \(\lambda_j\). The same argument holds for both parities and proves the exact characteristic equation claimed above.

**4. Expansion.** Writing \(s=n^{-1/2}\), the regular gamma quotient gives, uniformly for \(k\) near \(\kappa_j/a\),
\[
R(k^2s^2)=\beta k^2s^2\bigl(1+k^2s^2\log2+O_{a,j}(s^4)\bigr).
\]
The logarithmic coefficient follows from \(\psi(1)-\psi(1/2)=2\log2\). Expanding arctangent yields
\[
\theta_n(k)=\beta ks+d k^3s^3+O_{a,j}(s^5),
\qquad d=\beta\log2-\beta^3/3=\beta(\log2-\pi/6).
\]
Since \(\log2>\pi/6\), \(d>0\). Set \(A=a+\beta s\). The eigenvalue equation is \(Ak+dk^3s^3+O(s^5)=\kappa_j\), hence
\[
k=\frac{\kappa_j}{A}-\frac{d\kappa_j^3s^3}{A^4}+O_{a,j}(s^5).
\]
Squaring gives \(k^2=\kappa_j^2/A^2-2d\kappa_j^4s^3/A^5+O_{a,j}(s^5)\), which proves the theorem.

## Verification

The standalone file `verify.py` uses high-precision special functions to check the gamma quotient against derivatives of parabolic-cylinder functions, verifies the exterior differential equation, solves the exact characteristic equation, tests the effective-length and dispersive corrections for multiple interval sizes and modes, and independently approximates the low spectrum using the symmetrized Schrödinger operator on a fine grid. The recorded output is `verification_output.txt`. The script passed 378 assertions in the recorded run. No finite sample establishes the asymptotic remainder or exhaustive spectral ordering; those follow from the analytic and Sturm arguments above.

## Relationship to prior work

Mane, *Convergence of Reflected Langevin Diffusion for Constrained Sampling* (arXiv:2512.00386), introduces the metric-projection penalized Langevin process, studies invariant-measure convergence in Wasserstein distance and discretization, and motivates quantitative control of the penalty limit. The present model is its one-dimensional zero-interior-potential specialization. Its main new quantity is **the complete fixed-low-mode spectral expansion**, not stationary-measure convergence.

Gürbüzbalaban, Hu and Zhu's *Penalized Overdamped and Underdamped Langevin Monte Carlo Algorithms for Constrained Sampling* (arXiv:2212.00570) supplies an earlier penalty-sampling framework and complexity bounds. Darapaneni's *Zero temperature versus long time for diffusions driven by metric projections onto convex sets* (arXiv:2610.35145, first posted 26 October 2026) considers the same squared-distance potential under a different time normalization and gives general convergence-to-equilibrium statements. Its introductory theorem and mixing statements do not provide the exact interval eigenvalue expansion above; its later appearance makes it supporting literature rather than the age-qualifying primary source. Standard parabolic-cylinder evaluations are classical special-function identities, not presented as novel.

## Limitations

The theorem treats a centered one-dimensional interval, zero potential inside the interval, constant Brownian diffusivity and a quadratic metric-distance penalty. Constants in the remainder depend on the fixed eigenvalue index and interval half-width. The result does not assert uniformity as the mode index grows with the penalty or a sharp high-dimensional mixing theorem. Existing special-function treatments of piecewise Ornstein–Uhlenbeck processes might imply the formula without the same parameterization; historical-priority review remains open. Independent mathematical audit has not been performed.

## References

1. T. Mane, *Convergence of Reflected Langevin Diffusion for Constrained Sampling*, arXiv:2512.00386 (first public record dated 29 November 2025), https://arxiv.org/abs/2512.00386.
2. M. Gürbüzbalaban, Y. Hu, L. Zhu, *Penalized Overdamped and Underdamped Langevin Monte Carlo Algorithms for Constrained Sampling*, J. Mach. Learn. Res. 25 (2024), article 263, https://jmlr.org/papers/v25/22-1443.html.
3. N. Darapaneni, *Zero temperature versus long time for diffusions driven by metric projections onto convex sets*, arXiv:2610.35145v1 (26 October 2026), https://arxiv.org/html/2610.35145v1.
4. NIST Digital Library of Mathematical Functions, Chapter 12, *Parabolic Cylinder Functions*, https://dlmf.nist.gov/12.2.
