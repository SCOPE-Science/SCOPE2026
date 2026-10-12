# Packing-isolating sets of all graphs of maximum degree two

## Finding

A **packing-isolating set** of a finite simple graph \(G\) is a subset \(S\subseteq V(G)\) that is simultaneously a packing (distinct elements have disjoint closed neighborhoods) and an isolating set (the graph induced by \(V(G)\setminus N[S]\) contains no edge). Put
\[
I_G(z)=\sum_{S\text{ packing-isolating}}z^{|S|}.
\]
The empty set is permitted whenever it satisfies the definitions.

**Theorem.** If \(\Delta(G)\le2\), with path components \(P_{n_1},\ldots,P_{n_u}\) and cycle components \(C_{m_1},\ldots,C_{m_v}\), then
\[
\boxed{I_G(z)=\prod_{i=1}^{u}p_{n_i}(z)\prod_{j=1}^{v}c_{m_j}(z),}
\]
where the component polynomials have the exact bivariate generating functions
\[
\boxed{\sum_{n\ge1}p_n(z)x^n=x+\frac{zx(1+x+x^2)^2}{1-z(x^3+x^4)}}
\]
and
\[
\boxed{\sum_{n\ge3}c_n(z)x^n=\frac{z(3x^3+4x^4)}{1-z(x^3+x^4)}.}
\]
Here the first term \(x\) in the path generating function accounts for the empty packing-isolating set of the isolated-vertex graph \(P_1\).

Equivalently, with \(\binom ab=0\) unless \(0\le b\le a\),
\[
p_1(z)=1+z,
\]
\[
p_n(z)=\sum_{k\ge1}z^k
\sum_{a=0}^2\sum_{b=0}^2
\binom{k-1}{n-3k+2-a-b}
\qquad(n\ge2),
\]
and
\[
c_n(z)=\sum_{\substack{a,b\ge0\\3a+4b=n}}
\frac{n}{a+b}\binom{a+b}{a}z^{a+b}
\qquad(n\ge3).
\]

There exists a packing-isolating set in \(G\) **if and only if no connected component is \(C_5\)**. When it exists, the possible cardinalities form an unbroken integer interval. The componentwise endpoints are
\[
\begin{array}{c|c|c}
\text{component}&\text{minimum size}&\text{maximum size}\\\hline
P_1&0&1\\
P_n,\ n\ge2&\lceil(n-1)/4\rceil&\lfloor(n+2)/3\rfloor\\
C_n,\ n\ge3&\lceil n/4\rceil&\lfloor n/3\rfloor
\end{array}
\]
(the cycle interval is empty exactly for \(n=5\)). For disconnected \(G\), add the component minima and maxima.

## Assumptions and scope

Graphs are finite, simple, and undirected, and may be disconnected. A path \(P_n\) has \(n\ge1\) vertices. A cycle \(C_n\) has \(n\ge3\) vertices. The empty graph has \(I_G(z)=1\). In a packing, \(N[u]\cap N[v]=\varnothing\) for every distinct \(u,v\in S\), equivalent to pairwise graph distance at least \(3\) within a component. An isolating set requires that there be no edge with both endpoints outside \(N[S]\). The polynomial counts vertex subsets, not colorings or ordered tuples.

## Proof

**Path classification.** Number the vertices of \(P_n\) consecutively, and write a nonempty selected set as
\[
S=\{i_1<i_2<\cdots<i_k\}.
\]
The packing condition is exactly \(i_{j+1}-i_j\ge3\) for all consecutive selected indices. The uncovered vertices strictly between the closed neighborhoods of two consecutive selected vertices are
\[
i_j+2,i_j+3,\ldots,i_{j+1}-2,
\]
a run of length \(i_{j+1}-i_j-3\). The isolation condition demands that this run have length at most one, so \(i_{j+1}-i_j\le4\). Thus every internal gap equals \(3\) or \(4\).

The uncovered initial run has length \(i_1-2\) when positive, and the final run has length \(n-i_k-1\) when positive. These contain no edge exactly when
\[
0\le i_1-1\le2,
\qquad 0\le n-i_k\le2.
\]
Therefore the gap and endpoint conditions are simultaneously necessary and sufficient. For \(P_n\) with \(n\ge2\), the empty set does not isolate the existing edge; for \(P_1\), both the empty set and the singleton are allowed.

Put \(a=i_1-1\) and \(b=n-i_k\). There are \(k-1\) internal gaps, each of length \(3\) or \(4\). If exactly \(t\) gaps have length \(4\), then
\[
n=a+b+1+3(k-1)+t,
\]
so \(t=n-3k+2-a-b\). The number of such gap words is \(\binom{k-1}{t}\). Summing over \(a,b\in\{0,1,2\}\) proves the explicit polynomial formula. The generating-function construction starts with one selected vertex, uses two independent endpoint choices from \(1+x+x^2\), and adds each subsequent selected vertex at a gap of \(3\) or \(4\), giving
\[
\frac{zx(1+x+x^2)^2}{1-z(x^3+x^4)}.
\]
Adding the empty set of \(P_1\) proves the path generating function.

**Cycle classification.** For \(C_n\), write the selected vertices in cyclic order and let their successive cyclic arc lengths be \(d_1,\ldots,d_k\), with \(\sum_j d_j=n\). If \(k\ge2\), packing forces \(d_j\ge3\) for every arc. The vertices outside the closed neighborhoods within one arc form a contiguous run of \(d_j-3\) vertices. Hence isolation is equivalent to \(d_j\le4\). Thus all cyclic gaps are \(3\) or \(4\). If \(k=1\), the complement of the chosen vertex's closed neighborhood is a path on \(n-3\) vertices, edgeless exactly when \(n=3\) or \(n=4\). These are precisely the one-gap cyclic words of length \(3\) or \(4\). The empty set never isolates a cycle.

Suppose \(a\) cyclic gaps have length \(3\) and \(b\) have length \(4\). Then \(3a+4b=n\) and \(k=a+b\). To count selected subsets, mark a selected starting vertex (\(n\) choices), choose the order of the \(a\) and \(b\) cyclic gaps (\(\binom{k}{a}\) choices), and divide by the \(k\) choices of marked vertex within each selected subset. This yields exactly
\[
\frac{n}{k}\binom{k}{a}.
\]
Summing gives \(c_n(z)\). Equivalently, let \(T=x^3+x^4\). The logarithmic identity
\[
\sum_{k\ge1}\frac{z^kT^k}{k}=-\log(1-zT)
\]
counts cyclic gap words after marking one graph vertex by applying \(x\frac{d}{dx}\). This gives
\[
\sum_{n\ge3}c_n(z)x^n
=x\frac{d}{dx}[-\log(1-z(x^3+x^4))]
=\frac{z(3x^3+4x^4)}{1-z(x^3+x^4)}.
\]

**Existence and spectra.** For a cycle of order \(n\), a selected set of cardinality \(k\) exists exactly when
\[
3k\le n\le4k.
\]
Indeed, choose \(n-3k\) of the \(k\) gaps to be \(4\) and the rest \(3\). Thus \(\lceil n/4\rceil\le k\le\lfloor n/3\rfloor\). The interval is empty among \(n\ge3\) only at \(n=5\). In a path with \(n\ge2\), the endpoint slack \(a+b\) can be every integer from \(0\) to \(4\) and the number of longer internal gaps can be every integer from \(0\) to \(k-1\); hence a selected set of size \(k\) exists exactly when
\[
3k-2\le n\le4k+1.
\]
This gives the stated path interval.

Finally, a graph with maximum degree at most \(2\) is a disjoint union of paths and cycles. Both packing and isolation hold independently inside each connected component. The polynomial therefore factors, and the attainable cardinalities add. Sums of consecutive integer intervals remain intervals, proving the disconnected assertion and the unique obstruction.

## Verification

The standalone Python script `artifacts/verify.py` constructs paths and cycles from their edge lists, enumerates vertex subsets, and evaluates the packing and isolation definitions directly using closed-neighborhood bitmasks and the edges remaining outside the union. It independently computes the claimed coefficient formulas and checks equality coefficient by coefficient. It also checks every unordered disjoint-union component profile of total order at most \(9\).

Replay output:

`ALL CHECKS PASSED; graphs_checked=221; vertex_subsets_examined=577328; connected_paths_and_cycles_n=1..17; all_multicomponent_profiles_total_order<=9`

The finite checks corroborate, but do not establish, the universal claim. All orders and disjoint unions follow from the gap proof.

## Relationship to prior work

Boyer, Goddard, and Henning (first public June 16, 2026) introduced the question of sets simultaneously packing and isolating into a recent comparative study. Their Theorem 2 shows every tree has such a set; their Section 3 identifies \(C_5\) as an obstruction and proves NP-hardness of general existence. This paper does not enumerate packing-isolating sets of paths or cycles, classify the maximum-degree-two family, or give either generating function above. Our existence theorem isolates \(C_5\) as the **only component obstruction when \(\Delta(G)\le2\)** and counts every feasible set.

Bujtás, Iršič Chenoweth, Klavžar, and Zhang give a complete existence/minimum classification for sets simultaneously distance-\(d\) dominating and \(p\)-packing on cycles. Their Theorem 3.1 uses cyclic gaps between \(p+1\) and \(2d+1\), so its \(d=p=2\) case allows gaps \(3,4,5\). Our isolating requirement excludes gap \(5\); for example, the singleton of \(C_5\) is distance-\(2\) dominating and a packing but is not isolating. Thus their result neither implies the obstruction nor the counts here.

Additional searches used the aliases “\(2\)-packing vertex-edge domination” and “packing vertex-edge dominating set.” Ordinary independent vertex-edge domination imposes only adjacency avoidance, whereas packing requires disjoint closed neighborhoods, so those two notions are not interchangeable.

## Limitations

The theorem is restricted to graphs with maximum degree at most \(2\), and does not claim an analogous obstruction list for subcubic graphs. Although the counting formulas are complete and elementary to replay, their novelty is assessed through accessible published sources and database searches, not guaranteed by a failed keyword search. Literature under other names may exist. The coefficients enumerate labeled vertex subsets of a given graph, not graph-isomorphism orbits.

## References

1. G. Boyer, W. Goddard, and M. A. Henning, “On the Relationships between Domination, Isolation, and Packing,” arXiv:2606.18172v1 (June 16, 2026), MSC \(05C69\). Primary arXiv record: https://arxiv.org/abs/2606.18172 ; author-uploaded full text: https://www.researchgate.net/publication/407171402_On_the_Relationships_between_Domination_Isolation_and_Packing .
2. C. Bujtás, V. Iršič Chenoweth, S. Klavžar, and G. Zhang, “The \(d\)-distance \(p\)-packing domination number: complexity, cycles, and trees,” arXiv:2507.18272v1 (July 24, 2025); *Aequationes Mathematicae* 100 (2026), article 25, DOI 10.1007/s00010-026-01266-w.
3. J. R. Lewis, S. T. Hedetniemi, T. W. Haynes, and G. H. Fricke, “Vertex-edge domination,” *Utilitas Mathematica* 81 (2010), 193–213 (terminology background).
