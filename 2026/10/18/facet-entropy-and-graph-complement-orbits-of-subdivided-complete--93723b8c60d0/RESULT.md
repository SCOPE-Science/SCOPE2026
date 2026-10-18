# Facet entropy and graph-complement orbits of subdivided complete-graph transportation balls

## Finding
For each integer \(n\ge 2\), subdivide every edge of \(K_n\) once, obtaining the connected bipartite graph \(H_n=S(K_n)\). Equip its vertices with unit-edge shortest-path distance. Let \(B_n\) be the unit ball of the real Lipschitz-free space over this finite metric. Write \(M=\binom n2\). Its exact number of facets is
\[
\boxed{F_n=2^M+\sum_{k=1}^{n-1}\binom nk\,2^{\binom k2+\binom{n-k}2}.}
\]
The first values for \(n=2,3,4,5,6\) are \(4,20,152,1984,50176\). Moreover, as \(n\to\infty\),
\[
\boxed{F_n=2^M\bigl(1+n2^{2-n}+O(n^2 2^{-2n})\bigr).}
\]
In particular, a proportion tending to one of the facets have supporting potentials constant on the original \(n\) vertices.

For \(n\ge4\), let \(a_j\) denote the number of isomorphism classes of simple undirected graphs on \(j\) vertices, and let \(b_j\) denote the number of those classes after additionally identifying every graph with its complement. The facets of \(B_n\), under graph automorphisms of \(H_n\) and global negation of their supporting functionals, form exactly
\[
\boxed{O_n=b_n+\sum_{k=1}^{\lfloor(n-1)/2\rfloor} a_k a_{n-k}
+\mathbf 1_{\{2\mid n\}}\frac{a_{n/2}(a_{n/2}+1)}2}
\]
orbits. Thus \(O_4=13\) and \(O_5=37\). The proof gives a canonical combinatorial description of each orbit, not just its total count.

## Assumptions and scope
The original vertices are \(p_1,\ldots,p_n\). The subdivision vertex \(q_{ij}\) is adjacent precisely to \(p_i,p_j\), for \(1\le i<j\le n\). Thus \(H_n\) has \(n+M\) vertices, \(2M\) edges, and \(B_n\) is a full-dimensional polytope in the \((n+M-1)\)-dimensional real Lipschitz-free space.

Fix \(p_1\) as base point. Duality identifies \(B_n^\circ\) with the Lipschitz unit ball
\[
P_n=\{f:V(H_n)\to\mathbb R:f(p_1)=0,\ |f(u)-f(v)|\le1\ \text{on every edge }uv\}.
\]
Because graph distance is a shortest-path metric, edge inequalities imply all pairwise metric inequalities. A facet of \(B_n\) is dual to a vertex of \(P_n\); supporting potentials differing by constants represent the same normalized functional. For the orbit statement, the acting group is exactly \(\operatorname{Aut}(H_n)\times\{\pm1\}\); no assertion is made about the full linear automorphism group of the polytope.

## Proof
**1. A dual vertex on a connected bipartite unit-edge graph saturates every edge.** For an arbitrary connected finite graph, let \(T_f\) contain the edges at which \(|f(u)-f(v)|=1\). The active inequality normals are the signed edge-incidence vectors. Their rank modulo constants is \(|V|-c(T_f)\), where \(c(T_f)\) is the number of connected components. Hence \(f\) is a vertex of its normalized Lipschitz polytope if and only if \(T_f\) is connected.

Suppose now that the graph is bipartite and \(T_f\) is connected. Along any path in \(T_f\), heights change by integral increments \(\pm1\). Starting from a base point at zero, all heights are integers and have parity prescribed by their bipartition class. Every graph edge therefore joins two heights of opposite parity. Its difference is an odd integer of absolute value at most one, so it has absolute value exactly one. Conversely, if all edges are tight then \(T_f\) is the whole connected graph and \(f\) is extreme. Thus for \(H_n\), dual vertices are *exactly* the normalized height assignments making every edge tight.

**2. Classification by the original heights.** Write \(h_i=f(p_i)\). The equations \(|h_i-f(q_{ij})|=|h_j-f(q_{ij})|=1\) imply \(h_i-h_j\in\{-2,0,2\}\), because \(p_i\) and \(p_j\) have a common neighbor. Hence all original heights belong to one even lattice and have total range at most two. After translating by a constant, either (i) every original height is zero, or (ii) the originals occupy both heights zero and two.

In case (i), each \(q_{ij}\) independently has height \(+1\) or \(-1\), giving \(2^M\) normalized potentials. In case (ii), choose the nonempty proper set \(A=\{i:h_i=0\}\), of size \(k\), and its complement \(B=\{i:h_i=2\}\). For every cross-pair \(i\in A,j\in B\), the midpoint is forced to height one; for every pair within \(A\), it independently has height \(-1\) or \(+1\); for every pair within \(B\), it independently has height one or three. Thus each such \(A\) gives exactly \(2^{\binom k2+\binom{n-k}2}\) potentials. The cases are mutually disjoint and exhaust every vertex of \(P_n\), proving the formula for \(F_n\) by polarity.

**3. Symmetry orbits.** For \(n\ge4\), original vertices have degree \(n-1\ge3\), whereas subdivision vertices have degree two. Any automorphism must permute originals and hence act as one of the \(n!\) permutations of their labels. Conversely every permutation extends to an automorphism, so \(\operatorname{Aut}(H_n)\cong S_n\).

In case (i), encode every subdivision sign \(+1\) as an edge of an arbitrary graph \(L\) on \(\{1,\ldots,n\}\). Permutations relabel \(L\); global negation complements its edge set. Therefore these facets yield precisely \(b_n\) orbits.

In case (ii), encode independently the choices on within-\(A\) subdivision vertices by an arbitrary labeled graph \(L_A\), and similarly the choices on within-\(B\) vertices by \(L_B\): an edge means the midpoint lies *above* both of its original endpoints. For each fixed size \(|A|=k\), label permutations reduce the pair to an ordered pair of unlabeled graph classes of sizes \(k\) and \(n-k\), hence \(a_ka_{n-k}\) types. Global negation swaps lower and upper classes and reverses the above/below choice, acting by
\[
([L_A],[L_B])\longmapsto([\overline L_B],[\overline L_A]).
\]
When \(k<n-k\), this identifies the size-\(k\) and size-\(n-k\) strata, leaving \(a_ka_{n-k}\) orbits. If \(n=2k\), the involution acts on a set of size \(a_k^2\); it fixes exactly \(a_k\) ordered pairs, one for every choice of \([L_A]\), since \([L_B]=[\overline L_A]\). Burnside's lemma gives \((a_k^2+a_k)/2\) orbits. Summing gives \(O_n\). This classification includes all stabilizer types and is valid regardless of whether an unlabeled graph is self-complementary.

**4. Concentration estimate.** Divide the facet formula by \(2^M\). Since
\[
\binom k2+\binom{n-k}2=M-k(n-k),
\]
we obtain \(F_n/2^M=1+\sum_{k=1}^{n-1}\binom nk2^{-k(n-k)}\). Terms \(k=1,n-1\) total \(n2^{2-n}\). Terms \(k=2,n-2\) are \(O(n^2 2^{-2n})\). The remaining terms are smaller in aggregate: for \(3\le k\le n/6\), geometric summation bounded by \(\sum_{k\ge3}n^k2^{-5kn/6}\) gives \(O(n^3 2^{-5n/2})\); for \(n/6<k\le n/2\), their sum is at most \(2^n2^{-5n^2/36+O(n)}\), and the other half is symmetric. This proves the asymptotic estimate and the facet-concentration assertion.

## Verification
The standalone `verify.py` reconstructs the graph directly and uses a rooted spanning tree, rather than the closed-form classification, to enumerate every unit-edge-tight assignment for \(2\le n\le6\). It independently compares the cardinalities with the displayed formula. For \(n=4,5\), it applies all \(n!\) original-vertex automorphisms and sign reversal to the enumerated facets, constructs the actual orbits, and compares their number with a separate enumeration of unlabeled graph classes and complement classes. This finite exact computation checks the boundary cases and symmetry bookkeeping; only the analytic argument establishes the universal formula.

Run `python verify.py`. The executable reported `ALL EXACT CHECKS PASSED` for \(F_2=4,F_3=20,F_4=152,F_5=1984,F_6=50176\) and \(O_4=13,O_5=37\). The unequal-degree assumption for the orbit claim first holds at \(n=4\); the facet-count formula itself holds for \(n=2,3\) as well.

## Relationship to prior work
D'Alì, Delucchi and Michałek develop facets of symmetric edge polytopes and show, in particular, that for connected bipartite graphs the facet potentials have every edge tight. This general criterion explains the first step of our proof, but does not evaluate the facet count of the once-subdivided complete graph or classify its facets modulo automorphisms and negation. Higashitani, Jochemko and Michałek likewise provide general facet techniques and specific graph-family enumerations, not this metric family's graph-complement orbit structure. Chen, Davis and Korchevskaia study general facet subgraphs and fibers, but do not give the above explicit formulas for \(S(K_n)\).

An accessible exact-object calculation studies the Vietoris--Rips filtration of \(S(K_n)\), rather than facets or dual Lipschitz potentials. Another exact facet calculation treats equilateral metrics with disjoint shortened pairs, which are not graph-shortest-path metrics of the incidence graph \(S(K_n)\). Neither theorem implies the enumerations here. The finite-dimensional free-space framework is standard; the claimed new work is the evaluated formula, the graph-complement orbit classification, and concentration asymptotics.

## Limitations
The graph has exactly one subdivision vertex per edge, every graph edge has unit length, and the scalar field is real. The orbit classification is under graph automorphisms and global negation, rather than all possible linear isometries. There is no claim about higher face numbers, weighted subdivisions, or subdivision graphs of arbitrary source graphs. An equivalent enumeration in poorly indexed literature remains possible; exact computer checks by themselves do not prove originality or the all-parameter theorem. No independent external scientific audit has been performed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first public 2018-07-20), https://arxiv.org/abs/1807.07678.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (first public 2019-10-11), https://arxiv.org/abs/1910.05193.
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 2021-07-26), https://arxiv.org/abs/2107.12315.
4. A. Alexander, M. Fradelizi, G. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11), https://arxiv.org/abs/1911.10642.
