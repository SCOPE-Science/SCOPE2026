# Fifth-coefficient extremizers for 2-regular triple systems

## Finding

Let \(H=(V,E)\) be a finite simple \(3\)-uniform, \(2\)-regular hypergraph on \(n\ge 9\) vertices. Necessarily \(3\mid n\). Let \(i_3^{(5)}(H)\) be the number of five-element subsets of \(V\) that contain no hyperedge of \(H\). Then

\[
i_3^{(5)}(H)\le \binom{n}{5}-\frac{n(n-3)(n-5)}{3}.
\]

Equality holds if and only if the dual loopless cubic multigraph of \(H\) is a disjoint union of even cycles, each of length at least four, with edge multiplicities alternating between two and one around each cycle. In particular, when \(6\mid n\), this proves the coefficient-wise independent-set bound for the parameter slice \((r,d,k)=(3,2,5)\); the equality family is larger than the single construction made from disjoint copies of \(H_{3,2}\).

## Assumptions and scope

A hypergraph is simple if it has no repeated hyperedges. It is \(3\)-uniform if every hyperedge has three vertices, and \(2\)-regular if each vertex belongs to exactly two hyperedges. An independent set here means a vertex set containing no complete hyperedge (often called a weak independent set). The theorem concerns only independent sets of size five in finite simple \(3\)-uniform, \(2\)-regular hypergraphs with \(n\ge9\). It does not claim a coefficient inequality for other set sizes, uniformities, or degrees.

The dual multigraph \(F(H)\) has one vertex for each hyperedge of \(H\). Every vertex \(v\in V\), which belongs to exactly two hyperedges \(e,f\), becomes one edge joining the dual vertices \(e,f\). Thus \(F(H)\) is loopless and cubic; parallel-edge multiplicity is at most two because \(H\) is simple.

## Proof

Write \(m=|E|\). Counting incidences gives \(3m=2n\), so \(m=2n/3\).

For a five-set \(S\subseteq V\), let \(h(S)=|\{e\in E:e\subseteq S\}|\). Each vertex of \(S\) belongs to at most two hyperedges contained in \(S\), so \(3h(S)\le 10\) and hence \(h(S)\le3\).

Let \(p_2\) be the number of unordered pairs of distinct hyperedges whose intersection has size two, and let \(p_1\) be the number whose intersection has size one. No two distinct hyperedges can share three vertices. Since every vertex belongs to exactly two hyperedges, counting the pairs of hyperedges at each vertex gives

\[
p_1+2p_2=n.
\]

A pair counted by \(p_2\) has a four-vertex union and is contained in exactly \(n-4\) five-sets. A pair counted by \(p_1\) has a five-vertex union and is contained in exactly one five-set. Pairs of disjoint hyperedges are contained in no five-set. Therefore the number of pairwise hyperedge incidences inside five-sets, counted as unordered pairs, is

\[
(n-4)p_2+p_1=n+(n-6)p_2.
\]

Let \(t\) count unordered triples of distinct hyperedges whose union has size five. Since each five-set contains at most three hyperedges, inclusion-exclusion through triples is exact: the number of five-sets containing at least one hyperedge is

\[
m\binom{n-3}{2}-\bigl(n+(n-6)p_2\bigr)+t.
\]

Consequently,

\[
i_3^{(5)}(H)=\binom{n}{5}-m\binom{n-3}{2}+n+(n-6)p_2-t.
\]

A fixed hyperedge can share two vertices with at most one other hyperedge. Otherwise its two intersections of size two would overlap in at least one vertex, putting that vertex in three hyperedges and contradicting \(2\)-regularity. Thus the relation “shares two vertices” is a matching on the \(m\) hyperedges, and

\[
p_2\le \frac m2=\frac n3.
\]

Because \(n\ge9\), the coefficient \(n-6\) is positive. Using \(t\ge0\) and the bound on \(p_2\) yields

\[
\begin{aligned}
i_3^{(5)}(H)
&\le \binom{n}{5}-\frac{2n}{3}\binom{n-3}{2}+n+\frac{n(n-6)}{3}\\
&=\binom{n}{5}-\frac{n(n-3)(n-5)}{3}.
\end{aligned}
\]

Equality requires \(p_2=n/3=m/2\), so every dual vertex is incident with exactly one doubled edge. Since the dual graph is cubic, each vertex has exactly one further incident edge, of multiplicity one. After collapsing each doubled pair to a single support edge, the support graph is a simple graph of degree two, hence a disjoint union of cycles. The two edge types alternate, so every cycle is even and has length at least four; a support cycle of length two would require multiplicity three between the same dual vertices, which simplicity forbids. This structure also forces \(t=0\): a triple counted by \(t\) would give a triangle in the dual with one doubled edge and two single edges, making one of its vertices incident with two single edges and a doubled edge, contrary to degree three.

Conversely, a disjoint union of even cycles with alternating doubled and single edges is loopless and cubic, has maximum edge multiplicity two, and is the dual of a simple \(3\)-uniform, \(2\)-regular hypergraph. Every dual vertex belongs to a doubled pair, so \(p_2=m/2=n/3\), and the preceding argument gives \(t=0\). Equality follows. For every admissible \(n=3k\ge9\), a single alternating cycle of length \(2k\) supplies an equality example, so the bound is sharp.

## Verification

The proof above is exact and applies to every admissible order. A supplementary standard-library Python checker enumerates all 640 labeled loopless cubic multigraphs on six vertices with multiplicities at most two. These are duals of simple \(3\)-uniform, \(2\)-regular hypergraphs on nine vertices. For all 640 cases it checks the inclusion-exclusion identity and the upper bound; the maximum is \(54\), attained by 120 dual multigraphs. The checker also verifies alternating-cycle equality examples at orders \(n=9,12,15\), with independent-five-set counts \(54,540,2403\), respectively. These finite checks corroborate the proof and are not used as a substitute for the all-order argument.

The checker is included at `artifacts/verify_small.py` and uses only the Python standard library.

## Relationship to prior work

Balogh, Bollobás, and Narayanan proposed an extremal conjecture for the total number of independent sets in regular uniform hypergraphs, with a natural quasi-bipartite construction as the candidate maximizer. A later coefficient-wise formulation asks for the corresponding inequality separately at every fixed set size. The recent treatment of this problem proves the fourth-coefficient case for a restricted cross-edge-free class and proves a total-count result for degree-two hypergraphs of odd uniformity; neither total-count inequalities nor the fourth coefficient imply the fifth-coefficient statement here.

A closely related exact result classifies the fourth coefficient for all simple \(3\)-uniform, \(2\)-regular hypergraphs. The present theorem addresses the next coefficient, gives its sharp value, and classifies all equality types. The literature comparison is best-of-knowledge; no claim is made that an exhaustive search can exclude unindexed prior work.

## Limitations

The argument relies on \(2\)-regularity to bound the number of hyperedges inside a five-set and to make pairs sharing two vertices form a matching. It does not settle the coefficient-wise conjecture for other values of \(k\), \(r\), or \(d\), and it does not determine the full independent-set polynomial of a general regular hypergraph. Independent audit and independent validation have not been performed.

## References

1. J. Balogh, B. Bollobás, and B. Narayanan, “Counting independent sets in regular hypergraphs,” arXiv:2002.09995v1, first submitted 23 February 2020; *Journal of Combinatorial Theory, Series A* 180 (2021), 105405. https://arxiv.org/abs/2002.09995v1
2. M. Sarantis, P. Tetali, and Z. Zheng, “On Counting Independent Sets in Regular Hypergraphs,” arXiv:2609.17468v1, first submitted 15 September 2026. https://arxiv.org/abs/2609.17468v1
3. “Fourth-coefficient extremizers for 2-regular triple systems,” public mathematical record, 30 September 2026. https://github.com/Resultary/2026/blob/main/2026/9/30/SCOPE-fourth-coefficient-extremizers-for-2-regular-triple-systems--35d21af925ab/RESULT.md
