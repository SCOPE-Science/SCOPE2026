# Rank-one linked projective spaces are diagonal degenerations with full multigraded Hilbert function

## Finding

Let \(k=\mathbb C\). For any nontrivial exact finitely generated linked net \(\mathfrak V\) of **two-dimensional** vector spaces, let \(H\) be its finite minimum generating set of size \(h\ge2\). Its linked projective space, embedded as in [1,2], is
\[
X=\mathbb{LP}(\mathfrak V)\subseteq Y=\prod_{v\in H}\mathbb P(V_v)\cong(\mathbb P^1)^h.
\]

Then \(X\) is a nodal **tree of exactly \(h\) distinct coordinate lines**, each varying isomorphically in precisely one different factor. For every vector \(\boldsymbol d=(d_v)_{v\in H}\in\mathbb Z_{\ge0}^H\),
\[
H^1(X,\mathcal O_X(\boldsymbol d))=0,\qquad
h^0(X,\mathcal O_X(\boldsymbol d))=1+\sum_{v\in H}d_v.
\]
The natural restriction map \(H^0(Y,\mathcal O_Y(\boldsymbol d))\to H^0(X,\mathcal O_X(\boldsymbol d))\) is surjective in **every** nonnegative multidegree. Consequently the saturated multigraded coordinate ring has the Hilbert series
\[
\mathcal H_X(\boldsymbol t)=\frac{1+\sum_{v\in H}t_v/(1-t_v)}{\prod_{v\in H}(1-t_v)}
\]
and the relative \(K\)-polynomial
\[
K_X(\boldsymbol t)=\prod_{v\in H}(1-t_v)\left(1+\sum_{v\in H}\frac{t_v}{1-t_v}\right)
=1+\sum_{j=2}^{h}(-1)^{j-1}(j-1)\sum_{\substack{S\subseteq H\\|S|=j}}\prod_{v\in S}t_v.
\]
The curve \(X\) admits an **embedded flat smoothing** to a small diagonal, possibly after independent automorphisms of the factors and base change to a discrete valuation ring. This is a positive answer in dimension one to the flat-degeneration question asked in [1,2].

## Assumptions and scope

A linked net and the minimum set of generators are as defined in [1,2]. The key hypotheses are **exactness**, **finite generation**, and \(\dim_kV_v=2\) for all vertices. The embedding is the standard scheme-theoretic embedding in the product over the minimum generator set, not a projection to a smaller choice of factors. The conclusion concerns the **embedded curve**, not a simultaneous deformation of the underlying quiver representation.

The field \(k\) is complex. All Hilbert series statements concern nonnegative multidegrees. The irrelevant-ideal-saturated defining ideal is taken in the Cox polynomial ring with two degree-\(e_v\) variables for each factor.

## Proof

**1. Component counting and projection degrees.** The component theorem of [1,2] provides precisely \(h\) irreducible components \(C_v\) of dimension one, and the normal-crossings theorem of [1, Thm. 3.3] says they are smooth and meet only in ordinary nodes, without triple intersections. The Chow-class theorem [2, Thm. 4.5] says \(X\) has the Chow class of the small diagonal. Hence, writing \(\delta_{vw}\) for the degree of the projection \(C_v\to\mathbb P(V_w)\), each column of the nonnegative integer matrix \((\delta_{vw})\) has sum one. Each row has positive sum: a positive-dimensional curve cannot be constant in every factor. There are \(h\) rows and \(h\) columns, and the sum of all entries is \(h\). Thus every row and every column has exactly one entry equal to one, all other entries zero. Relabeling components by their unique moving factors, each \(C_v\) maps with degree one onto its factor and is constant on all others. Smoothness implies the moving projection is an isomorphism. These are precisely distinct coordinate lines.

**2. The dual graph is a tree.** Any two distinct coordinate lines meet in at most one point. If their nodal dual graph contained a cycle, fix a component \(C_v\) of that cycle and remove it. Its two cycle neighbors remain connected along the rest of the cycle. All components in that remaining path have constant \(v\)-coordinate, and adjacent ones must agree on it; thus the two nodes on \(C_v\) have the same \(v\)-coordinate. As all its other coordinates are constant, those nodes coincide, forcing at least three components through one point. This contradicts simple normal crossings. Hence the dual graph is a forest. The multivariate Hilbert-polynomial theorem [1, Thm. 4.4] specializes in dimension one to \(P_X(\boldsymbol d)=1+\sum_vd_v\). By the normalization exact sequence for a nodal curve, \(\chi(\mathcal O_X(\boldsymbol d))=h+\sum_vd_v-N\), where \(N\) is its number of nodes. Comparison with the Hilbert polynomial gives \(N=h-1\). A forest on \(h\) vertices with \(h-1\) edges is connected: the dual graph is a tree.

**3. Every nonnegative multigraded section and the Hilbert function.** Let \(L=\mathcal O_X(\boldsymbol d)\). On \(C_v\), \(L\) has degree \(d_v\ge0\). Remove a leaf line \(C_v\), let \(X'\) be the remaining tree, and let \(p=X'\cap C_v\). The normalization Mayer–Vietoris sequence
\[
0\to L\to L|_{X'}\oplus L|_{C_v}\to L|_p\to0
\]
shows by induction that \(H^1(X,L)=0\): both component sides have vanishing \(H^1\), and the evaluation at \(p\) from \(H^0(C_v,\mathcal O_{\mathbb P^1}(d_v))\) is surjective. The same sequence yields \(h^0(X,L)=1+\sum_v d_v\).

For the **ambient restriction** surjectivity, use induction on the number of lines. The \(v\)-coordinate is constant, say \(a\), on \(X'\). An arbitrary section of \(L|_{X'}\) can, by induction, be represented by an ambient form in factors other than \(v\); multiply it by a form of degree \(d_v\) taking value one at \(a\). This extends the section to \(Y\). Its discrepancy from the desired section on \(C_v\) vanishes at \(p\). That discrepancy is a degree-\(d_v\) binary form vanishing at \(a\); multiplying it by suitable degree-\(d_w\) forms in the remaining factors, each evaluating to one at the fixed coordinates of \(C_v\), produces an ambient correction that vanishes on \(X'\) and has the desired restriction on \(C_v\). This works also for \(d_v=0\), when the discrepancy is zero. The base case is a single coordinate line.

It follows that the nonnegative graded pieces of the saturated Cox quotient agree with \(H^0(X,L)\). Summing \(1+\sum_vd_v\) over all nonnegative \(\boldsymbol d\) yields the displayed Hilbert series. Division by the ambient Cox-ring Hilbert series \(\prod_v(1-t_v)^{-2}\) yields the displayed \(K\)-polynomial; expanding gives the subset formula.

**4. An actual embedded flat degeneration.** Cartwright–Sturmfels [3, Prop. 4.4] prove that a connected reduced union of projective lines in \((\mathbb P^1)^h\), with a unique line projecting isomorphically to each factor, represents a point of their diagonal multigraded Hilbert scheme \(H_{2,h}\). The curve \(X\) meets this criterion by Steps 1–2. Their Theorem 4.1 proves that \(H_{2,h}\) is irreducible and is the closure of the orbit of the small diagonal under factorwise projective automorphisms. Hence \([X]\) lies in that orbit closure. A curve through \([X]\) meeting the dense diagonal orbit, followed by normalization and localization at \([X]\), supplies a discrete-valuation-ring base and an embedded flat family with special fiber \(X\) and generic fiber a transformed diagonal. This is a deformation **of the embedded linked projective space**; no lifting of the linked net's quiver maps is asserted.

## Verification

The standalone script `verify_linked_lines.py` constructs reduced embedded coordinate-line trees with two to five components and computes exact ranks of multihomogeneous restriction matrices over \(\mathbb F_{101}\). It checks six tree topologies and \(684\) multidegrees (each coordinate degree \(0\), \(1\), or \(2\)) and prints `VERIFY_OK`. These are finite consistency tests, **not** an infinite proof or a certificate of linked-net realizability; the proof above supplies the universal statements.

## Relationship to prior work

[1] establishes the simple-normal-crossings geometry and **eventual** multivariate Hilbert polynomial, and expressly asks whether all linked projective spaces are embedded diagonal degenerations and how to calculate their complete Hilbert series. [2] establishes the Chow class and indexing of components but explicitly notes that this alone does not imply flat degeneracy. [3] gives a decisive older theorem for the larger class of **already identified** connected coordinate-line configurations and their irreducible diagonal Hilbert scheme. The present statement's additional identification of every rank-one linked projective space as such a tree is the bridge needed to apply [3]; it then determines all nonnegative graded pieces, not just their eventual polynomial. Thus the smoothing mechanism itself is **not** claimed as new. The step from linked-net conditions to the precise coordinate-line tree is the claimed contribution, and its simplicity is a real priority/value limitation.

## Limitations

No claim is made for linked nets with vector-space dimension greater than two, nor for the smoothability of the quiver representation, nor for a smoothing compatible with quiver arrows. The curve of any given tree type need not be obtainable by a single torus one-parameter subgroup of the diagonal, and no such stronger statement is used. The older theorem [3] supplies broad prior coverage, so novelty is restricted to its geometric application to linked nets and the resulting full Hilbert-function identity. Historical priority requires further expert assessment. No independent mathematical audit has been conducted.

## References

[1] F. De León, E. Esteves, E. Vital, *On the Hilbert polynomial of the linked projective space*, arXiv:2609.37634 (first version 2026-09-29), Theorems 3.3 and 4.4 and Introduction.

[2] E. Esteves and F. de León, *Polymatroidal tilings and the Chow class of linked projective spaces*, arXiv:2508.14799 (2025-08-20), components, Theorem 4.5, and Section 4.1.

[3] D. Cartwright and B. Sturmfels, *The Hilbert scheme of the diagonal in a product of projective spaces*, arXiv:0901.0212 (2009-01-02), Proposition 4.4 and Theorem 4.1.
