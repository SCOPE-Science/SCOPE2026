# Marked-base orbit spectra and a sharp single-parameter recovery threshold for random bipartite reducts

## Finding
Let \(\Gamma\) be the countable random bipartite graph with two named infinite sides. Consider the five side-preserving closed groups in Yun Lu's classification, in this order: \(G_0=\operatorname{Aut}(\Gamma)^*\) (including global edge complementation), \(G_l=S_l(\Gamma)\) (independent left-side switches), \(G_r=S_r(\Gamma)\) (independent right-side switches), \(G_{lr}=S_{l,r}(\Gamma)\), and \(G_\infty=\operatorname{Sym}(R_l)\times\operatorname{Sym}(R_r)\). Let \(\mathcal A\) be any finite individually named base with \(a\ge0\) left vertices and \(b\ge0\) right vertices. For \(k\ge0\), let \(T_G(a,b;k)\) count the orbits of the pointwise stabilizer \(G_{(\mathcal A)}\) on injective ordered \(k\)-tuples from \(\Gamma\setminus\mathcal A\). These are the complete nonalgebraic injective tuple types over the named base in the canonical \(\omega\)-categorical reduct associated with \(G\).

For each \(0\le x\le k\), put \(y=k-x\), \(u=a+x\), \(v=b+y\), and \(e=uv-ab\). Set the following integer ranks when \(uv>0\):
\[
\begin{aligned}
 r_0&=\mathbf{1}_{ab=0},\\
 r_l&=x+a\mathbf{1}_{b=0},\\
 r_r&=y+b\mathbf{1}_{a=0},\\
 r_{lr}&=u+v-1-\mathbf{1}_{ab>0}(a+b-1),\\
 r_\infty&=e.
\end{aligned}
\]
If \(uv=0\), all five ranks are zero. Then, for every choice of the named base and every \(k\ge0\),
\[
\boxed{T_G(a,b;k)=\sum_{x=0}^{k}\binom{k}{x}2^{uv-ab-r_G}.}
\]
In particular, the numbers depend only on \((a,b)\), not on the cross-edge matrix induced on the base.

This all-arity local spectrum has two sharp information properties.

**Balanced-base collision.** The numerical spectra of \(G_l\) and \(G_r\) agree for every arity \(k\) if and only if \(a=b\). Thus even arbitrarily many named parameters in a balanced pair of sides fail to distinguish these two distinct groups numerically; any unbalanced base separates them, at arity one except that a singleton base requires arity two.

**Sharp singleton recovery.** With no parameters, the \(G_l\) and \(G_r\) profiles are identical in every arity. With precisely one named parameter on the left, the ordered spectra for \(k=1,2,3\), in the group order above, are
\[
\begin{array}{c|ccccc}
 k&G_0&G_l&G_r&G_{lr}&G_\infty\\\hline
 1&2&2&2&2&2\\
 2&7&5&6&4&4\\
 3&41&20&26&11&8.
\end{array}
\]
Consequently **one** named parameter is necessary and sufficient for the all-arity numerical spectra to distinguish all five groups, and **three** is the smallest tuple arity that achieves simultaneous distinction with such a singleton base. All equalities and thresholds are exact.

The noninjective ordered tuple-type count \(\widehat T_G(a,b;n)\), which permits repeated coordinates among the new entries but never uses a parameter as a new entry, is exactly the Stirling transform
\[
\widehat T_G(a,b;n)=\sum_{k=0}^{n}\left\{\begin{matrix}n\\k\end{matrix}\right\}T_G(a,b;k).
\]

## Assumptions and scope
The two vertex sides are named and no permutation interchanges them. Both are infinite. A switch on a vertex reverses all its incident cross-edge states; adding switches is computed modulo two. A finite base of size zero is allowed. For fixed side-assignment of new coordinates, their order is retained; the \(\binom{k}{x}\) choices are not quotiented by coordinate permutations. All new tuple entries are distinct and disjoint from the individually named base. No restrictions are imposed on the edge matrix inside the base or on edges involving new entries. A rank stated as zero for \(uv=0\) avoids vacuous row/column actions in one-sided tuples.

## Proof
Fix \(k\), a side-assignment with \(x\) new left and \(y=k-x\) new right entries, and a specific cross-edge matrix on the base. The full finite tuple has \(uv\) possible cross-edges. The \(ab\) base cross-edges are frozen, leaving precisely \(e=uv-ab\) independently free binary entries. Every assignment to those entries occurs by the extension property of the random bipartite graph.

By homogeneity and Lu's characterization of the five closed groups, two such assignments lie in the same pointwise-stabilizer orbit if and only if their difference is a permitted finite switching pattern whose entries on the base rectangle vanish. Indeed, a permitted switch pattern preserving the base rectangle can first be realized on a finite copy by the group action and then composed with a graph automorphism identifying its unchanged named base with the original base; the resulting permutation fixes every named parameter. Conversely, every pointwise-fixed group element has the corresponding global-complement, left-row, right-column, or row-plus-column finite difference pattern. Thus each orbit is an affine coset of a binary linear subspace of the \(e\)-dimensional free-edge space.

For \(G_0\), the only nonzero finite difference is the all-one matrix; it acts on the free entries precisely when \(ab=0\) and \(e>0\). For \(G_l\), a row switch may be independently chosen on every new left vertex. A fixed base-left row may also be switched if and only if there is no fixed base-right vertex. When \(uv>0\), these permitted rows have disjoint nonempty supports and rank \(x+a\mathbf{1}_{b=0}\). The right-side formula is dual.

For \(G_{lr}\), all row-plus-column switching patterns on an \(u\)-by-\(v\) nonempty rectangle have rank \(u+v-1\): simultaneous reversal of all row and all column switch bits is the unique nonzero kernel. If \(ab>0\), restriction to the fixed \(a\)-by-\(b\) base rectangle has rank \(a+b-1\). The kernel of this restriction is exactly the subgroup preserving the base, and its action on the new-edge coordinates is faithful as a subspace of the full switching-pattern image. Rank-nullity gives \(u+v-1-(a+b-1)\). With \(ab=0\), there is no restriction. Finally, \(G_\infty\) realizes all \(2^e\) new-edge configurations in one orbit, yielding rank \(e\). Every group therefore has precisely \(2^{e-r_G}\) orbits for the fixed side-assignment; summing over assignments proves the boxed formula.

Swapping left and right throughout sends \(T_{G_l}(a,b;k)\) to \(T_{G_r}(b,a;k)\). When \(a=b\), substituting \(x\leftrightarrow y\) in the sum proves equality for every \(k\). Conversely, if \(a,b>0\), the one-point counts are
\[
T_{G_l}(a,b;1)=2^{b-1}+2^a,\qquad
T_{G_r}(a,b;1)=2^b+2^{a-1},
\]
whose difference is \(2^{a-1}-2^{b-1}\); hence an unbalanced positive pair separates immediately. If \(a>0,b=0\), the corresponding counts are \(2\) and \(1+2^{a-1}\), so they differ unless \(a=1\); the opposite one-sided case is symmetric. For a singleton base, the two-type counts \(5\) and \(6\) separate the left and right switch groups. This proves the claimed if-and-only-if.

For an empty base, left/right exchange is a bijection between the finite matrix actions, so \(G_l\) and \(G_r\) have identical numerical profiles in all arities. Substituting \((a,b)=(1,0)\) and \(k=1,2,3\) in the exact formula gives the displayed three rows. They prove that arities one and two do not distinguish all five, whereas arity three does. With a singleton on the right, the roles of \(G_l\) and \(G_r\) exchange, so the same threshold holds. Lastly, the equality partition on ordered tuple positions is preserved by every group; collapsing the \(n\) positions into \(k\) equality blocks proves the Stirling transform.

## Verification
The standalone `verify.py` independently generates allowed finite row, column, row-plus-column, and global-complement translation patterns subject to exactly preserving each frozen base rectangle. It counts translation cosets and, on smaller cases, actually enumerates every orbit in the full free-edge space. Its 910 independent group/configuration comparisons include all groups for nonnegative \(a,b,x,y\) with total tuple size at most seven and no more than ten free cross-edges. It separately checks the singleton-base counts, the balanced-base equalities through arity seventeen, and separation for unbalanced bases with side counts at most four. The recorded output is in `verify.out`. The unrestricted result follows from the proof, not from finite enumeration.

## Relationship to prior work
Lu (2011) classified these five groups, defined their switching generators, and characterized them by cross-edge parity conditions. A subsequent published exact **unbased** ordered-tuple orbit profile gives the global finite-matrix quotient counts and notes that the unmarked left- and right-switch profiles coincide. The present result does not claim either classification or those unbased orbit formulas. It addresses the different pointwise-stabilizer problem with a frozen finite base rectangle, gives its complete all-arity local formulas, and determines exactly when numerical base marking eliminates or preserves the left/right collision, including the sharp singleton parameter–arity tradeoff. The elementary switching mechanism is shared with both sources. Searches did not identify a previously stated covering theorem for these marked-base calculations or their exact thresholds.

## Limitations
The finding concerns the five *side-preserving* groups in Lu's classification and only numerical orbit/type spectra, not equivalence of the groups or recovery from arbitrary logical presentations. The proof exploits the known switching-group classification and is not an independent new classification of reducts. Unindexed prior work may already derive the same conditioned switching ranks or parameter thresholds; the original all-matrix orbit characterization makes them accessible by additional linear algebra. The finite verifier is corroboration, not a replacement for the all-size argument. Independent validation has not been performed.

## References
1. Yun Lu, “Reducts of the Random Bipartite Graph,” arXiv:1101.1947, first publicly posted 2011-01-10; *Notre Dame Journal of Formal Logic* 54(1), DOI 10.1215/00294527-1731371. https://arxiv.org/abs/1101.1947
2. “Exact ordered-tuple orbit profiles of the side-preserving random bipartite reducts,” published mathematical result (2026-09-30), https://github.com/published-finding corpus/2026/tree/main/2026/9/30/SCOPE-exact-ordered-tuple-orbit-profiles-of-the-side-preserving-random--f8b9342567cf
