# Vertex-rich facets of odd-prism transportation balls

## Finding
Let \(n\ge3\) be odd, let \(G_n=C_n\square K_2\) be the circular ladder with \(2n\) vertices and \(3n\) unit edges, and let \(M_n\) be its shortest-path metric. The real Lipschitz-free unit ball \(B_n=B_{\mathcal F(M_n)}\) has dimension \(2n-1\). Every facet of \(B_n\) contains at most \(3n-2\) vertices. This maximum is attained, and the exact number of facets attaining it is
\[
E_n=2n\,[z^0](z^{-1}+1+z)^{n-1}
 =2n\sum_{j=0}^{(n-1)/2}\binom{n-1}{2j}\binom{2j}{j}.
\]
Here \([z^0]\) extracts the Laurent polynomial's constant coefficient. In particular, for \(n=3,5,7,9,11\), the numbers are \(18,190,1974,19926,196966\). As \(n\) tends to infinity through odd integers,
\[
E_n\sim 3^{n-1}\sqrt{\frac{3n}{\pi}}.
\]
Each maximizing facet is uniquely described by a choice of one rim edge and a normalized integer potential satisfying the rules in the proof. Exactly \(2[z^0](z^{-1}+1+z)^{n-1}\) maximizing facets correspond to each of the \(n\) possible common slack-edge positions. This counts **only the facets with the largest number of vertices**, not all facets of \(B_n\).

## Assumptions and scope
The graph vertices are \(a_i,b_i\), where \(i\in\mathbb Z/n\mathbb Z\), with top rim edges \(a_i a_{i+1}\), bottom rim edges \(b_i b_{i+1}\), and rungs \(a_i b_i\). All edges have length one. Regard the unit ball as
\[
B_n=\operatorname{conv}\{\pm(\delta_u-\delta_v):uv\in E(G_n)\}\subseteq\{\mu:\sum_v\mu(v)=0\}.
\]
Every displayed edge molecule is a distinct vertex of this ball: for an edge of unit length, its metric segment has no third point. A facet is a face of codimension one in the ambient \(2n-1\) dimensional zero-sum space. A normalized facet-defining potential is \(f:V(G_n)\to\mathbb Z\) with \(f(a_0)=0\). Its tight edges are those satisfying \(|f(u)-f(v)|=1\), and there is one vertex of \(B_n\) in its face for each tight undirected edge. No additional vertices come from non-edge pairs because their molecules lie in the convex hull of edge molecules.

## Proof
**1. Facet criterion.** A normalized real potential \(f\) defines a supporting hyperplane precisely when \(|f(u)-f(v)|\le1\) on each edge; it defines a facet precisely when its tight-edge graph is connected and spanning. Indeed, the tight edge-root vectors span a space of dimension \(|V|-c\), where \(c\) is the number of connected components of that graph. It is a facet when this dimension is \(|V|-1\). If the tight graph is spanning connected, differences of \(f\) along a spanning tree are integers, so after fixing \(f(a_0)=0\) the potential is integer valued. Conversely every integer potential meeting the two conditions defines a unique facet. This is the standard graph-facet criterion (References 1 and 2), recalled here to fix normalization.

**2. Sharp upper bound.** Since each rim is an odd cycle, the integer sum of its oriented increments is zero. All increments have values in \(\{-1,0,1\}\); the sum of an odd number of increments each in \(\{-1,1\}\) cannot be zero. Therefore each rim has at least one slack edge. Thus at least two of the \(3n\) graph edges are not tight, giving the bound \(3n-2\).

**3. Classification of equality.** For equality, every rung is tight and each rim has exactly one slack edge. Put \(r_i=f(b_i)-f(a_i)\in\{-1,1\}\), \(p_i=f(a_{i+1})-f(a_i)\), and \(q_i=f(b_{i+1})-f(b_i)\). These obey \(q_i=p_i+r_{i+1}-r_i\). If \(r_i\ne r_{i+1}\), admissibility \(|p_i|,|q_i|\le1\) forces \(p_i=r_i\) and \(q_i=-r_i\); both rim edges are tight. If \(r_i=r_{i+1}\), then \(q_i=p_i\). Consequently both rim slack edges must be the same edge \(e_j=(j,j+1)\); at that edge \(p_j=q_j=0\), while every other rim increment is \(\pm1\). Conversely any cyclic rung signs and increments obeying these transition rules and the closure equation \(\sum_i p_i=0\) determine an admissible integer potential, up to a common additive constant. Its tight graph contains every rung and, on either rim, the spanning path obtained by deleting \(e_j\); hence it is connected. Thus it defines a facet with exactly \(3n-2\) vertices.

**4. Exact enumeration.** Choose the common slack position \(j\) in \(n\) ways. At the slack edge the rung sign is unchanged. Along each of the remaining \(n-1\) directed edges, record the top increment by a weight \(z^{p_i}\). With row/column states \(r=+1,-1\), the one-edge transfer matrix is
\[
T(z)=\begin{pmatrix}z+z^{-1}&z\\z^{-1}&z+z^{-1}\end{pmatrix}.
\]
The diagonal transitions keep the rung sign and allow increments \(\pm1\); the off-diagonal transitions flip it and force increment equal to the departure sign. The slack edge has matrix \(I\). Closed rung signs are enumerated by a matrix trace, and the integer height closes exactly when its net increment is zero. Therefore
\[
E_n=n[z^0]\operatorname{tr}\bigl(T(z)^{n-1}\bigr).
\]
The eigenvalues of \(T(z)\), as a formal Laurent-polynomial matrix, are \(z+z^{-1}+1\) and \(z+z^{-1}-1\); hence the trace is their \((n-1)\)-st powers' sum. Since \(n-1\) is even, the constant coefficients of these two powers agree: their difference consists of terms with an odd power of \(z+z^{-1}\), whose constant coefficient vanishes. This gives the stated \(2n\) times central-trinomial formula. Every choice is counted once, because a maximizing potential has a unique common slack edge and normalization fixes its additive constant.

**5. Asymptotics.** The coefficient \([z^0](z^{-1}+1+z)^m\) counts zero-displacement walks of length \(m\) with uniformly chosen steps \(-1,0,1\). The lattice local central limit theorem (step variance \(2/3\), span one) gives \(3^m\sqrt{3/(4\pi m)}(1+o(1))\). Substitution \(m=n-1\) proves the asserted asymptotic.

## Verification
The accompanying standalone Python program `verify_odd_prism.py` requires only the standard library. It performs (a) an independent Laurent-polynomial transfer expansion for odd \(n\le29\) and (b) direct exhaustive generation of all normalized integer edge-Lipschitz potentials for \(n=3,5,7\). For each directly generated potential it tests edge constraints, counts tight edges, and, when the maximum is reached, independently checks connectivity by graph traversal. All resulting maximum-facet counts are \(18,190,1974\) as predicted. These finite computations are corroboration; the proof above establishes the theorem for every odd \(n\).

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018) proved the general facet-potential criterion for symmetric edge polytopes. D'Alì, Delucchi and Michałek (2019) studied graph-metric interpretations, cycle and wheel facet enumeration, and a nowhere-zero-flow method for **bipartite planar graphs**. The odd prism is nonbipartite and this latter result does not enumerate its facets. Braun and Bruegge (2023) provide graph-family facet counts for sparse graphs and reproduce the general criterion, but their explicit graph constructions concern trees, few-cycle graphs, and parallel-path graphs, not this odd-prism maximizing layer. Aliaga (2021) establishes general extremal structure for Lipschitz-free unit balls rather than the vertex-rich facet multiplicities of this family. The present claim evaluates a specific, geometrically motivated top-support layer: the sharp maximum number of vertices on any facet and the precise number of maximizing facets, not merely a general rephrasing of the existing criterion.

## Limitations
No total facet count, full face vector, or complete classification of smaller facets is claimed. The formula applies to the real space and unit-edge odd circular ladders only. The known broad graph-facet characterization is reused, not claimed as new. No independent external audit has been conducted; an equivalent unindexed formula could exist.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public 2018-07-20), §3.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), Theorem 3.1, §4.5.
3. B. Braun, K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, Journal of Integer Sequences 26 (2023), Article 23.7.2, §§2–4.
4. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1 (first public 2021-02-01), Theorem 1.
