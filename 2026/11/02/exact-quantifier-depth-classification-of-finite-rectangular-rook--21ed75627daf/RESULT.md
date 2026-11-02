# Exact quantifier-depth classification of finite rectangular rook graphs

## Finding

Write \(R_{m,n}=K_m\square K_n\) for the rectangular rook graph, where \(2\le m\le n\). For every integer \(q\ge2\), first-order equivalence through quantifier rank \(q\), in the graph language of equality and adjacency alone, is characterized by

\[
R_{m,n}\equiv_q R_{m',n'}
\quad\Longleftrightarrow\quad
(\min\{m,q\},\min\{n,q\})=(\min\{m',q\},\min\{n',q\}).
\]

Consequently, the infinitely many finite rectangular rook graphs have exactly \(\binom q2\) rank-\(q\) equivalence classes. Their smallest side-size representatives are \(R_{a,b}\) for \(2\le a\le b\le q\). The largest of these smallest representatives has \(q^2\) vertices, and this cutoff is sharp within the rook-graph family.

A rank-preserving normal-form consequence holds: every first-order *sentence* of rank at most \(q\), when restricted to this family, is equivalent to a Boolean combination of sentences asserting a clique or independent set of cardinality at most \(q\). Thus full bounded-depth first-order logic requires no tests beyond two size thresholds on this family.

For two nonisomorphic graphs in the family, the minimum rank of a distinguishing sentence equals

\[
\min\bigl(\{\min\{m,m'\}+1:m\ne m'\}
\cup\{\min\{n,n'\}+1:n\ne n'\}\bigr),
\]

where an empty set term is omitted. The optimal distinguishing sentence is always an existential clique or independent-set test (up to negating a sentence to choose the direction).

## Assumptions and scope

The vertex set of \(R_{m,n}\) is \([m]\times[n]\). Distinct vertices \((i,j)\) and \((i',j')\) are adjacent if and only if \(i=i'\) or \(j=j'\). The factors are not named in the language; swapping coordinates produces an isomorphic graph, so side sizes are ordered \(m\le n\) for notation. All factors have at least two vertices. The language consists only of equality and one symmetric irreflexive adjacency predicate \(E\), with no counting quantifiers, order, coordinate predicates, constants, or extra sorts.

For \(k\ge2\) let \(C_k\) say that there exist \(k\) pairwise distinct mutually adjacent vertices, and let \(I_k\) say that there exist \(k\) pairwise distinct mutually nonadjacent vertices. Both have quantifier rank exactly \(k\), as displayed by their existential prefixes. Write \(\equiv_q\) for agreement on all first-order sentences of quantifier rank at most \(q\).

## Proof

**Clique and independence numbers.** In \(R_{m,n}\), a set of pairwise nonadjacent vertices has distinct first coordinates and distinct second coordinates. Hence an independent set has at most \(m\) vertices. A diagonal matching of \(m\) pairs realizes equality, so \(\alpha(R_{m,n})=m\). Likewise any row has \(n\) mutually adjacent vertices. If a clique contains at least three vertices, any two adjacent members share exactly one coordinate, say a row; any third vertex adjacent to both must lie in that row, and induction shows that the clique is contained in a single row or column. Therefore \(\omega(R_{m,n})=n\), also when the maximum clique has just two vertices.

**Necessary truncations.** Suppose \(R_{m,n}\equiv_qR_{m',n'}\). For every \(2\le k\le q\), the truth values of \(I_k\) agree, and thus \(m\ge k\) iff \(m'\ge k\). This is equivalent to \(\min\{m,q\}=\min\{m',q\}\). Applying the same argument to \(C_k\) gives the equality for the larger side sizes. Hence the displayed pair of truncations is necessary.

**Sufficient truncations.** Assume both truncations match. We exhibit a winning strategy for Duplicator in the \(q\)-round Ehrenfeucht–Fraïssé game. Duplicator maintains, after \(r\) moves, the following stronger invariant: for all already chosen pairs of vertices, their *first-coordinate equality patterns* match in the two structures, and their *second-coordinate equality patterns* match as well. It initially holds vacuously. If Spoiler selects a vertex with first coordinate already used, Duplicator uses the uniquely paired previously used first-coordinate value. If it is a fresh coordinate, Duplicator selects a fresh coordinate on the other side. Such a value exists: if a side has fewer than \(q\) values, its counterpart has exactly the same cardinality, hence the same number of unused values; if it has at least \(q\) values, then before the next of at most \(q\) moves fewer than \(q\) different values have been used. Apply the same procedure independently to the second coordinate. The resulting pair is a valid vertex, and the invariant survives. This argument works whichever graph Spoiler chooses and handles repeated vertices automatically. Since equality and adjacency of two graph vertices are determined by the two coordinate-equality patterns, the selected-vertex map is a partial graph isomorphism after \(q\) rounds. The Ehrenfeucht–Fraïssé theorem gives \(\equiv_q\).

**Normal form, class count and sharpness.** For \(2\le a\le b\le q\), the conjunction of \(I_a\), \(C_b\), and, where \(a<q\) or \(b<q\), respectively \(\neg I_{a+1}\) or \(\neg C_{b+1}\), identifies exactly the rank-\(q\) class with truncated sides \((a,b)\). Every conjunct has rank at most \(q\). A given rank-\(q\) sentence is constant on each such class, so taking the disjunction of the identifying formulas for precisely those classes on which it is true supplies the claimed Boolean normal form. There are \(\binom q2\) choices of \((a,b)\). For the class \((q,q)\), any representative has each side at least \(q\), hence at least \(q^2\) vertices; \(R_{q,q}\) attains this bound. Finally, when two sorted side pairs differ, the least index \(t\) at which their threshold vectors disagree is the formula displayed above. The Duplicator strategy proves no smaller rank distinguishes them; \(I_t\) or \(C_t\) achieves rank \(t\), proving optimality.

## Verification

Run `python3 rook_rank_verifier.py` from the directory containing this result's source file. The standalone checker computes full finite atomic-extension types recursively in two ways. Its orbit compression records row/column first-appearance patterns; a separate direct computation enumerates the actual graph vertices. The orbit checker tested every unordered side pair between \(2\) and \(7\) for quantifier ranks \(2\) through \(5\), recovering respectively \(1,3,6,10\) classes. Direct vertex-level recursion independently checked every unordered side pair between \(2\) and \(4\) through rank \(4\); additional exhaustive clique and independent-set tests covered those small graphs. The recorded output is `rook_rank_verifier_output.txt`. These finite checks are supplementary: the coordinate strategy proves the assertion for all dimensions and all ranks.

## Relationship to prior work

Pikhurko, Veith and Verbitsky introduce and analyze minimum quantifier depth distinguishing pairs of finite graphs and establish broad bounds; their 2003 preprint does not state the exact rook-graph depth formula or its rank-preserving Boolean threshold normal form. Pikhurko and Verbitsky's 2010 survey discusses Ehrenfeucht–Fraïssé methods and nonalternating logic generally, without stating these Cartesian-clique-product equivalence classes. Gray and Macpherson's study of connected-homogeneous graphs includes line graphs of complete bipartite graphs and their infinite analogues, but concerns structural homogeneity rather than finite-size first-order equivalence at every rank. The classic Feferman–Vaught product viewpoint motivates comparison, yet does not directly identify a sharp graph-reduct rank-preserving threshold in the binary adjacency signature.

## Limitations

The equivalence and sentence normal form are relative to rectangular rook graphs with both sides at least two, and to ordinary first-order sentences in the graph-only language. No assertion is made for arbitrary graph classes, higher Cartesian products, row/column-labelled expansions, counting logic, finite-variable logic at unbounded depth, or formulas with free variables. The proof is self-contained, but the absence of an equivalent older argument in all historical literature has not been certified; the normal form may be derivable from broader results not identified in the inspected material. Independent mathematical validation has not been performed.

## References

1. O. Pikhurko, H. Veith and O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041, first posted 4 November 2003, https://arxiv.org/abs/math/0311041.
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first posted 25 March 2010, https://arxiv.org/abs/1003.4865.
3. R. Gray and D. Macpherson, *Countable Connected-Homogeneous Graphs*, Journal of Combinatorial Theory, Series B 100 (2010), 97–118, doi:10.1016/j.jctb.2009.04.002.
