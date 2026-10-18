# Exact facet generating function for squared-path Lipschitz-free balls

## Finding
For every integer \(n\ge2\), let \(M_n=\{1,\dots,n\}\) have metric \(d(i,j)=\lceil |i-j|/2\rceil\), the shortest-path distance in the squared path \(P_n^2\). The real Lipschitz-free space \(\mathcal F(M_n)\) has a unit ball with exactly \(F_n\) facets, where
\[
\sum_{n\ge2}F_nz^n=\frac{2z^2(1+z)^2}{1-z-2z^2-2z^3}.
\]
Thus \(F_2=2\), \(F_3=6\), \(F_4=12\) and, for every integer \(n\ge5\),
\[
F_n=F_{n-1}+2F_{n-2}+2F_{n-3}.
\]
The first values are \(2,6,12,28,64,144,328,744,1688,3832\). The result includes a finite-state classification of every facet via connected tight-edge graphs.

## Assumptions and scope
All scalars are real. The squared path \(P_n^2\) has vertices \(1,\dots,n\), with an edge between distinct vertices at index distance one or two. Every edge has length one. The metric \(d(i,j)=\lceil|i-j|/2\rceil\) is the resulting graph metric. A base point, fixed at vertex \(1\), identifies the dual space \(\operatorname{Lip}_0(M_n)\) with the integer-dimensional real space of functions \(f\) satisfying \(f(1)=0\); the dual unit ball is cut out by \(|f(i)-f(j)|\le1\) on graph edges. A facet of the primal unit ball corresponds, by finite-dimensional polarity, to a vertex of that dual unit ball. Each such vertex is counted separately, including its antipode.

## Proof
**Tight-edge characterization.** Let \(L_n\) be the dual Lipschitz unit ball. Given \(f\in L_n\), form its tight-edge subgraph from those edges \(\{i,j\}\) with \(|f(i)-f(j)|=1\). Its vertex-spanning connected components describe the common kernel of all active equality constraints: vectors constant on each component. With \(f(1)=0\), the active constraint rank is \(n-c\), where \(c\) is the number of tight-edge components, so the face of \(L_n\) containing \(f\) has dimension \(c-1\). Consequently \(f\) is a vertex precisely if the tight-edge graph is connected. For a connected tight graph, a spanning tree determines all differences from the base point as sums of \(\pm1\), so every vertex height is an integer. In particular, consecutive increments belong to \(\{-1,0,1\}\); no continuous vertices are omitted in what follows.

**Complete boundary states.** Scan vertices from left to right. For a processed prefix of length at least two, write \(d=f(k)-f(k-1)\in\{-1,0,1\}\). Write \(c=1\) if the last two vertices are joined in the tight-edge subgraph restricted to that prefix, and \(c=0\) otherwise. Retain only partial labelings whose tight graph has no component disjoint from the last two vertices. This restriction loses no full connected graph: an abandoned component cannot ever reconnect, since later edges reach back at most two indices. Conversely, all partial tight components therefore have a boundary representative, so their full connectivity partition is determined by \(c\). The ordered state set is
\[
S=\{(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1)\}.
\]
When the current last two heights are \(0,d\), a prospective next increment \(e\in\{-1,0,1\}\) gives the next height \(d+e\). The prospective transition is admissible exactly when \(|d+e|\le1\), and, after merging the old boundary vertices if \(c=1\), merging old-first with new if \(|d+e|=1\), and merging old-second with new if \(|e|=1\), the old-first component remains represented by one of the new boundary vertices. The successor flag is \(1\) precisely when the new boundary vertices are connected in these merged components. This rule accounts for every extension exactly once.

In the stated order the integer transition matrix is
\[
T=\begin{pmatrix}
0&0&1&0&0&0\\
0&0&0&1&0&1\\
0&1&0&0&0&1\\
0&1&1&0&0&1\\
0&0&1&0&0&0\\
0&1&0&1&0&0
\end{pmatrix}.
\]
Initially \(f(1)=0\), with one value \(f(2)\in\{-1,0,1\}\) for each admissible initial state; the row of initial counts is \(v=(0,1,1,0,0,1)\). At the end the tight graph is connected exactly when \(c=1\), detected by the terminal column \(w=(0,1,0,1,0,1)^{\mathsf T}\). Consequently, by induction on the scan length,
\[
F_n=vT^{n-2}w\qquad(n\ge2).
\]
This establishes both the facet classification and the exact finite-state count, without numerical extrapolation.

**Rational simplification.** Direct multiplication of the six displayed rows and columns gives
\[
vT^3=vT^2+2vT+2v.
\]
Multiplication on the right by any nonnegative power of \(T\) and then by \(w\) proves \(F_n=F_{n-1}+2F_{n-2}+2F_{n-3}\) for every \(n\ge5\). Direct evaluation gives \(F_2=vw=2\), \(F_3=vTw=6\), and \(F_4=vT^2w=12\). Multiplying the resulting generating function by \(1-z-2z^2-2z^3\) yields \(2z^2+4z^3+2z^4\), proving the displayed identity for formal power series (and analytically for sufficiently small \(|z|\)). No finite experimental fit is used in this proof.

## Verification
Run \(\texttt{python3 verify_facets.py}\) from the directory containing the attached standalone program. The checker reconstructs the exact six-state transition rule, checks the key row identity, and independently enumerates all possible integer-valued feasible Lipschitz potentials for \(2\le n\le11\), testing connectivity of their saturated-edge graphs directly. It also compares the first 63 generated terms against the recurrence. These finite computations are corroborations of the general proof, not replacements for it.

## Relationship to prior work
The Banach-space framework is that of finite Lipschitz-free spaces and their dual Lipschitz balls; see Alexander–Fradelizi–García-Lirola–Zvavitch (arXiv:1911.10642) and Aliaga (arXiv:2102.01219). The characterization of facets by integral labelings and connected saturated-edge graphs is a specialization of general symmetric-edge-polytope theory, for example D'Alì–Delucchi–Michałek (2022, Theorem 11) and Chen–Davis–Korchevskaia (arXiv:2107.12315). Braun–Bruegge (arXiv:2201.13303) enumerate facets for certain sparse families including graphs with at most two independent cycles and windmills. Those general descriptions and restricted-family counts do not state the present squared-path recurrence or its all-dimensional rational generating function. The edge-gluing multiplicative result in D'Alì–Delucchi–Michałek (Proposition 37) requires bipartite factors, whereas the squared path contains overlapping triangles. The capped ordinary-path metric \(\min\{|i-j|,2\}\) is a different metric and does not yield the numbers above.

## Limitations
This theorem counts facets of the real Lipschitz-free unit ball only, not the entire face vector, and gives no claim about complex scalar spaces or arbitrary powers of paths. Its originality is assessed against the specifically inspected literature and available research records, not guaranteed against inaccessible or unindexed results. Independent validation has not been performed.

## References
1. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public version, 2019-11-24), https://arxiv.org/abs/1911.10642.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public version, 2021-02-01), primary MSC2020 46B20, https://arxiv.org/abs/2102.01219.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public version, 2021-07-26), https://arxiv.org/abs/2107.12315.
4. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, Electronic Journal of Combinatorics 29(3) (2022), P3.24, https://doi.org/10.37236/10387.
5. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (first public version, 2022-01-31), https://arxiv.org/abs/2201.13303.
