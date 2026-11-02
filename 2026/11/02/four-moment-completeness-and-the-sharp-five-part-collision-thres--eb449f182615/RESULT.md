# Four-moment completeness and the sharp five-part collision threshold for metric-graph distance histograms

## Finding
Let \(r\geq2\), let \(a_1,\ldots,a_r\) be positive integers, and let \(G\) be the **unit-edge intrinsic metric graph** of the complete multipartite graph \(K_{a_1,\ldots,a_r}\). Select \(X,Y\) independently by normalized one-dimensional arclength on all edges, and write \(f_G\) for the density of their shortest-path distance \(d_G(X,Y)\). Define the part-size power sums \(P_j=\sum_{i=1}^r a_i^j\), for \(j=1,2,3,4\).

**Theorem.** For any two such graphs, their complete continuous two-point distance distributions agree **if and only if** their four power sums \(P_1,P_2,P_3,P_4\) agree. Four directly observable features of the distance density reconstruct the four sums by the formulas below. Consequently, the distance distribution determines the unordered part sizes among complete multipartite graphs with **at most four parts**. This threshold is sharp: the nonisomorphic **five-partite** metric graphs
\[
K_{1,5,9,17,18}\qquad\text{and}\qquad K_{2,3,11,15,19}
\]
have identical entire two-point intrinsic-distance distributions. Each has \(50\) vertices and \(890\) unit edges, with matching power-sum vector \((50,720,11600,195684)\).

Here is the explicit inversion. Set \(m=|E(G)|\), let \(A\) count ordered pairs of distinct edges sharing a vertex, let \(T\) count ordered pairs of distinct edges sharing a vertex whose other endpoints are adjacent, and let \(H\) be the weighted count of disjoint-edge pairs defined in the proof. The density determines these four numbers without prior knowledge of the graph:
\[
\begin{aligned}
m&=\frac{2}{f_G(0+)},\\
A&=m^2 f'_G(0+)+2m,\\
T&=m^2\bigl(f_G(3/2-)-f_G(3/2+)\bigr),\\
H&=\frac{m^2}{2}f_G(2-).
\end{aligned}
\]
With \(N=P_1\), the recovered power sums are
\[
\begin{aligned}
N&=2+\frac{2A-T}{2m},\\
P_2&=N^2-2m,\\
P_3&=A+N^3-4mN+2m,\\
P_4&=2H-N(N+1)P_2+N^3+2NP_3-2m.
\end{aligned}
\]
All derivatives and one-sided limits refer to the canonical piecewise-linear density on open intervals; pointwise values at the breakpoints are immaterial.

## Assumptions and scope
The underlying abstract graph is finite, simple, connected and complete multipartite, with at least two nonempty parts. Each edge is a **separate unit-length interval** glued at its endpoint vertices, and distance is the intrinsic shortest-path metric rather than Euclidean chord distance or the discrete vertex metric. The sampling measure is total arclength divided by the number of edges \(m\); graph vertices have zero probability. Part sizes are positive integers. Equality of two distance distributions means equality of probability measures, or equivalently equality of their densities almost everywhere. No claim is made for non-multipartite graphs, unequal edge lengths, or local distance-profile data.

## Proof
Write \(N=\sum_i a_i\), \(m=(N^2-P_2)/2\). For independent uniform \(U,V\in[0,1]\), classify an **ordered** pair of selected edges into six types. Types \(S,O,T\) are respectively: the same edge; two different edges sharing a vertex, with nonadjacent other endpoints; and two different edges sharing a vertex, with adjacent other endpoints. Types \(B,C,F\) are disjoint edges whose two unordered pairs of endpoint-part labels have respectively two, one, or zero parts in common. Under consistent endpoint orientations the six conditional shortest-path distances have exactly the following representations:

| Type | Exact conditional distance |
|---|---|
| \(S\) | \(\lvert U-V\rvert\) |
| \(O\) | \(U+V\) |
| \(T\) | \(\min(U+V,3-U-V)\) |
| \(B\) | \(2-\lvert U-V\rvert\) |
| \(C\) | \(\min(2-\lvert U-V\rvert,3-U-V)\) |
| \(F\) | \(1+\min(U,1-U)+\min(V,1-V)\) |

For two distinct edges, every shortest path between interior points exits the first edge through one endpoint and enters the second through an endpoint. In a complete multipartite graph, distinct vertices in different parts are distance one and vertices in the same part are distance two. Taking the minimum over the four endpoint routes proves the table. For two points on the same edge, the intervening edge segment is shortest. In type \(C\), for example, when \(u=\min(U,V)\leq1/2\) the distance is \(2-|U-V|\), while for \(u>1/2\) it is \(3-U-V\). This produces the density shown below, not just a heuristic upper bound.

The six conditional probability densities \(q_\ast(t)\) are zero outside the intervals indicated:

| Type | \(0<t<1\) | \(1<t<3/2\) | \(3/2<t<2\) |
|---|---|---|---|
| \(S\) | \(2(1-t)\) | \(0\) | \(0\) |
| \(O\) | \(t\) | \(2-t\) | \(2-t\) |
| \(T\) | \(t\) | \(1\) | \(0\) |
| \(B\) | \(0\) | \(2(t-1)\) | \(2(t-1)\) |
| \(C\) | \(0\) | \(3(t-1)\) | \(3-t\) |
| \(F\) | \(0\) | \(4(t-1)\) | \(4(2-t)\) |

Each row integrates to one. The \(C\) row follows by splitting the ordered triangle \(0\leq u\leq v\leq1\) at \(u=1/2\); the \(F\) row is the convolution of two independent uniforms on \([0,1/2]\). Moreover, \(q_C=(q_B+q_F)/2\) everywhere away from breakpoints.

Let the same letters \(S,O,T,B,C,F\) denote the **numbers of ordered edge pairs** in these six classes. Counting vertices and part labels gives
\[
\begin{aligned}
S&=m,\\
O&=(N+1)P_2-P_3-N^2,\\
T&=N^3-3NP_2+2P_3,\\
B&=\frac{P_2^2-P_4}{2}-NP_2+P_3+m,\\
C&=(N^2-P_2)(P_2-N)-2N(P_3-P_2)+2(P_4-P_3),\\
F&=m^2-m-O-T-B-C.
\end{aligned}
\]
For instance, \(O=\sum_i a_i\sum_{j\ne i}a_j(a_j-1)\), \(T=\sum_i a_i\sum_{j\ne k;\ j,k\ne i}a_ja_k\), and \(B=\sum_{i<j}a_i(a_i-1)a_j(a_j-1)\). Likewise \(C=\sum_i a_i(a_i-1)\sum_{j\ne k;\ j,k\ne i}a_ja_k\). Each formula counts **ordered** selections of two distinct edges, not unoriented abstract edge sets.

The exact distance density is therefore
\[
f_G(t)=\frac{S q_S(t)+O q_O(t)+T q_T(t)+B q_B(t)+C q_C(t)+F q_F(t)}{m^2}.
\]
This proves the forward dependence on \(P_1,P_2,P_3,P_4\), including all boundaries in probability-law sense.

To prove the converse, set \(A=O+T\) and \(H=B+C/2\). The latter has the direct combinatorial identity
\[
2H=\sum_{i=1}^r a_i(a_i-1)(N-a_i)(N-a_i-1)
=P_4+N(N+1)P_2-N^3-2NP_3+2m.
\]
The first density interval has \(m^2f_G(t)=2m(1-t)+At\). At \(t=3/2\), only the triangle-wedge conditional density \(q_T\) jumps, with downward jump exactly one. At \(t=2\), only the \(B,C\) densities have nonzero left limits, respectively \(2\) and \(1\). These are the four observable identities in the theorem. Finally, direct simplification of the wedge counts yields
\[
2A-T=2m(N-2),\qquad A=-N^3+4mN-2m+P_3.
\]
Solving them together with \(m=(N^2-P_2)/2\) and the displayed expression for \(2H\) proves all four reconstruction formulas. Thus equality of distance laws forces equality of \(P_1,P_2,P_3,P_4\), completing the equivalence.

If each of two multipartite graphs has at most four parts, pad each positive part-size list with zeros to length four. Equality of its first four power sums forces equality of all four elementary symmetric polynomials by Newton's identities, hence equality of the two monic quartics whose roots are the padded part sizes. Therefore both unordered positive part-size lists agree, proving injectivity on this restricted class.

For sharpness let \((s_i)=(-9,-5,-1,7,8)\). Direct calculation gives \(\sum_i s_i=\sum_i s_i^3=0\). The five positive integers \(10+s_i\) are \((1,5,9,17,18)\), while the five integers \(10-s_i\) are a permutation of \((2,3,11,15,19)\). The binomial theorem and vanishing odd sums show equality of all four power sums through degree four, while the two unordered lists are different. Each yields \(N=50\) and \(m=890\); their intrinsic metric graphs are nonisometric because every original vertex has branch valence at least \(31\), and the original part-size multisets (equivalently their vertex degree profiles) differ. The equivalence just proved gives identical full distance laws. Adding any common collection of positive part sizes to both lists produces collisions with exactly any chosen number of parts at least five. This establishes the **sharp threshold**.

## Verification
The accompanying self-contained Python verifier uses exact rational arithmetic for 45 complete-multipartite configurations, totaling **247,806 edge-pair/interior-point shortest-path comparisons**. It separately enumerates all ordered edge pairs, compares class counts against the power-sum formulas, checks the six case-specific distances against shortest paths computed independently from vertex distances, integrates all three density pieces exactly, reconstructs the four observables, and checks the explicit five-part collision and fifth-power separation. Execution command: `python3 verify.py`. Successful output begins with `PASS: ordered-edge classification`.

The universal theorem is established by the preceding six-case analytic proof. Finite checks and algebraic assertions in code are supporting tests, not an exhaustive proof for infinitely many multipartite graphs.

## Relationship to prior work
Jin and Zhang (2013) proved that complete multipartite **discrete graphs are determined by their full distance-matrix spectra**. That spectral theorem does not imply injectivity of the much coarser scalar random-arclength distance histogram; indeed the five-part collision shows that the latter fails to recover the graph even though the former succeeds. Mémoli and Needham (first public 2018) formulated global and local distance-distribution inverse problems for metric-measure spaces and exhibited nonisomorphic metric-tree examples; their inspected metric-graph results do not supply the present complete-multipartite four-power-sum equivalence or the sharp five-part boundary. Garijo, Márquez and Silveira (first public 2021) established algorithms for continuous mean distances and calculated the mean for unit-edge complete graphs; those scalar means and special-edge calculations do not contain the complete multipartite distance law or its exact inverse classification. The arithmetic equal-power-sum identity is a classical Prouhet–Tarry–Escott phenomenon; it is used here, not claimed as new.

## Limitations
The law is global and two-point only; equality does not assert equality of local distance profiles, distance matrices, distance spectra, or graph isometry. The five-part examples disprove injectivity only for the global histogram, not for the stronger information studied by Jin–Zhang or Mémoli–Needham. The proof assumes exactly equal unit edge lengths and positive integer part sizes. No generalization to weighted or non-multipartite metric graphs is asserted. Historical priority for an equivalent complete-multipartite identity in older metric-graph or network literature cannot be eliminated by finite literature searches; independent assessment is still appropriate.

## References
1. Y.-L. Jin and X.-D. Zhang, *Complete multipartite graphs are determined by their distance spectra*, first publicly posted 2013-07-23, arXiv:1307.5931, https://arxiv.org/abs/1307.5931 .
2. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, first publicly posted 2018-10-23, arXiv:1810.09646, https://arxiv.org/html/1810.09646v5 .
3. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, first publicly posted 2021-03-22, arXiv:2103.11676, https://arxiv.org/abs/2103.11676 .
