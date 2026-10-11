# Second off-diagonal magnitude homology of the Tutte–Coxeter graph
## Finding
Let \(T\) be the Tutte–Coxeter graph with its shortest-path metric. Over \(\mathbb F_2\), the endpoint-localized bidegree-\((3,5)\) magnitude homology satisfies
\[
\dim_{\mathbb F_2}\operatorname{MH}^{x,y}_{3,5}(T;\mathbb F_2)=
\begin{cases}
0,&d(x,y)=1,\\
4,&d(x,y)=3,
\end{cases}
\]
for ordered endpoints \(x,y\) in opposite bipartition classes; for same-side endpoints the length-\(5\) chain groups are zero. Consequently \(\dim_{\mathbb F_2}\operatorname{MH}_{3,5}(T;\mathbb F_2)=1440\). Every ordered distance-\(3\) pair has a unique three-edge geodesic, and that geodesic is contained in exactly four \(8\)-cycles.


## Assumptions and scope
The Tutte–Coxeter graph is taken in its standard realization as the point-line incidence graph of the generalized quadrangle \(\mathrm{GQ}(2,2)\). It is a bipartite cubic graph on \(30\) vertices with girth \(8\). Magnitude chains use the graph shortest-path metric and the standard smooth-point deletion differential. Coefficients are only asserted over \(\mathbb F_2\), and the claim concerns only bidegree \((3,5)\).

For fixed ordered endpoints \(x,y\), write \(C_k^{x,y}\) for the length-\(5\) magnitude chain group in homological degree \(k\). Since a bipartite graph has distance parity determined by the two bipartition classes, an odd total length forces opposite-side endpoints. Thus every same-side localized length-\(5\) chain group is zero.

## Proof
A complete finite chain calculation proves the statement. The graph is reconstructed without an external graph table from the symplectic model of \(\mathrm{GQ}(2,2)\): the points are the \(15\) one-dimensional subspaces of \(\mathbb F_2^4\), the lines are the \(15\) totally isotropic two-dimensional subspaces for the standard nondegenerate alternating form, and incidence gives the edges. This produces \(30\) vertices and \(45\) edges, each vertex of degree \(3\).

For every ordered opposite-side endpoint pair, the verifier enumerates all tuples of total metric length \(5\) in degrees \(2,3,4\), constructs the two boundary matrices over \(\mathbb F_2\), checks \(\partial_3\partial_4=0\), and performs exact bitwise Gaussian elimination. There are exactly two endpoint profiles.

If \(d(x,y)=1\), then
\[
(\dim C_2^{x,y},\dim C_3^{x,y},\dim C_4^{x,y})=(8,36,56),
\]
while
\[
(\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)=(8,28).
\]
Hence
\[
\dim \operatorname{MH}^{x,y}_{3,5}=36-8-28=0.
\]

If \(d(x,y)=3\), then
\[
(\dim C_2^{x,y},\dim C_3^{x,y},\dim C_4^{x,y})=(14,45,40),
\]
and
\[
(\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)=(14,27).
\]
Therefore
\[
\dim \operatorname{MH}^{x,y}_{3,5}=45-14-27=4.
\]

The exhaustive endpoint scan finds \(90\) ordered distance-\(1\) pairs and \(360\) ordered distance-\(3\) pairs. Thus
\[
\dim_{\mathbb F_2}\operatorname{MH}_{3,5}(T;\mathbb F_2)=360\cdot4=1440.
\]
Equivalently, summing the endpoint blocks gives global chain dimensions \((5760,19440,19440)\) in degrees \((2,3,4)\) and boundary ranks \((5760,12240)\).

Finally, girth \(8\) implies that every distance-\(3\) pair has a unique three-edge geodesic, since two distinct such geodesics would create a cycle of length at most \(6\). Independent enumeration finds exactly \(90\) simple \(8\)-cycles and checks that each ordered distance-\(3\) pair has its unique geodesic contained in exactly four of them.

## Verification
Run `python verify_tutte_coxeter_mh.py` using the accompanying standalone Python file. It uses only the standard library. It reconstructs \(\mathrm{GQ}(2,2)\), computes all shortest-path distances, enumerates every relevant localized magnitude chain, checks the chain condition, computes all boundary ranks over \(\mathbb F_2\), verifies every endpoint block, counts all \(8\)-cycles, and reproduces the total rank \(1440\). The saved output is in `tutte_coxeter_verify_output.txt`.

## Relationship to prior work
Asao, Hiraoka and Kanazawa prove girth-controlled vanishing of near-diagonal magnitude homology by algebraic Morse theory. Their theorem gives the relevant second-off-diagonal vanishing once the girth reaches the next threshold; the Tutte–Coxeter graph has girth \(8\), so it lies at the sharp boundary not forced to vanish by that result. Their full text does not compute the Tutte–Coxeter graph or the endpoint-localized bidegree \((3,5)\) ranks above. The closest previously checked projective-incidence magnitude result concerns bidegree \((3,4)\) for finite projective planes, rather than the girth-eight generalized-quadrangle graph and bidegree \((3,5)\).

The Tutte–Coxeter graph is a particularly natural boundary example: it is the unique \((3,8)\)-cage and the incidence graph of \(\mathrm{GQ}(2,2)\). Thus the computation is an exact value at the first girth where the second off-diagonal can survive, rather than an arbitrary finite graph calculation.

## Limitations
No claim is made over \(\mathbb Z\) or over fields of odd characteristic, and no other magnitude-homology bidegree is determined. The equality between the local rank \(4\) and the number of \(8\)-cycles through the unique distance-\(3\) geodesic is established for this graph; no general cycle-count theorem for all girth-eight graphs is asserted.

## References
1. Y. Asao, Y. Hiraoka, S. Kanazawa, “Girth, magnitude homology, and phase transition of diagonality,” arXiv:2101.09044v1; DOI 10.1017/prm.2023.7.
2. R. Hepworth, S. Willerton, “Categorifying the magnitude of a graph,” arXiv:1505.04125.
3. G. Exoo, R. Jajcay, “Dynamic Cage Survey,” Electronic Journal of Combinatorics, Dynamic Survey DS16; section on the Tutte–Coxeter graph.
