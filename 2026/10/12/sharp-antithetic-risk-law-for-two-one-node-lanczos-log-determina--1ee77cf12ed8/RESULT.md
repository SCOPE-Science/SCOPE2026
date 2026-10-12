# Sharp antithetic risk law for two one-node Lanczos log-determinant probes

## Finding

Let \(A\) be any real symmetric positive-definite \(2\times2\) matrix with distinct eigenvalues \(\lambda>\mu>0\), and put \(\kappa=\lambda/\mu\). For Haar-uniform unit vectors \(v,w\in\mathbb R^2\), with arbitrary dependence but individually uniform marginals, consider the **two separate one-node Lanczos quadratures**
\[
\widehat L(v,w)=\log(v^{\mathsf T}Av)+\log(w^{\mathsf T}Aw),
\qquad L=\log\det A.
\]
Write
\[
 h=\tfrac14\log\kappa,\qquad k=\tanh h,\qquad B=4\log\cosh h,
\qquad \operatorname{Li}_2(z)=\sum_{j=1}^{\infty}\frac{z^j}{j^2}.
\]
Then every admissible coupling has the **same strictly positive bias** \(\mathbb E(\widehat L-L)=B\). Among all such couplings, an orthogonal (antithetic) pair \(w=Jv\), where \(J\) is a fixed quarter-turn, minimizes both variance and mean-squared error. Equality holds precisely when the two squared projections onto a \(\lambda\)-eigenvector add to one almost surely; this describes all minimizing couplings at the level relevant to the estimator.

The **exact optimum and independent-probe risks** are
\[
\begin{aligned}
 \operatorname{Var}(\widehat L_{\perp})&=2\operatorname{Li}_2(k^4),
& \mathbb E(\widehat L_{\perp}-L)^2&=B^2+2\operatorname{Li}_2(k^4),\\
 \operatorname{Var}(\widehat L_{\mathrm{iid}})&=4\operatorname{Li}_2(k^2),
& \mathbb E(\widehat L_{\mathrm{iid}}-L)^2&=B^2+4\operatorname{Li}_2(k^2).
\end{aligned}
\]
The antithetic inequalities are strict against iid probes whenever \(\kappa>1\).

More precisely, the antithetic **entire error law** is
\[
\widehat L_{\perp}-L\ \overset{\mathrm d}=\
\log(1+\tau W),\quad \tau=\frac{(\kappa-1)^2}{4\kappa},\quad
W\sim\operatorname{Beta}(\tfrac12,\tfrac12).
\]
For \(0\le\xi\le\log(1+\tau)\), its CDF is
\[
\mathbb P(\widehat L_{\perp}-L\le\xi)
=\frac2\pi\arcsin\sqrt{\frac{\exp(\xi)-1}{\tau}}.
\]
Outside this interval the CDF is respectively zero or one. In particular the antithetic error is nonnegative for **every** probe, whereas the iid error need not be. With \(s=\log\kappa\downarrow0\),
\[
 \mathbb E(\widehat L_{\perp}-L)^2=\frac{3s^4}{128}+O(s^6),
 \qquad
 \mathbb E(\widehat L_{\mathrm{iid}}-L)^2=\frac{s^2}{4}+O(s^4).
\]
Thus antithetic coupling cancels the first-order random error, but not the one-node quadrature bias.

## Assumptions and scope

The matrix is real, two-dimensional, strictly positive definite, and nonscalar. Each direction separately follows normalized Haar measure on the Euclidean unit circle; its orientation or sign may depend on the other direction. Each scalar Lanczos calculation stops after **one** iteration and uses its own \(1\times1\) tridiagonal matrix \([v^{\mathsf T}Av]\) or \([w^{\mathsf T}Aw]\). This is **not** two-step Lanczos, block Lanczos, or a trace estimator based on exact evaluation of \(v^{\mathsf T}(\log A)v\). Two applications of \(A\) suffice to evaluate the separate Rayleigh quotients in exact arithmetic.

The result optimizes coupling **within this fixed two-scalar-one-node estimator class**, not across different estimators or access models. For \(\lambda=\mu\), separately excluded above, both estimators equal \(L\) exactly for all directions, with zero bias and variance.

## Proof

**One-node identification.** For a unit starting vector \(v\), one Lanczos step has scalar tridiagonal entry \(v^{\mathsf T}Av\), so scalar Gaussian quadrature applied to \(f(t)=\log t\) yields \(\log(v^{\mathsf T}Av)\). Orthogonal diagonalization makes the joint distribution depend only on \(\lambda,\mu\). Parameterize one Haar direction as \(v=(\cos\theta,\sin\theta)^{\mathsf T}\), with \(\theta\) uniform modulo \(\pi\). Define
\[
 a=\left(\frac{\sqrt\lambda+\sqrt\mu}{2}\right)^2,
 \qquad k=\frac{\sqrt\lambda-\sqrt\mu}{\sqrt\lambda+\sqrt\mu}=\tanh h.
\]
Then direct multiplication gives the exact trigonometric factorization
\[
 R(\theta)=v^{\mathsf T}Av
 =\lambda\cos^2\theta+\mu\sin^2\theta
 =a\left|1+k\exp(2\mathrm i\theta)\right|^2.
\]
Since \(0<k<1\), the following real Fourier series converges absolutely and uniformly:
\[
 \log R(\theta)=\log a+
 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}k^n}{n}\cos(2n\theta).
\]
Its expectation is \(\log a\); therefore the two-node estimator's expectation, independent of coupling, is \(2\log a\). Writing \(\sqrt\lambda=\sqrt\mu\exp(2h)\) gives
\[
 2\log a-\log(\lambda\mu)=4\log\cosh h=B>0.
\]

**Exact independent and orthogonal variances.** Parseval orthogonality \(\mathbb E\cos^2(2n\theta)=1/2\) yields
\[
 \operatorname{Var}(\log R(\theta))
 =2\sum_{n\ge1}\frac{k^{2n}}{n^2}=2\operatorname{Li}_2(k^2).
\]
Adding two independent copies doubles this variance. Under a quarter-turn, \(R(\theta+\pi/2)=\lambda\sin^2\theta+\mu\cos^2\theta\), and the Fourier terms of odd index cancel in their log sum, leaving
\[
 \log R(\theta)+\log R(\theta+\pi/2)
 =2\log a-2\sum_{j\ge1}\frac{k^{2j}}{j}\cos(4j\theta).
\]
Parseval then gives \(2\operatorname{Li}_2(k^4)\). Because \(0<k<1\), the difference \(4\operatorname{Li}_2(k^2)-2\operatorname{Li}_2(k^4)>0\). Adding the common squared bias gives the stated risks.

**Global optimality over all probe couplings.** Write \(U=|\langle v,e_\lambda\rangle|^2\), where \(e_\lambda\) is a unit \(\lambda\)-eigenvector. For a Haar direction, \(U\sim\operatorname{Beta}(1/2,1/2)\), whose distribution is nonatomic and invariant under \(u\mapsto1-u\). The one-point output is \(g(U)=\log(\mu+(\lambda-\mu)U)\), a strictly increasing continuous function of \(U\). For two copies with fixed marginals, variance differs only through \(2\mathbb E[g(U)g(V)]\). The rearrangement inequality states that this expectation is minimized when the two quantiles are paired in opposite order. Here its minimizing coupling is exactly \(V=1-U\) almost surely. For completeness, in every finite quantile partition, replacing two same-order pairs \((u_1,v_1),(u_2,v_2)\) with \(u_1<u_2\) and \(v_1<v_2\) by crossed pairs changes the old minus new product sum by
\[
 [g(u_2)-g(u_1)]\,[g(v_2)-g(v_1)]>0.
\]
Repeated crossings yield the oppositely sorted pairing. Approximation by successively finer equal-mass quantile partitions and bounded continuity of \(g\) proves optimality; strict monotonicity and the nonatomic marginal show that equality requires countermonotone quantile pairing almost surely. Since the beta distribution is symmetric, this is \(V=1-U\). A quarter-turn realizes that pairing. The squared bias is fixed, so the same coupling minimizes mean-squared error.

**Distribution and small-contrast boundary.** Multiplication of the perpendicular Rayleigh quotients gives
\[
 R(\theta)R(\theta+\pi/2)
 =\lambda\mu+(\lambda-\mu)^2\cos^2\theta\sin^2\theta
 =\lambda\mu\bigl(1+\tau\sin^2(2\theta)\bigr).
\]
A Haar angle makes \(\sin^2(2\theta)\) arcsine-distributed, establishing the support and CDF. Finally \(k=\tanh(s/4)=s/4+O(s^3)\), \(B=4\log\cosh(s/4)=s^2/8+O(s^4)\), and \(\operatorname{Li}_2(z)=z+O(z^2)\) near zero. Substitution gives \(B^2+2\operatorname{Li}_2(k^4)=3s^4/128+O(s^6)\) and \(B^2+4\operatorname{Li}_2(k^2)=s^2/4+O(s^4)\). No finite experiment is used in these analytic steps.

## Verification

Run \(\texttt{python3 verify.py}\) using the accompanying standalone source. It checks 252 exact-rational Rayleigh-product identities, 870 exhaustive finite-quantile rearrangement inequalities, 35 transformed arcsine CDF identities, 21 numerical quadrature moment comparisons using midpoint integration, and six leading-coefficient checks. These provide reproducible falsification tests; the preceding algebraic, Fourier, and rearrangement arguments establish the infinite statements.

## Relationship to prior work

Chen, Trogdon, and Ubaru (arXiv:2204.01941; first public version 2022-04-05) formalize randomized matrix-free quadrature and explicitly average independently drawn weighted spectral measures before Lanczos quadrature; their §§1 and 3.2 identify the basic object and Gaussian quadrature construction. Chen, Trogdon, and Ubaru (arXiv:2105.06595) analyze stochastic Lanczos spectral approximation with independent spherical probes. These works motivate the estimator but do not in their inspected results state this fixed-two-probe antithetic optimal coupling or the two-dimensional log-determinant risk distribution and dilogarithm formulas.

Yeon, Ghosal, and Anitescu (arXiv:2505.12289), in the later BOLT method, analyze orthonormal **block** probes and \(v^{\mathsf T}f(A)v\)-type trace moments. With a full two-column block in dimension two, that approach can calculate the exact log-determinant; this is a **different, stronger estimator**, not a contradiction or prior proof of the nonzero one-node scalar risk established here. Standard countermonotone rearrangement is used as a known inequality, not claimed as a new mathematical principle. The contribution is the combined sharp coupling statement, exact nonlinear scalar-quadrature risk, and small-gap order separation for this specific sampling design.

## Limitations

The exact minimax optimality is conditional on individually Haar-uniform directions and a prescribed sum of two *separately* evaluated scalar one-node Lanczos logarithms. It does not apply to alternative estimators that combine the two observed Rayleigh values as a matrix, apply block Lanczos, use more iterations, allow non-Haar marginals, or exploit additional matrix entries. In particular it is **not** a universal lower bound on two-matrix-vector-product log-determinant estimation. There is no established analogue here in dimensions above two, and numerical floating-point conditioning is not analyzed. The bibliographic novelty comparison is based on inspected accessible work and indexed searches, not on exhaustive access to unpublished or unindexed results.

## References

1. T. Chen, T. Trogdon, S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941, first submitted 2022-04-05; SIAM J. Sci. Comput. (2025), DOI 10.1137/23M1600414. https://arxiv.org/html/2204.01941v3
2. T. Chen, T. Trogdon, S. Ubaru, *Analysis of stochastic Lanczos quadrature for spectrum approximation*, arXiv:2105.06595 (2021). https://arxiv.org/html/2105.06595v2
3. K. Yeon, P. Ghosal, M. Anitescu, *BOLT: Block-Orthonormal Lanczos for Trace Estimation of Matrix Functions*, arXiv:2505.12289 (2025). https://arxiv.org/html/2505.12289v2
4. R. A. Horn, C. R. Johnson, *Matrix Analysis*, Cambridge University Press, 2nd ed. (2012), for standard spectral facts and rearrangement background.
