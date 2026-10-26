# A seventh-order moment law for narrow-band Fourier concentration on bounded sets

## Finding

Let \(E\subset\mathbb R\) be any bounded Lebesgue-measurable set of positive measure \(m=|E|\). Write its centroid as \(t_0=m^{-1}\int_E t\,dt\), and its centered moments as \(\mu_j=m^{-1}\int_E(t-t_0)^j\,dt\). For \(W>0\), define the optimal bandlimited concentration fraction
\[
\Lambda_E(W)=\sup_{0\ne f\in L^2(\mathbb R),\;\operatorname{supp}\widehat f\subset[-W/2,W/2]}
\frac{\int_E |f(t)|^2\,dt}{\int_{\mathbb R}|f(t)|^2\,dt},\qquad
\widehat f(\xi)=\int_{\mathbb R} f(t)e^{-2\pi i\xi t}\,dt.
\]
As \(W\downarrow0\), the following asymptotic expansion holds for every such \(E\):
\[
\begin{aligned}
\frac{\Lambda_E(W)}{mW}={}&1-\frac{\mu_2}{3}(\pi W)^2
+\frac{2\mu_4+\mu_2^2}{45}(\pi W)^4\\
&+\frac{7\mu_2^3-10\mu_2\mu_4+23\mu_3^2-3\mu_6}{945}(\pi W)^6
+O\big((WD)^8\big),
\end{aligned}
\]
where \(D=\operatorname{essdiam}(E)\). The remainder is uniform over measurable \(E\) of fixed positive measure and diameter at most a fixed constant when \(WD\) is sufficiently small, with an absolute constant after the displayed normalization.

The normalized leading concentration eigenfunction on \(L^2(E)\), with a positive mean, obeys
\[
u_W(t)=m^{-1/2}\left[1-\frac{(\pi W)^2}{6}\big((t-t_0)^2-\mu_2\big)\right]
+O_{L^2(E)}\big((WD)^4\big).
\]
In particular, if \(I\) is any interval of length \(m\), then
\[
\Lambda_I(W)-\Lambda_E(W)=\frac{\pi^2m}{3}\left(\mu_2-\frac{m^2}{12}\right)W^3+O_E(W^5),
\]
with strictly positive leading coefficient unless \(E\) is an interval modulo null sets.

## Assumptions and scope

The set need not be connected, regular, symmetric, or a finite union of intervals; boundedness and \(0<m<\infty\) suffice. Essential diameter removes irrelevant null-set outliers. The expansion treats the bandwidth \(W\to0\) for a **fixed** observation set. The concentration fraction is an \(L^2\) energy fraction, not a pointwise bound. The Fourier transform and bandwidth conventions above fix every factor of \(\pi\).

## Proof

**1. Concentration operator and normalization.** Fourier inversion and Plancherel identify the nonzero spectrum of bandlimiting followed by restriction to \(E\) with the compact self-adjoint integral operator on \(L^2(E)\) of kernel
\[
K_W(x,y)=\int_{-W/2}^{W/2}e^{2\pi i\xi(x-y)}\,d\xi
=W\,\operatorname{sinc}\big(\pi W(x-y)\big),\qquad
\operatorname{sinc}(z)=\frac{\sin z}{z}.
\]
Its largest eigenvalue is \(\Lambda_E(W)\). With \(d\nu(x)=dx/m\) on \(E\), and centered coordinate \(X=x-t_0\), this is \(mW\) times the largest eigenvalue \(\lambda(\varepsilon)\) of \(B_\varepsilon\) acting on \(L^2(\nu)\), where \(\varepsilon=(\pi W)^2\) and
\[
B_\varepsilon(X,Y)=\operatorname{sinc}(\sqrt\varepsilon(X-Y))
=\sum_{j=0}^{\infty}\frac{(-1)^j\varepsilon^j(X-Y)^{2j}}{(2j+1)!}.
\]
The last power series is entire in \(\varepsilon\) and converges in operator norm uniformly when \(|\varepsilon|D^2\) is bounded. At \(\varepsilon=0\), \(B_0=P\), the rank-one orthogonal projection onto constant functions, whose simple eigenvalue \(1\) has gap \(1\) from the remaining spectrum. Consequently \(\lambda\) and its normalized eigenvector admit convergent power series for sufficiently small \(|\varepsilon|D^2\), uniformly over these sets.

**2. Exact perturbation calculation.** Write \(B_\varepsilon=P+\varepsilon B_1+\varepsilon^2 B_2+\varepsilon^3B_3+O(\varepsilon^4D^8)\), where \(B_j(X,Y)=(-1)^j(X-Y)^{2j}/(2j+1)!\). Decompose \(L^2(\nu)=\mathbb C1\oplus QL^2(\nu)\), \(Q=I-P\). Set \(a=\langle1,B_1 1\rangle=-\mu_2/3\), \(v_1=QB_1 1=-(X^2-\mu_2)/6\), and
\[
v_2=QB_2 1=\frac{(X^4-\mu_4)+6\mu_2(X^2-\mu_2)-4\mu_3X}{120}.
\]
Taking the Schur complement of the constant block yields
\[
\begin{aligned}
\lambda(\varepsilon)={}&1+a\varepsilon
+\varepsilon^2\left(\langle1,B_2 1\rangle+\|v_1\|^2\right)\\
&+\varepsilon^3\left(\langle1,B_3 1\rangle
+2\langle v_1,v_2\rangle
+\langle v_1,B_1v_1\rangle-a\|v_1\|^2\right)+O(\varepsilon^4D^8).
\end{aligned}
\]
The needed centered-moment identities are
\[
\begin{aligned}
\langle1,B_2 1\rangle&=\mu_4/60+\mu_2^2/20,\\
\|v_1\|^2&=(\mu_4-\mu_2^2)/36,\\
\langle1,B_3 1\rangle&=-\mu_6/2520-\mu_2\mu_4/168+\mu_3^2/252,\\
2\langle v_1,v_2\rangle&=-(\mu_6+5\mu_2\mu_4-6\mu_2^3-4\mu_3^2)/360,\\
\langle v_1,B_1v_1\rangle&=\mu_3^2/108.
\end{aligned}
\]
Substitution produces the coefficients \((2\mu_4+\mu_2^2)/45\) and \((7\mu_2^3-10\mu_2\mu_4+23\mu_3^2-3\mu_6)/945\) exactly. Because \(|X-Y|\le D\) almost everywhere, the analytic remainder is \(O(\varepsilon^4D^8)\) uniformly for \(\varepsilon D^2\) sufficiently small.

**3. Eigenvector and shape gap.** The orthogonal part of the leading eigenvector is \(\varepsilon v_1+O_{L^2(\nu)}(\varepsilon^2D^4)\); its constant part differs from \(1\) only at order \(\varepsilon^2\). Conversion to \(L^2(E)\) gives the eigenfunction statement. For an interval \(I\) of length \(m\), the centered variance is \(m^2/12\); the symmetric-difference argument comparing \(E\) with the centered interval shows \(\mu_2\ge m^2/12\), with equality only for intervals modulo null sets. Subtracting the two expansions gives the asserted cubic-order gap.

## Verification

The coefficient identities are finite exact moment algebra, not a sampling-based inference. A self-contained optional numerical checker, `check_bandwidth_expansion.py`, computes leading Nyström eigenvalues with Gaussian quadrature for a disconnected two-interval set and a single interval at three positive bandwidths; in both cases the residual divided by \(mW(\pi W)^8\) remains bounded and nearly constant as predicted. These finite numerical tests corroborate normalization and signs; the operator-norm perturbation argument, not quadrature, proves the infinite-dimensional claim.

## Relationship to prior work

Baeza-Guasch's 2023 Paley–Wiener phase symmetrization and no-aliasing theorem addresses optimal interval concentration for specified bandwidth–diameter regimes and disconnected-set aliasing effects. It does not give the explicit arbitrary-observation-set low-bandwidth spectral moments above. Bonami and Karoui study the interval sinc-kernel / prolate eigenproblem, concentrating on spectral decay and approximation of prolate functions. Faou and Le Hénaff develop concentration operators for general spatial and spectral masks with computational spectral methods; the explicit geometric seventh-order expansion and nonzero-skewness coefficient are not presented in their examined sections. Andén and Romero study arbitrary-domain discrete multitaper concentration, not this one-dimensional fixed-set small-bandwidth expansion. The result is consistent with classical prolate perturbation for intervals but allows disconnected and nonsymmetric measurable sets and specifies the optimizer's first correction.

## Limitations

The result is asymptotic at fixed \(E\), not uniform for sets whose diameter grows as \(W\to0\). It does not give global-in-bandwidth eigenvalue inequalities or asymptotics for higher eigenvalues. The mathematical statement has undergone a proof and literature comparison; historical priority for all possible older small-bandwidth perturbation formulas cannot be guaranteed, particularly in unindexed non-open literature. Independent verification is not claimed here.

## References

1. O. Baeza-Guasch, *Phase symmetrization and a no-aliasing concentration principle in Paley–Wiener spaces* (2023), arXiv:2307.04558v1, https://arxiv.org/abs/2307.04558 .
2. A. Bonami and A. Karoui, *Spectral decay of the sinc kernel operator and approximations by prolate spheroidal wave functions* (2010), arXiv:1012.3881, https://arxiv.org/abs/1012.3881 .
3. E. Faou and Y. Le Hénaff, *A general framework for the spectral analysis of concentration operators* (2024), arXiv:2410.01465, https://arxiv.org/abs/2410.01465 .
4. J. Andén and J. L. Romero, *Multitaper estimation on arbitrary domains* (2018), arXiv:1812.03225, https://arxiv.org/abs/1812.03225 .
