# Sharp angular minimax calibration of an inexact rank-one spectral preconditioner

## Finding

Consider a real symmetric positive-definite two-mode system with eigenvalues \(\kappa>1\) and \(1\). A rank-one spectral limited-memory preconditioner is constructed from an approximate dominant Ritz vector, whose angle from the true dominant eigenvector is unknown but bounded by \(\Phi\in[0,\pi/4]\). Its fixed positive scaling \(\theta\) is chosen before the unknown angle is revealed. Among all fixed positive scalings, the **unique** minimax choice and the exact worst-case spectral condition number are

\[
\boxed{\theta_*=1+(\kappa-1)\sin^2\Phi},
\qquad
\boxed{\mathcal K_*=(\sqrt{1+z}+\sqrt z)^2},
\qquad
z=\frac{(\kappa-1)^2}{\kappa}\sin^2\Phi\cos^2\Phi.
\]

The worst angle for this optimal calibration is exactly \(\Phi\). At \(\Phi=0\) the minimum is \(1\); for \(0<\Phi<\pi/4\) it lies strictly between \(1\) and the raw condition number \(\kappa\); at \(\Phi=\pi/4\) it equals \(\kappa\).

For the common unshifted target \(\theta=1\), the preconditioner is **worse than no preconditioner** precisely when

\[
\sin^2\varphi>\frac{2}{3+\sqrt{4\kappa+5}},\qquad 0\le\varphi\le\pi/4.
\]

Equality gives the original condition number. This non-worsening cutoff has angular scale \(\kappa^{-1/4}\) as \(\kappa\to\infty\). In contrast, the optimally recalibrated worst-case condition number stays bounded with increasing \(\kappa\) if and only if \(\Phi=O(\kappa^{-1/2})\). More precisely, when \(\sqrt\kappa\Phi\to c\ge0\), it approaches \((\sqrt{1+c^2}+c)^2\).

## Assumptions and scope

After an orthogonal change of coordinates and normalization by the smaller eigenvalue, set \(H=\operatorname{diag}(\kappa,1)\) with \(\kappa>1\). Let \(u_\varphi=(\cos\varphi,\sin\varphi)^\mathsf T\) be a unit approximate leading vector, where \(\varphi\in[0,\Phi]\), \(0\le\Phi\le\pi/4\). Its Rayleigh quotient is \(\rho_\varphi=u_\varphi^\mathsf THu_\varphi\). The rank-one Rayleigh-normalized spectral preconditioner is

\[
P_\theta(\varphi)=I+\left(\frac{\theta}{\rho_\varphi}-1\right)u_\varphi u_\varphi^\mathsf T,
\qquad \theta>0.
\]

It is positive definite. Measure spectral conditioning by \(\mathcal K_\theta(\varphi)=\kappa_2(P_\theta^{1/2}HP_\theta^{1/2})\), the ratio of its largest to smallest eigenvalues. A single \(\theta\), independent of \(\varphi\), must minimize \(\sup_{0\le\varphi\le\Phi}\mathcal K_\theta(\varphi)\). The preconditioner is a two-dimensional exact-arithmetic model of one inexact spectral Ritz direction, not a claim about arbitrary dimensions, matrix-free implementations, or whole conjugate-gradient iterations.

## Proof

**1. Exact characteristic invariant.** Put \(r=\sin^2\varphi\), \(R=\sin^2\Phi\), and \(d=\kappa-1>0\). In the orthonormal frame \((u_\varphi,v_\varphi)\), where \(v_\varphi=(-\sin\varphi,\cos\varphi)^\mathsf T\), the original matrix has diagonal entries

\[
\rho=\kappa-dr,\qquad \sigma=1+dr,
\]

and an off-diagonal entry with absolute value \(d\sqrt{r(1-r)}\). Since \(P_\theta^{1/2}\) acts by \(\sqrt{\theta/\rho}\) on \(u_\varphi\) and by \(1\) on \(v_\varphi\), its SPD congruence has diagonal entries \(\theta,\sigma\) and off-diagonal magnitude \(d\sqrt{\theta r(1-r)/\rho}\). Thus

\[
T=\operatorname{tr}(P_\theta^{1/2}HP_\theta^{1/2})=\theta+\sigma,
\qquad
D=\det(P_\theta^{1/2}HP_\theta^{1/2})=\frac{\theta\kappa}{\rho}.
\]

For any SPD two-by-two matrix, its eigenvalue ratio increases strictly with \(T^2/D\), since \(T^2/D=\mathcal K+2+\mathcal K^{-1}\) and \(\mathcal K\ge1\). Therefore it suffices to minimize and maximize

\[
F(\theta,r)=\frac{(\theta+1+dr)^2(\kappa-dr)}{\kappa\theta}.
\]

**2. Pointwise lower bound and minimax attainment.** For fixed \(r\), \(F(\theta,r)=(\rho/\kappa)(\theta+2\sigma+\sigma^2/\theta)\). The arithmetic-geometric mean inequality gives a unique minimum at \(\theta=\sigma\). In particular, every fixed scale must have

\[
\sup_{0\le r\le R}F(\theta,r)\ge F(\sigma_R,R),\qquad \sigma_R=1+dR.
\]

Choose \(\theta_*=\sigma_R\). Direct differentiation gives

\[
\frac{\partial}{\partial r}\big[(\theta_*+1+dr)^2(\kappa-dr)\big]
=d(\theta_*+1+dr)\big[2(\kappa-dr)-\theta_*-1-dr\big].
\]

For \(0\le r\le R\le1/2\), one has \(\kappa-dr\ge\kappa-dR\ge1+dR=\theta_*\ge1+dr\). Therefore the derivative is nonnegative. The supremum of \(F(\theta_*,r)\) occurs at \(R\); it equals the unavoidable endpoint lower bound. The endpoint pointwise optimizer is unique, so \(\theta_*\) is the unique global minimax scale, including \(R=0\) and \(R=1/2\).

At \(\theta=\sigma_R\), the endpoint matrix has equal diagonals and off-diagonal magnitude \(d\sqrt{\sigma_R R(1-R)/\rho_R}\). Its correlation \(q\) has \(q^2=d^2 R(1-R)/(\rho_R\sigma_R)\), while \(\rho_R\sigma_R=\kappa+d^2R(1-R)\). Thus its condition number is \((1+q)/(1-q)=(\sqrt{1+z}+\sqrt z)^2\), with \(z=d^2R(1-R)/\kappa\). The endpoint assertions follow from the strict increase of \(R(1-R)\) on \([0,1/2)\) and the identity \(z_{R=1/2}=d^2/(4\kappa)\), which yields \(\mathcal K_*=\kappa\).

**3. Sharp unshifted misalignment barrier.** At \(\theta=1\), comparison with the unpreconditioned invariant \((\kappa+1)^2/\kappa\), with positive denominators cleared, produces the exact identity

\[
(2+dr)^2(\kappa-dr)-(\kappa+1)^2=d^2(1-r)(dr^2+3r-1).
\]

The quadratic on the right is strictly increasing on \(r\ge0\) and has one positive zero

\[
r_{\mathrm{crit}}=\frac{\sqrt{9+4d}-3}{2d}=\frac{2}{3+\sqrt{4\kappa+5}}.
\]

Its location is in \((0,1/3)\); hence it lies in the admitted interval \([0,1/2]\). The sign of the factorization proves the exact strict-worsening, equality and improvement regions. As \(\kappa\to\infty\), \(r_{\mathrm{crit}}\sim\kappa^{-1/2}\) and \(\arcsin\sqrt{r_{\mathrm{crit}}}\sim\kappa^{-1/4}\).

**4. Uniform conditioning criterion.** The monotone function \(z\mapsto(\sqrt{1+z}+\sqrt z)^2\) stays bounded exactly when \(z\) does. For \(R\in[0,1/2]\), \(R/2\le R(1-R)\le R\). Thus as \(\kappa\to\infty\) the minimax conditioning is bounded exactly when \(\kappa R\) is bounded, equivalently \(\Phi=O(\kappa^{-1/2})\). If \(\sqrt\kappa\Phi\to c\), then \(z\to c^2\) and the stated limit follows by continuity. The case \(c=0\) includes exact alignment.

## Verification

The supplied standalone `verify.py` uses standard-library exact fractions for 5,913 factorization identities, evaluates the minimax formula and its entire sampled angle range against alternate scalings, checks the strict-worsening cutoff, and independently reconstructs the two eigenvalues from trace and determinant. One deterministic run returned `VERIFY_OK 42521`. These finite checks are supplementary: the four algebraic proof steps establish the universal quantifiers for every \(\kappa>1\), \(0\le\Phi\le\pi/4\), \(\theta>0\) and \(\varphi\in[0,\Phi]\).

For illustration, at \(\kappa=100\) and \(\Phi=\pi/6\), the optimum is \(\theta_*=25.75\) with worst-case condition approximately \(75.494254\); the unshifted choice \(\theta=1\) has condition approximately \(536.458917\) at that same worst angle, compared with raw condition \(100\).

## Relationship to prior work

Daužickaitė, Gürol, Destouches, Berre and Weaver (2026, Section 3.1, equations (7)–(8)) study randomized spectral limited-memory preconditioners and scaled eigenvalue clustering. Their numerical experiments compare scaling heuristics and observe sensitivity to approximate eigendirections; they do not give this exact angular uncertainty minimax law. Diouane, Gürol, Mouhtal and Orban (2026, Sections 3–4 and Appendix A) optimize scaled spectral preconditioners for a fixed conjugate-gradient iteration budget using ideal spectral information and an energy-error objective, not the present unknown-angle worst-case spectral condition objective. Giraud and Gratton (2006, Sections 3.2–3.3) study sensitivity of multiple spectral preconditioners using first-order perturbative eigenvalue formulas; their stated results do not imply the global finite-angle minimax optimizer or the exact strict-worsening cutoff. The exact rank-one two-mode calculation shares standard SPD spectral and Rayleigh-quotient ingredients with this literature; independent historical priority remains unverified.

## Limitations

The rank-one Ritz direction is assumed to be exactly unit-normalized and to have a known acute angular upper bound not exceeding \(45^\circ\). Both the larger and smaller eigenvalues of the two-mode system are assumed known to define \(\kappa\); numerical estimation or uncertainty in these values is not addressed. The optimum depends on that angular uncertainty bound, and the model is not an adaptive estimator of it. Results are for a Rayleigh-normalized spectral LMP, not every Nyström, coarse-grid, or multilevel preconditioner. No claims are made about nonsymmetric or indefinite systems, more than two eigenmodes, measured finite-precision conditioning, or complete Krylov solver speedups. Originality is assessed against the cited inspected sources rather than asserted as a definitive exhaustive historical theorem.

## References

1. I. Daužickaitė, S. Gürol, M. Destouches, L. Berre, A. T. Weaver, *Accelerating an ensemble of variational data assimilations with randomized preconditioning*, arXiv:2605.23571, first posted 2026-05-22. https://arxiv.org/html/2605.23571v2
2. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969, 2026-03-30. https://arxiv.org/html/2603.28969v1
3. L. Giraud, S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl. 27(4) (2006), 1089–1105, DOI:10.1137/040617546. Author-supplied full text: https://www.researchgate.net/publication/220656613_On_the_Sensitivity_of_Some_Spectral_Preconditioners
4. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *An Efficient Scaled Spectral Preconditioner for Sequences of Symmetric Positive Definite Linear Systems*, arXiv:2410.02204, 2024-10-03. https://arxiv.org/abs/2410.02204
