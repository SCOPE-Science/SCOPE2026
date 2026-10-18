# Exact endpoint norms and integer-order cusps of the lattice fractional Laplacian

## Finding
Let \(L=2I-S-S^{-1}\), where \((Sf)(j)=f(j+1)\) on sequences over \(\mathbb Z\). For \(\alpha>0\), define \(T_\alpha=L^\alpha\) as convolution with the absolutely summable Fourier coefficients
\[
 a_k(\alpha)=(-1)^k\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha-k+1)\Gamma(\alpha+k+1)},\qquad k\in\mathbb Z,
\]
where reciprocal gamma is zero at its poles; put \(T_0=I\). This definition agrees with the positive self-adjoint functional-calculus power on \(\ell^2\). Define \(N(\alpha)=\|T_\alpha\|_{\ell^1\to\ell^1}=\|T_\alpha\|_{\ell^\infty\to\ell^\infty}\).

**All-order endpoint norm.** For every integer \(r\ge0\),
\[
 N(\alpha)=
 \begin{cases}
 2a_0(\alpha)+4\displaystyle\sum_{j=1}^{r}a_{2j}(\alpha),&2r<\alpha<2r+1,\\[4pt]
 -4\displaystyle\sum_{j=0}^{r}a_{2j+1}(\alpha),&2r+1<\alpha<2r+2.
 \end{cases}
\]
At every integer \(m\ge0\), \(N(m)=4^m\). Thus this infinite convolution has a finite gamma-expression for its exact endpoint norm at every order.

**Sharp normaloidity and integer cusps.** For noninteger \(\alpha>0\), put \(m=\lfloor\alpha\rfloor\). Then
\[
 \boxed{N(\alpha)-4^\alpha
 =4\sum_{j=0}^{\infty}|a_{m+2+2j}(\alpha)|>0.}
\]
The spectral radius of \(T_\alpha\) on both endpoint spaces is \(4^\alpha\), so equality of norm and spectral radius holds **precisely at positive integer orders**. The function \(N\) is real-analytic between successive positive integers, continuous at every positive integer, and has the exact jump in its first one-sided derivatives
\[
 \boxed{N'_+(m)-N'_-(m)=\frac{2}{m},\qquad m=1,2,3,\ldots.}
\]

**Order-zero endpoint discontinuity.** Although \(N(0)=1\),
\[
 \boxed{\lim_{\alpha\downarrow0}N(\alpha)=2,\qquad
 \lim_{\alpha\downarrow0}\|T_\alpha-I\|_{\ell^1\to\ell^1}
 =\lim_{\alpha\downarrow0}\|T_\alpha-I\|_{\ell^\infty\to\ell^\infty}=1.}
\]
As \(\alpha\downarrow0\), the operators converge strongly to the identity on \(c_0(\mathbb Z)\) and on \(\ell^p(\mathbb Z)\) for \(1<p<\infty\), but **not** on \(\ell^1\) or \(\ell^\infty\). In particular \(\|T_\alpha\|_{\ell^2\to\ell^2}=4^\alpha\to1\), while both endpoint norms tend to \(2\).

## Assumptions and scope
The power parameter is real and nonnegative. The lattice spacing and the positive normalization of \(L\) are fixed as stated; multiplying \(L\) by a positive constant changes the norm profile and derivative-jump normalization. The sequence spaces are complex or real, with counting measure. For \(p\ne2\), the notation \(L^\alpha\) means the bounded convolution extension of the \(\ell^2\) spectral power; the statement does not posit a holomorphic functional calculus at the zero spectral point. The symbol is \((2-2\cos\theta)^\alpha\) for \(\alpha>0\). All sums over empty index sets are zero. One-sided derivatives refer to varying \(\alpha\), not spatial derivatives. These conclusions are for the infinite, translation-invariant one-dimensional lattice and are not asserted for arbitrary finite or irregular graphs.

## Proof
**1. Coefficients and summability.** The elementary Fourier beta integral for \((2-2\cos\theta)^\alpha\) gives
\[
 a_k(\alpha)=\frac1{2\pi}\int_{-\pi}^{\pi}(2-2\cos\theta)^\alpha e^{-ik\theta}\,d\theta
 =(-1)^k\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha-k+1)\Gamma(\alpha+k+1)}.
\]
In particular \(a_{-k}=a_k\), \(a_0>0\), and
\[
 a_{k+1}(\alpha)=a_k(\alpha)\frac{k-\alpha}{k+\alpha+1},\qquad k\ge0.
\]
For noninteger \(\alpha>0\), reflection of gamma in the tail implies \(a_k=O_\alpha(k^{-2\alpha-1})\). For integer \(m\), the coefficients terminate at \(|k|=m\), with \(a_k(m)=(-1)^k\binom{2m}{m-k}\). Thus the coefficient series is absolutely summable for every positive order, and evaluating its Fourier series at \(\theta=0\) yields \(\sum_{k\in\mathbb Z}a_k(\alpha)=0\) for every \(\alpha>0\).

**2. Sign pattern and exact norms.** For noninteger \(\alpha\in(m,m+1)\), successive terms of the product
\[
 a_k(\alpha)=a_0(\alpha)(-1)^k
 \prod_{j=0}^{k-1}\frac{\alpha-j}{\alpha+j+1}
\]
show that \(\operatorname{sgn}a_k=(-1)^k\) for \(0\le k\le m+1\), while \(\operatorname{sgn}a_k=(-1)^{m+3}\) for all \(k\ge m+2\). For \(m=2r\), precisely \(a_0\) and the positive even-indexed coefficients through \(a_{2r}\) are positive; for \(m=2r+1\), precisely the odd-indexed coefficients through \(a_{2r+1}\) are negative. Since the entire coefficient sum is zero, the total absolute sum is twice the positive sum or minus twice the negative sum. Every convolution kernel \(a\in\ell^1\) has induced \(\ell^1\) norm \(\|a\|_1\) (test a point mass) and induced \(\ell^\infty\) norm \(\|a\|_1\) (test the conjugate sign of the row at the origin). This proves the two finite formulas. At integer \(m\), the central-binomial formula and \(\sum_{k=-m}^m\binom{2m}{m-k}=4^m\) give \(N(m)=4^m\).

**3. Spectral-radius gap.** At the alternating character \(f(j)=(-1)^j\), one has \(T_\alpha f=4^\alpha f\). If \(\lambda\) lies outside the compact range of the Fourier symbol, the reciprocal \((\lambda-(2-2\cos\theta)^\alpha)^{-1}\) has absolutely summable Fourier coefficients by Wiener's lemma. Thus \(\lambda I-T_\alpha\) has a convolution inverse bounded on both endpoints; the same spectral radius \(4^\alpha\) follows on \(\ell^1\), using its regular convolution representation. Comparing \(N(\alpha)=\sum|a_k|\) with \(4^\alpha=\sum(-1)^ka_k\), and using the sign pattern above, only \(k=m+2,m+4,\ldots\) and their negative partners contribute to the defect. This gives exactly the displayed strictly positive series. For integer orders every coefficient aligns with the alternating character, and the defect vanishes.

**4. The exact integer cusp.** Fix \(m\ge1\). The coefficients with \(|k|\le m\) remain nonzero and retain their signs near \(m\). For \(k=m+1+j\), \(j\ge0\), the reciprocal-gamma expansion at a nonpositive integer gives
\[
 a'_k(m)=(-1)^{m+1}\frac{(2m)!\,j!}{(2m+j+1)!},
 \qquad |a'_k(m)|=\mathrm B(j+1,2m+1).
\]
Near any fixed \(m>0\), the coefficient derivatives are uniformly absolutely summable: gamma-ratio differentiation yields a summable bound of order \(k^{-2\alpha-1}\log k\) on a sufficiently small compact order interval. We may therefore differentiate the total absolute coefficient sum on each side of \(m\). The finite nonzero coefficients contribute the same derivative from both sides, whereas each zero tail coefficient contributes a jump of \(2|a'_k(m)|\). Using symmetry and the beta integral,
\[
 \begin{aligned}
 N'_+(m)-N'_-(m)
 &=4\sum_{j=0}^{\infty}\mathrm B(j+1,2m+1)\\
 &=4\int_0^1(1-t)^{2m}\left(\sum_{j=0}^{\infty}t^j\right)dt
 =4\int_0^1(1-t)^{2m-1}dt=\frac2m.
 \end{aligned}
\]
The finite expressions in Step 2 establish real analyticity on every interval not containing an integer, while uniform absolute convergence establishes continuity for \(\alpha>0\).

**5. The singular zero-order limit and strong topologies.** For \(0<\alpha<1\), all \(a_k\) with \(k\ne0\) are negative and sum to \(-a_0\). Hence
\[
 N(\alpha)=2a_0(\alpha)
 =2\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha+1)^2}\longrightarrow2.
\]
The coefficient of the origin in \(T_\alpha-I\) is \(a_0-1\ge0\), and its off-origin absolute mass is \(a_0\), so the exact endpoint norm of \(T_\alpha-I\) is \(2a_0-1\to1\). (The inequality \(a_0\ge1\) follows, for instance, from log-convexity of gamma.) For \(k\ge1\), the recurrence yields \(\sup_{k\ge1}|a_k(\alpha)|=|a_1(\alpha)|=a_0\alpha/(1+\alpha)\to0\). Therefore \((T_\alpha-I)\delta_0\to0\) in \(c_0\) and in every \(\ell^p\), \(1<p<\infty\): for the latter use \(\sum_{k\ne0}|a_k|^p\le(\sup_{k\ne0}|a_k|)^{p-1}\sum_{k\ne0}|a_k|\to0\). Translates and finite linear combinations of \(\delta_0\) are dense in those spaces; the operator norms are uniformly bounded for \(0<\alpha<1\), so strong convergence follows. In contrast, on \(\ell^1\), \(\|(T_\alpha-I)\delta_0\|_1=2a_0-1\to1\). On \(\ell^\infty\), \(T_\alpha\mathbf1=0\) for every \(\alpha>0\), so the constant-one sequence witnesses failure of strong convergence. Finally, the \(\ell^2\) norm is the supremum of the real nonnegative symbol, namely \(4^\alpha\), and tends to one.

## Verification
The accompanying `verify.py` runs exact integer-binomial checks, high-precision independent Fourier-integral checks, order-strip sign checks, and comparisons of the finite gamma formula against the full absolute coefficient sum with an **analytically summed** constant-sign tail. For orders above the sign-change boundary, the recurrence yields
\[
 \sum_{k=K+1}^{\infty}|a_k(\alpha)|
 =|a_{K+1}(\alpha)|\frac{K+\alpha+1}{2\alpha},
 \quad K\ge\lfloor\alpha\rfloor+1,
\]
which avoids treating a truncated numerical series as an exact infinite sum. The checker also tests the beta-series identity for cusp jumps and finite-difference approximations to those jumps. One complete execution returned `VERIFY_OK checks= 739`. All infinite-parameter and topology assertions follow from the analytical argument, not the finite tests.

## Relationship to prior work
Ortigueira (2006) developed fractional centered differences in a closely related kernel representation; only its introductory material was accessible, so its complete claim coverage remains unresolved. Ciaurri, Gillespie, Roncal, Torrea and Varona (arXiv:1401.2091, first posted 2014-01-09) developed discrete heat-semigroup methods, including maximum principles for fractional powers with orders between zero and one. Michelitsch, Collet, Nowakowski and Nicolleau (arXiv:1412.5904, first posted 2014-12-18; arXiv:1511.01251, first posted 2015-11-04) derived the **same gamma-function lattice coefficients for arbitrary positive orders**, with finite-chain formulas and physical localization at integer powers. The coefficient formula in Step 1 is accordingly prior art, not presented as new. Ciaurri, Roncal, Stinga, Torrea and Varona (arXiv:1507.04986, first posted 2015-07-17) gave an explicit positive jump kernel for the restricted range \(0<\alpha<1\) and pointwise order-zero convergence for suitable sequences. The norm formula restricted to \((0,1)\) follows readily from that known signed kernel; it is not alone the asserted contribution.

What is assessed here is the complete **all-order endpoint operator-norm profile**, its strict comparison with the spectral radius, the **exact infinite sequence of integer derivative jumps \(2/m\)**, and the distinction between strong order-zero limits across \(\ell^1\), \(\ell^\infty\), \(c_0\), and interior \(\ell^p\) spaces. The inspected primary texts do not state these joint norm and topology conclusions, but the possibility of a classical equivalent Fourier-algebra-norm formula under different terminology remains a residual priority risk.

## Limitations
The gamma coefficient identity itself is classical. The endpoint norm is a specialization to a highly structured one-dimensional convolution kernel, not an estimate for arbitrary graph fractional powers. The order-zero norm discontinuity is consistent with earlier pointwise convergence results and does not contradict them. The proof establishes no uniform-in-\(p\) convergence rate and makes no claim for \(\alpha<0\), for complex exponents, or for boundary conditions.

## References
1. M. D. Ortigueira, *Riesz potential operators and inverses via fractional centred derivatives*, International Journal of Mathematics and Mathematical Sciences 2006, Article 48391, first online 13 August 2006, https://doi.org/10.1155/IJMMS/2006/48391 (introductory material consulted; full text unavailable).
2. Ó. Ciaurri, T. A. Gillespie, L. Roncal, J. L. Torrea and J. L. Varona, *Harmonic Analysis associated with a discrete Laplacian*, arXiv:1401.2091v1 (9 January 2014), https://arxiv.org/abs/1401.2091, Sections 1–3.
3. T. M. Michelitsch, B. A. Collet, A. Nowakowski and F. C. G. A. Nicolleau, *Fractional Laplacian matrix on the finite periodic linear chain and its periodic Riesz fractional derivative continuum limit*, arXiv:1412.5904v1 (18 December 2014), https://arxiv.org/abs/1412.5904, Sections 2–3 and appendices.
4. Ó. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea and J. L. Varona, *Fractional discrete Laplacian versus discretized fractional Laplacian*, arXiv:1507.04986v1 (17 July 2015), https://arxiv.org/abs/1507.04986, Theorem 1.2.
5. T. M. Michelitsch, B. A. Collet, A. Nowakowski and F. C. G. A. Nicolleau, *Lattice fractional Laplacian and its continuum limit kernel on the finite cyclic chain*, arXiv:1511.01251v1 (4 November 2015), https://arxiv.org/abs/1511.01251, Section 1.3 and Appendix.
