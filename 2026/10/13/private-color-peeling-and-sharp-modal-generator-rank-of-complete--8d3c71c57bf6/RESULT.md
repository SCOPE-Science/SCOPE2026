# Private-color peeling and sharp modal-generator rank of complete multipartite frames
## Finding

Let \(G=K_{n_1,\ldots,n_k}\) be the loopless undirected complete multipartite graph with nonempty parts \(V_i\), and interpret its edge relation as a single ordinary diamond modality on the powerset Boolean algebra. Give its vertices arbitrary propositional colors from a finite palette \(C\). Write \(S_i\subseteq C\) for the **set** of colors appearing in part \(V_i\), ignoring repeated occurrences within the part.

Form a sequence of remaining part indices \(R_0=[k]\), deleting at each simultaneous round every part that has at least one *private color* relative to the remaining parts: a color that belongs to its support and to no other support among \(R_t\). Call the stationary set \(R_*\) the visibility core. This purely combinatorial peeling procedure exactly computes the modal-equivalence classes: they are the nonempty sets of vertices of color \(c\) inside each peeled part, and, for every color \(c\) occurring in the core, the entire set of core vertices of that color. Thus the number of atoms in the generated Boolean modal algebra is
\[
T=\sum_{i\notin R_*}|S_i|+\left|\bigcup_{i\in R_*}S_i\right|,
\]
and the algebra has exactly \(2^T\) members. This includes the case \(R_*=\varnothing\), where the second summand is zero.

For \(r\) ordered propositions, each vertex is colored by its truth-value word from a palette of size \(q=2^r\). These propositions generate the entire powerset algebra if and only if the color words within every part are pairwise distinct and the visibility core is empty. Equivalently, every nonempty subfamily of parts has a color appearing in precisely one of those parts.

Order part sizes \(n_{(1)}\ge\cdots\ge n_{(k)}\ge1\). The exact minimum number of generators, allowing \(r=0\), is
\[
\boxed{\operatorname{rank}(\mathcal P(V(G)),\Diamond)=\left\lceil\log_2\left(\max_{1\le i\le k}(n_{(i)}+i-1)\right)\right\rceil.}
\]
In every coloring, the modal type partition stabilizes by depth \(\max(0,k-1)\). This universal bound is sharp for every \(k\ge2\), even when all parts have size at most two.

## Assumptions and scope

Fix any integer \(k\ge1\) and any positive integers \(n_1,\ldots,n_k\). Vertices are adjacent exactly when they lie in distinct parts; there are no loops. Boolean propositional connectives are unrestricted, and \(\Diamond X=\{v:\exists w\,(v\sim w\land w\in X)\}\). The generated algebra is the least Boolean subalgebra containing the chosen propositions and closed under \(\Diamond\); modal depth counts nested modalities. Distinct truth-value words correspond to disjoint Boolean color predicates; unused words are harmless. No graded modalities, additional named relations, constants beyond Boolean truth/falsity, or counting tests are assumed.

Define
\[
R_{t+1}=R_t\setminus\left\{i\in R_t:\exists c\in S_i\text{ such that }c\notin\bigcup_{j\in R_t\setminus\{i\}}S_j\right\}.
\]
Because every part is nonempty, a nonempty stationary core has at least two parts and each color it uses occurs in at least two of its parts.

## Proof

**Part identification.** Suppose all parts removed before a given peeling round have already been defined by formulas. For a part \(V_i\) newly removed, select a witness color \(c_i\) private among the remaining supports. The Boolean formula
\[
\theta_i=(\text{color }c_i)\land\neg\bigvee_{h\notin R_t}\psi_h
\]
has a nonempty extension contained in \(V_i\), where \(\psi_h\) defines the previously removed part \(V_h\). Since adjacency is complete across distinct parts and empty within any part, \(\neg\Diamond\theta_i\) defines exactly \(V_i\). Therefore each removed part is definable; intersecting its characteristic formula with a color predicate defines its color classes. The final sole remaining part, if any, is alternatively definable by complementation of the preceding parts.

**Core indistinguishability.** Relate vertices from peeled parts precisely when they have the same part and color, and relate vertices from any of the surviving core parts whenever they have the same color. Related peeled vertices have identical sets of neighboring parts and hence match all successor colors. For related core vertices in parts \(V_i,V_j\), each successor in a peeled part can be matched in that same peeled part. Any core successor of color \(d\) has a matching core successor outside \(V_j\), since \(d\) appears in at least two distinct core parts. The matching condition is symmetric. Hence this relation is a color-preserving bisimulation, so modal formulas cannot split its classes. Conversely all those classes are distinguished by the formulas above or by their colors. Their count is \(T\), proving the exact atom formula. A finite Boolean algebra with \(T\) atoms has exactly \(2^T\) elements.

**Generation.** Within any one part, identical colors give indistinguishable vertices, so injectivity inside each part is necessary. If the core is nonempty, a color occurs in at least two core parts; its vertices are bisimilar, precluding full generation. If there are no repeated partwise colors and the core is empty, each quotient atom is a singleton; every singleton is definable, proving sufficiency. The all-subfamilies private-color formulation is equivalent: a nonempty stationary core violates it, while a nonempty subfamily with no private color cannot be reduced by peeling from any larger family.

**Exact rank.** Set \(Q=\max_i(n_{(i)}+i-1)\). In a successful sequential peeling order, choose one private witness color from each removed part (refining simultaneous removals arbitrarily). The \(i\)-th chosen witness is new relative to all earlier witnesses and is absent from every subsequent part. Thus the \(i\)-th part in that order has at most \(q-i+1\) available distinct colors. Rearranging part sizes in descending order minimizes the maximum of \(n_{\pi(i)}+i-1\): whenever a smaller part precedes a larger one, swapping them does not increase this maximum. Therefore \(q\ge Q\). Conversely, for \(q=Q\), order parts by decreasing size and label the palette \(c_1,\ldots,c_Q\). In part \(i\), choose \(n_{(i)}\) distinct colors from \(\{c_i,\ldots,c_Q\}\), always including \(c_i\). Such a choice exists since \(Q-i+1\ge n_{(i)}\). After the preceding parts are removed, \(c_i\) is private to part \(i\), so peeling succeeds. The minimum feasible power-of-two palette size is \(2^{\lceil\log_2 Q\rceil}\).

**Depth and sharpness.** Every nonterminal peeling round removes at least one part. At most \(k-1\) rounds are needed to identify all parts: if a single part remains, its indicator is the complement of the identified other parts. Each identification introduces at most one additional modal nesting. Hence the full modal-equivalence partition stabilizes by depth \(k-1\) when \(k\ge2\), and by depth zero for \(k=1\). To attain the bound, choose different colors \(c_0,\ldots,c_{k-1}\). Put colors \(\{c_0,c_1\}\) in part one, \(\{c_{j-1},c_j\}\) in each intermediate part \(2\le j\le k-1\), and \(\{c_{k-1}\}\) in the last part. At depth zero there are \(k\) colors. Iterative successor-type-set refinement splits precisely the two occurrences of \(c_t\) in round \(t\), for \(1\le t\le k-1\), giving exactly \(k+t\) depth-\(t\) types. This proves sharpness for all \(k\ge2\).

## Verification

The self-contained standard-library program `verify.py` independently computes modal successor-type refinements on 19,607 exhaustively enumerated nonempty support configurations, checks the sorted-size rank threshold against 274 brute-force feasibility cases, tests the depth-sharp examples for thirteen part counts, and directly closes the finite Boolean modal operations on 600 randomized colorings that permit repeated colors within parts. Running `python3 verify.py` prints:

```
VERIFY_OK exhaustive_support_cases 19607 rank_bruteforce_cases 274 sharp_depth_cases 13 direct_boolean_closures 600
```

These finite checks corroborate the proof; they do not prove its unbounded claims by enumeration.

## Relationship to prior work

Beohar, Gurke, König, and Messing (2022) develop general Hennessy–Milner connections between modal-logical indistinguishability and bisimulation. The present result specializes ordinary modal bisimulation to **loopless complete multipartite frames** and derives an explicit peeling quotient, closed-form generator rank, and sharp modal-depth bound; none of these specialized formulas was identified in the inspected primary text. Alon, Fachini, and Körner (2000) study locally thin set families, providing an important antecedent for the private-color condition: the latter is not claimed as an independently new combinatorial concept. The full generator-rank and quotient formulas concern a separate algebraic-modal question.

## Limitations

The result concerns one ordinary modal diamond on finite complete multipartite simple graphs. It does not address reflexive frames, graded/counting modalities, arbitrary graph families, or the number of all generating valuations. No exhaustive investigation of older modal-coloring and locally-thin-family literature has been completed; an implicit or equivalent antecedent may exist. Computational checks are finite; independent mathematical and originality audits have not been performed.

## References

1. H. Beohar, S. Gurke, B. König, K. Messing, *Hennessy-Milner Theorems via Galois Connections*, arXiv:2207.05407, first submitted July 12, 2022. https://arxiv.org/abs/2207.05407.
2. N. Alon, E. Fachini, J. Körner, *Locally Thin Set Families*, Combinatorics, Probability and Computing 9 (2000), 481–488, DOI:10.1017/S0963548300004521. https://doi.org/10.1017/S0963548300004521.
