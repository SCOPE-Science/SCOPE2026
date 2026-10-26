# A sharp one-bit height law for online learning of rooted-tree descendant cones

## Finding

For any finite nonempty rooted tree \(T\), take a hypothesis for every node \(v\): membership in its principal descendant cone \(C_v=\{x\in V(T):v\preceq x\}\), where \(v\preceq x\) means that \(v\) is an ancestor of or equal to \(x\). Write \(h\) for maximum root-to-node distance in edges. If \(h=0\), then \(\operatorname{Ldim}(\mathcal C(T))=0\). For \(h\ge1\),

\[\lfloor\log_2(h+1)\rfloor\le\operatorname{Ldim}(\mathcal C(T))\le1+\lfloor\log_2(h+1)\rfloor.\]

Both limits are attained for every height: paths attain the lower limit; complete binary trees attain the upper for \(h\ge2\); a three-leaf star attains the upper for \(h=1\). More precisely, for the full \(b\)-ary rooted tree \(B_{b,h}\), \(b\ge2\),

\[\operatorname{Ldim}(\mathcal C(B_{b,h}))=\begin{cases}0,&h=0,\\1,&h=1,\ b=2,\\2,&h=1,\ b\ge3,\\1+\lfloor\log_2(h+1)\rfloor,&h\ge2.\end{cases}\]

The VC dimension is at most two for every rooted tree, and equals two for \(B_{b,h}\) when \(h\ge2\) or when \(h=1,b\ge3\). Thus even an exponentially large family of cone hypotheses on a complete tree has online complexity governed by the tree's height, up to one bit.

## Assumptions and scope

All trees are finite, nonempty, rooted, with edges directed away from the root. Nodes (not leaves alone) constitute both the hypothesis-index set and the query domain. Duplicates are identified, although the cones here are distinct. The Littlestone dimension is the maximum depth of a complete binary query tree whose every root-to-leaf labeling is realized by a concept, with depth zero for a singleton hypothesis family. Height counts edges, not levels. This statement concerns deterministic realizable online learning (not noisy or agnostic mistakes).

## Proof

**Upper bound.** Fix any query node \(x\). The hypotheses answering one are exactly cones rooted at ancestors of \(x\), at most \(h+1\) nodes. A class of \(m\) distinct hypotheses cannot shatter a binary tree of depth greater than \(\lfloor\log_2 m\rfloor\), since distinct label strings require distinct hypotheses. Thus, if \(\mathcal C(T)\) shattered depth \(d\ge1\), then its first positive branch would shatter depth \(d-1\), and \(2^{d-1}\le h+1\). This establishes the stated upper bound, including singleton case.

**Lower bound and sharp path.** Choose a maximal root-to-leaf path \(v_0,v_1,\ldots,v_h\). Restrict hypotheses to \(C_{v_i}\) and queries to \(v_j\). The resulting membership matrix has entry one precisely when \(i\le j\): the \(h+1\) ordered threshold functions. A balanced binary search of ordered thresholds yields a complete mistake tree of depth \(\lfloor\log_2(h+1)\rfloor\) (inductively split a consecutive block into two blocks each of at least \(2^{d-1}\) possibilities). Hence the full class has at least this dimension. A rooted path has precisely these hypotheses, and the hypothesis-count upper bound is then tight.

**Sharpness on branching trees.** Let \(T=B_{b,h}\) with \(h\ge2,b\ge2\), and put \(k=\lfloor\log_2(h+1)\rfloor\). Query the leaf \(x=00\cdots0\) of depth \(h\). Its positive branch is the chain of \(h+1\) ancestor cones. For each prefix-depth \(j\), \(0\le j<h\), a query \(y=0^j1\) has value one exactly on the first \(j+1\) members of that ancestor chain. Consequently the positive branch has dimension at least \(k\) by the same balanced-threshold construction. The negative branch contains the entire cone concept class attached to the first-child subtree labeled \(1\), isomorphic to \(B_{b,h-1}\), and queries within that subtree distinguish its concepts exactly as in the smaller tree. For \(h=2\), this smaller class has Littlestone dimension at least one, equaling \(k=1\). For \(h\ge3\), induction gives dimension \(1+\lfloor\log_2 h\rfloor\ge\lfloor\log_2(h+1)\rfloor=k\). Thus both branches shatter depth \(k\), so the original class shatters depth \(k+1\). The universal upper bound gives equality. For \(h=1\), the binary root-with-two-leaves class has three hypotheses and dimension one, since every query has a singleton negative branch. With \(b\ge3\) leaves, a leaf query has two hypotheses in its positive branch (root and that leaf) and at least two other leaf hypotheses in its negative branch; each branch shatters depth one, hence the dimension is two. The \(h=0\) case is a singleton class.

**VC bound.** Descendant cones form a laminar family: two cones are disjoint or nested. If three points were VC-shattered, there would be traces selecting each pair of points while omitting the third. Any two of those three pair-selecting cones intersect, and therefore must be nested. But two distinct two-element traces on the same three-point set cannot be nested: contradiction. Thus \(\operatorname{VCdim}\le2\). For \(b\ge2,h\ge2\), choose two sibling leaves inside one first-child subtree; the cones rooted at their individual leaves, their parent, and a node in another first-child subtree respectively realize the four dichotomies. For a star with \(b\ge3\), two leaves together with root, their singleton cones and a third leaf give the four traces. This proves sharpness.

## Verification

A standalone finite-exact checker in `check_tree_cones.py` independently implements the definition of Littlestone dimension via version-space recursion, checks complete binary shattered-tree certificates stored in `witness_trees.json`, and evaluates VC traces. Its output, `verification_output.txt`, records checked complete binary trees and all parent-before-child rooted trees up to seven vertices. The all-height proof above does not use induction from this finite enumeration.

To reproduce, place the three files in one directory and run `python3 check_tree_cones.py`. The code emits `ALL_CERTIFICATES_OK` only after checking its certificates and enumerations; no external packages are used.

## Relationship to prior work

Malliaris and Moran [1] develop general model-theoretic foundations and bounds for Littlestone dimension and online learning. Their results are not an exact calculation for the principal descendant-cone class of each finite rooted tree. Walker [2] studies embedded tree dimension and the Sauer–Shelah dichotomy for leaf families in finite branching trees, and supplies general Littlestone/VC context. A leaf-family embedded-tree dimension is not the Littlestone dimension of the node-indexed descendant-cone concept class defined here, and the inspected argument does not yield the present sharp universal height law or complete-branching equality cases. The simple finite-class information bound and laminar VC bound are classical; the contribution claimed here is their sharp simultaneous specialization to all finite rooted trees with matching branch constructions.

## Limitations

The one-bit interval is exact and globally sharp, but does not distinguish which endpoint an arbitrary nonregular rooted tree attains. The lower and upper witnesses are explicit, not statements of uniqueness. No independent peer review or exhaustive historical-priority certificate is claimed; analogous ancestor-query bounds may have appeared under alternative hierarchical-learning terminology. Finite checker output alone cannot prove the general statement.

## References

[1] Maryanthe Malliaris and Shay Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, first posted 2021-08-12.

[2] Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted 2022-03-23.
