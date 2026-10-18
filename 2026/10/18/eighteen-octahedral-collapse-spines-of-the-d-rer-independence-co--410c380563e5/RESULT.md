# Eighteen octahedral collapse spines of the Dürer independence complex

## Finding

Let \(D=GP(6,2)\) be the twelve-vertex Dürer graph, and let \(K=\operatorname{Ind}(D)\) be its ordinary independence simplicial complex. Exactly **18** induced six-vertex subgraphs of \(D\) consist of three disjoint edges. For each of these vertex sets \(W\), the induced subcomplex \(K[W]\) is the boundary of the three-dimensional crosspolytope (an octahedral two-sphere), and there is a sequence of exactly **72 elementary simplicial collapses**
\[
K\searrow K[W]\cong\partial\mathcal O_3\cong S^2.
\]
The eighteen cores form exactly two orbits, of sizes \(6\) and \(12\), under the entire automorphism group \(\operatorname{Aut}(D)\cong D_6\) of order twelve. This classifies all induced flag two-spheres with the minimum possible six vertices and shows that *every* one is a collapse spine.

Writing the rotation \(r\) and reflection \(s\) as in the next section, the induced integral homology representation is
\[
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z,
\qquad (r^a s^b)_*=(-1)^{a+b}
\quad(0\le a<6,\ b\in\{0,1\}).
\]
All other reduced integral homology groups vanish. Although \(K\simeq S^2\), it is a **pure three-dimensional** flag complex, with 36 tetrahedral facets. Consequently \(K\) is not Cohen–Macaulay over any field and is not pure shellable.

## Assumptions and scope

Indices lie in \(\mathbb Z/6\mathbb Z\). The graph has vertices \(u_i,v_i\) and exactly the edges
\[
\{u_i,u_{i+1}\},\quad \{u_i,v_i\},\quad \{v_i,v_{i+2}\}
\qquad (i\in\mathbb Z/6\mathbb Z).
\]
A face of \(K\) is any set of pairwise nonadjacent vertices of \(D\). In the certificate, vertices \(u_0,\ldots,u_5\) carry labels \(0,\ldots,5\), while \(v_0,\ldots,v_5\) carry labels \(6,\ldots,11\). A nonempty simplex is encoded by the unsigned bit mask \(\sum_{j\in\sigma}2^j\).

The dihedral generators are \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\), \(s(u_i)=u_{-i}\), and \(s(v_i)=v_{-i}\), with all indices modulo six. The symbol \(K[W]\) denotes the *included induced subcomplex* on \(W\), not merely an abstractly isomorphic replacement. Every collapse in the theorem is ordinary, nonequivariant, and preserves every face of its chosen target \(K[W]\).

## Proof

**1. The graph, independent faces, and minimal octahedral cores.** Exhaustively test the \(2^{12}-1=4095\) nonempty vertex subsets against the eighteen specified graph edges. The resulting face vector, by dimensions zero through three, is
\[
(f_0,f_1,f_2,f_3)=(12,48,74,36).
\]
There are precisely 36 maximal faces, all of cardinality four, so the complex is pure of dimension three. Among all \(\binom{12}{6}=924\) six-element subsets, exactly eighteen induce three disjoint graph edges. Such an induced graph has independence complex the join of three two-point sets, namely \(S^0*S^0*S^0\cong\partial\mathcal O_3\); its face vector is \((6,12,8)\), comprising 26 nonempty faces.

An induced subcomplex of an independence complex is flag. A flag triangulated two-sphere needs at least six vertices: every vertex has degree at least four (a three-cycle link would force a tetrahedral face), whereas the average degree in a triangulated two-sphere on \(n\) vertices is \(6-12/n\). At six vertices every degree equals four, so the complementary one-skeleton consists of three disjoint edges. Thus the eighteen sets above exhaust the minimum-vertex induced flag two-spheres.

**2. Exact relative simplicial collapses.** The accompanying `octahedral_spines.json` records an ordered list of 72 pairs of face masks for each of the eighteen cores. For each step \((\tau,\sigma)\), the independent verifier reconstructs the *current* complex and checks that \(\tau\subset\sigma\), \(|\sigma\setminus\tau|=1\), and \(\sigma\) is the sole remaining strict coface of \(\tau\). It also checks that neither removed face belongs to \(K[W]\). After the last pair the current face set is **equal**, not merely homotopy equivalent, to the original induced \(K[W]\). Each pair is therefore an elementary free-face collapse. Since \(170-26=144\), precisely \(144/2=72\) such pairs are necessary and sufficient in each record. The eighteen certificates collectively check 1,296 collapse pairs. An elementary collapse is a strong deformation retraction in geometric realization, which establishes the integral homotopy and homology conclusions.

**3. Dihedral orbits and the full automorphism group.** The vertices \(v_i\) are exactly those lying in graph triangles (the two inner triangles); the six \(u_i\) lie in none. Hence every graph automorphism preserves the \(u\)-vertices, which induce a hexagonal cycle; its action is determined by an automorphism of that cycle because each \(u_i\) has its unique \(v_i\) spoke neighbor. Thus there are at most twelve automorphisms. The listed rotations and reflections realize all twelve, proving \(\operatorname{Aut}(D)=\langle r,s\rangle\cong D_6\). Acting on the eighteen core vertex sets yields two orbits of cardinalities six and twelve. In particular, no individual core is invariant under the full group; the collapse sequences are not asserted equivariant.

**4. Integral orientation character.** Since the certified collapses give reduced integral homology concentrated in degree two, the reduced simplicial Lefschetz number of an automorphism equals its trace on \(\widetilde H_2(K;\mathbb Z)\). For each of the twelve permutations \(g=r^as^b\), enumerate every nonempty simplex fixed *setwise*. Its contribution to the alternating simplicial trace is \((-1)^{\dim\sigma}\) times the sign of the induced permutation of the ordered vertices of \(\sigma\); subtract one for the augmentation (empty-face) term. Exact enumeration gives
\[
\widetilde L(r^a s^b)=(-1)^{a+b}.
\]
The homology group is rank-one free abelian, so these traces determine its integral \(D_6\)-action, without assuming any of the collapses are equivariant.

**5. Non-Cohen–Macaulay consequence.** The pure complex has dimension three, but nonzero reduced second homology with coefficients in *every* field. The empty-face homological vanishing condition for Cohen–Macaulayness therefore fails. Pure shellability would imply Cohen–Macaulayness, so it fails as well.

## Verification

Run `python3 verify.py octahedral_spines.json` with Python 3 and no nonstandard packages. The program constructs the graph and all 170 nonempty faces from scratch; enumerates all 924 six-subsets, identifies the eighteen matching triples; verifies every face and every free-face pair in the supplied certificates; proves the full twelve-element graph symmetry group by the triangle and spoke structure; identifies its two orbits; and independently recomputes all twelve signed reduced Lefschetz traces. Its successful deterministic output is:

```
VERIFY_OK: F_VECTOR_12_48_74_36, CORES_18, COLLAPSES_1296, ORBITS_6_12, DIHEDRAL_CHARACTER
```

The code deliberately treats the certificate solely as a list of claims to be checked. No finite-field rank calculation, probabilistic approximation, or unverified extrapolation is used. The only noncomputational ingredients are the standard identifications of an independence complex of three disjoint edges with an octahedral boundary, the elementary-collapse theorem, the Lefschetz trace formula, and the Cohen–Macaulay vanishing criterion.

## Relationship to prior work

Campbell, Ellingham and Royle's classification of well-covered cubic graphs identifies this graph as a distinguished well-covered example; it does not determine the homotopy or the eighteen induced sphere retractions. Ehrenborg–Hetyei develop sphere and collapse methods, particularly for independence complexes of forests, which do not include this multiply cyclic graph. Marietti–Testa prove crosspolytope collapses for forests and more general methods for reducing simplicial complexes; their forest or unicyclic theorems do not imply the present eighteen relative collapses for \(GP(6,2)\), whose cycle rank is seven. Kozlov treats related simple-homotopy deformations of neighborhood/Hom complexes, which are different functors from the independence complex here. A separate graph-metric Vietoris–Rips study of the Dürer graph also concerns a different simplicial filtration.

The contribution is not simply the Betti number of a small graph: it classifies the *entire set of smallest flag sphere spines*, proves preservation of each included sphere under explicit ordinary collapses, identifies the two natural symmetry orbits and the integral orientation character, and exposes a concrete pure well-covered example with a non-Cohen–Macaulay independence complex.

## Limitations

The theorem treats exactly \(GP(6,2)\), not the generalized Petersen family. The eighteen cores are the six-vertex induced octahedral spines; no claim is made that larger sphere subcomplexes are classified. Collapse sequences need not be \(D_6\)-equivariant, and no equivariant deformation retraction is asserted. The dihedral result identifies the homology character, not a canonical equivariant geometric equivalence. A semantically equivalent computation in unindexed literature cannot be excluded; originality assessment is provisional pending independent review.

## References

1. S. R. Campbell, M. N. Ellingham and G. F. Royle, *A characterisation of well-covered cubic graphs*, J. Combin. Math. Combin. Comput. 13 (1993), 193–212. Full author-hosted text: https://math.vanderbilt.edu/ellingmn/paper/wccg/wccg-final-2p.pdf .
2. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European J. Combin. 27 (2006), 906–923, doi:10.1016/j.ejc.2005.04.010 . Author-hosted text: https://www.ms.uky.edu/~jrge/papers/independence.pdf .
3. M. Marietti and D. Testa, *Cores of simplicial complexes*, Discrete Comput. Geom. 40 (2008), 444–468, arXiv:math/0703351 (first public arXiv version 2007-03-12).
4. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (first posted 2005-03-28).
