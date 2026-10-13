# Semipaired domination polynomial of crown graphs
## Finding
Let \\(\\operatorname{Cr}_n=K_{n,n}-M\\) be the crown graph for \\(n\\ge3\\), with bipartition \\(A=\\{a_1,\\ldots,a_n\\}\\), \\(B=\\{b_1,\\ldots,b_n\\}\\), and deleted perfect matching \\(M=\\{a_i b_i:1\\le i\\le n\\}\\). A vertex set is semipaired dominating if and only if it is a dominating set of even cardinality at least \\(4\\).

Let
\\[
D_n(z)=2z^n+\\big((1+z)^n-1-nz\\big)^2+n z^2\\big(2(1+z)^{n-1}-1\\big).
\\]
Then \\(D_n(z)\\) is the ordinary domination polynomial and
\\[
P_{pr2}(\\operatorname{Cr}_n;z)=\\frac{D_n(z)+D_n(-z)}2-nz^2.
\\]
Consequently
\\[
\\gamma_{pr2}(\\operatorname{Cr}_n)=4,
\\]
the number of minimum semipaired dominating sets is
\\[
\\binom n2^2+2n\\binom{n-1}2+2\\mathbf 1_{\\{n=4\\}},
\\]
and the total number of semipaired dominating sets is
\\[
2^{2n-1}-(n+2)2^{n-1}+n^2-2n+2+(-1)^n.
\\]

## Assumptions and scope
A semipaired dominating set in a graph without isolated vertices is a dominating set \\(S\\) whose vertices can be partitioned into two-element blocks so that the two vertices in every block have graph distance at most \\(2\\). The polynomial \\(P_{pr2}(G;z)\\) counts semipaired dominating sets by cardinality.

## Proof
Write \\(a=|S\\cap A|\\) and \\(b=|S\\cap B|\\). If \\(b=0\\), an omitted vertex of \\(A\\) has no selected neighbor, so domination forces \\(S=A\\); symmetrically, \\(a=0\\) forces \\(S=B\\). If \\(a,b\\ge2\\), every omitted vertex has a selected opposite-side neighbor different from its deleted-matching mate, so \\(S\\) dominates. If \\(a=1\\), say \\(S\\cap A=\\{a_i\\}\\), domination is equivalent to \\(b_i\\in S\\); the case \\(b=1\\) is symmetric. These disjoint cases yield
\\[
D_n(z)=2z^n+\\big((1+z)^n-1-nz\\big)^2+n z^2\\big(2(1+z)^{n-1}-1\\big).
\\]

For \\(n\\ge3\\), distinct vertices on the same side have distance \\(2\\), nonmatched opposite-side vertices have distance \\(1\\), and \\(d(a_i,b_i)=3\\). Hence the only forbidden semipartner pairs inside a selected set are selected deleted-matching pairs; those forbidden pairs form a matching.

Every even selected set of size at least \\(4\\) admits a legal partition. With no forbidden pair, pair arbitrarily. With exactly one forbidden pair \\(\\{x_1,y_1\\}\\), choose two other vertices \\(u,v\\), pair \\(x_1\\) with \\(u\\) and \\(y_1\\) with \\(v\\), then pair the remainder arbitrarily. With at least two forbidden pairs \\(\\{x_i,y_i\\}\\), cyclically pair \\(x_i\\) with \\(y_{i+1}\\), and pair all remaining vertices arbitrarily. Every constructed pair has distance at most \\(2\\).

The only dominating sets of size \\(2\\) are the deleted-matching pairs \\(\\{a_i,b_i\\}\\), and these have distance \\(3\\), so none is semipaired. Therefore semipaired dominating sets are exactly the even dominating sets of size at least \\(4\\). Taking the even part of \\(D_n(z)\\) and removing the \\(n\\) size-two matched pairs proves the polynomial formula.

For the minimum coefficient, a \\(2+2\\) split contributes \\(\\binom n2^2\\). A \\(3+1\\) split must contain the singleton's matched opposite-side vertex, contributing \\(2n\\binom{n-1}2\\). An all-one-side four-set dominates only when \\(n=4\\), contributing two more. Evaluating the polynomial at \\(z=1\\) gives the total-set formula.

## Verification
The included checker constructs \\(\\operatorname{Cr}_n\\) for \\(3\\le n\\le8\\), enumerates every vertex subset, checks domination from adjacency, and checks semipairability by exact perfect-matching search in the distance-at-most-two partner graph. It compares the complete cardinality histogram, minimum value, minimum-set count, and total-set count with the theorem.

## Relationship to prior work
Semipaired domination was introduced in 2018 as a relaxation of paired domination. The introducing paper establishes general inequalities and studies relations with ordinary and total domination. A later full-text primary paper proves NP-completeness even for bipartite graphs and gives algorithms for interval graphs and trees; targeted full-text searches found no crown-graph or complete-bipartite specialization.

A 2021 continuation studies subclasses of chordal graphs and records Mathematics Subject Classification \\(05C69\\); its inspected material likewise contains no crown-graph formula. The exact crown theorem therefore supplies a closed tractable benchmark inside a graph class for which the general optimization problem is computationally hard.

The closest same-family results retrieved concern paired or restrained domination. These do not imply the theorem: paired domination requires partner distance \\(1\\), whereas restrained domination constrains the complement. Here the deleted perfect matching is exactly the set of distance-\(3\) partner obstructions, so semipaired feasibility collapses to an exact parity condition above size two.

## Limitations
The theorem concerns crown graphs \\(K_{n,n}-M\\) with \\(n\\ge3\\); it does not address arbitrary deleted matchings or unequal bipartite graphs. The exhaustive computation through \\(n=8\\) is corroborative only; the arbitrary-order result is analytic. The full text of the 2018 introducing article was unavailable through the accessible lawful route; its institutional metadata and abstract were inspected, while detailed same-parameter comparison used later full-text primary sources. A differently phrased or non-indexed crown-specific result may remain a literature risk.

## References
1. T. W. Haynes, M. A. Henning, “Semipaired Domination in Graphs,” Journal of Combinatorial Mathematics and Combinatorial Computing 104 (2018), 93–109; institutional record publication date 1 February 2018.
2. M. A. Henning, A. Pandey, V. Tripathi, “Complexity and Algorithms for Semipaired Domination in Graphs,” arXiv:1904.00964v1, 1 April 2019; later Theory of Computing Systems, DOI 10.1007/s00224-020-09988-3.
3. M. A. Henning, A. Pandey, V. Tripathi, “Semipaired Domination in Some Subclasses of Chordal Graphs,” Discrete Mathematics & Theoretical Computer Science 23:1 (2021), DOI 10.46298/dmtcs.6782.
