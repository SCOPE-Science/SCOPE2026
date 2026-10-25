# Exact integral homotopy types of matching complexes of fan graphs

## Finding
For every integer \(n\ge3\), let \(F_n=K_1\vee P_n\) be the fan graph with a central hub adjacent to all vertices of an \(n\)-vertex path. Its **ordinary matching complex** (the simplicial complex of all pairwise vertex-disjoint edge sets) satisfies
\[
\mathcal M(F_n)\simeq
\begin{cases}
\bigvee^{q+1}S^{q-1},&n=3q,\\[2pt]
\bigvee^{q}S^{q},&n=3q+1,\\[2pt]
\bigvee^{2q+2}S^{q},&n=3q+2,
\end{cases}
\qquad q\ge1.
\]
This determines the entire **integral homotopy type** and every integral reduced homology group. There are no unspecified summands, torsion groups, or higher-dimensional attaching maps. In the first case \(q=1\), the wedge of two zero-spheres is a space of three discrete points.

## Assumptions and scope
Label the central vertex \(h\) and the path vertices \(v_1,\ldots,v_n\). The graph has spokes \(s_i=hv_i\) for \(1\le i\le n\) and rim edges \(e_j=v_jv_{j+1}\) for \(1\le j<n\). It is a finite simple maximal outerplanar graph for \(n\ge2\). The complex \(\mathcal M(F_n)\) is *not* the perfect matching complex or a higher matching complex. Join and suspension below refer to the standard topological realizations of finite simplicial complexes. We use the augmented empty-edge complex \(\{\emptyset\}\) as the neutral element for simplicial joins and as a formal \(S^{-1}\); for ordinary geometric realization, the special case \(n=3\) is handled explicitly.

## Proof
**1. The path lemma.** Write \(I_m=\operatorname{Ind}(P_m)\), with \(I_0=\{\emptyset\}\). For \(m\ge4\), delete the penultimate vertex of the \(m\)-vertex path. Its deletion leaves a graph with an isolated last vertex, so the deletion complex is contractible. Its link is \(I_{m-3}\). The deletion/link cofibration therefore yields \(I_m\simeq\Sigma I_{m-3}\). The initial cases are \(I_1\simeq\mathrm{pt}\), \(I_2\simeq S^0\), and \(I_3\simeq S^0\). Thus, for nonnegative \(m\),
\[
 I_{3a}\simeq S^{a-1}\ (a\ge1),\qquad
 I_{3a+1}\simeq\mathrm{pt},\qquad
 I_{3a+2}\simeq S^a.
\]
The formal convention \(I_0=S^{-1}\) is used only to simplify joins. This proves the path lemma rather than presupposing a table of computations.

**2. The hub-cone decomposition.** Let \(A\subseteq\mathcal M(F_n)\) consist of matchings using only rim edges. These are the independent sets in a path on \(n-1\) vertices, so \(A\cong I_{n-1}\). Distinct spokes cannot both appear in a matching. The faces containing a fixed spoke \(s_i\) are exactly the cone \(s_i*B_i\), where
\[
 B_i\cong I_{\max(i-2,0)}*I_{\max(n-i-1,0)}.
\]
Indeed the available rim edges are precisely those strictly to the left of \(e_{i-1}\) and to the right of \(e_i\). When a side contributes no rim edges, its complex is \(I_0=\{\emptyset\}\), the join unit. Hence
\[
 \mathcal M(F_n)=A\cup\bigcup_{i=1}^n(s_i*B_i),
\]
where each cone meets \(A\) precisely in \(B_i\), and distinct cones meet only in \(A\). This is an exact simplicial equality for every \(n\ge3\).

**3. Classify the attaching links.** For \(n=3q\) with \(q\ge2\), \(A\simeq S^{q-1}\), and \(B_i\) is noncontractible precisely when \(i\equiv2\pmod3\). There are \(q\) such indices and each \(B_i\simeq S^{q-2}\). All other links are contractible. Every map \(B_i\to A\) is null-homotopic: for \(q\ge3\), spheres of dimension \(q-1\) are \((q-2)\)-connected, and for \(q=2\) each map from \(S^0\) to connected \(S^1\) is null. Attaching the cones successively therefore wedges \(q\) copies of \(\Sigma S^{q-2}\) onto \(A\), giving \(\bigvee^{q+1}S^{q-1}\).

For \(n=3\), \(A\cong S^0\); the cone on \(B_2=I_0*I_0\) introduces one isolated vertex, and the two other spoke cones attach over contractible nonempty links. The resulting complex has exactly three contractible components and is homotopy equivalent to \(\bigvee^2S^0\).

For \(n=3q+2\), \(A\cong I_{3q+1}\) is contractible. Exactly the \(2q+2\) indices \(i\equiv1,2\pmod3\) give noncontractible links, all homotopy equivalent to \(S^{q-1}\). Every map of a link into \(A\) is null-homotopic. Coning the links yields \(\bigvee^{2q+2}S^q\).

For \(n=3q+1\), \(A\simeq I_{3q}\simeq S^{q-1}\), and the noncontractible links occur exactly at \(i\equiv1\pmod3\), in number \(q+1\), each homotopy equivalent to \(S^{q-1}\). In particular \(B_1\cong I_{3q-1}\), included in \(A\cong I_{3q}\) as the deletion of an endpoint of the path. The associated endpoint link is \(I_{3q-2}\), which is contractible because \(3q-2\equiv1\pmod3\). Consequently the inclusion \(B_1\hookrightarrow A\) is a homotopy equivalence. Attaching the cone \(s_1*B_1\) therefore makes the base contractible. Each of the remaining \(q\) noncontractible links then contributes one \(\Sigma S^{q-1}\simeq S^q\); all other links are contractible. Hence \(\mathcal M(F_n)\simeq\bigvee^q S^q\).

At every step, the cone-attachment splitting follows from the homotopy pushout of a cofibration along a null map. In particular, the argument establishes the homotopy equivalences, not just equality of Euler characteristics or field homology.

## Verification
The standalone file `fan_complex_verify.py` creates every matching of each fan graph with \(3\le n\le15\) by disjoint-vertex edge selection, constructs every simplicial boundary matrix, and computes its exact rank over \(\mathbb F_2\). The program checks the full reduced Betti vector against the three cases above, for all 13 orders. The largest order has 7,852 faces including the augmented empty face; the logged count for \(n=3\) is eight faces including the empty face. The exact program output is in `fan_verification_output.txt`. These finite computations independently check signs of multiplicity and dimensional indexing but are not used as the proof for arbitrarily large \(n\).

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *Matching Complexes of Outerplanar Graphs* (first submitted November 7, 2024), Theorem 2, establish that every outerplanar graph has a matching complex homotopy equivalent to a wedge of spheres or to a contractible space. Since each fan is outerplanar, that theorem covers **wedge existence** but not the exact sphere dimensions, multiplicities or residue-class formulas proved here. The proof above specifies those parameters directly. In their earlier *General polygonal line tilings and their matching complexes*, the authors give sphere formulas for triangular line tilings. Those graphs are different: in a fan, every consecutive triangular face uses the same hub, whereas the referenced triangular line tiling has a different graph structure and facet-incidence pattern. Research on matching polynomials of fan graphs gives numbers of matchings but does not by itself determine their integral homotopy type. The stated periodic classification was not found in the primary or mathematical-record material examined; see `REVIEW.md` for the comparison and uncertainties.

## Limitations
The theorem applies to \(F_n=K_1\vee P_n\) only, with \(n\ge3\); it does not assert a general formula for all outerplanar graphs, fan triangulations with deleted spokes, wheels, or higher matching complexes. The finite verifier computes mod-two homology, whereas the **integral homotopy conclusion** depends on the preceding all-parameter cofibration argument. Completeness of bibliographic searches cannot be guaranteed; an unindexed earlier formula remains a residual originality risk.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, originally submitted 2024-11-07, Theorem 2. https://arxiv.org/abs/2411.04601
2. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, originally submitted 2022-11-22, Section 4 and Appendix A. https://arxiv.org/abs/2211.12559
3. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* 17 (2025), 133, section on fan matching polynomials, https://doi.org/10.3390/sym17010133
