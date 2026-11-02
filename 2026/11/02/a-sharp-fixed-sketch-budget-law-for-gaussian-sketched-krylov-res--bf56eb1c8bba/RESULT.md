# A sharp fixed-sketch budget law for Gaussian-sketched Krylov residuals

## Finding
Fix a real spectral condition-number bound \(K>1\) and an integer Gaussian sketch budget \(s\ge3\). For every Krylov depth \(0\le k\le s-2\), the sharp worst-case expected squared true residual for a one-shot sketched GMRES solve on real symmetric positive-definite matrices, relative to the initial squared residual, is
\[
 R_{s,k}(K)=\frac{s-1}{s-k-1}\operatorname{sech}^{2}\left(k\operatorname{arcosh}\frac{K+1}{K-1}\right).
\]
The supremum is attained for \(k\ge1\) by explicit \((k+1)\)-point Chebyshev spectral extremizers, and \(R_{s,0}=1\). If the deterministic best residual is nonzero, a sketch with \(s=k\) or \(s=k+1\) has **infinite expected squared true residual** even though the almost-sure sketched solution exists.

Write \(a=\operatorname{arcosh}((K+1)/(K-1))\) and \(B_K=(e^{2a}-1)^{-1}=(\sqrt K-1)^2/(4\sqrt K)\). For each fixed \(K>1\), for all sufficiently large integers \(s\), the **unique** choice of depth minimizing the sharp worst-case expected squared residual over \(0\le k\le s-2\) is
\[
 \boxed{k_s=s-1-t_K,\qquad t_K=\lfloor B_K\rfloor+1.}
\]
Consequently, the optimal fixed mean-square oversampling reserve \(t_K=s-k_s-1\) has scale \(\sqrt K/4+O(1)\) as \(K\to\infty\). At exact integral values of \(B_K\), the larger of the two asymptotically tied reserves is strictly preferable for sufficiently large finite \(s\).

## Assumptions and scope
Let \(A\) be any real symmetric positive-definite \(n\times n\) matrix, \(r\ne0\) an initial residual, and \(\sigma(A)\subseteq[\mu,L]\), where \(0<\mu<L\) and \(L/\mu=K\). The \(k\)-step Krylov correction space is \(\mathcal K_k(A,r)=\operatorname{span}\{r,Ar,\ldots,A^{k-1}r\}\), with \(\mathcal K_0=\{0\}\). Draw a single fresh matrix \(S\in\mathbb R^{s\times n}\) of independent \(N(0,1/s)\) entries, independent of \(A,r\), and choose \(z\in\mathcal K_k(A,r)\) minimizing \(\|S(r-Az)\|_2\); denote the resulting true residual by \(\widehat r_k=r-Az\). Every depth is considered as a separate one-shot solve with the prescribed row budget \(s\). In particular, the theorem does not assert validity for data-dependent stopping using the same sketch, nor that computing the deepest subspace is free. When the Krylov space terminates early, the residual is exactly zero.

The guarantee is over all dimensions \(n\ge k+1\) and all such \(A,r\). If one requires actual dimension reduction \(s<n\), the equality examples may be padded with spectrally admissible coordinates on which \(r\) vanishes. The risk is an expectation over the Gaussian sketch alone. No floating-point or cost-of-matvec claim is made.

## Proof
**1. Exact Gaussian projection risk.** Fix a full-rank \(n\times k\) correction-image basis \(V=A[r,Ar,\ldots,A^{k-1}r]\). Write the Euclidean orthogonal residual \(r_*=r-V(V^{\mathsf T}V)^{-1}V^{\mathsf T}r\), \(d=\|r_*\|_2/\|r\|_2\). By orthogonal invariance of the Gaussian sketch, after whitening columns of \(V\), its sketch is a standard \(s\times k\) Gaussian matrix \(G\), independent of the sketched component \(g\) from \(r_*\). The excess fitted-coefficient vector is \(G^\dagger g\), and Euclidean Pythagoras gives
\[
 \frac{\|\widehat r_k\|_2^2}{\|r_*\|_2^2}\ \overset{d}{=}\ 1+\frac{X}{Y},\qquad X\sim\chi_k^2,\quad Y\sim\chi_{s-k+1}^2,\quad X\perp Y.
\]
This is the established Gaussian complete-sketch Student law; alternatively, it follows by conditioning on the Gaussian design and the inverse-Wishart identity. For \(s\ge k+2\), \(\mathbb E[X/Y]=k/(s-k-1)\). Therefore
\[
 \mathbb E\|\widehat r_k\|_2^2=\frac{s-1}{s-k-1}\|r_*\|_2^2.
\]
For \(s=k\) or \(k+1\), the denominator chi-square has at most two degrees of freedom, so the positive excess has divergent first moment whenever \(r_*\ne0\). For \(k=0\), no adjustment is made.

**2. Sharp Krylov minimax.** A \(k\)-step true GMRES residual has the polynomial representation \(p(A)r\), with \(\deg p\le k\) and \(p(0)=1\). The classical Chebyshev extremal argument gives
\[
 \min_{p(0)=1}\max_{\lambda\in[\mu,L]}|p(\lambda)|=\operatorname{sech}(ka).
\]
For equality set \(\lambda_i=(L+\mu)/2+(L-\mu)\cos(i\pi/k)/2\), \(0\le i\le k\), and let \(D_i=\prod_{j\ne i}(\lambda_i-\lambda_j)\). Take \(A=\operatorname{diag}(\lambda_0,\ldots,\lambda_k)\) and positive normalized \(w_i\propto[\lambda_i|D_i|]^{-1}\), with \(r_i=\sqrt{w_i}\). The normalized Chebyshev polynomial \(p_*\) has alternating values of constant magnitude at these points and \(\operatorname{sign}p_*(\lambda_i)=\operatorname{sign}D_i\), up to a common sign. Consequently, the GMRES normal equations hold:
\[
 \sum_{i=0}^{k}w_i\lambda_i^j p_*(\lambda_i)
 \ \propto\ \sum_{i=0}^{k}\frac{\lambda_i^{j-1}}{D_i}=0
 \quad (1\le j\le k),
\]
where the last equality is the barycentric interpolation identity for polynomials of degree at most \(k-1\). Thus the \(k\)-step Euclidean GMRES residual is exactly \(\operatorname{sech}(ka)\|r\|_2\), and the worst-case stochastic formula follows with equality.

**3. Exact eventual budget optimizer.** Set the positive integer reserve \(t=s-k-1\), so \(1\le t\le s-1\). Up to a factor independent of \(t\), the minimax risk is
\[
 \frac{e^{2at}}{t\,[1+e^{-2a(s-1-t)}]^2}.
\]
For each fixed \(t\), this tends to \(g(t)=e^{2at}/t\). Its adjacent ratio is \(g(t+1)/g(t)=e^{2a}t/(t+1)\), so its discrete minimum is at \(t=\lfloor(e^{2a}-1)^{-1}\rfloor+1\), except that an integer value \(B_K=m\) gives a tie between \(t=m\) and \(m+1\). In the tied case, the finite-\(s\) correction strictly favors \(m+1\), because its denominator is larger. To justify minimizing the asymptotics globally over a growing set of candidate reserves, use \(e^{-2x}\le\operatorname{sech}^2x\le4e^{-2x}\) for \(x\ge0\). Any minimizer must then satisfy \(g(t)\le4g(t_K)\), so all optimal reserves lie in a finite set independent of \(s\). Pairwise convergence and the tie correction complete the eventual uniqueness proof. The exact identity \(B_K=(\sqrt K-1)^2/(4\sqrt K)\) yields the stated large-condition-number reserve.

## Verification
A standalone script `verify.py` checks the Chebyshev equality construction for 16 combinations of degree and condition bound, numerically solves the unsketched least-squares problems, generates 18,000 genuinely Gaussian sketch-and-solve examples, compares mean and median to the exact Student risk, tests 15 finite-budget optimizations including the integral-reserve tie, and checks arithmetic with numerical tolerances. It prints `VERIFY_OK` on success. These finite tests are diagnostic; the all-dimension result is established by the proof above.

## Relationship to prior work
Nakatsukasa and Tropp introduced the sGMRES sketch-and-solve formulation with subspace-embedding performance guarantees. Ahfock, Astle and Richardson established the exact multivariate Student law for complete Gaussian-sketched least squares; the one-depth Gaussian risk identity here is an application of their theorem, not a new distributional result. Classical Chebyshev polynomial bounds and worst-case GMRES theory give the separate deterministic extremal ingredient. The distinct conclusion investigated here is the **sharp joint fixed-row-budget minimax risk and eventual integer-valued depth/reserve law**, including integral tie resolution and an attainable SPD extremal family. Related randomized GMRES papers use prescribed oversampling ratios rather than this exact mean-square minimax optimization.

## Limitations
The risk criterion is squared true residual in exact arithmetic, not elapsed time or solution error. Gaussian sketches only, SPD real systems, one-shot depth selection independent of the sketch, and uniform worst case over all dimensions are essential. Near the integrability boundary the variance of squared-error estimates can be very large. The eventual optimizer theorem fixes \(K\) before sending \(s\) to infinity; no uniform joint asymptotic is claimed. The primitive Student and Chebyshev statements are established literature; specialized previous treatment of their combined allocation problem cannot be excluded without independent priority review.

## References
- Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, initial preprint dated October 29, 2021, arXiv:2111.00113, https://arxiv.org/abs/2111.00113.
- D. Ahfock, W. Astle and S. Richardson, *Statistical properties of sketching algorithms*, 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC7612324/ (Theorem 1).
- V. Faber, J. Liesen and P. Tichý, *Characterization of worst-case GMRES*, arXiv:1302.5535, https://arxiv.org/abs/1302.5535.
- E. Burke, S. Güttel and K. Soodhalter, *Sketch-and-recycle GMRES*, initial 2023 preprint, arXiv:2311.14206, https://arxiv.org/abs/2311.14206.
