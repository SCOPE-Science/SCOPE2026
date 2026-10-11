# Sharp facet-count transitions for snowflaked complete bipartite metrics

## Finding
Let \(m,n\ge2\) be integers. Partition a finite pointed metric space \(M=A\sqcup B\) into sets of cardinalities \(m\) and \(n\), and fix \(o\in A\). For \(1\le t\le2\), give \(M\) the metric
\[
d_t(u,v)=\begin{cases}0&u=v,\\1&u\in A,\ v\in B\ \text{or vice versa},\\t&u\ne v\text{ and }u,v\text{ lie in the same part}.\end{cases}
\]
Let \(\mathcal F(M,d_t)\) be the real Lipschitz-free space, and write \(F_{m,n}(t)\) for the number of facets of its unit ball. Then
\[
\boxed{F_{m,n}(t)=
\begin{cases}
2^{m+n}-2,&t=1,\\
2(2^m-1)(2^n-1),&1<t<2,\\
2^m+2^n-2,&t=2.
\end{cases}}
\]
The formula gives a complete classification of vertices of the dual unit ball. The integer facet count is constant throughout the open snowflake interval, jumps upward from the equilateral endpoint, and drops at the ordinary graph-metric endpoint. In the smallest nontrivial case \(m=n=2\), the respective numbers are \(14\), \(18\), and \(6\).

## Assumptions and scope
The scalars and Lipschitz functions are real. A function \(f:M\to\mathbb R\) belongs to the dual unit ball \(L_t=B_{\operatorname{Lip}_0(M,d_t)}\) exactly when \(f(o)=0\) and \(|f(u)-f(v)|\le d_t(u,v)\) for every pair. The primal space has dimension \(m+n-1\), and its ball is the convex hull of the normalized molecules \((\delta_u-\delta_v)/d_t(u,v)\); polarity therefore identifies facets of the primal ball with vertices of \(L_t\). The metric is the power snowflake of the shortest-path metric of the complete bipartite graph \(K_{m,n}\) at \(t=2^\alpha\), \(0\le\alpha\le1\). Every triangle inequality holds, including at both endpoints.

A pair \(\{u,v\}\) is **tight** for \(f\in L_t\) when \(|f(u)-f(v)|=d_t(u,v)\). Let \(H_f\) be the undirected graph on \(M\) consisting of all tight pairs. The elementary extremality criterion is
\[
\boxed{f\in\operatorname{ext}L_t\quad\Longleftrightarrow\quad H_f\text{ is connected}.}
\]
Indeed, when \(H_f\) is connected, a midpoint representation \(f=(g+h)/2\) forces both summands to have the same increment as \(f\) along every tight edge, hence to coincide with \(f\) after the base-point normalization. Conversely, if the tight graph is disconnected, shift the values on any component not containing \(o\) by \(\pm\varepsilon\). All inequalities across this cut have strictly positive slack; finiteness permits a common sufficiently small \(\varepsilon>0\), producing a nontrivial midpoint representation. This proves the criterion with no genericity assumption.

## Proof
**Interior regime \(1<t<2\).** Put \(\operatorname{osc}_A f=\max_Af-\min_A f\), and similarly for \(B\). Both oscillations are at most \(t\). If \(\operatorname{osc}_A f=t\), set \(L=\min_A f\). Because each member of \(B\) is at distance one from both an \(A\)-minimum and an \(A\)-maximum, every \(b\in B\) satisfies
\[
L+t-1\le f(b)\le L+1.
\]
Thus \(\operatorname{osc}_B f\le2-t<t\), so no pair of points in \(B\) is tight. Every member of \(A\) with value strictly between \(L\) and \(L+t\) is isolated in \(H_f\): it has no tight within-part edge and is at distance strictly less than one in value from each \(B\)-value. Likewise, every member of \(B\) with value strictly between \(L+t-1\) and \(L+1\) is isolated, since the oscillation within \(B\) is smaller than \(t\). Consequently, if \(H_f\) is connected, \(f(A)=\{L,L+t\}\) with both levels present, while every \(B\)-value belongs to \(\{L+t-1,L+1\}\). Conversely, any such assignment has connected tight graph: the two levels of \(A\) are joined by tight edges, each upper \(B\)-value is joined to every lower \(A\)-point, and each lower \(B\)-value to every upper \(A\)-point. Since adding a constant is removed uniquely by \(f(o)=0\), this gives exactly \((2^m-2)2^n\) vertices.

The disjoint symmetric case \(\operatorname{osc}_B f=t\) contributes \((2^n-2)2^m\) vertices. These two cases cannot overlap because the range of one part forces the other part to oscillate by at most \(2-t<t\).

If neither part has a tight internal pair, all edges of the connected graph \(H_f\) are cross edges, and each tight cross edge changes the function value by \(\pm1\). Along a tight path between two points in the same part, the path has even length, so their values differ by an even integer. Yet the diameter bound in that part is \(t<2\); the difference must therefore be zero. Hence \(f\) is constant on each part, the two constants differ by precisely \(1\) in absolute value, and there are exactly two such vertices. The total is
\[
(2^m-2)2^n+(2^n-2)2^m+2=2(2^m-1)(2^n-1).
\]

**Equilateral endpoint \(t=1\).** All distinct points are distance one apart. For an extreme \(f\), connectedness of \(H_f\) forces every value to differ from \(f(o)=0\) by an integer, while the entire range of \(f\) is at most one. Thus \(f\) takes exactly two values separated by one; conversely every nonconstant two-level assignment is extreme, as its tight graph is complete bipartite between the levels. There are exactly \(2^{m+n}-2\) ordered choices of a nonempty proper upper level, counting both orientations after fixing \(f(o)=0\).

**Graph-metric endpoint \(t=2\).** If \(\operatorname{osc}_A f=2\), cross-distance constraints force every \(B\)-value to be the common midpoint \(L+1\), where \(L=\min_A f\). Any \(A\)-value strictly between \(L\) and \(L+2\) is isolated in the tight graph. Therefore vertices of this type are exactly the nonconstant assignments of \(L\) or \(L+2\) to \(A\), with all of \(B\) at \(L+1\); there are \(2^m-2\). Symmetrically, vertices with \(\operatorname{osc}_B f=2\) contribute \(2^n-2\), disjointly. Otherwise neither part has a tight internal pair, and the even-path argument above applies (an even integer of absolute value less than two is zero). This gives two further vertices constant on each part at levels separated by one. Hence the final count is \(2^m+2^n-2\). All cases are exhaustive, and each listed assignment was shown to have connected tight graph. Polarity converts these three vertex counts into the asserted facet counts. \(\square\)

## Verification
The proof is uniform in the positive integers \(m,n\ge2\) and every real \(1\le t\le2\). It uses exact inequalities, an extremality criterion proved above, and a disjoint exhaustive classification. No finite enumeration is assumed in the general argument. The accompanying standalone Python program enumerates feasible intersections of independent tight constraints using rational arithmetic. Running it gives the predicted dual-vertex counts \(14,18,6\) for the three regimes with \((m,n)=(2,2)\), and \(30,42,10\) with \((m,n)=(2,3)\), testing the three parameter regimes at \(t=1,3/2,2\).

## Relationship to prior work
Cobollo, Guirao and Montesinos (arXiv:2304.13183v1, first publicly available 25 April 2023, primary MSC 46B20) develop the geometry and numerical index of two-dimensional Lipschitz-free spaces. Their exact formulas are for three-point metrics, whereas the family here has at least four points and the invariant is the number of facets. Gordon and Petrov (arXiv:1608.06848) study Lipschitz-polytope face graphs and give the generic-metric face numbers and the equilateral endpoint; their generic formula does not apply directly here because our homogeneous metric has many equal tight four-cycles. Their face-connectivity framework is prior art, not claimed as new.

Higashitani, Jochemko and Michałek (arXiv:1807.07678v1, Proposition 3.4 and Section 3.1) classify facets of symmetric edge polytopes of complete bipartite graphs: this already covers the \(t=2\) endpoint, since the Lipschitz-free unit ball is then exactly the symmetric edge polytope. Their theorem does not cover the strictly snowflaked metric \(1<t<2\): there every same-part pair has length \(t<2\) and gives an additional extremal molecule, so the associated unit ball is no longer the symmetric edge polytope of \(K_{m,n}\). Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642) study extreme molecules, geometry and decompositions of general finite Lipschitz-free spaces, but do not provide this complete interior facet enumeration. The claimed contribution is the complete sharp piecewise face-count law and explicit classification for the nontrivial snowflake interval, together with its comparison to both known limiting regimes.

## Limitations
The formula concerns real scalars, finite complete bipartite metrics with at least two vertices per part, and the zero-dimensional face count of the dual polytope (equivalently facets of the primal). It does not compute the full face lattice, volumes or numerical indices for the interior metrics. The general tight-graph criterion and the equilateral and ordinary graph endpoints are known mathematical tools or prior cases, not independent novelty claims. Although several directly pertinent full papers and targeted published-results records were checked, an equivalent enumeration in unindexed transportation-polytope or polyhedral literature remains a bibliographic risk. Numerical checks at small cardinalities are illustrations, not the proof for arbitrary \(m,n\).

## References
1. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first public 2023-04-25), https://arxiv.org/html/2304.13183v1 .
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, Arnold Mathematical Journal 3 (2017), 205–218, arXiv:1608.06848, https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/17-63/index.html .
3. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018), https://arxiv.org/html/1807.07678v1 .
4. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, https://arxiv.org/html/1911.10642v2 .
5. E. Delucchi and L. Hoessly, *Fundamental polytopes of metric trees via parallel connections of matroids*, arXiv:1612.05534 (2016), https://arxiv.org/abs/1612.05534 .
