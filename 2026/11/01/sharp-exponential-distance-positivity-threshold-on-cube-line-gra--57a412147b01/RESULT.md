# Sharp exponential-distance positivity threshold on cube line graphs

## Finding

For every integer \(d\ge2\), let \(Q_d\) be the graph on the Boolean cube \(\{0,1\}^d\), with two vertices adjacent when exactly one coordinate changes. Let \(G_d=L(Q_d)\) be its line graph, on \(N=d2^{d-1}\) vertices, and let \(\rho\) denote the ordinary, unweighted shortest-path distance in \(G_d\). For \(0<z<1\), set \(K_d(z)=(z^{\rho(e,f)})_{e,f\in E(Q_d)}\).

The complete eigenvalue multiset of \(K_d(z)\) is explicit. For every integer \(0\le s\le d-1\), define
\[
 a_s=1-z+z(1+z)^{d-1-s}(1-z)^s,\qquad
 b_s=\begin{cases}
 2z(1+z)^{d-2-s}(1-z)^s,&s\le d-2,\\
 0,&s=d-1.
 \end{cases}
\]
There are eigenvalues
\[
 P_s=a_s+(d-s-1)b_s\quad\text{with multiplicity }\binom ds,
\]
and, whenever \(s\le d-2\),
\[
 M_s=a_s-b_s=(1-z)\bigl[1-z(1+z)^{d-2-s}(1-z)^s\bigr]
 \quad\text{with multiplicity }(d-s-1)\binom ds.
\]
Multiplicities add when distinct displayed expressions coincide. Their total is \(N\).

For \(d=2\), the matrix \(K_d(z)\) is positive definite for all \(0<z<1\). For every \(d\ge3\), there is a unique \(z_d\in(0,1)\) satisfying
\[
 z_d(1+z_d)^{d-2}=1.
\]
The sharp positive-semidefiniteness criterion is
\[
 \boxed{K_d(z)\succeq0\quad\Longleftrightarrow\quad0<z\le z_d.}
\]
It is positive definite for \(z<z_d\); at \(z=z_d\), its nullity is exactly \(d-1\), and its other \(N-d+1\) eigenvalues are strictly positive. At \(z>z_d\), it has a negative eigenvalue of multiplicity at least \(d-1\). The nullspace at equality consists exactly of the functions that are constant on cube edges of each fixed coordinate direction, with the \(d\) directional constants summing to zero.

Equivalently, \(\exp(-t\rho)\) is positive semidefinite if and only if \(t\ge t_d=-\log z_d\) for \(d\ge3\), whereas it is positive definite for every \(t>0\) when \(d=2\). For the cuboctahedral graph \(G_3\), \(t_3=\log((1+\sqrt5)/2)\). The thresholds increase strictly with \(d\), and
\[
 z_d\sim\frac{W(d)}d,\qquad t_d=\log d-\log W(d)+o(1),
\]
where \(W\) is the positive Lambert function satisfying \(W(u)e^{W(u)}=u\).

As a spectral corollary, the ordinary distance matrix \(D_d=(\rho(e,f))\) has eigenvalue multiset
\[
 \bigl[2^{d-2}(d^2+1)-1\bigr]^{[1]},\qquad
 \bigl[2^{d-2}-1\bigr]^{[d-1]},\qquad
 \bigl[-(d-1)2^{d-2}-1\bigr]^{[d]},\qquad
 (-1)^{[N-2d]},
\]
where the exponents in square brackets denote multiplicities, including a zero multiplicity when \(d=2\). In particular, for every \(d\ge3\), this graph metric is **not** conditionally negative semidefinite: its distance matrix has a strictly positive nonconstant eigenvalue even though its exponential kernel becomes positive definite at sufficiently large scale.

## Assumptions and scope

The dimension \(d\) is an arbitrary integer at least two. Edges of \(Q_d\) are unweighted and undirected, and distances on \(G_d\) count edges in a shortest path. The kernel parameter is real \(0<z<1\), equivalently \(t>0\); no assertion about arbitrary complex parameters or all graph line graphs is made. The standard Euclidean inner product is used on real-valued functions on the \(N\) graph vertices. No approximation is needed for the eigenvalue formulas or the root characterization.

## Proof

**1. Exact distance.** Identify an edge with a pair \((i,x)\), where \(i\in\{1,\dots,d\}\), \(x\in\{0,1\}^d\), and \(x_i=0\). Its endpoints are \(x\) and \(x+e_i\) (with coordinate addition modulo two). For two distinct edges, their line-graph distance is one plus the minimum hypercube distance between an endpoint of the first edge and an endpoint of the second. Indeed, a shortest vertex path connecting selected endpoints extends to an edge chain, and conversely every line-graph chain projects to such an endpoint walk; the possible first and last vertex-edge coincidences are handled by the additive one. Thus, writing \(h_A(x,y)=\#\{k\in A:x_k\ne y_k\}\),
\[
 \rho((i,x),(j,y))=
 \begin{cases}
 0,&(i,x)=(j,y),\\
 1+h_{[d]\setminus\{i\}}(x,y),&i=j,\ (i,x)\ne(j,y),\\
 1+h_{[d]\setminus\{i,j\}}(x,y),&i\ne j.
 \end{cases}
\]
All pairs have been covered, including incident edges, for which the last formula gives one.

**2. Fourier fiber decomposition.** For each subset \(S\subseteq[d]\) and each direction \(i\notin S\), define the function \(\phi_{S,i}\) to be zero away from edges of direction \(i\), and on \((i,x)\) let it be \((-1)^{\sum_{k\in S}x_k}\). These functions constitute an orthogonal basis: on each direction fiber they are exactly the Walsh characters of its \(d-1\) free coordinates, and their number is \(\sum_{S\subseteq[d]}(d-|S|)=d2^{d-1}=N\).

Fix \(S\) with \(|S|=s\). On a single direction fiber, the kernel is
\[
 (1-z)I+z\begin{pmatrix}1&z\\z&1\end{pmatrix}^{\!\otimes(d-1)},
\]
so its eigenvalue on \(\phi_{S,i}\) is \(a_s\). For two distinct direction fibers, the distance expression in step 1 yields a factor of \(2z\) from their two free endpoint-coordinate choices, and a product of \(d-2\) two-point Fourier transforms. The off-diagonal Walsh coefficient is therefore \(b_s\) whenever both directions lie outside \(S\); it vanishes if \(S\) contains either direction. Consequently the span of \(\{\phi_{S,i}:i\notin S\}\) is invariant, and its matrix has all diagonal entries \(a_s\) and all off-diagonal entries \(b_s\).

The all-ones direction vector has eigenvalue \(P_s\). Its orthogonal complement, of dimension \(d-s-1\), has eigenvalue \(M_s\). There are \(\binom ds\) independent subsets of size \(s\), giving the claimed multiplicities. The special case \(s=d-1\) has a one-dimensional direction fiber and requires no off-diagonal coefficient.

**3. Positivity and the sharp endpoint.** Since \(0<z<1\), every \(a_s>0\) and \(b_s\ge0\); hence all \(P_s>0\). For \(s\le d-2\), direct factorization gives the stated expression for \(M_s\). Its bracket is largest at higher \(s\), because
\[
 (1+z)^{d-2-s}(1-z)^s
 =(1+z)^{d-2}\left(\frac{1-z}{1+z}\right)^{\!s}.
\]
Thus \(M_0\) is the least of these eigenvalues, and the inequality is strict for every \(s>0\) when \(d\ge3\). For \(d=2\), \(M_0=(1-z)^2>0\). For \(d\ge3\), \(M_0=(1-z)[1-z(1+z)^{d-2}]\). The function \(z\mapsto z(1+z)^{d-2}\) is strictly increasing on \((0,1)\), starts at zero, and ends above one. It has one root at level one; the preceding comparison proves the exact semidefinite, definite, and nullity claims. Since \(S=\varnothing\) supplies the direction-constant eigenvectors, the equality nullspace is as stated.

The function defining this root increases with dimension, so \(z_d\) decreases strictly and \(t_d\) increases strictly. Taking logarithms of the root equation shows first that \(z_d\to0\) and \(dz_d=O(\log d)\); expansion of \(\log(1+z_d)\) then yields \(\log z_d+dz_d=o(1)\). Hence \((dz_d)e^{dz_d}=d(1+o(1))\), yielding \(dz_d\sim W(d)\) and the stated logarithmic asymptotic.

**4. Ordinary distance spectrum.** At \(z=1\), \(K_d(1)\) is the all-ones matrix, and entrywise differentiation gives \(K_d'(1)=D_d\). On a nonconstant invariant Walsh block, the limit of the corresponding eigenvalue of \(K_d(z)\) divided by \(z-1\) equals its distance-matrix eigenvalue. The \(S=\varnothing\) direction-contrast block yields \(2^{d-2}-1\), the \(|S|=1\) direction-constant block yields \(-(d-1)2^{d-2}-1\), and all remaining nonconstant modes yield \(-1\). The constant vector has row sum \(2^{d-2}(d^2+1)-1\), obtained by differentiating \(P_0(z)\) at one. The multiplicities above give exactly the displayed list. The zero-sum positive distance mode for \(d\ge3\) rules out conditional negative semidefiniteness.

## Verification

The accompanying standalone `verify.py` independently constructs each line graph from explicit cube-edge endpoints, computes all shortest-path distances by breadth-first search rather than using the displayed formulas, and checks every pairwise distance against the formula for \(2\le d\le5\). It then tests the complete Fourier action on every Walsh basis vector for \(z\in\{1/2,2/3,9/10\}\), using exact rational arithmetic. It additionally matches two integer moments of the claimed distance spectrum and checks rational bracketing of the threshold for dimensions \(3\le d\le14\). The completed checker reports `EXACT_LINEGRAPH_KERNEL_SPECTRUM_OK 30368`. This is a finite consistency check; the proof in steps 1–4 establishes all orders and the complete continuum of \(z\).

## Relationship to prior work

Liu, Cao, Pan and Elaiw (2013) study \(L(Q_d)\) itself but derive its **Laplacian** spectrum and electrical-resistance/Kirchhoff invariants, not an exponential kernel of ordinary shortest-path distance. Aalipour and collaborators (2015) determine ordinary distance spectra of halved cubes, double odd graphs and other graph families; their line-graph examples concern complete or complete bipartite graphs, not cube line graphs. Hou and Bian (2021) determine the **adjacency** spectrum of cube line graphs and related spanning-tree data, again different from the present family of all-distance kernel matrices. DeVille (2017) provides a more general distance-spectrum framework, but no inspected theorem specializes to the displayed sharp positive-definite threshold on \(L(Q_d)\). These results supply methods and context without a statement that implies the cutoff or its singular directional eigenspace.

## Limitations

The originality review has been bounded by the specific original texts and related published records inspected; independently rediscovering an equivalent statement in older, differently indexed work remains possible. The theorem concerns unweighted cube line graphs, not all median or partial-cube line graphs. For \(z>z_d\) it establishes at least \(d-1\) negative eigenvalues, not an exact negative inertia at every such parameter. The finite checker does not constitute an infinite proof. Independent mathematical validation has not been performed.

## References

1. J. Liu, J. Cao, X.-F. Pan and A. Elaiw, *The Kirchhoff Index of Hypercubes and Related Complex Networks*, Discrete Dynamics in Nature and Society (first published 12 December 2013), DOI: 10.1155/2013/543189; https://doi.org/10.1155/2013/543189.
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first posted 3 September 2015); https://arxiv.org/abs/1509.01196.
3. L. DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294 (2017); https://arxiv.org/abs/1708.02294.
4. S. Hou and H. Bian, *Research on the Properties of Spectrum on the Line Graph of Hypercube*, Advances in Applied Mathematics 10 (2021), 4415–4421, DOI: 10.12677/AAM.2021.1012470; https://doi.org/10.12677/AAM.2021.1012470.
