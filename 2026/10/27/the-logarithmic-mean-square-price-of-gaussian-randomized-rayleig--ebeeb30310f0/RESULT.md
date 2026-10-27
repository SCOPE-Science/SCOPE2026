# The logarithmic mean-square price of Gaussian randomized Rayleigh–Ritz for an interior eigenvector

## Finding

Consider the Gaussian Petrov–Galerkin randomized Rayleigh–Ritz (RRR) procedure on the three-dimensional interior-eigenvalue example below. Even if an oracle chooses the more accurate of **both** resulting randomized Ritz vectors, its squared sine-angle risk has the sharp asymptotic
\[
\mathbb E\,E_\varepsilon^2
=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2)
\qquad(\varepsilon\downarrow0).
\]
The best deterministic vector in the prescribed trial subspace has squared sine-angle error exactly \(\varepsilon^2\). The extra logarithm is therefore a genuine mean-square penalty, not simply loss from choosing an inconvenient Ritz value.

More precisely, the normalized oracle error converges almost surely under a fixed Gaussian coupling,
\[
\frac{E_\varepsilon}{\varepsilon}\longrightarrow
Z=\sqrt{1+|G_2/G_1|^2},\qquad
\Pr\{Z>t\}=t^{-2}\quad(t\ge1),
\]
where \(G_1,G_2\) are independent standard circular complex Gaussians. For every \(0<p<2\),
\[
\lim_{\varepsilon\downarrow0}
\varepsilon^{-p}\mathbb E\,E_\varepsilon^p
=\frac{2}{2-p}.
\]
The critical \(p=2\) moment diverges upon normalization with an **exact logarithmic leading coefficient one**.

## Assumptions and scope

All operations are exact. Set \(A=\operatorname{diag}(-1,0,1)\), target \(v=e_2\), and orthonormal vectors
\[
w_2=(e_1-e_3)/\sqrt2,\quad
w_3=(e_1+e_3)/\sqrt2,\quad
c=\sqrt{1-\varepsilon^2},\quad 0<\varepsilon<1/2.
\]
Let the orthonormal trial basis be
\[
W_\varepsilon=[\,c e_2+\varepsilon w_3,\ w_2\,].
\]
Its best approximation to \(v\) has sine angle \(\varepsilon\). Independently of \(\varepsilon\), draw a single \(3\times2\) matrix \(\Omega\) whose entries are independent \(\mathcal N_\mathbb C(0,1)\), meaning real and imaginary parts each have variance \(1/2\). For each \(\varepsilon\), take *all* generalized eigenvectors of the Gaussian compressed pencil
\[
\Omega^* A W_\varepsilon y=\mu\,\Omega^*W_\varepsilon y.
\]
For each fixed \(\varepsilon\), there are two finite, simple generalized eigenpairs almost surely; under the common coupling, they are also distinct for all sufficiently small positive \(\varepsilon\) almost surely. Define the oracle-best sine-angle error
\[
E_\varepsilon=\min_{j=1,2}\sin\angle(v,W_\varepsilon y_j).
\]
The same Gaussian draw for all \(\varepsilon\) supplies the almost-sure coupling. The expectations and probabilities refer only to the Gaussian test matrix. No assertion concerns finite-precision computation, other matrices, or automatic eigenvalue selection.

## Proof

**1. Gaussian kernel and exact quadratic.** A complex Gaussian \(3\times2\) test matrix has full column rank almost surely, and its null line \(\ker\Omega^*\) is uniformly distributed. Therefore it can be represented by \(q=q_0e_2+q_1w_2+q_2w_3\), where \(q_0,q_1,q_2\) are independent standard circular complex Gaussians. Since \(Aw_3=-w_2\) and \(Aw_2=-w_3\), a direction \(y=(1,z)^\mathsf T\) is a generalized eigenvector if and only if \((A-\mu I)W_\varepsilon y\) lies in \(\mathbb Cq\). Its coordinates in \((e_2,w_2,w_3)\) are
\[
(-\mu c,\ -\varepsilon-\mu z,\ -z-\mu\varepsilon).
\]
Eliminating \(\mu\) and the proportionality factor gives the **exact** root equation
\[
q_0z^2-cq_1z+\varepsilon cq_2-\varepsilon^2q_0=0. \tag{1}
\]
The exceptional events \(q_0q_1=0\) or vanishing discriminant have probability zero. For either root \(z\), the corresponding Ritz vector is \(W_\varepsilon(1,z)^\mathsf T\), and its squared sine-angle error is
\[
\frac{\varepsilon^2+|z|^2}{1+|z|^2}.
\]
Writing \(r_\varepsilon\) for the smaller modulus of the two roots, we obtain
\[
E_\varepsilon^2=\frac{\varepsilon^2+r_\varepsilon^2}{1+r_\varepsilon^2}. \tag{2}
\]

**2. Pointwise limit and its distribution.** On the probability-one event \(q_0q_1\ne0\), the two roots of (1) tend respectively to \(0\) and \(q_1/q_0\). The implicit-function derivative of the root at zero yields
\[
\frac{r_\varepsilon}{\varepsilon}\longrightarrow |q_2/q_1|.
\]
Equation (2) gives \(E_\varepsilon/\varepsilon\to\sqrt{1+|q_2/q_1|^2}\). Since \(U=|q_1|^2\) and \(V=|q_2|^2\) are independent unit-rate exponential variables,
\[
\Pr(Z>t)=\Pr(V>(t^2-1)U)=t^{-2}\qquad(t\ge1). \tag{3}
\]
This law has density \(2t^{-3}\) on \([1,\infty)\), hence moment \(2/(2-p)\) exactly for \(p<2\).

**3. Uniform integrability below order two.** Put \(a=q_0\), \(d_0=cq_2-\varepsilon q_0\), and \(U=|q_1|^2\). Then (1) is
\[
az^2-cq_1z+\varepsilon d_0=0.
\]
Condition on \((a,d_0)\); \(U\) remains independent and unit exponential. Divide outcomes into
\[
\mathcal G=\{U\ge t_\varepsilon\},\qquad
 t_\varepsilon=8\varepsilon|a|\,|d_0|/c^2,
\]
and its complement. On \(\mathcal G\), let \(w=4\varepsilon a d_0/(c^2q_1^2)\), so \(|w|\le1/2\). The smaller-modulus root is
\[
z_s=\frac{\varepsilon d_0}{cq_1}\,
\frac{2}{1+\sqrt{1-w}},
\qquad |z_s|\le 2\varepsilon|d_0|/(c\sqrt U), \tag{4}
\]
with the square-root branch near \(1\). On \(\mathcal G^c\), the product of root moduli gives
\[
r_\varepsilon^2\le\varepsilon|d_0|/|a|. \tag{5}
\]
For any \(0<p<2\), (4), \(\mathbb E U^{-p/2}<\infty\), and \(\Pr(U<t_\varepsilon)\le t_\varepsilon\) imply
\[
\sup_{0<\varepsilon<1/2}
\mathbb E (r_\varepsilon/\varepsilon)^p<\infty.
\]
Indeed, the bad-event contribution is at most
\[
8c^{-2}\varepsilon^{1-p/2}
\mathbb E\{|d_0|^{1+p/2}|a|^{1-p/2}\}<\infty,
\]
uniformly: \(c\ge\sqrt3/2\) and all displayed Gaussian moments are bounded. To pass expectations of order \(p\), apply this estimate with any fixed \(p<p'<2\). Equations (2)–(3) and uniform integrability yield the claimed \(p\)-moment limit.

**4. The critical logarithm, including its coefficient.** On \(\mathcal G\), the analytic factor in (4) satisfies
\[
\left|\left|\frac{2}{1+\sqrt{1-w}}\right|^2-1\right|
\le C|w| \quad (|w|\le1/2).
\]
After integrating in \(U\), using \(\int_t^\infty u^{-2}e^{-u}\,du\le1/t\), we obtain
\[
\mathbb E\left[
\left|r_\varepsilon^2-
\frac{\varepsilon^2|d_0|^2}{c^2U}\right|\mathbf1_\mathcal G\right]
\le C\varepsilon^2\mathbb E|d_0|^2.
\]
By (5) the contribution from \(\mathcal G^c\) to \(\mathbb E r_\varepsilon^2\) is also at most \(8\varepsilon^2c^{-2}\mathbb E|d_0|^2\). Thus, with \(E_1(t)=\int_t^\infty e^{-u}du/u\),
\[
\mathbb E r_\varepsilon^2
=\frac{\varepsilon^2}{c^2}\,
\mathbb E\{|d_0|^2E_1(t_\varepsilon)\}
+O(\varepsilon^2). \tag{6}
\]
The exact identity
\[
E_1(t)=-\gamma-\log t+
\int_0^t\frac{1-e^{-u}}u\,du
\]
has a last term between zero and \(t\). Since \(d_0=cq_2-\varepsilon q_0\) is itself standard circular complex Gaussian, \(\mathbb E|d_0|^2=1\). Gaussian logarithmic and polynomial moments (including correlations between \(a\) and \(d_0\)) are uniformly integrable. Substitution of \(t_\varepsilon\) into (6) gives
\[
\mathbb E r_\varepsilon^2
=\frac{\varepsilon^2}{c^2}\log(1/\varepsilon)+O(\varepsilon^2)
=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2). \tag{7}
\]
Finally (4)–(5), integrated as above, give
\[
\mathbb E r_\varepsilon^4
\le C\varepsilon^3
\mathbb E\frac{|d_0|^3}{|a|}=O(\varepsilon^3).
\]
The finite expectation here follows from \(d_0=cq_2-\varepsilon a\), independence of \(q_2,a\), and \(\mathbb E|a|^{-1}<\infty\) for a complex Gaussian. By (2),
\[
\left|E_\varepsilon^2-(\varepsilon^2+r_\varepsilon^2)\right|
\le\varepsilon^2r_\varepsilon^2+r_\varepsilon^4.
\]
Its expectation is \(O(\varepsilon^3)\). Combining with (7) proves the theorem.

## Verification

Execute \(\texttt{python3 verify.py}\) in the unpacked package (Python standard library only). The deterministic checker confirms the root equation, each generalized residual, and equality of the root and eigenvector angle descriptions on fixed-seed complex Gaussian samples and several values of \(\varepsilon\). It also checks the subcritical Pareto law numerically and the growth of normalized second moments. These finite calculations check algebra and are **not** substitutes for the proof of limits or uniform integrability.

## Relationship to prior work

Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization* (first public version 1 April 2026), introduced the Gaussian Petrov–Galerkin RRR method and used precisely the same \(3\times3\) Hermitian interior-eigenvalue and trial-subspace example to illustrate **deterministic** Rayleigh–Ritz failure (Example 1). That example is acknowledged as existing, not new. Its RRR convergence theorem bounds eigenvector error at prescribed success probability with a confidence-dependent constant, rather than computing expectations, the best-of-two Ritz-vector law, or the critical squared-risk logarithm. The present result is a moment-level refinement for that concrete example, not a replacement or contradiction of high-probability convergence.

Classical complex Gaussian ratio laws already explain the limiting Pareto exponent. The additional assertion is that a **nonlinear quadratic generalized eigenproblem**, with both roots available for oracle selection, cuts this tail off at precisely the scale that produces the leading \(\varepsilon^2\log(1/\varepsilon)\) squared-risk loss. The explicit coefficient, all subcritical moments, and finite-\(\varepsilon\) root analysis are established above. Randomized singular-value bounds and deterministic sketched Krylov analyses do not alone imply this result.

## Limitations

This is an exact-arithmetic asymptotic theorem for a fixed three-dimensional Hermitian interior-eigenvalue example with independent complex Gaussian test entries and no oversampling. The oracle chooses the better of both computed eigenvectors using knowledge of the true eigenvector, so it is a lower bound on the error of any rule restricted to picking one of these two Ritz eigenvectors, not a prescription for an implementable selector. The result does not imply the same moment spectrum in higher dimensions, with real random sketches, with non-Gaussian sketches, or for refined Ritz vectors. The literature comparison is not a proof of worldwide priority; independent scientific verification has not been performed.

## References

1. Nian Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1, 1 April 2026, Sections 2 and 4, especially Example 1 and Theorem 2. https://arxiv.org/html/2604.01037v1
2. Nian Shao, same paper, revision history confirming the initial public date and later revisions. https://arxiv.org/abs/2604.01037
3. Kai Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158, 2026 (different deterministic subspace-sketching setting). https://arxiv.org/abs/2604.07158
