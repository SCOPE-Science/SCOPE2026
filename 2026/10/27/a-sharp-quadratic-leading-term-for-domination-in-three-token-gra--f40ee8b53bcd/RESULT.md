# A sharp quadratic leading term for domination in three-token graphs of \(K_{2,n}\)

## Finding

Let \(F_3(G)\) be the *three-token graph* of a finite simple graph \(G\): its vertices are the three-element subsets of \(V(G)\), and two such subsets are adjacent when one can be obtained from the other by moving one token along one edge of \(G\) into an unoccupied vertex. Write \(\gamma(H)\) for the smallest cardinality of a dominating vertex set of \(H\).

For every integer \(n\ge4\), put
\[
 t_n=\binom{n}{2}-\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
Then
\[
 \boxed{t_n\ \le\ \gamma\bigl(F_3(K_{2,n})\bigr)\ \le\ t_n+n-2.}
\]
In particular,
\[
 \boxed{\lim_{n\to\infty}\frac{\gamma(F_3(K_{2,n}))}{n^2}=\frac14.}
\]
The upper bound is achieved by an explicitly specified dominating set of cardinality \(t_n+n-2\). Neither an exact formula for \(\gamma(F_3(K_{2,n}))\) nor the optimality of this construction for arbitrary \(n\) is asserted.

## Assumptions and scope

All graphs are finite, simple, and undirected. Fix an integer \(n\ge4\). The two sides of \(K_{2,n}\) are \(A=\{a_0,a_1\}\) and \(B=\{b_1,\ldots,b_n\}\), with all edges between the sides and no edges within either side. The token graph has three layers \(\mathcal L_0,\mathcal L_1,\mathcal L_2\), where a vertex in \(\mathcal L_j\) contains exactly \(j\) elements of \(A\). Domination uses **closed** neighbourhoods: a chosen vertex dominates itself and its neighbours.

## Proof

**Lower bound.** Let \(D\) be any dominating subset of \(V(F_3(K_{2,n}))\). Let \(P\subseteq\binom B2\) comprise exactly the unordered pairs of \(B\) that occur in a selected layer-one token position; if both positions \(\{a_0,b_i,b_j\}\) and \(\{a_1,b_i,b_j\}\) are selected, the pair \(\{b_i,b_j\}\) is counted just once. Let \(R\subseteq\binom B3\) be the selected layer-zero positions.

For each triple \(T\in R\), select an arbitrary pair of its elements and adjoin it to \(P\); call the resulting pair family \(P'\). Thus \(|P'|\le |P|+|R|\le|D|\). **Every** three-element subset \(T\subseteq B\) contains some pair belonging to \(P'\). Indeed, this is immediate if \(T\in R\). Otherwise the unselected layer-zero vertex \(T\) must have a selected neighbour. Its only neighbours lie in \(\mathcal L_1\), and a layer-one neighbour contains exactly a pair from \(T\), necessarily a member of \(P\).

Form the simple graph \(H\) on \(B\) whose edges are precisely the pairs *not* in \(P'\). This graph has no triangle, since the edges of a triangle would be the three pairs of a triple missing \(P'\). By Mantel's inequality, \(|E(H)|\le\lfloor n^2/4\rfloor\), whence
\[
 |D|\ge |P'|=\binom n2-|E(H)|\ge t_n.
\]
For completeness, Mantel's inequality follows by observing that for every edge \(uv\) in any triangle-free graph, its endpoint neighbourhoods are disjoint and hence \(d(u)+d(v)\le n\). Summing over the edges yields \(\sum_v d(v)^2\le n|E(H)|\). Cauchy--Schwarz gives \(\sum_v d(v)^2\ge4|E(H)|^2/n\), and thus \(|E(H)|\le n^2/4\); the integral floor follows.

**Upper bound.** Partition \(B=X\sqcup Y\) with \(|X|=\lfloor n/2\rfloor\) and \(|Y|=\lceil n/2\rceil\). Because \(n\ge4\), both parts contain at least two vertices. Fix any three-element subset \(W\subset B\) and define
\[
\begin{aligned}
D_1&=\{\{a_0,b,c\}:\{b,c\}\in\tbinom X2\cup\tbinom Y2\},\\
D_0&=\{W\},\\
D_2&=\{\{a_0,a_1,b\}:b\in B\setminus W\},\\
D_*&=D_0\cup D_1\cup D_2.
\end{aligned}
\]
These three disjoint layers contain, respectively, one vertex, \(\binom{|X|}{2}+\binom{|Y|}{2}=t_n\) vertices, and \(n-3\) vertices. Hence \(|D_*|=t_n+n-2\).

We verify domination in each layer. A position consisting of three vertices of \(B\) contains two elements of \(X\) or two of \(Y\) by the pigeonhole principle, and is therefore adjacent to the corresponding position in \(D_1\). For a layer-one position \(\{a_i,b,c\}\), if at least one of \(b,c\) lies outside \(W\), the position is adjacent to the member of \(D_2\) using that element of \(B\). If instead both lie in \(W\), it is adjacent to the selected layer-zero position \(W\). Finally, a layer-two position \(\{a_0,a_1,b\}\) is itself in \(D_2\) when \(b\notin W\); when \(b\in W\), choose another vertex \(c\) in the same one of \(X,Y\) as \(b\), which exists since both parts have size at least two. The position is adjacent to \(\{a_0,b,c\}\in D_1\). Thus every position is in \(D_*\) or adjacent to one of its members.

Combining the bounds and using \(t_n=n^2/4+O(n)\) proves the stated limit.

## Verification

`verify.py` uses only the Python standard library. It independently constructs the proposed token-position family, tests actual token adjacency by symmetric difference and base-graph bipartition, and checks domination of every token position for each \(4\le n\le18\). It separately exhausts all simple graphs on at most six vertices to confirm the integer Mantel bound in these ranges. Run `python3 verify.py` from the same directory. `check_output.json` records the exact output of this verification. The infinite theorem rests on the proof above rather than these finite checks.

For example, the lower and upper bounds are \([2,4]\), \([4,7]\), \([6,10]\), \([9,14]\), and \([12,18]\) when \(n=4,5,6,7,8\), respectively. These are **bounds**, not assertions of an exact minimum.

## Relationship to prior work

Fabila-Monroy and Gómez-Galicia (arXiv:2509.16448, first public 19 September 2025) develop domination bounds for token graphs of stars and complete graphs; their three-token complete-graph analysis also uses Mantel's theorem, but it does not concern the three-token graph of \(K_{2,n}\). Fabila-Monroy and Trujillo-Negrete (arXiv:2302.07914) investigate automorphisms of token graphs of complete bipartite graphs, a different invariant.

Chinman, Cortijo, Pedroni, Seong, and Stenger (arXiv:2610.28936, first public 20 October 2026) compute the two-token bipartite domination number and provide general bounds for larger token counts. Their Theorem 1.2 specializes to \(\binom{n+2}{3}/(2n+1)\le\gamma(F_3(K_{2,n}))\le\binom{n+2}{3}\), which has lower leading constant \(1/12\) and an order-\(n^3\) upper bound. The bounds here instead have the sharp common leading constant \(1/4\) and a linear-size gap. This is a comparison of mathematical implications, not a claim of independent confirmation or exhaustive historical priority.

## Limitations

The result determines the leading asymptotic coefficient and an explicit additive interval of length \(n-2\), not the exact domination number. The construction is not proved optimal, including when finite optimisation finds matching small cases. The theorem addresses the narrow graph family \(F_3(K_{2,n})\); no extension to arbitrary \(m\) or higher token count is claimed. Historical priority and independent mathematical review remain outstanding.

## References

1. R. Fabila-Monroy and S. G. Gómez-Galicia, *Domination number of Token Graphs* (2025), arXiv:2509.16448, https://arxiv.org/abs/2509.16448.
2. R. Fabila-Monroy and A. L. Trujillo-Negrete, *On the Automorphism Group of Token Graphs of Complete Bipartite Graphs and Cartesian Products of Connected Graphs* (2023), arXiv:2302.07914, https://arxiv.org/abs/2302.07914.
3. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, and L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)* (2026), arXiv:2610.28936, https://arxiv.org/abs/2610.28936.
4. W. Mantel, *Problem 28*, Wiskundige Opgaven **10** (1907), 60--61; the required inequality is proved independently above.
