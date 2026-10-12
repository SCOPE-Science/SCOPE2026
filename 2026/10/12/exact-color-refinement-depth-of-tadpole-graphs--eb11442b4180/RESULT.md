# Exact color-refinement depth of tadpole graphs
## Finding
For integers \(m\ge 3\) and \(k\ge 1\), let \(T_{m,k}\) be the tadpole graph obtained by joining one vertex \(q\) of the cycle \(C_m\) by a bridge to the first vertex \(p_1\) of a path \(p_1,\ldots,p_k\). Start ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least \(s\) for which rounds \(s\) and \(s+1\) induce the same vertex partition. Then
\[
\operatorname{Stab}(T_{m,k})
=
\max\left\{
\left\lfloor\frac m2\right\rfloor,\,
\left\lceil\frac k2\right\rceil,\,
\min\{m,k\}
\right\}.
\]

The three terms have distinct causes. The cycle needs \(\lfloor m/2\rfloor\) rounds to resolve all distances from the attachment vertex up to reflection. The tail needs \(\lceil k/2\rceil\) rounds for the waves from the attachment vertex and the leaf to meet. Finally, a cycle neighbor of \(q\) and the tail neighbor \(p_1\) remain color-equivalent through round \(\min\{m,k\}-1\) and split exactly in round \(\min\{m,k\}\); this is the extra cycle-versus-tail ambiguity that is absent on a path.

As a fixed-order consequence, among all tadpole graphs on \(N\) vertices the largest stabilization depth is
\[
\max_{m+k=N}\operatorname{Stab}(T_{m,k})
=
\begin{cases}
1,&N=4,\\
\left\lfloor N/2\right\rfloor,&N\ge5.
\end{cases}
\]
For every \(N\ge5\), a balanced choice \(m=\lfloor N/2\rfloor\), \(k=\lceil N/2\rceil\) attains the maximum.

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. Round \(0\) is the uniform coloring. Each later color records the previous color together with the multiset of previous colors of the neighbors. The parameter \(k\) counts the path vertices outside the cycle, so \(T_{m,k}\) has \(m+k\) vertices. The theorem concerns stabilization on one graph, not distinguishing two graphs by running refinement on their disjoint union.

The final stable partition of \(T_{m,k}\) consists of the attachment vertex \(q\), all singleton tail vertices \(p_i\), and the cycle reflection orbits: two cycle vertices have the same final color exactly when they have the same graph distance from \(q\).

## Proof
Krebs and Verbitsky prove that, for a vertex \(v\), its color after round \(r\) is exactly the isomorphism type of the depth-\(r\) truncation of the universal cover rooted above \(v\). The universal cover of \(T_{m,k}\) has a particularly simple form. Its spine is a bi-infinite path whose degree-three branch vertices occur every \(m\) edges, and from every such branch vertex hangs a path of \(k\) edges ending in a leaf. Every other vertex has degree two.

This description reduces the refinement process to comparing rooted positions in that periodic tree.

First consider two cycle positions. A cycle vertex at distance \(d\) from \(q\), where \(1\le d\le\lfloor m/2\rfloor\), lifts to a spine vertex whose two nearest degree-three spine vertices are at distances \(d\) and \(m-d\). Distinct values of \(d\) are therefore eventually distinguished. The deepest possible distinction is between the two central distance classes: they agree through depth \(\lfloor m/2\rfloor-1\) and differ at depth \(\lfloor m/2\rfloor\). Hence the maximum round needed to separate two distinct cycle reflection orbits is \(\lfloor m/2\rfloor\). For \(m=3\), there is only one nontrivial cycle orbit, and the value \(1\) is already forced by the degree split between \(q\) and the degree-two vertices.

Next consider the tail. The endpoint types are different from the first round: \(q\) has degree three and \(p_k\) has degree one. Inductively, after round \(r\), the vertices \(p_i\) with \(i<r\) have been separated by the wave from \(q\), and those with \(i>k-r\) have been separated by the wave from the leaf. Any remaining middle interval \(p_r,\ldots,p_{k-r}\) is still internally indistinguishable. Thus all tail positions are pairwise distinguished exactly by round \(\lceil k/2\rceil\).

It remains to compare cycle and tail positions. The worst pair is a cycle neighbor \(c_1\) of \(q\) and the tail neighbor \(p_1\). In the universal cover, both roots lie one edge from the same kind of degree-three branch vertex. Looking away from that branch vertex, one root lies on a spine segment whose next degree-three event is \(m\) edges from the branch vertex, while the other lies on a pendant segment whose leaf event is \(k\) edges from the branch vertex. Before depth \(\min\{m,k\}\), these events lie beyond the visible truncation, so the rooted truncations are isomorphic. At depth \(\min\{m,k\}\), the shorter branch exposes its endpoint type and the rooted truncations cease to be isomorphic. Hence \(c_1\) and \(p_1\) split exactly in round \(\min\{m,k\}\).

More generally, if a cycle position and a tail position are both at distance \(i\) from \(q\), their first possible cycle-versus-tail discrepancy is obtained by shortening the preceding argument by \(i-1\) levels, so it occurs no later than round \(\min\{m,k\}-i+1\). If their distances from \(q\) differ, they separate no later than the corresponding distance wave. Therefore no cycle-tail pair survives beyond
\[
\max\left\{
\left\lfloor\frac m2\right\rfloor,\,
\left\lceil\frac k2\right\rceil,\,
\min\{m,k\}
\right\}.
\]
Each of the three terms is also a genuine lower bound by the cycle, tail, and \(c_1\)-versus-\(p_1\) witnesses above. This proves the exact formula.

For the fixed-order statement, put \(N=m+k\). Each term in the formula is at most \(\lfloor N/2\rfloor\) when \(N\ge5\): the first because \(m\le N-1\), the second because \(k\le N-3\), and the third because \(\min\{m,k\}\le\lfloor N/2\rfloor\). The balanced choice \(m=\lfloor N/2\rfloor\), \(k=\lceil N/2\rceil\) is admissible for \(N\ge5\) and makes the third term equal to \(\lfloor N/2\rfloor\). The unique order-\(4\) tadpole is \(T_{3,1}\), which stabilizes in one round.

## Verification
The accompanying `verify.py` implements color refinement directly, with no graph-library dependency. It checks the depth formula for every \(3\le m\le50\) and \(1\le k\le80\), checks that the cycle neighbor and tail neighbor separate exactly in round \(\min\{m,k\}\) for every such parameter pair, and checks the fixed-order extremum for every \(4\le N\le100\). Its terminal output is:

`VERIFY_OK depth_checks=3840 cross_witness_checks=3840 order_checks=97 m=3..50 k=1..80 N=4..100`

The computation is a finite consistency check. The all-parameter result rests on the universal-cover argument above.

## Relationship to prior work
DeMaio and Jacobson use the same standard tadpole family \(T_{m,k}\), a cycle joined to a path by a bridge, for exact graph-invariant calculations. Krebs and Verbitsky define the stabilization parameter for color refinement and prove the exact equivalence between round-\(r\) colors and depth-\(r\) rooted universal-cover truncations. Their paper gives near-linear worst-case examples for unrestricted graphs, not a tadpole-family formula.

Kiefer and McKay later study the iteration number of color refinement systematically. They note the path lower bound and prove that unrestricted graphs can require \(N-1\) iterations. The inspected full text does not state a tadpole, kite, or dragon-graph stabilization formula. Targeted searches under all three family names and under the aliases “color refinement”, “colour refinement”, “1-WL”, “Weisfeiler-Leman”, and “iteration number” likewise did not locate the formula above.

The new point is the exact three-scale competition. On a tadpole, stabilization is controlled not only by the cycle radius and the two-ended tail propagation, but also by the delayed local ambiguity between a cycle edge and the bridge into the tail. Balanced tadpoles make that third mechanism dominant and attain half the graph order.

## Limitations
The theorem is specific to ordinary one-dimensional color refinement from the uniform coloring. It does not claim the same formula for higher-dimensional Weisfeiler-Leman refinement, arbitrary initial colors, or general unicyclic graphs. The literature search was targeted rather than exhaustive, so an obscure family-specific occurrence under unusual terminology remains a residual priority risk.

## References
1. Andreas Krebs and Oleg Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015.
2. Joe DeMaio and John Jacobson, *Fibonacci number of the tadpole graph*, Electronic Journal of Graph Theory and Applications 2(2) (2014), 129–138, DOI: 10.5614/ejgta.2014.2.2.5.
3. Sandra Kiefer and Brendan D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73.
