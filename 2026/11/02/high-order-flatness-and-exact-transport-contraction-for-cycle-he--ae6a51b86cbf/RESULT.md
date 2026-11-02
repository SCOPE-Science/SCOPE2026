# High-order flatness and exact transport contraction for cycle heat semigroups

## Finding
For every integer \(N\ge 3\), put \(C_N=\mathbb Z/N\mathbb Z\), equipped with unit-edge shortest-path distance, and let \(L\) be its combinatorial Laplacian (jump rate one along each of the two incident edges). Write \(P_t=e^{-tL}\), \(p_t(j)=P_t(0,j)\), and
\[
\mathcal C_N(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)}.
\]
Set \(r_N=\lfloor(N+1)/4\rfloor\). For **every** \(t\ge0\), the exact operator norm is
\[
\boxed{\mathcal C_N(t)=\sum_{j=0}^{N-1}|p_t(j)-p_t(r_N)|
=2\!\sum_{d(0,j)<r_N}p_t(j)-1+(N-4r_N+2)p_t(r_N).}
\]
In particular \(\mathcal C_N(0)=1\), while \(0<\mathcal C_N(t)<1\) for each \(t>0\), and \(\mathcal C_N\) is strictly decreasing on \([0,\infty)\).

There is a sharp, dimension-dependent **first nonzero time derivative**. Define
\[
 k_N=\left\lfloor\frac{N+2}{4}\right\rfloor,\qquad
 a_N=\begin{cases}2&N\equiv0\pmod4,\\1&N\equiv1\pmod4,\\4&N\equiv2\pmod4,\\3&N\equiv3\pmod4.\end{cases}
\]
Then, as \(t\downarrow0\) for each fixed \(N\),
\[
\boxed{\mathcal C_N(t)=1-\frac{a_N}{k_N!}\,t^{k_N}+O_N(t^{k_N+1}).}
\]
Thus, for \(N\ge6\), the first derivative vanishes despite strict contraction at every positive time; the number of vanishing derivatives grows without bound as the circumference increases. No uniform bound of the form \(\mathcal C_N(t)\le e^{-ct}\) for **all** \(t\ge0\) exists with \(c>0\) when \(N\ge6\), even though every cycle has a positive spectral gap.

For completeness, when \(N\ge4\), put \(\lambda_j=2-2\cos(2\pi j/N)\) and
\[
A_N=\frac2N\sum_{j=0}^{N-1}\left|\cos(2\pi j/N)-\cos(2\pi r_N/N)\right|.
\]
Then \(\mathcal C_N(t)=A_Ne^{-\lambda_1 t}+O_N(e^{-\lambda_2t})\) as \(t\to\infty\), and \(A_N\to4/\pi\) as \(N\to\infty\). For the triangle \(\mathcal C_3(t)=e^{-3t}\). For the six-cycle the full norm simplifies to \(\mathcal C_6(t)=\frac43e^{-t}-\frac13e^{-4t}=1-2t^2+O(t^3)\).

## Assumptions and scope
The vertex set is the finite cycle \(\mathbb Z/N\mathbb Z\) with \(N\ge3\). Distance is the shortest number of unit edges. The generator is exactly \((Lf)(j)=2f(j)-f(j-1)-f(j+1)\); there is **no** degree normalization or lazy-time convention. The Wasserstein distance is the ordinary distance-cost \(W_1\) between probability measures, and \(P_t\) is the symmetric stochastic semigroup. All quantifiers over \(N\) and \(t\) in the exact identity are unrestricted in those ranges; the small- and large-time \(O_N\) terms are for each fixed \(N\), not uniform in \(N\).

## Proof
**1. Reduction to neighboring starts.** On any finite metric space and for any Markov kernel \(P\), coupling each input pair and then each of their output distributions shows that the Wasserstein Lipschitz norm equals \(\max_{x\ne y}W_1(P(x,\cdot),P(y,\cdot))/d(x,y)\); equality follows by choosing point masses. When the metric is an unweighted connected graph distance, the triangle inequality along a shortest path bounds every such ratio by the maximum over adjacent vertices. Translation symmetry makes the cycle's adjacent ratios equal. Hence \(\mathcal C_N(t)=W_1(p_t,\tau p_t)\), where \((\tau p)(j)=p(j-1)\).

**2. Exact cyclic transportation.** For signed zero-total-mass \(\sigma_j\), let \(F(j)=\sum_{h=0}^j\sigma_h\). Every edge flow realizing \(\sigma\) on an oriented cycle differs from the flow \(F\) by an additive constant. Its minimal \(\ell^1\) cost, equal to the graph-distance Kantorovich–Rubinstein norm, is
\[
\|\sigma\|_{\mathrm{KR}}=\min_{c\in\mathbb R}\sum_{j=0}^{N-1}|F(j)-c|.
\]
This is the classical circular-histogram median formula, also stated by Delon, Rabin and Gousseau, Eq. (12), and is used here as a **known ingredient**. For \(\sigma_j=p_t(j)-p_t(j-1)\), telescoping yields \(F(j)=p_t(j)-p_t(N-1)\). Therefore
\[
\mathcal C_N(t)=\min_{c\in\mathbb R}\sum_j|p_t(j)-c|.
\]

**3. Heat kernel radial ordering.** Reflection symmetry implies \(p_t(j)=p_t(N-j)\). Put \(m=\lfloor N/2\rfloor\) and \(u_j(t)=p_t(j)-p_t(j+1)\), for \(0\le j<m\). Direct substitution in \(\dot p_t(j)=p_t(j-1)+p_t(j+1)-2p_t(j)\) gives the cooperative linear system
\[
\dot u_0=-3u_0+u_1,\quad
\dot u_j=u_{j-1}-2u_j+u_{j+1}\quad(1\le j<m-1),
\]
with terminal equation \(\dot u_{m-1}=u_{m-2}-3u_{m-1}\) when \(N\) is odd and \(m\ge2\), or \(\dot u_{m-1}=u_{m-2}-4u_{m-1}\) when \(N\) is even. For \(N=3\), the sole equation is \(\dot u_0=-3u_0\). Initial data are \(u_0(0)=1\) and all other \(u_j(0)=0\). Each coefficient matrix is an irreducible Metzler matrix, so \(u_j(t)>0\) for \(t>0\). Thus \(p_t(0)>p_t(1)>\cdots>p_t(m)\) for all positive times.

**4. Locate the median and evaluate.** Distance shell zero has one vertex, intermediate shells have two, and the antipodal shell for even \(N\) has one. Counting these shells shows \(p_t(r_N)\) is a median of all \(N\) kernel entries; when \(N\equiv2\pmod4\) the median interval may also contain \(p_t(r_N+1)\). The median property minimizes the sum in step 2 and gives the first boxed identity. For the second, precisely \(2r_N-1\) vertices satisfy \(d(0,j)<r_N\); subtract the total kernel mass one. The \(t=0\) identity follows by continuity.

**5. Sharp short-time order.** The exact first identity rearranges as
\[
1-\mathcal C_N(t)
=(4r_N+2-N)p_t(r_N)
+4\sum_{j=r_N+1}^{\lfloor (N-1)/2\rfloor}p_t(j)
+2\mathbf1_{\{N\ \mathrm{even}\}}p_t(N/2).
\]
All coefficients and terms in this expression are nonnegative. The coefficient \(4r_N+2-N\) equals \(2,1,0,3\) for \(N\equiv0,1,2,3\pmod4\), respectively. The kernel has Taylor expansion \(p_t(d)=t^d/d!+O_N(t^{d+1})\) for each \(1\le d\le N/2\) (at an even antipode there are two shortest paths, but that term has strictly higher order than the first nonzero term here). This expansion follows from the matrix exponential and the minimum number of graph jumps. When the first coefficient vanishes (\(N\equiv2\pmod4\)), the next distance shell contributes \(4t^{r_N+1}/(r_N+1)!\); otherwise the term at distance \(r_N\) is leading. These cases yield precisely \(k_N\) and \(a_N\) above, including \(N=3,4\). The positive defect proves \(\mathcal C_N(t)<1\) for all positive times; positivity follows from distinct neighboring heat kernels. By the semigroup property and submultiplicativity, \(\mathcal C_N(s+t)\le\mathcal C_N(s)\mathcal C_N(t)<\mathcal C_N(s)\) for \(s\ge0,t>0\).

**6. Long-time decay.** The discrete Fourier expansion is
\[
p_t(j)=\frac1N\sum_{h=0}^{N-1}e^{-\lambda_h t}\cos(2\pi hj/N).
\]
For \(N\ge4\) the first nonconstant eigenspace is spanned by the conjugate frequencies \(1,N-1\), and the next eigenvalue is \(\lambda_2>\lambda_1\). Substituting into the absolute-value formula gives the stated \(A_N\) and error estimate, since absolute value is 1-Lipschitz. A Riemann-sum limit proves \(A_N\to(2/2\pi)\int_0^{2\pi}|\cos\theta|\,d\theta=4/\pi\). The \(N=3\) kernel gives the separate identity.

## Verification
The companion `checker.py` constructs \(e^{-tL}\) by matrix exponentiation and checks the theorem's predicted Wasserstein cost against a **separate Kantorovich dual linear program** for 28 cycle sizes and five positive times (140 comparisons, numerical tolerance \(3\times10^{-6}\)). It also checks 589 exact-integer Taylor coefficient identities across \(N=3,\ldots,64\), and verifies several long-time prefactors. The checker uses NumPy and SciPy; run `python checker.py`. These finite calculations support the independently supplied all-size mathematical proof; finite sampling alone would not establish the theorem.

## Relationship to prior work
The median formula for circular \(W_1\) transport is **previously known**, including Eq. (12) of Delon–Rabin–Gousseau, *Transportation Distances on the Circle and Applications* (arXiv:0906.5499), and is not a novelty claim. Münch–Wojciechowski (first posted 2017-12-04, arXiv:1712.00875v1) prove a semigroup/curvature equivalence governing exponential Lipschitz contraction, but their semigroup characterization does not determine this finite-cycle all-time norm or its first nonzero high-order Taylor coefficient. Pedrotti (arXiv:2308.00516v1) develops general coupling estimates for Wasserstein semigroup contraction, but the checked relevant sections do not provide the exact cycle size-dependent order. The new quantitative statement is the **sharp high-order flatness law and its explicit coefficient**, together with the direct all-time heat-profile specialization, not the general circular median identity or the general curvature criterion.

## Limitations
Only finite unweighted simple cycles, the unnormalized generator with rate one per edge, and ordinary \(W_1\) are treated. The leading asymptotics are pointwise in fixed cycle size. The claim does not address weighted cycles, higher Wasserstein exponents, or uniform-in-size heat-kernel scaling. Older literature on diffusion coupling around finite circles might contain an equivalent time-derivative calculation; this priority risk has not been independently resolved. Independent mathematical audit is not claimed.

## References
- F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875v1 (2017-12-04), https://arxiv.org/abs/1712.00875.
- F. Pedrotti, *Contractive coupling rates and curvature lower bounds for Markov chains*, arXiv:2308.00516v1 (2023-08-01), https://arxiv.org/abs/2308.00516.
- J. Delon, J. Rabin, and Y. Gousseau, *Transportation Distances on the Circle and Applications*, arXiv:0906.5499, especially Eq. (12), https://arxiv.org/abs/0906.5499.
- J. Delon, J. Salomon, and A. Sobolevski, *Fast transport optimization for Monge costs on the circle*, arXiv:0902.3527, https://arxiv.org/abs/0902.3527.
