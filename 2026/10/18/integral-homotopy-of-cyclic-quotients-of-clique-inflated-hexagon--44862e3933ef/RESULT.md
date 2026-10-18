# Integral homotopy of cyclic quotients of clique-inflated hexagon independence complexes

## Finding
Let \(q\ge1\) be an integer and let \(G_q=C_6[K_q]\) be the lexicographic product: its vertices are \((i,a)\) with \(i\in\mathbb Z/6\mathbb Z\) and \(a\in\{1,\ldots,q\}\), and distinct vertices are adjacent if they have the same first coordinate or cyclically adjacent first coordinates. Let \(X_q=|\operatorname{Ind}(G_q)|\). The rotation \(r(i,a)=(i+1,a)\) induces a geometric action of the cyclic group \(C_6\). Then **as integral homotopy types of geometric orbit spaces**, for every \(q\ge1\),

\[
X_q/C_6\simeq
\bigvee^{q(q-1)/2}S^1\ \vee\
\bigvee^{((q-1)^3+2(q-1))/3}S^2.
\]

Empty wedges mean a point. Thus all reduced integral homology of this quotient is torsion-free, and its fundamental group is free of rank \(q(q-1)/2\). The claim is an orbit-space homotopy equivalence, not merely an assertion about rational invariants of ambient homology representations.

## Assumptions and scope
Independence complexes include all subsets with no adjacent pair. The quotient is taken **after geometric realization** (equivalently after subdividing to avoid simplex inversions). The rotation acts on cyclic positions and fixes each palette label. The statement concerns this uniform clique inflation of the six-cycle; it makes no assertion about longer cycles, dihedral quotients, or arbitrary clique sizes.

## Proof
Write \(A\) for the subcomplex on positions \(0,2,4\) and \(B\) for the subcomplex on \(1,3,5\). Each is the join of three discrete \(q\)-point sets. Every independent set of the hexagon of cardinality at least three uses just one of these two parity triples. Every independent pair not contained in either parity triple consists of two antipodal positions \(\{i,i+3\}\). Therefore the entire complex is \(A\sqcup B\) together with \(3q^2\) *bridge edges* joining the two disjoint components. (Edges internal to either parity triple already belong to \(A\) or \(B\).)

The subgroup \(\langle r^2\rangle\cong C_3\) preserves each component, and \(r\) swaps them. Hence the quotient of \(A\sqcup B\) by \(C_6\) is \(Y_q=A/C_3\). The action cyclically permutes the three factors of \(A\). A cellular description of \(Y_q\) has exactly \(q\) zero-cells indexed by palette labels, \(q^2\) one-cells \(e_{ab}\) directed from label \(a\) to label \(b\), and \((q^3+2q)/3\) two-cells indexed by cyclic orbits of ordered triples \((a,b,c)\). The count of two-cells is Burnside's count for the cyclic permutation of three entries. For nonconstant triples the attaching word is \(e_{ab}e_{bc}e_{ca}\); for constant triples \((a,a,a)\), whose triangular face has a threefold stabilizer, the attaching word is the **single** loop \(e_{aa}\), not its third power. This description is the geometric quotient cell structure, not naive identification of abstract simplex labels.

These cells give \(\pi_1(Y_q)=1\). Indeed, constant triangles kill every \(e_{aa}\); triangles \((a,a,b)\) then give \(e_{ba}=e_{ab}^{-1}\); and triangles \((1,a,b)\) express all \(e_{ab}\) via edges \(e_{1a}\) of a spanning tree. Upon collapsing that tree all remaining generators vanish. The calculation also applies at \(q=1\).

The complex \(Y_q\) is a connected two-dimensional CW complex, with Euler characteristic
\[
\chi(Y_q)=q-q^2+(q^3+2q)/3.
\]
Thus its second integral homology is free of rank
\[
\chi(Y_q)-1=((q-1)^3+2(q-1))/3.
\]
A connected, simply connected two-dimensional CW complex is homotopy equivalent to a wedge of as many two-spheres as the rank of its second homology: to see this, choose homology-generating maps \(S^2\to Y_q\) by Hurewicz, wedge them, and apply Whitehead's theorem to the resulting simply connected CW complexes, since it is a homology equivalence.

For bridge edges, the half-turn \(r^3\) interchanges the edge between antipodal positions labeled \((a,b)\) with the edge labeled \((b,a)\). If \(a\ne b\), these six edges form a rotation orbit whose quotient is an ordinary edge joining the two palette vertices \(a,b\) of \(Y_q\). There is one such orbit for each unordered two-element palette subset, giving \(\binom q2\) extra edges. If \(a=b\), the orbit has three edges; the half-turn fixes the midpoint and reverses each edge, so its quotient is a free-ended interval (a contractible leaf) attached at palette vertex \(a\). There are \(q\) such leaves. Attaching the \(\binom q2\) remaining edges to the connected \(Y_q\) produces precisely \(\binom q2\) new wedge circles, while the leaves can be collapsed. Combining this with the homotopy description of \(Y_q\) proves the theorem.

## Verification
The standalone file `verify.py` reconstructs the original simplicial faces, forms all chains of nonempty faces (the barycentric subdivision), takes actual geometric-orbit cells under the six rotations, and computes their cellular boundaries. It checks the product of the two explicit boundary matrices vanishes and agrees with the predicted reduced Betti numbers modulo \(2,3,5,7\) at \(q=1,2,3,4\). For \(q=1,2\), Smith normal forms of both boundary matrices have only unit nonzero entries, independently verifying the absence of integral torsion in those cases. The general theorem rests on the complete CW and fundamental-group argument above, not on these finite checks. Run `python verify.py` with Python 3 and SymPy. The file `verification_output.txt` records its output.

## Relationship to prior work
Björner–Wachs–Welker's poset-fiber and inflation theorems (including their **equivariant rational homology** corollary) cover the nonequivariant homotopy type of an inflated complex and provide the rational homology representations under compatible symmetries. Those prior results are explicitly **not** claimed as new here. In particular, their Corollary 8.5 does not establish the **integral homotopy type of the geometric rotation orbit space**, nor a free fundamental group or the absence of its integral torsion; those conclusions require the stabilizer-aware quotient cells and the above fundamental-group calculation. Their equivariant homotopy theorem has additional fixed-point connectivity hypotheses and does not directly give the quotient decomposition here. Okura studies independence complexes of lexicographic products over forests, excluding the cycle base used here. No exact quotient homotopy classification for this family was found in the inspected literature or indexed mathematical-record comparisons.

## Limitations
This is a uniform six-cycle computation; extension to other cycle lengths, reflections, or unequal palette sizes is not proved. The literature search cannot rule out an unindexed equivalent argument. The proof gives a homotopy equivalence, not a canonical simplicial collapse. Finite-field verification at small palette sizes is corroborative and is not an exhaustive test of the infinite family. There is no independent mathematical audit.

## References
1. A. Björner, M. Wachs and V. Welker, *Poset fiber theorems*, Transactions of the American Mathematical Society 357 (2005), 1877–1899, especially Corollary 8.5 and Theorem 7.1. DOI: 10.1090/S0002-9947-04-03496-8. Publisher DOI: https://doi.org/10.1090/S0002-9947-04-03496-8.
2. K. Okura, *Independence Complex of the Lexicographic Product of a Forest*, first posted 2021-09-09, arXiv:2109.04181, https://arxiv.org/abs/2109.04181.
3. K. Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984 (2023), https://arxiv.org/abs/2303.11984.
