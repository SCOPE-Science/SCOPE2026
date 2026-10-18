# A Borel facet law and logarithmic mean surface-area excess for Cayley-tree graphical zonotopes

## Finding

Let \(n\ge3\), let \(T_n\) be a uniformly random labeled tree on \([n]\), and define its standard graphical zonotope
\[
 Z_T=\sum_{\{i,j\}\in E(T)}[e_i,e_j]\subset\mathbb R^n.
\]
Give its \((n-1)\)-dimensional affine hull the Euclidean metric induced from \(\mathbb R^n\). Denote its intrinsic boundary surface area by \(S(T)\). For \(1\le k\le\lfloor n/2\rfloor\), put
\[
 q_{n,k}=\frac{\binom nk k^{k-1}(n-k)^{n-k-1}}{n^{n-2}},\qquad
 c_{n,k}=\begin{cases}q_{n,k}/2,&2k=n,\\q_{n,k},&2k<n.\end{cases}
\]

**Theorem (exact expectation, sharp asymptotic, and typical-facet law).** For every integer \(n\ge3\),
\[
 \mathbb E S(T_n)
  =2\sum_{k=1}^{\lfloor n/2\rfloor}c_{n,k}\sqrt{k(n-k)}.
\]
As \(n\to\infty\),
\[
 \boxed{\mathbb E S(T_n)=\sqrt{\frac2\pi}\,n^{3/2}\log n+O(n^{3/2}).}
\]
Equivalently, the expected intrinsic volume \(V_{n-2}(Z_{T_n})=S(T_n)/2\) has leading constant \(1/\sqrt{2\pi}\). The intrinsic \((n-1)\)-volume is exactly \(\sqrt n\) for every individual tree, despite the varying surface area.

Choose uniformly one of the \(2(n-1)\) facets of \(Z_{T_n}\), independently conditional on \(T_n\), and let \(A_n\) denote its intrinsic \((n-2)\)-volume. Then
\[
 \frac{A_n}{\sqrt n}\ \xrightarrow{d}\ \sqrt B,
 \qquad \mathbb P(B=k)=\frac{e^{-k}k^{k-1}}{k!},\quad k\in\{1,2,\ldots\},
\]
where \(B\) is the total progeny of a critical Poisson(1) Galton--Watson tree (the Borel(1) law). The limiting variable has infinite mean, and the finite-dimensional expectation grows logarithmically:
\[
 \boxed{\mathbb E\frac{A_n}{\sqrt n}\sim\frac{\log n}{\sqrt{2\pi}}.}
\]
All statements refer to the canonical unit-edge segment embedding above; a differently scaled zonotope has correspondingly scaled surface areas.

## Assumptions and scope

Trees are finite, simple, unrooted, and labeled on \([n]\), with the uniform Cayley distribution assigning mass \(n^{-(n-2)}\) to each of the \(n^{n-2}\) labeled trees. The segment \([e_i,e_j]\) has Euclidean length \(\sqrt2\). All facet areas, surface areas, and volumes are intrinsic to the affine span, rather than ambient \(n\)-dimensional Lebesgue measure. Surface area means the sum of the intrinsic facet areas; for an \((n-1)\)-dimensional body this equals twice \(V_{n-2}\). Random facets are chosen uniformly from facets, not according to their areas.

For an individual tree \(T\) and edge \(e\), let \(k_e\in\{1,\ldots,\lfloor n/2\rfloor\}\) be the smaller size of the two components of \(T-e\), and let \(N_k(T)=\#\{e:k_e=k\}\). The normalization is fixed throughout, and no concentration or almost-sure limit for the surface area is asserted.

## Proof

**1. Intrinsic facet geometry.** Orient the edges of \(T\) arbitrarily, and write \(b_e=e_i-e_j\). Translating each generating segment turns \(Z_T\) into the parallelotope \(\sum_{e\in E(T)}[0,b_e]\). A tree's \(n-1\) incidence columns are linearly independent. Each facet is obtained by choosing one edge \(e\), fixing its interval parameter at an endpoint, and allowing every other parameter to vary. Thus there are exactly two facets for each edge.

For any forest \(F\), let \(B_F\) be its incidence matrix. If its connected-component sizes are \(m_1,\ldots,m_c\), then
\[
 \det(B_F^\top B_F)=\prod_{a=1}^{c}m_a.
\]
Indeed, permute rows and columns by components. In a connected tree of order \(m\), the Cauchy--Binet expansion of the \((m-1)\)-column Gram determinant sums the squares of the \(m\) maximal row minors. Deleting any one row from a tree incidence matrix leaves a unimodular square matrix, so each squared minor is one. Multiply over components.

For \(F=T-e\), the sizes are \(k_e,n-k_e\), so both facets indexed by \(e\) have intrinsic area \(\sqrt{k_e(n-k_e)}\). Consequently
\[
 \boxed{S(T)=2\sum_{e\in E(T)}\sqrt{k_e(n-k_e)}}
 \quad\text{and}\quad
 \operatorname{vol}_{n-1}(Z_T)=\sqrt{\det(B_T^\top B_T)}=\sqrt n.
\]
This fixed-tree identity is the geometric input; classical zonotope Gram-minor and tree edge-division principles are not presented as independent discoveries.

**2. Exact edge-cut counting.** For \(k<n/2\), a tree with an edge whose smaller component has a prescribed \(k\)-subset \(A\) is assembled uniquely by choosing a labeled tree on \(A\), one on \([n]\setminus A\), and one joining edge. Cayley's formula gives \(k^{k-2}(n-k)^{n-k-2}\) choices for the two trees and \(k(n-k)\) choices for the bridge; the convention \(1^{-1}=1\) handles the singleton tree. Summing over \(\binom nk\) subsets and dividing by \(n^{n-2}\) gives \(\mathbb EN_k(T_n)=q_{n,k}\). For \(2k=n\), the two equal-size sides label the same undirected edge-cut twice, giving \(\mathbb EN_k(T_n)=q_{n,k}/2\). By the facet identity and linearity of expectation the exact formula follows.

**3. Sharp logarithmic asymptotic.** Write Stirling's factorial expansion as
\[
 m!=\sqrt{2\pi m}(m/e)^m e^{\varepsilon_m},\qquad0<\varepsilon_m<\frac1{12m},\quad m\ge1.
\]
A direct cancellation in \(q_{n,k}\) yields the exact expression
\[
 q_{n,k}=\frac{n^{5/2}}{\sqrt{2\pi}[k(n-k)]^{3/2}}
 \exp(\varepsilon_n-\varepsilon_k-\varepsilon_{n-k}).
\]
Uniformly for \(1\le k\le n/2\), the exponential factor equals
\(1+O(1/k+1/(n-k))\), with an absolute implied constant. Set \(w_{n,k}=1\) when \(2k<n\) and \(w_{n,k}=1/2\) when \(2k=n\). The total contribution of the resulting error to the expectation is bounded by
\[
 O\!\left(n^{3/2}\sum_{k\le n/2}
 \left(\frac{1}{k^2}+\frac{1}{k(n-k)}\right)\right)=O(n^{3/2}).
\]
The exact partial-fraction identity \(1/[k(n-k)]=\frac1n(1/k+1/(n-k))\), with the half-weight correction for a balanced split, gives
\[
 \sum_{k=1}^{\lfloor n/2\rfloor}\frac{w_{n,k}}{k(n-k)}
 =\frac{H_{n-1}}n.
\]
Hence
\[
 \mathbb ES(T_n)=\sqrt{\frac2\pi}\,n^{3/2}H_{n-1}+O(n^{3/2})
 =\sqrt{\frac2\pi}\,n^{3/2}\log n+O(n^{3/2}),
\]
as claimed. The error estimate applies to the complete sum; it does not rely on extrapolating finite experiments.

**4. Borel-distributed typical facet and divergent means.** Let \(K_n\) be the smaller-component size for a uniformly selected edge of \(T_n\). Because every tree has \(n-1\) edges,
\[
 \mathbb P(K_n=k)=\frac{c_{n,k}}{n-1}.
\]
For each fixed integer \(k\ge1\), the explicit formula and \((1-k/n)^{n-k-1}\to e^{-k}\) show
\[
 \mathbb P(K_n=k)\longrightarrow p_k=\frac{e^{-k}k^{k-1}}{k!}.
\]
The numbers \(p_k\) sum to one: a Poisson(1) Galton--Watson process becomes extinct almost surely, since its generating function \(f(s)=e^{s-1}\) has only the fixed point \(s=1\) in \([0,1]\); the total-progeny generating function \(G(z)=ze^{G(z)-1}\) has, by Lagrange inversion, coefficients \(p_k\). Thus pointwise convergence of the discrete probabilities implies \(K_n\Rightarrow B\). Moreover, a facet with cut size \(K_n\) has area \(\sqrt{K_n(n-K_n)}\); tightness and the continuous mapping argument imply
\[
 A_n/\sqrt n=\sqrt{K_n(1-K_n/n)}\Rightarrow\sqrt B.
\]
Stirling's formula gives \(p_k\sim(2\pi)^{-1/2}k^{-3/2}\), so \(\mathbb E\sqrt B=\infty\). Finally
\[
 \mathbb E(A_n/\sqrt n)=\frac{\mathbb ES(T_n)}{2(n-1)\sqrt n}
 \sim\frac{\log n}{\sqrt{2\pi}}.
\]
The finite expectation divergence is therefore compatible with convergence in distribution but rules out uniform integrability.

**5. Geometric location among fixed-tree extremes (background comparison).** Edge-division-vector order is established in earlier tree-index work: stars minimize and paths maximize every strictly increasing additive function of the smaller edge-cut size. Applying this to \(k\mapsto\sqrt{k(n-k)}\) gives
\[
 S(K_{1,n-1})=2(n-1)\sqrt{n-1}\le S(T)
 \le 2\sum_{j=1}^{n-1}\sqrt{j(n-j)}=S(P_n),
\]
with the usual uniqueness for \(n\ge4\). The rightmost Riemann sum is \((\pi/4)n^2+o(n^2)\). The random-tree expectation therefore lies asymptotically between a minimum of order \(n^{3/2}\) and a maximum of order \(n^2\), acquiring an intermediate logarithmic factor. No priority is claimed for the tree extremal order itself.

## Verification

The standalone standard-library Python program `check.py` independently enumerates the Prüfer sequences of all labeled trees on \(3\le n\le6\), for a total of 1,440 trees. It computes each intrinsic facet Gram minor by integer-preserving Bareiss elimination and compares it with the cut-size product, checks whole-tree volume determinants, verifies exact Cayley expected cut multiplicities and surface areas against direct enumeration, and checks the star/path bounds. It separately evaluates the exact expectation stably at orders \(100,1000,10000\) and reports leading-asymptotic ratios. Run using `python3 check.py` with no additional packages. The finite checks substantiate the formulas but do not prove their infinite-range validity; the analytical proof above supplies that justification.

## Relationship to prior work

Padrol, Pilaud, and Poullot (arXiv:2111.12422, first posted 2021-11-24) study graphical zonotopes and their deformation cones, establishing the geometric object and its combinatorial setting. Pešović and Stojadinović (arXiv:2209.12053) study interpolating graph polytopes and lattice enumerators, not Euclidean random-tree surface expectation. Schneider (arXiv:2202.06774) derives intrinsic-volume expectation formulas for zonotopes built from **independent identically distributed** random generators; Cayley-tree incidence generators are neither independent nor identically distributed conditional on being a tree, and their intrinsic dimension grows with sample size. Song, Huang, and Wang (arXiv:2010.03981), citing earlier work of Vukićević and Sedlar, study tree edge-division vectors and star/path extremal orders. The present claim does not appropriate that order. Standard Cayley counting, Stirling asymptotics, and the Borel total-progeny law are cited as proof ingredients, not new theorems.

The assessed contribution is the exact **Cayley-average intrinsic surface area**, its sharp critical-logarithmic coefficient, and the **typical-facet Borel law with divergent normalized mean** for this canonical realization. Comparison against relevant previous mathematical findings on graphical-zonotope width variance, inradii, and other tree geometries did not identify a statement implying this stochastic-geometric combination. A missing equivalent theorem under alternative tree-topological-index language remains possible.

## Limitations

The result is an expectation asymptotic, not a concentration theorem or an almost-sure limit for surface area. The random-facet law uses *uniform selection among facets*, not surface-area-weighted selection; the latter has a different distribution. The leading asymptotic assumes the **uniform Cayley labeled-tree model**, not recursive trees, uniform unlabeled trees, or independent segment zonotopes. The finite checker is corroborative, not a substitute for asymptotic arguments. The literature search cannot establish absolute novelty, and no independent mathematical audit has been performed.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first posted 2021-11-24), https://arxiv.org/abs/2111.12422.
2. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (2022), https://arxiv.org/abs/2209.12053.
3. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774 (2022), https://arxiv.org/abs/2202.06774.
4. R. Song, Q. Huang, P. Wang, *The extremal graphs of order trees and their topological indices*, arXiv:2010.03981 (2020), https://arxiv.org/abs/2010.03981.
5. Classical results: Cayley's labeled-tree enumeration and Prüfer correspondence; the Borel total-progeny distribution; the matrix-tree/Cauchy--Binet Gram identities; Stirling's factorial bounds.
