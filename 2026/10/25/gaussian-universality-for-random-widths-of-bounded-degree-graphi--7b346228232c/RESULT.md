# Gaussian universality for random widths of bounded-degree graphical zonotopes

## Finding
Let \(G_n\) be any sequence of finite, connected, simple graphs with \(n\to\infty\) vertices and uniformly bounded maximum degree. Put \(m_n=|E(G_n)|\) and \(t_n=\sum_v\binom{\deg(v)}2\), the number of unordered incident-edge pairs. Suppose the two limits
\[
\alpha=\lim_{n\to\infty}\frac{m_n}{n},\qquad
\tau=\lim_{n\to\infty}\frac{t_n}{n}
\]
exist. In the standard Euclidean metric of \(\mathbf1^\perp\), form the centered graphical zonotope
\[
Z(G_n)=\sum_{\{i,j\}\in E(G_n)}[-(e_i-e_j)/2,(e_i-e_j)/2].
\]
For \(U_n\) Haar-uniform on the unit sphere of \(\mathbf1^\perp\), let \(W_n=h_{Z(G_n)}(U_n)+h_{Z(G_n)}(-U_n)\) be its directional width. Define
\[
\mu=\frac2{\sqrt\pi},\quad
v=2-\frac4\pi,\quad
\kappa=\frac13+\frac{2\sqrt3-4}{\pi},\quad
s^2=\alpha v+2\tau\kappa-\frac{2\alpha^2}{\pi}.
\]
Then \(s^2>0\) and
\[
\boxed{\ W_n-\frac{\mu m_n}{\sqrt n}\ \Longrightarrow\ N(0,s^2).\ }
\]
The same conclusion holds on replacing \(\mu m_n/\sqrt n\) by the **exact** spherical mean
\[
\mathbb EW_n=m_n\sqrt{\frac2\pi}\,
\frac{\Gamma((n-1)/2)}{\Gamma(n/2)}.
\]
In particular, the limiting distribution only depends on two local graph counts, the edge density \(\alpha\) and incident-edge-pair density \(\tau\); triangles and higher motifs do not enter the limiting law, despite their relevance to finite higher width moments. For paths and cycles, the limiting variance is
\[
\frac83+\frac{4\sqrt3-14}{\pi},
\]
whereas for any fixed-degree \(d\ge2\) connected \(d\)-regular graph sequence it is
\[
\frac d2\left(2-\frac4\pi\right)
+d(d-1)\kappa-\frac{d^2}{2\pi}.
\]
These are consequences of the same single asymptotic width theorem, not independent classifications.

## Assumptions and scope
All graphs are unweighted, undirected, simple and connected, and each \(G_n\) has vertex set of size \(n\). The graph sequence is deterministic. A fixed degree bound, independent of \(n\), is essential to the dependency-graph proof. The intrinsic scalar product on \(\mathbf1^\perp\subset\mathbb R^n\) is inherited from the standard Euclidean product; there is no rescaling of generators. The centered zonotope above is centrally symmetric. The limiting constants are finite because \(\deg(v)\le D\). Connectivity implies \(\alpha\ge1\), since \(m_n\ge n-1\). Asymptotic normality is weak convergence of the random width induced by uniformly random directions, not a statement about randomly sampled graphs.

## Proof
**1. Exact support identity.** Every centered segment \([-a/2,a/2]\) contributes \(|\langle u,a\rangle|/2\) to its support function. Therefore
\[
W_n(u)=\sum_{\{i,j\}\in E(G_n)}|u_i-u_j|.
\]
With independent \(X_i\sim N(0,1)\), put \(\bar X=n^{-1}\sum_iX_i\), \(R_n=(\sum_i(X_i-\bar X)^2)^{1/2}\), and \(S_n=\sum_{\{i,j\}\in E(G_n)}|X_i-X_j|\). The normalized centered Gaussian vector is Haar-uniform on the sphere of \(\mathbf1^\perp\), so the following is an equality in distribution (indeed, an identity under this coupling):
\[
W_n=\frac{S_n}{R_n}.
\]
Its exact mean follows by applying the standard spherical coordinate integral to each generator of Euclidean length \(\sqrt2\): \(\mathbb E|\langle U_n,e_i-e_j\rangle|=\sqrt{2/\pi}\,\Gamma((n-1)/2)/\Gamma(n/2)\). The gamma ratio expansion and \(m_n=O(n)\) give \(\mathbb EW_n-\mu m_n/\sqrt n=O(n^{-1/2})\).

**2. Exact covariance ingredients.** Let \(A_n=S_n-\mu m_n\) and \(Q_n=\sum_i(X_i^2-1)\). A single difference \(X_i-X_j\) has law \(N(0,2)\), hence its absolute value has mean \(\mu\) and variance \(v\). Absolute differences from vertex-disjoint edges are independent. For two distinct edges incident to a common vertex, their (suitably oriented) Gaussian differences have correlation of magnitude \(1/2\). The standard bivariate normal formula
\[
\mathbb E(|Y||Y'|)=\frac2\pi\bigl(\sqrt{1-r^2}+r\arcsin r\bigr)
\]
for standard normals of correlation \(r\) can be derived by differentiating with respect to \(r\) (Gaussian integration by parts yields derivative \(2\arcsin(r)/\pi\)) and using the independent case at \(r=0\). On multiplying by two for variance-two differences, their covariance is exactly \(\kappa\). Thus
\[
\operatorname{Var}(A_n)=m_nv+2t_n\kappa.
\]
For one edge let \(B=(X_i-X_j)/\sqrt2\) and \(C=(X_i+X_j)/\sqrt2\). These are independent standard normals and \(X_i^2+X_j^2=B^2+C^2\). Therefore, using \(\mathbb E|B|^3=2\mathbb E|B|\),
\[
\operatorname{Cov}\bigl(|X_i-X_j|,X_i^2+X_j^2-2\bigr)
=\sqrt2\,\mathbb E[|B|(B^2-1)]=\mu.
\]
Consequently \(\operatorname{Cov}(A_n,Q_n)=\mu m_n\) and \(\operatorname{Var}(Q_n)=2n\).

**3. Joint central limit theorem.** Fix real \(a,b\). The linear combination \(aA_n+bQ_n\) is a sum of centered random variables, each depending on one vertex-normal or on two endpoint-normals. Form its dependency graph by joining two summands if their underlying sets of Gaussian coordinates intersect. Its maximum degree is bounded in terms of the graph-degree bound \(D\), while the number of summands is \(m_n+n=O(n)\). All fixed-order absolute moments of the summands are uniformly finite. For each fixed integer \(r\ge3\), the joint-cumulant expansion has nonzero contributions only from connected \(r\)-tuples in this dependency graph. There are \(O_r(n)\) such tuples, and the magnitude of each joint cumulant is bounded by a constant depending only on \(r,a,b,D\). The order-\(r\) cumulant of \((aA_n+bQ_n)/\sqrt n\) is therefore \(O_r(n^{1-r/2})\to0\). Its second cumulant converges by Step 2. Gaussian moment determinacy and the method of moments give the centered normal limit for each linear combination (with the zero-variance case converging in \(L^2\)). Cramér-Wold now gives
\[
\left(\frac{A_n}{\sqrt n},\frac{Q_n}{\sqrt n}\right)
\Longrightarrow N\left(0,
\begin{pmatrix}
\alpha v+2\tau\kappa&\alpha\mu\\
\alpha\mu&2
\end{pmatrix}\right).
\]
This also proves the needed dependency-graph lemma rather than assuming independent edge differences.

**4. Random spherical normalization.** Since \(\sum_iX_i=O_{\mathsf P}(\sqrt n)\),
\[
R_n^2=n+Q_n-\frac1n\left(\sum_iX_i\right)^2
=n+Q_n+O_{\mathsf P}(1).
\]
From Step 3, \(Q_n=O_{\mathsf P}(\sqrt n)\), so
\[
\frac1{R_n}=\frac1{\sqrt n}\left(1-\frac{Q_n}{2n}+O_{\mathsf P}(n^{-1})\right).
\]
Because \(A_n=O_{\mathsf P}(\sqrt n)\) and \(m_n/n\to\alpha\), multiplication gives
\[
W_n-\frac{\mu m_n}{\sqrt n}
=\frac{A_n}{\sqrt n}-\frac{\mu\alpha}{2}\frac{Q_n}{\sqrt n}+o_{\mathsf P}(1).
\]
The joint CLT then yields variance
\[
(\alpha v+2\tau\kappa)
+\frac{\mu^2\alpha^2}{2}-\mu^2\alpha^2
=\alpha v+2\tau\kappa-\frac{\mu^2\alpha^2}{2}=s^2.
\]

**5. Nondegeneracy and boundaries.** The degree-sum identity and Cauchy-Schwarz give
\[
\frac{t_n}{n}=\frac1{2n}\sum_v\deg(v)^2-\frac{m_n}{n}
\ge2\left(\frac{m_n}{n}\right)^2-\frac{m_n}{n},
\]
so \(\tau\ge2\alpha^2-\alpha\). Hence
\[
s^2\ge\alpha(v-2\kappa)+\alpha^2(4\kappa-2/\pi)>0.
\]
Both coefficients are strictly positive: \(v-2\kappa\approx0.401257\) and \(4\kappa-2/\pi\approx0.0143865\); their positivity follows, for example, from \(3.14<\pi\) and \(1.732<\sqrt3<1.733\). The path, cycle and regular-graph formulas result from substituting their edge and wedge counts. No stronger tail, local limit, or unbounded-degree conclusion is asserted.

## Verification
The standalone `graphical_width_checker.py` uses only `numpy` and the Python standard library. Run `python graphical_width_checker.py`. It independently enumerates every segment-sign combination in four small graphs and verifies 160 support/width identities to tolerance \(10^{-12}\); it also generates 12,000 independent Gaussian direction samples for each of a path, a cycle, and a four-regular circulant graph, each with 360 vertices. The observed centered-width variances were respectively \(0.417701\), \(0.411029\), \(0.855115\), versus theoretical limiting expressions \(0.415349\), \(0.415644\), \(0.860061\) evaluated from their finite local counts. These finite numerical checks test normalization and the constants but are **not** a proof of an infinite-dimensional central limit theorem; that proof is Steps 1–5.

## Relationship to prior work
Padrol, Pilaud and Poullot (arXiv:2111.12422, publicly available November 24, 2021) give the deformation-cone and normal-fan structure of the same graphical zonotopes; their explicit theorems concern facet descriptions and combinatorial deformation, not directional random-width CLTs. Pešović and Stojadinović (arXiv:2209.12053, 2022) investigate an interpolation between graphical zonotopes and graph-associahedra, weighted enumerators and normal fans, not Euclidean directional fluctuations. Existing exact first/second width moment results and finite third-moment motif formulas are respected as prior work: knowing finitely many moments does not imply a limiting distribution. In contrast to previously studied individual graph families, the present statement is a single uniform theorem for every fixed-maximum-degree connected graph sequence with convergent two local densities. No claim is made that dependency-graph CLT methods themselves are new.

## Limitations
The degree bound is fixed: sequences with growing hubs can exhibit non-Gaussian fluctuations and are excluded. Both normalized local graph counts must converge; without these limits the stated single variance need not exist. The theorem concerns the canonical unweighted Euclidean embedding only, not arbitrary zonotope deformations or edge weights. It gives convergence in distribution, not an explicit quantitative rate or a uniform finite-sample Kolmogorov bound. The originality comparison is limited to accessible indexed research and inspected primary papers; a less-indexed treatment of Gaussian graph variation may provide equivalent coverage. Independent mathematical assessment has not been performed.

## References
1. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (initial public submission 2021-11-24), https://arxiv.org/html/2111.12422v2.
2. Marko Pešović and Tanja Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (initial public submission 2022-09-24), https://arxiv.org/html/2209.12053v1.
3. Germain Poullot, *Rays of the deformation cones of graphical zonotopes*, arXiv:2404.02669 (initial public submission 2024-04-03), https://arxiv.org/abs/2404.02669.
4. *Sharp width-variance extremizers among tree graphical zonotopes*, published research record dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269. Referenced solely for its exact first/second moment comparison, not for authorship or the present CLT.
