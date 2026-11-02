# Complete color-preserving symmetry characters and quotient Betti numbers for two-point configurations of multipartite graphs

## Finding
For \(k\ge3\) and integers \(a_1,\ldots,a_k\ge3\), put \(G=K_{a_1,\ldots,a_k}\), \(X=\operatorname{UConf}_2(|G|)\), and \(P=\prod_{i=1}^k S_{a_i}\). Here \(X\) consists of unordered pairs of distinct points of the geometric realization of \(G\). A permutation \(g\in P\) acts by permuting vertices within their color classes.

Let \(f_i(g)\) and \(t_i(g)\) be the numbers of one-cycles and two-cycles of \(g\) on color class \(i\). Put
\[
F=\sum_i f_i,\qquad E=\sum_{i<j}f_if_j,\qquad D=\binom E2-\sum_i f_i\binom{F-f_i}{2}.
\]
For every \(g\in P\), all rational homology characters are determined by
\[
\boxed{\chi_{H_0}(g)=1,\qquad\chi_{H_1}(g)=E-F+1,}
\]
\[
\boxed{\chi_{H_2}(g)=D-2\sum_{i<j}t_it_j-E(F-3)+\binom F2+\sum_i t_i-F.}
\]
All rational homology in degrees above two vanishes. These values are actual characters, not merely alternating characters. The integral first homology is \(\mathbb Z^\beta\oplus\mathbb Z/2\), where \(\beta=\sum_{i<j}a_ia_j-\sum_i a_i+1\); the second homology is free abelian.

An unexpected size-independent consequence is
\[
\boxed{(b_0,b_1,b_2)(X/P;\mathbb Q)=\left(1,\binom{k-1}{2},\;3\binom k4\right),}
\]
with all other quotient rational Betti numbers zero. Thus three color classes always yield quotient Betti vector \((1,1,0)\), although the original space has potentially large second homology.

## Assumptions and scope
All graphs are finite, simple, with edges between different color classes and no edges within one class. The vertices of each class are distinguishable before taking the indicated \(P\)-quotient. The lower bounds \(a_i\ge3\) ensure that \(G\) is nonplanar and three-connected, that distinct nonadjacent particles have spectator vertices, and that the required edge-pair stabilizers exist. The binomial symbol is interpreted as \(\binom s2=s(s-1)/2\) for any nonnegative integer \(s\). All character formulas are over \(\mathbb Q\); the integral homology statement does not assert an integral equivariant decomposition.

## Proof
**1. Exact two-dimensional model.** For the two-point configuration space of a simple graph, the unordered cubical discrete model \(UD_2(G)\) has cells represented by two graph cells with disjoint closures: two distinct vertices (dimension zero), one closed edge and a vertex not incident to it (dimension one), or two edges without a common endpoint (dimension two). The standard sufficient subdivision hypotheses hold here: each essential-to-essential path contains at least one edge, and each graph cycle has length at least three. The model is a deformation retract of \(X\). The model and its cellular boundary operators are natural under vertex permutations preserving color classes.

Write \(N=\sum_i a_i\), \(M=\sum_{i<j}a_i a_j\), and \(\beta=M-N+1\). The cubical chain ranks are
\[
c_0=\binom N2,\quad c_1=M(N-2),\quad c_2=\binom M2-\sum_i a_i\binom{N-a_i}{2}.
\]
The final term deletes pairs of graph edges incident to a vertex. The space is connected, hence \(H_0(X;\mathbb Q)=\mathbb Q\). There are no cells above dimension two, so \(H_j=0\) for \(j\ge3\), and integral \(H_2=\ker\partial_2\) is free.

**2. The first homology as the graph-cycle representation.** Ko and Park's three-connected graph-braid first-homology theorem (Theorem 3.16 of [2]) gives \(H_1(X;\mathbb Z)\cong\mathbb Z^\beta\oplus\mathbb Z/2\). Indeed \(G\) is three-connected and nonplanar for the stated parameters. There is also a canonical \(P\)-equivariant cellular map of chain complexes from the cubical model to graph chains: send \(\{u,v\}\) to \(u+v\), a moving edge with spectator vertex to its oriented edge, and a two-cube to zero. This induces a surjection \(H_1(X;\mathbb Q)\twoheadrightarrow H_1(G;\mathbb Q)\): a graph-cycle basis may be assembled from chordless triangles and quadrilaterals, and each such small cycle admits a stationary spectator vertex outside it (there are at least nine vertices). The dimensions of both sides are \(\beta\), hence the map is an isomorphism of rational \(P\)-modules. Orient each edge from its lower-indexed color class to its higher-indexed class. A color-preserving permutation never reverses an individual oriented edge. Thus the traces on graph vertex and edge chain modules are \(F\) and \(E\); the graph chain Euler identity gives \(\chi_{H_1}(g)=E-F+1\).

**3. Signed fixed-cube calculation.** The trace on zero-cubes counts invariant two-element vertex sets. Such a pair consists either of two fixed vertices or one two-cycle, giving
\[\operatorname{tr}(g|C_0)=\binom F2+\sum_i t_i.\]
A one-cube is invariant precisely if its moving edge and its spectator vertex are both fixed; orientation is preserved because colors are fixed. Therefore
\[\operatorname{tr}(g|C_1)=E(F-2).\]
For a two-cube, two fixed disjoint edges contribute positively. The number of these pairs is \(D\), since \(E\) is the number of fixed edges, and \(\sum_i f_i\binom{F-f_i}{2}\) counts the edge pairs meeting at a fixed vertex. The only remaining fixed two-cubes arise when the two edges are exchanged. For each two-cycle from color \(i\) and two-cycle from color \(j\ne i\), there are exactly two matchings by disjoint edges exchanged by \(g\); exchanging cubical factors reverses the two-dimensional orientation. Consequently
\[\operatorname{tr}(g|C_2)=D-2\sum_{i<j}t_it_j.\]
The alternating trace equality for finite cellular complexes now yields
\[\operatorname{tr}(g|H_2)=\operatorname{tr}(g|C_2)-\operatorname{tr}(g|C_1)+\operatorname{tr}(g|C_0)-1+\operatorname{tr}(g|H_1),\]
which is the asserted formula, for every color-preserving permutation, including arbitrary longer cycles.

**4. Rational homology of every full color-permutation quotient.** Over \(\mathbb Q\), averaging over finite \(P\) gives \(H_*(X/P;\mathbb Q)\cong H_*(X;\mathbb Q)^P\). This can be seen after barycentric subdivision, which eliminates cell inversions. Set \(q=\binom k2\), the number of possible unordered pairs of different colors. The invariant chain ranks in degrees zero and one are respectively \(k+q\) and \(kq\): a vertex-pair orbit has either one color or two different colors, and a moving-edge orbit remembers its pair of colors and the spectator color. In degree two, invariant oriented chains have dimension \(\binom q2\): two different moving-edge color-types give one orbit each, while a pair of edges of the same color-type has an element of its stabilizer exchanging those edges and negating the orientation, hence contributes no invariants.

The invariant graph-cycle rank is the cycle rank of the quotient color graph \(K_k\), namely \(b_1(X/P)=q-k+1=\binom{k-1}{2}\). With \(b_0=1\), the Euler relation for the invariant chain complex gives
\[
 b_2(X/P)=\binom q2-kq+(k+q)-1+(q-k+1)=3\binom k4.
\]
This proves the quotient formula and concludes the proof.

## Verification
The companion `multipartite_config_checker.py` reconstructs all cubical cells and both integral boundary operators from their definitions. It checks each identity \(\partial_1\partial_2=0\), boundary ranks modulo three, signed cellular traces for the identity, selected individual two- and three-cycles, and pairs of simultaneous transpositions. It reproduces for \((a_i)=(3,3,3)\) the rational Betti numbers \((1,19,81)\) and quotient Betti numbers \((1,1,0)\); for \((3,3,4)\), \((1,24,146)\) and \((1,1,0)\); and for \((3,3,3,3)\), \((1,43,567)\) and \((1,3,3)\). The infinite-family conclusion relies on the proof above, not those finite-field calculations.

## Relationship to prior work
Ko and Park [2] prove the nonequivariant first-homology formula for broad classes of graph braid groups and the two-dimensional cubical-model approach. Farber and Hanbury [3] study ordered two-particle configurations and mature-graph Betti numbers. An and Knudsen [1] describe second homology of planar graph braids and an obstruction to extending their generator statement to nonplanar graphs. The present calculation instead gives the complete degree-by-degree color-permutation character for ordinary **unordered** configurations of nonplanar complete multipartite graphs, together with all full-color-symmetry quotient Betti numbers. Earlier results on ordered two-particle sink configurations of complete bipartite graphs use different collision conditions and cover only two color classes. Indexed computations of individual polyhedral graph-configuration modules likewise do not imply this all-parameter formula.

## Limitations
The theorem does not describe integral torsion in homology of finite-group quotients, does not classify the fundamental group or homotopy type of the quotient, and does not include permutations of different color classes or color classes smaller than three. An inaccessible or unindexed equivalent equivariant calculation remains possible. Independent validation has not been performed.

## References
[1] B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first posted 2020-08-24), https://arxiv.org/abs/2008.10371.

[2] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (2011), https://arxiv.org/abs/1101.2648. Theorem 3.16.

[3] M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010), https://arxiv.org/abs/1005.2300.
