# A binary-power orientation dichotomy for Kneser boundary spheres

## Finding
For every integer \(n\ge2\), let \(X_n\) be the independence complex of the Kneser graph on the \(n\)-subsets of \([2n]\), where disjoint subsets are adjacent. Write
\[
N_n=\frac12\binom{2n}{n},\qquad b_n=\binom{2n-2}{n-1},\qquad G_n=S_{2n}.
\]
The sphere \(|X_n|\cong S^{N_n-1}\) has the following full symmetry description.

For any subgroup \(H\le G_n\), let \(\mathcal P_n\) be the set of unordered complement pairs \(\{A,A^c\}\) of \(n\)-subsets. An \(H\)-orbit of these pairs is *untwisted* if the stabilizer of a representative pair fixes each member individually, rather than exchanging the two. Let \(d(H)\) count the untwisted orbits. Then
\[
|X_n|^H\cong_{\mathrm{PL}}
\begin{cases}S^{d(H)-1},&d(H)>0,\\ \varnothing,&d(H)=0.\end{cases}
\]
For a transposition \(\tau\in G_n\), \(d(\langle\tau\rangle)=N_n-b_n/2\), hence \(|X_n|^{\langle\tau\rangle}\cong_{\mathrm{PL}}S^{N_n-b_n/2-1}\); the fixed space of the full \(G_n\) is empty.

The integral top-dimensional representation is completely determined:
\[
\widetilde H_{N_n-1}(X_n;\mathbb Z)\cong_{\mathbb Z[G_n]}
\begin{cases}\mathbb Z_{\mathrm{sgn}},& n-1\text{ is a power of }2,\\
\mathbb Z_{\mathrm{triv}},&\text{otherwise}.
\end{cases}
\]
Consequently the full orbit space \(Y_n=|X_n|/G_n\) is simply connected, and
\[
\widetilde H_j(Y_n;\mathbb Q)\cong
\begin{cases}\mathbb Q,&j=N_n-1\text{ and }n-1\text{ is not a power of }2,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the integral orientation action changes at the sparse indices \(n=2,3,5,9,17,\ldots\).

## Assumptions and scope
We use the standard Kneser notation \(\operatorname{KG}(n,0)\): vertices are \(n\)-element subsets of \([2n]\), edges join disjoint subsets. All homology is reduced unless explicitly stated. The acting group is the entire label-permutation group \(G_n=S_{2n}\), or an arbitrary subgroup \(H\) for the fixed-space formula. The quotient is the geometric topological orbit space, not the naive quotient of abstract faces. We impose \(n\ge2\) so that no label transposition can interchange an \(n\)-set and its complement.

## Proof
**1. An explicit equivariant sphere.** For an \(n\)-subset \(A\subset[2n]\), its only disjoint \(n\)-subset is \(A^c\). Thus the Kneser graph is a perfect matching on \(2N_n\) vertices and its independence complex is the join of \(N_n\) copies of \(S^0\), the boundary of the \(N_n\)-cross-polytope. Select one member \(A_P\) of each complementary pair \(P\in\mathcal P_n\), and identify its two vertices with \(\pm e_P\) in \(V_n=\mathbb R^{\mathcal P_n}\). A label permutation acts on \(V_n\) by a signed permutation matrix: it carries \(e_P\) to \(e_{gP}\) or \(-e_{gP}\) according as \(gA_P\) is the chosen member of \(gP\) or its complement. The geometric complex is the \(\ell^1\)-unit sphere in \(V_n\), naturally equivariantly homeomorphic to the Euclidean unit sphere.

**2. All subgroup fixed spaces.** A vector \(v\in V_n\) invariant under \(H\) has coordinates determined on each \(H\)-orbit \(\mathcal O\subset\mathcal P_n\) by any one coordinate. The consistency condition on the stabilizer of a pair is exactly that this stabilizer never exchanges its two halves. On an untwisted orbit there is one independent real invariant coordinate; on a twisted orbit the coordinate must vanish. Therefore \(\dim V_n^H=d(H)\). The fixed space is the boundary of the centrally symmetric convex section of the cross-polytope by \(V_n^H\); it is empty for zero-dimensional section and is a PL sphere of dimension \(d(H)-1\) otherwise. For \(H=G_n\), there is one pair orbit and its stabilizer includes a permutation carrying \(A\) onto \(A^c\), so \(d(G_n)=0\).

**3. Counting transposition eigenvalues.** Let \(\tau=(1\ 2)\). An \(n\)-subset fixed by \(\tau\) contains both or neither of \(1,2\). Hence there are
\[
2\binom{2n-2}{n-2}
\]
such fixed subsets and \(F=\binom{2n-2}{n-2}\) fixed unordered complementary pairs. Since \(n\ge2\), \(\tau A\ne A^c\) for every \(A\); thus every fixed pair contributes eigenvalue \(+1\), not \(-1\). The remaining \(N_n-F\) pairs form \(T=(N_n-F)/2\) transposition orbits, each producing a two-coordinate signed-swap block with eigenvalues \(+1\) and \(-1\). The binomial identity
\[
N_n-\binom{2n-2}{n-2}=\binom{2n-2}{n-1}=b_n
\]
therefore gives \(T=b_n/2\). Hence \(\dim V_n^{\langle\tau\rangle}=F+T=N_n-b_n/2\), proving the fixed-sphere dimension. The determinant of the same linear involution is \((-1)^T=(-1)^{b_n/2}\).

**4. Binary arithmetic and integral top homology.** The determinant of a linear automorphism of \(V_n\) is its topological degree on the unit sphere, and hence its action on \(\widetilde H_{N_n-1}(X_n;\mathbb Z)\cong\mathbb Z\). Because all transpositions are conjugate and generate \(S_{2n}\), the integral top action is either trivial or the ordinary permutation sign. It is the latter exactly when \(b_n/2\) is odd. Put \(m=n-1\). Legendre's formula gives \(v_2(m!)=m-s_2(m)\), where \(s_2(m)\) counts the ones in the binary expansion of \(m\). Thus
\[
v_2\!\left(\binom{2m}{m}\right)
=2s_2(m)-s_2(2m)=s_2(m).
\]
Since \(m\ge1\), the binomial coefficient is even, and half of it is odd precisely when \(s_2(m)=1\), or \(m\) is a power of two. This establishes the character dichotomy for every \(n\).

**5. The full quotient.** A finite simplicial group action can be barycentrically subdivided without inversions. Over \(\mathbb Q\), averaging identifies the reduced homology of its geometric quotient with the group-invariant part of the reduced homology of the original complex. The latter is one-dimensional only in degree \(N_n-1\), and is invariant exactly in the trivial-character case, proving the rational quotient classification. Finally, \(N_n\ge3\), so the sphere is simply connected. Every transposition fixes a vertex, for example an \(n\)-subset containing the two transposed labels. Armstrong's orbit-space fundamental-group theorem identifies \(\pi_1(Y_n)\) with \(G_n\) modulo the normal subgroup generated by elements having fixed points. That subgroup contains all transpositions and hence equals \(G_n\); therefore \(\pi_1(Y_n)=1\).

## Verification
The accompanying `verify.py` independently constructs complementary pairs, signed coordinate matrices, their integral determinants, and fixed-coordinate consistency. It checks all \(41,064\) permutations in the symmetric groups on \(4,6,8\) labels; for each it compares the signed determinant with the predicted trivial/sign character. It checks the exact fixed-space dimension of a label transposition for \(2\le n\le8\), and compares the stabilizer consistency rule against the average signed trace for \(70\) cyclic subgroup actions. `verify_output.txt` records `ALL_VERIFY_OK` and the final counters. The unrestricted assertion is proved above; finite checks are independent corroboration.

## Relationship to prior work
Feng and Wang (arXiv:2404.10566, first public April 16, 2024) explicitly identify the zero-excess Kneser independence complex as a cross-polytope boundary, then study cross-polytopal generators when extra ground-set labels are present. Feng (arXiv:2610.17394, first public October 12, 2026) develops a rational homology classification for Kneser graphs on triples and uses the six-label cross-polytope as its initial case. Neither of these inspected analyses determines the integral \(S_{2n}\) orientation character, fixed-point PL spheres for arbitrary subgroups, or the full-orbit-space rational homology dichotomy. The general quotient fundamental-group criterion itself is due to Armstrong, and is used here rather than claimed as new.

## Limitations
The result treats the zero-excess Kneser graph \(\operatorname{KG}(n,0)\), not arbitrary positive excess \(\operatorname{KG}(n,k)\). It does not determine integral torsion or the full homotopy type of \(Y_n\), nor does rational acyclicity mean contractibility. The fixed-space classification uses a subgroup's signed complementary-pair orbits; closed formulas for those orbit counts for every family of subgroups are not asserted. The topological and computational checks are not independent mathematical certification.

## References
1. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394, first public October 12, 2026. https://arxiv.org/abs/2610.17394
2. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first public April 16, 2024. https://arxiv.org/abs/2404.10566
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. **61** (1965), 639–646, DOI: 10.1017/S0305004100038974.
4. Legendre's formula for the \(2\)-adic valuation of factorials; the identity used in Step 4 is derived explicitly there.
