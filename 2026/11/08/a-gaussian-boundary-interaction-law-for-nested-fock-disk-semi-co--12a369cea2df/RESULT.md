# A Gaussian boundary-interaction law for nested Fock disk semi-commutators

## Finding
For moving concentric disk indicators on the one-dimensional Gaussian Fock space, the entire singular-value boundary layer of the Toeplitz semi-commutator is governed by a one-parameter product of normal distribution functions. Its Schatten moments, operator-norm edge, counting profile and trace norm have exact limits; the trace norm also has a non-asymptotic Skellam/Poisson representation.

## Assumptions and scope
Fix \(R>0\) and \(\eta\in\mathbb R\). On the Fock Hilbert space \(\mathcal F_t^2\) with \(d\mu_t(z)=(\pi t)^{-1}e^{-|z|^2/t}\,dA(z)\) and normalized monomials \(e_n(z)=z^n/\sqrt{t^n n!}\), write \(T_h^{(t)}=P_tM_h\). For sufficiently small \(t>0\), set
\[
f=\mathbf1_{\{|z|\le R\}},\quad
 g_t=\mathbf1_{\{|z|\le\sqrt{R^2+\eta R\sqrt t}\}},\quad
 D_t=T_f^{(t)}T_{g_t}^{(t)}-T_{fg_t}^{(t)}.
\]
Let \(L=R^2/t\), \(B=L+\eta\sqrt L\), \(L_- =\min(L,B)\), \(L_+=\max(L,B)\), \(a=|\eta|\). Let \(\Phi\) be the standard-normal distribution function and \(w_a(x)=\Phi(x-a/2)\Phi(-x-a/2)\). Define \(Q_y(n)=\mathbb P\{\mathrm{Pois}(y)\ge n+1\}\).

The singular values of \(D_t\), before rearrangement, are exactly
\[
 d_n(t)=Q_{L_-}(n)\bigl[1-Q_{L_+}(n)\bigr],\qquad n\ge0.
\]
In particular, \(D_t\) is trace class at each fixed \(t\). For every fixed \(0<p<\infty\),
\[
 \lim_{t\downarrow0}\frac{\|D_t\|_{\mathcal S_p}^{p}}{\sqrt L}
 =C_p(a):=\int_{-\infty}^{\infty}w_a(x)^p\,dx.
\]
Moreover
\[
 \lim_{t\downarrow0}\|D_t\|=\Phi(-a/2)^2,
\quad
 \lim_{t\downarrow0}\frac{\#\{n:s_n(D_t)>s\}}{\sqrt L}
 =\operatorname{Leb}\{x:w_a(x)>s\}
\]
for each \(0<s<\Phi(-a/2)^2\). The level set is a bounded interval because \(w_a\) is even and strictly decreasing on the positive half-line.

For independent Poisson variables \(X\sim\mathrm{Pois}(L_-)\) and \(Y\sim\mathrm{Pois}(L_+)\), there is the exact identity
\[
 \|D_t\|_{\mathcal S_1}=\mathbb E[(X-Y)_+],
\]
where \(u_+=\max(u,0)\). Its sharp limiting coefficient is
\[
 C_1(a)=\frac{e^{-a^2/4}}{\sqrt\pi}-a\Phi\!\left(-\frac a{\sqrt2}\right).
\]
In particular \(C_1(0)=1/\sqrt\pi\), whereas \(C_1(a)\) decreases strictly to zero as \(a\to\infty\). The parameter \(a\) measures boundary displacement on the natural \(\sqrt t\) scale; only fixed \(a\) is asserted in the limits.

## Proof
**Exact spectrum.** The radial Toeplitz operators commute and diagonalize in the normalized monomial basis. Direct polar integration gives
\[
 \langle T_{\mathbf1_{|z|^2\le ty}}^{(t)}e_n,e_n\rangle
 =\frac1{n!}\int_0^y u^ne^{-u}\,du
 =\mathbb P\{\mathrm{Pois}(y)\ge n+1\}=Q_y(n).
\]
Since \(fg_t\) is the indicator of the smaller disk, \(D_t e_n=-d_n(t)e_n\), so the formula lists *all* singular values with multiplicities. Large-deviation tails of the Poisson distribution make \(\sum_n d_n(t)<\infty\) at each fixed \(t\).

**Boundary scaling.** Write \(n=L+(\eta/2+x)\sqrt L+O(1)\). The classical Poisson central limit theorem, uniformly for \(x\) in compact intervals, gives \(d_n(t)\to w_a(x)\); reversing the sign of \(\eta\) only interchanges the two disk radii and translates/reflections the limiting coordinate. Chernoff estimates for both opposite Poisson tails bound \(d_n(t)\) by Gaussian tails for \(|n-L|\le L/2\), up to constants depending on \(a\), and by exponentially summable tails farther away. The bounds remain summable after taking any fixed positive power. Riemann sums therefore yield \(L^{-1/2}\sum_n d_n(t)^p\to\int w_a^p\) for every fixed \(p>0\). The same compact-uniform convergence and tail bounds give the operator norm. Strict log-concavity of \(\Phi\) makes \(w_a\) even and strictly decreasing for positive \(x\), so each interior level is crossed at exactly two points and the count follows.

**Finite-scale trace formula.** The identities \(Q_{L_-}(n)=\mathbb P(X\ge n+1)\) and \(1-Q_{L_+}(n)=\mathbb P(Y\le n)\) imply, by nonnegative Tonelli summation,
\[
 \sum_{n\ge0}d_n(t)=\mathbb E\sum_{n\ge0}\mathbf1_{\{Y\le n<X\}}
 =\mathbb E[(X-Y)_+].
\]
For the limit, integrate \(w_a(x)\) by interpreting the product of two Gaussian tails as the expected length of a random interval: if \(Z_1,Z_2\) are independent standard normals, \(\int w_a(x)dx=\mathbb E[(Z_1-Z_2-a)_+]\). Their difference is \(N(0,2)\). Integrating this positive-part expectation gives the displayed coefficient. Differentiation yields \(C_1'(a)=-\Phi(-a/\sqrt2)<0\).

## Verification
The accompanying standard-library checker independently checks the finite-count identity for 225 pairs of nonnegative integers and evaluates 12 Poisson pairs at three increasing large scales for four boundary separations. It compares trace and top singular-value values with the Gaussian crossover formulas. Finite tests are corroboration only: the theorem for every \(t\) and every \(p>0\) follows from the exact diagonalization, Tonelli identity, central limit theorem and dominated Poisson-tail Riemann sums.

## Relationship to prior work
Qin (arXiv:2610.30787v1; October 22, 2026) characterizes **convergence to zero** of Fock Toeplitz semi-commutators with a fixed bounded second symbol across Schatten scales. Here both indicator boundaries can depend on the semiclassical parameter, and the result quantifies a distinct critical interaction through *full singular-value counts and moments*. Apredoaei (arXiv:2606.24503v1) establishes general fixed-domain indicator Toeplitz trace/Weyl asymptotics with a Gaussian boundary profile; the present two-boundary double-scaling product is not a one-symbol fixed-domain polynomial trace. Fenzl and Lambert (arXiv:2003.07776v1) analyze disk-count fluctuations of rotational determinantal processes, and may imply the **trace coefficient** through a two-disk covariance formula. The scalar trace coefficient is not asserted to be unprecedented independently of that literature; the emphasized claim is the simultaneous arbitrary-\(p\) singular-value crossover with exact moving-boundary spectrum.

## Limitations
The result is for concentric circular indicators on the one-complex-dimensional Gaussian Fock space. It does not establish the same profile for general moving smooth domains, multiple interacting boundaries, spatially varying weights, or any uniform regime in which \(|\eta|\to\infty\). General boundary Szegő methods or determinantal-process results may imply portions of the formula under another representation, especially the scalar trace limit. Independent priority review and mathematical audit are not performed.

## References
- J. Qin, *Schatten limits for semi-commutators in Toeplitz quantization on Fock space*, arXiv:2610.30787v1 (2026-10-22), https://arxiv.org/abs/2610.30787.
- R. Apredoaei, *Asymptotics for Toeplitz operators with symbol and indicator function*, arXiv:2606.24503v1 (2026-06-23), https://arxiv.org/abs/2606.24503.
- M. Fenzl and G. Lambert, *Precise deviations for disk counting statistics of invariant determinantal processes*, arXiv:2003.07776v1 (2020-03-17), https://arxiv.org/abs/2003.07776.
