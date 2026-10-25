# Log-log imbalance crossover for Gaussian widths of complete-bipartite graph associahedra

## Finding

Let \(p_n\le q_n\), \(p_n\to\infty\), and \(n=p_n+q_n\to\infty\). For the standard unit-weight graph associahedron \(P_{p,q}\) of the complete bipartite graph \(K_{p,q}\), let \(W_{p,q}\) denote its Euclidean directional width in a uniform unit vector in the intrinsic linear space \(\mathbf1^\perp\). Put \(b_n=\Phi^{-1}(1-1/n)\), where \(\Phi\) is the standard normal distribution function. Let \(E_r^+,E_r^-\) be mutually independent unit-mean exponential random variables, \(\Gamma_r^\pm=\sum_{j=1}^rE_j^\pm\), and define the almost surely convergent series
\[
\Xi_\pm=-\sum_{r=1}^{\infty}2^{-r}\log\Gamma_r^\pm,\qquad T=\Xi_++\Xi_-.
\]
Then
\[
b_n\left(\frac{\sqrt{n-1}}{2^n}W_{p_n,q_n}-2(1-2^{-p_n})b_n\right)\ \Longrightarrow\ T.
\]
The law \(T\) is non-Gaussian, with
\[
\mathbb E T=2(\gamma-\log2),\qquad
\operatorname{Var}T=2\bigl(\pi^2/6-2\operatorname{Li}_2(1/2)+\operatorname{Li}_2(1/4)\bigr).
\]
If additionally \(\lambda_n=(\log n)/2^{p_n}\to\lambda\in[0,\infty)\), then
\[
b_n\left(\frac{\sqrt{n-1}}{2^n}W_{p_n,q_n}-2b_n\right)\Longrightarrow T-4\lambda.
\]
If \(\lambda_n\to\infty\), this last expression tends to \(-\infty\) in probability. The sharp transition therefore lies at a smaller bipartition size of order \(\log_2\log n\).

## Assumptions and scope

For every nonempty vertex subset \(S\) of \(K_{p,q}\) inducing a connected subgraph, set \(\Delta_S=\operatorname{conv}\{e_i:i\in S\}\). The **standard unweighted graph associahedron** here means precisely \(P_{p,q}=\sum_{S\text{ connected}}\Delta_S\), with no additional scale factors. The direction is Haar-uniform on the sphere in \(\mathbf1^\perp\subset\mathbb R^n\), dimension \(n-1\). A singleton simplex has width zero. The theorem holds for every integer sequence \(1\le p_n\le q_n\) with \(p_n\to\infty\), and makes no assertion for fixed smaller-part size. All logarithms are natural, except the explicitly indicated base-two threshold.

## Proof

**1. Exact finite directional-support decomposition.** Write \(z_{(1)}\ge\cdots\ge z_{(m)}\) for descending order statistics of an \(m\)-coordinate vector. Each nonempty simplex \(\Delta_S\) has width \(\max_{i\in S}z_i-\min_{i\in S}z_i\), so, by counting each subset having a given maximum or minimum,
\[
H_m(z):=2^{-m}\sum_{\varnothing\ne S\subseteq[m]}\bigl(\max_{i\in S}z_i-\min_{i\in S}z_i\bigr)
=\sum_{r=1}^m2^{-r}(z_{(r)}-z_{(m+1-r)}).
\]
A nonempty induced subgraph of \(K_{p,q}\) is connected exactly when it is a singleton or its subset meets both vertex classes. Subtracting the widths of subsets supported entirely in each class gives the **exact identity**
\[
2^{-n}\operatorname{width}_{P_{p,q}}(z)
=H_n(z)-2^{-p}H_q(z_B)-2^{-q}H_p(z_A).
\tag{1}
\]
This identity is independent of ties and holds for every real vector.

**2. Gaussian spherical representation.** Let \(G=(G_1,\ldots,G_n)\) have independent standard Gaussian coordinates, \(\bar G=n^{-1}\sum_iG_i\), and \(R=\|G-\bar G\mathbf1\|\). Then \(U=(G-\bar G\mathbf1)/R\) is Haar-uniform in the intrinsic sphere and \(R^2\sim\chi^2_{n-1}\). Every width in (1) is translation-invariant and homogeneous. Hence
\[
\frac{\sqrt{n-1}}{2^n}W_{p,q}(U)
=\frac{\sqrt{n-1}}R\bigl(H_n(G)-2^{-p}H_q(G_B)-2^{-q}H_p(G_A)\bigr).
\tag{2}
\]
Since \(\sqrt{n-1}/R=1+O_{\mathbb P}(n^{-1/2})\), it is enough to analyze the rightmost bracket to fluctuations of order \(1/b_n\). The bracket is \(O_{\mathbb P}(b_n)\); therefore the radial correction, multiplied by \(b_n\), is \(O_{\mathbb P}(\log n/\sqrt n)=o_{\mathbb P}(1)\).

**3. Extremal weighted order-statistic limit.** Set \(b_m=\Phi^{-1}(1-1/m)\), so \(b_m^2\sim2\log m\). The normal tail ratio \(m[1-\Phi(b_m+x/b_m)]\to e^{-x}\) implies joint convergence of any fixed number of upper and lower Gaussian extremes to independent Poisson point processes on \(\mathbb R\) with intensity \(e^{-x}dx\). Their respective decreasing order statistics are \(-\log\Gamma_r^+\) and \(-\log\Gamma_r^-\). Thus, for every fixed cutoff \(K\), the first \(K\) summands in
\[
b_m(H_m(G)-2b_m)
=\sum_{r=1}^m2^{-r}\bigl[b_m(G_{(r)}-b_m)+b_m(-G_{(m+1-r)}-b_m)\bigr]-2^{1-m}b_m^2
\]
converge jointly to the corresponding truncated series defining \(T\). The displayed (negative) final term tends to zero.

The infinite series truncation is legitimate, **not merely a finite-experiment inference**. For \(r\le m/4\), the random variable \(V_r=1-\Phi(G_{(r)})\) has the \(\operatorname{Beta}(r,m-r+1)\) law. On \(V_r\le1/2\), Gaussian Mills-hazard monotonicity and the lower bound \(\phi(x)/(1-\Phi(x))\ge x\) for \(x\ge0\) show
\[
|b_m(G_{(r)}-b_m)|\le2|\log(mV_r)|.
\]
The beta-binomial identity gives \(\Pr(mV_r<e^{-t})\le e^{-t}\) for \(t\ge0\). Jensen's inequality gives \(\mathbb E\log(mV_r)\le\log r\), hence \(\mathbb E|\log(mV_r)|\le\log r+2\). The exceptional event \(V_r>1/2\) has exponentially small probability uniformly for \(r\le m/4\); its expectation contribution is negligible by Cauchy--Schwarz and the standard \(O(\sqrt{\log m})\) expected Gaussian maximum bound. For \(r>m/4\), the geometric weights make the entire remaining contribution \(O(m\,2^{-m/4}\log m)\). Identical estimates hold for lower extremes. Therefore the expected absolute truncated tail is bounded, asymptotically, by \(C\sum_{r>K}2^{-r}(1+\log r)\to0\). This proves convergence to \(T\) and uniform integrability for the first moments.

**4. Removing the smaller side.** Because \(q\ge n/2\), the normal quantile comparison yields \(b_q/b_n\to1\) and \(b_n(b_q-b_n)=O(1)\). Step 3 applied to the independent \(q\)-coordinate sample gives \(H_q(G_B)=2b_q+O_{\mathbb P}(1/b_q)\). Thus
\[
2^{-p}b_n(H_q(G_B)-2b_n)=o_{\mathbb P}(1)
\]
when \(p\to\infty\). Also \(2^{-q}b_nH_p(G_A)=o_{\mathbb P}(1)\) since \(H_p=O_{\mathbb P}(b_p)\) and \(q\ge n/2\). Inserting into (1)--(2) yields the primary limit.

**5. The sharp transition.** Replacing \(2(1-2^{-p})b_n\) by \(2b_n\) subtracts exactly \(2^{1-p}b_n^2\) on the \(b_n\)-scale. Since \(b_n^2\sim2\log n\), this deterministic difference tends to \(4\lambda\) when \((\log n)/2^p\to\lambda\), and diverges positively when that ratio tends to infinity. The centered limit from step 4 remains tight, proving both statements.

**6. Moments and non-Gaussianity.** For integer \(r\ge1\), the gamma-log identities give \(\mathbb E\log\Gamma_r=H_{r-1}-\gamma\) and \(\operatorname{Cov}(\log\Gamma_r,\log\Gamma_s)=\psi_1(\max\{r,s\})\), where \(H_{r-1}\) is harmonic and \(\psi_1\) is the trigamma function. Consequently \(\mathbb E\Xi=\gamma-\log2\). Summing the geometric covariance array and using
\[
\sum_{m\ge1}x^m\psi_1(m)=\frac{x}{1-x}\bigl(\pi^2/6-\operatorname{Li}_2(x)\bigr)
\]
proves the stated variance formula, with two independent copies. For non-Gaussianity, condition on the exponential increments after the first: there is an almost surely finite random variable \(C\), independent of \(E_1^+\), such that for \(E_1^+\le1\), \(\Xi_+\ge-\tfrac12\log E_1^+-C\). Choose finite \(K\) with positive probability that \(C\le K\) and \(\Xi_-\ge-K\). Independence then gives \(\Pr(T>t)\ge c\exp(-2t)\) for all sufficiently large \(t\), impossible for any Gaussian distribution. This completes the proof.

## Verification

A standalone Python checker exhaustively constructs all connected induced subsets in dimensions \(2\) through \(8\), compares support widths with formula (1) for \(520\) sampled vectors, and evaluates the two exact Poisson-series moments against \(60{,}000\) independent exponential-series samples (truncation \(38\)). Expected output includes `EXACT_SUPPORT_PASS` and `POISSON_MOMENT_PASS`. These checks verify finite identities and moment numerics; the infinite-dimensional distributional assertions follow from the proof, not the simulations.

## Relationship to prior work

Graph associahedra and generalized permutahedra are standard Minkowski sums of coordinate simplices. Jochemko and Ravichandran (arXiv:1909.08448) study Minkowski linear functionals, Ehrhart positivity and lattice-point geometry rather than random-direction widths. Cardinal, Pournin and Valencia-Pabon (arXiv:2106.16130) establish combinatorial diameter estimates for graph associahedra, including complete bipartite graph families; these neither state nor imply this weighted Poisson width limit. Existing stellohedron calculations concern fixed one-vertex bipartition and are not within the growth hypothesis \(p_n\to\infty\). The exact finite identity is related to classical Gaussian order-statistic decompositions; the asserted novelty is the geometric double scaling with a log-log part-size crossover, not the standalone Poisson limit of Gaussian maxima.

## Limitations

The theorem is restricted to the specified unit-weight Minkowski-sum realization, isotropic intrinsic Euclidean directions, and both bipartition sizes tending to infinity. It does not imply identical behavior for affinely equivalent realizations or fixed smaller class sizes. The limiting law is characterized by a convergent exponential series; no elementary closed-form distribution function is claimed. Comparisons with less-indexed or inaccessible literature may still reveal priority overlap. Independent mathematical validation has not been performed.

## References

1. K. Jochemko and M. Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, arXiv:1909.08448, first posted 2019-09-18, journal version 2022. https://arxiv.org/abs/1909.08448
2. J. Cardinal, L. Pournin and M. Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first posted 2021-06-30. https://arxiv.org/abs/2106.16130
3. S. Forcey and M. Ronco, *Algebraic structures on graph associahedra*, arXiv:1910.00670, first posted 2019-10-01. https://arxiv.org/abs/1910.00670
