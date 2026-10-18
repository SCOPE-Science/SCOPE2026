# A sharp alphabet transition in the skeleton metrics of complete layered path polytopes

## Finding

Let \(k\ge1\), and let \(n_1,\ldots,n_k\ge2\) be integers. Define a directed acyclic network with a source, a sink, internal layers \(L_i\) of cardinality \(n_i\), and **all** arcs from each layer to the next, including arcs from the source to \(L_1\) and from \(L_k\) to the sink. Let \(P\) be the convex hull, in arc-incidence coordinates, of its source-to-sink paths, and let \(\Gamma\) be the one-skeleton graph of \(P\). Identify a path with its sequence \(x=(x_1,\ldots,x_k)\), where \(x_i\in L_i\).

**Theorem.** Two distinct paths \(x,y\) are adjacent in \(\Gamma\) precisely when their disagreement set \(\{i:x_i\ne y_i\}\) is a nonempty interval of integers. In particular, \(\Gamma\) is connected and regular, has \(N=\prod_{i=1}^k n_i\) vertices, and has degree
\[
 d=\sum_{1\le a\le b\le k}\prod_{i=a}^b(n_i-1).
\]
Its number of edges is \(Nd/2\).

For each sign vector \(\eta=(\eta_1,\ldots,\eta_k)\) with \(\eta_i\in\{n_i-1,-1\}\), set
\[
 \Lambda(\eta)=d-\sum_{1\le a\le b\le k}\prod_{i=a}^b\eta_i,
 \qquad m(\eta)=\prod_{i:\eta_i=-1}(n_i-1).
\]
The full combinatorial Laplacian spectrum of \(\Gamma\), counting repeated values with their summed multiplicities, is \(\Lambda(\eta)\) with multiplicity \(m(\eta)\). The all-positive signature contributes the sole zero eigenvalue. Therefore the exact number of spanning trees is
\[
 \boxed{\displaystyle \tau(\Gamma)=\frac1N\!
 \prod_{\eta\ne(n_1-1,\ldots,n_k-1)}\!
 \Lambda(\eta)^{m(\eta)}.}
\]

For the *uniform* layer size \(n_i=q\ge2\), the exact graph-distance behavior has a sharp threshold:

* If \(q=2\), then the distance between paths is the number of maximal runs of disagreements. At every vertex, the number of vertices at distance \(r\) is \(\binom{k+1}{2r}\) for \(0\le r\le\lceil k/2\rceil\). Consequently,
\[
 \operatorname{diam}(\Gamma)=\lceil k/2\rceil,
 \qquad W(\Gamma)=(k+1)2^{2k-3},
\]
where \(W\) is the sum of unordered pairwise graph distances. The complete Laplacian spectrum simplifies to \(2j(k+1-j)\) with multiplicity \(\binom kj\), for \(0\le j\le k\). Moreover \(\Gamma\) is isomorphic to the familiar halved cube graph on \(k+1\) coordinates; the standard distance and spectral properties of that graph are not claimed as independently novel.

* If \(q\ge3\), put
\[
 d_{q,k}=\sum_{j=1}^k(k-j+1)(q-1)^j.
\]
For \(k=1,2\) the skeleton is complete; for **every** \(k\ge3\) it has diameter exactly \(2\), independently of the number of layers. At any vertex its distance generating polynomial is
\[
 \boxed{\displaystyle 1+d_{q,k}t+(q^k-1-d_{q,k})t^2,}
\]
and its Wiener index is
\[
 \boxed{\displaystyle W(\Gamma)=q^k(q^k-1)-\frac{q^kd_{q,k}}2.}
\]
At \(k\ge5\), changing the common layer cardinality from \(2\) to \(3\) thus changes the skeleton diameter from \(\lceil k/2\rceil\), unbounded as \(k\) grows, to \(2\), although both families have exponentially many vertices.

## Assumptions and scope

Each directed layer transition is complete, there are no arcs skipping layers, each internal layer contains at least two vertices, and \(P\) uses the original arc coordinates (not a projection that could change adjacencies). Each source-to-sink path uses exactly one vertex in each internal layer, hence exactly \(k+1\) arcs. The graph distance and spanning-tree number concern the **one-skeleton of the polytope**, not the underlying directed network. The formula for \(\tau\) is valid for every nonuniform layer profile; the explicit graph-distance formulas in the theorem are asserted only for uniform layer sizes. No formula for arbitrary nonuniform-profile graph distance is asserted.

## Proof

**1. Vertex and edge characterization.** Every path incidence vector is a vertex: assign weight \(1\) to its used arcs and weight \(0\) elsewhere. It is the unique path maximizing that linear functional, because every other path, of the same \(k+1\)-arc length, omits at least one of those arcs.

Fix two distinct paths \(x,y\). Split \(\{i:x_i\ne y_i\}\) into \(r\ge1\) maximal consecutive runs. The face exposed by setting all arc coordinates **outside** the union of the two paths to zero is the convex hull of the paths using only arcs in this union. At each mismatch run there are two possible alternative branches; at the intervening equal-position layers the branches rejoin. Hence there are exactly \(2^r\) supported paths. If \(r=1\), these are precisely \(x,y\), so their segment is an exposed edge. If \(r\ge2\), exchange the selected branch for exactly the first run between \(x\) and \(y\), producing two other distinct paths \(u,v\) in the same face. Arc-by-arc, \(\chi_x+\chi_y=\chi_u+\chi_v\). Thus the midpoint of \([\chi_x,\chi_y]\) is also a midpoint of two other polytope vertices, and the original segment cannot be an edge. This proves the adjacency criterion without requiring nondegeneracy of the flow polytope.

**2. Degree and general spectrum.** For any given vertex \(x\), its neighbors are obtained by choosing one interval \([a,b]\) and replacing each coordinate there with a different symbol; the total number of choices for that interval is \(\prod_{i=a}^b(n_i-1)\), and distinct intervals give distinct neighbors. This proves \(d\), regularity, and the edge count. Single-coordinate changes are permitted, proving connectivity. On the space of functions on \(L_i\), let \(B_i=J_{n_i}-I_{n_i}\), the adjacency matrix of a complete graph. The total adjacency operator is the sum, over intervals \([a,b]\), of the tensor product with \(B_i\) inside the interval and \(I_{n_i}\) outside it. The constant subspace has \(B_i\)-eigenvalue \(n_i-1\); its orthogonal complement has \(B_i\)-eigenvalue \(-1\) with dimension \(n_i-1\). Diagonalizing the commuting tensor factors proves the entire spectrum and multiplicities. Because the graph is connected, the all-positive signature is the unique Laplacian zero eigenvalue. Kirchhoff's matrix-tree theorem gives the exact product for \(\tau\). All factors are positive integers for nontrivial signatures.

**3. Binary graph distances and spectrum.** With two symbols, take their coordinatewise exclusive-or word \(z\). One skeleton step toggles precisely one contiguous interval of bits. Let \(T(z)\) be the number of transitions in the padded word \((0,z_1,\ldots,z_k,0)\); then \(T(z)\) is twice the number of runs of ones. Toggling one interval alters at most two boundary transitions, so at least \(T(z)/2\) steps are necessary to reach \(z=0\). Flipping each run separately realizes that bound. The maximum number of runs is \(\lceil k/2\rceil\), and choosing \(2r\) of the \(k+1\) possible transition boundaries gives exactly \(\binom{k+1}{2r}\) words with \(r\) runs. The probability of a new run beginning at position \(1\) in a uniform random binary word is \(1/2\), and at every later position it is \(1/4\). The average distance from any vertex is \((k+1)/4\), which, after multiplying by \(2^k\) and dividing by two for unordered pairs, yields \(W=(k+1)2^{2k-3}\).

For completeness, the invertible boundary-difference map
\[
 (z_1,\ldots,z_k)\longmapsto
 (z_1,z_1\mathbin\oplus z_2,\ldots,z_{k-1}\mathbin\oplus z_k,z_k)
\]
identifies binary words with even-parity vectors of length \(k+1\), and an interval toggle with toggling exactly two of those coordinates. Thus \(\Gamma\) is the halved cube. Independently, Fourier characters on \(\mathbb F_2^k\) indexed by \(s\in\mathbb F_2^k\) give interval-toggle character values \(p_{a-1}p_b\), where \(p_0=1\) and \(p_j=(-1)^{s_1+\cdots+s_j}\). If \(j\) of the signs \(p_1,\ldots,p_k\) are negative, summing over \(0\le a<b\le k\) gives adjacency eigenvalue \(((k+1-2j)^2-(k+1))/2\). Subtracting from degree \(k(k+1)/2\) produces Laplacian eigenvalue \(2j(k+1-j)\), with \(\binom kj\) characters.

**4. The three-symbol diameter collapse.** For uniform \(q\ge3\), and arbitrary paths \(x,y\), independently choose \(z_i\) distinct from both \(x_i\) and \(y_i\) for every \(i\). This is possible at each layer because there are at least three symbols. Both pairs \((x,z)\) and \((z,y)\) differ at **every** internal position, so both are adjacent by step 1. Hence all distances are at most two. For \(k\ge3\), two paths that differ only at positions \(1\) and \(3\) are nonadjacent, establishing exact diameter two. If \(k\le2\), every nonempty disagreement set is contiguous, hence the graph is complete. The degree formula specialized to \(q\) counts exactly the distance-one vertices, leaving all other distinct vertices at distance two. Counting ordered distances, then dividing by two, gives the stated distance polynomial and Wiener index. This also completes the threshold proof.

## Verification

Run \(\texttt{python checker.py}\) with Python, NumPy, SciPy and SymPy installed. The checker constructs the actual arc-incidence vectors, independently identifies every pair's support face by enumerating paths contained in the two-route union, checks graph distances by breadth-first search, and separately solves midpoint linear programs to check adjacency on smaller instances. It verifies the Fourier/tensor eigenvalue multiset against a direct dense Laplacian diagonalization and, for small profiles, verifies the matrix-tree product against an **exact** reduced-Laplacian determinant. Exact distance checks cover binary \(k\le8\), ternary \(k\le5\), and quaternary \(k\le4\); the LP checks use six small profiles, and spectral checks use eleven profiles including nonuniform ones. The output ends with \(\texttt{ALL CHECKS PASS}\). These computations are finite consistency tests and are not used to infer the all-dimensional theorem.

## Relationship to prior work

The general fact that two distinct shortest-path-polytope vertices are adjacent precisely when their united support contains one cycle is attributed by Blanchard, De Loera and Louveaux (2020, Section 3) to Rispoli (1992, Lemma 2). Our elementary exposed-face proof specializes that **previously known** principle; neither the principle nor the existence of a flow-path encoding is claimed to be new. Borgwardt, De Loera and Finhold (2016) prove a broad Hirsch bound on network-flow-polytope graph diameters; that bound does not give the exact distance laws for these particular networks. Classical halved-cube theory already supplies graph distance-regularity and spectral information for the binary case, once the present incidence-graph identification is made. The contribution asserted here is the combined **all-profile spectrum and spanning-tree factorization of the actual path-polytope skeleton**, together with the sharp uniform binary-to-ternary **diameter and distance-distribution transition**. No novelty is claimed for the general adjacency lemma, Kirchhoff's theorem, elementary complete-graph eigenvalues, or classical halved-cube invariants.

## Limitations

The vertices of the polytope are path incidence vectors; the results do not extend without proof to arbitrary flow capacities, graphs with interlayer omissions or skip-layer arcs, shortest-path *projections*, or nonuniform-layer graph distances beyond the spectral statement. The spectra are specified by a finite signature product, not as a closed list of pairwise distinct eigenvalues. The formulas do not determine monotone simplex pivot complexity. Literature searches did not identify a prior complete layer-profile skeleton-spectrum classification, but an equivalent description in terms of other graph families remains possible. Rispoli's 1992 primary full text could not be obtained; its verified adjacency attribution is available from the inspected 2020 paper. Independent mathematical evaluation remains outstanding.

## References

1. M. Blanchard, J. A. De Loera and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, first public preprint January 27, 2020, arXiv:2001.09575, SIAM J. Discrete Math. 35 (2021), 1746–1768, doi:10.1137/20M1315646. Relevant: Section 3, unique-cycle adjacency statement and shortest-path-polytope discussion. Author-postprint full text: https://orbi.uliege.be/bitstream/2268/259347/1/BlanchardDeLoeraLouveaux.pdf.
2. F. J. Rispoli, *The monotonic diameter of the perfect matching and shortest path polytopes*, Oper. Res. Lett. 12 (1992), 23–27, doi:10.1016/0167-6377(92)90018-X. General adjacency result cited through reference 1; full text not inspected.
3. S. Borgwardt, J. A. De Loera and E. Finhold, *The Diameters of Network-flow Polytopes satisfy the Hirsch Conjecture*, arXiv:1603.00325 (first posted March 1, 2016), Math. Program. 171 (2018), 283–309. General network-flow diameter bound.
4. A. E. Brouwer, A. M. Cohen and A. Neumaier, *Distance-Regular Graphs*, Springer, 1989, chapter on halved cubes. Classical graph identification only; cited as background, not directly inspected in full. See also the accessible SageMath graph-generator documentation for \(\texttt{HalfCube}\): https://sagemath.gitlab.io/documentation/html/en/reference/graphs/sage/graphs/graph_generators.html.
