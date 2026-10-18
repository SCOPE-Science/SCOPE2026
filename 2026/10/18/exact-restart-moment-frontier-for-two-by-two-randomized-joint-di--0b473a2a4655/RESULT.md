# Exact restart-moment frontier for two-by-two randomized joint diagonalization

## Finding

For each real \(0<\varepsilon<1\), consider the symmetric matrix pair
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
B_\varepsilon=\varepsilon\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For each of \(L\ge1\) independent trials, sample \((g_1,g_2)\) from the standard bivariate Gaussian, compute any orthogonal eigenbasis of \(g_1 A+g_2 B_\varepsilon\), and return the trial with the smallest joint squared off-diagonal Frobenius loss
\[
\mathcal L(Q)=\|\operatorname{offdiag}(Q^{\mathsf T}AQ)\|_F^2+
\|\operatorname{offdiag}(Q^{\mathsf T}B_\varepsilon Q)\|_F^2.
\]
This is the basic best-of-\(L\) randomized joint diagonalization (RJD) algorithm of He and Kressner, with exact eigenvector arithmetic. Let \(\mathcal L_L\) denote its returned loss. Let \(\Theta_{(1)}\) be the minimum of \(L\) independent uniform random variables on \((0,\pi/2)\). Then
\[
\mathcal L_L\ \overset{d}=\ 
\frac{2\varepsilon^2}{\cos^2\Theta_{(1)}+\varepsilon^2\sin^2\Theta_{(1)}}.
\]
In particular the expectation is exactly
\[
\mathbb E\mathcal L_L=\frac{4L\varepsilon^2}{\pi}
\int_0^{\pi/2}\frac{(1-2\theta/\pi)^{L-1}}{\cos^2\theta+\varepsilon^2\sin^2\theta}\,d\theta.
\]
As \(\varepsilon\downarrow0\), the sharp leading laws are
\[
\begin{aligned}
\mathbb E\mathcal L_1&=2\varepsilon\quad\text{exactly},\\
\mathbb E\mathcal L_2&\sim\frac{16}{\pi^2}\varepsilon^2\log(1/\varepsilon),\\
\mathbb E\mathcal L_3&\sim\frac{48\log2}{\pi^2}\varepsilon^2,\\
\mathbb E\mathcal L_L&\sim C_L\varepsilon^2\qquad(L\ge3),
\end{aligned}
\]
where the finite, positive constant is
\[
C_L=\frac{4L}{\pi}\int_0^{\pi/2}(1-2\theta/\pi)^{L-1}\sec^2\theta\,d\theta.
\]
The optimal orthogonal joint squared loss is exactly \(2\varepsilon^2\). Hence three independent best-of trials are **necessary and sufficient on this pair** for the expected squared residual to remain bounded by a constant multiple of the optimal residual as \(\varepsilon\downarrow0\); one and two trials incur, respectively, an unbounded inverse-linear and logarithmic ratio. No minimality claim for arbitrary other algorithms is made.

## Assumptions and scope

All matrices and coefficient vectors are real. The matrices are exactly \(2\times2\), \(0<\varepsilon<1\), and trials are independent with isotropic standard normal coefficients. Eigenproblems and loss comparisons are solved exactly. Eigenbasis sign, permutation and zero-probability spectral ties do not change the loss. The input is a perturbation of the commuting pair \((A,0)\), with combined Frobenius perturbation size \(\sqrt2\,\varepsilon\). The expectation concerns the *squared Frobenius off-diagonal residual*, not the unsquared residual, the solution error, or a runtime statistic.

## Proof

**Eigenbasis loss.** A real orthogonal basis in dimension two is, up to signs and permutations, a rotation through an angle \(\alpha\). Direct conjugation shows that the two squared off-diagonal Frobenius norms are \(2\sin^2(2\alpha)\) and \(2\varepsilon^2\cos^2(2\alpha)\), respectively. Thus
\[
\mathcal L(Q)=2\sin^2(2\alpha)+2\varepsilon^2\cos^2(2\alpha).
\]
This is at least \(2\varepsilon^2\) for every \(Q\), with equality when \(\alpha\) is an integer multiple of \(\pi/2\). This proves the exact optimum.

For an eigenbasis of \(g_1A+g_2B_\varepsilon\), the traceless symmetric matrix has diagonal coefficient \(g_1\) and off-diagonal coefficient \(\varepsilon g_2\). Its eigendirections satisfy
\[
\sin^2(2\alpha)=\frac{\varepsilon^2g_2^2}{g_1^2+\varepsilon^2g_2^2},\qquad
\cos^2(2\alpha)=\frac{g_1^2}{g_1^2+\varepsilon^2g_2^2}.
\]
Substitution gives the *exact* one-trial squared loss
\[
\mathcal L(g_1,g_2)=
\frac{2\varepsilon^2(g_1^2+g_2^2)}{g_1^2+\varepsilon^2g_2^2}.
\]

**Order statistic.** Isotropy of the Gaussian coefficient vector makes its unsigned angle \(\Theta=\arctan|g_2/g_1|\) uniform on \((0,\pi/2)\); zero denominators have probability zero. Rewriting the loss gives
\[
\mathcal L(\Theta)=\frac{2\varepsilon^2}{\cos^2\Theta+\varepsilon^2\sin^2\Theta}.
\]
Because \(0<\varepsilon<1\), its denominator strictly decreases on \((0,\pi/2)\). Thus the loss increases strictly with \(\Theta\); the best-of-\(L\) choice uses the minimum angle. Its density is
\[
f_L(\theta)=\frac{2L}{\pi}\left(1-\frac{2\theta}{\pi}\right)^{L-1}\quad(0<\theta<\pi/2).
\]
Integrating the loss against this density proves the distributional formula and the exact expectation formula.

**One trial.** The elementary integral
\[
\int_0^{\pi/2}\frac{d\theta}{\cos^2\theta+\varepsilon^2\sin^2\theta}=\frac{\pi}{2\varepsilon}
\]
follows from \(t=\tan\theta\), yielding \(\mathbb E\mathcal L_1=2\varepsilon\) without an asymptotic remainder.

**Two-trial logarithm.** Substitute \(u=\pi/2-\theta\) and obtain
\[
\mathbb E\mathcal L_2=\frac{16\varepsilon^2}{\pi^2}\int_0^{\pi/2}
\frac{u}{\sin^2u+\varepsilon^2\cos^2u}\,du.
\]
Fix a sufficiently small constant \(\delta\in(0,\pi/4)\). The integrand is uniformly integrable on \([\delta,\pi/2]\), contributing \(O(1)\) to the integral. On \((0,\delta)\), Taylor bounds \(\sin^2u=u^2(1+O(u^2))\) and \(\cos^2u=1+O(u^2)\), uniform in \(0<\varepsilon<1\), show that the difference from \(u/(u^2+\varepsilon^2)\) has a bounded integral. Indeed the relative denominator perturbation is \(O(u^2)\), giving an absolute integrand error bounded by a constant multiple of \(u^3/(u^2+\varepsilon^2)\), integrable uniformly. Finally,
\[
\int_0^\delta\frac{u}{u^2+\varepsilon^2}\,du
=\log(1/\varepsilon)+O(1).
\]
Hence the full integral is \(\log(1/\varepsilon)+O(1)\), which proves the coefficient \(16/\pi^2\).

**Three or more trials.** After dividing the exact expectation by \(\varepsilon^2\), the pointwise limit of the integrand is \(4L(1-2\theta/\pi)^{L-1}\sec^2\theta/\pi\). It is dominated by this nonnegative function, because \(\cos^2\theta+\varepsilon^2\sin^2\theta\ge\cos^2\theta\). Near \(\theta=\pi/2\), put \(u=\pi/2-\theta\); the dominating function has order \(u^{L-3}\), which is integrable exactly for integers \(L\ge3\). Dominated convergence proves the finite constants \(C_L\). For \(L=3\),
\[
C_3=\frac{48}{\pi^3}\int_0^{\pi/2}u^2\csc^2u\,du
=\frac{96}{\pi^3}\int_0^{\pi/2}u\cot u\,du
=\frac{48\log2}{\pi^2},
\]
using integration by parts and the classical definite integral \(\int_0^{\pi/2}\log(\sin u)\,du=-(\pi/2)\log2\). Every integration-by-parts endpoint is finite; in particular \(u^2\cot u\to0\) as \(u\downarrow0\). Dividing the three rates by the exact optimum \(2\varepsilon^2\) proves the final necessary-and-sufficient statement.

## Verification

The accompanying `verify.py` is a standalone Python 3 standard-library checker. It verifies the rational two-by-two eigenbasis loss identities for 2,100 choices of parameters and coefficients, independently reconstructs 1,872 numerical eigenbases of the actual matrix pencils, and compares candidate choices and independently evaluates the expectation integral by composite Simpson quadrature. The one-trial expectation is compared to \(2\varepsilon\), and the triple-trial limiting constant is compared to \(48\log2/\pi^2\). Run `python verify.py` in the same directory. The expected output begins with `VERIFY_OK`. Numerical quadrature and the finite exact checks do not replace the analytical arguments, especially the uniform error estimate and dominated-convergence step.

## Relationship to prior work

He and Kressner introduced this exact best-of-\(L\) RJD algorithm and its off-diagonal squared Frobenius loss. Their Theorems 6 and 8 establish high-probability robustness under near commutativity; their Section 3.4 predicts and experimentally exhibits a failure-probability exponent equal to \(L\). These already imply useful sufficient mean-square bounds after appropriate tail integration and deterministic truncation. The present result is an *exact two-dimensional extremal example*: it gives the full loss law, sharp one- and two-trial divergence rates, the necessity of a third trial on the example, and the three-trial leading constant. It does not re-claim the algorithm, the tail upper bounds, or the previously observed failure exponent.

Related work on simultaneous diagonalization by congruence analyzes generalized matrix pencils rather than this orthogonal single-combination procedure. Work on joint eigenvalue extraction primarily studies Rayleigh-quotient errors, not the same best-of-trials off-diagonal loss. An equivalent specialized result outside the inspected sources remains possible; no independent priority validation has been performed.

## Limitations

The result applies only to the displayed two-by-two family and the particular isotropic Gaussian best-of-trials RJD algorithm. It does not prove the minimum number of trials for *every* near-commuting family, nor establish optimality against adaptive sampling or deterministic joint diagonalizers. The trial count depends on the squared-loss expectation: high-probability guarantees require a different interpretation. The exact calculations assume arithmetic without rounding, and no wall-clock or floating-point performance is asserted. The originality comparison is limited to the cited and inspected accessible material and published research searches.

## References

1. H. He and D. Kressner, *Randomized Joint Diagonalization of Symmetric Matrices*, arXiv:2212.07248 (first posted 2022-12-14), especially Algorithm 1, Theorems 6 and 8, and Section 3.4; https://arxiv.org/html/2212.07248v4 .
2. H. He and D. Kressner, *A randomized algorithm for simultaneously diagonalizing symmetric matrices by congruence*, arXiv:2402.16557, https://arxiv.org/html/2402.16557v2 .
3. H. He, D. Kressner, and B. Plestenjak, *Randomized methods for computing joint eigenvalues, with applications to multiparameter eigenvalue problems and root finding*, arXiv:2409.00500, https://arxiv.org/html/2409.00500v1 .
