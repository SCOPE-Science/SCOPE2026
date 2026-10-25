# The Paley-seventeen flag complex is a wedge of sixteen spheres with the vertex-augmentation homology character

## Finding
For the Paley graph \(P_{17}\), the flag (clique) complex \(K=\operatorname{Cl}(P_{17})\) has homotopy type
\[
K\simeq\bigvee^{16}S^2.
\]
Its natural affine symmetry group \(G=\mathbb F_{17}\rtimes(\mathbb F_{17}^{\times})^2\), of order \(136\), acts on rational second homology by the vertex-augmentation representation:
\[
H_2(K;\mathbb Q)\cong\left\{(c_x)_{x\in\mathbb F_{17}}:\sum_xc_x=0\right\},
\qquad\operatorname{tr}(g\mid H_2)=\#\operatorname{Fix}_{\mathbb F_{17}}(g)-1.
\]
The character takes values \(16,-1,0\) on the identity, the other \(16\) translations, and the \(119\) elements with nontrivial multiplier, respectively. Integral homology is free and concentrated (in positive degrees) in degree two, of rank \(16\).

## Assumptions and scope
The graph has vertex set \(\mathbb F_{17}=\{0,1,\ldots,16\}\), with an undirected edge between distinct \(u,v\) precisely if \(v-u\) is in the square set \(R=\{1,2,4,8,9,13,15,16\}\pmod{17}\). The simplices of \(K\) are all cliques, including isolated vertices and triangles; only the ordinary (unordered, undirected) clique construction is used. The affine group consists of maps \(x\mapsto ax+b\) for \(a\in R\), \(b\in\mathbb F_{17}\). The rational representation is meant up to \(\mathbb Q[G]\)-isomorphism. No assertion of a canonical integral equivariant lattice isomorphism is made.

## Proof
**Face counts and dimension.** Directly from the adjacency test, the numbers of vertices, edges, and triangles are \((17,68,68)\), and there is no four-clique. The latter can also be deduced from the classical Ramsey property of this graph. Thus \(K\) is connected and has dimension two, and its Euler characteristic is \(17-68+68=17\).

**A finite integral certificate for simple connectivity.** Contract a spanning tree in the one-skeleton. The following list of \(16\) edges is a spanning tree (unordered pairs):

```
(0,1) (0,2) (0,4) (0,8) (0,9) (0,13) (0,15) (0,16)
(1,3) (1,5) (1,10) (1,14) (2,6) (2,11) (4,12) (7,8)
```

Enumerate triangles as the increasing triples among all \(\binom{17}{3}\) triples, retaining only graph triangles, in lexicographic order; number them from \(0\) through \(67\). Read these \(52\) triangle indices in the stated order:

```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29 33 34 35 36 37 38 39
41 44 45 40 30 31 32 42 46 47 49 52 56 59 61
```

For each indexed triangle, **exactly one** of its three edges is not in the tree or among the edges eliminated by earlier triangles. The triangle relator therefore sets that edge's fundamental-group generator equal to the identity, inductively. At the end all \(52\) non-tree edges have been eliminated, proving \(\pi_1(K)=1\). The same ordered rows and columns of the integral simplicial \(\partial_2\) matrix, restricted to the successive newly eliminated edges, give a triangular \(52\)-square minor with diagonal entries \(\pm1\). Thus the triangle boundaries generate the entire integral one-cycle lattice; no rational approximation or modular rank extrapolation is needed.

**Homotopy type.** The connected one-skeleton has \(68-17+1=52\) independent one-cycles. The preceding certificate gives \(H_1(K;\mathbb Z)=0\) and \(\operatorname{rank}\partial_2=52\). As there are \(68\) triangles and no cells above dimension two, \(H_2(K;\mathbb Z)=\ker\partial_2\cong\mathbb Z^{16}\). A basis of \(H_2\) is realized by maps from \(16\) two-spheres, since the simply connected \(K\) satisfies the Hurewicz theorem. Their wedge induces an isomorphism on all integral homology groups; the homological Whitehead theorem for simply connected CW complexes makes this map a homotopy equivalence.

**Complete character.** The signed Lefschetz number of any simplicial automorphism is
\[
L(g)=\sum_{i=0}^{2}(-1)^i\operatorname{tr}(g\mid C_i(K;\mathbb Q))
=1+\operatorname{tr}(g\mid H_2(K;\mathbb Q)).
\]
An identity map has \(L=17\). A nonidentity translation has orbits of size \(17\) on vertices and cannot preserve any simplex of cardinality at most \(3\); therefore \(L=0\). An affine map with nontrivial multiplier is conjugate by a translation to multiplication by \(a\in R\setminus\{1\}\), with a unique fixed vertex. If the order of \(a\) is \(4\) or \(8\), no positive-dimensional simplex is setwise fixed, so \(L=1\). If \(a=-1\), four edges \(\{v,-v\}\) are fixed setwise, each with orientation sign \(-1\), and the four triangles \(\{0,v,-v\}\) are likewise setwise fixed, each with orientation sign \(-1\); the only fixed vertex is \(0\). Therefore \(L=1-(-4)+(-4)=1\) also in this case. It follows that \(\operatorname{tr}(g\mid H_2)\) equals \(16,-1,0\) in the three classes just described.

The vertex-permutation module \(\mathbb Q^{\mathbb F_{17}}\) has character equal to the number of fixed points. Removing its trivial line gives the same character \(\#\operatorname{Fix}-1\). Characters determine rational representations of finite groups (semisimplicity and ordinary character uniqueness), proving the claimed \(\mathbb Q[G]\)-module isomorphism.

## Verification
Run `python3 verify.py`. This dependency-free verifier reconstructs the \(17\) vertices, \(68\) edges, \(68\) triangles, absence of tetrahedra, a spanning tree, all \(52\) successive single-new-edge triangular relators, and signed Lefschetz traces for all \(136\) affine automorphisms. It asserts the exact three-valued character and exits with `VERIFY_OK_PALEY17_FLAG_HOMOTOPY_CHARACTER`. Its output is embedded separately in `verification_output.txt`. The argument above, including the integral \(\pm1\)-minor, is logically sufficient independently of its transcript.

## Relationship to prior work
The classical Paley graph and its affine automorphisms, as well as its orientably regular *surface embeddings*, are studied by Jones [1] and Lim–Praeger [2]. The surface underlying a Paley **map** is not the clique complex \(\operatorname{Cl}(P_{17})\); the topological realizations and assertions are different. Cioabă and Mim [3] study first clique homology of strongly regular graphs and give sufficient vanishing results for sufficiently large conference graphs; their Latin-square graph results on second homology do not apply to this graph. Neither these statements nor the inspected results on the Lovász open-neighborhood complex of \(P_{17}\) imply the stated flag-complex wedge decomposition or its affine second-homology character. These are distinguished by both the construction and the resulting groups.

## Limitations
The theorem applies to this specific \(17\)-vertex Paley graph and to rational, not asserted integral, symmetry modules. It does not claim the same homotopy type for other Paley graphs. The computational certificate is exhaustive for the stated finite object, not an infinite-family classification. The literature comparison cannot exclude every unindexed equivalent formulation; independent validation has not been performed.

## References
[1] Gareth A. Jones, *Characterisations and Galois conjugacy of generalised Paley maps*, arXiv:1006.0514 (first posted 2010-06-02), https://arxiv.org/abs/1006.0514 ; full text https://arxiv.org/html/1006.0514v1 .

[2] Tian Khoon Lim and Cheryl E. Praeger, *On generalised Paley graphs and their automorphism groups*, arXiv:math/0605252 (2006), https://arxiv.org/abs/math/0605252 .

[3] Sebastian M. Cioabă and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (first posted 2026-06-25), https://arxiv.org/abs/2606.27328 .
