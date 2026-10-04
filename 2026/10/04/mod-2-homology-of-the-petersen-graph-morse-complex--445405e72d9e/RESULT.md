# Mod-2 homology of the Petersen graph Morse complex

## Finding
For the Petersen graph \(P\), the ordinary Morse complex \(\mathcal M(P)\) of discrete gradient vector fields has reduced mod-2 homology
\[
\widetilde H_i(\mathcal M(P);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{38},& i=7,\\
\mathbb F_2^{294},& i=8,\\
0,&\text{otherwise}.
\end{cases}
\]
The nonempty face vector, indexed by dimensions \(0,\ldots,8\), is
\[
(30,390,2880,13305,39882,77640,94800,66000,20000).
\]

## Assumptions and scope
The Petersen graph is presented on vertices \(0,\ldots,9\) with the outer cycle \(0,1,2,3,4,0\), spokes joining \(i\) to \(5+i\), and inner edges joining \(5+i\) to \(5+(i+2\bmod 5)\). A vertex of \(\mathcal M(P)\) is a primitive discrete vector \((v,e)\) with \(v\) incident to \(e\). A simplex is a set of pairwise compatible primitive vectors containing no closed \(V\)-path. For a graph, this is equivalently an acyclic partial orientation in which each vertex has outdegree at most one and no edge is chosen from both ends.

The claim is only about reduced homology with coefficients in \(\mathbb F_2\). It does not assert integral homology, torsion-freeness, a wedge decomposition, or a complete homotopy type.

## Proof
Write a chosen primitive vector \((v,\{v,w\})\) as an arrow \(v\to w\). Every face is then a partial function from the ten graph vertices to adjacent vertices, with three constraints: a vertex is a tail at most once, an unoriented edge cannot be selected from both ends, and the resulting directed graph has no directed cycle. Conversely, those three conditions give an acyclic matching in the vertex-edge Hasse diagram, hence a simplex of \(\mathcal M(P)\).

Exhausting the four choices at each graph vertex—no outgoing arrow or one of its three neighbors—gives \(4^{10}=1,048,576\) raw assignments. Filtering by the matching and acyclicity conditions gives face counts by cardinality \(k=0,\ldots,9\)
\[
(1,30,390,2880,13305,39882,77640,94800,66000,20000).
\]
As an independent count, let \(L\) be the Petersen graph Laplacian. The matrix-forest theorem identifies the coefficient of \(x^k\) in \(\det(I+xL)\) with the number of rooted spanning forests with \(k\) edges. A graph Morse face is exactly such a rooted forest with every tree oriented toward its selected root, so the sums of all principal \(k\)-minors of \(L\) reproduce the same ten counts.

Over \(\mathbb F_2\), form the reduced simplicial boundary maps, including the augmentation in cardinality one. Exact bitset Gaussian elimination gives ranks, for cardinalities \(1,\ldots,9\),
\[
(1,29,361,2519,10786,29096,48544,46256,19706).
\]
For \(k\)-element faces, dimension is \(k-1\), so
\[
\beta_{k-1}=f_k-\operatorname{rank}(\partial_k)-\operatorname{rank}(\partial_{k+1}).
\]
Substitution yields zero through dimension \(6\), then \(38\) in dimension \(7\) and \(294\) in dimension \(8\), as claimed.

## Verification
The accompanying `artifacts/verify.py` reconstructs the Petersen graph from the stated presentation, exhausts all \(4^{10}\) tail assignments, verifies simplicial closure, and independently recomputes every face count from principal Laplacian minors using exact Bareiss determinants. It then constructs the complete reduced mod-2 boundary complex and computes every rank twice: once by highest-pivot forward elimination and once by lowest-pivot reverse elimination. Both routes return the stated rank vector. The script also checks the reduced Euler characteristic in two independent forms and terminates with `PETERSEN_MORSE_VERIFY_OK`.

## Relationship to prior work
Donovan, Lin, and Scoville develop homotopy methods for ordinary Morse complexes and compute several graph families, while Scoville and Zaremsky establish general connectivity bounds. Neither result determines the exact homology of the Petersen case. The 2026 paper of Knudson and Owens-White emphasizes that ordinary Morse-complex homotopy types are still known only for a limited collection of standard families; its new computations concern the distinct strong-discrete-Morse subcomplex. Exact searches for Petersen/Morse-complex aliases and for the numerical Betti pair did not locate a published statement implying the result here.

## Limitations
The computation is finite and exact for this one graph. It does not prove an integral homology statement, does not exclude odd-primary or integral torsion, and does not identify attaching maps or a homotopy decomposition. A non-indexed computation or unpublished table could duplicate the numerical result; the literature comparison therefore supports originality but is not a proof of global uniqueness.

## References
1. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1 (2019); doi:10.4153/S0008439522000121.
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1 (2020).
3. K. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (2026).
