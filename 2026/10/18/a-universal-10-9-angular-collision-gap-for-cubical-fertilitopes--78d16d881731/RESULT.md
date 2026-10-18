# A universal \(10/9\) angular-collision gap for cubical fertilitopes

## Finding

Let \(T\) be a rooted full plane binary tree with \(n\ge2\) leaves, consecutively labeled by \([n]\). For an internal node \(v\), write \(I_v\) for its leaf set, \(a_v,b_v\) for the respective left and right child leaf counts, and \(m_v=a_v+b_v\). Let \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\). For arbitrary strictly positive weights \(w_v\) at all internal nodes and arbitrary singleton translation weights \(u_i>0\), consider the intrinsic Euclidean polytope
\[
K(T,w,u)=\sum_{v\ \mathrm{internal}}w_v\Delta_{I_v}+\sum_{i=1}^n u_i\{e_i\}\subseteq\mathbb R^n.
\]
It has affine dimension \(n-1\) and exactly \(2^{n-1}\) vertices. With integer positive weights it is an integral binary nestohedron and hence a fertilitope, in the sense of Defant [1]. The normal-cone results below are independent of the positive weights.

Let \(G,G'\) be independent standard Gaussian vectors in \(\mathbb R^n\), projected orthogonally onto the direction space \(\mathbf1^\perp\), and let \(V(G)\) be the almost surely unique vertex of \(K\) exposed by \(G\). Define the **Gaussian angular collision**
\[
C(T)=\Pr\bigl\{V(G)=V(G')\bigr\}.
\]
Each vertex corresponds bijectively to a left/right winner pattern \(\varepsilon=(\varepsilon_v)\) on the internal nodes. Its normalized Gaussian normal-cone angle is exactly
\[
\alpha_\varepsilon=\prod_{v\ \mathrm{internal}}
\begin{cases}
 a_v/m_v,&\varepsilon_v=\mathrm{left},\\
 b_v/m_v,&\varepsilon_v=\mathrm{right}.
\end{cases}
\]
In particular,
\[
C(T)=\prod_{v\ \mathrm{internal}}\frac{a_v^2+b_v^2}{(a_v+b_v)^2},\qquad
2^{n-1}C(T)=\prod_{v\ \mathrm{internal}}
\left(1+\frac{(a_v-b_v)^2}{(a_v+b_v)^2}\right).
\]

**Sharp dimension-independent forbidden gap:**
\[
\boxed{\quad 2^{n-1}C(T)=1\quad\text{or}\quad 2^{n-1}C(T)\ge\frac{10}{9}.\quad}
\]
Equality at \(1\) holds exactly for the completely balanced perfect binary tree, necessarily with \(n\) a power of two. Equality at \(10/9\) holds exactly when the root joins two perfect binary trees with respective leaf counts \(2^k\) and \(2^{k+1}\), in either order, for an integer \(k\ge0\). Thus the gap is sharp in infinitely many dimensions \(n=3\cdot2^k\), and no other non-perfect tree attains the lower endpoint.

For example, with \(n=6\), the unique minimizer of collision probability up to tree reflection and leaf relabeling joins perfect two-leaf and four-leaf subtrees, and has \(C(T)=5/144\). A tree with an exactly balanced root split into two three-leaf subtrees instead has \(C(T)=25/648\), which is \(10/9\) times larger. Both give combinatorial five-cubes with the same number of vertices.

## Assumptions and scope

All sums of polytopes are Minkowski sums in the displayed coordinate embedding; no affine rescaling of the metric is allowed. Singleton summands translate the polytope and do not affect normal cones. Every internal weight is strictly positive; allowing a zero weight could merge normal cones and invalidate the vertex count. Gaussian projection is harmless because every coordinate-simplex support comparison is invariant under adding a common scalar to every directional coordinate. In particular, isotropic Gaussian exposure in \(\mathbf1^\perp\) has the same comparison ranks as independent continuous identically distributed ambient coordinate scores.

The tree includes **every** internal node as a positive simplex summand. The result is not asserted for binary building sets obtained by omitting internal nodes, nor for arbitrary nestohedra or arbitrary realizations of the cube. The normalized collision \(2^{n-1}C(T)\) equals one exactly when the angular law is uniform across all vertices.

## Proof

**Support rule and vertices.** For any direction \(g\) with distinct coordinates,
\[
h_{K}(g)=\sum_{v\ \mathrm{internal}}w_v\max_{i\in I_v}g_i+\sum_{i=1}^n u_ig_i.
\]
Each internal simplex contributes its positive weight to the coordinate achieving the maximum among the descendant leaves. The winning leaf for a node is obtained recursively by comparing the winning leaves of its two children, so all maximizers are determined by the internal left/right pattern.

Every prescribed pattern has positive probability: for independent continuous identically distributed scores, at each node both branches have positive chances to contain the subtree maximum, and the recursive internal orderings can be arranged compatibly. Two different patterns cannot give the same exposed vertex. Indeed, suppose a vertex is exposed by two generic directions with different simplex maximizers. Expressing the vertex as the sum of its simplex maximizers for the second direction and evaluating at the first direction gives equality in a sum of termwise support inequalities. Because all internal weights are positive and each first-direction simplex maximizer is unique, equality forces the simplex maximizers to agree in every internal node, contradiction. Thus there are exactly \(2^{n-1}\) distinct exposed vertices, one per pattern. The dimension is \(n-1\) because the root simplex has full dimension in the constant-coordinate-sum hyperplane, and every summand lies in a translate of that hyperplane.

**Independence of winner-side decisions.** The ranking of independent continuous coordinate scores is a uniform random permutation. Given a split into disjoint leaf sets of sizes \(a\) and \(b\), the order induced inside each set and the interleaving of the two orders are mutually independent; the interleaving is uniform among the \(\binom{a+b}{a}\) possibilities. The winning side of the union is the side occupying the first position in this interleaving, with respective probabilities \(a/(a+b)\) and \(b/(a+b)\), independent of all decisions strictly inside either child. Applying this decomposition recursively yields independent Bernoulli winner-side indicators across all internal nodes, with the stated parameters. The product formula for each Gaussian normal-cone angle follows.

**Collision identity.** Two independent exposed vertices agree if and only if all their winner-side bits agree. The agreement probability at a node is \((a_v/m_v)^2+(b_v/m_v)^2\). Independence gives the stated formula for \(C(T)\). The normalized product follows from the exact identity
\[
2\frac{a_v^2+b_v^2}{(a_v+b_v)^2}
=1+\left(\frac{a_v-b_v}{a_v+b_v}\right)^2.
\]
There are precisely \(n-1\) internal nodes in a full binary tree with \(n\) leaves.

**Forbidden gap and rigidity.** A perfect tree has equal-sized children at every internal node and therefore normalized collision one. Conversely, if every split has equal sizes, recursive induction makes every subtree perfect; in particular its leaf count is a power of two. Otherwise choose, among all imbalanced internal nodes, one with minimal number of descendant leaves. Every internal split below it is balanced, so each of its two child subtrees is perfect and has a power-of-two leaf count. Those counts are unequal. The ratio of two unequal positive powers of two is at least two, so for that node
\[
\frac{|a_v-b_v|}{a_v+b_v}\ge\frac13.
\]
All other factors of the normalized collision product are at least one, proving the \(10/9\) gap. Equality forces this to be the only imbalanced node, with child sizes in ratio exactly two, and all descendant nodes balanced. It cannot be a proper non-root node: its descendant count would then be \(3\cdot2^k\), not a power of two, whereas a balanced parent would require a sibling subtree with that same non-power-of-two leaf count; the sibling would contain another imbalanced node. Hence the unique imbalanced node must be the root. Conversely, joining perfect subtrees of sizes \(2^k\) and \(2^{k+1}\) has exactly one imbalanced node with relative imbalance \(1/3\), giving normalized collision \(10/9\).

**The six-leaf comparison.** The \(2+4\) perfect-subtree tree attains the universal gap bound; hence it globally minimizes collision among all six-leaf trees and is the only shape attaining it. Its collision is \(2^{-5}(10/9)=5/144\). For a \(3+3\) root, each three-leaf subtree necessarily has one \(1+2\) split, contributing an excess factor \(10/9\), while the root is balanced. Hence its collision is \(2^{-5}(10/9)^2=25/648\).

## Verification

The standalone Python 3 script `VERIFY.py` uses only the standard library and exact rational arithmetic. Run `python VERIFY.py` in a directory containing the script. It exhaustively enumerates all coordinate orderings and all rooted plane full binary tree shapes with two through six leaves. It compares observed winner-pattern frequencies against the exact product law, verifies that each pattern gives a distinct exposed vertex, and verifies support values against direct Minkowski-simplex support calculations with nonconstant positive integer weights. It also checks every tree shape through eight leaves against the sharp gap, the global six-leaf optimum, and six dyadically grafted infinite-family instances. The final output is `ALL VERIFICATIONS PASSED`.

These finite checks independently test the formulas at the specified sizes, but are not used to infer the infinite-dimensional gap: that follows from the exact split independence and the minimal-imbalanced-node argument above.

## Relationship to prior work

Defant [1, Section 2.6 and Theorem 3.2] characterized integral binary nestohedra as fertilitopes. Postnikov, Reiner, and Williams [2, Proposition 7.4] established that the nestohedra of full binary-tree building sets are combinatorial cubes, and their cone–poset correspondence [2, Sections 3 and 8] provides a general description of normal fans. These are foundational results, not claimed here as new. In particular, vertex-angle probabilities can in principle be recovered from pre-existing normal-cone/linear-extension machinery; the new assertion is the **sharp uniform positive gap in normalized collision, its complete equality classification, and its geometric six-leaf consequence**. The proof supplies a direct rank-coupling and rigidity argument specific to the full-tree simplex realization.

The checked related research on Euclidean inradii of connected fertilitopes and on Gaussian collisions of graphical zonotopes concerns different invariants or different polytopes and gives no implication of this sharp binary-nestohedral angular gap. Searches for alternate formulations under cubical nestohedra, Stanley–Pitman polytopes, normal-cone solid angles, random maxima on binary trees, and Rényi collision did not locate a covering theorem. This negative search evidence is not a proof of bibliographic uniqueness.

## Limitations

The conclusion concerns intrinsic Gaussian normal-cone angles for the specified positive simplex-sum realization. It is not affine invariant, and neither the collision gap nor its equality classification is asserted for all combinatorial cubes. It does not establish new facts about general binary nestohedra with missing internal summands. The strong structural statements do not rely on finite enumeration. An independently conducted mathematical review has not occurred. A prior equivalent result phrased in terms of hierarchical random rankings or tree-poset linear extensions remains a bibliographic risk.

## References

[1] Colin Defant, *Fertilitopes*, arXiv:2102.11836, first publicly posted 2021-02-23; *Discrete & Computational Geometry* 70 (2023), 713–752, DOI: 10.1007/s00454-023-00488-y. https://arxiv.org/abs/2102.11836

[2] Alexander Postnikov, Victor Reiner, Lauren Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184, first posted 2006-09-06, especially Sections 3, 7.2, 8. https://arxiv.org/abs/math/0609184
