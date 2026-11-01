# Continuous two-point geodesic tomography of complete bipartite metric graphs

## Finding
Let \(p,q\) be arbitrary positive integers. Give each of the \(pq\) edges of the complete bipartite graph \(K_{p,q}\) length one, and regard its geometric realization as a compact intrinsic length-metric graph \(G_{p,q}\). Choose \(X,Y\) independently from normalized total arclength, and let \(D=d_{G_{p,q}}(X,Y)\). The law of \(D\) is absolutely continuous. Its density, extended by zero outside \([0,2]\), is
\[
f_{p,q}(t)=\begin{cases}
\dfrac{2+(p+q-4)t}{pq},&0<t<1,\\[4pt]
\dfrac{(p+q-2)(2-t)+2(p-1)(q-1)(t-1)}{pq},&1<t<2.
\end{cases}
\]
Consequently, \(\mathbb E D=\frac53-\frac23(\frac1p+\frac1q)\). The complete two-point distance law determines the unordered bipartition \(\{p,q\}\) uniquely, even among all positive integer part sizes. Indeed, with \(\ell=2/f_{p,q}(0+)\) and \(m=\mathbb E D\), the values \(p,q\) are exactly the two positive integer roots of
\[
z^2-\frac{\ell}{2}(5-3m)z+\ell=0.
\]
The same formulas include stars \(K_{1,q}\) and the single-edge graph \(K_{1,1}\). If both part sizes diverge, the distance law converges in total variation to the triangular law with density \(2(t-1)\) on \([1,2]\); its total-variation distance to that law is at most \((p+q-1)/(pq)\).

## Assumptions and scope
Vertices and edges are those of a simple complete bipartite graph, not a complete graph, and each edge has *geometric length exactly one*. The distance is the intrinsic shortest-path distance in the continuous one-dimensional realization, not a discrete vertex metric and not Euclidean ambient distance. Arclength gives zero mass to vertices. The two points are independent. Equality of laws is asserted only within this specified family, up to switching the two color classes; no reconstruction claim is made for arbitrary metric graphs or unequal edge lengths.

## Proof
Write \(M=pq\) for the total number of edges and their total length. Picking a uniform point is equivalent to independently picking one of these edges uniformly and then an independent uniform coordinate on that edge. Orient every edge from its left endpoint to its right endpoint, with coordinates \(x,y\in[0,1]\).

For two sampled edges, the ordered edge-pair probabilities are
\[
w_0=\frac1M,\qquad w_1=\frac{p+q-2}{M},\qquad w_2=\frac{(p-1)(q-1)}M.
\]
These correspond respectively to: the same edge; two different edges sharing a vertex; two edges with disjoint endpoints. To prove the counts, each fixed edge has one identical partner, \((q-1)+(p-1)\) distinct adjacent partners, and \((p-1)(q-1)\) disjoint partners. The weights sum to one.

On the same edge, the shortest route is the direct segment, of length \(|x-y|\). For distinct edges meeting at a left vertex, the route through that vertex has length \(x+y\), and every competing route uses at least the remaining portions and two other whole edges, hence cannot beat it since \(x+y\le2\). When they meet at a right vertex the route has length \(2-x-y\), which has the same distribution. For disjoint edges, because the graph is complete bipartite, the cross-endpoint routes have lengths \(2+x-y\) and \(2-x+y\); the same-side endpoint routes have length at least two. Their minimum is \(2-|x-y|\). The argument also covers the degenerate cases \(p=1\) or \(q=1\), in which the disjoint category is absent.

For independent uniform \(U,V\in[0,1]\), the three conditional distance densities are, respectively: \(2(1-t)\) for \(0<t<1\); \(t\) for \(0<t<1\) and \(2-t\) for \(1<t<2\); and \(2(t-1)\) for \(1<t<2\). Mixture with \(w_0,w_1,w_2\) yields the stated density, with no atoms. Their means are respectively \(1/3,1,5/3\), giving
\[
\mathbb ED=\frac{w_0}{3}+w_1+\frac{5w_2}{3}=\frac53-\frac{2(p+q)}{3pq}.
\]
Now \(f(0+)=2/(pq)\), so its reciprocal identifies \(\ell=pq\). The mean determines \(p+q=\ell(5-3m)/2\), and the unordered roots of the displayed monic quadratic are exactly \(\{p,q\}\). There is no other positive-integer pair in the family with the same law.

Finally, \(w_2\) is the mass of a component already equal to the limiting law; the other two components have total mass \(w_0+w_1=(p+q-1)/(pq)\). Convexity of total variation proves the stated quantitative convergence as \(p,q\to\infty\).

## Verification
The standalone Python 3 program `verify.py` uses exact rational arithmetic to check probability weights, conditional-mean aggregation, algebraic reconstruction, continuity at the joining point, and normalization for all \(1\le p,q\le19\) (361 pairs). These finite checks are auxiliary; the preceding symbolic argument proves the universal assertions.

## Relationship to prior work
Network shortest-path distribution work often samples *vertices* of random graph models rather than arclength points of a fixed metric realization; for example Blondel et al. (2007) and Nitzan et al. (2016). Calabuig et al. (2025) construct distance distribution functions indexed by a vertex and finite or countable graph balls; their framework differs from the pairwise normalized-arclength law here. The relevant published findings on weighted graph distances, metric bipartite graph invariants and metric-graph inverse reconstruction address different statements, as documented in the accompanying review.

## Limitations
The unit-edge condition is essential to the stated parameter recovery. The result does not characterize all metric graphs with the same pair-distance distribution. No independent scientific audit or comprehensive historical priority examination has been performed; unlocated earlier treatments of the same elementary family remain a risk. The result asserts no explicit formula for irregular bipartite graphs or unequal-edge complete bipartite metric graphs.

## References
Blondel, V. D., Guillaume, J.-L., Hendrickx, J. M., and Jungers, R. M., *Distance distribution in random graphs and application to network exploration*, Physical Review E **76** (2007), 066101, https://doi.org/10.1103/PhysRevE.76.066101 (first publicly published 2007-12-05).

Nitzan, M., Katzav, E., Kühn, R., and Biham, O., *Distance distribution in configuration-model networks*, Physical Review E **93** (2016), 062309, https://doi.org/10.1103/PhysRevE.93.062309.

Calabuig et al., *Metric symmetry and distance distribution functions on graphs*, Aequationes Mathematicae (2025), https://doi.org/10.1007/s00010-024-01145-2.
