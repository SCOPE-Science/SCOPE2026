# The first online-versus-static shattering gap for maximal independent sets of forests

## Finding

Let \(F\) be a finite simple undirected forest and let \(\mathcal M(F)\) be the Boolean vertex-membership concept class of its **inclusion-maximal** independent sets. An observation at \(v\in V(F)\) reports whether the unknown maximal independent set contains \(v\).

**Theorem (sharp first gap and amplification).** Every forest on at most seven vertices satisfies
\[
\operatorname{VCdim}(\mathcal M(F))=\operatorname{Ldim}(\mathcal M(F)).
\]
Up to isomorphism, the **only** eight-vertex forest with strict inequality is the spider \(H=S(1,2,4)\), whose three arms have respectively one, two and four edges. For this tree,
\[
\operatorname{VCdim}(\mathcal M(H))=2,\qquad
\operatorname{Ldim}(\mathcal M(H))=3.
\]
For the disjoint union \(F_s\) of \(s\ge1\) copies of \(H\),
\[
\operatorname{VCdim}(\mathcal M(F_s))=2s,\qquad
\operatorname{Ldim}(\mathcal M(F_s))=3s.
\]
Consequently, arbitrarily large differences occur within forests, although no forest with fewer than eight vertices exhibits any difference.

## Assumptions and scope

An independent set is *maximal* if no further vertex can be added while preserving independence; it need not have maximum cardinality. A set of vertex queries is VC-shattered if all its Boolean labelings occur as restrictions of concepts. The Littlestone dimension is the maximum depth of a complete binary adaptive query tree whose every root-to-leaf answer path is realized by a concept. Dimensions are zero for a singleton hypothesis class, including that of an edgeless forest. Trees are compared up to graph isomorphism. The small-order uniqueness claim ranges over all finite undirected forests of orders at most eight; the family formula holds for every positive integer \(s\).

## Proof

**1. An exact eight-vertex witness.** Label the vertices of \(H\) by \(0,\ldots,7\), with edges
\[
\{01,02,23,04,45,56,67\}.
\]
Thus vertex \(0\) is the branch point and the arm lengths are \(1,2,4\). Encode any vertex set by the integer whose \(v\)-th binary digit indicates membership of vertex \(v\). Directly from independence and domination, the complete list of maximal independent sets is
\[
\mathcal M(H)=\{73,86,90,150,154,166,169,170\}
\]
in this encoding. This list may also be obtained by running the accompanying independent enumeration. It contains eight sets, so no complete binary Littlestone tree has depth exceeding three.

The two vertices \(\{0,5\}\) are VC-shattered. No three vertices are VC-shattered: testing each of the \(\binom{8}{3}=56\) triples against the displayed eight masks gives at most seven distinct restrictions, never eight. Both assertions are finite, fully specified, reproducible checks in the attached verifier, and prove \(\operatorname{VCdim}=2\).

A complete depth-three adaptive witness is encoded by the nested triples
\[
(4,\ (0,\ (2,7,5),\ (5,0,6)),\ (2,\ (6,4,2),\ (6,3,1))).
\]
An internal triple \((v,L,R)\) queries vertex \(v\), following \(L\) on answer zero and \(R\) on answer one. A leaf integer \(j\) denotes the \(j\)-th maximal independent set in the displayed ascending list, indexed from zero. The eight leaves are the eight different concepts, and each satisfies all membership answers along its root-to-leaf path. This proves \(\operatorname{Ldim}=3\).

**2. Complete uniqueness up to eight vertices.** Starting with the one-vertex tree, create all candidates of order \(n+1\) by adjoining one leaf to every vertex of each retained order-\(n\) representative. Identify isomorphic outputs by the recursively sorted rooted-tree code at their one or two centers (the two-center code is the sorted pair of codes on either side of the central edge). Completeness follows by deleting a leaf of any tree with at least two vertices. The center code is a complete isomorphism invariant: a tree is determined recursively by the multiset of its rooted branches, and its center or central edge is isomorphism-invariant.

For each representative, enumerate all \(2^n\) vertex sets and keep exactly those that are independent and dominating. For each query support, count the different restrictions to compute VC dimension. For each nonempty hypothesis subfamily \(K\), compute the exact Littlestone recursion
\[
L(K)=\max_{v:\ K_{v,0},K_{v,1}\ne\varnothing}
\left(1+\min\{L(K_{v,0}),L(K_{v,1})\}\right),
\]
where \(L(K)=0\) when \(|K|\le1\), and the maximum over an empty set is zero. Both recursions are finite and exact, with no probabilistic steps.

The resulting counts of unlabelled trees and dimensions are:

| Vertices | Tree types | Types with unequal dimensions | Dimension pairs and multiplicities |
|---:|---:|---:|---|
| 1 | 1 | 0 | \((0,0):1\) |
| 2 | 1 | 0 | \((1,1):1\) |
| 3 | 1 | 0 | \((1,1):1\) |
| 4 | 2 | 0 | \((1,1):2\) |
| 5 | 3 | 0 | \((1,1):2, (2,2):1\) |
| 6 | 6 | 0 | \((1,1):3, (2,2):3\) |
| 7 | 11 | 0 | \((1,1):3, (2,2):7, (3,3):1\) |
| 8 | 23 | **1** | \((1,1):4, (2,2):13, (2,3):1, (3,3):5\) |

The only unequal eight-vertex representative has the same center code as \(S(1,2,4)\). A second implementation independently enumerates all unlabelled trees through order eight using a separate graph library and recomputes both dimensions by sets and recursive hypothesis partitions. Its results agree. These two executable enumerations, together with the proved exhaustive leaf-generation rule, establish the asserted finite boundary; sample random testing is not being used as a completeness argument.

**3. Disconnected forests and amplification.** If \(F=F_1\sqcup F_2\), maximal independent sets of \(F\) are precisely unions of maximal independent sets chosen independently in the two components. Therefore \(\mathcal M(F)\) is the Cartesian product of concept classes on disjoint query domains. VC dimensions add: a support is shattered by the product if and only if its separate intersections with the two domains are each shattered.

Littlestone dimensions add as well. To see this directly, apply the displayed subfamily recursion. A query in the first domain replaces \(K_1\times K_2\) by \((K_1)_{v,b}\times K_2\), and a query in the second domain behaves symmetrically. Induction on the number of hypotheses in these products gives
\[
L(K_1\times K_2)=L(K_1)+L(K_2).
\]
Thus every disconnected forest of order at most eight has equal dimensions, since each component has at most seven vertices. Together with the tree census, this proves unique first-forest status. Applying additivity repeatedly to the eight-vertex witness yields the claimed formulas for \(F_s\).

## Verification

Run `python3 check_mis_gap.py` with Python 3.9 or later. It constructs all nonisomorphic trees through eight vertices from first principles, evaluates their full sets of maximal independent sets, computes both dimensions by exact recursions, checks the explicit eight-vertex masks and depth-three certificate, and ends with `FOREST_MIS_FIRST_GAP_PASS`.

Independently, with NetworkX installed, run `python3 check_mis_gap_networkx.py`. It invokes its separate nonisomorphic-tree generator, derives maximal independent sets directly as vertex sets, and checks VC and Littlestone dimensions with a separate representation and recurrence, ending with `NETWORKX_FOREST_MIS_GAP_CROSSCHECK_PASS`. The included `verification_output.txt` records the actual execution output of both programs. The unrestricted amplification is mathematical, not inferred from these finite computations.

## Relationship to prior work

Drmota, Ramos, Requilé and Rué [1] investigate maximal-independent-set enumeration, asymptotic counts and size distributions in trees and related graph classes. Their enumerative results do not determine static-versus-adaptive shattering dimensions. Guingona, Kolesnikov, Nierwinski and Soucy [2] study VC and Littlestone dimensions of zero-set families arising from linear combinations; these are distinct concept classes, and their equality theorem does not imply equality for maximal independent sets. Michel and Scott [3] study **graph reconstruction** when a query requests a maximal independent set of an induced subgraph of an unknown graph. Here the graph is fixed, the unknown is one maximal independent set, and the query reports membership of one vertex; the roles of graph and hypothesis differ.

The proof includes a complete finite classification and an independently certified depth-three witness rather than inferring novelty from missing keywords. The general inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\) alone, or counting maximal independent sets alone, does not imply this classification or the witness. The literature comparisons do not establish exhaustive historical priority.

## Limitations

The exact first-order classification stops at eight vertices; it asserts no classification of all larger connected trees. The amplification uses **disjoint** copies of one eight-vertex tree and gives no universal extremal bound among all forests of a fixed larger order. The certified finite computation is exhaustive because of the explicit leaf-extension and isomorphism arguments, but it is not an infinite census. A broader priority search may uncover related results.

## References

[1] M. Drmota, L. Ramos, C. Requilé, J. Rué, *Maximal Independent Sets and Maximal Matchings in Series-Parallel and Related Graph Classes*, AofA 2018, LIPIcs 110, article 18, first publicly available June 18, 2018. DOI: 10.4230/LIPIcs.AofA.2018.18. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2018.18

[2] V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first posted September 10, 2021. https://arxiv.org/abs/2109.04805

[3] L. Michel, A. Scott, *Lower bounds for graph reconstruction with maximal independent set queries*, manuscript dated April 4, 2024. https://people.maths.ox.ac.uk/michel/Papers/graph-reconstruction-maximal-independent-set-queries.pdf
