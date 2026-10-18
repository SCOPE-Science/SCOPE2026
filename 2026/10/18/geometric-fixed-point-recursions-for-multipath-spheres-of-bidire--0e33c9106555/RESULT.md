# Geometric fixed-point recursions for multipath spheres of bidirected linear graphs

## Finding
For every integer \(n\ge2\), let \(B_n\) be the directed graph on \(0,1,\ldots,n\) with both arrows on each consecutive edge, and let \(X_n\) be its multipath simplicial complex. Let \(F\) reverse each arrow and let \(R\) be reflection of the underlying path, sending vertex \(i\) to \(n-i\). Although \(F\) reverses all arrows rather than acting as a covariant digraph automorphism, it is a simplicial involution of the multipath complex. Put \(J=FR\) and \(m=\lceil n/2\rceil\). These commuting involutions generate \(G\cong C_2\times C_2\).

There are canonical piecewise-linear homeomorphisms of geometric fixed-point spaces
\[
|X_n|^F=\varnothing,\qquad |X_n|^R\cong|X_{m-1}|,\qquad |X_n|^J\cong|X_m|.
\]
Here \(X_0\) is the augmented complex with only its empty face, whose geometric realization is empty. By the previously established nonequivariant sphere theorem, \(X_k\simeq S^{\lfloor(k-1)/2\rfloor}\) for every \(k\ge1\). Consequently, the \(R\)-fixed space is empty if \(m=1\) and otherwise has homotopy type \(S^{\lfloor(m-2)/2\rfloor}\); the \(J\)-fixed space has homotopy type \(S^{\lfloor(m-1)/2\rfloor}\) for all \(m\ge1\).

The complete action on the one-dimensional integral reduced homology group \(\widetilde H_{m-1}(X_n;\mathbb Z)\cong\mathbb Z\) is
\[
F\longmapsto(-1)^m,\qquad R\longmapsto(-1)^{\lceil m/2\rceil},\qquad J\longmapsto(-1)^{m+\lceil m/2\rceil}.
\]
All other reduced integral homology groups vanish. For the full symmetry quotient \(Y_n=|X_n|/G\), rational homology therefore satisfies
\[
\widetilde H_j(Y_n;\mathbb Q)\cong
\begin{cases}
\mathbb Q,&j=m-1\text{ and }n\equiv0,7\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]
This gives the fixed-point topology and all rational homology characters and full-group quotient Betti numbers in an infinite natural family.

## Assumptions and scope
A simplex of \(X_n\) is a finite set of directed arrows whose union has connected components that are coherently directed paths or isolated vertices, without directed cycles. Write \(a_i^+\) for the arrow \(i\to i+1\), and \(a_i^-\) for \(i+1\to i\), with \(0\le i<n\). Equivalently, a face uses at most one of \(a_i^+,a_i^-\) for each \(i\), and any two simultaneously selected arrows at neighboring positions have identical signs. The action is \(F(a_i^s)=a_i^{-s}\), \(R(a_i^s)=a_{n-1-i}^{-s}\), and \(J(a_i^s)=a_{n-1-i}^{s}\). All geometric fixed-point assertions refer to realizations of the unaltered simplicial complexes, not to merely fixed vertices. The integral homology statement is an action of \(G\) on the underlying rank-one free abelian group, and the quotient statement concerns ordinary rational homology only.

## Proof
**1. The orbit-barycenter fixed-point lemma.** Let a finite cyclic permutation group act simplicially on a finite complex \(K\). A point of \(|K|\) is fixed exactly when its barycentric coordinates are constant on vertex orbits. Because the support of a point is a unique simplex, a positive orbit can occur only when its whole vertex set is itself a face. Let \(K_{\mathrm{orb}}\) have as vertices the orbits that individually are faces; a set of orbit vertices is a simplex when their union is a face of \(K\). Sending each orbit vertex to the barycenter of that orbit, and extending affinely, gives a PL homeomorphism \(|K_{\mathrm{orb}}|\cong |K|^g\), since on every supporting simplex the map identifies precisely the fixed barycentric locus. This argument also includes the case of an empty fixed-point set.

**2. Global arrow reversal.** Every \(F\)-orbit on arrow vertices is \(\{a_i^+,a_i^-\}\). Its two arrows are incompatible, so the orbit complex has no vertices and \(|X_n|^F=\varnothing\).

**3. Geometric reflection.** Put \(m=\lceil n/2\rceil\). For \(0\le i\le m-2\), the two \(R\)-orbits indexed by signs \(s\in\{+,-\}\) are
\[
\{a_i^s,a_{n-1-i}^{-s}\}.
\]
If \(n=2m-1\) is odd, the central physical edge has an orbit containing both opposing arrows, so it cannot be selected. If \(n=2m\) is even, the two central adjacent physical edges are interchanged with opposite signs; either central orbit would create incompatible adjacent arrows and is forbidden. Every remaining orbit is legal. Two or more of them have a legal union if and only if the corresponding selections of \(a_i^s\), for \(0\le i<m-1\), form a multipath of the bidirected path with \(m-1\) physical edges. There is no interaction across the omitted central edge or the omitted central pair. The orbit complex is therefore simplicially isomorphic to \(X_{m-1}\). Step 1 proves the claimed PL homeomorphism for \(R\).

**4. Reflect positions while preserving the arrow sign.** Under \(J\), each left position \(i<m-1\) yields the orbit \(\{a_i^s,a_{n-1-i}^s\}\). There are two additional legal central orbits, indexed by the sign. If \(n=2m-1\), these are the singleton arrows \(\{a_{m-1}^s\}\) on the fixed central physical edge. If \(n=2m\), they are the pairs \(\{a_{m-1}^s,a_m^s\}\) on the two central physical edges; both edges in such a pair have the same sign and hence form a directed path. Opposite-sign central orbits are incompatible. Compatibility between these orbits, including the central ones, is exactly the adjacency-sign rule on a bidirected path with \(m\) physical edges. Thus the orbit complex is simplicially isomorphic to \(X_m\). Step 1 proves the asserted PL homeomorphism for \(J\).

**5. The nonequivariant sphere and its unique integral homology generator.** For \(n\ge2\), the stars of \(a_0^+\) and \(a_0^-\) cover \(X_n\); any face can be extended by one of these two arrows. Each star is a cone, and their intersection consists precisely of faces supported in positions \(2,\ldots,n-1\), hence is \(X_{n-2}\). Their union is homotopy equivalent to the unreduced suspension of that intersection. The bases are \(X_1\simeq S^0\) and \(X_2\simeq S^0\); in the second base the cone intersection is empty. Induction gives \(X_n\simeq S^{m-1}\). This homotopy type was established by Caputi, Collari and Smith (Proposition 2.2); it is recalled here to make the subsequent equivariant argument self-contained.

**6. The integral character.** For a finite simplicial involution \(g\), the alternating trace on the augmented simplicial chain complex equals the reduced Euler characteristic of its geometric fixed-point space. To see this without an equivariant homotopy assumption, a setwise invariant simplex decomposes into \(q\) vertex orbits; multiplying its chain-degree sign by the determinant of the permutation of its vertices contributes \((-1)^{q+1}\), the reduced Euler contribution of the orbit simplex. Thus \(\widetilde L(g)=\widetilde\chi(|X_n|^g)\). Since the only reduced homology occurs in degree \(m-1\), its trace is \((-1)^{m-1}\widetilde L(g)\). For \(F\), the fixed space is empty and has reduced Euler characteristic \(-1\), giving \((-1)^m\). For \(R\), if \(m\ge2\), Step 3 and the sphere formula give \(\widetilde L(R)=(-1)^{\lfloor(m-2)/2\rfloor}\), hence \(R\) acts by \((-1)^{m-1+\lfloor(m-2)/2\rfloor}=(-1)^{\lceil m/2\rceil}\). The same identity holds for \(m=1\), when the fixed set is empty and the degree-zero action is \(-1\). The action of \(J=FR\) is the product of these two signs. Because the homology is a free rank-one integral lattice, these rational traces are the exact integral actions.

**7. Quotients.** Barycentric subdivision removes simplex inversions, and averaging over a finite group in characteristic zero identifies rational homology of the geometric quotient with the invariant rational homology of the original complex. Our only nonzero reduced representation is a line. Both \(F\) and \(R\) act trivially precisely when \(m\) is divisible by four. Since \(m=\lceil n/2\rceil\), this occurs exactly when \(n\equiv0,7\pmod8\). This proves the quotient formula.

## Verification
The standalone program `verify_bidirected_linear_fixed_points.py` independently enumerates directed multipaths as ternary words, computes signed augmented-chain traces for \(F,R,J\) for all \(1\le n\le12\), checks the proposed orbit maps for both geometric involutions against every possible orbit-subset assignment for these sizes, and computes reduced mod-two homology using independently assembled simplicial boundary matrices for \(1\le n\le6\). All 12 character checks, all 24 orbit-complex checks and all six mod-two calculations pass; `verification_output.txt` records the exact execution. The all-size theorem follows from Steps 1–7, not from finite enumeration.

## Relationship to prior work
Caputi, Collari and Smith (2026), Proposition 2.2, established the ordinary sphere homotopy type of the bidirected linear multipath complex. Their paper's analysis of the linear and polygonal families does not calculate the geometric fixed spaces or the arrow-reversal and spatial-reflection integral characters of the linear family. A separate publicly available mathematical note, *Dihedral rational homology of bidirectional-polygon multipath complexes* (2026), calculates a dihedral representation for bidirected **cycles**, using fixed-orbit counts that fold reflected cycles to bidirected paths. Its cycle representations and use of path Euler characteristics do not assert or determine the present two fixed-point homeomorphisms for **linear** paths or their full \(C_2\times C_2\) character and quotients. The general orbit-barycenter mechanism is standard; the claimed contribution is the exact identification of the orbit complexes, all-parameter geometric fixed-point topology, and its symmetry consequences, not the generic mechanism or the known nonequivariant sphere theorem.

## Limitations
The result does not assert a new sphere classification for \(X_n\), nor a complete equivariant homotopy equivalence with a linear action on a sphere. Although it determines integral rank-one actions, it gives quotient homology only over \(\mathbb Q\), not the full integral homology or fundamental groups of the quotients. An unindexed general equivariant folding theorem could subsume the fixed-point description. The finite checker supports the symbolic proof but does not constitute a proof for arbitrary \(n\).

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first submitted 2026-01-09, especially Definition 1.2, Proposition 2.2 and the discussion in Section 2. https://arxiv.org/html/2601.05670v1
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, *Journal of Algebraic Combinatorics* 57 (2023), Section 6, DOI 10.1007/s10801-022-01180-9. https://link.springer.com/article/10.1007/s10801-022-01180-9
3. *Dihedral rational homology of bidirectional-polygon multipath complexes*, publicly available mathematical note (2026), especially the statements and proofs about cycle symmetries and reflection-orbit counts. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-rational-homology-of-bidirectional-polygon-multipath-co--627013477864
