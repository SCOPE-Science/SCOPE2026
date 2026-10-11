# Facet enumeration for equilateral metrics with independently shortened pairs

## Finding

Let \(n\geq 3\), let \(0\leq k\leq\lfloor n/2\rfloor\), and let \(t_1,\dots,t_k\in(0,1)\). On an \(n\)-point set, choose \(k\) disjoint unordered pairs. Set the distance within the \(i\)-th chosen pair to \(t_i\), and every other distance between distinct points to \(1\). For the corresponding real Lipschitz-free space \(\mathcal F(M)\), the unit ball has exactly

\[
\boxed{\operatorname{facets}(B_{\mathcal F(M)})=3^k\bigl(2^{n-k}-2\bigr).}
\]

Here a facet means a codimension-one face of the \((n-1)\)-dimensional unit ball. This formula holds uniformly for every choice of the independent real parameters \(t_i\in(0,1)\). The proof also classifies all dual extreme Lipschitz potentials.

## Assumptions and scope

Fix any base point \(o\in M\) and identify the dual of \(\mathcal F(M)\) with the real space \(\operatorname{Lip}_0(M)\). Its unit ball is the full-dimensional polytope

\[
P=\{f:M\to\mathbb R:f(o)=0,\ |f(u)-f(v)|\le d(u,v)\text{ for all }u,v\in M\}.
\]

The metric inequalities hold because \(0<t_i<1\) and every triangle has at most one chosen short edge; the sum of the other two lengths is strictly larger than the remaining length. There are \(k\) paired groups and \(s=n-2k\) singleton groups, hence \(n-k\) groups in total. Values of Lipschitz potentials may be shifted by a common additive constant before restoring \(f(o)=0\).

## Proof

**1. Extremality and tight-edge connectivity.** For \(f\in P\), let \(G_f\) be the undirected graph on \(M\) whose edges are exactly the pairs satisfying \(|f(u)-f(v)|=d(u,v)\). The active-constraint normals of \(P\) are signed incidence vectors of \(G_f\) in the quotient by constants. They span dimension \(n-1\) if and only if \(G_f\) is connected. Consequently \(f\) is a vertex of \(P\) if and only if \(G_f\) is connected. Equivalently, if it is disconnected one can perturb the potentials by small, opposite constants on its components while preserving the finitely many strict inequalities; if it is connected, all active equalities uniquely determine \(f\) after normalization at \(o\).

**2. The global anchors.** A connected tight graph contains some edge of length \(1\): the short edges themselves form a matching and cannot connect \(n\ge3\) vertices. As \(d(u,v)\le1\) for all vertices, the potential has range exactly \(1\). Shift its minimum to \(0\), so its maximum is \(1\). Any tight length-one edge must join a point at \(0\) to a point at \(1\). In particular, an isolated singleton must take value \(0\) or \(1\); otherwise it has no incident tight edge.

**3. Exhausting the paired states.** In each selected short pair, at least one endpoint is \(0\) or \(1\). Otherwise neither endpoint has a tight length-one edge, and their short edge alone cannot connect their two-vertex component to the rest of \(G_f\). Both \(0\) and \(1\) cannot belong to the same pair because their difference would exceed \(t_i<1\). If one endpoint is \(0\), the other endpoint must equal \(0\) or \(t_i\), because otherwise that endpoint has no tight incident edge. If one endpoint is \(1\), the other must equal \(1\) or \(1-t_i\). Thus the \(i\)-th pair has precisely six permissible ordered states:

\[
(0,0),\ (0,t_i),\ (t_i,0),\quad
(1,1),\ (1,1-t_i),\ (1-t_i,1).
\]

Each singleton has two possible states: \(0\) and \(1\). We call each of the first three paired states *lower* and each of the last three *upper*. A singleton at \(0\) is lower and a singleton at \(1\) is upper. Both lower and upper groups must occur, because the potential has range \(1\).

**4. Sufficiency.** Conversely, assign independently to each short pair one of the six states and to each singleton one of the two states, provided there is at least one lower group and at least one upper group. All values lie in \([0,1]\); every short-pair difference is either \(0\) or \(t_i\), and every cross-group difference is at most \(1\), so the assignment is feasible. The length-one tight edges connect every \(0\)-valued anchor to every \(1\)-valued anchor, yielding a connected complete bipartite core. Every remaining point of value \(t_i\) or \(1-t_i\) is connected to its anchor by a tight short edge. Therefore \(G_f\) is connected and the potential is a vertex. The classification is exact.

**5. Count and polarity.** There are \(6^k2^s\) unrestricted assignments. Exactly \(3^k\) choices are all lower, and another \(3^k\) are all upper. Because \(0<t_i<1\), distinct assignments yield distinct potentials modulo constants. Thus the number of vertices of \(P\) is

\[
6^k2^s-2\cdot3^k=3^k\bigl(2^{k+s}-2\bigr)
=3^k\bigl(2^{n-k}-2\bigr).
\]

The unit ball of \(\mathcal F(M)\) is the polar of \(P\) under the natural finite-dimensional pairing. Since both polytopes are full dimensional with the origin in their interiors, polar duality identifies vertices of \(P\) with facets of the free-space unit ball, proving the result.

## Verification

The standalone file `matching_facet_checker.py` independently enumerates candidate dual vertices by choosing every labeled spanning tree and every sign pattern of tight equations, solves for potentials by exact integer arithmetic, retains those satisfying all metric inequalities, and compares the resulting set with the classified states. It passed \(36\) test cases (with repetitions when \(k=0\)) with \(3\le n\le6\), all admissible matching sizes, and three independent rational-length choices for each case. Reproduce with `python matching_facet_checker.py`. The finite checker does not establish the universal count; that follows from the connectivity argument above.

The equilateral benchmark \(k=0\) gives \(2^n-2\) facets. For \(n=6\), using three independent shortened pairs gives \(162\) facets, compared with \(62\) for the equilateral metric, despite all the metrics having strict triangle inequalities. As any short length approaches \(1\) from below, the facet count can jump at the endpoint where that chosen pair ceases to be distinguished.

## Relationship to prior work

García-Lirola, Petitjean, Procházka and Rueda Zoca study extremal notions for **points of the free-space unit ball**, rather than counting facets of this particular weighted metric family. Aliaga and Pernecká characterize finitely supported **primal extreme molecules** under strict metric-segment conditions. Those results explain the primal vertices but do not determine how many dual extreme potentials appear.

Gordon and Petrov study combinatorics of Lipschitz polytopes, including a general tight-constraint viewpoint and formulas in the **generic-metric** regime. Their criterion is consistent with the connected tight-edge graph argument used here, but their enumerations do not supply the six-state independent-pair classification and the displayed count for all arbitrary shortened matching metrics. Higashitani, Jochemko and Michałek determine facets for symmetric edge polytopes of **unweighted graph metrics**; a weighted complete metric with independently shortened disjoint pairs is not their graph-metric endpoint. Çelik and collaborators treat discrete and other structured metrics, not this matching contraction formula. The equilateral specialization is classical and is not claimed as a new result.

## Limitations

The proof concerns real Lipschitz-free spaces over finite metrics in which *shortened* edges form a matching and all remaining distances equal \(1\). It does not classify arbitrary overlapping short edges, arbitrary weighted complete graphs, or infinite metric spaces. It does not determine every component of the face vector. Parameter values \(t_i=0\) are excluded because distinct metric points coalesce; at \(t_i=1\) the corresponding matching edge is no longer short. The exact finite arithmetic checks do not replace the analytic proof. No independent external audit has been performed.

## References

- L. García-Lirola, C. Petitjean, A. Procházka, A. Rueda Zoca, *Extremal structure and Duality of Lipschitz free spaces*, arXiv:1707.09307 (first public 2017-07-28), https://arxiv.org/abs/1707.09307.
- R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278 (first public 2018-10-26), https://arxiv.org/abs/1810.11278.
- J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (2016), https://arxiv.org/abs/1608.06848.
- A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018), https://arxiv.org/abs/1807.07678.
- B. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels and L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725 (2020), https://arxiv.org/abs/2003.06725.
