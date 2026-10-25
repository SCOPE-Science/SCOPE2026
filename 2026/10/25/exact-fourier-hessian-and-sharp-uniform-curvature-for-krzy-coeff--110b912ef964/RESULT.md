# Exact Fourier Hessian and sharp uniform curvature for Krzyż coefficient candidates

## Finding
For every integer \(n\ge2\), consider the analytic functions obtained by exponentiating finite positive Herglotz measures with exactly \(n\) atoms near the \(n\)-th roots of \(-1\). The deficit of their \(n\)-th Taylor-coefficient modulus from the candidate value \(2/e\) has an exact Fourier-block quadratic expansion, and its optimal **degree-independent quadratic coercivity constant** is
\[
c_* = \frac{3-\sqrt5}{2}.
\]
This is a quantitative refinement of the **previously known** strict local maximality of the regular Krzyż candidate, not a new proof of that qualitative assertion and not a proof of the global conjecture for \(n\ge7\).

For real \(u,\eta_j,\varepsilon_j\), \(0\le j<n\), with \(\sum_{j=0}^{n-1}\eta_j=0\), set
\[
\theta_j=\frac{(2j+1)\pi}{n}+\varepsilon_j,\qquad
w_j=\frac{1+u}{n}+\eta_j>0,
\qquad \mu=\sum_{j=0}^{n-1}w_j\delta_{e^{i\theta_j}}.
\]
Let
\[
f_\mu(z)=\exp\left(-\sum_{j=0}^{n-1}w_j\frac{e^{i\theta_j}+z}{e^{i\theta_j}-z}\right),\qquad A_n(\mu)=[z^n]f_\mu(z).
\]
Write \(W_k=\sum_j\eta_j e^{-2\pi i jk/n}\), \(E_k=\sum_j\varepsilon_j e^{-2\pi i jk/n}\), and \(t_k=k/n\). For \(\delta=|u|+\|\eta\|_2+\|\varepsilon\|_2\to0\),
\[
\boxed{2-e|A_n(\mu)|=u^2+\sum_{k=1}^{n-1}\left[(1-2t_k(1-t_k))|E_k|^2+2|W_k|^2+2(1-2t_k)\operatorname{Im}(W_k\overline{E_k})\right]+O_n(\delta^3).}
\]
For \(0<t<1\), the associated Hermitian matrix, in the coordinate order \((W,E)\), is
\[
M(t)=\begin{pmatrix}2&i(1-2t)\\-i(1-2t)&1-2t(1-t)\end{pmatrix},\qquad \det M(t)=1,\quad \operatorname{tr}M(t)=3-2t(1-t).
\]
Its two eigenvalues are
\[
\lambda_\pm(t)=\frac{3-2t(1-t)\pm\sqrt{(3-2t(1-t))^2-4}}{2}.
\]
Consequently the complete transverse quadratic form obeys
\[
\boxed{Q_n\ge c_*\left[u^2+\sum_{k=1}^{n-1}(|W_k|^2+|E_k|^2)\right],\qquad c_*=(3-\sqrt5)/2.}
\]
The equality direction in this lower bound does not occur at any fixed finite \(n\); the bound is **optimal uniformly in the degree**, approached by the first discrete Fourier modes as \(n\to\infty\). In particular, for each fixed \(n\), some neighborhood of the regular measure obeys
\[
\frac2e-|A_n(\mu)|\ge\frac{c_*}{2e}\left[u^2+n\|\eta\|_2^2+n\|\varepsilon-\overline\varepsilon\mathbf1\|_2^2\right].
\]
Here \(\overline\varepsilon=n^{-1}\sum_j\varepsilon_j\), and common rotation is necessarily neutral.

## Assumptions and scope
All mass and angular parameters are real; the weights remain positive, the \(n\) atoms remain distinct, and the perturbations are sufficiently small for the fixed chosen \(n\). The zero-sum condition fixes the weight decomposition and no normalization on the total mass is imposed. The functions are holomorphic maps from the disk into the punctured disk. The remainder \(O_n(\delta^3)\) may depend on \(n\). Fourier transforms use the unnormalized convention stated above; this normalization is essential for the constant.

## Proof
**Step 1: coefficient reduction.** Put \(m_k=\sum_jw_j e^{-ik\theta_j}\). The Herglotz expansion gives
\[
f_\mu(z)=e^{-(1+u)}\exp\left(-2\sum_{k\ge1}m_k z^k\right).
\]
At the regular configuration \(m_k=0\) for \(1\le k<n\) and \(m_n=-1\); therefore \(e A_n=2\) at the base. For \(1\le k<n\), its first variation is
\[
\delta m_k=e^{-\pi i k/n}\left(W_k-i\frac{k}{n}E_k\right).
\]
For the final moment, direct Taylor expansion of the atoms yields
\[
m_n=-1-u+i\sum_j\varepsilon_j+i u\sum_j\varepsilon_j+in\sum_j\eta_j\varepsilon_j+\frac n2\sum_j\varepsilon_j^2+O_n(\delta^3).
\]
The coefficient of \(z^n\) in the exponential, through degree two in the parameters, is
\[
-2m_n+2\sum_{k=1}^{n-1}(\delta m_k)(\delta m_{n-k})+O_n(\delta^3).
\]
**Step 2: modulus and Fourier pairing.** Multiply by the constant factor \(e^{-u}\) and use \(|2+ia+b|=2+\operatorname{Re}b+a^2/4+O(\delta^3)\) for real first-order \(a\) and second-order complex \(b\). All terms linear in \(u\) cancel, and the total-mass contribution is \(u^2\). The remaining angular-only contribution from the final moment is
\[
n\sum_j\varepsilon_j^2-\left(\sum_j\varepsilon_j\right)^2=\sum_{k=1}^{n-1}|E_k|^2.
\]
Since the perturbations are real, \(W_{n-k}=\overline{W_k}\) and \(E_{n-k}=\overline{E_k}\). Hence
\[
\operatorname{Re}[(\delta m_k)(\delta m_{n-k})]=-\lvert W_k\rvert^2+t_k(1-t_k)|E_k|^2-(1-2t_k)\operatorname{Im}(W_k\overline{E_k}).
\]
Summing over \(k\) gives exactly the displayed quadratic form. Its complex Fourier expression is real because conjugate frequencies contribute equal real terms. The expansion also holds for the unpaired real Nyquist mode when \(n\) is even.

**Step 3: spectrum and optimal degree-independent gap.** The displayed \(M(t)\) represents each Fourier block. Its determinant is identically \(2(1-2t(1-t))-(1-2t)^2=1\), and its trace lies in \([5/2,3)\). Consequently
\[
\lambda_-(t)>\frac{3-\sqrt5}{2},\qquad 0<t<1.
\]
The separate total-mass quadratic coefficient is \(1\), while the common-rotation component \(E_0\) is absent. Parseval's identity in the given normalization states \(\sum_{k=1}^{n-1}|W_k|^2=n\sum_j\eta_j^2\) and \(\sum_{k=1}^{n-1}|E_k|^2=n\sum_j(\varepsilon_j-\overline\varepsilon)^2\). The cubic remainder can be absorbed locally, proving the inequality with factor \(c_*/(2e)\).

For sharpness of the coefficient \(c_*\) **across degrees**, choose, for each \(n\ge3\), perturbations supported at conjugate frequencies \(1,n-1\), whose complex Fourier amplitudes approximate a minimizing eigenvector of \(M(1/n)\). The ratio of \(Q_n\) to the Fourier squared norm is then \(\lambda_-(1/n)\to(3-\sqrt5)/2\), so no larger all-degree constant is valid. This argument concerns the second variation, not a finite-radius uniform neighborhood.

## Verification
The standalone `checker.py` verifies the trace and determinant symbolically, evaluates the exact coefficient recurrence from Herglotz moments, compares the analytic quadratic form with independent finite differences over multiple small perturbations and degrees, and checks the sharp limiting Fourier eigenvalue numerically. Run using `python checker.py` with NumPy and SymPy installed. The checker is supplementary; Steps 1–3 supply the all-degree proof.

## Relationship to prior work
Hummel, Scheinberg, and Zalcman (1977) had already proved **strict local maximality** of the standard Krzyż candidate, as explicitly noted by Agler and McCarthy in the 2019 author manuscript, p. 3. Therefore strict local maximality by itself is **not** asserted as novel. Agler–McCarthy develop first-order/critical-point and entropy reductions, and Lei–Zhang prove the entropy inequality. Wikström's 2026 full-text sixth-coefficient proof uses the regular candidate and discusses numerical Hessian tests for certain local maxima (Section 7.3), but does not give the all-degree Fourier-block spectrum or its sharp universal curvature constant. The present quantitative second-variation identity supplements, and does not replace, those results.

## Limitations
The result applies only to perturbations with exactly \(n\) positive atoms near the regular \(n\)-atomic configuration. It proves neither a global inequality over all Herglotz measures nor the general Krzyż conjecture. The neighborhood size in the displayed local bound can depend on \(n\). The 1977 original local-maximality paper was not accessible in full for priority comparison; it could contain additional second-order computations. There has been no independent audit or historical-priority certification.

## References
1. F. Wikström, *A computer-assisted proof of Krzyż's conjecture for the sixth coefficient*, arXiv:2610.15206v1 (first posted 2026-10-10), especially Sections 2.4, 3, and 7.3.
2. J. Agler and J. E. McCarthy, *The Krzyż Conjecture and an Entropy Conjecture*, arXiv:1803.09718; author-hosted 2019 manuscript, especially pp. 2–3 and Sections 4 and 6.
3. J. Lei and T. Zhang, *Proof of the Agler–McCarthy entropy conjecture*, arXiv:2605.03949 (first posted 2026-05-05).
4. J. A. Hummel, S. Scheinberg, and L. Zalcman, *A coefficient problem for bounded nonvanishing functions*, J. Analyse Math. 31 (1977), 169–190, DOI:10.1007/BF02813302.
