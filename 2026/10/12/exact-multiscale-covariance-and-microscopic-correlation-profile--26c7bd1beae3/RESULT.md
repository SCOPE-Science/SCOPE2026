# Exact multiscale covariance and microscopic correlation profile for circular number variance

## Finding
Let \(U_1,\ldots,U_N\) be independent uniform points on the circle \(\mathbb T=\mathbb R/\mathbb Z\), with integer \(N\ge2\). For \(0<s<1\), set
\[
C_N(x,s)=\sum_{i=1}^N {\bf1}\{U_i\in(x,x+s]\pmod1\},\qquad
V_N(s)=\int_0^1(C_N(x,s)-Ns)^2\,dx.
\]
For arbitrary \(s,t\in(0,1)\), let \(r_s=\min(s,1-s)\), \(r_t=\min(t,1-t)\), \(a=\min(r_s,r_t)\), and \(b=\max(r_s,r_t)\). Then
\[
\boxed{\operatorname{Cov}(V_N(s),V_N(t))=2N(N-1)\left[a^2b(1-b)-\frac{a^3}{3}\right].}
\]
Every off-diagonal covariance is strictly positive. More strongly, for any integer \(m\ge1\) and any \(m\) pairwise distinct lengths \(s_1,\ldots,s_m\in(0,1/2]\), their \(m\times m\) covariance matrix is strictly positive definite. Thus two lengths in \((0,1)\) have correlation exactly one if and only if their reduced lengths \(r_s\) and \(r_t\) coincide, i.e. \(t=s\) or \(t=1-s\); all other correlations are strictly between zero and one.

The Pearson correlation is independent of \(N\) and equals
\[
\rho(a,b)=\frac{a^2b(1-b)-a^3/3}{\sqrt{(2a^3/3-a^4)(2b^3/3-b^4)}}.
\]
For every fixed \(q\in(0,1]\), as \(b\downarrow0\) with \(a=qb\), it converges to the universal profile
\[
\boxed{\lim_{b\downarrow0}\rho(qb,b)=\frac{3\sqrt q-q^{3/2}}2.}
\]
In particular the correlation tends to zero when both lengths shrink and their ratio tends to zero, and in that case \(\rho(a,b)\sim\frac32\sqrt{a/b}\).

## Assumptions and scope
The arc endpoints are immaterial because the uniform law is nonatomic. Random points are independent and uniform on \(\mathbb T\), and \(N\ge2\) is deterministic. All identities hold for *every* real \(s,t\in(0,1)\), not only rational lengths, and for *every* finite collection of pairwise distinct reduced lengths. The covariance uses the randomness of the sampled configuration, while each \(V_N(s)\) includes an exact integral over arc translation.

## Proof
**1. Complement symmetry.** The complement of an arc of length \(s\) is an arc of length \(1-s\). Reversing the endpoint and translating the integration variable gives \(V_N(1-s)=V_N(s)\) for each realization. Therefore it suffices to work with \(s,t\in(0,1/2]\).

**2. Canonical pair kernel.** Put \(d(u)=\min(\{u\},1-\{u\})\) and
\[
K_s(u)=(s-d(u))_+-s^2,\qquad 0<s\le1/2.
\]
Two intervals of length \(s\) positioned at points distance \(d(u)\) have overlap length \((s-d(u))_+\). Expanding the defining square therefore yields, identically for each sample,
\[
V_N(s)=Ns(1-s)+2\sum_{1\le i<j\le N}K_s(U_i-U_j).
\]
The kernel is canonical: for each fixed \(u\), \(\int_0^1K_s(u-v)\,dv=0\), because the integral of the overlap triangle is \(s^2\). The summands corresponding to distinct unordered pairs are consequently uncorrelated: disjoint pairs are independent, while pairs sharing one index have covariance zero after conditioning on that common point.

**3. Exact cross-scale moment.** Let \(0<s\le t\le1/2\). The preceding orthogonality gives
\[
\operatorname{Cov}(V_N(s),V_N(t))=4\binom N2\int_0^1K_s(u)K_t(u)\,du.
\]
Since \(\int_0^1(s-d(u))_+\,du=s^2\) and similarly for \(t\), symmetry around zero shows
\[
\begin{aligned}
\int_0^1K_s(u)K_t(u)\,du
&=2\int_0^s(s-v)(t-v)\,dv-s^2t^2\\
&=s^2t(1-t)-s^3/3.
\end{aligned}
\]
This proves the claimed formula, including all equality boundaries \(s=t\) and \(t=1/2\). The integral is strictly positive because \(t(1-t)\ge t/2\ge s/2\), giving \(s^2t(1-t)-s^3/3\ge s^3/6>0\). Setting \(s=t\) yields \(\operatorname{Var}(V_N(s))=2N(N-1)(2s^3/3-s^4)>0\).

**4. Strict positive definiteness.** For any real coefficients \(c_1,\ldots,c_m\), the variance of \(\sum_j c_jV_N(s_j)\) is the positive factor \(4\binom N2\) times the squared \(L^2(\mathbb T)\)-norm of \(\sum_jc_j K_{s_j}\). Sort the distinct widths \(0<s_1<\cdots<s_m\le1/2\). On the interval \((s_{m-1},s_m)\), with \(s_0=0\), the restrictions of \(K_{s_j}\) to \(u\in[0,1/2]\) have derivative zero for \(j<m\), while \(K_{s_m}\) has derivative \(-1\). Thus if their linear combination were zero almost everywhere, its derivative there would force \(c_m=0\). Descend inductively to get every \(c_j=0\). Therefore the covariance matrix is strictly positive definite. The two-variable strict Cauchy–Schwarz inequality yields the claimed exact criterion for correlation one; complement symmetry provides the equality cases.

**5. Correlation profile.** Divide the cross-covariance formula by the product of the positive standard deviations. On setting \(a=qb\) and letting \(b\downarrow0\), cancel the common factor \(b^3\), giving \(\frac32\sqrt q(1-q/3)\), the stated profile. If \(a/b\to0\) and \(b\to0\), the same expression and its uniform polynomial remainder yield \(\rho(a,b)\sim(3/2)\sqrt{a/b}\). No probabilistic limit theorem is used in this last step.

## Verification
A self-contained exact-rational checker, `check_multiscale.py`, independently integrates the piecewise quadratic product \(K_sK_t\) with Simpson quadrature (exact for quadratics), compares it against the closed expression on all \(64\) pairs in an eight-point rational grid, verifies samplewise pair-kernel representations and complement symmetry for configurations of sizes \(2\) through \(6\), and checks one five-scale covariance matrix by exact \(LDL^{\mathsf T}\) factorization. It passes \(341\) assertions. These tests are diagnostics; the preceding continuous proof establishes the all-real, all-\(N\) theorem.

## Relationship to prior work
Bramati, Brandolini, and Monguzzi study translated and dilated discrepancy tests on the torus, motivating comparison across geometric scales [1]. Aistleitner, Hörmann, and Manskova establish the one-window mean and variance for circular number variance and analyze its asymptotic *marginal* distribution [2, equation (17)]. Their variance formula is exactly the diagonal case of the formula above and is **not** claimed as new. The new statement supplies the complete finite-sample *off-diagonal* covariance kernel, full-rank multiscale covariance, and the microscopic correlation profile. A classical degenerate U-statistic calculation explains the orthogonality, but marginal moments alone do not specify these joint statistics.

## Limitations
The claim concerns covariances, not the full joint distribution or independence of the statistics. It applies to independent *uniform* circular points; nonuniform samples and higher-dimensional averaging sets may have different covariance kernels. The 2026 multi-dimensional discrepancy study [1] was accessible at the abstract level but its complete text was unavailable for detailed priority comparison; an equivalent earlier formulation of the multiscale kernel remains a residual risk. The 2026 circular-number-variance preprint [2] was read in relevant sections; no off-diagonal covariance identity or positive-definiteness classification was identified there. Independent external scientific validation has not been performed.

## References
[1] R. Bramati, L. Brandolini, A. Monguzzi, *Discrepancy estimates for multi-dimensional non-smooth convex bodies: a case study*, arXiv:2606.07028v1 (first public 5 June 2026). https://arxiv.org/abs/2606.07028

[2] C. Aistleitner, S. Hörmann, M. Manskova, *On the asymptotic behavior of the number variance of random points on the unit torus*, arXiv:2610.11687v1 (8 October 2026), especially equations (16)–(18) and Section 3. https://arxiv.org/html/2610.11687v1
