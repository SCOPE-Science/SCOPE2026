# The sharp power-phase transition for unimodular radial Fock Toeplitz operators

## Finding
On the normalized analytic Gaussian Fock space in every fixed complex dimension \(d\ge1\), consider the Toeplitz operator \(T_{d,\alpha}=P(a_\alpha\cdot)\) with the unit-modulus radial symbol
\[
a_\alpha(z)=\exp\!\bigl(i(|z|^2)^\alpha\bigr),\qquad \alpha>0.
\]
Its degree-\(n\) eigenvalue and multiplicity are, exactly,
\[
\lambda_{n,d,\alpha}=\frac1{\Gamma(n+d)}\int_0^\infty t^{n+d-1}e^{-t}e^{it^\alpha}\,dt,
\quad m_{n,d}=\binom{n+d-1}{d-1}.
\]
Put \(k=n+d\). Then the following complete phase transition holds:
\[
\begin{array}{ll}
0<\alpha<\frac12:&\lambda_{n,d,\alpha}=e^{ik^\alpha}+o(1),\\[2pt]
\alpha=\frac12:&\lambda_{n,d,\alpha}=e^{-1/8}e^{i\sqrt{k}}+o(1),\\[2pt]
\alpha>\frac12:&\lambda_{n,d,\alpha}=O_{d,\alpha,M}(k^{-M})\quad\text{for every }M>0.
\end{array}
\]
Consequently the Fredholm essential spectrum is the unit circle, the circle of radius \(e^{-1/8}\), or \(\{0\}\), respectively. For every \(\alpha>1/2\), the nonzero operator \(T_{d,\alpha}\) belongs to **every** Schatten class \(\mathcal S_p\) with \(p>0\), although its symbol has modulus one everywhere; when \(\alpha\le1/2\), it is noncompact. Finally, counting eigenvalues with their homogeneous-degree multiplicities, the empirical spectral measures converge to normalized arclength on the corresponding circle for \(\alpha\le1/2\), and to the point mass at zero for \(\alpha>1/2\).

## Assumptions and scope
Fix integers \(d\ge1\) and \(n\ge0\), and a real \(\alpha>0\). The Fock inner product uses \(d\mu(z)=\pi^{-d}e^{-|z|^2}dV(z)\). The Toeplitz symbol is bounded and measurable, so the compression of multiplication to the holomorphic Fock subspace is everywhere defined and bounded. Essential spectrum is the Fredholm essential spectrum; a spectral measure with cutoff \(N\) means
\[
\nu_{N,d,\alpha}=\binom{N+d}{d}^{-1}\sum_{n=0}^{N}\binom{n+d-1}{d-1}\delta_{\lambda_{n,d,\alpha}}.
\]
The asymptotic statements hold as \(n\to\infty\) with \(d\) and \(\alpha\) fixed. No uniformity is asserted when \(\alpha\) approaches \(1/2\), nor when \(d\) grows.

## Proof
**Diagonalization.** Rotational invariance makes the homogeneous monomial spaces orthogonal eigenspaces of radial multiplication compression. Polar integration in \(\mathbb C^d\) gives the Gamma law \(G_k\sim\operatorname{Gamma}(k,1)\), with \(k=n+d\), and \(\lambda_{n,d,\alpha}=\mathbb E[e^{iG_k^\alpha}]\). The degree-\(n\) multiplicity is \(m_{n,d}\), and \(\sum_{n=0}^{N}m_{n,d}=\binom{N+d}{d}\).

**Subcritical phase.** Gamma concentration gives \(\mathbb E|G_k-k|\le\sqrt{k}\) and \(\mathbb P(|G_k-k|>k/2)\le Ce^{-ck}\). On the complementary event the mean-value theorem yields \(|G_k^\alpha-k^\alpha|\le C_\alpha k^{\alpha-1}|G_k-k|\). Therefore, for \(0<\alpha<1/2\),
\[
|\lambda_{n,d,\alpha}-e^{ik^\alpha}|
\le C_\alpha k^{\alpha-1/2}+Ce^{-ck}=o(1).
\]

**Critical phase.** Write \(G_k\) as the sum of \(k\) independent mean-one exponentials. The central limit theorem and the delta method imply
\[
\sqrt{G_k}-\sqrt k=\frac{G_k-k}{\sqrt{G_k}+\sqrt k}\ \Longrightarrow\ N(0,1/4).
\]
Convergence of bounded characteristic functions at frequency one then gives
\(e^{-i\sqrt k}\lambda_{n,d,1/2}\to\exp(-1/8)\).

**Supercritical rapid decay.** Fix \(\alpha>1/2\) and choose \(0<\varepsilon<\min\{1/2,\alpha-1/2\}\). Set \(W=k^{1/2+\varepsilon}\), and choose a smooth cutoff equal to one on \(|t-k|\le W\) and supported in \(|t-k|\le2W\). A Gamma Chernoff bound makes the integral outside the core \(O(e^{-c k^{2\varepsilon}})\). On the support of the cutoff, the Gamma density \(f_k(t)=e^{-t}t^{k-1}/\Gamma(k)\) obeys, for each fixed integer \(j\ge0\),
\[
|f_k^{(j)}(t)|\le C_j k^{-j(1/2-\varepsilon)}f_k(t),
\]
because \((\log f_k)'=(k-1)/t-1=O(k^{-1/2+\varepsilon})\) and higher derivatives are \(O_j(k^{1-j})\). The cutoff derivatives are \(O_j(W^{-j})\). Repeatedly integrate by parts with
\[
e^{it^\alpha}=\frac1{i\alpha t^{\alpha-1}}\frac{d}{dt}e^{it^\alpha}.
\]
Each integration costs at most \(C k^{-(\alpha-1/2-\varepsilon)}\) in the integrated \(L^1\) bound. Indeed differentiating the reciprocal phase derivative contributes an even smaller relative factor \(O(k^{-\alpha})\). All boundary terms vanish because of the smooth cutoff. After any fixed number \(J\) of integrations, the integral is
\[
O_J(k^{-J(\alpha-1/2-\varepsilon)})+O(e^{-c k^{2\varepsilon}}).
\]
Taking \(J\) arbitrarily large proves the asserted super-polynomial decay. The multiplicity grows only polynomially, hence \(\sum_n m_{n,d}|\lambda_{n,d,\alpha}|^p<\infty\) for every \(p>0\).

**Essential spectra and spectral measures.** For \(0<\alpha<1\) and each fixed nonzero integer \(h\), comparison of a sum with its integral and one integration by parts give
\[
\sum_{n=1}^N e^{ih(n+d)^\alpha}
=O_{h,d,\alpha}(N^\alpha+N^{1-\alpha})=o(N).
\]
Thus \((n+d)^\alpha\) is equidistributed modulo \(2\pi\) by Weyl's criterion. Abel summation transfers this conclusion to weights \(m_{n,d}\asymp n^{d-1}\), because their partial sums grow as \(N^d\). Asymptotically vanishing errors in the eigenvalues transfer weak convergence of the empirical measures to Haar measure on the indicated circles. In the supercritical case the eigenvalues tend rapidly to zero, giving the point mass. Since the operator is normal and diagonal on finite-dimensional eigenspaces, its Fredholm essential spectrum equals the set of cluster points of its degree eigenvalues, giving exactly the asserted circles or \(\{0\}\). In particular no operator with \(\alpha\le1/2\) is compact.

**Nontriviality.** If all \(\lambda_{n,d,\alpha}\) were zero, the analytic Laplace transform of the nonzero measurable function \(t^{d-1}e^{-t}e^{it^\alpha}\), analytic in a half-plane around the unit Laplace parameter, would vanish to every order at a point and hence identically. Injectivity of the Laplace transform contradicts the symbol's unit modulus. Thus every \(T_{d,\alpha}\) is nonzero.

## Verification
The separate Python 3 checker `CHECK.py` numerically evaluates the Gamma integral, compares it with the exact \(\alpha=1\) transform, tests concentration limits in several dimensions, checks homogeneous-degree multiplicities, and samples phase equidistribution. It reports 63 deterministic assertions passing. These finite checks are corroboration; the infinite decay, all-Schatten, and spectral-limit conclusions follow from the analytical argument above, not from sampled computations.

## Relationship to prior work
Grudsky and Vasilevski (2002, Sections 3–4) give radial eigenvalue formulas and exhibit exponentially decaying eigenvalues for the special phase \(e^{i|z|^2}\), as well as related compact oscillatory symbols. Esmeral and Maximenko (2015, Example 4.5) treat the real symbol \(\cos|z|\), directly related to the critical exponent. Dewage and Ólafsson (2021, Corollary 2.13) develop quasi-radial Fock Toeplitz diagonalization. General compactness theorems (including Wu–Zheng 2021 and Fulsche 2024) provide important background but do not, in the inspected parts, state the simultaneous sharp phase boundary, complex circular limit laws, and super-polynomial Schatten decay for this entire unit-modulus power family. Some individual cases and compactness consequences are therefore established prior mathematics, not claimed as separate novelties here.

## Limitations
This is a fixed-complex-dimension theorem for the specific radial power-phase family, not for arbitrary oscillatory phases or nonradial symbols. No uniform estimates are asserted near \(\alpha=1/2\). The analysis does not compute the exact Schatten quasi-norms or provide a transition scaling with \(\alpha\) varying with degree. Literature comparisons are not a proof of historical priority, and independent mathematical validation has not been performed.

## References
1. S. Grudsky and N. Vasilevski, *Toeplitz operators on the Fock space: Radial component effects*, Integral Equations and Operator Theory **44** (2002), 10–37, DOI:10.1007/BF01197858.
2. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015).
3. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first made public 2021-07-03).
4. X. Wu and L. Zheng, *Toeplitz operators on the Fock space and their Berezin transforms*, arXiv:2103.03458 (2021).
5. R. Fulsche, *Essential positivity for Toeplitz operators on Fock spaces*, arXiv:2405.15496 (2024).
