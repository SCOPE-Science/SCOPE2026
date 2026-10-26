# Cycle-convexity independence systems of nonchordal cycle bouquets

## Finding

Let \(G\) be obtained from \(k\ge3\) cycles \(C_{\ell_1},\ldots,C_{\ell_k}\), each of length \(\ell_i\ge3\), by identifying precisely one common vertex \(c\) and no other vertices, and optionally attaching finite trees by bridges. Assume at least one \(\ell_i\ge4\). Let \(P_i\) be the \(p_i=\ell_i-1\) other vertices of the \(i\)-th cycle, and let \(t\) count vertices outside all cycles. In cycle convexity, every **nonempty** convexly independent set is simultaneously Helly independent and Radon independent, and conversely. Their common positive-degree set-enumerator is given by the following polynomial, whose constant term counts the empty convexly/Radon-independent set:

\[
\Phi_G(z)=(1+z)^t\left[(1+z)\prod_{i=1}^k A_i(z)+\sum_{i=1}^k z^{p_i}\prod_{j\ne i} A_j(z)\right],\qquad A_i(z)=(1+z)^{p_i}-z^{p_i}.
\]

The exact common maximum cardinality is

\[
\operatorname{rk}_{cc}(G)=\operatorname{hel}_{cc}(G)=\operatorname{rad}_{cc}(G)=|V(G)|-k,
\]

and the number of maximum-cardinality sets, for each of these three independence notions, is

\[
\prod_{i=1}^k p_i+\sum_{i=1}^k\prod_{j\ne i}p_j.
\]

Every maximum-cardinality set contains all vertices outside the cycles. Among the cycle vertices, it either contains \(c\) and omits exactly one peripheral vertex from every cycle, or omits \(c\), contains every peripheral vertex of exactly one cycle, and omits exactly one peripheral vertex from each remaining cycle.

## Assumptions and scope

The graph is finite, simple, and connected. Its only nontrivial blocks are the specified cycles, all meeting at \(c\). Remaining edges are bridges; equivalently, arbitrary pendant trees may be attached without introducing additional cycles. The parameter restrictions \(k\ge3\) and at least one \(\ell_i\ge4\) single out a nonchordal class beyond previously studied extremal values and chordal graph algorithms.

For a vertex set \(S\), the cycle interval \(I_{cc}(S)\) contains \(S\) and every vertex \(v\) lying on a cycle of \(G[S\cup\{v\}]\); its iterated fixed point is \(H_{cc}(S)\). A nonempty \(S\) is convexly independent if \(v\notin H_{cc}(S\setminus\{v\})\) for every \(v\in S\), Helly independent if \(\bigcap_{v\in S}H_{cc}(S\setminus\{v\})=\varnothing\), and Radon independent if the convex hulls of the two sides of every partition into two nonempty parts are disjoint. A polynomial coefficient at degree \(r\ge1\) counts sets of size \(r\) of **each** type. The empty-set convention affects only the constant coefficient.

## Proof

**Cycle and bridge closure.** A vertex is added by the cycle interval precisely when it has two neighbors in the same component of the current induced subgraph. Every simple cycle of \(G\) is one of the prescribed cycles; a bridge cannot lie on a cycle. Thus a vertex outside the cycles is never generated, and selecting or omitting such vertices does not change the closure process on cycle vertices. For a peripheral vertex \(v\in P_i\) not already selected, the only way it can be generated is that \(c\) and every vertex of \(P_i\setminus\{v\}\) have been selected. If \(c\) is absent, it can be generated exactly when all vertices of at least one \(P_i\) are selected.

**Classification of convex independence.** Fix any \(S\subseteq V(G)\). The preceding closure rules imply the exact characterization

\[
\begin{split}
&c\in S\quad\text{and}\quad |S\cap P_i|\le p_i-1\quad\text{for every }i,\\
&\hspace{15mm}\text{or}\\
&c\notin S\quad\text{and}\quad |\{i:P_i\subseteq S\}|\le1.
\end{split}
\tag{1}
\]

Indeed, if \(c\in S\) and one peripheral set \(P_i\) is complete, any selected peripheral vertex on that cycle is regenerated after its removal. Conversely, with all \(P_i\) incomplete, deleting a selected peripheral leaves at least two missing vertices on that cycle, which cannot be restored; deleting \(c\) leaves no complete peripheral set to generate it. If \(c\notin S\) and two peripheral sets are complete, deleting a vertex of either full set leaves another full set that first generates \(c\), after which the deleted vertex is regenerated. Conversely, if at most one set is complete, deleting a vertex from that set leaves no way to generate \(c\); deleting a vertex from any other set leaves at least two missing vertices on its cycle, even if \(c\) is subsequently generated elsewhere. Bridge-only vertices can never be regenerated. This proves (1) in both directions, including all closure iterations.

**Radon independence.** For a set satisfying (1) and any partition into two nonempty subsets, at least one part has no convex-hull growth: if \(c\in S\), choose the part not containing \(c\), because it contains no complete peripheral set; if \(c\notin S\), at most one part can contain a complete \(P_i\). A vertex of the growth-free part cannot belong to the hull of the other part, since otherwise it would lie in the hull of \(S\) with that vertex removed, contradicting convex independence. Hence the two hulls do not intersect.

**Helly independence.** Every selected vertex is absent from its own deletion hull, by (1), so no selected vertex lies in the intersection of all deletion hulls. An omitted bridge-only vertex belongs to none of them. For an omitted cycle vertex, if \(c\notin S\) and one peripheral set is complete, removing a vertex of that full set prevents *all* outsider generation; when no set is complete, no outsider is generated even from \(S\). If \(c\in S\) and an omitted peripheral vertex \(w\in P_i\) can ever be generated, then \(P_i\setminus\{w\}\subseteq S\) and some selected vertex \(a\in P_i\) can be removed to leave at least two missing peripheral vertices on that cycle, preventing \(w\)'s generation. Otherwise \(w\) is never generated. Therefore the deletion hulls have empty intersection. Since in any convexity Helly or Radon independence implies convex independence (an included deletion-hull vertex gives an immediate witness of the corresponding dependence), all three families coincide for nonempty sets.

**Polynomial and optimum.** Put \(A_i(z)=(1+z)^{p_i}-z^{p_i}\), the enumerator of proper subsets of \(P_i\). Condition (1) gives an optional choice from each \(P_i\) and forces a factor \(z\) for \(c\) when the center is selected. When \(c\) is omitted, either no \(P_i\) is complete, or exactly one \(P_i\) is complete. Hence the central factor is \((1+z)\prod_i A_i(z)+\sum_i z^{p_i}\prod_{j\ne i}A_j(z)\). Each of the \(t\) bridge-only vertices is freely chosen, multiplying by \((1+z)^t\). The degree is \(|V(G)|-k\); its leading coefficient is \(\prod_i p_i+\sum_i\prod_{j\ne i}p_j\). The configurations contributing to this degree are exactly those described in the Finding.

**Comparison with induced forests.** Deleting \(c\) leaves an induced forest of order \(|V(G)|-1\), and the graph contains cycles. The known equality between cycle-convexity general-position number and maximum induced-forest order therefore gives general-position number \(|V(G)|-1\). Its gap above the three invariants proved here is \(k-1\), unbounded as the number of cycles grows. This comparison is not presented as a new formula for the general-position number.

## Verification

A standalone verifier evaluates the cycle convex hull on the actual adjacency graph by recomputing components until closure. It independently tests convex, Helly, and Radon independence for every vertex subset on twelve sample graphs, with three or four cycles, mixed lengths, and attached bridge paths. Each independence family is compared to the explicit subset classification; the program verifies the generating polynomial coefficientwise and counts all maximizing sets. All cases pass with `VERIFY_OK`. The code is `verify_cycle_convex.py`, and exact recorded output is `verify_output.txt`. These finite computations check definitions and boundaries but are not an infinite-family proof.

For three four-cycles meeting at one vertex with no additional vertices, the cardinality polynomial is \(1+10z+45z^2+120z^3+207z^4+234z^5+162z^6+54z^7\), giving maximum cardinality \(7\) and exactly \(54\) maximizing sets.

## Relationship to prior work

Nair, Anand, Chandran, Nascimento, and Anil (2026) introduce the cycle-convexity Helly and Radon investigations in this form, establish complexity results, and characterize extremal values \(|V|-1\) and \(|V|-2\). Those results do not determine the full independence-set systems or cardinality polynomials for the nonchordal multicycle bouquets here, whose extremal cardinality is \(|V|-k\) with \(k\ge3\).

Aráujo, Aráujo, Medeiros, Nisse, and Silva (2026) establish that the cycle-convexity general-position number equals the maximum induced-forest order and give algorithms for the **rank** on several graph classes, including chordal and starlike graphs. The induced-forest equality is used explicitly above. The all-triangle special case is chordal, and its numerical rank should not be regarded as newly independent of that earlier coverage. The distinctive assertion here is equality of **three entire independence set systems** and their explicit all-cardinalities polynomial, including bouquets with an induced cycle of length at least four and arbitrary pendant trees. The author's freely available full technical report could not be inspected, so an unindexed exact formulation remains a bibliographic risk.

## Limitations

No formula is claimed for cacti whose cycles meet at more than one cut vertex, for graphs with additional non-bridge chords, or for arbitrary convexity operators. The polynomial counts vertex subsets, not sequences of convex-hull growth. No independent mathematical audit has been performed. The self-review do not establish publication priority; unavailable full texts are an explicit residual originality risk.

## References

1. R. S. Nair, B. S. Anand, U. Chandran S. V., J. R. Nascimento, A. Anil, *Computing the Helly Number, Radon Number and Rank in Cycle Convexity*, arXiv:2609.34236v1 (first posted 2026-09-28), https://arxiv.org/abs/2609.34236.
2. J. Aráujo, S. N. Aráujo, P. P. Medeiros, N. Nisse, C. Silva, *On the Rank and the General Position Number in Cycle Convexity*, IWOCA 2026, pp. 73–87, DOI:10.1007/978-3-032-27732-9_6; full technical-report record https://inria.hal.science/hal-05378038.
