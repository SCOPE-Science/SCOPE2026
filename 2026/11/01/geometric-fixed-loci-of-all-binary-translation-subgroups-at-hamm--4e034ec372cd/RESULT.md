# Geometric fixed loci of all binary translation subgroups at Hamming scale two

## Finding
Let \(Q_n=\{0,1\}^n\) with Hamming metric and let \(X_n=\operatorname{VR}_{\le2}(Q_n)\). For \(n\ge3\) and any nonzero binary linear subspace \(H\subseteq\mathbb F_2^n\), acting by translations, the actual geometric fixed locus is:

\[
|X_n|^H\cong_{\mathrm{PL}}
\begin{cases}
|Q_{n-1}|,&\dim H=1,\ \max_{h\in H}|h|\le2,\\
\{1,\ldots,2^{n-2}\}\text{ with the discrete topology},&\dim H=2,\ \max_{h\in H}|h|\le2,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]

The first case is a connected graph, hence has homotopy type \(\bigvee^{(n-3)2^{n-2}+1}S^1\); the second is \(\bigvee^{2^{n-2}-1}S^0\). This is an exhaustive classification for every nontrivial translation subgroup. The trivial subgroup fixes the entire original complex, whose ordinary homotopy type is given by Adamaszek and Adams [2].

## Assumptions and scope
Write \(\mathbb F_2^n\) additively. The Hamming weight \(|x|\) counts the nonzero coordinates of \(x\). The inclusive Vietoris–Rips complex \(X_n\) has every finite set of binary words of pairwise Hamming distance at most two as a face. The finite-dimensional vector subspace \(H\ne\{0\}\) acts simplicially by adding each codeword to every vertex. Geometric fixed points are points fixed individually by every element of \(H\), not vertices fixed pointwise and not homology invariants. The graph \(Q_{n-1}\) denotes its one-dimensional cubical graph (vertices binary words, edges at distance one), not the full cubical polytope.

## Proof
**Orbit realization lemma.** Given any finite simplicial complex \(K\) with simplicial finite-group action, partition its vertices into group orbits. An orbit is *admissible* if its union is a simplex. The pointwise fixed locus \(|K|^H\) is PL-homeomorphic to the complex whose vertices are barycenters of admissible orbits and whose faces are collections of orbits whose union is a simplex. Indeed a fixed barycentric point has equal coefficients at all vertices in each orbit; rescaling those nonnegative orbit-coefficients by orbit cardinality is a unique affine simplex identification. The identifications agree on overlapping faces.

Here every orbit is the coset \(x+H\). Its diameter is \(\max_{h\in H}|h|\), independent of \(x\). If some \(h\in H\) has weight greater than two, no orbit is admissible, so the fixed locus is empty. Assume henceforth every word of \(H\) has weight at most two.

**No rank-three admissible subgroup.** If \(H\) has dimension \(k\), let \(s\) count the coordinates on which some word in \(H\) is nonzero. Each such coordinate is a nonzero linear functional on \(H\), hence equals one on exactly \(2^{k-1}\) group elements. Thus \(\sum_{h\in H}|h|=s2^{k-1}\). Under the weight-two condition, \(s2^{k-1}\le2(2^k-1)\), which forces \(s<4\), hence \(s\le3\). Since \(k\le s\), any \(k\ge3\) must have \(k=s=3\). Such an \(H\) is the entire binary three-cube on its three active coordinates, and contains a word of weight three, a contradiction. Thus \(k\le2\).

**Rank two.** All \(2^{n-2}\) cosets are admissible and determine vertices of the fixed complex. Suppose two distinct cosets \(x+H\) and \(y+H\) could jointly span a simplex. Their union is the affine space \(x+\langle H,y-x\rangle\), since \(y-x\notin H\). Its differences form a three-dimensional subspace of weight at most two. The preceding argument rules this out. Consequently the orbit complex consists of exactly \(2^{n-2}\) isolated vertices.

**Rank one, weight one.** After permuting coordinates let \(H=\langle e_1\rangle\). The cosets are indexed by the remaining \(n-1\) bits \(y\). For two distinct cosets indexed by \(y,z\), the maximum Hamming distance between their vertices is \(1+d_H(y,z)\). Their union is a simplex exactly when \(d_H(y,z)=1\). Hence the orbit graph is exactly \(Q_{n-1}\). No three distinct cosets are pairwise compatible: the hypercube graph is triangle-free, so there are no higher faces.

**Rank one, weight two.** After permuting coordinates take \(H=\langle e_1+e_2\rangle\). Index a coset by \((p,y)\), where \(p=x_1+x_2\pmod2\) and \(y=(x_3,\ldots,x_n)\). Two distinct cosets of equal parity \(p\) have maximum cross-coset distance \(2+d_H(y,z)>2\). Cosets of opposite parity have maximum distance \(1+d_H(y,z)\), hence are compatible precisely when \(d_H(y,z)\le1\). The invertible relabeling \((p,y)\longmapsto(p+\sum_j y_j\pmod2,y)\) carries these edges to the ordinary Hamming-distance-one edges of \(Q_{n-1}\). Since this cube graph is triangle-free, there are no higher-dimensional orbit faces. This proves the PL identification.

Finally \(Q_{n-1}\) is connected with \(2^{n-1}\) vertices and \((n-1)2^{n-2}\) edges; its first Betti number is \((n-3)2^{n-2}+1\), giving the asserted wedge of circles. A discrete set of \(2^{n-2}\) points has the stated zero-sphere wedge homotopy type.

## Verification
The standalone Python 3 script `translation_fixed_verifier.py` enumerates every binary linear subspace in each dimension \(3\le n\le6\) (respectively 16, 67, 374, and 2825 subspaces), builds admissible cosets, computes all compatibility edges, and checks the explicit cubical isomorphism for every eligible rank-one subgroup and complete edge absence for every eligible rank-two subgroup. It reports PASS on these finite checks. These enumerations are finite corroboration; the proof above establishes all \(n\ge3\).

## Relationship to prior work
Adamaszek and Adams [2] determine the nonequivariant homotopy type of \(\operatorname{VR}_{\le2}(Q_n)\), a wedge of three-spheres for \(n\ge3\). Galetto, Montaño and Wellner [1] study hyperoctahedral representations on the complex's homology at several scales, including two. Their publicly accessible abstract describes representation decompositions, not geometric fixed loci for every translation subgroup. The present classification gives actual fixed-space PL types, including graphs, discrete spaces and empty loci, which are not determined solely by an ambient homology character. The full text of [1] was not accessible for a complete implication comparison; an undiscovered or implicit equivalent fixed-point result remains a risk.

## Limitations
The classification concerns pure binary translations of the inclusive Hamming scale-two complex, not arbitrary affine coordinate permutations or other Rips scales. It gives homotopy types of the fixed graph or point set, not equivariant homotopy equivalences of the entire ambient complex. No independent validation has been performed.

## References
[1] F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public 2026-06-18).

[2] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public 2021-03-01); see Theorem 1, its graph conventions and introductory table.
