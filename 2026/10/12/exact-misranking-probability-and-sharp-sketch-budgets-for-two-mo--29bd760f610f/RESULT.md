# Starting-error deterioration under two-mode fixed Gaussian sketch powering

## Finding

Let \(A=\operatorname{diag}(\kappa,1,0,\ldots,0)\in\mathbb R^{N\times N}\) with \(\kappa>1\). Take \(\ell\ge2\), \(N\ge\ell+1\), an \(N\times\ell\) standard real Gaussian matrix \(\Phi\), and an independent standard Gaussian vector \(\omega\). Put \(K=(A\Phi)(A\Phi)^{\mathsf T}\), \(Y=A\omega\), and let \(Q_q\) be the normalized vector \(K^qY\). In exact arithmetic, define \(R_q=\|(I-Q_qQ_q^{\mathsf T})A\|_F^2\) and \(R_\infty=\lim_{q\to\infty}R_q\). As proxy width \(\ell\to\infty\) at fixed \(\kappa>1\),
\[
\Pr(R_\infty>R_0)\sim
\frac{2}{\pi}\sqrt{\frac{2}{\pi}}\frac{\kappa^2}{\kappa^2-1}\,\ell^{-1/2}.
\]
In contrast, the probability of the limiting error exceeding the midpoint \((\kappa^2+1)/2\) is exactly
\[
p_\ell(\kappa)=I_{1/(1+\kappa^2)}(\ell/2,\ell/2),
\qquad \lim_{\ell\to\infty} p_\ell(\kappa)^{1/\ell}=\frac{2\kappa}{\kappa^2+1}<1,
\]
where \(I_z\) denotes the regularized incomplete beta function. The absolute-error benchmark and the random starting-error benchmark thus have different decay rates. A positive difference \(R_\infty-R_0\) means all sufficiently high powers perform worse than the starting sketch on that draw, not that the errors are monotone in depth or that the deterioration is large.

## Proof

In the first two coordinates, \(K\) has entries \(a=\kappa^2 U\), \(b=\kappa T\), and \(d=V\), with \(U=\sum_j\phi_{1j}^2\), \(V=\sum_j\phi_{2j}^2\), and \(T=\sum_j\phi_{1j}\phi_{2j}\). It has two positive distinct eigenvalues almost surely. Its independent Gaussian starting vector has a nonzero leading component almost surely, so the powered line converges to the top line, represented by a unit vector \(v=(v_1,v_2)\). For a unit vector \(u\) in the signal plane, the squared projection error is \(1+(\kappa^2-1)u_2^2\), increasing strictly with the absolute slope \(|u_2/u_1|\). The initial absolute slope is \(|\omega_2/\omega_1|/\kappa\), a scaled absolute standard Cauchy random variable independent of \(K\). Conditioning on \(K\) therefore gives the exact relation
\[
\Pr(R_\infty>R_0)=\mathbb E\left[\frac{2}{\pi}\arctan(\kappa |v_2/v_1|)\right].
\]
(A vertical limiting line, a null event, can be interpreted by continuity.)

Let \(\Delta=\kappa^2-1\). On the event \(G_\ell=\{a-d\ge\Delta\ell/2\}\), the leading slope is
\[
|v_2/v_1|=\frac{2|b|}{a-d+\sqrt{(a-d)^2+4b^2}}\le\frac{|b|}{a-d}.
\]
The diagonal difference has mean \(\Delta\ell\) and variance \(2(\kappa^4+1)\ell\), so Chebyshev gives \(\Pr(G_\ell^c)=O(\ell^{-1})\). Hence its contribution to \(\sqrt\ell\Pr(R_\infty>R_0)\) vanishes. By the law of large numbers and the scalar CLT, \((a-d)/\ell\to\Delta\) in probability and \(b/\sqrt\ell\Rightarrow\kappa Z\) for \(Z\sim N(0,1)\). The slope formula and \(\arctan x/x\to1\) at zero give
\[
\sqrt\ell\,\mathbf1_{G_\ell}\arctan(\kappa |v_2/v_1|)\Rightarrow \frac{\kappa^2}{\Delta}|Z|.
\]
On \(G_\ell\) this variable is bounded by \(2\kappa^2|T|/(\Delta\sqrt\ell)\), whose second moment is bounded uniformly since \(\mathbb ET^2=\ell\). Uniform integrability implies convergence of expectations. Inserting \(\mathbb E|Z|=\sqrt{2/\pi}\) proves the deterioration law.

For comparison, the difference of the diagonal entries of the top eigenprojector is \((a-d)/\sqrt{(a-d)^2+4b^2}\). Hence \(v_2^2>1/2\) iff \(V>\kappa^2 U\), almost surely. The independent chi-squares \(U,V\) have \(U/(U+V)\sim\operatorname{Beta}(\ell/2,\ell/2)\), proving the exact beta law. For its exponential rate, put \(z=1/(1+\kappa^2)<1/2\). The numerator integral of \([t(1-t)]^{\ell/2-1}\) over \([0,z]\) has \(\ell\)th root tending to \(\sqrt{z(1-z)}\): bound the integrand above by its maximum and below on a fixed interval near \(z\), then let that interval approach \(z\). The denominator over \([0,1]\) has root tending to \(1/2\) by the same argument near \(1/2\). Their ratio gives the stated root. Also, among reconstructions with left factor \(v\), the orthogonal projection minimizes squared Frobenius error, so the midpoint event applies to every reconstruction confined to that line.

## Relation to prior work and scope

Chang and Yang [1] give the fixed-proxy scheme and already identify its limiting singular subspace. The two-by-two covariance reduction uses the classical independent chi-square/beta ratio. Classical Gaussian PCA describes the fluctuation of sample eigenvectors; for example [2, Lemma 2.3] gives the fixed-gap Gaussian fluctuation and a stronger local-gap eigenvector law. The contribution here is the comparison against the independent unpowered starting error: it uses the conditional Cauchy probability and the moment transfer to obtain a deterioration rate much slower than the absolute midpoint-exceedance rate. No novelty of a classical angular CLT, beta-tail calculation, or local-gap limit is asserted. The result does not apply to ordinary power iteration using \(AA^{\mathsf T}\), to resampled proxies, or to complete oversampled co-range reconstruction.

## References

1. C. Chang and Y. Yang, *Improving Sketching Algorithms for Low-Rank Matrix Approximation via Sketch-Power Iterations*, arXiv:2603.26298v1, §1 and §7.
2. D. Paindaveine, J. Remy, and T. Verdebout, “Testing for principal component directions under weak identifiability,” *Annals of Statistics* 48 (2020), 324–345, DOI 10.1214/18-AOS1805.
