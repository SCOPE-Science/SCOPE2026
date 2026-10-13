# An antichain expansion for general-position polynomials of all trees

## Finding

Let \(T=(V,E)\) be any finite nonempty simple tree and attach a commuting indeterminate \(z_v\) to each vertex \(v\). A vertex subset \(S\subseteq V\) is in *general position* when no three distinct members of \(S\) occur on one shortest path. Define its multivariate general-position polynomial by

\[
\Gamma_T(\mathbf z)=\sum_{\substack{S\subseteq V\\S\text{ in general position}}}\ \prod_{v\in S}z_v.
\]

Choose **any** root \(r\) and orient each tree edge away from it. Write \(\operatorname{ch}(v)\) for the children of a vertex \(v\), and define recursively

\[
A_v(\mathbf z)=z_v+\prod_{u\in\operatorname{ch}(v)}A_u(\mathbf z),
\qquad\text{with the empty product equal to }1.
\]

**Theorem.** For every choice of root, the entire polynomial is given by the exact antichain expansion

\[
\boxed{\displaystyle \Gamma_T(\mathbf z)=A_r(\mathbf z)+\sum_{v\in V\setminus\{r\}}z_{\operatorname{par}(v)}\bigl(A_v(\mathbf z)-1\bigr).}
\]

Here \(\operatorname{par}(v)\) is the parent of \(v\). In particular, setting every \(z_v=x\) yields *all coefficients* of the ordinary general-position polynomial of **every tree**, not merely a maximum-set count. This gives a linear-size symbolic arithmetic circuit for the multivariate polynomial and an elementary polynomial-time coefficient algorithm after univariate specialization.

## Assumptions and scope

The tree is finite, nonempty, undirected, unweighted, and simple. The empty vertex subset counts once. A path means the unique shortest path in the tree; thus the general-position property excludes a vertex of \(S\) lying on the path between two other members of \(S\). The root is arbitrary and only determines an ancestor partial order, not the resulting polynomial. For a vertex \(v\), its *descendant subtree* \(T_v\) includes \(v\), and an *ancestor antichain* contains no distinct pair comparable under the rooted ancestor order. The product of variables over the empty set is \(1\).

## Proof

**Antichain lemma.** The expression \(A_v\) counts, with their vertex weights, all ancestor antichains of \(T_v\). Indeed, an antichain containing \(v\) consists solely of \(v\), contributing \(z_v\). An antichain omitting \(v\) is a unique independent choice of an antichain in each child subtree, contributing \(\prod_{u\in\operatorname{ch}(v)}A_u\). The two cases are disjoint. The argument includes leaf vertices, for which \(A_v=1+z_v\).

**Decomposition lemma.** Every general-position set \(S\) is in exactly one of the following disjoint classes:

1. \(S\) is an ancestor antichain of the whole rooted tree.
2. There is a uniquely determined oriented edge \(p\to v\) such that \(S=\{p\}\cup B\), where \(B\ne\varnothing\) is an ancestor antichain contained in \(T_v\).

To prove this, first observe that any ancestor antichain is in general position: if \(b\) lies on the path between \(a\) and \(c\), then either \(b\) is an ancestor of one of the endpoints, or one of the endpoints is an ancestor of \(b\). Thus three selected vertices on a path imply two comparable selected vertices.

Suppose instead that a general-position set is not an ancestor antichain. Select comparable vertices \(p,q\in S\) with \(p\) an ancestor of \(q\), and let \(v\) be the child of \(p\) on the path to \(q\). For any other selected vertex \(w\), it must lie in \(T_v\): if \(w\) were outside \(T_v\), the unique path from \(q\) to \(w\) would contain \(p\), contradicting general position. Moreover, any two distinct vertices in \(S\setminus\{p\}\) must be incomparable: if one were an ancestor of the other, their connecting path would extend toward \(p\) and hence \(p\), that ancestor, and the descendant would be collinear. Therefore \(B=S\setminus\{p\}\) is a nonempty antichain of \(T_v\).

Conversely, any \(\{p\}\cup B\) formed this way is in general position: no three vertices of \(B\) can be collinear (it is an ancestor antichain), and no vertex of \(B\) lies on the path from \(p\) to another vertex of \(B\), since such a vertex would be an ancestor of the other. The vertex \(p\) is the **unique** selected vertex that is an ancestor of another selected vertex; every member of \(B\) is incomparable with every other member of \(B\). The child \(v\) is uniquely the first edge common to all paths from \(p\) to vertices of \(B\). Hence the edge index is unique and the classes do not overlap.

By the first lemma, class 1 contributes \(A_r\), while for each parent-to-child edge \(p\to v\), class 2 contributes precisely \(z_p(A_v-1)\) (subtracting only the empty antichain). Summing these disjoint contributions proves the identity. The argument holds for all vertex counts and all assignments of vertex weights, and is independent of the root.

**Computational consequence.** A postorder traversal computes all \(A_v\); a second sum computes \(\Gamma_T\). The expression uses \(O(|V|)\) additions, subtractions, and multiplications in an arithmetic circuit (when children are multiplied successively). With \(z_v=x\), storing coefficient arrays of degree at most \(|V|\) and using ordinary polynomial multiplication gives a polynomial-time exact integer algorithm. In fact, naive multiplication can be organized in \(O(|V|^2)\) integer-coefficient arithmetic operations: each cross-subtree multiplication work unit can be charged to a distinct pair of vertices in different child subtrees, and all coefficient shifts and additions across vertices contribute at most quadratic work.

## Verification

The supplied independent pure-Python verifier is `verify.py` and needs only Python 3 standard library; run `python3 verify.py` from the directory containing it. It implements (i) the displayed edge-sum formula, (ii) a separately derived rooted recurrence for the general-position polynomial, and (iii) direct enumeration of vertex subsets with shortest-path distances from graph breadth-first search. It checks all labeled trees on orders \(1\) through \(6\) via Prüfer sequences, samples larger trees through order \(10\), checks alternative root choices and distinct vertex weights, checks every cubic coefficient using component sizes after vertex deletion, and reproduces a published broom-family expression.

The recorded finite verification tested **1,692 trees**, **166,590 unweighted subsets**, **3,384 additional root choices**, **110 vertex-weight assignments**, and **49 broom parameter pairs**. The exact log is included as `verification_output.txt`; the general theorem is proved above rather than inferred from these tests.

For illustration, two seven-vertex three-arm spiders, with arms of lengths \((1,1,4)\) and \((1,2,3)\), have different polynomials, respectively \(1+7x+21x^2+4x^3\) and \(1+7x+21x^2+6x^3\). Thus tree order and leaf count alone do not determine the enumerator.

## Relationship to prior work

Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial and in their Proposition 2.2 gave a general inclusion–exclusion expression over maximal general-position sets. The same paper computes the polynomial for paths and other particular graph families, discusses broom trees and unimodality, and presents examples of nonisomorphic trees sharing the polynomial. The present theorem is **not** the introduction of the invariant, nor does it assert that tree general-position sets were previously unknown. Its distinction is an explicit, root-independent, multivariate *all-tree* formula with a direct efficient recursion requiring neither maximal-set enumeration nor inclusion–exclusion over their intersections.

The maximum cardinality of a general-position set in a tree is a previously studied scalar invariant and is not claimed as new. Established family formulas for paths and broom trees are specializations of the all-tree identity; no particular family example is claimed as new. A search for an existing all-tree antichain polynomial identity did not identify a matching expression, but the possibility of an earlier equivalent under geodesic-convexity terminology remains.

## Limitations

The identity assumes the uniqueness of shortest paths in a tree; it is not asserted for cyclic or weighted graphs. The multivariate polynomial can have exponentially many monomials, so the stated compactness is that of its arithmetic circuit, not an expanded list of all monomials. Complexity bounds count arithmetic operations; coefficient bit lengths are not treated as unit-size in a bit-complexity theorem. Finite verification is supportive, not an exhaustive check over trees of unbounded order. Originality is subject to possible unindexed equivalent earlier statements, especially among antichain or convex-independence formulations. No independent validation is claimed.

## References

1. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General Position Polynomials*, arXiv:2401.05696, first posted 2024-01-11; *Results in Mathematics* **79**, article 110 (2024). https://arxiv.org/abs/2401.05696 ; https://doi.org/10.1007/s00025-024-02133-3 . Relevant inspected material: Definitions and Propositions 2.1–2.2, the discussion of nonisomorphic trees with equal polynomial, Section 4 on broom trees, and final discussion.
2. P. Manuel and S. Klavžar, *A general position problem in graph theory* (2018). Background on cardinality of general-position sets in trees; cited only for context, not used as a proof of the new all-tree identity.
