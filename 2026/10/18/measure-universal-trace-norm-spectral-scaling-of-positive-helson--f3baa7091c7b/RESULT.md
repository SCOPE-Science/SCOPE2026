# Measure-universal trace-norm spectral scaling of positive Helson matrices

## Finding
Let \(\nu\) be an arbitrary finite, nonzero, positive Borel measure on \((0,\infty)\), and suppose its inverse first moment
\[
I=\int_{(0,\infty)}\frac{d\nu(a)}{2a}<\infty.
\]
Set \(M=\nu((0,\infty))\), and, for every \(\varepsilon>0\), define the positive Helson matrix \(H_\varepsilon\) on \(\ell^2(\mathbb N)\) by
\[
H_\varepsilon(m,n)=\frac{\varepsilon}{\sqrt{mn}}\int_{(0,\infty)}(mn)^{-\varepsilon a}\,d\nu(a),\qquad m,n\ge1.
\]
Let \(K_\nu\) be the positive integral operator on \(L^2(\nu)\) whose kernel is \(k_0(a,b)=1/(a+b)\). This operator is trace class, and \(\operatorname{Tr}K_\nu=I\). If \(\lambda_j(T)\) denotes the eigenvalues of a positive trace-class operator in decreasing order with multiplicity and zero padding, then
\[
\boxed{\sum_{j\ge1}|\lambda_j(H_\varepsilon)-\lambda_j(K_\nu)|\ \le\ \gamma_{\mathrm E}\varepsilon M+\sqrt{\bigl(4I+2\varepsilon M\log2\bigr)\varepsilon M\log2}.}
\]
In particular the entire eigenvalue lists converge in \(\ell^1\), at rate \(O_\nu(\sqrt\varepsilon)\), with no density, support-separation, or positive-moment assumption on \(\nu\). At the same time \(H_\varepsilon\to0\) **strongly** on \(\ell^2\), while \(\|H_\varepsilon\|\to\|K_\nu\|>0\). Thus all surviving spectral mass migrates through the coefficient indices as the moment measure approaches the Dirichlet-evaluation boundary.

The exact first trace correction, for the same arbitrary measure, is
\[
\boxed{\operatorname{Tr}H_\varepsilon=I+\gamma_{\mathrm E}\varepsilon M+o(\varepsilon),}\qquad \varepsilon\downarrow0,
\]
where \(\gamma_{\mathrm E}\) is Euler's constant.

For a finite atomic measure \(\nu=\sum_{i=1}^r w_i\delta_{a_i}\) with distinct \(a_i>0\) and \(w_i>0\), the limiting positive eigenvalues are exactly those of the \(r\)-by-\(r\) Cauchy matrix \(C_{ij}=\sqrt{w_iw_j}/(a_i+a_j)\), with
\[
\det C=\frac{\bigl(\prod_{i=1}^r w_i\bigr)\bigl(\prod_{i<j}(a_j-a_i)^2\bigr)}{\prod_{i,j=1}^r(a_i+a_j)}>0.
\]
The finite Cauchy determinant is the classical identity; its role here is to display concrete limiting spectra, not to assert a new determinant formula.

## Assumptions and scope
The measure is finite, positive, nonzero, and carried by the open positive half-line. The sole integrability condition is the finite inverse moment \(I\). It is the natural trace-class condition for the limit: \(K_\nu\) has the feature representation \(k_0(a,b)=\int_0^\infty e^{-at}e^{-bt}\,dt\), and its trace equals \(I\). The scale \(\varepsilon\) is real and strictly positive. Every assertion is for fixed \(\nu\) as \(\varepsilon\downarrow0\); the displayed error bound is also uniform across measures when \(I,M\) are bounded.

The generating moment measure on the original Helson parameter axis is the pushforward of \(\varepsilon\nu\) by \(a\mapsto\tfrac12+\varepsilon a\). Consequently the matrices are in the positive trace-class Helson family of the cited trace-class criterion. These hypotheses include finite discrete measures, purely singular continuous measures, and measures with unbounded support and infinite positive moments.

## Proof
**1. Gram reduction.** Define \(B_\varepsilon:\ell^2(\mathbb N)\to L^2(\nu)\) by
\[
(B_\varepsilon x)(a)=\sqrt\varepsilon\sum_{n\ge1}x_n n^{-1/2-\varepsilon a}.
\]
By the integral comparison \(\zeta(1+y)\le1+1/y\), for \(y>0\),
\[
\|B_\varepsilon\|_{\mathcal S_2}^2=\varepsilon\int\zeta(1+2\varepsilon a)\,d\nu(a)\le I+\varepsilon M.
\]
Thus \(B_\varepsilon\) is Hilbert--Schmidt. Direct multiplication gives \(H_\varepsilon=B_\varepsilon^*B_\varepsilon\), and the companion operator \(K_\varepsilon=B_\varepsilon B_\varepsilon^*\) acts on \(L^2(\nu)\) with kernel
\[
k_\varepsilon(a,b)=\varepsilon\zeta(1+\varepsilon(a+b)).
\]
Their complete nonzero spectra agree, including multiplicities. All positive eigenvalues of \(H_\varepsilon\) and \(K_\varepsilon\) therefore agree after zero padding.

**2. Quantitative trace-norm approximation by logarithmic mesh.** Write \(u_t(a)=e^{-at}\) in \(L^2(\nu)\). Since \(I<\infty\),
\[
K_\nu=\int_0^\infty|u_t\rangle\langle u_t|\,dt,
\qquad
\int_0^\infty\|u_t\|_2^2\,dt=I,
\]
with a Bochner integral in the trace class. Let \(t_n=\varepsilon\log n\), \(\Delta_n=t_{n+1}-t_n=\varepsilon\log(1+1/n)\), and \(h=\varepsilon\log2\). For \(t\in[t_n,t_{n+1})\), put \(\tau(t)=t_n\). The logarithmic mesh is exhaustive, \(0\le t-\tau(t)\le h\), and
\[
K_\varepsilon=\sum_{n\ge1}\frac\varepsilon n|u_{t_n}\rangle\langle u_{t_n}|,
\quad
Q_\varepsilon=\sum_{n\ge1}\Delta_n|u_{t_n}\rangle\langle u_{t_n}|=\int_0^\infty|u_{\tau(t)}\rangle\langle u_{\tau(t)}|\,dt.
\]
Every coefficient \(\varepsilon/n-\Delta_n\) is nonnegative, and the classical harmonic-number limit gives
\[
\|K_\varepsilon-Q_\varepsilon\|_{\mathcal S_1}
\le M\varepsilon\sum_{n\ge1}\left(\frac1n-\log(1+1/n)\right)
=\gamma_{\mathrm E}\varepsilon M.
\]
For any two vectors \(u,v\) in a Hilbert space, the rank-one trace-norm estimate is
\[
\big\||u\rangle\langle u|-|v\rangle\langle v|\big\|_{\mathcal S_1}
\le(\|u\|+\|v\|)\|u-v\|.
\]
Because \(\tau(t)\in[\max(0,t-h),t]\), the scalar inequality \((x-y)^2\le x-y\) for \(0\le y\le x\le1\), followed by Tonelli, gives
\[
\int_0^\infty\|u_{\tau(t)}-u_t\|_2^2dt
\le \int d\nu(a)\int_0^\infty(e^{-a\tau(t)}-e^{-at})dt\le hM.
\]
The last bound follows from integrating the explicit majorant obtained by replacing \(\tau(t)\) with \(\max(0,t-h)\); its integral difference is exactly \(h\), for each \(a>0\). The analogous estimate for \(e^{-2at}\) implies
\[
\int_0^\infty\|u_{\tau(t)}\|_2^2dt\le I+hM.
\]
Cauchy--Schwarz and the rank-one inequality yield
\[
\|Q_\varepsilon-K_\nu\|_{\mathcal S_1}
\le\sqrt{\bigl(4I+2hM\bigr)hM}.
\]
Together with the preceding mesh-weight estimate this proves the displayed trace-norm bound. For positive compact operators, the trace-norm eigenvalue perturbation inequality
\(\sum_j|\lambda_j(A)-\lambda_j(B)|\le\|A-B\|_{\mathcal S_1}\) finishes the spectral claim.

**3. Boundary trace residue.** Let \(g(y)=\zeta(1+y)-1/y\) for \(y>0\). Integral comparison implies \(0\le g(y)\le1\) for all \(y>0\), and the Laurent expansion of the zeta function at one gives \(g(y)\to\gamma_{\mathrm E}\) as \(y\downarrow0\). The exact diagonal trace becomes
\[
\operatorname{Tr}H_\varepsilon
=\varepsilon\int\zeta(1+2\varepsilon a)d\nu(a)
=I+\varepsilon\int g(2\varepsilon a)d\nu(a).
\]
Dominated convergence with respect to the finite measure \(\nu\) gives the claimed \(o(\varepsilon)\) remainder without assuming any positive moment.

**4. Strong escape.** For each fixed \(n\ge1\),
\(\langle e_n,H_\varepsilon e_n\rangle\le\varepsilon M/n\), while \(\|H_\varepsilon\|\le\operatorname{Tr}H_\varepsilon\le I+\varepsilon M\). Since \(H_\varepsilon\ge0\),
\[
\|H_\varepsilon e_n\|^2\le\|H_\varepsilon\|\langle e_n,H_\varepsilon e_n\rangle\longrightarrow0.
\]
Density of finite-support vectors and the uniform norm bound imply strong convergence of \(H_\varepsilon\) to zero. Yet \(K_\nu\) has trace \(I>0\), hence \(\|K_\nu\|>0\), and spectral convergence proves \(\|H_\varepsilon\|\to\|K_\nu\|\). No norm convergence occurs.

**5. Atomic specialization.** The identification \(L^2(\nu)\cong\mathbb C^r\), after multiplying coordinates by \(\sqrt{w_i}\), yields the displayed positive Cauchy matrix. Its determinant is the classical Cauchy determinant times \(\prod_iw_i\). Since all nodes are distinct and positive, it is strictly positive. This completes the argument.

## Verification
The standalone numerical checker uses two finite atomic measures, independently computes the spectra of \(K_\varepsilon\) from the zeta Gram kernel, and compares with the limiting Cauchy Gram matrix at several scales. It tests the rigorous error bound and the critical trace correction, and checks the classical finite Cauchy determinant; these computations are diagnostics, not substitutes for the proof. The analytic inequalities above justify the result for all measures under the stated inverse-moment condition, not just the tested atomic cases.

## Relationship to prior work
Ma, Lu, and Zu (2026, arXiv:2610.12252v1, Theorem 3.4) establish the general positive Helson trace-class criterion and exact fixed-parameter trace representation. Their result does not state the moving-measure spectral scaling, uniform trace-norm approximation, or strong-operator spectral escape proved here. Their earlier 2026 paper on multiplicative Hilbert operators (arXiv:2608.22882v3) treats a different weighted noncompact model and its absolutely continuous spectral type, not this trace-class boundary family. Perfekt and Pushnitski (arXiv:1611.03772) provide the multiplicative moment framework and a finite-rank classification but do not give this boundary scaling law.

A previously studied smooth gamma-density Helson family is a **special case** after parameter rescaling, and for that family a finer first-order perturbation estimate is available. The contribution here is the complete finite-measure universality with a sharp minimal trace-class integrability assumption, including atomic and singular continuous measures without extra moment conditions, together with strong-operator escape. The special gamma example is not claimed as new. Standard general trace-ideal perturbation principles imply the spectral \(\ell^1\) conclusion *once* the new explicit trace-norm approximation has been established; they do not themselves supply that approximation. No global publication-priority guarantee is claimed.

## Limitations
The measure is required to be positive and finite, with finite inverse first moment; the theorem makes no claim for signed measures or a divergent inverse moment. The numerical bound is an explicit universal \(O_\nu(\sqrt\varepsilon)\) estimate, not a claim of optimality for any fixed measure. It does not determine the detailed eigenvalue decay of an arbitrary \(K_\nu\), and it does not assert an all-orders expansion. Existing special smooth measures can have faster convergence. Literature not indexed or otherwise inaccessible may contain stronger abstract theorems, so the originality assessment remains provisional pending independent scrutiny.

## References
- T. Ma, Y. Lu, C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first posted 2026-10-08), especially Theorem 3.4, https://arxiv.org/html/2610.12252v1 .
- T. Ma, Y. Lu, C. Zu, *On the Spectra of Multiplicative Hilbert Operator on Bergman Spaces of Dirichlet Series*, arXiv:2608.22882v3 (first posted 2026-08-24), https://arxiv.org/html/2608.22882v3 .
- K.-M. Perfekt, A. Pushnitski, *On Helson matrices: moment problems, non-negativity, boundedness, and finite rank*, arXiv:1611.03772 (first posted 2016-11-11), https://arxiv.org/abs/1611.03772 .
- Classical Cauchy determinant identity; classical Euler constant \(\gamma_{\mathrm E}=\lim_{N\to\infty}(\sum_{n=1}^N1/n-\log N)\); trace-ideal eigenvalue perturbation inequality for self-adjoint trace-class operators.
