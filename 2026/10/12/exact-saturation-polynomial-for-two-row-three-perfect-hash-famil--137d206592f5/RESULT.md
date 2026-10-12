# Exact saturation polynomial for two-row three-perfect hash families

## Finding

Fix an integer \(q\geq 3\). A *two-row strength-three perfect hash family* is a set \(C\subseteq[q]^2\) such that, for every three distinct columns of the corresponding \(2\times |C|\) array, at least one of the two rows contains three distinct symbols. The family is *inclusion-maximal* when no additional column from \([q]^2\) can be adjoined while retaining this property. Distinct labels in the two rows are fixed, the row order is fixed, and permutations of the columns do not make new families.

Let \(M_q(z)=\sum_C z^{|C|}\), summed over all inclusion-maximal families on these labels. Put
\[
H(x,y)=xy+x(e^y-1-y)+y(e^x-1-x),
\]
and let \(S_{\geq2}(q,k)\) be the number of partitions of a labeled \(q\)-element set into \(k\) nonempty blocks, each of size at least two. Then **for every \(q\geq3\)**,
\[
\boxed{M_q(z)=(q!)^2\sum_{k=2}^{q}\frac{z^{2q-k}}{k!}[x^q y^q]H(x,y)^k
+2z^q\sum_{k=1}^{\lfloor q/2\rfloor}\frac{q!}{(q-k)!}S_{\geq2}(q,k).}
\]
Every integer cardinality from \(q\) through \(2q-2\) occurs among inclusion-maximal families. In particular, their minimum cardinality is \(q\), their maximum is \(2q-2\), and exactly \(q^2\) labeled families attain the maximum. The ratio of smallest to largest terminal cardinality tends to \(1/2\). The exact first polynomials are
\[
\begin{aligned}
M_3(z)&=12z^3+9z^4,\\
M_4(z)&=104z^4+144z^5+16z^6,\\
M_5(z)&=530z^5+1800z^6+1000z^7+25z^8,\\
M_6(z)&=5832z^6+21600z^7+36900z^8+4500z^9+36z^{10}.
\end{aligned}
\]

## Assumptions and scope

The property quantifies over **all triples of distinct columns**. A family is a set, so duplicate columns do not occur. Inclusion-maximality is distinct from having greatest possible cardinality. Both rows use a common alphabet of size \(q\), and all \(q^2\) pairs are potential additions. The polynomial counts literal unordered column sets with fixed row and symbol labels, not equivalence classes under permutations. The theorem makes no assertion for three or more rows, for strength four, or for non-square row alphabets.

## Proof

**Step 1 (forbidden paths).** Interpret column \((i,j)\) as edge \(ij\) of the complete bipartite graph with vertex sides \([q]_L\) and \([q]_R\). Three distinct edges fail the hash condition exactly when the three first endpoints are not all distinct *and* the three second endpoints are not all distinct. Among three distinct bipartite edges this means that one pair shares a left endpoint and a different pair shares a right endpoint. Equivalently the three edges form a (not necessarily induced) path with three edges, \(P_4\). Consequently a hash family is precisely a \(P_4\)-free bipartite edge set, which is precisely a star forest (a disjoint union of isolated vertices and components \(K_{1,d}\), \(d\geq1\)). For the last equivalence, any connected bipartite component that is not a star contains an edge joining two vertices of degree at least two or a shortest path of length at least three; either produces a \(P_4\).

**Step 2 (all inclusion-maximal families).** A star forest with no isolated vertices is inclusion-maximal: every absent bipartite edge connects two different nontrivial components, and a neighbor of each endpoint together with this edge forms a \(P_4\). There are at least two components when \(q\geq2\). Conversely, suppose a maximal star forest has an isolated left vertex. It cannot have an isolated right vertex, since the edge joining those isolates can be added. Every right vertex must be a degree-one leaf attached to a left center of degree at least two. Indeed, adjoining an edge from an isolated left vertex to a right vertex leaves a star forest unless that right vertex is a leaf of such a left-centered star. This necessity is also sufficient: an edge from an isolated left vertex to a leaf creates a \(P_4\) through a second leaf; every other absent edge joins two different components with no isolated endpoint and also creates a \(P_4\). There is a symmetric type with isolated right vertices. These three types—spanning star forests, left-isolate star collections, and right-isolate star collections—are exhaustive and disjoint.

**Step 3 (spanning-family enumerator).** A star-forest component with at least one vertex on each side is either one edge, a left-centered star with at least two right leaves, or a right-centered star with at least two left leaves. In the two-sort labeled exponential generating function, their combined contribution is
\[
xy+\sum_{d\geq2}\frac{xy^d}{d!}+\sum_{d\geq2}\frac{yx^d}{d!}=H(x,y).
\]
The labeled exponential formula says that spanning star forests with \(q\) left and \(q\) right vertices and exactly \(k\) components number
\[
\frac{(q!)^2}{k!}[x^q y^q]H(x,y)^k.
\]
Since each component is a tree, such a forest has \(2q-k\) edges. The component number runs from \(2\) to \(q\). Inserting the edge weight gives the first term of \(M_q\).

**Step 4 (isolated-vertex types).** For a left-isolate family with \(k\) nonisolated left centers, choose an unordered set of \(k\) centers in \(\binom qk\) ways, partition the \(q\) labeled right vertices into \(k\) unlabeled blocks of size at least two, and match those blocks to the chosen centers in \(k!\) ways. Thus there are \(\frac{q!}{(q-k)!}S_{\geq2}(q,k)\) families. They all have exactly \(q\) edges, and necessarily \(1\leq k\leq\lfloor q/2\rfloor\). Doubling accounts for right-isolate families and gives the second term. This completes the exact polynomial formula.

**Step 5 (sharp spectrum).** An inclusion-maximal star forest has at least \(q\) edges: spanning forests have \(2q-k\geq q\), while either isolate type has exactly \(q\). A spanning forest has at least two components and hence at most \(2q-2\) edges; isolate types have \(q\). The maximum is attained by two disjoint opposite-oriented stars, one of size \(q-1\) centered on the left and one of size \(q-1\) centered on the right. Their centers may be selected in \(q^2\) ways, and every two-component spanning star forest on both sides is of this form. For any \(q\leq m\leq2q-2\), set \(k=2q-m\) and \(d=q-k+1\). Take a left-centered \(K_{1,d}\), a right-centered \(K_{d,1}\), and \(k-2\) separate edges, on disjoint labeled vertices; this uses exactly \(q\) vertices on each side and \(m\) edges. Thus there are no holes in the possible cardinalities. When \(k=q\), this construction is a perfect matching.

## Verification

The program `saturation_formula.py` independently evaluates the spanning labeled-component recurrence and the no-singleton set-partition recurrence, reporting the complete size polynomials through \(q=8\). The C++ program `brute_maximal.cpp` independently enumerates all subsets of the \(q\times q\) grid for \(q=3,4,5\), pruning those containing a forbidden three-edge path and testing every absent column for extendability. It returns precisely \(21\), \(264\), and \(3355\) maximal families, respectively, with each cardinality distribution identical to the formula. The smallest two sizes, the maximum coefficient, and complete interval support are checked by the formula program through \(q=8\). These finite checks supplement, but do not replace, the proof for arbitrary \(q\).

## Relationship to prior work

Perfect hash families in the standard fixed-row/fixed-alphabet model are described by Walker and Colbourn (2007), who investigate constructions, existence and extremal sizes. Shangguan and Ge (arXiv:1601.04807, first posted January 2016), Theorems 1.5 and 1.7, give bounds and a construction which already entail the **known maximum** \(2q-2\) for two rows and strength three. That maximum is **not** claimed as a new extremal result here. Aoudia, Nguyen, Mahjoub and Aïder (2014) study the general star-forest polytope and maximal star forests in cycles; the graph translation is likewise not a claim of new graph terminology. The present claim is the full characterization and **labeled cardinality polynomial of every inclusion-maximal two-row family**, including nonoptimal terminal families and their counts. No assertion of global bibliographic uniqueness is made.

## Limitations

The theorem is about inclusion-maximal sets, not outcomes under a specified distribution on greedy insertion orders. It does not count isomorphism classes under alphabet relabeling, and it says nothing about hash function running time or security strength. The literature comparison cannot rule out an unindexed equivalent enumeration; the exponential formula itself is standard, and its application here rests on the structural maximality classification.

## References

1. R. A. Walker II and C. J. Colbourn, *Perfect Hash Families: Constructions and Existence*, Journal of Mathematical Cryptology 1 (2007), 125–150, DOI: 10.1515/JMC.2007.008.
2. C. Shangguan and G. Ge, *Separating hash families: A Johnson-type bound and new constructions*, arXiv:1601.04807v1 (posted 2016-01-19), Theorems 1.5 and 1.7; later version arXiv:1601.04807v2.
3. L. Aoudia, V. H. Nguyen, A. R. Mahjoub and M. Aïder, *On the star forest polytope*, CoDIT (2014), pp. 263–268, DOI: 10.1109/CoDIT.2014.6996904.
