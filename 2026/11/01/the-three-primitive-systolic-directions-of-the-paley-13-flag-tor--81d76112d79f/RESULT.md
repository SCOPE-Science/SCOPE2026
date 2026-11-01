# The three primitive systolic directions of the Paley-13 flag torus

## Finding
Let \(P_{13}\) be the Paley graph with vertex set \(\mathbb Z/13\mathbb Z\) and edges of differences \(\pm1,\pm3,\pm4\), and put \(X=\operatorname{Cl}(P_{13})\). It is the flag cyclic torus \(T_{13,1,3}\). The integral fundamental and first homology groups have the geometric identification
\[
\pi_1(X)\cong H_1(X;\mathbb Z)\cong L=\{(a,b)\in\mathbb Z^2:a+3b\equiv0\pmod{13}\}.
\]
For **every** class \(w=(a,b)\in L\), the smallest number of edges in a closed walk representing that class equals
\[
\ell(w)=\max\{|a|,|b|,|a-b|\}.
\]
The shortest nonzero integral-homology edge loops have length exactly \(4\). There are exactly **39 distinct unoriented simple four-cycle carriers** representing nonzero classes, distributed equally among precisely three primitive unoriented homology classes
\[
\{\pm(3,-1)\},\qquad\{\pm(1,4)\},\qquad\{\pm(4,3)\}.
\]
Each class has exactly \(13\) simple carriers, and the affine graph symmetry group \(\mathbb Z/13\mathbb Z\rtimes C_6\) acts transitively on all \(39\). The minimum vectors in the first two directions, \((3,-1)\) and \((1,4)\), are a basis of \(L\); the third is their sum. In contrast, there are \(39\) **nullhomologous** simple four-cycles.

## Assumptions and scope
All edges have unit combinatorial length. A closed edge walk may repeat vertices; a simple cycle does not, and unoriented carriers are counted modulo cyclic rotation and reversal. The homology class of a closed walk is computed by lifting it to the triangular tessellation and recording its integral displacement. The phrase *complete marked length formula* refers to shortest closed walks for every class, not to a census of every possible carrier for every class. The lattice identification depends on the displayed vertex and step choices. The claim is specific to the 13-vertex complex and makes no assertion that it is the globally smallest flag triangulated torus.

## Proof
**(1) Identification of the torus and its deck lattice.** The six edge differences are exactly the nonzero quadratic residues modulo \(13\). Directly, the graph has \(13\) vertices and \(39\) edges, and its \(26\) triangles are precisely the translates of
\[
\{0,1,4\}\qquad\text{and}\qquad\{0,3,4\}.
\]
Its six-neighbor vertex links are induced six-cycles; it has no four-cliques. Thus its clique complex has precisely these triangles and triangulates a closed surface. More explicitly, start from the standard triangular tessellation on \(\mathbb Z^2\) with edges in the six directions
\[
\pm e_1,\quad\pm e_2,\quad\pm(e_1+e_2),
\]
and triangular faces \(\{z,z+e_1,z+e_1+e_2\}\) and \(\{z,z+e_2,z+e_1+e_2\}\). The labeling map \(\phi(a,b)=a+3b\pmod{13}\) takes these to the two triangle families above. Quotienting the planar tessellation by the index-\(13\) sublattice \(L=\ker\phi\) gives exactly \(X\): the faces and their vertex identifications match, and no quotient face has identified vertices. Because the planar tessellation is contractible, it is the universal cover. The torus is aspherical, with deck group \(L\cong\mathbb Z^2\), which is also its integral first homology.

**(2) Complete marked closed-walk length formula.** For \(w=(a,b)\), each permitted edge displacement changes each of \(a\), \(b\), and \(a-b\) by at most one. Thus any lifted edge path from the origin to \(w\) has at least \(N(w)=\max(|a|,|b|,|a-b|)\) edges. Equality is attained on the triangular lattice: when \(a,b\) have the same sign, take \(\min(|a|,|b|)\) diagonal steps in that sign direction, followed by the remaining axial steps. When \(a,b\) have opposite signs, use \(|a|+|b|\) axial steps in the respective sign directions. Both constructions take exactly \(N(w)\) steps. For \(w\in L\), their projections are closed edge walks in \(X\) of homology class \(w\), proving the formula for all \(w\).

**(3) Exhaustion of minimal homology directions.** If \(N(a,b)\le3\), then \(|a+3b|\le|a|+3|b|\le12<13\); hence \(a+3b\equiv0\pmod{13}\) forces \(a=-3b\), whose least nonzero norm is \(4\). Thus the nonzero minimum is at least \(4\). Under \(N(a,b)\le4\), the bound \(|a+3b|\le16\) confines the integer \(a+3b\) to \(-13,0,13\). Solving these three possibilities together with \(|a|,|b|,|a-b|\le4\) gives exactly the zero vector and
\[
\pm(3,-1),\qquad\pm(1,4),\qquad\pm(4,3).
\]
For clarity, at \(a+3b=0\), the norm constraint permits only \(b=0,\pm1\). At \(a+3b=13\), substituting \(a=13-3b\) forces \(b=3\) or \(4\), giving \((4,3)\) or \((1,4)\); the negative case follows by negation. The vectors \(A=(3,-1)\), \(B=(1,4)\) have determinant \(13\), the covolume of \(L\), so they form an integral basis and are primitive; \(A+B=(4,3)\) is primitive as well.

**(4) Exact carrier count.** For a four-edge lift with displacement \(A\), the coordinate \(a-b\) must increase by four. The only allowed step types attaining the required increase at each step are \(e_1\) and \(-e_2\), with multiset precisely \(\{e_1,e_1,e_1,-e_2\}\). Its cyclic permutations project to translates of the consecutive four-cycle \((i,i+1,i+2,i+3)\). There are exactly \(13\) different unoriented cycles of this type. For displacement \(B\), the coordinate \(b\) must increase at every step and the step multiset is \(\{e_2,e_2,e_2,e_1+e_2\}\); its projections are the \(13\) translates of the cycles \((i,i+3,i+6,i+9)\). For displacement \(A+B\), the coordinate \(a\) must increase at every step, giving \(\{e_1+e_2,e_1+e_2,e_1+e_2,e_1\}\); its projections are the \(13\) translates of \((i,i+4,i+8,i+12)\). The three representative cycles are simple modulo \(13\), and each translation orbit has size \(13\). Part (3) rules out all other nonzero four-edge homology classes. Therefore precisely \(39\) unoriented simple four-cycles carry nonzero homology.

**(5) Symmetry and the zero-class census.** The affine maps \(x\mapsto rx+t\) for \(t\in\mathbb Z/13\mathbb Z\) and \(r\in\{1,3,4,9,10,12\}\) preserve the edge graph. Their multiplier \(r=4\) has the linear lift \(R(a,b)=(a-b,a)\) on the deck lattice (its labels satisfy \(\phi(Rw)\equiv4\phi(w)\pmod{13}\)). This action cyclically permutes the three unoriented minimum vectors, \(A\mapsto A+B\mapsto B\mapsto-A\), while translations permute the \(13\) carriers in each direction. Hence the affine group is transitive on the \(39\) essential cycles. Finally, direct exhaustive enumeration of the finite one-skeleton, reproduced by `verify.py`, yields exactly \(78\) unoriented simple four-cycles in total, of which \(39\) are the essential carriers just classified; the other \(39\) lift with zero displacement and are nullhomologous. This last *total four-cycle census* is finite and verified by the accompanying full enumerator, not inferred from a mere sample.

## Verification
The standalone `verify.py` reconstructs every vertex, edge, clique triangle, link, simple triangle and simple four-cycle; exhausts the \(6^4\) sequences of at most four lifted steps; compares all displacements with the stated lattice types; verifies the single affine orbit; checks the norm formula against a breadth-first enumeration of the plane through distance \(16\); and independently confirms first mod-two Betti number \(2\). The packaged `verification_output.txt` is the output of an actual completed execution. The universal marked-length formula and the homology identification are proved symbolically in parts (1)–(2), not extrapolated from the bounded tests.

## Relationship to prior work
Datta and Upadhyay introduced the degree-regular cyclic torus family \(T_{n,1,k}\), including this parameter; Brehm and Kühnel provide the broader lattice-quotient framework for equivelar triangular torus maps. Hence neither the torus identification nor the triangular-lattice technique is new. Previously published work gives an exact arithmetic flag criterion and identifies \(T_{13,1,3}\) as the first flag member of this cyclic family. Another previously published result proves that the distinct tail \(T_{n,1,3}\) for \(n\ge17\) has precisely one primitive direction of shortest four-cycles and a different successive length scale. It does not cover \(n=13\), where three primitive shortest directions coexist; that distinction and the complete \(39\)-cycle shell are the new target.

General marked-spectrum algorithms for graphs on a torus establish norm structures and computability, but do not give this finite example's exact three-class, 39-carrier classification. No inspected source states a stronger result entailing the entire present theorem. Earlier classification and algorithmic methods are acknowledged, and equivalent older specialized terminology remains a novelty risk.

## Limitations
The integral marked length formula concerns edge **walks**; a shortest representative of a nonprimitive class need not be a simple edge cycle. Exact classification of **all** carriers is made only for length-four nonzero cycles. The larger affine graph automorphism group is used as a subgroup of the simplicial automorphism group; no assertion about a different ambient graph action is required. The calculation does not extend to all Paley graphs or all equivelar tori. Its finite verification is a reproducible complete census for this 13-vertex graph; the universal statement relies on the symbolic lattice proof. Independent validation has not been performed.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, first publicly submitted 2004-03-25.
2. U. Brehm and W. Kühnel, *Equivelar maps on the torus*, Stuttgart Mathematical Preprint 2006/013.
3. C. Bibby, A. Odesky, M. Wang, S. Wang, Z. Zhang, and H. Zheng, *Minimal flag triangulations of lower-dimensional manifolds*, arXiv:1909.03303.
4. V. Delecroix, M. Ebbens, F. Lazarus, and I. Yakovlev, *Algorithms for Length Spectra of Combinatorial Tori*, SoCG 2023, DOI:10.4230/LIPIcs.SoCG.2023.26.
5. *An exact flag criterion for the cyclic weakly regular torus family*, public research result (2026), identifier a170495e50a8.
6. *A one-direction systolic shell in the cyclic torus family*, public research result (2026), identifier ceddf77f71ea.
