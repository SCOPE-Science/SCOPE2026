# Two-term variance law for the logarithmic Mahler measure of Gaussian polynomials

## Finding
Let \(G_0,\ldots,G_{n-1}\) be independent standard circular complex Gaussians and set \(P_n(z)=\sum_{j=0}^{n-1}G_jz^j\). Define the logarithmic Mahler measure
\[
M_n=\frac1{2\pi}\int_0^{2\pi}\log|P_n(e^{it})|\,dt.
\]
For every positive integer \(n\), \(\mathbb E M_n=(\log n-\gamma)/2\) and
\[
V_n:=\operatorname{Var}(M_n)=\frac1{8\pi}\int_{-\pi}^{\pi}
\operatorname{Li}_2\!\left(\frac{\sin^2(n\theta/2)}{n^2\sin^2(\theta/2)}\right)\,d\theta.
\]
Here \(\operatorname{Li}_2(t)=\sum_{k\ge1}t^k/k^2\) for \(0\le t\le1\). Put \(S(x)=\sin(x/2)/(x/2)\), continued by \(S(0)=1\). Then
\[
V_n=\frac{C}{n}+\frac{A}{n^3}+o(n^{-3}),
\quad C=\frac1{8\pi}\int_{\mathbb R}\operatorname{Li}_2(S(x)^2)\,dx\approx0.3311986,
\]
\[
A=\frac1{96\pi}\int_{\mathbb R}x^2[-\log(1-S(x)^2)-S(x)^2]dx\approx0.039306>0.
\]
The middle \(n^{-2}\) coefficient is exactly zero. Both displayed integral constants are absolutely convergent; at \(x=0\) the logarithmic singularity is integrable after multiplication by \(x^2\).

## Assumptions and scope
A standard circular complex Gaussian \(G\) has density \(\pi^{-1}e^{-|z|^2}\,dA(z)\). All random coefficients are independent. Integration is against normalized arc length on the entire unit circle. The polynomial is almost surely nonzero, and \(\log|P_n|\) is integrable on the circle almost surely. No additional assumptions on \(n\ge1\) are used. The statement is a variance result for \(M_n\), not for its exponential.

## Proof
**Gaussian logarithmic covariance.** If \(Z,W\) are standard jointly circular complex Gaussian variables with \(\mathbb E(Z\overline W)=\rho\), then
\[
\operatorname{Cov}(\log|Z|,\log|W|)=\frac14\operatorname{Li}_2(|\rho|^2).
\]
Indeed, for \(X=|Z|^2\), the Laguerre polynomials \(L_k\) form an orthonormal family in \(L^2(e^{-x}dx)\), and the centered expansion is
\[
\log|Z|+\frac\gamma2=-\frac12\sum_{k\ge1}\frac{L_k(|Z|^2)}k
\quad\text{in }L^2.
\]
The Gaussian generating function implies \(\mathbb E[L_k(|Z|^2)L_\ell(|W|^2)]=\mathbf 1_{k=\ell}|\rho|^{2k}\). Orthogonality and \(L^2\) convergence give the identity, including \(|\rho|=1\) by continuity. Also \(\mathbb E\log|Z|=-\gamma/2\).

**Exact finite variance.** The standardized Gaussian field \(n^{-1/2}P_n(e^{it})\) is stationary on the circle with correlation modulus
\[
|\rho_n(\theta)|=\left|\frac1n\sum_{j=0}^{n-1}e^{ij\theta}\right|
=\left|\frac{\sin(n\theta/2)}{n\sin(\theta/2)}\right|.
\]
Integrate the covariance formula over two angles and use rotational invariance to get the exact variance. Tonelli's theorem and Parseval also give the exact positive coefficient series
\[
V_n=\frac14\sum_{k\ge1}\frac{1}{k^2n^{2k}}\sum_{s=0}^{k(n-1)}c_{n,k}(s)^2,
\qquad c_{n,k}(s)=[z^s](1+z+\cdots+z^{n-1})^k.
\]
This series converges because the inner normalized term does not exceed \(1\). The \(k=1\) contribution equals \(1/(4n)\) **exactly**, by orthogonality of \(1,z,\ldots,z^{n-1}\).

**Second-order scaling, including the missing order.** Define \(s(x)=S(x)^2\),
\(q_n(x)=(x/(2n)/\sin(x/(2n)))^2\) for \(|x|\le\pi n\), with continuous value \(1\) at zero, and \(H(t)=\operatorname{Li}_2(t)-t\). Changing variables \(\theta=x/n\) and separating the exact \(k=1\) term yields
\[
nV_n=\frac14+\frac1{8\pi}\int_{-\pi n}^{\pi n}H(s(x)q_n(x))dx.
\]
Since \(H(t)=O(t^2)\) as \(t\downarrow0\), the limit is
\[
C=\frac14+\frac1{8\pi}\int_{\mathbb R}H(s(x))dx,
\]
identical to the first displayed expression by \(\int_{\mathbb R}s(x)dx=2\pi\). Furthermore
\[
n^2(q_n(x)-1)\longrightarrow x^2/12,
\qquad H'(t)=-\log(1-t)/t-1.
\]
For each fixed nonzero \(x\),
\[
n^2[H(s(x)q_n(x))-H(s(x))]
\longrightarrow \frac{x^2}{12}[-\log(1-s(x))-s(x)].
\]
Here is an integrable majorant needed for the interchange of limit and integral. For \(|x|\le1\), the Dirichlet-window expressions satisfy \(1-s(x)\asymp x^2\), \(1-s(x)q_n(x)\asymp x^2\) for \(n\ge2\), and \(n^2s(x)(q_n(x)-1)=O(x^2)\), giving a bound \(C_0x^2(1+|\log|x||)\). On any fixed compact region away from zero, the integrand is uniformly bounded, including at the isolated zeros of \(S\). For sufficiently large \(|x|\), uniformly over \(|x|\le\pi n\), one has \(s(x)q_n(x)=O(x^{-2})\), \(n^2s(x)(q_n(x)-1)=O(1)\), and \(H'(t)=O(t)\), giving the integrable bound \(C_1x^{-2}\). Finally, \(n^2\int_{|x|>\pi n}H(s(x))dx=O(n^{-1})\), because \(H(s(x))=O(x^{-4})\). Dominated convergence proves
\[
\lim_{n\to\infty}n^3(V_n-C/n)
=\frac1{96\pi}\int_{\mathbb R}x^2[-\log(1-s(x))-s(x)]dx=A.
\]
The integrand is strictly positive whenever \(x\ne0\) and \(0<s(x)<1\), so \(A>0\); this establishes both the vanished \(n^{-2}\) term and the positive \(n^{-3}\) term.

## Verification
The standalone `verify_mahler.py` computes exact finite variances using dilogarithm quadrature, checks the convergent integer collision series against its positive remainder, evaluates the cases \(n=1\) and \(n=2\), and tests the scaling at \(n=16,32,64,128,256,512\). It passed 21 assertions. It is corroboration only; the preceding dominated-convergence proof supplies the infinite-\(n\) justification. In particular,
\[
V_1=\pi^2/24,\qquad V_2=\pi^2/24-(\log2)^2/2.
\]
The midpoint extrapolations \(C\approx0.331198585647\) and \(A\approx0.0393059\) are consistent with the integral constants. Quadrature values are approximate, not a rigorous enclosure.

## Relationship to prior work
Klurman–Lamzouri–Munsch (2023), the motivating complex-polynomial Mahler-measure source, analyze character-coefficient Fekete polynomials through a non-Gaussian limiting process; they do not provide a variance expansion for independent Gaussian coefficients. Kiro–Nishry (2021) use related Gaussian logarithmic covariance and dilogarithms for counts of analytic zeros, which motivates but does not state the circle-averaged logarithmic Mahler variance or its second asymptotic coefficient. Choi–Mossinghoff (2011) and Choi–Erdélyi (2014) concern averages/concentration for unimodular/Littlewood coefficient ensembles rather than the sharp variance law here. This comparison does not exclude unknown equivalent formulations.

## Limitations
This statement is restricted to independent equal-variance circular complex Gaussian coefficients and the full unit circle. It makes no central-limit claim, covers neither deterministic Fekete polynomials nor non-Gaussian unimodular coefficients, and does not quantify the remainder beyond \(o(n^{-3})\). The covariance identity is classical; originality is asserted only for the fully specified variance asymptotic and its exact second correction, subject to historical-priority uncertainty. No independent audit has been completed.

## References
- O. Klurman, Y. Lamzouri, M. Munsch, *\(L_q\) norms and Mahler measure of Fekete polynomials* (2023), arXiv:2306.07156v1, https://arxiv.org/abs/2306.07156 .
- A. Kiro, A. Nishry, *Fluctuations for zeros of Gaussian Taylor series* (2021), DOI:10.1112/jlms.12457, https://doi.org/10.1112/jlms.12457 .
- K. Choi, M. Mossinghoff, *Average Mahler's measure and \(L_p\) norms of unimodular polynomials* (2011), DOI:10.2140/pjm.2011.252.31, https://doi.org/10.2140/pjm.2011.252.31 .
- K. Choi, T. Erdélyi, *Average Mahler's measure and \(L_p\) norms of Littlewood polynomials* (2014), https://www.sfu.ca/~schoia/paper/meanmeasurelittlewood.pdf .
