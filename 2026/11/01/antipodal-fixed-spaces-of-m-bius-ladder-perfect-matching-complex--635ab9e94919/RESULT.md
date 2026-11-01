# Antipodal fixed spaces of Möbius-ladder perfect-matching complexes

## Finding

For every integer \(n\ge2\), let \(M_{2n}\) be the graph on \(\mathbb Z/(2n)\) with consecutive rim edges and antipodal spoke edges. Let \(X_n=\mathcal M_p(M_{2n})\) denote its **perfect-matching complex**: its vertices are graph edges and its faces are matchings that extend to a perfect matching. Let \(\tau(i)=i+n\) act on graph vertices and hence on the complex.

The *actual geometric fixed-point space* has the following complete homotopy classification:

\[
\boxed{
 |X_n|^{\langle\tau\rangle}\simeq
 \begin{cases}
 \{\mathrm{pt}\},&n\text{ odd},\\
 S^{n/2-1}\vee S^{n/2-1},&n\text{ even}.
 \end{cases}
}
\]

More strongly, it has a canonical piecewise-linear homeomorphism to the independence complex of the explicitly defined graph \(H_n\) below. In particular, for even \(n\), its total mod-two Betti number equals that of the ambient complex; the Smith total-Betti inequality is sharp. For odd \(n\ge3\), the fixed-point space is contractible although the ambient complex is a nontrivial bouquet of spheres.

## Assumptions and scope

All complexes are finite and simplicial; geometric fixed points mean *points* in the geometric realization fixed by the action, rather than a complex formed by pointwise fixed original vertices. Index the antipodal graph-vertex columns by \(i\in\mathbb Z/n\). The spoke \(t_i\) occupies column \(i\). The pair \(r_i\) of antipodal rim edges joining columns \(i\) and \(i+1\) occupies both these columns. For \(n=2\), retain the two **distinct** parallel rim-orbit choices \(r_0,r_1\); the occupancy rule still applies.

Define the incompatibility graph \(H_n\) on the \(2n\) abstract vertices \(\{t_i,r_i:i\in\mathbb Z/n\}\). Distinct vertices are adjacent exactly when their occupied sets of columns intersect. Equivalently, the \(t_i\) are independent, consecutive rim-orbits conflict, and \(r_i\) is adjacent to \(t_i\) and \(t_{i+1}\). The independent sets form \(K_n=\operatorname{Ind}(H_n)\).

## Proof

**1. Orbit simplices model the geometric fixed space.** Every simplicial vertex of \(X_n\) is a graph edge. Under \(\tau\), its orbits are precisely the \(n\) singleton spokes \(t_i\) and the \(n\) pairs of antipodal rim edges \(r_i\). A fixed point in a simplex has equal barycentric coefficients on members of each orbit, and the minimal simplex supporting that point must be \(\tau\)-invariant. Each admissible orbit is therefore represented by its barycenter, and the union of these orbit barycenters forms a canonical triangulation of the geometric fixed set.

An invariant edge collection is a matching if and only if its orbit members occupy disjoint antipodal columns. Conversely, any such disjoint orbit collection extends to a perfect matching by inserting a spoke in every unoccupied column. Hence the admissible orbit sets are *exactly* the independent sets of \(H_n\), and the orbit-barycenter map induces

\[
 |K_n|\cong_{\mathrm{PL}} |X_n|^{\langle\tau\rangle}.
\]

The map is piecewise affine on each independent-set simplex; the inverse sends a point to its total barycentric mass on each orbit. This proves both continuity and the PL assertion.

**2. A contractible star-covered core.** Write \(\operatorname{st}_{K_n}(t_i)\) for the closed simplicial star of the spoke vertex \(t_i\), and set

\[
 B_n=\bigcup_{i\in\mathbb Z/n}\operatorname{st}_{K_n}(t_i).
\]

For every nonempty index set \(J\), the intersection of its closed stars is the closed star of the simplex \(\{t_i:i\in J\}\): a face is extendible by all spokes in \(J\) exactly when it is extendible by their union. This follows because \(K_n\) is a flag complex of independently occupied columns. Since every set of spokes is a face, this intersection is a nonempty cone and therefore contractible. Thus the family is a finite good cover by subcomplexes with full-simplex nerve; the simplicial nerve theorem gives \(B_n\simeq\{\mathrm{pt}\}\).

**3. The only faces outside the core.** A face lies outside \(B_n\) precisely if it contains no spoke and no new spoke can be added. Such a face is a collection of pairwise disjoint rim-orbits that covers every quotient column. In other words, it is a perfect dimer tiling of the cyclic column graph. If \(n\) is odd, no such tiling exists, whence \(K_n=B_n\) and the fixed space is contractible.

If \(n=2q\ge4\) is even, exactly two dimer tilings exist, given by alternating rim orbits. Each gives a \((q-1)\)-simplex \(\Delta_0\) or \(\Delta_1\) in \(K_n\). They have no common vertices; each proper face belongs to \(B_n\), because omitting any selected dimer frees its two columns, permitting a spoke. There are no other faces outside \(B_n\). Therefore \(K_n\) is obtained from the contractible subcomplex \(B_n\) by attaching two \((q-1)\)-simplices along their entire boundaries. Since the attaching maps into the contractible core are nullhomotopic, this is homotopy equivalent to \(S^{q-1}\vee S^{q-1}\). For \(q=2\), the boundaries are two disjoint pairs of vertices and the argument gives two circles. The same cofibration argument works for all \(q\ge2\).

For \(n=2\), \(K_2\) is the edge on the two spoke vertices together with two isolated rim-orbit vertices: it has three components, hence homotopy type \(S^0\vee S^0\). This supplies the small exceptional case without using an attachment theorem for zero-dimensional cells.

**4. Smith sharpness.** Agarwal–Basak [1] show that for even \(n\) the ambient perfect-matching complex itself has homotopy type \(S^{n/2-1}\vee S^{n/2-1}\). The preceding fixed-space theorem gives exactly the same mod-two Betti numbers (including the component count when \(n=2\)). Thus \(\sum_j\dim_{\mathbb F_2}H_j(|X_n|^{\langle\tau\rangle};\mathbb F_2)=\sum_j\dim_{\mathbb F_2}H_j(|X_n|;\mathbb F_2)\) for all even \(n\). This is an equality of Betti totals, not a claim that the inclusion induces isomorphisms in homology.

## Verification

The accompanying standard-library Python 3 program `verify_fixed_space.py` independently enumerates perfect matchings of the **original labeled graph**, all their extendible faces, and the actual antipodal edge-orbits. For every \(2\le n\le8\), it checks face-by-face that invariant extendible sets coincide with the disjoint-occupied-columns model, and then computes reduced mod-two boundary ranks of the fixed orbit complex. The resulting reduced ranks are \(2\) in dimension \(n/2-1\) for even \(n\), and zero for odd \(n\). There are 1,966 admissible orbit faces across the seven parameter values. Run `python3 verify_fixed_space.py`; success prints `VERIFY_OK`. These finite comparisons are consistency checks and do not establish the infinite theorem; the star cover and dimer classification do.

## Relationship to prior work

Agarwal–Basak [1] classify the *nonequivariant* homotopy types of the ambient perfect-matching complexes for all Möbius ladders. The published calculation [2] of the central antipodal half-turn establishes its rational homological character and explicitly identifies invariant edge sets with column monomer–dimer packings. That orbit description is **prior work**, not asserted to be new here. The present additional theorem classifies the *actual geometric fixed space* via a contractible star-covered core and exactly two missing top simplices for even width; neither a Lefschetz number nor an ambient homology character specifies this homotopy type. The stronger odd-case dihedral-character calculation [3] also concerns ambient homology representations, not the fixed-point space or its contraction.

The even-case Smith equality is a consequence of the *new fixed-space homotopy classification* together with the published ambient sphere count; it is not an independent novelty claim based only on matching numerics.

## Limitations

The theorem addresses the antipodal involution on Möbius-ladder perfect-matching complexes, not the whole dihedral family of geometric fixed sets. For the odd case it proves ordinary contractibility, not an equivariant collapse of the ambient complex. It uses the cited nonequivariant homotopy theorem only for the Smith-equality corollary, not for the fixed-space classification. Direct machine checks cover finitely many small instances and cannot replace the general proof. Equivalent unindexed geometric fixed-space work is a residual originality risk. Independent mathematical validation remains unperformed.

## References

1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first version publicly posted August 31, 2026; revised version September 14, 2026. https://arxiv.org/html/2608.30601v2
2. *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*, published research result, October 11, 2026. https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-antipodal-half-turn-representation-on-m-bius-ladder-perfect--317e26dcb314/RESULT.md
3. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*, published research result, October 11, 2026. https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-complete-dihedral-rational-homology-representations-of-odd-m-biu--d5bba5f21863/RESULT.md
