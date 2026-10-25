# Sharp minimum and stability of surface area for unicyclic graphical zonotopes

## Finding

For integers \(n>c\ge3\), let \(G\) be any simple connected unicyclic graph with \(n\) vertices and a unique cycle of length \(c\). In the Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_jx_j=0\}\), define its unweighted, centered graphical zonotope
\[
 Z_G=\sum_{\{u,v\}\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2].
\]
Every such zonotope has intrinsic \((n-1)\)-volume \(c\sqrt n\). Its intrinsic boundary \((n-2)\)-area \(\mathcal S(G)\) satisfies the **sharp universal lower bound**
\[
 \boxed{\mathcal S(G)\ge 2c(n-c)\sqrt{n-1}
 +2\sum_{k=1}^{c-1}(c-k)\sqrt{k(n-k)}.}\tag{1}
\]
Equality holds if and only if all \(n-c\) off-cycle vertices are leaves adjacent to one and the same cycle vertex (unique graph up to isomorphism). Thus identical intrinsic volume and graphic matroid do not force identical Euclidean surface area.

There is a complementary quantitative extremum within the natural **cycle-with-leaves family**: require all off-cycle vertices to be leaves directly adjacent to cycle vertices. Write \(a_i\ge1\) for the number of vertices consisting of cycle vertex \(i\) and its leaves, indexed cyclically, so \(\sum_i a_i=n\). When \(c\mid n\),
\[
 \boxed{\mathcal S(G)\le 2c(n-c)\sqrt{n-1}
 +n\sum_{k=1}^{c-1}\sqrt{k(c-k)}.}\tag{2}
\]
Equality holds exactly when every cycle vertex carries \(n/c-1\) leaves. The upper bound and the following stability inequality remain valid for all integer \(n>c\ge3\), whether or not \(c\mid n\), but the upper bound is then not attained:
\[
 \boxed{\mathcal S_{\mathrm{bal}}-\mathcal S(G)
 \ge {1\over n}\sum_{k=1}^{c-1}\sum_{i=1}^c
 \left(\sum_{j=0}^{k-1}a_{i+j}-{kn\over c}\right)^2.}\tag{3}
\]
Indices in (3) are taken modulo \(c\); \(\mathcal S_{\mathrm{bal}}\) denotes the right-hand side of (2). If \(c\mid n\), equality in (3) can occur only for the balanced leaf allocation. For fixed \(c\) and \(n\to\infty\) through multiples of \(c\), the two sharp surface-area extrema in this leaf family are separated by
\[
\mathcal S_{\mathrm{bal}}-\mathcal S_{\mathrm{min}}
 =n\sum_{k=1}^{c-1}\sqrt{k(c-k)}+O_c(\sqrt n),
\qquad
 {\mathcal S_{\mathrm{bal}}\over\mathcal S_{\mathrm{min}}}
 =1+{1\over2c\sqrt n}\sum_{k=1}^{c-1}\sqrt{k(c-k)}+O_c(n^{-1}).
\]

## Assumptions and scope

Graph edges are unweighted and simple. The ambient intrinsic metric is inherited from \(\mathbb R^n\), and volume and boundary area are measured in \(H\), not in a coordinate quotient with distorted Euclidean norm. The cycle has \(c\ge3\) vertices. The nontrivial assertions (1)–(3) assume \(n>c\); for \(n=c\), the only graph is the cycle and the general surface-area formula in the proof applies. The maximization in (2) is ONLY over graphs whose off-cycle vertices are directly attached leaves; no maximum over all unicyclic graphs is claimed.

## Proof

**1. Graphical forest determinants.** Orient each edge and let its incidence vector be \(b_e=e_u-e_v\). For any forest with two connected components of orders \(s,n-s\), its \(n-2\) vectors are independent, and their parallelepiped \((n-2)\)-volume is \(\sqrt{s(n-s)}\). Indeed, the product of the nonzero Laplacian eigenvalues of a tree of order \(r\) equals \(r\), by the matrix-tree theorem, and the Gram matrix \(B^TB\) for the two-component forest has determinant \(s(n-s)\). Similarly, every spanning-tree edge basis has determinant volume \(\sqrt n\).

The general zonotope intrinsic-volume identity says that \(V_j(Z_G)\) equals the sum of the parallelepiped volumes of all independent \(j\)-subsets of edge vectors (the factor of \(1/2\) in each symmetric segment gives no length change). The \(c\) spanning trees are obtained by dropping one cycle edge, proving \(V_{n-1}(Z_G)=c\sqrt n\). By the Steiner convention, boundary area is \(\mathcal S(G)=2V_{n-2}(Z_G)\).

**2. Exact decomposition of boundary area.** Delete the cycle edges; write \(T_i\) for the rooted tree attached to cycle vertex \(i\), and \(a_i=|T_i|\), so \(a_i\ge1\) and \(\sum_i a_i=n\). For a bridge \(e\), let \(s_e\) be the size of the component of \(G-e\) containing no cycle vertex. To obtain an independent \((n-2)\)-edge subset from \(n\) edges one must delete exactly two edges. Deleting a bridge and one of the \(c\) cycle edges gives \(c\) forests with component orders \(s_e,n-s_e\). Deleting two cycle edges gives one two-component forest with component sizes \(A_{i,k}=a_i+\cdots+a_{i+k-1}\) and \(n-A_{i,k}\), where \(1\le k<c\) and indices are modulo \(c\). Each unordered pair of removed cycle edges appears twice in this ordered interval list. Deleting two bridges leaves an undisturbed cycle, hence a linearly dependent set and contributes zero. Therefore the **exact identity for every unicyclic graph** is
\[
 \mathcal S(G)=2c\sum_{e\ \mathrm{bridge}}\sqrt{s_e(n-s_e)}
 +\sum_{i=1}^c\sum_{k=1}^{c-1}\sqrt{A_{i,k}(n-A_{i,k})}.\tag{4}
\]
This step specializes an existing general intrinsic-volume formula; only the ensuing sharp unicyclic optimization is asserted as the new result.

**3. Sharp global minimum.** Define \(f(t)=\sqrt{t(n-t)}\) on \((0,n)\). Every bridge component satisfies \(1\le s_e\le n-c\le n-3\), so
\[
 f(s_e)^2-f(1)^2=(s_e-1)(n-s_e-1)\ge0,
\]
with equality if and only if \(s_e=1\). There are exactly \(n-c\) bridges. Their contribution to (4) is at least \(2c(n-c)\sqrt{n-1}\), with equality exactly when all off-cycle vertices are direct leaves.

For the cycle contribution define \(F(a)=\sum_{i,k} f(A_{i,k})\), over all \(1\le i\le c\) and \(1\le k<c\). Since
\[
 f''(t)=-{n^2\over4[t(n-t)]^{3/2}}<0,
\]
\(F\) is **strictly concave** on the positive part of \(\sum_i a_i=n\): the length-one intervals already detect every nonzero tangent variation. Every permitted real vector \(a\) is a convex combination of the \(c\) extreme vectors with one entry \(n-c+1\) and the remaining \(c-1\) entries equal to \(1\). All these extremes have equal \(F\) by cyclic symmetry, so strict concavity places the minimum only at one of them. At an extreme vector the \(c-k\) length-\(k\) intervals avoiding the large entry have size \(k\); complementary intervals contribute the same by \(f(t)=f(n-t)\). Thus
\[
 F_{\min}=2\sum_{k=1}^{c-1}(c-k)\sqrt{k(n-k)}.
\]
Combining the bridge bound with this sharp bound gives (1). Equality in both requires all leaves at exactly one cycle vertex, proving rigidity.

**4. Balanced maximum and stability for direct-leaf graphs.** For a cycle-with-leaves graph every bridge has \(s_e=1\), so the bridge term in (4) is constant. Also \(\sum_i A_{i,k}=kn\) for each \(k\). Jensen's strict inequality gives
\[
 \sum_{i=1}^c f(A_{i,k})\le c f(kn/c)
 =n\sqrt{k(c-k)}.
\]
Sum over \(k\) to obtain (2). Strictness for \(k=1\) makes equality possible only if \(a_1=\cdots=a_c=n/c\), realized by integers exactly when \(c\mid n\).

For a quantitative refinement, \(t(n-t)\le n^2/4\) gives \(f''(t)\le-2/n\) everywhere. Hence the strong concavity inequality
\[
 f(y)\le f(x)+f'(x)(y-x)-{(y-x)^2\over n}
\]
for any \(x,y\in(0,n)\). Put \(x=kn/c\) and sum over cyclic \(i\); all first-order terms cancel. Summing over \(k\) yields (3), with strict equality classification from \(k=1\). Finally for fixed \(c\), the bridge term is \(2c(n-c)\sqrt{n-1}=2c n^{3/2}+O_c(\sqrt n)\), whereas the extremal cycle terms are respectively \(O_c(\sqrt n)\) and \(n\sum_k\sqrt{k(c-k)}\). Division gives the two asymptotics.

## Verification

An included standalone numerical checker enumerates connected unlabeled unicyclic graphs on at most seven vertices, checks (1) and its equality type, enumerates leaf allocations for small parameters to check both sharp extrema and (3), and checks the direct formula (4) against independent convex-hull surface/volume computations in eight small examples. The finite tests are not the proof of the all-dimensional claims; the preceding matrix-tree, concavity, and forest-enumeration argument supplies that proof. Run `python CHECK.py` with `networkx`, `numpy`, and `scipy` installed.

## Relationship to prior work

The generator-sum formula for **all** zonotope intrinsic volumes is established by Brazitikos–McIntyre and by Joós–Lángi (specifically Corollary 1 of the latter). It already implies (4) after nontrivial but elementary specialization to graph forests; neither that general identity nor Steiner's surface-area normalization is claimed as new. Padrol–Pilaud–Poullot study graphical zonotope deformation cones and combinatorial properties. The contribution here is the sharp **fixed-cycle-length unicyclic** surface-area minimization over all attached rooted trees, rigid equality classification, and the sharp opposite bound with quantitative stability inside the direct-leaf family. Related earlier tree results concern acyclic graphs rather than graph families containing one cycle, and so do not imply the equal-matroid unicyclic extremal comparison. Comparisons with algebraically equivalent graph-cut weighted sums and other isoperimetric inequalities may require further bibliographic review.

## Limitations

The result does not identify the maximal surface area among **all** unicyclic graphs. In (2), when \(c\nmid n\), the displayed upper bound is strict but is not asserted to equal the integer-constrained maximum. The family uses unit edge vectors with the intrinsic ambient Euclidean metric; arbitrary positive edge weights are not covered. Existing general intrinsic-volume formulas remain established background, and no claim is made of independent validation or exhaustive worldwide novelty certification.

## References

1. A. Padrol, V. Pilaud, and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first publicly posted 24 November 2021, https://arxiv.org/abs/2111.12422.
2. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204, first publicly posted 7 June 2022, especially Corollary 1 and Sections 3–4, https://arxiv.org/abs/2206.03204.
3. D. Brazitikos and A. McIntyre, *Vector-valued Maclaurin inequalities*, arXiv:2102.05900 (2021), general intrinsic-volume identity as acknowledged by Joós–Lángi, https://arxiv.org/abs/2102.05900.
