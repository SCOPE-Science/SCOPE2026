# Block-transitive fixed loci of the rooted-forest skeleton of strong Morse simplices

## Finding
Let \(N\ge2\), let \(\mathcal F_N\) be the simplicial complex whose vertices are ordered pairs \((u,v)\) of distinct elements of \([N]\), and whose faces are the sets of directed edges \(u\to v\) forming rooted directed forests (at most one incoming edge at any vertex, and no directed cycle). Under the explicit correspondence \(u\to v\leftrightarrow(v,\{u,v\})\), this is the canonical vertex-edge-pair subcomplex of the strong discrete Morse matching complex \(\mathcal{SM}(\Delta^{N-1})\), not an assertion about the fixed points of the entire latter complex.

Partition \([N]=F\sqcup B_1\sqcup\cdots\sqcup B_t\), where \(t\ge1\), \(|F|=f\ge0\), and all \(|B_i|\ge2\). Let \(G=H_1\times\cdots\times H_t\) act on labels, with each \(H_i\le \mathfrak S(B_i)\) transitive and acting trivially outside \(B_i\); all of \(F\) is fixed. Write \(D_f\) for the discrete simplicial complex on \(f\) vertices. For \(f\ge2\), the **actual geometric fixed space** has a canonical piecewise-linear homeomorphism
\[
 |\mathcal F_N|^G \cong_{\mathrm{PL}}
 \left|\mathcal F_f*D_f^{*t}\right|.
\]
The same orbit description also gives these boundary cases: when \(f=0\), the geometric fixed space is empty; when \(f=1\), it is a simplex of dimension \(t-1\).

Consequently, for \(f\ge2\),
\[
 |\mathcal F_N|^G\simeq
 \bigvee^{(f-1)^{f-1+t}} S^{f+t-2},
\qquad
 \widetilde H_j(|\mathcal F_N|^G;\mathbb Z)\cong
 \begin{cases}
 \mathbb Z^{(f-1)^{f-1+t}},&j=f+t-2,\\
 0,&j\ne f+t-2.
 \end{cases}
\]
In particular the fixed homotopy type depends on the number \(t\) of nontrivial independently transitive blocks and the number \(f\) of singleton labels, **not** on the sizes of those blocks or the choices of transitive groups. For example, two such blocks and two singleton labels always give a two-sphere, regardless of block sizes.

## Assumptions and scope
The simplicial complex \(\mathcal F_N\) is the complete-directed-graph rooted-forest complex: an arrow is directed from parent to child. Each component of a face is a tree directed away from its root. The action of \(G\) permutes labels and thus directed-edge vertices. The fixed space means pointwise fixed elements of the *geometric realization*, not a subcomplex comprised only of vertexwise fixed directed edges. The group acts independently and transitively on its distinct nontrivial blocks; the claim is not made for a diagonally coupled action on those blocks. The result concerns \(\mathcal F_N\), identified in Knudson–Owens-White as the vertex-edge-pair skeleton \(X_{N-1}\subseteq\mathcal{SM}(\Delta^{N-1})\); it does **not** claim a homotopy equivalence on fixed spaces for the inclusion in the full strong Morse complex.

## Proof
**Step 1 (the only admissible arrow orbits).** Every directed edge has a \(G\)-orbit. Arrows between two singleton vertices \(u,v\in F\), \(u\ne v\), each form a singleton orbit. For a singleton \(u\in F\) and a block \(B_i\), transitivity supplies the orbit \(\{u\to b:b\in B_i\}\), which is a directed forest (a star with source \(u\)). Conversely, the orbit \(\{b\to u:b\in B_i\}\) has at least two arrows incoming to \(u\), hence cannot belong to a forest.

For distinct nontrivial blocks \(B_i,B_j\), independence and transitivity imply the orbit of \(b\to c\), where \(b\in B_i\), \(c\in B_j\), is all \(B_i\times B_j\) in that direction. Each target then has at least two incoming arrows. Finally, for any arrow whose endpoints both lie in \(B_i\), its \(H_i\)-orbit has positive and constant indegree at every vertex of \(B_i\), by transitivity. A finite directed graph with positive indegree at every vertex contains a directed cycle. Such an orbit cannot occur in a directed forest. These exhaust the possibilities.

**Step 2 (compatibility).** A family of singleton orbits on \(F\) is admissible precisely when it forms a directed forest on \(F\). For a fixed \(i\), two distinct allowed star orbits \(\{u\to b:b\in B_i\}\) and \(\{v\to b:b\in B_i\}\) cannot coexist: each child in \(B_i\) would have two incoming arrows. At most one such star orbit is chosen for each block. Conversely, any directed forest on \(F\), together with independently either zero or one star orbit for every block, is a directed forest on all of \([N]\): the arrows into nontrivial blocks end at terminal leaves, and cannot create cycles or compete for other incoming arrows. Thus admissible orbit collections form the simplicial join \(\mathcal F_f*D_f^{*t}\). This assertion is valid at \(f=0,1\) with the usual abstract empty-face conventions.

**Step 3 (actual fixed points).** For any finite simplicial complex with a simplicial finite-group action, a point in the interior of a simplex is fixed precisely when its barycentric coordinates are constant on every orbit of the vertices occurring in its support. Such support must be a union of full vertex orbits. In every invariant simplex, the fixed affine slice is the simplex on the barycenters of its constituent orbits. These slices glue face-to-face and define the canonical orbit-barycenter triangulation of the actual geometric fixed space. Applying Step 2 gives the displayed PL homeomorphism. In particular no single vertex orbit is admissible when \(f=0\); for \(f=1\), exactly one star-orbit vertex per block is available, with every combination admissible, giving a \((t-1)\)-simplex.

**Step 4 (homotopy and integral homology).** The classical complete-digraph directed-forest theorem gives \(|\mathcal F_f|\simeq\bigvee^{(f-1)^{f-1}}S^{f-2}\) for \(f\ge2\) (Kozlov; also Theorem 9.2 of Knudson–Owens-White). The complex \(D_f\) has the homotopy type of a wedge of \(f-1\) zero-spheres, with free reduced integral homology of that rank in degree zero. The simplicial join realizes the topological join, and the reduced join Künneth formula, or the homotopy identification \(X*Y\simeq\Sigma(X\wedge Y)\) for appropriately based CW complexes, gives a wedge of \((f-1)^{f-1}(f-1)^t=(f-1)^{f-1+t}\) spheres in degree \((f-2)+t\). There is no torsion, and other reduced integral homology groups vanish. This completes the proof for every parameter in the stated domain.

## Verification
The standalone `verify_block_fixed_forests.py` reconstructs directed-arrow orbits under cyclic and full symmetric actions on independently permuted blocks of sizes two, three and four. It enumerates 490 edge orbits and exhaustively compares the actual forest condition with the join criterion on 142,870 orbit subsets in 46 finite test cases. Output: `PASS: 490 edge orbits classified; 142870 orbit-subsets checked exhaustively over 46 finite cases (cyclic and symmetric block actions).` These are finite cross-checks only; Steps 1–4 and the cited complete-digraph theorem provide the general proof. Run with Python 3 using `python verify_block_fixed_forests.py` in the directory containing this file.

## Relationship to prior work
Knudson and Owens-White (2026), especially Section 9 and Theorem 9.3, identify the vertex-edge-pair subcomplex of \(\mathcal{SM}(\Delta^{N-1})\) with the rooted directed-forest complex \(\mathcal F_N\), prove a nonequivariant collapse, and state its ordinary sphere-wedge homotopy type (Theorem 9.2, citing Kozlov). Kozlov's earlier work establishes the ordinary directed-tree complex framework. Engström (2005) studies related directed-forest topology. The new statement here is the complete actual geometric fixed-locus classification for every independently block-transitive label group, including a uniform PL join model, two boundary regimes, and the integral sphere multiplicity. Neither the underlying nonequivariant sphere count nor a character/Euler formula alone determines these fixed-space homotopy types. No claim is made that the nonequivariant collapse from the entire strong Morse complex is equivariant.

## Limitations
The group hypothesis explicitly requires independent transitive actions on disjoint nontrivial blocks. It does not classify arbitrary subgroups, particularly diagonal actions coupling several blocks. It does not determine the fixed loci of the **full** strong discrete Morse matching complex, only those of its canonical rooted-forest subcomplex. This self-review mathematical analysis is not independently validated. A possible unindexed equivalent fixed-space result remains an originality risk; the full 1999 publisher text was not accessible during source review.

## References
1. K. P. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first posted 2026-09-06), Sections 4 and 9, Theorems 9.2–9.3. https://arxiv.org/pdf/2609.06844
2. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122. (Source identified through reference 9 of Knudson–Owens-White; complete publisher text was not retrieved.)
3. A. Engström, *Complexes of directed trees and independence complexes*, arXiv:math/0508148v1 (2005), Section 2. https://arxiv.org/pdf/math/0508148
