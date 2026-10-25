# Translation homology remembers the evaluation directions of affine orthogonal-array inflations
## Finding
Let \(q\ge 3\) be a prime power, \(4\le n\le q+1\), and let \(L_0,\ldots,L_{n-1}:\mathbb F_q^2\to\mathbb F_q\) be pairwise nonproportional nonzero linear forms. Associate to these forms the simplicial complex \(K_L\) whose facets are the \(q^2\) sets
\[
 F_z=\{(i,L_i(z)):0\le i<n\},\qquad z\in\mathbb F_q^2.
\]
The translation group \(T=(\mathbb F_q^2,+)\) acts by \(t\cdot(i,a)=(i,a+L_i(t))\). Then \(K_L\) admits a \(T\)-equivariant sequence of simplicial elementary collapses onto the complete bipartite graph \(K_{q,(n-1)q}\), with the first color class consisting of vertices in coordinate zero. In particular,
\[
 |K_L|\simeq\bigvee^{(n-1)q^2-nq+1}S^1.
\]
The further, symmetry-sensitive classification is exact. Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). For a linear form \(L\), let \(D(L)\subseteq\widehat T\) be the \(q\)-element character line \(\{z\mapsto\psi(aL(z)):a\in\mathbb F_q\}\). If \(m(\chi)\) is the multiplicity of \(\chi\in\widehat T\) in \(H_1(K_L;\mathbb C)\), then
\[
 m(1)=0,\qquad m(\chi)=
 \begin{cases}
 n-2,&1\ne\chi\in\bigcup_iD(L_i),\\
 n-1,&\chi\notin\bigcup_iD(L_i).
 \end{cases}
\]
Consequently, as a representation of the specified translation group \(T\), the first homology recovers **exactly** the chosen set of projective evaluation directions \(\{\mathbb F_q^\times L_i\}\), even though the ordinary homotopy type depends only on \(q\) and \(n\).

Equivalently, the character of the first homology is
\[
 \operatorname{tr}(t\mid H_1)=
 \begin{cases}
 (n-1)q^2-nq+1,&t=0,\\
 1-q,&0\ne t\in\bigcup_i\ker L_i,\\
 1,&t\ne0\text{ and }t\notin\bigcup_i\ker L_i.
 \end{cases}
\]
The associated diagram over the simplex has surjective restriction maps on every **comparable pair of faces** but its sheaf is not flabby: this provides a representation-theoretically distinguishable family outside the flabby-sheaf homotopy theorem.

## Assumptions and scope
The field \(\mathbb F_q\) exists for prime powers \(q\). A set of \(n\) distinct points in its projective line exists exactly for \(n\le q+1\), and the proof applies to every such choice. The index-one strength-two orthogonal array \(\{(L_i(z))_i:z\in T\}\) has \(q^2\) rows because any two chosen nonproportional forms are an invertible linear coordinate system on \(T\). The face poset of \(K_L\) is the generalized simplicial inflation corresponding to the finite assignment diagram \(D(I)=\{(L_i(z))_{i\in I}:z\in T\}\) for nonempty coordinate subsets \(I\). This is a simplicial complex rather than a multicomplex because every pair of coordinate entries extends to a unique row, and \(n\ge4\).

The group action is a labeled \(T\)-action: the recovery statement refers to this identified translation group, not to an unlabelled simplicial homotopy type or an arbitrary change of group coordinates. The character formula is over \(\mathbb C\); the nonequivariant homotopy equivalence and the equivariant collapse are integral statements. No claim is made about multiplicative or semilinear automorphisms beyond translations.

## Proof
**1. Pairwise intersections and local restriction maps.** For distinct \(i,j\), the map \((L_i,L_j):T\to\mathbb F_q^2\) is invertible. Consequently each ordered pair \((a,b)\) occurs exactly once as \((L_i(z),L_j(z))\). Any two distinct facets therefore intersect in at most one vertex: intersection in two coordinates would determine the same \(z\). Every restriction \(D(J)\to D(I)\), for nonempty \(I\subseteq J\), is surjective because an assignment in \(D(I)\) is by definition the restriction of some full row, which also supplies an element of \(D(J)\).

This does **not** imply flabbiness. Consider restriction of sections from the full simplex to its one-skeleton. The latter has every possible pair assignment, so its compatible sections are all \(q^n\) choices of vertex values, while the former has only the \(q^2\) full rows. Since \(n\ge4\), the restriction is not onto. This is a concrete failure of the required arbitrary-open-set extension property.

**2. Translation-equivariant elementary collapse.** Fix coordinate zero. For each row \(z\), let its root be \(r_z=(0,L_0(z))\) and its other \(n-1\) vertices be \(U_z\). For each cardinality \(s=n-1,n-2,\ldots,2\), and for each \(z\) and each \(s\)-element subset \(B\subseteq U_z\), delete the pair \((B,B\cup\{r_z\})\). At the moment it is deleted, \(B\) is free: its unique containing facet is \(F_z\), all larger faces have been removed at preceding stages, and its unique remaining immediate coface is \(B\cup\{r_z\}\). Any competing facet would contain at least two common vertices with \(F_z\), contradicting step 1. The collections of pairs are disjoint and translate into one another under \(z\mapsto z+t\); hence the sequence may be ordered in complete \(T\)-orbits, giving an equivariant elementary-collapse reduction.

Precisely the vertices and the edges meeting coordinate zero remain. For each \(i\ne0\), invertibility of \((L_0,L_i)\) gives every edge between the \(q\) coordinate-zero vertices and the \(q\) coordinate-\(i\) vertices exactly once. Thus the remainder is \(G=K_{q,(n-1)q}\). This connected graph has \((n-1)q^2\) edges and \(nq\) vertices, so its first Betti number is \((n-1)q^2-nq+1\), and its realization is a wedge of that number of circles.

**3. The complete translation representation.** The cellular chain complex of \(G\) over \(\mathbb C\) has \(n-1\) free and transitive \(T\)-orbits of edges (one for each nonzero coordinate index). Therefore \(C_1(G;\mathbb C)\cong\mathbb C[T]^{\oplus(n-1)}\). The coordinate-\(i\) vertices form the transitive \(T\)-set \(T/\ker L_i\), hence \(C_0(G;\mathbb C)\cong\bigoplus_{i=0}^{n-1}\mathbb C[T/\ker L_i]\). The connected graph has \(H_0(G;\mathbb C)\cong\mathbf1\) and no higher homology, so semisimplicity of \(\mathbb C[T]\) and its equivariant chain exact sequence give the identity of representations
\[
 [H_1(G;\mathbb C)]=(n-1)[\mathbb C[T]]-\sum_i[\mathbb C[T/\ker L_i]]+[\mathbf1].
\]
The regular representation contains every character once. The permutation representation \(\mathbb C[T/\ker L_i]\) contains exactly the \(q\) characters trivial on \(\ker L_i\), namely \(D(L_i)\), each once. The projective directions are distinct, so these character lines meet only in the trivial character. The displayed multiplicity formula follows immediately; it is unchanged by the equivariant homotopy equivalence \(K_L\simeq_TG\).

For \(t\ne0\), no edge of \(G\) is fixed, and only the coordinate-\(i\) vertex orbit can have fixed points when \(L_i(t)=0\), in which case all \(q\) vertices in that coordinate are fixed. Since distinct linear kernels intersect only at zero, at most one coordinate has this property. The equivariant Euler–Poincaré trace identity \(\operatorname{tr}(t\mid H_1)=1-\#V^t+\#E^t\) gives the stated three-case trace formula. Finally, the directions can be recovered as the unique order-\(q\) character subgroups whose nontrivial elements have the smaller multiplicity \(n-2\), proving the recovery assertion without a choice of basis for homology.

## Verification
The standalone standard-library script `verify.py` constructs prime-field examples for \((q,n)=(3,4),(5,4),(5,5),(5,6),(7,8)\). It generates all faces, verifies unique pair completion and the private-face property, and performs each elementary simplex collapse with a direct free-face check. It independently constructs the complete bipartite terminal graph. For each translation element it enumerates the simplices fixed by that element and computes its Lefschetz trace, then Fourier-transforms the entire trace table to compare all complex character multiplicities with the theorem. For the first four examples it also independently enumerates allowed faces from all partial assignments, without using the facet-subface constructor. It ends with `VERIFY_OK`. The experiment tests finite prime-field examples; the theorem is proved uniformly for all prime powers and all permissible directions.

## Relationship to prior work
Ayzenberg and Khoroshavkina prove a generalized-inflation wedge theorem subject to a **globally flabby** finite-set sheaf. The present codeword diagrams do not satisfy that hypothesis, and their topology occupies degree one rather than the top dimension of the supporting simplex; the source's theorem does not determine the representation above.

The published *Latin-array inflations exhibit lower homotopy despite unique local lifting* studies arrays of strength \(n-1\), whose facets form \(q^{n-1}\) full words and whose homology appears in degree \(n-2\). The present arrays have strength two with \(q^2\) rows for \(n\ge4\), and the new result specifies the complete translation-character profile rather than merely nonequivariant homotopy.

The published *Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs* gives a useful general method of collapsing simplex unions intersecting in individual vertices. That relative-collapse method suggests the **nonequivariant** graph reduction here; it does not compute how the translation group acts on first homology or prove that the representation recovers the projective evaluation directions. The graph chain-module calculation and representation recovery are the distinguishing results, not an assertion that the elementary relative-collapse lemma is new.

## Limitations
The result recovers evaluation directions relative to a **specified** translation-group action and character identification, not from the underlying nonequivariant homotopy type. It does not assert that arrays with different direction sets are nonisomorphic as plain simplicial complexes, or that distinct sets must be inequivalent under all field-semilinear changes of coordinates. The finite checker covers prime fields only and supports, rather than replaces, the all-prime-power proof. Bibliographic priority cannot exclude unindexed work on equivariant homology of transversal designs or orthogonal-array complexes; no independent scientific audit has been performed.

## References
A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (first public 2026-02-09), Theorem 5.1, Remark 6.2 and Sections 5–7; https://arxiv.org/html/2602.08694v1 .

*Latin-array inflations exhibit lower homotopy despite unique local lifting*, public mathematical research record, 2026, indexed at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-latin-array-inflations-exhibit-lower-homotopy-despite-unique-loc--12e4d5a0c16a .

*Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs*, public mathematical research record, 2026, indexed at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-twin-circle-wedges-in-neighborhood-complexes-of-steiner-design-i--5b757c0a694f .
