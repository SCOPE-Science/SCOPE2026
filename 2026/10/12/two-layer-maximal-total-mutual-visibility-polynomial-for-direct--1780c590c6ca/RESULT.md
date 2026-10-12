# Two-layer maximal total-mutual-visibility polynomial for direct products of complete graphs

## Finding
For every pair of integers \(m,n\ge4\), consider the **direct (tensor) graph product** \(G=K_m\times K_n\), whose vertices are cells \((i,j)\in[m]\times[n]\), with two distinct cells adjacent exactly when both their coordinates differ. A set \(X\subseteq V(G)\) is *total mutual-visible* when every two vertices of \(G\) have a shortest connecting path with all internal vertices outside \(X\). It is *inclusion-maximal* if no strict superset remains total mutual-visible.

Identify the omitted cells \(Y=V(G)\setminus X\) with edges of a bipartite graph on the labeled rows and columns. Then \(X\) is inclusion-maximal total mutual-visible **if and only if** precisely one of these cases occurs:

1. \(Y\) consists of four pairwise nonattacking cells (a matching of size four).
2. There are exactly three occupied rows, each holding precisely two cells, and their three two-element column-neighborhoods are pairwise different.
3. There are exactly three occupied columns, each holding precisely two cells, and their three two-element row-neighborhoods are pairwise different.

Cases 2 and 3 overlap precisely on six-cycles supported on three rows and three columns.

Write \(\mathcal M_{m,n}(z)=\sum_X z^{|X|}\), summing over inclusion-maximal total mutual-visible sets. Put \(b_s=\binom{s}{2}\). The complete polynomial is
\[
\boxed{\mathcal M_{m,n}(z)=24\binom m4\binom n4 z^{mn-4}
+\left[\binom m3 b_n(b_n-1)(b_n-2)+\binom n3 b_m(b_m-1)(b_m-2)-6\binom m3\binom n3\right]z^{mn-6}.}
\]
Both coefficients are positive for \(m,n\ge4\). Consequently the previously studied largest total-mutual-visibility cardinality is \(mn-4\), whereas the **lower total-mutual-visibility number** (the smallest inclusion-maximal cardinality) is \(mn-6\). There are no other maximal-set cardinalities. For instance \(\mathcal M_{4,4}(z)=864z^{10}+24z^{12}\) and \(\mathcal M_{5,5}(z)=13800z^{19}+600z^{21}\).

## Assumptions and scope
All graphs are finite, simple and undirected. The product is direct/tensor, **not** Cartesian or strong. The factors satisfy \(m,n\ge4\), with labeled row and column vertices, and the empty set is not inclusion-maximal here. Inclusion-maximal does not mean maximum cardinality. The claimed polynomial counts distinct vertex subsets, not isomorphism classes. The lower number is denoted \(\mu^-_t(G)\). Ordinary total visibility (all vertex pairs in the ambient graph, not only pairs in \(X\)) is essential.

## Proof
**1. The local covering condition.** The graph \(G\) has diameter two for \(m,n\ge3\). Adjacent pairs need no internal vertex. Two distinct nonadjacent cells share exactly a row or a column. For a same-row pair \((i,j),(i,k)\) with \(j\ne k\), their possible internal vertices on shortest paths are exactly cells \((r,c)\) with \(r\ne i\) and \(c\notin\{j,k\}\). Hence the pair is \(X\)-visible exactly when the omitted set \(Y\) includes such a cell. As this must hold for every distinct \(j,k\), the set of distinct column labels represented in \(Y\) **outside row** \(i\) must have cardinality at least three. Symmetrically, outside each fixed column the omitted cells must represent at least three distinct rows. Call these two requirements (R) and (C). They are necessary and sufficient for \(X\) to be total mutual-visible.

**2. The four-matching dichotomy.** If \(Y\) contains a matching of four row-column edges, (R) and (C) hold: deleting one specified row or column can remove at most one edge of this matching and leaves at least three different labels on the opposite side. Conversely, suppose (R) and (C) hold and \(Y\) has no four-matching. By König's bipartite matching-cover theorem, the edges of \(Y\) admit a vertex cover \(C\) using at most three row and column vertices. If \(C\) contains a row and two columns, then after deleting that row at most two occupied column labels remain, contradicting (R). If \(C\) contains two rows and a column, then after deleting that column at most two occupied row labels remain, contradicting (C). The same contradiction handles every smaller mixed cover. A cover of fewer than three rows alone violates (C), and a cover of fewer than three columns alone violates (R). Thus every possible cover consists entirely of three rows or entirely of three columns; in either case all three must be occupied. Therefore a valid \(Y\) either contains a four-matching or is supported on exactly three rows or exactly three columns.

**3. Minimal omissions with three occupied rows.** Suppose all edges lie on exactly three occupied rows whose column-neighborhoods are \(A_1,A_2,A_3\). Requirement (C) is equivalent to \(|A_i|\ge2\) for each \(i\): deleting any one column must not empty a row. Requirement (R), upon deleting one of the three rows, is equivalent to \(|A_i\cup A_j|\ge3\) for all distinct \(i,j\). There are no further requirements for unoccupied rows or columns.

An inclusion-minimal valid \(Y\) must have \(|A_i|=2\) for every \(i\). Indeed, if some \(|A_i|\ge4\), deletion of any incident edge leaves that degree at least three and preserves every pairwise union bound. If \(|A_i|=3\), delete an edge \(e\in A_i\). The resulting neighborhood has size two. A pairwise union can then violate the bound of three only if \(A_i\setminus\{e\}=A_j\) for one of the other two rows with \(|A_j|=2\). Each such other row forbids at most one choice of \(e\), whereas three choices exist. An edge can therefore be deleted while preserving (R) and (C), contradicting minimality.

When each \(A_i\) has size two, the pairwise union condition says exactly that the three two-sets are distinct. Every such six-edge \(Y\) is inclusion-minimal: deleting one edge leaves its row with degree one, and deleting the sole remaining neighbor column then violates (C). Interchanging rows and columns gives the third case.

**4. Four-matchings and maximality.** Every four-matching is inclusion-minimal valid: its deletion leaves only three occupied cells, and three cells cannot satisfy (R) and (C). If a valid \(Y\) contains a four-matching and is inclusion-minimal, it equals that matching. Together with Step 3 and the dichotomy, this classifies all inclusion-minimal valid omitted sets. Because enlarging \(X\) is the same as shrinking \(Y\), inclusion-maximal total-visible \(X\) correspond exactly to inclusion-minimal valid \(Y\).

**5. Counting.** Four-matchings number \(\binom m4\binom n4 4!\). For a fixed three-row support, each row independently chooses one of the \(b_n=\binom n2\) pairs of columns, with all three choices distinct. There are \(b_n(b_n-1)(b_n-2)\) ordered choices, and \(\binom m3\) choices of rows. The symmetric three-column count is \(\binom n3 b_m(b_m-1)(b_m-2)\). An omitted set counted on both sides has exactly three occupied rows and columns, all with degree two. It is a six-cycle in the bipartite \(K_{3,3}\). For fixed row and column triples there are six such cycles, giving the subtraction term \(6\binom m3\binom n3\). The two support sizes are four and six, so the corresponding selected-set sizes are \(mn-4\) and \(mn-6\). This establishes the polynomial and both extremal cardinalities.

## Verification
The standalone `verify.py` reconstructs direct-product adjacency rather than using the proof's row/column criterion. For each unordered nonadjacent pair it computes its common-neighbor mask. It then tests total visibility of \(X\) by requiring its complement to hit every such mask, and tests inclusion-maximality by attempting all single-cell additions to \(X\). It exhausts all subsets of the \(3\times3\), \(3\times4\), \(3\times5\), and \(4\times4\) boards (a total of 102,912 masks), verifying the three-type characterization and the counts. It also tests predetermined samples on \(4\times5\) and \(5\times5\) boards. The small boards with a factor three are checks of the same structural argument, but the formal theorem is restricted to factors at least four. The exact infinite statement is proved combinatorially above; finite checking is not its proof.

Reproduce using `python3 verify.py` with only Python's standard library. See `verification_output.txt` for the recorded output.

## Relationship to prior work
Brešar and Yero, *Lower (total) mutual-visibility number in graphs* (first arXiv posting 6 July 2023, arXiv:2307.02951), define inclusion-maximal total mutual visibility and its lower cardinality, prove general results, and study other graph products, notably Cartesian ones. The material examined does not cover the direct product of two complete graphs in this form. Cicerone, Di Stefano, Klavžar and Yero, *Mutual-visibility problems on graphs of diameter two* (arXiv:2401.02373, first posted 4 January 2024; European Journal of Combinatorics 120 (2024), 103995), prove \(\mu_t(K_m\times K_n)=mn-4\) for \(m,n\ge5\) and construct a four-cell diagonal complement in their Theorem 2.2. The known maximum cardinality and that construction are **not** claimed as novel. Their theorem does not give the lower cardinality, the two-layer inclusion-maximal classification, or the multiplicity polynomial. The present proof uses the classical König matching-cover theorem to rule out further types.

## Limitations
The classification and formulas concern total mutual visibility and the direct product with \(m,n\ge4\); they do not describe ordinary, dual, or outer mutual visibility, nor Cartesian products. They count only inclusion-maximal sets, not every total-visible subset. The prior-literature comparison is based on the identified primary papers, relevant full-text sections and searches; an independently discovered equivalent result under the language of neighborhood transversals is a residual originality risk. No independent audit or certification has been performed.

## References
1. B. Brešar and I. G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951 (initial public posting 2023-07-06), later *Applied Mathematics and Computation* 465 (2024), 128411. https://arxiv.org/pdf/2307.02951
2. S. Cicerone, G. Di Stefano, S. Klavžar and I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (initial public posting 2024-01-04), *European Journal of Combinatorics* 120 (2024), 103995. https://arxiv.org/abs/2401.02373
3. König's bipartite matching-cover theorem (classical).
