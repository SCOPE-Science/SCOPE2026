# Size-biased leaf depth determines the Euclidean boundary-to-volume ratio of rooted-tree order polytopes

## Finding

Let \(T\) be any finite rooted tree with \(n\geq3\) vertices, ordered by ancestry with the root minimal. Its *standard order polytope* is
\[
\mathcal O(T)=\{x\in[0,1]^{V(T)}:x_u\leq x_v\text{ whenever }u\text{ is a parent of }v\}.
\]
Let \(V(T)\) be its ordinary Euclidean \(n\)-volume and \(S(T)\) its total \((n-1)\)-dimensional Euclidean boundary measure, without lattice normalization. For each vertex \(u\), write \(s_u\) for the number of vertices in the descendant subtree of \(u\), including \(u\).

Start a random walk at the root and at each nonleaf vertex \(u\) choose a child \(v\) with probability \(s_v/(s_u-1)\). Stop at the first leaf; let \(D_T\) denote the number of traversed edges. Then the **exact geometric-to-genealogical identity** is
\[
\boxed{\frac{S(T)}{V(T)}=n\left(2+\sqrt2\,\mathbb E D_T\right).}
\]
The individual tree-cover facet \(x_u=x_v\) for a parent–child edge \(u\to v\) has Euclidean area
\[
\boxed{\operatorname{area}_{n-1}(F_{uv})=\sqrt2\,nV(T)\,p_{uv}},\qquad
p_{uv}=\prod_{(a,b)\in\mathrm{path}(r,v)}\frac{s_b}{s_a-1},
\]
where \(p_{uv}\) is exactly the probability that the size-biased root-to-leaf path traverses \(u\to v\). In particular, the tree-cover facet areas define a unit probability flow from root to leaves after division by \(\sqrt2 nV(T)\). The volume itself is \(V(T)=\prod_{u\in V(T)}s_u^{-1}\).

A *leaf-equidistant* rooted tree is one whose leaves all have the same depth \(h\). For every such tree,
\[
\boxed{S(T)/V(T)=n(2+\sqrt2 h),}
\]
**irrespective of its branching profile**. For arbitrary \(T\), writing \(h_{\min}\) and \(h_{\max}\) for minimum and maximum leaf depths, one has
\[
n(2+\sqrt2 h_{\min})\leq S(T)/V(T)\leq n(2+\sqrt2 h_{\max}),
\]
with equality in either inequality if and only if all leaves have the same depth. The global order-\(n\) extrema are
\[
\boxed{n(2+\sqrt2)\leq S(T)/V(T)\leq n(2+\sqrt2(n-1)),}
\]
with equality uniquely for the rooted star and the rooted chain, respectively.

There are sharp **second-extremal gaps**: for \(n\geq4\), if \(T\) is not a rooted star then
\[
\boxed{S(T)/V(T)\geq n\left(2+\sqrt2\left(1+\frac2{n-1}\right)\right),}
\]
with equality exactly when one leaf edge of the rooted star is subdivided once. If \(T\) is not a rooted chain, then
\[
\boxed{S(T)/V(T)\leq n(2+\sqrt2(n-2)),}
\]
with equality exactly for a root-to-branch chain ending in two terminal sibling leaves (a *terminal cherry*).

## Assumptions and scope

All trees are finite, simple, and rooted. Edges are oriented away from the root. The ancestry order requires \(x_u\leq x_v\) along every parent–child edge. Ambient coordinates use the usual orthonormal standard basis; neither the surface area nor volume is normalized by lattice covolumes. Every descendant size \(s_u\) is a positive integer, and for internal vertices \(s_u-1=\sum_{v\text{ child of }u}s_v\). A random linear extension means a uniformly selected total order compatible with ancestry. The structural identity and the leaf-depth bounds hold for all \(n\geq2\), but the statement uses \(n\geq3\) to avoid degenerate classifications; the second-extremal statements require \(n\geq4\).

## Proof

**1. Facet-volume identity for an arbitrary poset.** Let \(P\) be any finite \(n\)-element poset and \(e(P)\) its number of linear extensions. The braid-arrangement triangulation partitions \(\mathcal O(P)\) into \(e(P)\) unimodular coordinate orthoschemes, so \(V(P)=e(P)/n!\). Stanley's irredundant facets are \(x_a=0\) for minimal elements, \(x_b=1\) for maximal elements, and \(x_u=x_v\) for covers \(u\lessdot v\). On each coordinate facet, the induced Euclidean measure agrees with the standard \((n-1)\)-dimensional measure; the sum of their extension counts is \(e(P)\) for minimal elements and \(e(P)\) for maximal elements, since every extension has a unique first and last element. Their combined Euclidean area divided by \(V(P)\) is exactly \(2n\).

For a cover \(u\lessdot v\), the intersection with \(x_u=x_v\) is parametrized by contraction of the cover pair. The elementary map duplicating one coordinate has Euclidean Jacobian \(\sqrt2\). Each linear extension of the contracted poset corresponds bijectively to a linear extension of \(P\) in which \(u,v\) are consecutive in that order. Write \(p_{uv}\) for this adjacency probability. Thus that cover facet has area \(\sqrt2 e(P/uv)/(n-1)!=\sqrt2 nV(P)p_{uv}\). Consequently
\[
\frac{S(\mathcal O(P))}{V(\mathcal O(P))}
=n\left(2+\sqrt2\sum_{u\lessdot v}p_{uv}\right).
\]
This reduction holds for every poset; the following conservation law and extremal rigidity use the rooted-tree assumption essentially.

**2. Rooted-tree hook ratios.** For the ancestry poset of a rooted tree, the familiar recursive shuffle count gives \(e(T)=n!/\prod_ws_w\): after placing the root, independently order the child subtrees and shuffle their extension sequences. If an edge \(u\to v\) is contracted, the contracted tree has \(n-1\) vertices; the new subtree size at \(u\) is \(s_u-1\), and that of each strict ancestor of \(u\) is one less than before; all other subtree factors other than the deleted \(v\)-factor remain unchanged. Comparing the two hook-length products yields
\[
p_{uv}=\frac{s_v}{n}\prod_{w\in\mathrm{path}(r,u)}\frac{s_w}{s_w-1}.
\]
Here the path includes both \(r\) and \(u\). For an edge leaving the root this simplifies to \(s_v/(n-1)\); for two consecutive edges \(u\to v\to z\) the ratios satisfy
\[
\frac{p_{vz}}{p_{uv}}=\frac{s_z}{s_v-1}.
\]
Because the children sizes sum to \(s_v-1\), the probabilities \(p_{uv}\) form a conserved outgoing flow of total mass one. This is precisely the law obtained by choosing a child according to its descendant-subtree size. Every root-to-leaf path's probability is the product of those transition probabilities; hence \(\sum_{u\to v}p_{uv}=\mathbb E D_T\), by writing path length as the sum of traversed-edge indicators. Substitution into Step 1 proves the principal identity and the facet-area formula. The hook-length product also gives \(V(T)=1/\prod_ws_w\).

**3. Fixed-depth and global extremality.** The random path has strictly positive probability of reaching *every* leaf, because every transition probability is positive. Therefore its expected length is bounded between the shallowest and deepest leaf lengths, and equality on either side forces them all to have one common depth. In particular, among rooted trees of order \(n\), \(1\leq D_T\leq n-1\). Identically depth one forces the star; identically depth \(n-1\) forces the chain. This proves all equal-depth and global claims. For a perfect \(b\)-ary tree of height \(h\), \(n=(b^{h+1}-1)/(b-1)\) and the ratio is exactly \(n(2+\sqrt2 h)\), even though the number and sizes of facets vary with branching.

**4. Sharp gap above the star.** For a nonstar, choose a deepest internal vertex \(u\ne r\); all its \(d\geq1\) children are leaves, and \(s_u=d+1\). The probability that the random path reaches \(u\) is at least \(s_u/(n-1)\geq2/(n-1)\): the factor entering the first nonroot vertex is its subtree size divided by \(n-1\), and every subsequent factor can be compared by the hook formula with an extra factor \(s_w/(s_w-1)>1\). As every path makes its first step, and every path reaching \(u\) makes at least a second step, \(\mathbb E D_T\geq1+2/(n-1)\). Equality requires \(s_u=2\), depth of \(u\) equal to one, and no other nonroot internal vertices, precisely the star with one subdivided leaf edge. Conversely that tree's size-biased path has depth two with probability \(2/(n-1)\) and depth one otherwise.

**5. Sharp gap below the chain.** For a nonchain, every linear extension contains at least one pair of consecutive incomparable elements; otherwise it would be a chain ordering and its underlying poset would be total. Thus its number \(A\) of consecutive parent–child pairs is at most \(n-2\), so \(\mathbb E D_T=\mathbb E A\leq n-2\). A terminal cherry has a common chain prefix and two incomparable last leaves, hence every extension has exactly one incomparable adjacency and equality follows. Conversely, if a rooted tree has at least three leaves, a depth-first preorder is a linear extension with at least two consecutive transitions between incomparable branches. If it has exactly two leaves but either branch beyond their last common ancestor has length at least two, start the two branches in an interleaved order with first element of the longer branch, first element of the other branch, then second element of the longer branch; that extension has at least two incomparable adjacent pairs. In either case its expected \(A\) is strictly below \(n-2\). Thus equality forces exactly two terminal sibling leaves after a chain prefix. This completes the classification.

## Verification

The standalone Python program `check.py` uses only the standard library. It enumerates every labeled rooted tree with fixed root zero for orders three through seven (18,247 trees, by Prüfer codes), and compares independently: (i) explicit contracted-tree hook ratios, (ii) a recursive child-size sampling expectation, and (iii) for sampled trees, direct enumeration of all linear extensions and independent coordinate/cover facet incidence counts. It also checks the sharp star, chain, second-star, and terminal-cherry equality characterizations for all 18,247 trees. It reports `VERIFY_OK`. These finite computations corroborate, but do not replace, the proofs for arbitrarily many vertices; the latter are in Steps 1–5.

The reproducible area formula is: build rooted descendant sizes by a postorder traversal; compute the expected remaining path depth via \(D(u)=0\) for leaves and \(D(u)=1+\sum_{v\text{ child}}s_vD(v)/(s_u-1)\) for internal vertices; return \(n(2+\sqrt2 D(r))\). All arithmetic except the final square root may be performed exactly over rational numbers.

## Relationship to prior work

Stanley's order-polytope facets and canonical triangulation give the general positional framework, and the rooted-tree hook-length formula is classical. Can and Hibi (2021) work with order polytopes of tree posets to study toric codes; von Bell and collaborators (2021) study volumes, triangulations, and generalized snake posets. The novel object assessed here is the **ordinary Euclidean surface-area/volume ratio as a size-biased root-to-leaf depth**, including its conserved edge-facet area law, branching-invariant equal-depth classes, and sharp second-extremal rigidity. Those statements are neither volume formulas nor inradius statements. Familiarity with the constituent facet, volume, and hook-length identities is not claimed as new.

## Limitations

The scope is the ordinary standard-coordinate Euclidean embedding of rooted-tree order polytopes. The identity does not claim the same formula for unrooted posets, arbitrary edge lengths, lattice-normalized boundary volumes, or metric changes under unimodular transformations. The second-extremal conclusions concern the fixed number of vertices and this specific ratio; they do not address other intrinsic volumes. Searches of the relevant primary literature and mathematical-record database did not identify the combined spine-law and rigidity result, but terminology differences may leave an equivalent prior formulation undiscovered. Independent validation has not been performed.

## References

- R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680.
- M. B. Can and T. Hibi, *Toric Codes from Order Polytopes*, arXiv:2102.03651, first posted 2021-02-06; sections on tree-poset order polytopes.
- M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, Order Polytopes, and Generalized Snake Posets*, arXiv:2102.11306, first posted 2021-02-22; background and volume section.
