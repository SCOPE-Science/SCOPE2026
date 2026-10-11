# Equivariant top homology of triangular-book Morse complexes

## Finding
For each integer \(k\ge2\), the *triangular book* is the graph \(B_k=K_2\vee\overline{K_k}\) with adjacent hubs \(a,b\) and \(k\) other vertices, each adjacent to both hubs and to no other page vertex. Let \(X_k=\mathcal M(B_k)\) be its ordinary discrete Morse complex. Its full automorphism group \(C_2\times S_k\) acts naturally on \(X_k\). The following formulas determine the **entire rational character** of this action on reduced homology.

If \(\sigma\in S_k\) has \(f\) fixed points, \(t\) two-cycles, and \(e\) cycles of even length, and \(s\) denotes interchanging the two hubs, then the only nonzero reduced homology is free abelian in degree \(k\), with rank \((k+1)^2\), and its character \(\chi_k\) satisfies
\[
\boxed{\chi_k(1,\sigma)=\operatorname{sgn}(\sigma)(f+1)^2,\qquad
\chi_k(s,\sigma)=(-1)^{k+1+e}(1-f+2t).}
\]
In particular, as a rational \(S_k\)-module, the restriction is
\[
\widetilde H_k(X_k;\mathbb Q)\big|_{S_k}
\cong\operatorname{sgn}_{S_k}\otimes
\bigl(\mathbf1\oplus\mathbb Q[\{1,\ldots,k\}]\bigr)^{\otimes2}.
\]
The complete group character, not the already-known shellability mechanism or merely the rank, is the new calculation.

## Assumptions and scope
The Morse complex of a graph has a vertex for each matched incidence \((v,\{v,w\})\). Identify it with the directed arrow \(v\to w\). A set of arrows is a simplex exactly when every graph vertex has at most one outgoing arrow and no directed cycle occurs; the empty set is allowed. With arrows reversed, this is the usual directed-forest complex, which is pure shellable for any bidirected connected graph possessing a complete source (Kozlov's complete-source theorem, as reproduced and used by Jojić). Both hubs of \(B_k\) are universal, so \(X_k\) is pure shellable of dimension \(k\), with integral reduced homology only in degree \(k\), without torsion. We do not claim an equivariant wedge decomposition or an integral decomposition into named permutation modules.

## Proof
**1. A signed fixed-forest formula.** For \(g\in C_2\times S_k\), let \(\mathcal F_g\) comprise the \(g\)-invariant allowable oriented forests, including the empty forest. For a forest \(F\), the group element permutes its constituent arrows, with permutation sign \(\operatorname{sgn}(g|_F)\). Put
\[
Z(g)=\sum_{F\in\mathcal F_g}(-1)^{|F|}\operatorname{sgn}(g|_F).
\]
The trace of \(g\) on a simplicial chain group is the signed count of invariant oriented simplices. Subtracting the unreduced degree-zero contribution gives the reduced Hopf trace identity; since reduced homology is concentrated in degree \(k\),
\[
\chi_k(g)=(-1)^{k+1}Z(g). \tag{1}
\]
All signs below include the sign of the permutation of arrows, not merely parity of the size of a forest.

**2. The hubs fixed separately.** Fix \(\sigma\in S_k\), and let \(r\) be its number of nontrivial page cycles. In an invariant forest, a hub can point to a page only when that page is fixed by \(\sigma\). For every nontrivial page cycle of length \(\ell\), its pages therefore have precisely three invariant local states: all roots, all pointing to \(a\), or all pointing to \(b\). Either nonroot state contributes \((-1)^\ell\) from its arrows times \((-1)^{\ell-1}\) from their cyclic permutation, hence \(-1\). The sum of these three states is \(-1\), independent of \(\ell\), and they cannot create a directed cycle with the rest of the forest.

After factoring out these \(r\) cycles, the remaining graph is \(B_f\), permitting \(f=0\) and thus \(B_0=K_2\). The signed enumeration of rooted forests is \(\det(I-L_{B_f})\), by the matrix-forest identity. For \(f\ge1\), the Laplacian has eigenvalues \(0\), \(f+2\) twice, and \(2\) with multiplicity \(f-1\); for \(f=0\), the eigenvalues are \(0,2\). Consequently, uniformly for \(f\ge0\),
\[
Z(1,\sigma)=(-1)^r\det(I-L_{B_f})
=(-1)^{r+f-1}(f+1)^2. \tag{2}
\]
Since \(\operatorname{sgn}(\sigma)=(-1)^{k-f-r}\), substituting (2) into (1) gives \(\chi_k(1,\sigma)=\operatorname{sgn}(\sigma)(f+1)^2\).

**3. The hubs interchanged.** Write \(g=(s,\sigma)\). Invariance forces the two hub arrows to be simultaneously absent or simultaneously present. An invariant pair of opposite hub-to-hub arrows is forbidden because it forms a directed two-cycle.

If both hub arrows are absent, every odd page cycle must consist of roots. Every even page cycle permits exactly three states: all roots, or either of the two alternating choices of arrows towards the two hubs. Each alternating state is a single even arrow orbit and has signed weight \(-1\). Thus an even cycle has local sum \(-1\), and all such cycles give
\[
Z_{\mathrm{hub\ roots}}=(-1)^e. \tag{3}
\]
If both hubs have outgoing arrows, their targets are transformed into one another by \(\sigma\), so the targets are either a single fixed page or a pair forming a two-cycle. For each fixed page there is one invariant hub-arrow pair; it forces that page to be a root and contributes \(-1\) from exchanging the two arrows. The remaining page cycles give \((-1)^e\), so the combined contribution is \(-f(-1)^e\).

For each page two-cycle there are **two** choices for the hub-arrow pair. Their two targets must be roots: making either target point back toward a hub creates a directed two- or four-cycle. The selected page two-cycle previously contributed \(-1\) to (3), whereas the hub-arrow pair itself contributes \(-1\); replacing the former by the latter leaves \(+(-1)^e\) for either choice. Thus the two-cycle-target cases contribute \(2t(-1)^e\). No longer page cycle can receive invariant hub arrows, since applying \(g\) twice must fix each hub's unique target. Summing all mutually exclusive cases proves
\[
Z(s,\sigma)=(-1)^e(1-f+2t). \tag{4}
\]
Equation (1) now yields the second character formula.

**4. Representation statement.** The character of the page permutation module \(\mathbb Q[\{1,\ldots,k\}]\) at \(\sigma\) equals its fixed-point count \(f\). Tensoring twice with the extra trivial summands therefore gives character \((f+1)^2\); twisting by sign proves the claimed \(S_k\)-module isomorphism over \(\mathbb Q\). At the identity this has dimension \((k+1)^2\). By shellability this is the integral top Betti number, and all other reduced integral homology groups vanish.

## Verification
The standalone standard-library script `verify.py` enumerates all incidence-arrow subsets satisfying outdegree and directed-cycle constraints, constructs each automorphism on arrows, computes signed traces of invariant simplices (including the empty one), and checks the stated formulas across all conjugacy classes of \(S_k\) and both hub-swap states for \(2\le k\le6\). It runs 56 distinct conjugacy-class tests. An independent mod-two chain-boundary calculation for \(k=2,3,4\) checks that the only reduced Betti number is \((k+1)^2\) in degree \(k\). Execution reports `CONJUGACY_CHECKS= 56` and `VERIFY_OK`. The universal proof is the orbit classification and Hopf trace argument above; these computations are finite cross-checks, not an extrapolation.

## Relationship to prior work
Donovan and Scoville (2022), the date- and classification-eligible source motivating this direction, compute Morse-complex homotopy types for paths and extended star graphs and matching-complex types for Dutch windmills. Their Dutch windmill has cycles sharing a **vertex**, and their matching complex is not the graph's ordinary Morse complex; no triangular-book automorphism character follows. Jojić (2012) states Kozlov's complete-source shellability theorem, which does cover the triangular-book *homological concentration* but does not determine the hub-swap character or page-permutation action. Bernardi and Klivans give the signed matrix-forest ingredient. The publicly available exact calculation of \(\mathcal M(K_{2,n})\) concerns a **different graph** without the common hub edge and computes its nonequivariant homotopy type; the published \(K_{3,3}\) and other small graph Morse-complex calculations likewise do not imply these two general character formulas. Kook's equivariant results concern cycle-matroid independence complexes, not the incidence-arrow Morse complex.

## Limitations
The theorem gives the character over \(\mathbb Q\), not an integral isomorphism type of the full \(\mathbb Z[C_2\times S_k]\)-module or an equivariant homotopy classification. Existing shellability is used as a cited premise, not claimed as a new result. The exhaustive checks stop at six pages, whereas the combinatorial argument is uniform for all \(k\ge2\). An unindexed equivalent equivariant computation may exist.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first public 2022-07-27; primary MSC 57Q70. https://arxiv.org/html/2207.13780v1
2. D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v2 (2012), especially Sections 1 and 2 and the complete-source shellability theorem. https://arxiv.org/html/1109.4475v2
3. O. Bernardi and C. J. Klivans, *Directed rooted forests in higher dimension* (2016), for matrix-forest identities and forest enumeration.
4. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122.
5. Exact published comparison, *The Morse complex of \(K_{2,n}\) is a wedge of \(n^2-1\) \(n\)-spheres*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-morse-complex-of-k-2-n-is-a-wedge-of-n-2-1-n-spheres--6e0567ab1610
6. W. Kook, *The homology of the cycle matroid of a coned graph* (2007), an equivariant result for a different simplicial complex.
