# Fixed-variable theories of finite level-homogeneous ancestry trees

## Finding

For a positive-integer vector \(b=(b_0,\ldots,b_{h-1})\), define \(T(b)\) to be the rooted prefix tree of all words of lengths \(0,\ldots,h\), where the letter in coordinate \(i\) belongs to \(\{0,\ldots,b_i-1\}\). The sole nonlogical relation \(u\prec v\) means that \(u\) is a *proper* prefix of \(v\); equality is available, but root, child, level, sibling and counting predicates are **not** part of the signature. The empty vector describes the one-element tree. Write \(\beta(b)=\min\{i<h:b_i\ge2\}\), with \(\beta(b)=h\) when every level has one child.

**Theorem.** For arbitrary such vectors \(b,c\), with heights \(h,h'\):

1. All these nonempty trees satisfy the same one-variable first-order sentences.
2. In unrestricted-depth two-variable first-order logic, \(T(b)\equiv_{\mathrm{FO}^{2}}T(c)\) precisely when \(h=h'\) and \(\beta(b)=\beta(c)\).
3. For every integer \(k\ge3\), unrestricted-depth \(k\)-variable equivalence is characterized by
   \[
   T(b)\equiv_{\mathrm{FO}^{k}}T(c)
   \quad\Longleftrightarrow\quad
   h=h'\ \text{and}\ \min\{b_i,k\}=\min\{c_i,k\}\quad(0\le i<h).
   \]

Thus fixed-height \(h\) contains exactly \(h+1\) two-variable theories and exactly \(k^h\) \(k\)-variable theories for every \(k\ge3\). In particular, the two-variable fragment detects only the first branching generation, whereas three variables detect branching at *every* generation, up to the cutoff three.

Each equivalence class has a unique smallest member within this family. For \(k\ge3\), if \(a_i=\min\{b_i,k\}\), its size is
\[
1+\sum_{j=1}^{h}\prod_{i=0}^{j-1}a_i.
\]
For \(k=2\), a class with first branching at \(t<h\) has minimum size \(2h-t+1\), and the entirely unbranched class has minimum size \(h+1\).

## Assumptions and scope

All heights are finite, all \(b_i\) are positive integers, and every vertex at depth \(i<h\) has exactly \(b_i\) children. No assumption \(b_i\ge2\) is imposed; unary levels are essential for the two-variable boundary. The language is precisely equality plus strict ancestry. The semantics are ordinary first-order semantics with at most \(k\) reusable variable *names*, no counting quantifiers, and no bound on quantifier rank. Results concern equivalence **within the displayed family**; no assertion identifies a tree among arbitrary finite posets.

## Proof

**1. All node levels are definable using two variables.** Let \(A_0(x)\) be \(x=x\), and recursively let
\[
A_{r+1}(x)=\exists y\,(y\prec x\ \wedge\ A_r(y)),
\]
renaming bound variable names alternately so that only two names occur. In any prefix tree, \(A_r(x)\) means that \(x\) has at least \(r\) proper ancestors. Hence \(L_r(x)=A_r(x)\wedge\neg A_{r+1}(x)\) defines depth \(r\). Distinct heights are therefore separated by a two-variable sentence \(\exists x\,A_r(x)\) for an appropriate \(r\).

**2. The two-variable lower bound.** The formula
\[
\exists x\,\exists y\;[L_r(x)\wedge L_r(y)\wedge\neg(x=y)\wedge\neg(x\prec y)\wedge\neg(y\prec x)]
\]
uses just two variables (the level tests locally rebind variables) and holds exactly when at least one branching generation precedes level \(r\). Thus the least such \(r\), if present, is \(\beta(b)+1\). This distinguishes any unequal first-branch positions.

**3. The two-variable upper bound.** Duplicator maintains the depth of every currently pebbled vertex and the order/equality relation between the at most two pebbles. Once one pebble is removed, let the surviving vertex have depth \(a\). A replacement at depth \(d\) can be equal to it exactly if \(d=a\), its ancestor exactly if \(d<a\), its descendant exactly if \(d>a\), or incomparable exactly if
\[
\beta(b)<\min\{a,d\}.
\]
Every possibility, and its impossibility, depends only on height and the first branching level, independently of the chosen vertex, by level homogeneity. The same option exists in the other tree. This gives a permanent strategy in the two-pebble game and proves equivalence at all quantifier depths.

**4. Branching cutoffs are expressible with three or more variables.** Fix a level \(i<h\) and an integer \(t\ge2\). For two nodes \(u,v\) at depth \(i+1\), a three-variable subformula \(S_i(u,v)\) says that they have a common strict ancestor at depth \(i\):
\[
S_i(u,v):=\exists z\,[L_i(z)\wedge z\prec u\wedge z\prec v].
\]
For \(t\) distinct nodes at depth \(i+1\), requiring \(S_i\) on every pair says they are siblings, because each has a unique ancestor at depth \(i\). With \(k\ge3\) available variable names and \(2\le t\le k\), this is a \(k\)-variable sentence: individual \(S_i\) subformulas can locally rebind a third one of the \(k\) names not denoting their two free arguments. It is true precisely when \(b_i\ge t\). Therefore a difference between truncated branching parameters is detectable with at most \(k\) variables.

**5. Permanent \(k\)-pebble strategy for \(k\ge3\).** Suppose heights and all \(k\)-truncated branching parameters agree. Duplicator preserves the depths of selected nodes and the depth of the longest common prefix of every pair. A configuration of at most \(k\) selected nodes then has a matched depth-labelled, prefix-closed skeleton in both trees. When Spoiler moves a pebble, at most \(k-1\) nodes remain fixed. At any skeleton vertex of depth \(i\), at most \(k-1\) child directions are occupied by paths to these remaining nodes. Follow matched occupied child directions as long as the new chosen path does. If it chooses an unused direction, the matching tree has an unused direction too: if \(b_i<k\), both branch factors equal \(b_i\); if \(b_i\ge k\), both factors are at least \(k\), exceeding the at-most-\(k-1\) occupied directions. After leaving the old skeleton, extend the new path arbitrarily to its prescribed depth. The resulting pairwise longest-common-prefix depths agree. The same construction works with the two trees reversed, including repeated selections and ancestors of selected nodes. Equality and strict ancestry are preserved, so Duplicator can continue indefinitely. The standard fixed-variable pebble-game equivalence proves the implication.

**6. Enumeration and sharp representatives.** Each generation has \(k\) possible truncation labels \(1,\ldots,k-1,k\), independently, yielding \(k^h\) distinct classes for \(k\ge3\). The possible first-branch values \(0,\ldots,h\) give \(h+1\) two-variable classes. Replacing each branch factor by its smallest representative in the same equivalence class strictly minimizes every affected level size and hence the total size \(1+\sum_{j=1}^{h}\prod_{i<j}b_i\). This proves the claimed sharp minimum-size formulas and uniqueness up to isomorphism. In one-variable logic, all atomic instances are \(x=x\) or the always-false \(x\prec x\); on nonempty structures every sentence has the same truth value, proving item 1.

## Verification

Two independent, standard-library Python checks accompany this result. `code/support_check.py` enumerates all ordered two- and three-pebble anchor extension supports for short branching vectors, compares every pair of profiles of heights through three with the predicted classes, and checks four-variable boundary examples. `code/logic_refinement.py` independently stabilizes the exact noncounting \(k\)-variable logical-type partition over partial pebble assignments, including the empty assignment, for nine illustrative pairs. The recorded deterministic outputs are in `verification/support_output.txt` and `verification/logic_output.txt`. Run both scripts with Python 3 in the package root. The proofs in steps 1–6, not the finite checks, establish the theorem for all finite heights and arbitrary branching integers.

## Relationship to prior work

Charatonik, Kieroński and Mazowiecki study two-variable first-order logic over finite trees with descendant and other navigation relations, obtaining finite satisfiability and model-size results; their stated results do not give a classification of unrestricted-depth equivalence for individual level-homogeneous prefix orders. Bohman and collaborators analyze quantifier depth needed to define trees in the *graph-adjacency* language, which is a different resource and signature. Backofen, Rogers and Vijay-Shanker discuss first-order axiomatizations of classes of finite trees; their catalog abstract alone does not resolve the present exact classification. The difference between an arbitrary fixed quantifier-rank comparison and equivalence at *all* ranks is substantive: the permanent pebble invariants here prove the latter. An unspecified broader theorem about finite pebble games on tree orders might still imply this specialization; priority is not certified.

## Limitations

The classification is for finite, level-homogeneous, rooted prefix trees, not arbitrary finite rooted trees; the signature contains only strict ancestry and equality. Named child/level/sibling relations, colors, counting quantifiers, or arbitrary branching at vertices of one level can change the equivalence classes. The verification programs exhaust only their stated small finite tests. The older finite-tree axiomatization report was available as a catalog abstract, not a readable full text in this inspection. No independent mathematical audit has been performed.

## References

1. W. Charatonik, E. Kieroński, and F. Mazowiecki, *Satisfiability of the Two-Variable Fragment of First-Order Logic over Trees* (first arXiv submission 2013-04-26), arXiv:1304.7204, https://arxiv.org/abs/1304.7204.
2. T. Bohman, A. Frieze, T. Łuczak, O. Pikhurko, C. Smyth, J. Spencer, and O. Verbitsky, *First-Order Definability of Trees and Sparse Random Graphs*, Combinatorics, Probability and Computing 16 (2007), 375–400, first online 2007-01-23, doi:10.1017/S0963548306008376.
3. R. Backofen, J. Rogers, and K. Vijay-Shanker, *A First-Order Axiomatization of the Theory of Finite Trees*, DFKI Research Report RR-95-05 (1995), report catalog https://www.dfki.de/en/web/research/projects-and-publications/publication/6123.
