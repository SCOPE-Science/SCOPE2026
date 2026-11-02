# Crown-graph fort hypergraphs and an asymptotic threefold zero-forcing gap

## Finding
For each integer \(n\ge3\), let \(G_n\) be the crown graph with indexed bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). For \(S\subseteq[n]\), write \(A_S=\{a_i:i\in S\}\) and \(B_S=\{b_i:i\in S\}\). A fort is a nonempty vertex set having no exterior vertex with exactly one neighbor in it.

**Theorem (complete obstruction and forcing classification).** The inclusion-minimal forts of \(G_n\) are exactly
\[
 A_S\quad(|S|=3),\qquad B_T\quad(|T|=3),\qquad A_U\cup B_U\quad(|U|=2).
\]
There are exactly \(2\binom n3+\binom n2\) such forts; the minimal-fort hypergraph has rank four. The polynomial counting all standard zero-forcing initial sets by their cardinalities is
\[
 \mathcal Z_{G_n}(z)=\sum_{a=0}^{2}\sum_{b=0}^{2}\binom na\binom nb z^{2n-a-b}-\binom n2 z^{2n-4}.
\]
Its smallest nonzero exponent is \(2n-4\), attained exactly \(\binom n2(\binom n2-1)\) times: the minimum zero-forcing sets are precisely the complements of \(A_S\cup B_T\), where \(|S|=|T|=2\) and \(S\ne T\).

Let \(\operatorname{ft}(G)\) denote the maximum number of vertex-disjoint forts and \(Z^*(G)\) the minimum total weight of a fractional fort transversal, with vertex weights in \([0,1]\). Then
\[
 \operatorname{ft}(G_n)=\left\lfloor\frac{2n}{3}\right\rfloor,\qquad Z^*(G_n)=\frac{2n}{3},\qquad Z(G_n)=2n-4.
\]
For \(n\ge4\), the unique optimal fractional transversal assigns weight \(1/3\) to every vertex. Thus
\[
 \lim_{n\to\infty}\frac{Z(G_n)}{Z^*(G_n)}=3.
\]

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled as specified. Standard zero forcing starts with an initially blue set; a blue vertex with exactly one white neighbor changes that neighbor to blue. The process succeeds if every vertex eventually becomes blue. A fort is inclusion-minimal when it contains no proper nonempty fort. The fort number permits arbitrary forts, but each may be shrunk to a minimal one without losing disjointness. A fractional fort transversal satisfies \(\sum_{v\in F}x_v\ge1\) for every fort \(F\), with \(0\le x_v\le1\). Minimal-fort inequalities suffice for both integral and fractional transversal problems.

## Proof
**Neighborhood counts.** Write a candidate fort as \(F=A_S\cup B_T\), with \(s=|S|\) and \(t=|T|\). The number of neighbors in \(F\) of an exterior vertex \(a_i\), where \(i\notin S\), is \(t-\mathbf1_{i\in T}\); for exterior \(b_j\), where \(j\notin T\), it is \(s-\mathbf1_{j\in S}\). Thus the fort condition is exactly the requirement that neither displayed number equal one.

**All minimal forts.** An entire three-subset of one bipartition side is a fort: every exterior vertex on the opposite side sees two or three of its vertices, and exterior vertices on its own side see none. Conversely, a nonempty one-sided subset of size at most two is not a fort when \(n\ge3\): if its size is one, an exterior opposite-side vertex of another index sees exactly one; if its size is two, either opposite-side vertex with one of the selected indices sees exactly one. Therefore the one-sided minimal forts are exactly the triples.

A mixed minimal fort cannot meet either side in at least three vertices, since it would contain a proper one-sided triple fort. Suppose both sides are met, and their selected cardinalities are at most two. If \(s=1\), the condition at exterior vertices \(b_j\) forces \([n]\setminus T\subseteq S\), whence \(t\ge n-1\). As \(t\le2\), this requires \(n=3\) and \(t=2\). In that case \(S=[n]\setminus T\), and either exterior \(a_i\) with \(i\in T\) has one neighbor in \(F\), a contradiction. The case \(t=1\) is symmetric. Hence \(s=t=2\). An exterior \(b_j\) for \(j\in S\setminus T\) would see exactly one selected neighbor; thus \(S\subseteq T\). Symmetrically \(T\subseteq S\), so \(S=T\). Conversely, when \(S=T=U\) and \(|U|=2\), every exterior vertex sees both selected vertices on the opposite side, so this is a fort. It contains no proper fort by the cases already proved. This establishes the complete list and its count.

**All zero-forcing sets.** An initial blue set succeeds precisely when it intersects every fort: a disjoint fort cannot be penetrated by a force, whereas if the process stops with any white vertices, the residual white set is itself a fort. Consequently a set with white vertices \(A_S\cup B_T\) succeeds exactly when it contains no minimal fort among the three classified types. This means \(|S|,|T|\le2\), excluding precisely the case \(|S|=|T|=2\) and \(S=T\). Counting labelled choices of the two white index sets gives the displayed zero-forcing polynomial, all its minimum sets, and \(Z(G_n)=2n-4\).

**Fractional optimum and rigidity.** Every three-subset of side \(A\) gives a transversal inequality. Summing these \(\binom n3\) inequalities, each vertex of \(A\) appears \(\binom{n-1}{2}\) times, so the total weight on \(A\) is at least \(n/3\). Likewise the total weight on \(B\) is at least \(n/3\). The constant assignment \(x_v=1/3\) satisfies every triple constraint with equality and every four-vertex constraint with left-hand side \(4/3\); hence \(Z^*(G_n)=2n/3\). At equality, every triple inequality on each side must be tight. If \(n\ge4\), two triples sharing two vertices imply equality of the two remaining vertex weights; varying the triples forces all weights on a side to be equal, hence each equals \(1/3\). For \(n=3\) uniqueness is false: giving weight one to \(a_1\) and \(b_2\) and zero elsewhere is another optimal fractional transversal.

**Disjoint fort packing.** Every fort has weight at least one under the feasible uniform fractional transversal, so disjoint forts number at most \(\lfloor2n/3\rfloor\). If \(n\equiv0\) or \(1\pmod3\), split each side into \(\lfloor n/3\rfloor\) disjoint triples; these provide \(2\lfloor n/3\rfloor=\lfloor2n/3\rfloor\) disjoint forts. If \(n\equiv2\pmod3\), take one aligned four-vertex fort on two indices and partition the remaining \(n-2\) vertices on each side into triples; this provides \(1+2(n-2)/3=\lfloor2n/3\rfloor\) disjoint forts. This proves the fort-number identity. The integrality-gap limit follows immediately from the established formulas.

## Verification
The accompanying standalone `verify.py` constructs the crown adjacency relation directly and performs exact finite checks. It enumerates every nonempty vertex subset for each \(3\le n\le8\), checks the exterior-neighbor fort predicate, and tests minimality against **all** proper subsets using an exhaustive subset recurrence; the resulting families exactly equal the three types above. For \(3\le n\le7\), it also executes the standard zero-forcing process from every initial set and compares the complete polynomial, computes disjoint-fort packing by an independent exact subset dynamic program, and solves the fractional transversal linear program numerically as corroboration when SciPy is installed. The arithmetic and infinite-domain conclusions follow from the written proof, not the finite checks.

The verified minimal-fort counts for \(n=3,4,5,6,7,8\) are respectively \(5,14,30,55,91,140\). The verified minimum-zero-forcing-set counts for \(n=3,4,5,6,7\) are \(6,30,90,210,420\). The checker terminates with `VERIFY_OK`.

## Relationship to prior work
Cameron, Hogben, Kenter, Mojallal, and Schuerger introduce the fort hypergraph, its fractional transversal, and their connections to zero forcing. They evaluate complete bipartite graphs, for which \(Z^*(K_{n,n})=n\) and \(Z(K_{n,n})=2n-2\). Deleting a perfect matching yields a crown graph, and the present calculation shows that its fractional invariant drops to \(2n/3\) while the integer invariant drops by only two: the limiting integrality gap changes from two to three.

Becker, Cameron, Hanely, Ong, and Previte establish formulas for minimal forts of various graph families, including complete bipartite graphs (their Proposition 9), and constructions for joins, coronas, and vertex sums. Their inspected results do not give the crown-graph minimal-fort hypergraph or its complete forcing enumerator. A published complete-multipartite classification establishes minimal forts of cardinality at most three and a corresponding fractional forcing formula; crown graphs with \(n\ge3\) are **not** complete multipartite, and their aligned four-vertex forts are not covered by that classification. Abiad and Ghasemi Nezhad study minimal-fort abundance and exact tree counting; their accessible abstract does not announce the crown-graph formulas, but the complete manuscript was inaccessible for a decisive text comparison.

## Limitations
The result concerns ordinary, not positive-semidefinite or skew, zero forcing. The graph must be a crown graph with \(n\ge3\), and zero forcing is counted on labelled vertices. The exact theorem is proved without numerical extrapolation. The full text of the 2026 motivating manuscript was not accessible, so historical priority against an unlocated or differently phrased theorem is not certified.

## References
1. A. Abiad and S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing*, arXiv:2609.11754v1, first publicly submitted 2026-09-10. https://arxiv.org/abs/2609.11754
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v3. https://arxiv.org/abs/2310.17904
3. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1. https://arxiv.org/abs/2404.05963
