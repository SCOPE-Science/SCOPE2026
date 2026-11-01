# Dihedral-subgroup fixed-point topology of Möbius-ladder independence complexes

## Finding

Let \(n\ge4\). The Möbius ladder \(M_{2n}\) has vertex set \(\mathbb Z/(2n)\), rim edges \(\{v,v+1\}\), and antipodal chords \(\{v,v+n\}\), with indices modulo \(2n\). Write \(X_n=\operatorname{Ind}(M_{2n})\), \(r(v)=v+1\), and \(s(v)=-v\). Its standard dihedral group is \(D_{2n}=\langle r,s\rangle\). Every subgroup is of one of the forms

\[
H_d=\langle r^d\rangle,\qquad H_{d,b}=\langle r^d,r^bs\rangle,
\qquad d\mid2n,\quad 0\le b<d.
\]

Here \(d=2n\) denotes the trivial rotation subgroup. The following classification is an exact geometric fixed-space result, rather than a classification of invariant vertices or rational Lefschetz traces.

**Theorem.** If \(d\mid n\), both \(|X_n|^{H_d}\) and \(|X_n|^{H_{d,b}}\) are empty. Otherwise \(d\) is even, say \(d=2m\). Define \(M_2=K_2\), \(L_t=P_t\square K_2\) for \(t\ge1\), and the convention \(|\operatorname{Ind}(L_0)|=\varnothing\). There are piecewise-linear homeomorphisms

\[
|X_n|^{H_d}\cong_{\mathrm{PL}}|\operatorname{Ind}(M_{2m})|,
\qquad
|X_n|^{H_{d,b}}\cong_{\mathrm{PL}}|\operatorname{Ind}(L_{t(m,b)})|,
\]

where

\[
t(m,b)=\begin{cases}
\lceil m/2\rceil,&b\text{ even},\\
\max\{0,\lfloor m/2\rfloor-1\},&b\text{ odd}.
\end{cases}
\]

For every positive \(t\), \(\operatorname{Ind}(L_t)\simeq S^{\lfloor(t-1)/2\rfloor}\), integrally and nonequivariantly. Cyclic-subgroup fixed spaces have the smaller-Möbius homotopy types computed by the cited ambient theorem, with \(M_2=K_2\) as a direct base case. Thus the theorem completely determines the integral homotopy type of the fixed space for every subgroup of the specified dihedral group (but not the maps between fixed spaces).

For both reflection classes \(\langle s\rangle\) and \(\langle rs\rangle\), the fixed space is a sphere when \(n\ge4\). Its total mod-two Betti number is two. The ambient homotopy theorem of Agarwal and Basak gives total mod-two Betti number four when \(n\equiv2\pmod4\), and two otherwise. Consequently Smith inequality is **sharp for both reflection classes precisely when \(n\not\equiv2\pmod4\)**.

## Assumptions and scope

All graphs are simple. The independence complex includes the empty face, but its geometric realization has no points when there are no nonempty faces. The symbol \(M_2\) is the explicitly defined two-vertex graph \(K_2\), not an assertion that it is a conventional cubic Möbius ladder. The finite graph \(L_0\) has no vertices. Homotopy equivalences concern integral homotopy types, and the fixed spaces are those of the actual geometric realization of \(X_n\) under affine vertex permutations. All subgroup cases use the complete standard dihedral action; no classification of the possibly larger full graph automorphism group is asserted.

## Proof

**1. Fixed-orbit lemma.** Let a finite group \(H\) permute the vertices of a graph \(G\). A point of \(|\operatorname{Ind}(G)|\) is specified by nonnegative barycentric coordinates summing to one. It is fixed by \(H\) exactly when its coordinates are constant on each \(H\)-orbit. A vertex orbit can carry positive weight only if it is an independent subset of \(G\); two such orbits can occur together only if no edge runs between them. Hence the fixed space is canonically PL homeomorphic to the independence complex of the *orbit incompatibility graph*: vertices are the independent vertex orbits, and two orbits are adjacent when at least one graph edge joins them. Explicitly, one assigns total orbit weight \(w_O\) to an orbit \(O\), then places barycentric coordinate \(w_O/|O|\) on each vertex of \(O\). This gives inverse piecewise-linear maps on every simplex.

**2. Rotation reduction.** For \(H_d=\langle r^d\rangle\), the rotation orbits are precisely the residue classes modulo \(d\). If \(d\mid n\), each class contains two antipodal vertices joined by a chord; no orbit is independent, so the fixed space is empty. Conversely, if \(d\nmid n\), the divisor relation \(d\mid2n\) forces \(d\) even and \(n\equiv d/2\pmod d\). In this case \(d\ge2\), no rim edge or chord lies inside a residue class, and the orbit graph has edges between residues differing by \(1\) or \(d/2\). It is exactly \(M_d=M_{2m}\), with the explicit \(K_2\) convention when \(d=2\). The first claimed PL homeomorphism follows.

**3. Reduction of arbitrary dihedral subgroups.** Every subgroup either lies in the rotation group or has rotation subgroup \(H_d\) and one reflection coset represented by \(r^bs\). On the rotation-orbit graph \(M_d\), this reflection sends the residue \(i\) to \(b-i\pmod d\). Applying the fixed-orbit lemma a second time computes \(|X_n|^{H_{d,b}}\) as the fixed space for this reflection on \(|\operatorname{Ind}(M_{2m})|\). Since \(d=2m\) is even, the parity of \(b\) selects the two conjugacy types.

**4. Even reflection axis.** For the reflection \(i\mapsto-i\) of \(M_{2m}\), choose orbit representatives \(O_i=\{i,-i\}\) for \(0\le i\le m\). The endpoint orbits are singletons. When \(m\) is even, the sole forbidden orbit is \(O_{m/2}\), whose two elements are joined by an antipodal chord; for odd \(m\) there are no forbidden orbits. Rim edges give adjacency of consecutive orbit labels; chords give adjacency between \(O_i\) and \(O_{m-i}\). With \(t=\lceil m/2\rceil\), the two rails of a ladder are \(O_j\) and \(O_{m-j}\) for \(0\le j<t\). These are all allowed orbits, and the listed rim and chord adjacencies are exactly the two rails and their \(t\) rungs. There are no other adjacencies. Thus the orbit graph is \(L_t\).

**5. Odd reflection axis.** For \(i\mapsto1-i\), representatives are \(O_i=\{i,1-i\}\), \(1\le i\le m\). The orbits \(O_1\) and \(O_m\) contain rim edges. If \(m\) is odd, \(O_{(m+1)/2}\) additionally contains an antipodal chord. These are precisely the forbidden orbits, with coincidences in the small cases understood. The remaining labels form two rails with representatives \(O_{2+j}\) and \(O_{m-1-j}\), for \(0\le j<t\), where \(t=\max\{0,\lfloor m/2\rfloor-1\}\). Rim edges give consecutive rail edges, and chords give the rungs. Thus the orbit graph is \(L_t\) if \(t>0\), and has no vertices otherwise. This proves every PL assertion, including the small cutoff \(m\le3\) for odd-axis emptiness.

**6. Ladder homotopy.** Write \(L_t\) with rail vertices \(a_1,\ldots,a_t\) and \(b_1,\ldots,b_t\). The standard independence-complex fold lemma says that \(N(u)\subseteq N(v)\) permits deletion of \(v\) up to homotopy. For \(t\ge3\), \(N(a_1)=\{a_2,b_1\}\subseteq N(b_2)\), so delete \(b_2\). In the remaining graph \(N(b_1)=\{a_1\}\subseteq N(a_2)\), so delete \(a_2\). The resulting graph is the disjoint union of an isolated edge \(a_1b_1\) and \(L_{t-2}\). Since the independence complex of an isolated edge is \(S^0\), disjoint graph union becomes a simplicial join, and therefore

\[
\operatorname{Ind}(L_t)\simeq\Sigma\operatorname{Ind}(L_{t-2})\qquad(t\ge3).
\]

The base cases \(L_1=K_2\) and \(L_2=C_4\) both have independence complexes homotopy equivalent to \(S^0\). Induction gives \(S^{\lfloor(t-1)/2\rfloor}\) for every \(t\ge1\). The fold lemma follows, for example, by pairing faces containing \(v\) without \(u\) with the faces obtained by adding \(u\), since \(N(u)\subseteq N(v)\); this is an acyclic elementary collapse.

**7. Smith equality.** For the two reflections on \(M_{2n}\), \(d=2n\), \(m=n\), and the ladder lengths are \(\lceil n/2\rceil\) and \(\lfloor n/2\rfloor-1\), both positive for \(n\ge4\). Each fixed space is a sphere, hence has total mod-two Betti rank two. The established nonequivariant homotopy formula for \(\operatorname{Ind}(M_{2n})\) is a wedge of three spheres if \(n\equiv2\pmod4\) and a single sphere otherwise. Comparing total mod-two ranks gives strict Smith inequality exactly in the first case.

## Verification

The standalone `verify_reflection.py` checker constructs every relevant graph and subgroup orbit directly from vertex permutations, independently of the above symbolic reduction. It compares exact labeled orbit graphs with the displayed ladder identifications for both reflection types at \(4\le n\le120\). It also checks 4,711 direct subgroup orbit graphs, including all divisor-subgroup types and additional noncanonical generating exponents. Augmented mod-two simplicial boundary calculations confirm the reduced homology of both reflection fixed spaces for \(4\le n\le18\), and the cited ambient Betti ranks for \(4\le n\le9\). The exceptional small quotient cases are checked separately. Running `python verify_reflection.py` requires only the standard library. These finite verifications corroborate but do not replace Steps 1–7, which are the proof for all parameters.

## Relationship to prior work

Agarwal and Basak, first publicly posted on August 31, 2026 and revised on September 14, 2026, determine the ordinary homotopy types of Möbius and circular-ladder independence complexes. Their Section 4.1 studies nonequivariant Möbius-ladder topology, while Section 6 explicitly identifies further questions about graph complexes and symmetries. Their ordinary sphere counts are used here for the cyclic quotient and Smith comparison; they are not claimed as new. Previously indexed dihedral *rational homology character* computations for Möbius-ladder independence complexes determine traces on ordinary homology, not the geometric fixed-point homotopy types of every subgroup. The orbit-graph homeomorphisms, subgroup-complete classification, and exact Smith-equality criterion are the present contribution. A related fixed-space classification for circular-ladder independence complexes concerns a different graph and does not logically supply these Möbius-ladder subgroup reductions. The known fold lemma is used as a standard tool rather than presented as new.

## Limitations

The result classifies individual subgroup fixed-space homotopy types and provides PL models but does not determine all restriction maps among those fixed spaces, a complete equivariant homotopy type, or the integral dihedral homology lattice. It concerns the specified dihedral action, not every possible graph automorphism in small exceptional cases. The source's ordinary homotopy classification is relied upon for the cyclic-quotient sphere multiplicities and Smith comparison. A previously unindexed equivariant classification could affect the originality assessment. Independent mathematical audit has not been performed.

## References

- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, original public submission August 31, 2026, revised September 14, 2026. https://arxiv.org/html/2608.30601v2 . See Sections 2, 4.1, and 6.
- Standard independence-complex fold lemma, recalled as Proposition 6 in Agarwal and Basak (citing the earlier literature there).
