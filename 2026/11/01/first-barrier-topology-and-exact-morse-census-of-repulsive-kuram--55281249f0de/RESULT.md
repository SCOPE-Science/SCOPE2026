# First-barrier topology and exact Morse census of repulsive Kuramoto dynamics on triangular cacti

## Finding

For every connected **triangular cactus** assembled from one vertex by successively adjoining \(r\geq1\) triangles, each new triangle sharing exactly one existing vertex and introducing two new vertices, the uniform repulsive, identical-frequency Kuramoto flow has a complete, nondegenerate equilibrium energy-and-index census. Write \(E_*=-3r/2\) for the minimum energy. With the common phase removed, the complete generating polynomial is

\[
\sum_{\theta\in\operatorname{Crit}(E)/S^1}
 z^{\,2E(\theta)+3r}t^{\,\operatorname{ind}(\theta)}
 =\bigl(2+3zt+z^9t^2\bigr)^r.
\]

Here \(\operatorname{ind}\) is the number of negative eigenvalues of the Hessian of \(E\) on the phase quotient. In particular, exactly \(6^r\) equilibrium classes exist, precisely \(2^r\) are asymptotically attracting minima, and there are exactly \(3r2^{r-1}\) saddles of index one at the lowest saddle energy \(E_*+1/2\). The remaining critical energies, including the all-aligned maximum at \(3r\), are determined by the polynomial.

The *sharp pairwise switching barrier* between any two distinct minimizing configurations is independent of the number and arrangement of triangles:

\[
 \inf_{\gamma(0)=\alpha,\;\gamma(1)=\beta}
 \max_{0\leq s\leq1} E(\gamma(s))
 = E_*+\frac12
 \qquad (\alpha\ne\beta\text{ minima}).
\]

For every \(E_*\leq h<E_*+1/2\), the energy sublevel \(\{E\leq h\}\) has exactly \(2^r\) connected components, each contractible. For every
\(E_*+1/2<h<E_*+1\), that sublevel is connected and has homotopy type

\[
 \bigvee^{\,3r2^{r-1}-2^r+1} S^1.
\]

Thus the first saddle-energy transition merges every ground-state component, but also creates a growing number of independent one-dimensional holes. For the special **friendship graph** in which all triangles meet at a common center, the basins of the \(2^r\) sinks have equal Haar measure \(2^{-r}\) each; at a sink the linearized flow has transverse spectral gap \(1/2\) when \(r\geq2\) (gap \(3/2\) for \(r=1\)).

## Assumptions and scope

The vertices carry phases \(\theta_v\in\mathbb R/(2\pi\mathbb Z)\), with no natural-frequency differences and unit-magnitude **negative** coupling along each edge. The equations and associated energy are

\[
 \dot\theta_v=-\sum_{w\sim v}\sin(\theta_w-\theta_v)
 =-\frac{\partial E}{\partial\theta_v},
 \qquad
 E(\theta)=\sum_{\{v,w\}\in E(G)}\cos(\theta_v-\theta_w).
\]

Here the repeated symbol \(E\) denotes the scalar energy, while \(E(G)\) denotes the graph's edge set. Energies are *not* divided by vertex count or number of edges. The simultaneous global phase shift is quotiented out. A triangular cactus contains \(2r+1\) vertices, \(3r\) edges, and no edges beyond those belonging to its \(r\) triangles. This is not a theorem about all cactus graphs, unequal couplings, larger polygonal blocks, discrete-time updates, or arbitrary input frequencies.

## Proof

**1. Global angular coordinates.** Choose a root vertex of phase zero and order the triangular blocks in an attachment order. For block \(i\), let \(p_i\) be its old attachment vertex, and let \(a_i,b_i\) be its two new vertices. Set
\(\phi_i=\theta_{a_i}-\theta_{p_i}\) and
\(\psi_i=\theta_{b_i}-\theta_{p_i}\).
Because each vertex other than the root first appears in exactly one such block, these \(2r\) angles give a global smooth torus coordinate system on the phase quotient. No two blocks share an edge, so

\[
 E=\sum_{i=1}^r e(\phi_i,\psi_i),\qquad
 e(\phi,\psi)=\cos\phi+\cos\psi+\cos(\phi-\psi).
\]

The original flow is a gradient flow of this energy in the positive-definite Riemannian metric transported from the Euclidean quotient metric; it is **not** generally a product flow in these coordinates. Critical points, energies, and Hessian inertias nonetheless separate because coordinate changes give congruent Hessians at critical points.

**2. One-triangle critical points and Hessians.** The stationary equations are
\(\sin\phi+\sin(\phi-\psi)=0\) and
\(\sin\psi-\sin(\phi-\psi)=0\).
Their sum gives \(\sin\phi+\sin\psi=0\). Hence either
\(\psi\equiv-\phi\) or \(\psi\equiv\pi+\phi\) modulo \(2\pi\). In the first branch, \(\sin\phi(2\cos\phi+1)=0\); in the second, \(\sin\phi=0\). Therefore the complete six-point list is

\[
\begin{array}{c|c|c|c}
(\phi,\psi)& e&\text{Morse index}&\text{multiplicity}\\\hline
(2\pi/3,-2\pi/3),\;(-2\pi/3,2\pi/3)&-3/2&0&2\\
(0,\pi),\;(\pi,0),\;(\pi,\pi)&-1&1&3\\
(0,0)&3&2&1
\end{array}
\]

The Hessian is

\[
D^2e=\begin{pmatrix}
-\cos\phi-\cos(\phi-\psi)&\cos(\phi-\psi)\\
\cos(\phi-\psi)&-\cos\psi-\cos(\phi-\psi)
\end{pmatrix}.
\]

At the two chiral minima its eigenvalues are \(1/2,3/2\). At each of the three intermediate points its determinant is \(-1\). At the fully aligned maximum its eigenvalues are \(-1,-3\). Thus all six are nondegenerate. For an independent energy lower bound, use \(u=(\phi+\psi)/2\), \(v=(\phi-\psi)/2\) to obtain

\[
e=2\cos u\cos v+2\cos^2v-1
\geq 2\bigl(|\cos v|-\tfrac12\bigr)^2-\tfrac32
\geq-\tfrac32.
\]

**3. Product critical census and dynamics.** In the independent block coordinates, the critical Hessian is block diagonal with \(r\) copies of the displayed two-dimensional Hessian, so Hessian inertia is additive. Choosing among two index-zero minima, three index-one saddles, and one index-two maximum on each block gives the claimed polynomial: relative to a ground state, the three possible block-energy increments are \(0,1/2,9/2\), corresponding respectively to exponents \(0,1,9\) after multiplication by two. It follows immediately that the minimum is \(E_*=-3r/2\), the number of sinks is \(2^r\), and the first excited critical level has \(3r2^{r-1}\) index-one saddles.

Along every actual trajectory, \(\dot E=-\sum_v|\partial E/\partial\theta_v|^2\leq0\). Because the quotient phase space is compact and the critical set consists of finitely many isolated points, the omega limit of any forward trajectory is a single critical point (the omega limit is connected and lies in the critical set). Thus every trajectory converges modulo common phase; all but a Haar-null union of stable manifolds of nonminima converge to one of the sinks.

**4. Sharp switching barrier.** Two distinct minima assign opposite orientations to at least one triangular block. Along any continuous connecting path, the continuous quantity \(\sin(\phi_i-\psi_i)\) must cross zero in that block. At a point where \(\phi_i-\psi_i\equiv0\), one has \(e_i=1+2\cos\phi_i\geq-1\); where the difference is \(\pi\), one has \(e_i=-1\). All other blocks contribute at least \(-3/2\); therefore \(E\geq E_*+1/2\) somewhere on the path.

Conversely, change the chiralities of differing blocks one at a time, holding every other block at one of its chiral minima. During the change in block \(i\), use the coordinate path \((\phi_i,\psi_i)=(s,-s)\), with \(s\) traversing from \(2\pi/3\) to \(4\pi/3\) (or in reverse). On this arc
\(e_i=2\cos s+\cos(2s)\leq-1\), with maximum exactly \(-1\). Coordinate independence ensures this is a continuous path of full vertex phases even when blocks are nested. Concatenate finitely many such paths to give the reverse inequality and the exact minimax barrier.

**5. First-sublevel topology.** The only critical values strictly below \(E_*+1\) are \(E_*\) (\(2^r\) critical points of index zero) and \(E_*+1/2\) (\(3r2^{r-1}\) critical points of index one). The next possible critical increment is at least \(1\) (two separate index-one block excitations); for \(r=1\) the next increment is \(9/2\). Standard finite-dimensional Morse handle attachment thus gives \(2^r\) zero-handles before the first saddle level and, just above it, precisely \(3r2^{r-1}\) one-handles and no higher-dimensional handles. The explicit switching paths in step 4 imply the resulting one-dimensional CW complex is connected. Its first Betti number is its edge count minus its vertex count plus one, namely
\(3r2^{r-1}-2^r+1\), and every connected graph is homotopy equivalent to the wedge of that many circles. Before the saddle level, each component is contractible. This proves the stated entire open-height intervals, without claiming a topology formula at any higher critical level.

**6. Friendship-graph consequences.** When all triangles share the same hub, independently swapping the two outer vertices in each triangle is a measure-preserving graph automorphism commuting with the flow. These swaps act transitively on the \(2^r\) sinks and permute their full basins. Since nonminimizing stable manifolds have zero Haar measure, each sink's basin occupies exactly \(2^{-r}\) of quotient phase space. At any sink, all graph-edge phase differences have cosine \(-1/2\), hence the original-coordinate energy Hessian is exactly \(L(G)/2\). The friendship-graph Laplacian has spectrum
\(0\) once, \(1\) with multiplicity \(r-1\), \(3\) with multiplicity \(r\), and \(2r+1\) once. Therefore the relaxation spectral gap after removing the common phase is \(1/2\) for \(r\geq2\) and \(3/2\) for \(r=1\).

## Verification

The standalone Python/NumPy checker `artifacts/verify_triangle_cactus.py` reconstructs the original graph and all \(6^r\) equilibrium phase assignments, **independently** calculates the original-coordinate energy, vertex gradients, and full Hessian eigenvalue inertias on windmill and chain-shaped cacti of sizes \(r=1,2,3,4\), and compares complete bivariate coefficient tables with the polynomial. It checks \(3{,}108\) labelled critical configurations and samples \(40{,}690\) points along explicit pairwise ground-state connecting paths. The recorded output `artifacts/verification_output.txt` ends with `TRIANGLE_CACTUS_REPULSIVE_VERIFY_OK`. These tests corroborate the formulas only for the tested instances; the proof above, including Morse theory, establishes the infinite-family conclusions.

To reproduce, use Python 3 with NumPy and run `python artifacts/verify_triangle_cactus.py` from the extracted package root. The code is self-contained aside from this declared dependency; no external datasets are required.

## Relationship to prior work

Mehta, Daleo, Dörfler and Hauenstein (first public preprint 2014-12-01, arXiv:1412.0666) analyze equilibrium equations and stability for the general Kuramoto model using algebraic geometry and numerical examples, but do not give an all-size triangular-cactus Morse polynomial or the stated sublevel transition. Bronski, DeVille and Ferguson (2015, arXiv:1508.01507), Theorem 2.6, already reduce Hessian/Laplacian stability indices to cycle-intersection matrices, a **general index tool**, and discuss rings and graphs with one or two loops; this result is not claimed as new here. Delabays, Coletta and Jacquod (2016, arXiv:1609.02359) analyze phase-locked multistability on planar graphs under a different (attractive) coupling regime, without this repulsive cactus energy-barrier formula. Zhao and Zhou (2024, arXiv:2407.11314) classify the six local critical points and their stability for weighted three-oscillator triangles: the single-triangle classification is accordingly **prior work**, not the novelty claim.

The claim assessed here is the joint, arrangement-independent all-size energy-and-Morse census, the *exact pairwise minimax barrier*, the first nontrivial **sublevel homotopy transition**, and the windmill basin-symmetry consequence. The proof gives reductions from local known facts explicitly; the claim does not assert the local triangle six-state fact or the abstract Morse handle theorem as novel.

## Limitations

Unit repulsive couplings and identical intrinsic frequencies are essential; arbitrary edge weights or nonzero frequency discrepancies do not generally retain the product structure. Morse indices are quotient indices, not counts of nonzero eigenvalues of an arbitrarily gauge-fixed Jacobian. The full original-coordinate ODE does not decouple into block-wise flows. The sublevel topology is determined only in the two indicated energy intervals, and no quantitative transient-time bound or universal basin volume outside the friendship graph is asserted. Although the primary sources checked do not state the combined all-size barrier/sublevel result, an unindexed earlier equivalent remains a possible originality risk.

## References

1. D. Mehta, N. Daleo, F. Dörfler and J. D. Hauenstein, *Algebraic Geometrization of the Kuramoto Model: Equilibria and Stability Analysis*, first public 2014-12-01, arXiv:1412.0666. https://arxiv.org/abs/1412.0666
2. J. C. Bronski, L. DeVille and T. Ferguson, *Graph Homology and Stability of Coupled Oscillator Networks*, first public 2015-08-06, arXiv:1508.01507. https://arxiv.org/abs/1508.01507
3. R. Delabays, T. Coletta and P. Jacquod, *Multistability of Phase-Locking in Equal-Frequency Kuramoto Models on Planar Graphs*, first public 2016-09-08, arXiv:1609.02359. https://arxiv.org/abs/1609.02359
4. X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, first public 2024-07-16, arXiv:2407.11314. https://arxiv.org/abs/2407.11314
