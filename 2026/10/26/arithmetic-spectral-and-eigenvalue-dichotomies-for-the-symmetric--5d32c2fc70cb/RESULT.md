# Arithmetic spectral and eigenvalue dichotomies for the symmetric recurrence derivative on Hardy space

## Finding

For \(0<\alpha<1\) put \(\theta=\pi\alpha\). On \(H^2(\mathbb D)\), initially for polynomials, define the symmetric recurrence derivative
\[
D_\alpha f(z)=\frac{f(e^{i\theta}z)-f(e^{-i\theta}z)}{2iz\sin\theta},
\qquad D_\alpha 1=0.
\]
It extends uniquely to a bounded operator. Its complete spectrum obeys the arithmetic dichotomy
\[
\sigma(D_\alpha)=\begin{cases}
\{0\},&\alpha\in\mathbb Q,\\
\{\lambda\in\mathbb C:|\lambda|\le (2\sin(\pi\alpha))^{-1}\},&\alpha\notin\mathbb Q.
\end{cases}
\]
If \(\alpha=p/q\in(0,1)\) is reduced, \(D_\alpha\) has **exact nilpotency index** \(q\). For irrational \(\alpha\), set
\[
P_N(\alpha)=\prod_{j=1}^{N}2|\sin(\pi j\alpha)|,
\quad P_0(\alpha)=1,
\quad R_\alpha=(2\sin(\pi\alpha))^{-1}.
\]
For irrational \(\alpha\), the complete point spectrum is determined by the exact square-summability criterion
\[
\sigma_{\mathrm p}(D_\alpha)=\{0\}\cup\left\{\lambda\ne0:
\sum_{N=0}^{\infty}\frac{(|\lambda|/R_\alpha)^{2N}}{P_N(\alpha)^2}<\infty\right\}.
\]
In particular the point spectrum contains every \(|\lambda|<R_\alpha\) when \(\alpha\) has eventually all continued-fraction partial quotients at most \(3\), whereas it reduces to \(\{0\}\) for the explicit irrational \(\alpha_L\) in the proof. These two irrational types have the same disk-spectrum law but opposite nonzero-eigenvalue behavior.

## Assumptions and scope

The field is complex, \(H^2(\mathbb D)\) is the classical Hardy Hilbert space with orthonormal basis \(e_n(z)=z^n\) for \(n\ge0\), and the spectrum is the bounded-operator spectrum. Rational \(p/q\) is in lowest terms, with \(q\ge2\). The operator is the normalized symmetric two-root derivative associated to the second-order recurrence \(U_n=\sin(n\theta)/\sin\theta\); no claim is made for other recurrence families or other Banach norms.

## Proof

**Shift realization.** Direct substitution gives
\[
D_\alpha e_0=0,\qquad D_\alpha e_n=w_ne_{n-1},\quad w_n=\frac{\sin(n\theta)}{\sin\theta}\quad(n\ge1).
\]
The weights are uniformly bounded; hence the polynomial action extends uniquely and continuously to \(H^2\). Moreover, for each \(k\ge1\),
\[
\|D_\alpha^k\|=\sup_{n\ge k}\prod_{j=0}^{k-1}|w_{n-j}|.
\]
If \(\alpha=p/q\) is reduced, \(w_n=0\) exactly when \(q\mid n\). Every block of \(q\) consecutive weights contains a zero, proving \(D_\alpha^q=0\), while \(D_\alpha^{q-1}e_{q-1}\ne0\), proving that the index is exactly \(q\).

**Irrational spectral radius.** Suppose \(\alpha\notin\mathbb Q\). Density of \(\{n\alpha:n\ge1\}\) modulo \(1\) implies, for every fixed \(k\),
\[
\|D_\alpha^k\|=(\sin\theta)^{-k}
\max_{x\in[0,1]}\prod_{j=0}^{k-1}|\sin(\pi(x+j\alpha))|.
\]
Let \(u(x)=\log|2\sin(\pi x)|\), with \(-\infty\) at integral points. The classical sine integral gives \(\int_0^1u(x)\,dx=0\). For each fixed \(k\), the integral of \(\sum_{j=0}^{k-1}u(x+j\alpha)\) is zero, so the maximum of the corresponding continuous nonnegative product is at least \(1\). For \(M>0\), the truncation \(u_M=\max\{u,-M\}\) is continuous and periodic, and \(u\le u_M\). The irrational rotation has uniform Birkhoff averages for every continuous periodic function: this follows by uniform trigonometric-polynomial approximation and the geometric-sum bound for each nonconstant Fourier mode. Consequently,
\[
\limsup_{k\to\infty}\frac1k\max_x\sum_{j=0}^{k-1}u(x+j\alpha)
\le\int_0^1u_M(x)\,dx.
\]
Monotone convergence for \(u_M\downarrow u\) as \(M\to\infty\) (or dominated convergence after subtracting a constant) makes this upper bound tend to \(0\). The matching lower bound above yields
\[
\lim_{k\to\infty}\left(\max_x\prod_{j=0}^{k-1}|2\sin(\pi(x+j\alpha))|\right)^{1/k}=1.
\]
The spectral-radius formula therefore gives \(r(D_\alpha)=R_\alpha\). A general unilateral weighted-shift spectrum theorem, valid for bounded possibly zero weights, states that its spectrum is the closed disk of its spectral radius (D'Aniello--Maiuriello, Proposition 2.2.5). This proves the full spectrum formula.

**Point spectrum.** For irrational \(\alpha\), none of the weights vanishes. For nonzero \(\lambda\), a nonzero eigenvector \(\sum x_ne_n\) must have \(x_0\ne0\) and satisfies \(w_{n+1}x_{n+1}=\lambda x_n\). Hence
\[
|x_N|=|x_0|\frac{(2\sin\theta\,|\lambda|)^N}{P_N(\alpha)}
=|x_0|\frac{(|\lambda|/R_\alpha)^N}{P_N(\alpha)}.
\]
The \(H^2\) square-summability condition is precisely the stated series criterion; \(0\) is always an eigenvalue via \(e_0\). If partial quotients of \(\alpha\) are eventually at most \(3\), Gayfulin--Hauke, Theorem 1, proves \(\liminf_N P_N(\alpha)>0\). Thus the series converges for all \(|\lambda|<R_\alpha\). It cannot converge outside the closed spectral disk.

For a contrasting explicit irrational choose \(b_1=2\), \(b_{m+1}=10^{3b_m}\), and
\[
\alpha_L=\sum_{m\ge1}10^{-b_m},\qquad q_m=10^{b_m}.
\]
The truncation through term \(m\) is an integer multiple of \(1/q_m\), while the remaining tail has size less than \(2\cdot10^{-b_{m+1}}\). These approximations show \(\alpha_L\) is irrational (a rational different from the truncation cannot be this close for unbounded \(q_m\)). At \(N=q_m\), the last Sudler factor is at most \(4\pi q_m10^{-b_{m+1}}\), with all previous factors at most \(2\). Therefore
\[
P_{q_m}(\alpha_L)\le 2^{q_m+1}\pi q_m10^{-b_{m+1}},\qquad
\lim_{m\to\infty}P_{q_m}(\alpha_L)^{1/q_m}=0.
\]
For each fixed \(\lambda\ne0\), the eigenvector's \(N=q_m\) coefficient cannot tend to zero, since its magnitude's \(q_m\)-th root tends to \(+\infty\). Thus \(\sigma_{\mathrm p}(D_{\alpha_L})=\{0\}\), although its spectrum is the positive-radius disk above.

## Verification

The proof uses exact coefficient identities, the finite-power weighted-shift norm formula, uniform Fourier-average bounds for irrational rotations, and the cited published Sudler-product lower-bound theorem. Finite symbolic instances of the rational nilpotency and trigonometric two-step identity can be checked independently; no numerical experiment or unverified computational certificate is needed for the infinite-dimensional claims. In particular, for irrational \(\alpha\), \(\|D_\alpha\|=(\sin\theta)^{-1}\) and \(\|D_\alpha^2\|=(1+|\cos\theta|)/(2\sin^2\theta)\), directly from the dense-phase maximum.

## Relationship to prior work

Orozco López (2026) establishes the recurrence derivative and its polynomial algebraic calculus; the bounded Hardy realization's irrational spectral radius and point-spectrum arithmetic are not derived there. D'Aniello and Maiuriello (2022) provide the general disk-spectrum theorem and power-norm formula for weighted shifts but not the trigonometric irrational-rotation product evaluation. Gayfulin and Hauke (2023/2024) establish quantitative Sudler-product lower bounds for a Diophantine class; these give the eigenvalue contrast after the exact recurrence-shift correspondence and spectral-radius calculation. Aistleitner, Technau, and Zafeiropoulos (2020/2022) study the same pointwise Sudler products but not this Hardy-space spectral classification. Related variational principles for weighted dynamical-system shifts, such as Bakhtin (2008), concern a different operator setting and do not state the present spectrum or eigenvalue dichotomy.

## Limitations

The series criterion leaves possible eigenvalues exactly on \(|\lambda|=R_\alpha\) to be decided case by case. It does not classify the point-spectrum radius for every irrational continued-fraction class, nor claim essential-spectrum formulas, an operator-norm continuity statement in \(\alpha\), or an independent priority audit. Uniform-in-phase asymptotics and pointwise Sudler products are different objects; no pointwise asymptotic for arbitrary irrational \(\alpha\) is assumed. An older general theorem might subsume the irrational spectral-radius component; this historical-priority risk remains.

## References

1. R. Orozco López, *The U-Derivative Associated with Linear Recurrence Sequences*, arXiv:2610.20593v1 (first submitted 14 October 2026), especially the monomial identity and Sections 9--10. https://arxiv.org/html/2610.20593v1
2. E. D'Aniello and M. Maiuriello, *On the spectrum of weighted shifts*, arXiv:2210.01510v1 (2022), especially Section 2.2, Proposition 2.2.5, and Section 3.1. https://arxiv.org/pdf/2210.01510
3. D. Gayfulin and M. Hauke, *Hausdorff Dimension Estimates for Sudler Products with Positive Lower Bound*, arXiv:2312.06548v2, Theorem 1. https://arxiv.org/pdf/2312.06548
4. C. Aistleitner, N. Technau and A. Zafeiropoulos, *On the order of magnitude of Sudler products*, arXiv:2002.06602v2 (2022). https://arxiv.org/pdf/2002.06602
5. V. I. Bakhtin, *T-entropy and Variational principle for the spectral radius of weighted shift operators*, arXiv:0809.3106 (2008). https://arxiv.org/abs/0809.3106
