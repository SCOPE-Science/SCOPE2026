# Full Pappus independence-homology symmetry: irreducible dimensions four and six

## Finding
Let \(P\) be the Pappus graph, realized as the incidence graph between the nine points \((x,y)\in\mathbb F_3^2\) and the nine affine lines \((m,b)\) with incidence \(y=mx+b\). Let \(X=\operatorname{Ind}(P)\) be its ordinary vertex independence complex and \(G=\operatorname{Aut}(P)\). Thus \(|G|=216\). The rational reduced homology of \(X\) is zero except in dimension four, and
\[
V=\widetilde H_4(X;\mathbb Q)\cong V_4\oplus V_6
\]
as a \(\mathbb Q[G]\)-module, where **both summands are absolutely irreducible** and have dimensions four and six. In particular, the full group fixes no nonzero rational fourth-homology class.

There is a canonical intrinsic characterization of the two summands. Let \(z\) translate every point \((x,y)\mapsto(x,y+1)\) and every line \((m,b)\mapsto(m,b+1)\). The order-three subgroup \(Z=\langle z\rangle\) is normal in \(G\), and
\[
V_4=V^Z,\qquad V_6=\ker(1+z+z^2:V\longrightarrow V).
\]
The complete degree-four character \(\chi\) has, over the 216 automorphisms, trace multiplicities
\[
\begin{array}{c|rrrrrr}
\operatorname{tr}&-2&-1&0&1&2&10\\\hline
\operatorname{multiplicity}&21&72&54&32&36&1
\end{array}
\]
with \(\chi(z)=\chi(z^2)=1\). The table in the proof specifies the character on each element by its explicit affine/duality permutation together with the character formula. The top rational character has norm squared two, while each displayed constituent has norm squared one.

## Assumptions and scope
All graphs are finite and simple. Label point vertices \(0,\ldots,8\) in lexicographic order of \((x,y)\in\mathbb F_3^2\), and label line vertices \(9,\ldots,17\) in lexicographic order of \((m,b)\in\mathbb F_3^2\). A face of \(X\) is a set of these eighteen vertices containing no incidence edge. Graph automorphisms act on oriented simplicial chains by the sign of the induced permutation of a face's ordered vertices. Homology and representations in the claim are over \(\mathbb Q\); no integral equivariant decomposition is asserted.

## Proof
**The full group.** Any part-preserving automorphism permutes the nine point vertices and preserves their nine collinear triples. Two points have no common incident line precisely when their first coordinates coincide. Hence an automorphism permutes the three vertical point columns. Every permutation of \(\mathbb F_3\) is affine, so the first coordinate transforms as \(x'=ax+b\), with \(a\in\mathbb F_3^\times\). Within each column the second coordinate is initially of the form \(y'=d_x y+e_x\). A triple with first coordinates \(0,1,2\) is collinear exactly when its second coordinates sum to zero. Preservation of every such triple forces all \(d_x\) to equal one nonzero \(d\) and forces \(e_0+e_1+e_2=0\), equivalently \(e_x=cx+e\). Thus the part-preserving automorphisms are exactly
\[
(x,y)\longmapsto(ax+b,cx+dy+e),\qquad a,d\in\{1,2\},\quad b,c,e\in\mathbb F_3,
\]
with induced line transformation
\[
(m,k)\longmapsto\bigl(a^{-1}(c+dm),\ dk+e-a^{-1}(c+dm)b\bigr).
\]
There are \(2\cdot2\cdot3^3=108\) such maps. The involution \(\delta\) interchanges \((x,y)\) on the point side with \((x,-y)\) on the line side; it preserves incidence because \(y=mx+b\) if and only if \(-b=xm-y\). As the graph is connected and bipartite, every automorphism either preserves the sides or exchanges them, and \(\delta\) gives all 108 side-exchanging maps. Hence \(|G|=216\). Moreover, affine maps conjugate \(z\) to \(z^d\), and \(\delta z\delta=z^{-1}\); therefore \(Z=\langle z\rangle\) is normal.

**Rational homology concentration.** Direct exhaustive independent-face enumeration gives exactly \(2598\) faces including the empty face, with nonempty face counts in dimensions zero through eight
\[
(18,126,438,801,756,348,90,18,2).
\]
The boundary ranks over \(\mathbb F_2\) in degrees one through eight are, by exact bit-vector elimination,
\[
(17,109,329,472,274,74,16,2).
\]
Consequently the ordinary mod-two Betti vector is \((1,0,0,0,10,0,0,0,0)\). For an integer boundary matrix, its rank over \(\mathbb Q\) is at least its rank modulo two. Thus rational Betti numbers cannot exceed these mod-two dimensions; in particular no rational homology occurs outside degrees zero and four. The face-vector Euler characteristic is exactly eleven, forcing the fourth rational Betti number to equal ten. This step proves the rational concentration independently of any earlier calculation and does not use modular data to assert an integral torsion statement.

**Equivariant character.** For any \(g\in G\), sum the signed traces on oriented chains, with the augmented empty face contributing \(-1\). The resulting exact reduced Lefschetz sum is
\[
\chi(g)=-1+\sum_{\substack{\varnothing\ne F\in X\\gF=F}}(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
Since all reduced rational homology except \(V\) vanishes, this is exactly the character of \(V\). Enumerating every independent face for each of the 216 explicitly generated automorphisms yields \(\chi(1)=10\), \(\chi(z)=\chi(z^2)=1\), \(\sum_{g\in G}\chi(g)=0\), and
\[
\frac1{216}\sum_{g\in G}\chi(g)^2=2.
\]
The multiplicities in the finding are the complete exhaustive tally, independently checkable from the provided script.

**Canonical irreducible splitting.** Since \(Z\lhd G\), the rational idempotents \(e_+=(1+z+z^2)/3\) and \(e_-=1-e_+\) commute with \(G\). They split \(V\) into two nonzero rational \(G\)-modules of dimensions
\[
\dim e_+V=(10+1+1)/3=4,\qquad \dim e_-V=6.
\]
Their characters satisfy
\[
\chi_4(g)=\frac{\chi(g)+\chi(zg)+\chi(z^2g)}3,\qquad\chi_6(g)=\chi(g)-\chi_4(g).
\]
The two characters are orthogonal because they belong to complementary submodules. Every nonzero complex character has positive integral squared norm. Since \(\langle\chi,\chi\rangle=2\), these two nonzero orthogonal characters must each have squared norm one, proving that \(V_4\) and \(V_6\) are absolutely irreducible. The average character zero shows that the full group has no invariant line.

For reproducibility, the following is the entire distribution of the two characters. Each row gives element order, whether the automorphism preserves or exchanges the bipartition, \(\chi_4\), \(\chi_6\), and number of elements. Together with the formula above and explicit transformations, it determines their values on every element (rows need not be conjugacy classes):

| Order | Sides | \(\chi_4\) | \(\chi_6\) | Count |
|---:|:---|---:|---:|---:|
|1|preserving|4|6|1|
|2|exchanging|0|0|18|
|2|preserving|0|-2|9|
|2|preserving|2|0|18|
|3|preserving|-2|0|12|
|3|preserving|1|0|12|
|3|preserving|4|-3|2|
|4|exchanging|0|2|18|
|6|exchanging|0|0|36|
|6|preserving|-1|0|36|
|6|preserving|0|1|18|
|12|exchanging|0|-1|36|

## Verification
Run `python3 verify_pappus_full_character.py` using the Python standard library. It reconstructs the graph, proves every displayed group map preserves its full 27-edge set, enumerates all 2598 independent faces, computes all mod-two boundary ranks by exact bit-vector elimination, calculates every signed Lefschetz trace, checks \(Z\)-normality, and verifies both irreducible character norms, cross-orthogonality, absence of invariant lines, and the complete 216-element distribution. The calculation makes no floating-point approximations. The affine completeness argument and the representation-theoretic norm argument are supplied above rather than inferred from a finite test on an unbounded family.

## Relationship to prior work
Barmak's triangle-free suspension theorem applies to this graph but does not determine its homology character. Tsukuda's incidence-graph Alexander-duality result concerns ordinary homotopy types; the available abstract does not compute this graph's full symmetry representation. Two earlier exact Pappus independence-complex studies explicitly establish the nonequivariant ten-sphere wedge and the representation restricted to one order-three automorphism, with character \((10,-2,-2)\). Neither determines the full 216-element character, its normal-subgroup splitting, or the absolutely irreducible dimensions four and six. In particular, the present subgroup \(Z\) has character \((10,1,1)\), distinguishing two different conjugacy types of order-three symmetry in the same graph. The prior cyclic module and rank-ten homology do not imply the full-group decomposition.

## Limitations
This is one finite incidence graph and its rational homology; no classification for all incidence graphs, a natural integral \(\mathbb Z[G]\)-lattice, or equivariant wedge decomposition is established. Exhaustive finite computations certify this specific graph only. General literature searches and direct comparison with the most relevant published Pappus claims do not rule out every unpublished or unindexed equivalent character calculation. The Tsukuda journal PDF could not be retrieved during the check, so the specific comparison with that paper rests on its accessible abstract; the closer Pappus studies were read in full.

## References
1. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, submitted **2010-07-02**, Theorems 3.4 and 3.5, https://arxiv.org/html/1007.0418v1 .
2. Shuichi Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), https://doi.org/10.55016/ojs/cdm.v12i1.62277 .
3. *The Pappus graph independence complex is a wedge of ten four-spheres*, public research record `ff7e4637c061`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-pappus-graph-independence-complex-is-a-wedge-of-ten-four-sph--ff7e4637c061 .
4. *Order-three symmetry on Pappus independence homology*, public research record `ea65a5211f31`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31 .
5. *Pappus graph*, MathWorld/Wolfram graph reference, https://mathworld.wolfram.com/PappusGraph.html .
