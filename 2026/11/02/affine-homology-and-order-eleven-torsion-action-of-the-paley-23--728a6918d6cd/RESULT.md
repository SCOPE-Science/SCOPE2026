# Affine homology and order-eleven torsion action of the Paley-23 directed flag complex

## Finding
Let \(Q=(\mathbb F_{23}^{\times})^2=\langle2\rangle\). For the Paley tournament \(P_{23}\) with \(x\to y\) when \(y-x\in Q\), let \(X=\operatorname{dFl}(P_{23})\) and let \(G=\mathbb F_{23}\rtimes Q\) act by affine transformations. Denote by \(W\) the augmentation of the rational permutation representation on the 23 vertices. This is a 22-dimensional rational irreducible \(G\)-representation.

The complete reduced rational homology modules are
\[
\widetilde H_3(X;\mathbb Q)\cong\mathbf1\oplus W,\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbf1\oplus 2W,
\]
with all other reduced rational homology zero. More remarkably, the cyclic torsion subgroup \(\operatorname{Tor} H_3(X;\mathbb Z)\cong\mathbb Z/23\) is not a trivial module: translations act trivially, while the multiplier \(m(x)=2x\) acts by multiplication by \(12\) modulo 23. Since \(12\) has order 11 modulo 23, the torsion detects the full multiplier subgroup.

Consequently \(\widetilde H_3(|X|/G;\mathbb Q)\cong\widetilde H_4(|X|/G;\mathbb Q)\cong\mathbb Q\), with all remaining reduced rational groups zero.

## Assumptions and scope
Work with 23 vertices \(\mathbb F_{23}\), the eleven quadratic residues \(Q=\{1,2,3,4,6,8,9,12,13,16,18\}\), and the transitive-subtournament simplicial complex. A simplex is a subset admitting a total ordering with all arcs forward. In a tournament this ordering is unique. Cellular orientations in the computation use increasing numeric vertex order; changing to the tournament's transitive order only reorients individual simplices and does not change the results. Let \(T\cong C_{23}\) be the translation subgroup and \(M\cong C_{11}\) the multiplier subgroup of \(G\); \(|G|=253\). All integral statements refer to singular or simplicial homology of the geometric realization.

## Proof
A tournament subset is transitive if and only if none of its three-vertex subsets is a directed cycle. Enumerating all cyclic triples (506) and rejecting every subset containing one yields the exact face vector \((23,253,1265,2530,1518)\). Pair an unmatched face with its augmentation by vertex \(v\) whenever both remain, processing \(v=0,1,\ldots,22\) and the faces in increasing bitmask order. This gives 2,681 pairs, with one critical vertex, 102 critical three-cells, and 124 critical four-cells. The directed Hasse graph, in which matched incidences are reversed, is acyclic on all 5,589 nonempty faces; 22,011 codimension-one incidences are checked. Recursive algebraic Morse cancellation yields an exact integer matrix of shape \(102\times124\), whose Smith invariants are 78 units and one 23. Thus \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{23}\oplus\mathbb Z/23\) and \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{45}\). The nonequivariant homotopy classification to which these groups belong was already published [1]; it is not the novelty claim here.

The affine transformations preserve the arc relation. Form signed invariant cellular chain groups by taking the orbit-sums of oriented simplices; an orbit with a sign-reversing stabilizer contributes zero. Over the field \(\mathbb F_{1009}\), the invariant chain dimensions in degrees 0 through 4, boundary ranks, and resulting Betti numbers are as follows:

| Subgroup | Invariant chain dimensions | Boundary ranks | Betti numbers |
|---|---|---|---|
| \(T\) | \((1,11,55,110,66)\) | \((0,11,44,65)\) | \((1,0,0,1,1)\) |
| \(M\) | \((3,23,115,230,138)\) | \((2,21,94,133)\) | \((1,0,0,3,5)\) |
| \(G\) | \((1,1,5,10,6)\) | \((0,1,4,5)\) | \((1,0,0,1,1)\) |

Since 1009 is prime to 253 and the exact integral Smith calculation shows no 1009-torsion, these dimensions are the rational invariant dimensions. Any irreducible rational representation of \(G\) is either inflated from \(G/T\cong C_{11}\) or has nontrivial translation action. The inflated irreducibles have dimensions 1 and 10, while the 22-dimensional augmentation module \(W\) is the unique irreducible rational type with nontrivial translation action: the two 11-dimensional complex inductions from the nontrivial translation characters are interchanged by Galois conjugation. The \(T\)-invariant dimension one, together with total rational ranks 23 and 45, forces exactly the stated \(\mathbf1\oplus W\) and \(\mathbf1\oplus2W\) decompositions.

To detect torsion equivariance, decompose the full cellular chain complex over \(\mathbb F_{23}\) into eigenspaces for the order-eleven map \(m:x\mapsto2x\). All eleven eigenvalues lie in \(\mathbb F_{23}\). The eigenvalue-one reduced Betti dimensions are \((3,5)\) in degrees \((3,4)\); the eigenvalue-12 dimensions are also \((3,5)\); each of the other nine eigenvalues has dimensions \((2,4)\). On the reduction modulo 23 of the free integral homology, \(\mathbf1\oplus W\) contributes multiplicities 3 at eigenvalue one and 2 otherwise in degree three; \(\mathbf1\oplus2W\) contributes 5 at eigenvalue one and 4 otherwise in degree four. Because \(|M|=11\) is prime to 23, passage to mod-23 eigenspaces of free integral lattices is exact, and the additional degree-three eigenspace comes from \(\mathbb Z/23\subset H_3(X;\mathbb Z)\). It is precisely the eigenvalue 12. The universal coefficient sequence independently accounts for the same additional eigenvalue in degree four. Every translation has order 23 and acts on a cyclic group of order 23 through the multiplicative group of order 22, hence trivially. Thus the torsion module action is exactly as stated.

For finite cellular actions, barycentric subdivision and rational transfer give \(H_j(|X|/G;\mathbb Q)\cong H_j(X;\mathbb Q)^G\); the full-invariant ranks give the orbit-space conclusion.

## Verification
Run `python paley23_equivariant_check.py` with Python 3.10+ and SymPy. This program reconstructs all simplices from the tournament, verifies every matched Hasse edge and global acyclicity, computes the integral Smith normal form without cached external matrices, enumerates all 253 affine transformations for the invariant complexes, and computes all 11 eigenchain complexes over \(\mathbb F_{23}\). Expected completion marker: `PAL23_AFFINE_FREE_MODULES_AND_23_TORSION_CHARACTER_OK`. These are finite exhaustive computations for this explicitly specified tournament; no claim of a uniform infinite-family theorem is made.

## Relationship to prior work
Govc's complete order-23 doubly regular tournament classification already contains the nonequivariant Moore-space wedge \(M(\mathbb Z/23,3)\vee\bigvee^{23}S^3\vee\bigvee^{45}S^4\) in Proposition 3.4 [1]. Thus the homotopy type and Betti numbers are premises and independently rechecked, not presented as original. The theorem here refines that known type by computing its canonical affine action, including the previously undetermined scalar on the 23-primary torsion class and the induced rational orbit-space homology. Related results on the affine homology of the 19-vertex Paley tournament concern a different graph and do not imply this character.

## Limitations
The result is for the natural affine subgroup of the Paley tournament automorphism group. It does not assert an integral classification of the orbit space or an equivariant homotopy decomposition. The characteristic-23 action is determined at the level of homology, not chain-homotopy type. Exhaustive finite computations are reproducible but still require external independent review before being treated as independently validated. Equivalent specialized work outside the inspected literature may exist.

## References
[1] Dejan Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333v1 (public June 9, 2020), especially §3.2, Proposition 3.4. https://arxiv.org/html/2006.05333v1

[2] Dejan Govc, Ran Levi, and Jason P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, arXiv:2003.00324 (2020). https://arxiv.org/abs/2003.00324
