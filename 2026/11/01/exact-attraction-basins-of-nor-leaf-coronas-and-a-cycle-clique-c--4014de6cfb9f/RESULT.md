# Exact attraction basins of NOR leaf coronas and a cycle–clique crossover

## Finding

Let \(G=(V,E)\) be any finite loopless simple graph on \(n\ge1\) labelled vertices, and form the one-leaf corona \(W(G)\) by attaching a distinct pendant vertex \(v'\) to every \(v\in V\). Under synchronous **open-neighborhood NOR**, every vertex becomes \(1\) exactly when all its neighbors are \(0\). Write \(F\) for the resulting map on the \(4^n\) binary configurations.

Let \(N_G(S)=\{v\in V: v\text{ has a neighbor in }S\}\) be the **open** neighborhood of a vertex set, and let \(I(H)\) be the number of independent vertex sets of a graph \(H\), including the empty set. The following is a complete classification of the attractors and their attraction basins.

1. Recurrent states are in bijection with independent sets of the bipartite double cover \(G\times K_2\). More explicitly, they are the ordered phase states
   \[q_{A,B}=(\mathbf1_A,\mathbf1_{V\setminus B}),\quad N_G(A)\cap B=\varnothing,\]
   where the first coordinate is the set of active base vertices and the second is the set of active private leaves. The update exchanges \(A\) and \(B\): \(F(q_{A,B})=q_{B,A}\). Therefore there are precisely \(I(G)\) fixed configurations and \((I(G\times K_2)-I(G))/2\) primitive two-cycle orbits.

2. Every configuration enters its final orbit within **at most one update**; this is sharp when \(E\ne\varnothing\). For a fixed point indexed by an independent set \(S\), the entire attraction basin has size
   \[\operatorname{Bas}(S)=2^{|N_G(S)|}.\]
   For a primitive two-cycle indexed by the unordered pair \(\{A,B\}\), where \(A\ne B\) and \(N_G(A)\cap B=\varnothing\), the basin size is
   \[\operatorname{Bas}(A,B)=2^{|N_G(A)|}+2^{|N_G(B)|}.\]
   Consequently, for uniformly random initial conditions the probability of eventual fixation is exactly
   \[\mathbb P_G(\mathrm{fix})=4^{-n}\sum_{S\subseteq V\,\mathrm{independent}}2^{|N_G(S)|}.\]

3. For the two canonical families with the same \(2n\)-vertex corona size, there is an **exact crossover**. For the complete base graph \(K_n\), the total fixed-point basin population is
   \[B_n^{\mathrm{clique}}=1+n2^{n-1}.\]
   For the cycle base graph \(C_n\), \(n\ge3\), put \(B_n^{\mathrm{cycle}}=\sum_{S\,\mathrm{independent}}2^{|N_{C_n}(S)|}\). Then
   \[B_3^{\mathrm{cycle}}=13,\quad B_4^{\mathrm{cycle}}=25,\quad B_5^{\mathrm{cycle}}=61,\]
   and for every \(n\ge6\),
   \[\boxed{B_n^{\mathrm{cycle}}=B_{n-1}^{\mathrm{cycle}}+2B_{n-2}^{\mathrm{cycle}}+2B_{n-3}^{\mathrm{cycle}}}.\]
   The populations are equal at \(n=3\), the clique has the larger fixed basin population at every \(4\le n\le16\), and the cycle has the larger population at **every \(n\ge17\)**. Writing \(\lambda\approx2.269530842\) for the unique positive root of \(\lambda^3-\lambda^2-2\lambda-2=0\), the fixation probabilities satisfy
   \[\mathbb P_{C_n}(\mathrm{fix})\sim(\lambda/4)^n,\qquad \mathbb P_{K_n}(\mathrm{fix})\sim n/2^{n+1}.\]
   Thus the less-connected cycle corona eventually has more fixed-basin configurations than the clique corona, with an exponentially growing ratio of their fixation probabilities.

For cycles, one also has the exact recurrent census
\[I(C_n)=L_n,\qquad I(C_n\times K_2)=\begin{cases}L_n^2,&n\text{ even},\\L_{2n},&n\text{ odd},\end{cases}\]
where \(L_n\) is the Lucas sequence \(L_0=2,L_1=1,L_{n+2}=L_{n+1}+L_n\). Hence \((I(C_n\times K_2)-L_n)/2\) counts primitive temporal two-cycles.

## Assumptions and scope

All graphs are finite, undirected, simple and loopless; isolated base vertices are allowed. No vertex reads its own state, and the update is synchronous. The corona has exactly one private pendant vertex per base vertex. The exact crossover concerns \(n\ge3\), so that \(C_n\) is a simple cycle. The first-entry time of an initially recurrent configuration is defined to be zero. Only fixed points and primitive two-cycles occur. The one-step bound applies to every base graph, but it is attained only if the base graph has an edge.

## Proof

Represent a full state by a pair \((A,L)\) of subsets of \(V\), respectively the currently active base vertices and active private leaves. An active base vertex at the next step must have an inactive private leaf and no active base neighbor, while each private leaf becomes active precisely when its base vertex is inactive. Thus
\[\boxed{F(A,L)=((V\setminus L)\setminus N_G(A),\ V\setminus A)}.\]
Define \(B=(V\setminus L)\setminus N_G(A)\). By construction \(B\cap N_G(A)=\varnothing\). Since \(G\) is undirected, this condition is symmetric in \(A,B\): it is equivalent to \(A\cap N_G(B)=\varnothing\). Accordingly, \(F(A,L)=q_{B,A}\), and its next step is \(q_{A,B}\), followed by \(q_{B,A}\) again. In particular, \(F^3=F\), every image state is recurrent, and the recurrent states are exactly the \(q_{A,B}\) satisfying the cross-nonneighbor condition. A pair \((A,B)\) with this condition chooses an independent set in the bipartite graph with vertex classes \(V\times\{0\}\) and \(V\times\{1\}\) and an edge between \((u,0)\) and \((v,1)\) whenever \(uv\in E\). This is precisely the bipartite double cover \(G\times K_2\). Phase exchange interchanges \(A,B\). Fixed states have \(A=B=S\), so \(S\) is independent in \(G\). Counting the remaining recurrent states in pairs proves the orbit census.

To count predecessors of the periodic state \(q_{A,B}=(A,V\setminus B)\), a predecessor \((C,L)\) must satisfy \(C=B\), because its leaf output is \(V\setminus C\). Its base output equals \(A\) exactly when \(L_v=0\) for \(v\in A\), \(L_v=1\) for \(v\in V\setminus(N_G(B)\cup A)\), while \(L_v\) is unrestricted for each \(v\in N_G(B)\). The cross-nonneighbor condition ensures these requirements are consistent. The predecessor fiber therefore has size \(2^{|N_G(B)|}\). Every state is recurrent after one update, so the basin of an orbit is the disjoint union of the predecessor fibers of its distinct phases. This establishes the fixed- and two-cycle basin formulas, as well as their completeness and the fixation probability.

For \(K_n\), independent sets are the empty set and the \(n\) singletons. The empty set has open neighborhood size zero, and each singleton has neighborhood size \(n-1\); this yields \(1+n2^{n-1}\). The general one-step bound is sharp whenever the base contains an edge: choose a core set containing an endpoint of an edge and make all leaves initially inactive; at least one leaf changes between the starting configuration and the second iterate, so the starting state is not periodic. If the base has no edges, the corona is a disjoint union of edges, and every state is periodic from time zero.

For \(C_n\), each independent set is a cyclic binary word with no two adjacent ones. Write \(z\) for the weight assigned to each base vertex neighboring a selected vertex. Transfer states record consecutive bits \(00,01,10\); triples \((a,b,c)\) with no adjacent ones assign weight \(z\) to the middle vertex when \(a\lor c=1\), and weight one otherwise. Their transfer matrix is
\[T(z)=\begin{pmatrix}1&z&0\\0&0&1\\z&z&0\end{pmatrix},\qquad \sum_{S\,\mathrm{independent}}z^{|N_{C_n}(S)|}=\operatorname{tr}(T(z)^n).\]
At \(z=2\) the characteristic polynomial is \(t^3-t^2-2t-2\). Cayley–Hamilton proves the stated recurrence and three initial values by direct matrix multiplication. Its unique positive root \(\lambda\) has largest modulus; its other roots are conjugate with modulus \(\sqrt{2/\lambda}<1\). Therefore \(\operatorname{tr}(T(2)^n)\sim\lambda^n\), proving the cycle asymptotic. The clique asymptotic follows from its explicit formula.

For the crossover, direct recurrence evaluation shows equality at \(n=3\), the strict clique inequality at each \(n=4,\ldots,16\), and the strict cycle inequality at \(n=17,18,19\):
\[(B_n^{\mathrm{cycle}},B_n^{\mathrm{clique}})=(1124381,1114113),(2551817,2359297),(5791429,4980737)\]
for these last three indices. If \(b_n=1+n2^{n-1}\), then for every \(n\ge9\),
\[b_{n-1}+2b_{n-2}+2b_{n-3}-b_n=(n-9)2^{n-3}+4>0.\]
The recurrence therefore propagates three consecutive strict cycle inequalities to every larger index by induction. This establishes the exact unique crossover.

Finally, the bipartite double cover of a cycle is two disjoint copies of that cycle when \(n\) is even, and a single cycle of length \(2n\) when \(n\) is odd. The standard recurrence for independent sets on a path and cyclic closure gives \(I(C_m)=L_m\), completing the recurrent-orbit specialization.

## Verification

The independent Python program `verify_nor.py` exhaustively verifies the map, periodic-phase correspondence and every individual attraction fiber over all labelled simple base graphs through four vertices (75 labelled graphs, 16,932 initial states). It independently checks the cycle transfer trace against direct independent-set enumeration for \(3\le n\le12\), checks the Lucas orbit census, and verifies the crossover with exact integer arithmetic through \(n=59\). The separate C++ program `verify_nor.cpp` exhaustively checks 1,065,508 labelled initial configurations over all 1,099 labelled simple base graphs on one through five vertices, including each phase-fiber weight and the total partition of initial states into basins. Neither finite check substitutes for the all-graph proof.

Reproduce with `python3 verify_nor.py` and `g++ -std=c++17 -O2 verify_nor.cpp -o verify_nor && ./verify_nor`. Reproduced outputs are provided in `verify_nor_output.txt` and `verify_nor_cpp_output.txt`; all input files and logs are included with this result.

## Relationship to prior work

Aledo, Martínez and Valverde's 2015 survey discusses the general recurrence theory of parallel Boolean graph dynamics, including minterm and maxterm NOR-type systems. Its surveyed local rules use the vertex's own input as well as a graph neighborhood, so the present **open-neighborhood** corona map is not the same local rule. General period-at-most-two conclusions, and the identity \(F^3=F\) for symmetric open-neighborhood NOR, are background and are not claimed as new. The claimed contribution is the explicit double-cover parametrization of all corona phases, an exact attraction-basin weight for **each** orbit, and the cycle–clique reversal at the sharp index \(17\). Later work by Aledo and collaborators on counting periodic states in parallel graph systems uses different local conventions and graph-dependent dominating-set reductions rather than these corona-specific basin formulas. No broad claim is made that the counting problem for independent sets or a three-term transfer recurrence is itself novel.

## Limitations

The formulas are for one private leaf per vertex and **open** NOR, not self-inclusive NOR, majority, NAND, or asynchronous dynamics. The cycle–clique reversal compares only the indicated two base families; it is not an extremal theorem over all graphs. The exact predecessor-fiber identity and the crossover are proved, but absence of an equivalent identity in every historical publication is not certified. The 2012 original maxterm/minterm article was identified through bibliographic records but its full text was not available in the inspected sources; an unknown historical specialization remains an originality risk. No independent external mathematical audit has been performed.

## References

- J. A. Aledo, S. Martínez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics **2015**, article 594294 (first published 24 March 2015), https://doi.org/10.1155/2015/594294.
- J. A. Aledo, S. Martínez, F. L. Pelayo, J. C. Valverde, *Parallel discrete dynamical systems on maxterm and minterm Boolean functions*, Mathematical and Computer Modelling **55** (2012), 666–671, https://doi.org/10.1016/j.mcm.2011.08.040. The exact first-online date and full text were not established here.
- J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan, J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity **2020**, article 9708347, https://doi.org/10.1155/2020/9708347.
