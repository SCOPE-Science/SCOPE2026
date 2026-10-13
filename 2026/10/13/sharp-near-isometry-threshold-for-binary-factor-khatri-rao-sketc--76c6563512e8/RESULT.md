# Sharp near-isometry threshold for binary-factor Khatri–Rao sketches

## Finding
Fix \(0<\varepsilon<1\), and let \(N=2^d\) tend to infinity through powers of two. Form a Khatri–Rao sketch with independent columns that are Kronecker products of \(d\) independent, two-entry Rademacher factors. If the number of columns is \(m=\lfloor cN\log N\rfloor\), its covariance embedding is an \(\varepsilon\)-near-isometry on the **whole** ambient space with probability tending to zero or one according as
\[
 c< c_*(\varepsilon):=\frac{1}{(1+\varepsilon)\log(1+\varepsilon)-\varepsilon}
 \quad\text{or}\quad c>c_*(\varepsilon).
\]
The boundary case is not decided. This gives the exact leading constant for the oversampling requirement in this natural discrete tensor-sketch model, not merely an exponential-in-tensor-order bound or a rank condition.

An exact finite-dimensional characterization accompanies the threshold: the sketch covariance is diagonal in a fixed Walsh–Hadamard basis, with eigenvalues equal to normalized multinomial category counts. In particular, its full-rank probability is given by an explicit inclusion–exclusion formula. For the illustrative distortion \(\varepsilon=1/2\), the critical coefficient is \(9.242343873386666\ldots\), whereas the leading coefficient for full rank is only \(1\). The latter is the classical coupon-collector scale, not a claim of a new coupon-collector theorem.

## Assumptions and scope
For every integer \(d\ge1\), put \(N=2^d\). Independently for each \(r\in\{1,\ldots,d\}\) and \(j\in\{1,\ldots,m\}\), let \(\xi_{rj}=(\xi_{rj,1},\xi_{rj,2})\) with independent coordinates each equal to \(-1\) or \(+1\) with probability one half. Set
\[
 w_j=\xi_{1j}\otimes\cdots\otimes\xi_{dj}\in\mathbb R^N,\qquad
 \Psi_{d,m}=m^{-1/2}[w_1\ \cdots\ w_m],\qquad
 S_{d,m}=\Psi_{d,m}\Psi_{d,m}^{\mathsf T}.
\]
A full-space squared-norm \(\varepsilon\)-embedding means
\[
 (1-\varepsilon)\|x\|_2^2\le \|\Psi_{d,m}^{\mathsf T}x\|_2^2
 \le(1+\varepsilon)\|x\|_2^2\quad\text{for all }x\in\mathbb R^N,
\]
equivalently \(\|S_{d,m}-I_N\|_{\mathrm{op}}\le\varepsilon\). The probability concerns all factor and column draws; the asymptotics keep \(c\) and \(\varepsilon\) fixed. The logarithm is natural. The sampling matrix uses *independent* columns and unmodified real Rademacher factors; there is no sign preconditioning or orthogonalization.

## Proof
**Exact spectral reduction.** Write each factor uniquely as \(\xi_{rj}=\sigma_{rj}(1,t_{rj})\), where \(\sigma_{rj},t_{rj}\) are independent fair signs. Let \(h_t=\bigotimes_{r=1}^d(1,t_r)\) for \(t\in\{-1,1\}^d\). The \(N\) vectors \(h_t\) satisfy \(h_t^{\mathsf T}h_u=N\mathbf1_{t=u}\). Moreover, \(w_j=\eta_jh_{T_j}\) where \(\eta_j\) is a sign and \(T_j\) is uniform on the \(N\) labels, independent across \(j\). Thus, with \(C_t=\#\{j:T_j=t\}\),
\[
 S_{d,m}=\frac1m\sum_t C_t h_th_t^{\mathsf T},\qquad
 S_{d,m}h_t=\frac{NC_t}{m}h_t.
\]
This proves the claimed exact eigenvalue law. Full rank holds precisely when no category is empty; inclusion–exclusion yields
\[
 \Pr(\operatorname{rank}\Psi_{d,m}=N)
 =\sum_{j=0}^N(-1)^j{N\choose j}(1-j/N)^m.
\]
In particular, \(\mathbb E(N-\operatorname{rank}\Psi_{d,m})=N(1-1/N)^m\). These are finite exact identities. At the full-rank scale \(m=\lfloor cN\log N\rfloor\), the expected number of missing labels is \(N^{1-c+o(1)}\). When \(c>1\), Markov’s inequality shows that all labels appear with probability tending to one. When \(c<1\), empty-bin indicators also have nonpositive pairwise covariances, since \(\Pr(C_s=C_t=0)=(1-2/N)^m\le(1-1/N)^{2m}\), and the second-moment bound gives full-rank probability tending to zero. Thus the classical full-rank coefficient is exactly one.

**Sufficient sample coefficient.** Write \(\lambda=m/N\) and define the Poisson rate functions
\[
 H_+(u)=(1+u)\log(1+u)-u,\qquad
 H_-(u)=u+(1-u)\log(1-u).
\]
Every count \(C_t\) is \(\mathrm{Bin}(m,1/N)\). Its Chernoff bounds give \(\Pr(C_t>(1+\varepsilon)\lambda)\le e^{-\lambda H_+(\varepsilon)}\) and \(\Pr(C_t<(1-\varepsilon)\lambda)\le e^{-\lambda H_-(\varepsilon)}\). On \((0,1)\), \(H_->H_+>0\): their difference vanishes at zero and has derivative \(-\log(1-\varepsilon^2)>0\). Consequently,
\[
 \Pr(\|S_{d,m}-I_N\|_{\mathrm{op}}>\varepsilon)
 \le N e^{-\lambda H_+(\varepsilon)}+N e^{-\lambda H_-(\varepsilon)}.
\]
For \(m=\lfloor cN\log N\rfloor\) and \(cH_+(\varepsilon)>1\), this tends to zero.

**Necessity of that coefficient.** Suppose \(cH_+(\varepsilon)<1\). Let \(k=\lfloor(1+\varepsilon)\lambda\rfloor+1\), let \(I_t=\mathbf1_{\{C_t\ge k\}}\), and put \(Z=\sum_t I_t\). The local binomial mass at \(k\), compared to the Poisson mass with mean \(\lambda\), has ratio \(1+o(1)\) because \(k=O(\log N)\), \(m=\Theta(N\log N)\), \(k^2/m=o(1)\), and \(m/N^2=o(1)\). Stirling's formula therefore gives
\[
 \log\Pr(C_t=k)=-\lambda H_+(\varepsilon)+O(\log\lambda)+o(\log N)
 =-cH_+(\varepsilon)\log N+o(\log N).
\]
Hence \(\mathbb EZ=N\Pr(C_t\ge k)\ge N^{1-cH_+(\varepsilon)+o(1)}\to\infty\).

For distinct labels \(s\ne t\), conditional on \(C_s=a\), the remaining count has distribution \(C_t\mid C_s=a\sim\mathrm{Bin}(m-a,1/(N-1))\). The conditional probability \(\Pr(C_t\ge k\mid C_s=a)\) is nonincreasing in \(a\), whereas \(\mathbf1_{\{a\ge k\}}\) is nondecreasing. Oppositely monotone functions of one random variable have nonpositive covariance, so \(\mathrm{Cov}(I_s,I_t)\le0\). It follows that \(\operatorname{Var} Z\le\mathbb EZ\). By Chebyshev's inequality,
\[
 \Pr(Z=0)\le\frac{\operatorname{Var}Z}{(\mathbb EZ)^2}
 \le\frac1{\mathbb EZ}\longrightarrow0.
\]
If \(Z>0\), an eigenvalue of \(S_{d,m}\) exceeds \(1+\varepsilon\), and the embedding fails. This proves the converse and the strict two-sided phase transition. No assertion is made about \(c=c_*(\varepsilon)\).

## Verification
Run `python verify.py` with a standard Python interpreter; no third-party packages are needed. The supplied program constructs tensor-sign columns, identifies their Walsh label and exact Gram eigenvectors, and checks the full-rank inclusion–exclusion formula independently against Stirling-number counts and finite exhaustive experiments. It also checks the ordering of the two rate functions. These are finite exact consistency checks. The infinite-dimensional probability limits and the conditional covariance argument are proved above, not inferred from tests.

## Relationship to prior work
The source literature on tensorized sketches establishes embedding and least-squares performance guarantees, typically as upper bounds on sample size or more permissive subspace-injection conditions. Chen and Jin (2020) establish row-wise tensorized Rademacher sketching bounds for constrained least squares, with two tensor factors. Saibaba, Verma, and Ballard (2025) give a general Khatri–Rao subspace-embedding theorem for sub-Gaussian factors. Camaño, Epperly, Meyer, and Tropp (2025), Section 5.3, explicitly show the catastrophic one-vector orthogonality of *this same two-entry Rademacher factor distribution* and an exponential-in-order lower bound. Meyer, Swartworth, and Woodruff (2025) study adaptive Kronecker query lower bounds, including finite-alphabet zero testing. Beretta and Musco (2026) give general Khatri–Rao OSE sufficient bounds. None of those inspected results establishes the exact **full-space** covariance spectrum or the distortion-dependent sharp constant above. The reduction to occupancy, the classical Chernoff bounds and the coupon-collector formula are established tools; the claimed specific conclusion is their sharp combination for this numerical sketch model, not new occupancy theory.

## Limitations
This result is about full-space near-isometry under a particular discrete factor law; it is not a lower bound for all tensor sketches, all subspaces, or even all choices of factor distributions. It does not establish optimal computational runtime or gains over a dense Gaussian sketch. The critical equality window and the precise limiting probability there are not determined. The finite verifier cannot certify any asymptotic statement. Novelty is assessed against inspected accessible literature and could be affected by an equivalent specialized result elsewhere; independent audit has not been performed.

## References
1. K. Chen and R. Jin, *Tensor-structured sketching for constrained least squares*, arXiv:2010.09791 (first posted 2020-10-19), Sections 1–3. https://arxiv.org/abs/2010.09791
2. C. Camaño, E. N. Epperly, R. A. Meyer, and J. A. Tropp, *Faster Linear Algebra Algorithms with Structured Random Matrices*, arXiv:2508.21189 (2025), Sections 1.5.3, 5.3, 5.4. https://arxiv.org/abs/2508.21189
3. A. K. Saibaba, B. D. Verma, and G. Ballard, *Improved Analysis of Khatri-Rao Random Projections and Applications*, arXiv:2507.23207 (2025), Sections 2–3. https://arxiv.org/abs/2507.23207
4. R. A. Meyer, W. Swartworth, and D. P. Woodruff, *Understanding the Kronecker Matrix-Vector Complexity of Linear Algebra*, arXiv:2502.08029 (2025), Sections 1 and 3–5. https://arxiv.org/abs/2502.08029
5. L. Beretta and C. Musco, *A Tight Analysis of Khatri-Rao Oblivious Subspace Embeddings*, arXiv:2608.28094 (2026), main embedding theorem. https://arxiv.org/abs/2608.28094
