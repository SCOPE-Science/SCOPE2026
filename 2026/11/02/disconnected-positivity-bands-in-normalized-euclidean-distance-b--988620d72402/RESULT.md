# Disconnected positivity bands in normalized Euclidean-distance Bergman kernels

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1}\). For real \(t>-1\), write \(K_t\) for the holomorphic reproducing kernel associated with the unnormalized-area norm
\[
\|f\|_t^2=\int_{\mathbb D}|f(z)|^2(1-|z|)^t\,dA(z).
\]
The **origin-normalized kernel** is \(\mathcal B_t(z,w)=K_t(z,w)/K_t(0,0)\). It admits the unique extension, entire in the complex parameter \(t\) for each pair \(z,w\in\mathbb D\),
\[
\mathcal B_t(z,w)=\sum_{n=0}^\infty\frac{(t+3)_{2n}}{(2n+1)!}(z\overline w)^n
={}_2F_1\!\left(\frac{t+3}2,\frac{t+4}2;\frac32;z\overline w\right).
\]
Here \((a)_0=1\) and \((a)_m=a(a+1)\cdots(a+m-1)\) for positive integers \(m\). Its **complete real positivity set** is
\[
\boxed{\mathcal W=[-3,\infty)\cup\bigcup_{j=2}^\infty[-(2j+1),-2j].}
\]
For \(t\in\mathcal W\), \(\mathcal B_t\) is a Hermitian positive-semidefinite kernel on \(\mathbb D\); outside this set it is not. In the open intervals of \(\mathcal W\), every Taylor coefficient is strictly positive, so the kernel is strictly positive definite on every set of pairwise distinct disk points and its reproducing-kernel Hilbert space has infinite dimension. At \(t=-k\) with an integer \(k\ge3\), the kernel instead is a polynomial of **exact rank**
\[
\boxed{\operatorname{rank}\mathcal B_{-k}=\left\lfloor\frac{k-1}2\right\rfloor.}
\]
These are the only finite-rank parameters in \(\mathcal W\). In particular, \(\mathcal B_{-3}=\mathcal B_{-4}=1\), \(\mathcal B_{-5}(z,w)=1+z\overline w/3\), while \(\mathcal B_{-1}(z,w)=(1-z\overline w)^{-1}\) and \(\mathcal B_{-2}(z,w)=\operatorname{arctanh}\sqrt{z\overline w}/\sqrt{z\overline w}\), with the removable value at zero. The two latter kernels have infinite rank.

## Assumptions and scope
The disk is one complex dimensional. The boundary distance is exactly \(1-|z|\), **not** the more customary smooth defining function \(1-|z|^2\). The integration measure for \(K_t\) is ordinary, unnormalized planar Lebesgue area; the normalization is by the strictly positive scalar \(K_t(0,0)\) only for \(t>-1\). Analytic continuation is performed on the **normalized kernel** as a function of \(t\), not by interpreting \((1-|z|)^t\,dA\) as an integrable weight when \(t\le-1\). At negative parameters, positive semidefiniteness has its usual kernel-theoretic meaning: every finite Gram matrix \((\mathcal B_t(z_i,z_j))_{i,j}\) is positive semidefinite. Here strict positive definiteness means positive definite for every finite tuple of pairwise distinct points, while rank is the dimension of the span of all kernel sections.

## Proof
**1. Identification and entire extension.** For \(t>-1\), circular orthogonality and the beta integral give
\[
\|z^n\|_t^2=2\pi\int_0^1 r^{2n+1}(1-r)^t\,dr
=\frac{2\pi\Gamma(2n+2)\Gamma(t+1)}{\Gamma(2n+t+3)}.
\]
The monomials form a complete orthogonal basis by angular Parseval and Tonelli. Hence
\[
K_t(z,w)=\sum_{n\ge0}\frac{\Gamma(2n+t+3)}{2\pi\Gamma(2n+2)\Gamma(t+1)}(z\overline w)^n,
\qquad K_t(0,0)=\frac{(t+1)(t+2)}{2\pi}.
\]
Dividing yields \(d_n(t)=(t+3)_{2n}/(2n+1)!\). The duplication formula for rising factorials yields the hypergeometric expression in the finding. For every compact parameter set \(T\subset\mathbb C\), the bound
\[
|d_n(t)|\le\frac1{2n+1}\prod_{j=1}^{2n}\left(1+\frac{\max_{t\in T}|t+2|}j\right)
=O_T((n+1)^{C_T})
\]
holds uniformly on \(T\), for some \(C_T\). Therefore the disk power series converges locally normally in both \(t\) and \(z\overline w\), proving existence and uniqueness of an entire continuation in \(t\).

**2. Positivity is precisely coefficient positivity.** If all \(d_n(t)\ge0\), then for arbitrary disk points \(z_1,\ldots,z_m\) and scalars \(c_1,\ldots,c_m\), absolute convergence gives
\[
\sum_{i,j=1}^m c_i\overline{c_j}\,\mathcal B_t(z_i,z_j)
=\sum_{n\ge0}d_n(t)\left|\sum_{i=1}^m c_i z_i^n\right|^2\ge0.
\]
Conversely, if \(\mathcal B_t\) is positive semidefinite, integrate its Gram quadratic form against the Fourier mode of order \(n\) on any circle of radius \(0<r<1\):
\[
\int_0^{2\pi}\!\int_0^{2\pi}
\mathcal B_t(re^{i\theta},re^{i\phi})
 e^{-in\theta}e^{in\phi}\,d\theta\,d\phi
=(2\pi)^2d_n(t)r^{2n}\ge0.
\]
Positive-semidefinite finite Gram forms imply nonnegative integrated forms by Riemann-sum approximation; therefore every coefficient is nonnegative. If every coefficient is **positive**, then equality in the displayed Gram form forces \(\sum_i c_i z_i^n=0\) for \(0\le n<m\). The Vandermonde determinant at distinct \(z_i\) is nonzero, hence all \(c_i=0\), giving strict positive definiteness and infinite rank.

**3. Complete sign classification.** For \(t>-3\), each factor in \((t+3)_{2n}\) is strictly positive, so every \(d_n(t)>0\). At \(t=-3\), all coefficients except \(d_0=1\) vanish. If \(t<-3\) is nonintegral, exactly
\[
q=\lceil-t-3\rceil
\]
of the consecutive real factors \(t+3,t+4,\ldots\) are negative. If \(q\) is even, the even prefix of any length \(2n\) contains an even number of negative factors, hence \(d_n(t)>0\) for every \(n\). If \(q\) is odd, taking \(n=(q+1)/2\) includes precisely \(q\) negative factors and at least one positive factor, so \(d_n(t)<0\) and positive semidefiniteness fails. The even-\(q\) regions are exactly \((-(2j+1),-2j)\) for \(j\ge2\); the odd-\(q\) regions are the interposed open gaps.

**4. Integer endpoints and exact rank.** At \(t=-k\), integer \(k\ge3\), the first zero factor in \((t+3)_{2n}\) occurs exactly when \(2n\ge k-2\). For \(2n\le k-3\), all \(2n\) factors are negative, so their product is positive. Consequently the nonzero coefficients have precisely indices
\[
0\le n\le\left\lfloor\frac{k-3}2\right\rfloor,
\]
and their number is \(\lfloor(k-1)/2\rfloor\). This is also the Gram rank because the corresponding monomials are linearly independent. The endpoints \(t=-1,-2\) belong to the full-rank interval \((-3,\infty)\), with the series values stated in the finding. This exhausts all real parameters and proves all conclusions.

## Verification
The standalone pure-Python checker `kernel_check.py` recomputes exact rational coefficients and verifies the first coefficients at selected positive, negative-integer, positivity-band and excluded-gap parameters. The script also confirms the finite rank and the Hardy/elementary specializations. These calculations only cross-check identities: positivity for all real parameters and all Gram matrix sizes follows from the analytical Fourier and sign proof, not from finite testing.

## Relationship to prior work
Marinescu--Xing (2026) prove parameter analyticity for Euclidean boundary-distance weighted Bergman kernels on smooth pseudoconvex domains in the original integral range \(t>-1\). Their theorem does not classify analytically continued positive-definite kernels for negative parameters. Engliš (2010) proves general meromorphic continuation for smooth defining functions and gives the classical disk formula for \(1-|z|^2\), but not the above disconnected positivity set for \(1-|z|\). A publicly available exact disk computation, *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (2026), gives the same unnormalized coefficient formula and an exact **zero** classification in the original range \(t>-1\), not a positivity classification for normalized continuation across \(t=-1,-2\). Moravík (2026) studies disconnected Wallach phenomena for Möbius-invariant **\(H\)-harmonic**, rather than holomorphic, Bergman spaces with a different weight. The present result concerns a distinct holomorphic family and characterizes all real parameters and ranks. Positivity here is **normalization-sensitive**: its statement does not transfer without adjustment to the unnormalized continuation, which vanishes identically at \(t=-1,-2\).

## Limitations
No analytically continued kernel at \(t\le-1\) is claimed to arise from the original positive weighted-area integral; the continued family is defined by its holomorphic power series. The result is for the Euclidean-distance weight on the one-dimensional unit disk and normalization at the origin; arbitrary defining functions, domains and normalizations may have different positivity sets. Existing general hypergeometric positivity literature might implicitly include the coefficient-sign phenomenon under another parametrization; such overlap cannot be fully excluded without a broader expert bibliography review. The present proof does not treat nonreal parameter kernel positivity, a notion outside the Hermitian setting.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1 (first public September 21, 2026), https://arxiv.org/html/2609.24258.
2. M. Engliš, *Analytic Continuation of Weighted Bergman Kernels*, ESI Preprint 2263 (September 7, 2010), https://www.esi.ac.at/preprints/esi2263.pdf.
3. M. Moravík, *Analytic continuation of weighted H-harmonic Bergman spaces*, arXiv:2606.19810v1 (June 18, 2026), https://arxiv.org/html/2606.19810v1.
4. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (2026), public scientific result, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0/RESULT.md.
