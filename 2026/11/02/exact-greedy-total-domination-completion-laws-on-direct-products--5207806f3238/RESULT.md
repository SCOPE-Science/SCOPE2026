# Exact greedy total-domination completion laws on direct products of complete graphs

## Finding

Let \(m,n\ge2\) be integers and let \(Q_{m,n}=K_m\times K_n\), with vertices the ordered pairs \((r,c)\in[m]\times[n]\) and adjacency precisely when both coordinates differ. A *completed legal total-dominating sequence* is an ordered sequence of distinct vertices in which each newly chosen vertex has an open neighbor not adjacent to any earlier chosen vertex, and the final selected vertices totally dominate the graph. Let \(T_{m,n}(z)\) be the polynomial counting these completed sequences by their length, with each distinct order counted separately.

The complete polynomial is
\[
\boxed{T_{m,n}(z)=m n(m-1)(n-1)(m-2)(n-2)z^3+3m n(m-1)^2(n-1)^2(m+n-2)z^4.}
\]
In particular, all completed sequences have length three or four; length three is possible precisely when \(m,n\ge3\). The largest length is four for all \(m,n\ge2\). The scalar length statements follow from the known theory, and the new object here is the ordered completion distribution.

Among the length-four completed sequences, precisely
\[
\boxed{24\left[\binom m2\binom n2^2+\binom n2\binom m2^2-\binom m2\binom n2\right]}
\]
have an *inclusion-minimal* underlying total dominating four-set. The remaining, genuinely redundant, completed sequences number
\[
\boxed{3m n(m-1)(n-1)(m-2)(n-2)(m+n).}
\]
Thus length-four legal completion can select a redundant underlying total dominating set if and only if \(m,n\ge3\).

Consider two probability distributions: (U) draw uniformly from all completed legal ordered sequences, and (G) begin with the empty sequence and repeatedly choose uniformly among all currently legal next vertices, stopping as soon as all vertices are totally dominated. The respective probabilities of finishing after exactly three choices are
\[
\boxed{p_U(m,n)=\frac{(m-2)(n-2)}{(m-2)(n-2)+3(m-1)(n-1)(m+n-2)}}
\]
and
\[
\boxed{p_G(m,n)=\frac{(m-1)(n-1)(m-2)(n-2)}{(mn-1)(mn-2)}.}
\]
For square factors \(m=n=q\to\infty\), \(p_U(q,q)\to0\) but \(p_G(q,q)\to1\). Therefore uniformly sampling *completed histories* favors four steps, while uniformly choosing each next legal move favors three steps. Their expected completion lengths tend to four and three, respectively.

## Assumptions and scope

The graph is finite, simple, labeled, and has two complete-graph factors of orders at least two. Total domination uses open neighborhoods, not closed neighborhoods. A legal next choice must newly cover at least one vertex; repeated vertices are automatically illegal. The sampling rules (U) and (G) are distinct and must not be interchanged. No factor of order one is included.

## Proof

**Uncovered-cross reduction.** For a cell \(v=(r,c)\), write \(C(v)=\{(i,j):i=r\text{ or }j=c\}\). Because adjacency requires *both* coordinates to differ, the open neighborhood of \(v\) is the complement of \(C(v)\). After the first \(k\) selected cells, the still-undominated set is exactly the intersection of their crosses. Selecting another cell is legal precisely when this intersection strictly decreases, and the sequence is complete precisely when it becomes empty.

**The first two steps.** Every first choice is legal. Every other cell is a legal second choice: with the first cross \(C(r_1,c_1)\), the second cross is a proper restriction whenever the cells differ. If the first two cells share a row, the remaining undominated set is that entire row, of size \(n\); if they share a column it is that entire column, of size \(m\). Otherwise it is the pair of opposite corners \((r_1,c_2)\), \((r_2,c_1)\) of their two-by-two rectangle. The undominated set is always nonempty, so two moves never suffice.

**Three- and four-step counts.** For two cells in the same row, there are \(mn(n-1)\) ordered initial pairs. A legal third vertex must lie outside that row; there are \((m-1)n\) choices, and it leaves exactly one undominated cell. The final legal fourth vertex must differ in both coordinates from that cell; there are \((m-1)(n-1)\) choices. The same-column calculation interchanges \(m\) and \(n\).

For an initial pair differing in both coordinates, of which there are \(mn(m-1)(n-1)\), the remaining two cells are opposite corners. A third cell whose cross avoids *both* corners completes the sequence; it must lie outside both used rows and both used columns, giving exactly \((m-2)(n-2)\) choices. A third cell whose cross contains exactly one corner leaves a singleton. Each corner belongs to \(m+n-1\) crosses, and exactly two crosses contain both corners, namely those centered on the original selected pair. Hence exactly \(2(m+n-3)\) third vertices are legal but nonterminal. Any resulting singleton can be eliminated by exactly \((m-1)(n-1)\) choices of a fourth cell. There are no longer legal sequences, because every legal third move leaves at most one undominated cell.

It follows that the number of length-three completions is \(mn(m-1)(n-1)(m-2)(n-2)\). The number of length-four completions is
\[
(m-1)(n-1)\big[ mn(n-1)(m-1)n+mn(m-1)m(n-1)+mn(m-1)(n-1)2(m+n-3)\big],
\]
which simplifies to \(3mn(m-1)^2(n-1)^2(m+n-2)\). Every counted fourth move is distinct from all earlier moves: any earlier move's cross contains the surviving undominated cell, whereas the required final cross must omit it.

**Inclusion-minimal versus redundant four-sets.** The same crossed-neighborhood argument shows that three cells totally dominate if and only if they lie in three distinct rows and three distinct columns. Consequently, an inclusion-minimal total dominating four-set can contain no three-cell matching in the associated bipartite incidence graph of selected rows and columns. By the elementary bipartite matching-cover theorem, its four chosen edges are covered by at most two row/column vertices. A cover consisting of one row and one column is impossible: their intersection cell has no selected neighbor. With a cover of two rows, total domination holds exactly when each row contains at least two chosen cells, hence exactly two each. Similarly, the only other possibility is two chosen cells in each of two columns. Conversely, each of these four-sets is total dominating and becomes non-dominating after any deletion.

The two-row family has \(\binom m2\binom n2^2\) members, the two-column family has \(\binom n2\binom m2^2\), and their intersection consists exactly of the \(\binom m2\binom n2\) complete two-by-two rectangles. Let their union size be \(M_4\). Every ordering of a minimal total dominating four-set is legal: if a member \(v\) is deleted, some vertex becomes undominated by the rest, so \(v\) has a private neighbor that it newly covers irrespective of where \(v\) appears in an ordering. Hence there are exactly \(4!M_4\) legal four-step completions with minimal underlying set. Subtraction from the total count and factorization gives
\[
3mn(m-1)(n-1)\big[(m-1)(n-1)(m+n-2)-m(m-1)-n(n-1)+2\big]
=3mn(m-1)(n-1)(m-2)(n-2)(m+n).
\]
This count is positive precisely when both factors have order at least three.

**The two probability laws.** Under (U), divide the length-three coefficient by the sum of the two coefficients. Under (G), the second chosen cell differs in both coordinates from the first with probability \((m-1)(n-1)/(mn-1)\). Only then can three choices suffice. There are \(mn-2\) legal third choices and exactly \((m-2)(n-2)\) complete at that choice; multiplying these probabilities gives \(p_G\). For \(m=n=q\),
\[
p_U(q,q)=\frac{(q-2)^2}{(q-2)^2+6(q-1)^3},\qquad
p_G(q,q)=\frac{(q-1)^2(q-2)^2}{(q^2-1)(q^2-2)}.
\]
The first tends to zero and the second to one, proving the claimed opposite asymptotic biases.

## Verification

A separate standard-library Python checker constructs each graph directly from the adjacency rule, enumerates all ordered legal sequences under the original open-neighborhood predicate, independently enumerates inclusion-minimal total dominating four-sets, and evaluates the uniform-next-legal-choice probability by exact rational dynamic programming. It reproduces all coefficients and redundancy counts for every \(2\le m\le n\le6\): 15 dimension pairs and 1,469,556 terminal ordered sequences in total, including 1,438,200 length-four sequences. This finite verification is a consistency test and is not the proof for all orders. The source file is `total_sequence_checker.py`, with a corresponding exact `CHECK_RESULTS.json` output.

## Relationship to prior work

Brešar, Henning, and Rall introduced total dominating sequences and the longest-length parameter. Brešar et al. subsequently investigated direct products and explicitly discussed the known maximum length for products of complete graphs. These scalar conclusions are not claimed as new. The three-cell minimum configuration count and the auxiliary minimal-four-set classification are also not asserted as novel; they are independently established here only to support the ordered-history comparison. What is assessed is the complete *ordered* two-term sequence-count polynomial, the exact count of length-four histories with redundant final sets, and the opposite limiting probabilities under two explicitly different sampling laws. The inspected published statements give length bounds or graph-structure classifications, not these ordered counts or sampling comparisons.

## Limitations

The theorem applies to two complete factors with both orders at least two; extensions to more factors or arbitrary graph products are not established. The calculation concerns sequences that stop at first total domination, not arbitrary prematurely stopped legal prefixes or weighted/nonuniform greedy rules. Full publication-priority certainty is not claimed: differently formulated sequence-enumeration results might exist outside the inspected sources. The exact computations validate finite instances only. Independent mathematical validation has not been performed.

## References

1. B. Brešar, M. A. Henning, and D. F. Rall, *Total Dominating Sequences in Graphs*, arXiv:1601.07525 (first posted 2016-01-27).
2. B. Brešar, Cs. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Zs. Tuza, and M. Vizer, *On Grundy Total Domination Number in Product Graphs*, arXiv:1712.08780 (first posted 2017-12-23); see especially Section 2.
3. S. Bahadır, D. Gözüpek, and O. Doğan, *Total \(k\)-Uniform Graphs*, arXiv:2010.08368 (2020); the abstract was consulted as related context.
