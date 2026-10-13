# An exact five-state edge-open-packing polynomial recursion for forests

## Finding
For every finite simple forest \(F\), including the empty forest and forests with isolated vertices, the complete edge-open-packing polynomial
\[
\mathcal P_F(z)=\sum_{S\subseteq E(F)\colon S\text{ is an edge-open packing}} z^{|S|}
\]
is given by a disjoint, five-state rooted recursion. The recurrence determines the number of admissible edge sets of **every** cardinality in \(O(n^3)\) integer-arithmetic operations for an \(n\)-vertex forest (using ordinary quadratic polynomial multiplication). In particular, it computes the number of maximum edge-open packings, not only their maximum cardinality.

For a rooted component and every vertex \(u\), let \(C(u)\) be its children. Introduce five polynomial states \(a_u,b_u,h_u,c_u,d_u\) and the following auxiliary child-selection polynomials:
\[
Q_{j,u}=[t^j]\prod_{v\in C(u)}(a_v+t z b_v)\quad(j\ge0),\qquad
Q_{\ge2,u}=\sum_{j\ge2}Q_{j,u}.
\]
Then the recursion is
\[
\begin{aligned}
a_u&=\prod_{v\in C(u)}(a_v+h_v+c_v),&
 b_u&=\prod_{v\in C(u)}a_v,\\
h_u&=\sum_{v\in C(u)}z(b_v+d_v)\prod_{w\in C(u)\setminus\{v\}}a_w,&
 c_u&=Q_{\ge2,u},\\
d_u&=Q_{1,u}+Q_{\ge2,u}.&&
\end{aligned}
\]
The base cases at a leaf are \(a_u=b_u=1\) and \(h_u=c_u=d_u=0\). Empty products are one; empty sums are zero. With \(r\) the root of a component \(T\),
\[
\mathcal P_T(z)=a_r+h_r+c_r,\qquad
\mathcal P_F(z)=\prod_{T\text{ component of }F}\mathcal P_T(z).
\]

## Assumptions and scope
An **edge-open packing** is a set \(S\subseteq E(F)\) such that for any distinct \(e_1,e_2\in S\) there is **no third edge** \(f\in E(F)\setminus\{e_1,e_2\}\) joining an endpoint of \(e_1\) to an endpoint of \(e_2\). The empty edge set is included and contributes the constant term one. The input graph is finite, undirected, simple and acyclic; neither connectedness nor a minimum order is required. The indeterminate \(z\) marks the number of selected edges.

## Proof
**Step 1: a known structural equivalence, made bijective.** Given an edge-open packing \(S\), let \(U\) be the set of endpoints of edges in \(S\). Every edge of the induced subgraph \(F[U]\) belongs to \(S\). Indeed, an edge outside \(S\) joining two vertices of \(U\) joins endpoints of two distinct edges in \(S\), contrary to the packing definition; they must be distinct because \(F\) is simple and the outside edge is not selected. If a connected component of \(F[U]\) were not a star, then, being a tree, it would contain an induced path of three edges. All three edges would lie in \(S\), and the middle edge would forbid the outer two. Hence each component of \(F[U]\) is a nontrivial star. Conversely, for any \(U\subseteq V(F)\) whose induced graph is a disjoint union of nontrivial stars, the edge set \(E(F[U])\) is an edge-open packing, since a third edge between endpoints of two its edges would belong to \(F[U]\) and create an induced path of three edges. The two constructions are inverse. This equivalence is consistent with the star observation in Chelladurai et al. [1] and Brešar--Samadi [2]; it is not offered as a novel characterization.

**Step 2: canonical degree colors.** Color the vertices of \(U\) by their degree in \(F[U]\): color \(1\) for degree exactly one, color \(2\) for degree at least two, and color \(0\) outside \(U\). A finite induced forest is a disjoint union of nontrivial stars if and only if (i) every selected vertex has selected degree at least one, and (ii) no edge joins two color-\(2\) vertices. Necessity is clear. Conversely, a nonstar tree contains two adjacent vertices of degree at least two along a longest path; the conditions therefore force every component to be a star. The colors are completely determined by \(U\), even for a two-vertex star (both endpoints have color \(1\)), so no auxiliary choice of star center is being counted.

**Step 3: five disjoint parent-interface states.** At a vertex \(u\), the following states count configurations inside the descendant subtree, with an edge to its parent *already included when stated*:

* \(a_u\): \(u\) has color \(0\), and all descendant components are complete and valid.
* \(b_u\): \(u\) has color \(1\), its parent is selected, and it has no selected child.
* \(h_u\): \(u\) has color \(1\), its parent is unselected, and it has exactly one selected child.
* \(c_u\): \(u\) has color \(2\), its parent is unselected, and it has at least two selected children.
* \(d_u\): \(u\) has color \(2\), its parent has color \(1\), and it has at least one selected child.

Every selected edge inside the subtree and every specified selected child edge contributes one factor \(z\); the edge from \(u\) to its parent is not included in the state weight itself, and is counted once by the parent when it attaches the state. Thus the five classes are disjoint, including their parent interfaces.

If \(u\) is unselected, a child must itself be unselected (state \(a_v\)) or be the root of a completed star (state \(h_v\) or \(c_v\)), giving the formula for \(a_u\). If \(u\) is a selected leaf attached to a selected parent, its children are all unselected: the formula for \(b_u\). If \(u\) is a selected leaf attached to an unselected parent, it has one selected child. That child is either a leaf with selected parent (state \(b_v\)) or a center with leaf parent (state \(d_v\)); the edge contributes \(z\), giving the formula for \(h_u\). If \(u\) is a center, each selected child must be a leaf (state \(b_v\)), otherwise two adjacent centers would occur. It needs at least two such children if its parent is unselected (state \(c_u\)), and at least one if its parent is selected and a leaf (state \(d_u\)); these are precisely the indicated coefficients of \(\prod_v(a_v+tzb_v)\). The five base cases follow at a leaf.

Induction from leaves proves that these rules enumerate exactly the configurations described by their state definitions, without omissions or multiple counting. At a component root, the parent is absent, so precisely states \(a_r,h_r,c_r\) are possible. Vertex-disjoint components make their edge choices independent, proving the forest product formula and the full polynomial identity.

**Step 4: arithmetic complexity.** During each child traversal, track the contributions of zero, one, and at least two selected children, together with the two other products and the one-child sum; this uses a constant number of polynomial additions, shifts and multiplications per child. Every polynomial has degree at most \(|E(F)|\). With naive convolution each such operation takes \(O(n^2)\) arithmetic operations and there are \(O(n)\) child incidences, yielding \(O(n^3)\) integer-arithmetic operations. No division or exponential subset enumeration is used. The bound counts arithmetic operations, not bit complexity.

## Verification
The bundled file `edgeopen_forest_verify.py` independently applies the defining three-edge exclusion test to every edge subset of 436 nonisomorphic trees with at most 11 vertices, and compares the resulting polynomial to the recursion. It additionally checks the vertex-support/star equivalence for all 310,855 such edge subsets. For 600 independently generated random forests, it compares all 350,018 edge subsets directly with the recursion. Ninety-eight star-family tests compare with the binomial coefficients of \((1+z)^{n-1}\). All tests passed. Reproduce with `python -m pip install -r requirements.txt` followed by `python edgeopen_forest_verify.py`. Output is captured in `edgeopen_forest_verify.out`.

These finite checks are cross-checks of the implementation, not a substitute for the induction proving the theorem for all forests.

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan [1] introduced edge-open packing and explicitly observed that the support of a packing induces a union of stars. Brešar and Samadi [2] proved a linear-time algorithm computing the **maximum size** of an edge-open packing in each tree using scalar dynamic programming. The present formula refines this scalar optimization by counting all feasible sets at every size, using canonical degree-state classes to avoid multiple counting of a single packing. Brešar, Dravec, Hedžet and Samadi [3] investigated the relationship to induced matchings and characterized equality of the two optimal sizes in trees; these statements do not determine cardinality distributions. Counting exact packings is also distinct from counting vertex-open packings or induced matchings: adjacent edges within a star are allowed.

## Limitations
Only finite forests are covered, not unicyclic or arbitrary graphs. The induced-star correspondence itself is known; the claimed mathematical contribution is the five-state **all-coefficient recurrence**, not the scalar optimum or an assertion of new general complexity bounds. An equivalent unpublished or unindexed recurrence may exist. The recurrence gives an integer-arithmetic complexity bound, not a guarantee of short binary output or a real-rootedness/unimodality theorem. No independent audit or external proof certification is claimed.

## References
[1] G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776, DOI: `10.1051/ro/2022171` (published online 2022-11-01). Open-access PDF: https://www.numdam.org/item/10.1051/ro/2022171.pdf .

[2] B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (2024-03-01), https://arxiv.org/pdf/2403.00750 .

[3] B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06), https://arxiv.org/pdf/2406.04020 .
