# Bessel-square and Gumbel crossover in random widths of complete-bipartite symmetric edge polytopes

## Finding
Let \(p,q\ge2\), \(p\le q\), and let \(P_{p,q}\) be the symmetric edge polytope of the complete bipartite graph \(K_{p,q}\), realized in the standard coordinate Euclidean metric. Put \(d=p+q-1\). For a uniform random direction \(U\) on the unit sphere of the \(d\)-dimensional sum-zero subspace, write \(W_{p,q}(U)\) for the projected width and \(D_{p,q}=\sqrt d\,W_{p,q}(U)/2\).

For \(m\ge2\) define
\[
b_m=\sqrt{2\log m}-\frac{\log\log m+\log(4\pi)}{2\sqrt{2\log m}},\qquad a_m=(2\log m)^{-1/2}.
\]
The following distributional limits and convergences of the first two moments hold.

**Fixed-side regime.** For every fixed integer \(p\ge2\), as \(q\to\infty\),
\[
D_{p,q}-b_q\ \Longrightarrow\ M_p:=\max_{1\le i\le p}|N_i|,
\]
where the \(N_i\) are independent standard normals. Thus, for \(x\ge0\), the limit CDF is \((2\Phi(x)-1)^p\), and is zero for \(x<0\).

**Two-growing-sides regime.** Suppose \(p\to\infty\), \(q\ge p\), and
\[
\sqrt{\frac{\log p}{\log q}}\longrightarrow\gamma\in[0,1].
\]
Then
\[
\frac{D_{p,q}-b_p-b_q}{a_p}\ \Longrightarrow\ Z_\gamma
:=\max\{G_1+\gamma G_2,\ G_3+\gamma G_4\},
\]
where \(G_1,G_2,G_3,G_4\) are independent standard Gumbels, with CDF \(e^{-e^{-x}}\). The two competing sums in the maximum are independent. Their exact common limit CDF is
\[
\boxed{\Pr(Z_\gamma\le x)=\left[\int_0^\infty\exp\{-s-e^{-x}s^{-\gamma}\}\,ds\right]^2.}
\]
In particular the balanced logarithmic regime \(\gamma=1\) has the Bessel-square law
\[
\Pr(Z_1\le x)=4e^{-x}K_1(2e^{-x/2})^2,
\]
where \(K_1\) is the modified Bessel function of the second kind. At the extreme-imbalance endpoint \(\gamma=0\), the CDF becomes \(e^{-2e^{-x}}\), corresponding to a standard Gumbel shifted by \(\log 2\).

**Moment consequences.** In the fixed-side regime,
\[
\operatorname{Var}(D_{p,q})\to\operatorname{Var}(M_p).
\]
In the two-growing-sides regime,
\[
\frac{\operatorname{Var}(D_{p,q})}{a_p^2}\to\operatorname{Var}(Z_\gamma).
\]
These are Euclidean spherical widths, not Gaussian widths with an unnormalized random direction. There is no claim of a uniform error rate in the growing-part ratio.

## Assumptions and scope
Partition \(\{1,\ldots,p+q\}=A\sqcup B\) with \(|A|=p\) and \(|B|=q\). Set
\[
H=\{z\in\mathbb R^{p+q}:\sum_i z_i=0\},\qquad
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in A,\ j\in B\}\subset H.
\]
All Gaussian variables below are independent standard normal unless specified otherwise. The width of a convex body in direction \(u\) is \(\max_{x\in P}\langle u,x\rangle-\min_{x\in P}\langle u,x\rangle\). The exceptional case of a fixed size-one part is not needed and is excluded. Both parts have at least two vertices, and only the explicitly stated asymptotic regimes are covered.

## Proof
**1. Exact Gaussian support reduction.** Let \(g=(g_1,\dots,g_{p+q})\) be a vector of independent standard Gaussians, and write \(\bar g=(p+q)^{-1}\sum_i g_i\). The random vector \(U=(g-\bar g\mathbf1)/\|g-\bar g\mathbf1\|\) is uniform on the intrinsic sphere in \(H\). Because every edge root is orthogonal to \(\mathbf1\), defining \(A_i=g_i\) and \(B_j=g_{p+j}\), we have the exact identity
\[
D_{p,q}=\frac{\sqrt d}{\|g-\bar g\mathbf1\|}\,R_{p,q},\quad
R_{p,q}:=\max_{i,j}|A_i-B_j|.
\]
Set \(X_A=\max_i A_i\), \(Y_A=-\min_i A_i\), and similarly \(X_B,Y_B\). Then
\[
\boxed{R_{p,q}=\max\{X_A+Y_B,\ X_B+Y_A\}.}
\]
An exact finite-dimensional CDF, obtained by conditioning on the larger part, is
\[
\Pr(R_{p,q}\le t)
=\mathbb E\left[\big(\Phi(\min_j B_j+t)-\Phi(\max_j B_j-t)\big)_+^p\right],\qquad t\ge0.
\]
This also explicitly specifies the normalization of the width statistic.

**2. Independent double extremes.** For \(m\to\infty\), the normal-tail asymptotic \(m\Pr(N>b_m+a_m x)\to e^{-x}\) holds for each fixed real \(x\). For any fixed \(x,y\), the events \(N>b_m+a_m x\) and \(N<-b_m-a_m y\) are disjoint for large \(m\). Consequently,
\[
\Pr\left(\frac{\max_{i\le m}N_i-b_m}{a_m}\le x,\ \frac{-\min_{i\le m}N_i-b_m}{a_m}\le y\right)
=\left(1-\Pr(N>b_m+a_m x)-\Pr(N<-b_m-a_m y)\right)^m
\longrightarrow e^{-e^{-x}-e^{-y}}.
\]
The upper and lower sample maxima are therefore asymptotically independent Gumbels. The two graph parts are independent from the beginning, so all four standardized upper/lower extrema converge jointly to independent Gumbels.

**3. Growing-part competition.** With both \(p,q\to\infty\), subtract \(b_p+b_q\) from both alternatives in the boxed expression for \(R_{p,q}\) and divide by \(a_p\). Their fluctuations are respectively one upper extreme from one part and one lower extreme from the other. Because \(a_q/a_p=\sqrt{\log p/\log q}\to\gamma\), joint convergence and the continuous-mapping theorem give the stated \(Z_\gamma\) limit. The two alternatives use four distinct independent limiting extrema. When \(p\) is fixed, the \(q\)-part maxima both equal \(b_q+o_{\Pr}(1)\). Therefore \(R_{p,q}-b_q\Rightarrow\max(X_A,Y_A)=M_p\), with the stated normal absolute-maximum CDF.

**4. Exact Bessel-square CDF.** Write each standard Gumbel as \(-\log E\), where \(E\) is an independent exponential variable of mean one. For \(\gamma\ge0\), conditional integration gives
\[
\Pr(G_1+\gamma G_2\le x)=\int_0^\infty e^{-s-e^{-x}s^{-\gamma}}\,ds.
\]
The two sums are independent, so their maximum has the squared CDF. When \(\gamma=1\), the standard defining integral
\[
\int_0^\infty e^{-s-z/s}\,ds=2\sqrt z\,K_1(2\sqrt z),\quad z>0,
\]
proves the displayed Bessel formula. When \(\gamma=0\), the integral equals \(e^{-e^{-x}}\).

**5. Transfer to uniform Euclidean directions and moments.** The squared norm \(\|g-\bar g\mathbf1\|^2\) has a chi-square distribution with \(d=p+q-1\) degrees of freedom. Standard chi-square concentration yields \(\sqrt d/\|g-\bar g\mathbf1\|=1+O_{\Pr}(d^{-1/2})\), and for large \(d\) its centered fourth moment is \(O(d^{-2})\). Gaussian maximal inequalities give \(\mathbb E R_{p,q}^4=O((\log(p+q))^2)\). By Cauchy--Schwarz, the squared \(L^2\) error from replacing \(D_{p,q}\) by \(R_{p,q}\) is \(O(\log(p+q)/d)\); after division by \(a_p^2\) in the growing regime it is \(O(\log(p+q)\log p/d)=o(1)\), since \(p\le q\). In the fixed-side regime the unscaled error is \(o(1)\) in \(L^2\). Standard integrable Gaussian extreme-value tail bounds, obtained from the same one-sided normal-tail estimates and the union bound, make the centered/scaled maxima uniformly square-integrable in both regimes. Therefore the distributional limits transfer from \(R_{p,q}\) to \(D_{p,q}\) with convergence of first and second moments. The variance statements follow.

## Verification
The standalone file `verify_width.py` independently constructs all \(2pq\) signed edge-root vertices, samples intrinsic Euclidean directions, and compares the directly evaluated maximum/minimum over the actual vertices against the Gaussian extreme-value reduction. It performs \(840\) exact-tolerance support/width comparisons for \(2\le p\le7\) and \(2\le q\le8\), together with five numerical tests of the Bessel integral against \(K_1\). It returns `VERIFY_OK`. These finite checks are not proofs of the limiting distributions; the analytical argument above supplies the infinite-parameter justification.

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018), particularly Proposition 3.4, describe the facet combinatorics of the same complete-bipartite symmetric edge polytopes; their Proposition 4.5 even determines the *normalized volumes of individual facets*. Both are distinct from random Euclidean directional widths. D'Alì, Delucchi and Michałek (2019) study geometric/combinatorial properties and normalized volumes of symmetric edge polytopes. Chen, Davis and Korchevskaia (2021) develop the facet-subgraph picture of this graph-polytope family.

Kabluchko, Litvak and Zaporozhets (2015, Theorem 3.7) establish Gumbel-related directional-width limits for **regular simplices and regular crosspolytopes**, including a sum-of-two-Gumbels law for simplices. The present calculation concerns a distinct graph-indexed polytope family and the maximum of **two independent sums** of Gumbels with a continuously varying relative weight. The resulting Bessel-square CDF is not the single sum-of-Gumbels distribution. The limiting-law reduction uses classical Gaussian extreme-value theory, which is not presented as original.

## Limitations
This is a self-review, not an independently audited result. The growth-ratio condition is an assumption and no uniform convergence rate is established. The source comparison covers the identified primary full texts and closely related published records; an equivalent Gaussian-array formulation elsewhere remains a bibliographic risk. No claim is made about all connected graphs or about a minimax extremality principle. The finite checker tests formulas in bounded dimensions only.

## References
- A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, first public arXiv version 2018-07-20, arXiv:1807.07678v1, particularly Propositions 3.4 and 4.5.
- A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, first public arXiv version 2019-10-11, arXiv:1910.05193v1.
- T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, first public arXiv version 2021-07-26, arXiv:2107.12315v1; primary MSC2020 includes 52B20.
- Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, first public arXiv version 2015-11-26, arXiv:1511.08479v1, Theorem 3.7.
