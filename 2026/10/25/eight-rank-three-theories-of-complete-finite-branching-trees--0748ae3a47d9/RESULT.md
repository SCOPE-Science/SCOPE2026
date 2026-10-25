# Eight rank-three theories of complete finite branching trees

## Finding
Let \(T_{b,h}\) be the finite rooted directed tree of all words over an alphabet of size \(b\) of length at most \(h\), with \(b\ge2\) and \(h\ge1\). Its **only** nonlogical relation is \(E(u,v)\), true precisely when \(v\) extends \(u\) by one letter. The root is not named. In ordinary first-order logic with equality and this directed parent–child relation, the rank-three equivalence of \(T_{b,h}\) and \(T_{c,k}\) holds exactly when their parameters have the same key:

\[
\kappa(b,h)=\begin{cases}
(1,\min(b,3)),&h=1,\\
(2,\min(b,3)),&h=2,\\
(\min(h,6),0),&h\ge3.
\end{cases}
\]

Thus precisely eight rank-three theories occur. Every theory has a representative with at most \(127\) vertices and the bound is sharp, realized for the height-at-least-six class by \(T_{2,6}\). This is a classification **within this family**, not of all finite directed trees.

## Assumptions and scope
Finite branching factor and height are integers with \(b\ge2\), \(h\ge1\). The language contains equality and \(E\) but no named root, ancestor closure, sibling predicate, colors, child indices, functions, or counting quantifiers. Rank is nesting depth of ordinary first-order quantifiers, not the number of variables in the sentence.

## Proof
**Exact type recursion.** For an ordered tuple \(\bar a\) write \(A(\bar a)\) for its full atomic diagram (all equalities and all directed edges). Define
\[
Q(x,y)=\bigl(A(x,y),\{A(x,y,z):z\in T_{b,h}\}\bigr),\qquad
S(x)=\{Q(x,y):y\in T_{b,h}\},\qquad
\Sigma(T_{b,h})=\{S(x):x\in T_{b,h}\}.
\]
By the standard Hintikka-type induction, \(\Sigma\) is a complete invariant for first-order sentences of quantifier rank at most three: starting with atomic triple diagrams, apply existential projection and Boolean operations twice for singleton types and once more for sentences. In particular, \(T\equiv_3 U\) iff \(\Sigma(T)=\Sigma(U)\).

**Finite branching and depth pattern lemma.** Suppose \(b\ge2\), \(h\ge3\). For any ordered pair \(x,y\), the set of triple diagrams in \(Q(x,y)\) is obtained by taking \(z=x\), \(z=y\), all parents and children of \(x\) or \(y\), and one \(z\) adjacent to neither. Such an additional vertex always exists: the union of two closed neighborhoods has at most \(2b+4\) vertices, whereas \(|T_{b,h}|\ge1+b+b^2+b^3>2b+4\). Up to their diagrams relative to \(x,y\), these witnesses depend only on the statuses root/internal/leaf, and on whether \(x=y\), one is the parent of the other, the two are siblings, one is the grandparent of the other, or their undirected distance is at least three. The common-neighbor cases are exactly siblings and grandparent/grandchild. Every required additional child of a previously selected parent exists for \(b\ge2\). Thus the descriptions of \(Q(x,y)\) are **independent of the actual branching factor** whenever \(b\ge2\), \(h\ge3\).

Fix a vertex \(x\) at depth \(d\), and write \(r=h-d\). For possible \(y\), the previous paragraph gives the following exhaustive case distinctions. A parent exists iff \(d\ge1\) and is root iff \(d=1\); a grandparent exists iff \(d\ge2\) and is root iff \(d=2\). A child exists iff \(r\ge1\) and is a leaf iff \(r=1\); a grandchild exists iff \(r\ge2\) and is a leaf iff \(r=2\). A sibling exists iff \(d\ge1\), and is a leaf iff \(r=0\). A vertex \(y\) at distance at least three from \(x\) can be root iff \(d\ge3\), can be internal iff \(d\ge1\) or \(h\ge4\), and can be a leaf in every case. The latter assertions use a different top-level branch when necessary (available because \(b\ge2\)). The listed alternatives exhaust every oriented three-vertex diagram, and prove the finite depth-pattern lemma for all \(h\), not merely checked heights.

For explicit inspection, encode an atomic triple diagram by the three equality bits followed by six ordered-edge bits; its integer is \(\sum_{i=0}^{8}2^i a_i\). Encode \(Q(x,y)\) by the two-point atomic flags and the bitset of all triple diagram integers. Give each distinct \(S(x)\), sorted by its number of pair types and then lexicographically by its sorted pair-type codes, the labels \(0,\ldots,10\). The preceding exhaustive cases give these exact depth profiles (commas separate depths from the root):

| Height | Labels at successive depths |
|---|---|
| \(3\) | 0, 4, 3, 2 |
| \(4\) | 1, 5, 7, 6, 2 |
| \(5\) | 1, 5, 8, 9, 6, 2 |
| \(h\ge6\) | 1, 5, 8, then label 10 at every depth from 3 through \(h-3\), then 9, 6, 2 |

All eleven labels denote distinct sets of pair types, and label 10 occurs at least once exactly for \(h\ge6\). In particular the *sets* of labels for heights 3, 4, 5 and \(h\ge6\) are pairwise distinct, and equal within each case for every \(b\ge2\). This proves the infinite-tail equivalence and sharp height cutoff without finite extrapolation.

**Heights one and two.** For \(h=1,2\), the defining type recursion on the finite representatives with \(b=2,3\) gives four types, distinct from the four higher-height types. Any \(b,c\ge3\) at a fixed height at most two are three-round equivalent: the three chosen points traverse at most three distinct child branches, and the matching root-preserving partial configuration can always be realized with three or more children. Branching two is distinguished from branching at least three at height one by the existence of an independent three-set of leaves; at height two, the undirected underlying tree admits a dominating pair exactly when \(b=2\). A dominating-pair sentence uses two existentials and one universal quantifier. All remaining cross-height distinctions are witnessed by unequal exact rank-three type signatures from the stated recurrence. The standalone verifier computes these boundary signatures directly from all triples.

Finally, the eight classes have shortest representatives \(T_{2,1}\), \(T_{3,1}\), \(T_{2,2}\), \(T_{3,2}\), and \(T_{2,h}\) for \(h=3,4,5,6\). Their orders are respectively \(3,4,7,13,15,31,63,127\). Strictly increasing order in \(b\) and \(h\), together with the exact key classification, shows that \(127\) is optimal.

## Verification
Run `python3 VERIFY.py`. It implements the complete atomic-type recursion on actual finite trees, independently of a compact orbit-and-neighborhood implementation; compares all overlapping cases, replays the exact small-height classification, and checks the depth profiles up to height 60. Its recorded output is in `VERIFY_OUTPUT.txt`. The infinite-height step is proved by the depth-pattern lemma above; no finite loop is treated as an infinite proof.

## Relationship to prior work
The general Ehrenfeucht–Fraïssé framework is classical. Verbitsky's 2004 paper studies first-order definability of trees and other graphs with separators, primarily bounds in the *undirected adjacency* language, rather than this fixed-rank eight-class classification in the directed parent–child language. The known rank threshold for directed paths handles branching factor one and does not imply the branching-at-least-two classification. Research on ordinal trees with named successor functions uses a richer signature and different (often infinite) structures; no equivalent eight-class statement was established in the accessible material. No claim of exhaustive global novelty is made.

## Limitations
The result concerns only complete regular rooted trees, branching at least two, finite positive height, and rank three. It does not extend automatically to arbitrary rooted trees, counting logic, child-indexed functions, the ancestor order, or higher quantifier ranks. The computational program independently verifies finite instances; the proof of arbitrary heights is the explicit case analysis. Unindexed or inaccessible literature remains a possible overlap risk. No independent expert audit has been performed.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361 (first public version 2004-01-26), https://arxiv.org/abs/math/0401361 .
2. J. Chen and Y. Zhang, *The elementary theory of full n-branching ordinal trees with successor functions*, arXiv:2608.08426 (2026); its successor-function and ordinal setting is distinguished from the present relational finite-tree statement, https://arxiv.org/abs/2608.08426 .
