# Second-order Boolean entropy from Nevanlinna interlacing and fixed-moment nonuniversality

## Finding

Let \(r\geq1\) and let \(\nu=\sum_{i=1}^{r}w_i\delta_{a_i}\) be a probability law with distinct real atoms \(a_1<\cdots<a_r\) and weights \(w_i>0\), \(\sum_i w_i=1\). Define
\[
 g(z)=G_\nu(z)=\sum_{i=1}^{r}\frac{w_i}{z-a_i},\quad
 m=\sum_iw_i a_i,\quad s_2=\sum_iw_i a_i^2,\quad v=s_2-m^2.
\]
Let \(\mu\) be the unique law satisfying \(K_\mu(z)=z-G_\mu(z)^{-1}=g(z)\), and let \(\mu_n=D_{n^{-1/2}}(\mu^{\uplus n})\) be its normalized \(n\)-fold Boolean additive convolution power. Let \(\mathbf b=(\delta_{-1}+\delta_1)/2\) and define the relative Boolean logarithmic entropy in this normalized setting as
\[
 \Gamma(\mu_n\mid\mathbf b):=-\int_{\mathbb R}\log|x|\,\mu_n(dx)\in[0,+\infty].
\]
The law \(\mu\) is centered with variance one and has third and fourth moments \(m_3(\mu)=m\) and \(m_4(\mu)=1+s_2\).

For \(r\geq2\), the transform \(g\) has exactly one simple zero \(q_j\) in every interval \((a_j,a_{j+1})\), \(1\leq j<r\). Put
\[
 c_j=\left(\sum_{i=1}^{r}\frac{w_i}{(q_j-a_i)^2}\right)^{-1}>0.
\]
If **all** \(q_j\ne0\), then the relative entropy is finite for every integer \(n\ge1\) and
\[
 \boxed{\displaystyle
 \Gamma(\mu_n\mid\mathbf b)
 =\frac{v}{2}\frac{\log n}{n}+
 \frac1n\left(\frac{3m^2-2s_2}{4}-\sum_{j=1}^{r-1}c_j\log|q_j|\right)
 +o\!\left(\frac1n\right).}
\]
Here \(\sum_j c_j=v\), including the empty-sum convention when \(r=1\). If **some** \(q_j=0\), the law \(\mu_n\) has a strictly positive atom at zero for every integer \(n\ge1\); consequently \(\Gamma(\mu_n\mid\mathbf b)=+\infty\) for every such \(n\).

The second coefficient is **not controlled by the first four moments of \(\mu\)**. Fix any \(v>0\). For each \(0<p<1\), take
\[
 \nu_p=(1-p)\delta_0+\frac p2\bigl(\delta_{-\sqrt{v/p}}+\delta_{\sqrt{v/p}}\bigr).
\]
All corresponding initial laws \(\mu_p\) have the identical first four moments \((m_1,m_2,m_3,m_4)=(0,1,0,1+v)\), yet
\[
 \boxed{\displaystyle
 \Gamma((\mu_p)_n\mid\mathbf b)
 =\frac v2\frac{\log n}{n}
 +\frac{v}{2n}\left[-1-\log\left(\frac{v(1-p)}p\right)\right]
 +o\!\left(\frac1n\right).}
\]
As \(p\) varies over \((0,1)\), the coefficient of \(1/n\) ranges bijectively over all of \(\mathbb R\). Thus the next-order entropy term admits no upper or lower bound based only on those four moments, even among compactly supported initial laws with finite Boolean entropy.

## Assumptions and scope

The input consists of a **fixed**, finite, positive atomic Nevanlinna probability measure \(\nu\), with fixed distinct real atoms and positive weights; the asymptotic limit varies only \(n\to\infty\). The initial law \(\mu\) is defined by its analytic Cauchy transform \(G_\mu(z)=(z-g(z))^{-1}\), which is the spectral law at the central vertex of the finite real symmetric matrix constructed below. Therefore no independent existence or regularity assumption on \(\mu\) is needed. The transform of normalized powers is \(G_{\mu_n}(z)=(z-\sqrt n\,g(\sqrt n z))^{-1}\). All logarithms are natural. The asymptotic remainder may depend on the fixed input law; no uniformity is asserted as atoms collide, weights approach zero, or any zero approaches the origin.

For \(r=1\), the zero list is empty, \(v=0\), and the formula simplifies to \(\Gamma(\mu_n\mid\mathbf b)=m^2/(4n)+o(1/n)\), including the identically Rademacher case \(m=0\). A zero \(q_j=0\) is an exact singular boundary: the entropy is infinite, not an asymptotic finite correction.

## Proof

**1. Exact spectral construction and normalization.** Write \(t=n^{-1/2}\) and define the symmetric star matrix
\[
 B_t=\begin{pmatrix}
 0&\sqrt{w_1}&\cdots&\sqrt{w_r}\\
 \sqrt{w_1}&t a_1&&0\\
 \vdots&&\ddots&\\
 \sqrt{w_r}&0&&t a_r
 \end{pmatrix}.
\]
Its upper-left resolvent entry, by the Schur complement, is
\[
 \langle e_0,(zI-B_t)^{-1}e_0\rangle
 =\left(z-\sum_{i=1}^r\frac{w_i}{z-ta_i}\right)^{-1}
 =\left(z-\sqrt n\,g(\sqrt n z)\right)^{-1}.
\]
At \(t=1\) this defines \(\mu\), and at \(t=n^{-1/2}\) it is exactly the stated Boolean convolution law by the defining \(K\)-transform rule. Since \((B_t)_{00}=0\) and \((B_t^2)_{00}=\sum_i w_i=1\), every \(\mu_n\) is centered with variance one. At \(t=1\), expansion of \((z-g(z))^{-1}\) at infinity yields \(m_3(\mu)=m\) and \(m_4(\mu)=1+s_2\).

**2. Interlacing eigenvalues and their masses.** Away from the poles \(ta_i\), every eigenvalue \(\lambda\) is a zero of
\[
 F_t(\lambda)=\lambda-\sum_i\frac{w_i}{\lambda-ta_i}.
\]
On each component of \(\mathbb R\setminus\{ta_i\}\), the derivative is \(F_t'(x)=1+\sum_iw_i/(x-ta_i)^2>0\), with opposite infinite limits at consecutive poles. Hence there is exactly one simple eigenvalue in each of the \(r+1\) intervals, including the two outer ones. Each has strictly positive mass
\[
 \pi_t(\lambda)=\left(1+\sum_i\frac{w_i}{(\lambda-ta_i)^2}\right)^{-1}
\]
in the central spectral measure. This proves that all spectral terms used below exist and have no hidden zero weights.

**3. Outer eigenvalues.** Put \(\sigma\in\{-1,1\}\) and \(t\downarrow0\). Since \(F_0(z)=z-1/z\) has simple roots \(\sigma\), analytic implicit expansion gives
\[
 \lambda_\sigma(t)=\sigma+\frac m2t
  +\sigma\left(\frac{s_2}{2}-\frac{3m^2}{8}\right)t^2+O(t^3),
\]
\[
 \pi_\sigma(t)=\frac12-\sigma\frac m4t
  +\frac{m^2-s_2}{2}t^2+O(t^3).
\]
For example, the first expansion follows upon substituting \(\lambda_\sigma=\sigma+A t+B t^2\) into \(\lambda_\sigma=\sum_iw_i/(\lambda_\sigma-ta_i)\) and equating coefficients; the mass expression follows by inserting it in the explicit formula above. The logarithms satisfy
\[
 \log|\lambda_\sigma(t)|=\sigma\frac m2t+\frac v2t^2+O(t^3).
\]
Multiplication and cancellation of odd terms yield the outer contribution to the ordinary Boolean entropy:
\[
 \sum_{\sigma=\pm1}\pi_\sigma(t)\log|\lambda_\sigma(t)|
 =\frac{2s_2-3m^2}{4}t^2+O(t^3).
\]

**4. Small eigenvalues and the zero boundary.** The derivative \(g'(x)=-\sum_iw_i/(x-a_i)^2\) is negative on each interval \((a_j,a_{j+1})\). The endpoint limits show that it has a single simple zero \(q_j\) there. Setting \(\lambda=t y\), the eigenvalue equation becomes
\[
 g(y)=t^2y.
\]
The implicit-function theorem at \((y,t)=(q_j,0)\), with \(g'(q_j)=-1/c_j\ne0\), gives
\[
 \lambda_j(t)=tq_j+O(t^3),\qquad
 \pi_j(t)=c_jt^2+O(t^4).
\]
If \(q_j\ne0\), then \(\log|\lambda_j(t)|=\log t+\log|q_j|+O(t^2)\). If \(q_j=0\), the equation \(g(y)=t^2y\) is solved exactly by \(y=0\) for every \(t>0\), and the spectral mass at zero is strictly positive. Thus the logarithmic entropy is \(-\infty\) and the relative entropy \(+\infty\) in the latter case.

**5. The residue sum and the second coefficient.** The outer spectral masses add to
\[
 \pi_+(t)+\pi_-(t)=1-(s_2-m^2)t^2+O(t^3)=1-vt^2+O(t^3).
\]
Since the \(r+1\) positive masses sum to one, comparing with the small-mass expansion forces the *exact* identity \(\sum_{j=1}^{r-1}c_j=v\). When no zero is at the origin, their logarithmic contribution is
\[
 \sum_{j=1}^{r-1}\pi_j(t)\log|\lambda_j(t)|
 =t^2\left(v\log t+\sum_{j=1}^{r-1}c_j\log|q_j|\right)
 +O(t^4|\log t|).
\]
Adding the outer contribution, negating to obtain relative Boolean entropy, and substituting \(t^2=1/n\), \(\log t=-\tfrac12\log n\) gives the displayed \(1/n\)-accurate expansion. Its remainder is \(O(n^{-3/2})+O(n^{-2}\log n)=o(n^{-1})\) for each fixed input.

**6. Equal first four moments and arbitrary second constants.** For the stated family \(\nu_p\), the mean is zero, its second moment is \(v\), and its Nevanlinna transform has zeros
\[
 q_\pm=\pm\sqrt{v(1-p)/p},\qquad c_+=c_-=v/2.
\]
Substitution gives precisely the second boxed expression. The coefficient \(\tfrac v2[-1-\log(v(1-p)/p)]\) is continuous and strictly increasing in \(p\), tending to \(-\infty\) as \(p\downarrow0\) and to \(+\infty\) as \(p\uparrow1\). Every fixed \(p\in(0,1)\) has nonzero zeros and finite entropy. Meanwhile the moment identities from Step 1 give the same first four moments for every member. This proves both the formula and the claimed nonuniversality.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library (`decimal` and `fractions`). It independently computes the \(r+1\) spectral poles by monotone bisection of the Schur-complement equation and their exact residue formulas; it never calls the asymptotic expansions to construct the spectral distribution. For six fixed test inputs with one through five Nevanlinna atoms, it compares the rescaled entropy \(n\Gamma(\mu_n\mid\mathbf b)-\tfrac v2\log n\) with the predicted second coefficient for \(n=100,1000,10000,100000,1000000\). It also checks normalization and the residue identity, confirms the previously published four-point special-case formula on multiple parameter values, and confirms an exact positive zero-atom mass in the symmetric two-point Nevanlinna boundary example.

Executing `python verify.py` yielded `PASS 116 root, residue, normalization, asymptotic, moment, published-special-case, and zero-atom assertions`. These finite computations provide cross-checks, **not** a proof of the all-atomic asymptotic theorem. The proof consists of Steps 1–6.

## Relationship to prior work

Pan (2026, arXiv:2610.20178v1), Theorem 1.3, proves the leading coefficient \(v\log n/(2n)\) under general moment assumptions, and Example 4.1 supplies an explicit symmetric four-point distribution with an \(O(1/n)\) remainder but does not state the general second coefficient. Its exact special-case eigenvalues allow the corresponding constant to be recovered by expansion; that **special case is prior coverage**, not claimed independently new here. The present statement addresses **all finite Nevanlinna laws with nonzero transform zeros**, identifies the complete second coefficient through the interlacing zero data, and exhibits fixed-four-moment families with arbitrary next coefficients; neither follows from the previously stated leading-only rate or the single explicit example.

Pan (2025, arXiv:2505.07907) introduced and investigated the Boolean entropy and its monotonicity. Cébron and Pan (2026, arXiv:2602.23527) developed Boolean Fisher-information inequalities and transport/Stein bounds. They give relevant foundations but do not supply the claimed finite-atomic second coefficient or the fixed-four-moment nonuniversality classification. The Boolean self-energy additive rule and Nevanlinna representation are standard ingredients, not new claims.

## Limitations

This is a finite-atomic Nevanlinna law theorem; arbitrary continuous or infinite-support Nevanlinna measures are **not** covered. The error terms are not uniform when atoms or weights degenerate or when a zero approaches zero. The relative entropy here is the Boolean logarithmic functional, **not** classical Kullback–Leibler divergence. The singular-zero boundary has infinite entropy and must not be assigned a finite second coefficient. The published example provides existing coverage of one special parameter choice; novelty is claimed only for the full all-atomic classification and fixed-four-moment nonuniversality, subject to the risk of an equivalent formulation in older spectral-perturbation literature. Independent scientific validation has not been performed.

## References

1. K. Pan, *Entropic Inequalities and Limit Theorems in Boolean Probability*, arXiv:2610.20178v1, first submitted 2026-10-14, https://arxiv.org/html/2610.20178v1 (Theorem 1.3; Example 4.1; Section 2.2).
2. K. Pan, *An entropy for Boolean independence*, arXiv:2505.07907, first submitted 2025-05-12, https://arxiv.org/abs/2505.07907 (entropy definition and central-limit monotonicity).
3. G. Cébron and K. Pan, *Functional inequalities for Boolean entropy*, arXiv:2602.23527, first submitted 2026-02-26, https://arxiv.org/abs/2602.23527 (Boolean entropy and Fisher-information framework).
4. R. Speicher and R. Woroudi, *Boolean convolution*, Fields Institute Communications **12** (1997), 267–279 (standard self-energy linearization, as cited in [1]).
