# A Gaussian-kernel bandwidth threshold separating isospectral three-state Markov chains

## Finding
For the three sites at spatial positions \(0,1,2\), set \(k_h(i,j)=\exp[-h(i-j)^2]\), with \(h>0\). Let \(\pi=(1/3,1/3,1/3)\). Consider the two strictly positive, symmetric Markov transition matrices
\[
P_{\mathrm{adj}}=\begin{pmatrix}7/12&1/12&1/3\\1/12&7/12&1/3\\1/3&1/3&1/3\end{pmatrix},\qquad
P_{\mathrm{end}}=\begin{pmatrix}7/12&1/3&1/12\\1/3&1/3&1/3\\1/12&1/3&7/12\end{pmatrix}.
\]
Both have invariant law \(\pi\), spectrum \(\{1,1/2,0\}\), absolute \(L^2(\pi)\) spectral gap \(1/2\), and total-variation one-step contraction coefficient \(1/2\). For any such transition matrix define its *sharp equilibrium MMD amplification*
\[
\Gamma_h(P):=\sup_{\mu\in\mathcal P(\{0,1,2\}),\,\mu\ne\pi}
\frac{\operatorname{MMD}_{k_h}(\mu P,\pi)}{\operatorname{MMD}_{k_h}(\mu,\pi)}.
\]
Put \(t=e^{-h}\) and
\[
R(t)=\frac{t^2(1+t+t^2)^2}{3+2t+2t^2+2t^3}.
\]
Then, for every \(h>0\),
\[
\boxed{\Gamma_h(P_{\mathrm{adj}})=\frac1{2\sqrt{1-R(e^{-h})}},\qquad
\Gamma_h(P_{\mathrm{end}})=\frac12.}
\]
There is a **unique** \(t_*\in(0,1)\) solving
\[
4t^6+8t^5+12t^4+2t^3-2t^2-6t-9=0,
\]
namely \(t_*=0.897711590608780\ldots\). Set \(h_*=-\log t_*=0.107906430852718\ldots\). The first chain amplifies the Gaussian-kernel MMD to equilibrium for some nonstationary probability law precisely when \(0<h<h_*\), is nonexpansive for every probability law when \(h\ge h_*\), and obeys the sharp broad-kernel asymptotic
\[
\Gamma_h(P_{\mathrm{adj}})\sim\sqrt{\frac3{32h}},\qquad h\downarrow0.
\]
The second chain remains an exact factor-\(1/2\) contraction at every bandwidth. Thus fixed spectral gap, reversibility, strict positivity and identical total-variation mixing do **not** determine Gaussian-MMD one-step contractivity, even on the smallest nontrivial three-state space.

## Assumptions and scope
The chain evolves in discrete time on the ordered state space \(\{0,1,2\}\), with row-vector laws and the stated matrices. The Gaussian kernel is the Gram matrix of the Euclidean positions and has entries \(K_h=(e^{-h(i-j)^2})_{i,j=0}^2\). MMD is defined by \(\operatorname{MMD}_{k_h}(\mu,\nu)^2=(\mu-\nu)K_h(\mu-\nu)^{\mathsf T}\). Every \(h>0\) is included, but the degenerate limiting kernel at \(h=0\) is not. Supremums are over actual probability laws, not just unconstrained signed vectors; equality of the two suprema is proved below. The first chain's gain is a *one-step* comparison to stationarity, not a claim that all trajectories grow indefinitely. No bound for other geometries or dimensions is asserted.

## Proof
**(1) Legitimate kernel and spectral data.** The Gaussian Gram matrix is strictly positive definite for three distinct positions. Indeed, the Gaussian Fourier identity writes the quadratic form of an arbitrary nonzero coefficient vector \(a\) as a positive multiple of
\[
\int_{\mathbb R}e^{-\omega^2/(4h)}\left|\sum_{j=0}^2a_j e^{i\omega j}\right|^2\,d\omega>0.
\]
The trigonometric polynomial cannot vanish identically unless all coefficients vanish. Hence MMD is nonzero for \(\mu\ne\pi\). Direct multiplication gives the claimed invariant laws and spectra. In fact, with
\[
u=\frac{(1,-1,0)}{\sqrt2},\quad v=\frac{(1,1,-2)}{\sqrt6},\quad
w=\frac{(1,0,-1)}{\sqrt2},
\]
and with \(\Pi\) the all-\(1/3\) matrix, the kernels are \(P_{\mathrm{adj}}=\Pi+uu^{\mathsf T}/2\) and \(P_{\mathrm{end}}=\Pi+ww^{\mathsf T}/2\). The total-variation Dobrushin coefficient is the maximum half row \(\ell^1\)-distance, which equals \(1/2\) for both matrices.

**(2) Exact MMD gain of the adjacent-mode chain.** Every signed row vector \(q\) with total mass zero is \(q=z_1u^{\mathsf T}+z_2v^{\mathsf T}\). In this basis \(qP_{\mathrm{adj}}=z_1u^{\mathsf T}/2\). Write \(t=e^{-h}\). Direct evaluation of the restriction of \(K_h\) to the zero-mass subspace gives the positive definite Gram matrix
\[
G_h=\begin{pmatrix}a&c\\c&b\end{pmatrix},\quad
a=1-t,\quad b=1-\frac t3-\frac{2t^4}3,\quad c=\frac{t-t^4}{\sqrt3}.
\]
Consequently
\[
\frac{\operatorname{MMD}_{k_h}(qP_{\mathrm{adj}},0)^2}{\operatorname{MMD}_{k_h}(q,0)^2}
=\frac{a z_1^2/4}{az_1^2+2cz_1z_2+bz_2^2}.
\]
Completing the square in the denominator yields the exact maximum \(ab/[4(ab-c^2)]\), attained by any nonzero \((z_1,z_2)\) proportional to \((b,-c)\). Every such signed vector can be scaled by a sufficiently small positive number \(\varepsilon\) so that \(\pi+\varepsilon q\) is a strictly positive probability law. Thus the unconstrained ratio is exactly the supremum over actual probability measures in the theorem. Algebra gives
\[
\frac{c^2}{ab}=
\frac{t^2(1+t+t^2)^2}{3+2t+2t^2+2t^3}=R(t),
\]
and the first boxed identity follows.

**(3) Unique threshold and strict direction.** Differentiating the rational function gives
\[
R'(t)=\frac{2t(1+t+t^2)(1+2t+3t^2)(3+t+t^2+t^3)}{(3+2t+2t^2+2t^3)^2}>0
\]
for every \(0<t<1\). Moreover \(R(0)=0\) and \(R(1)=1\). Therefore \(\Gamma_h(P_{\mathrm{adj}})>1\) exactly when \(R(e^{-h})>3/4\). A unique threshold exists; clearing denominators yields the displayed degree-six polynomial. Evaluating it at \(8977/10000\) and \(8978/10000\) yields opposite signs, which also brackets the unique root. Since \(e^{-h}\) decreases strictly as \(h\) increases, the claimed phase order follows. Its displayed decimals are approximations, not definitions.

**(4) Sharp broad-kernel growth.** Taylor expansion at \(h=0\), with \(t=e^{-h}\), gives
\[
ab=3h^2-7h^3+O(h^4),\qquad ab-c^2=8h^3+O(h^4).
\]
Therefore \(\Gamma_h(P_{\mathrm{adj}})^2=3/(32h)+O(1)\), proving the asymptotic. As \(h\to\infty\), \(t\to0\) and the gain tends to \(1/2\).

**(5) Reflection-compatible chain.** For \(P_{\mathrm{end}}\), take \(w=(1,0,-1)/\sqrt2\) and \(v'=(1,-2,1)/\sqrt6\). The Gram matrix \(K_h\) is invariant under exchanging sites \(0\) and \(2\), so \(wK_h(v')^{\mathsf T}=0\) for every \(h>0\). Moreover \(P_{\mathrm{end}}\) kills the \(v'\) mode and multiplies the \(w\) mode by \(1/2\). Orthogonality in the MMD metric gives a universal gain at most \(1/2\), attained by any sufficiently small nonzero probability perturbation along \(w\). This proves the second boxed identity and the comparison. On two states the zero-mass space is one-dimensional, so every strictly positive two-state Markov chain has MMD gain equal to the modulus of its sole nontrivial eigenvalue, independent of the strictly positive definite kernel; three states are minimal for the phenomenon.

## Verification
The companion standalone script `verify_gaussian.py` uses only Python standard libraries. It checks exact Markov stochasticity, reversibility, the two spectra, total-variation contraction, the restricted-kernel determinant and the rational identity for \(R\) at 999 rational parameter values. It also checks the explicit threshold interval, the exact positive-factor derivative against finite differences, and seven direct Gaussian Gram-matrix evaluations. These finite checks support but do not replace the analytic proofs of strict monotonicity, kernel positivity, uniqueness of the threshold, or the singular asymptotic.

## Relationship to prior work
Kachaiev, Brogat-Motte, Villa and Rosasco (2026, arXiv:2610.13916v1) separate absolute \(L^2(\pi)\) spectral-gap and kernel-induced relaxation assumptions, explicitly distinguish one-step contraction from relaxation of iterates, and provide Fourier-domain examples for expanding noisy maps. Their stated results do not give a sharp Gaussian-bandwidth criterion for two isospectral, strictly positive, three-state reversible chains on equally spaced sites. The present comparison quantifies a different finite-state geometric boundary. Demmel (1983) gives general sharp condition-number bounds for similarity transformations of matrices; those linear-algebra facts are compatible with this analysis, but the present exact Gaussian bandwidth function, critical polynomial, isospectral comparison and \(h^{-1/2}\) coefficient require the specific probability kernel and Gaussian Gram calculation. Classical kernel characteristicness and Markov divergence-contraction results provide background rather than this formula.

## Limitations
The theorem concerns a particular natural three-point location geometry and two explicit rank-one perturbation chains, not an all-kernel or all-chain classification. One-step MMD amplification does not contradict convergence to stationarity: both chains have positive entries and geometric mixing, and the first has \(P_{\mathrm{adj}}^m=\Pi+2^{-m}uu^{\mathsf T}\) for \(m\ge1\). A large ratio arises when the initial probability perturbation has small Gaussian-MMD norm. The source literature and database search did not establish exhaustive global priority; differently phrased earlier Gaussian-kernel similarity or finite-Markov results remain an originality risk. No independent audit or peer review has been performed.

## References
- O. Kachaiev, L. Brogat-Motte, S. Villa, L. Rosasco, *Markov Chain Convergence in Kernel-Induced Geometry*, arXiv:2610.13916v1 (first public 2026-10-09), https://arxiv.org/html/2610.13916v1 .
- J. W. Demmel, *The Condition Number of Similarities that Diagonalize Matrices*, Technical Report UCB/CSD-83-127 (1983), https://www2.eecs.berkeley.edu/Pubs/TechRpts/1983/CSD-83-127.pdf .
- P. Caputo, Z. Chen, Y. Gu, Y. Polyanskiy, *Entropy Contractions in Markov Chains: Half-Step, Full-Step and Continuous-Time*, arXiv:2409.07689 (2024), https://arxiv.org/abs/2409.07689 .
- A. Gretton et al., *A Kernel Two-Sample Test*, Journal of Machine Learning Research 13 (2012), 723–773, https://jmlr.org/papers/v13/gretton12a.html .
