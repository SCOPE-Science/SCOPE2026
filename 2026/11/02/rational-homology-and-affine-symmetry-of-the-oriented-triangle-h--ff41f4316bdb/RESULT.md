# Rational homology and affine symmetry of the oriented-triangle Hom complex of the Paley tournament of order \(19\)

## Finding
Let \(T\) be the quadratic-residue tournament on \(\mathbb F_{19}\), with \(i\to j\) if and only if \(j-i\) is a nonzero square. For the directed three-cycle \(\overrightarrow C_3\), let
\[
X=\operatorname{Hom}^{\to}(\overrightarrow C_3,T)
\]
be the regular polyhedral complex of directed multihomomorphisms. Its reduced rational homology is zero outside degree two, and
\[
\dim_{\mathbb Q}\widetilde H_2(X;\mathbb Q)=683.
\]
The natural affine tournament automorphisms form the group
\[
G=\mathbb F_{19}\rtimes(\mathbb F_{19}^{\times})^2\cong C_{19}\rtimes C_9,
\qquad |G|=171.
\]
Let \(V_3\) be the rational two-dimensional cyclotomic representation \(\mathbb Q(\zeta_3)\), inflated from \(G/C_{19}\cong C_9\) through \(C_9\twoheadrightarrow C_3\); let \(V_9=\mathbb Q(\zeta_9)\), inflated from \(C_9\); and let \(W_{19}=\ker(\mathbb Q[\mathbb F_{19}]\xrightarrow{\sum}\mathbb Q)\), with its natural affine action. Then the **complete rational representation** is
\[
\boxed{\widetilde H_2(X;\mathbb Q)\cong 5\mathbf1\oplus6V_3\oplus3V_9\oplus36W_{19}.}
\]
In particular the full affine quotient has
\[
\widetilde H_j(|X|/G;\mathbb Q)\cong
\begin{cases}\mathbb Q^5,&j=2,\\0,&j\ne2.\end{cases}
\]
No assertion of an integral wedge-of-spheres homotopy type is made.

## Assumptions and scope
Write
\[
R=\{1,4,5,6,7,9,11,16,17\}\subset\mathbb F_{19}.
\]
The tournament has vertex set \(\mathbb F_{19}\) and arc relation \(i\to j\iff j-i\in R\). A cell of \(X\) is an ordered triple \((A,B,C)\) of **nonempty** subsets of \(\mathbb F_{19}\) such that every edge in \(A\times B\), \(B\times C\), and \(C\times A\) is a tournament arc. It is the product of simplices \(\Delta(A)\times\Delta(B)\times\Delta(C)\) with dimension \(|A|+|B|+|C|-3\). The regular CW structure is obtained by deleting elements from one coordinate at a time; the group \(G\) acts on all coordinates simultaneously. This is a directed Hom complex, not the directed flag complex of transitive subtournaments.

## Proof
**Exhaustive cell description.** Define \(N^+(v)=\{w:v\to w\}\) and \(N^-(v)=\{w:w\to v\}\). For each nonempty \(A\), form
\[
B_A=\bigcap_{a\in A}N^+(a),\qquad
C_{A,B}=\bigcap_{a\in A}N^-(a)\cap\bigcap_{b\in B}N^+(b).
\]
The cells are exactly the triples of nonempty \(A\), \(B\subseteq B_A\), and \(C\subseteq C_{A,B}\). Iterating these finite sets gives the complete cell vector
\[
(f_0,f_1,f_2,f_3,f_4)=(855,5130,9234,4959,684).
\]
There are \(20862\) nonempty cells and Euler characteristic \(684\). Every vertex subset and every subset choice in the displayed description is exhausted by the standalone verifier.

**Boundary ranks and rational concentration.** Orient each product cell by first ordering the vertices of \(A\), then \(B\), then \(C\), each increasingly in \(\{0,\ldots,18\}\). With \(d_A=|A|-1\) and \(d_B=|B|-1\), the cellular boundary obeys
\[
\partial(\Delta A\times\Delta B\times\Delta C)
=(\partial\Delta A)\times\Delta B\times\Delta C
+(-1)^{d_A}\Delta A\times(\partial\Delta B)\times\Delta C
+(-1)^{d_A+d_B}\Delta A\times\Delta B\times(\partial\Delta C).
\]
Direct exact elimination over \(\mathbb F_2\) gives boundary ranks
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_4)
=(854,4276,4275,684),
\]
verified separately by row and column reductions. The complete signed boundary also satisfies \(\partial^2=0\) on every cell. Hence the \(\mathbb F_2\)-Betti vector is \((1,0,683,0,0)\). Universal coefficients imply that every rational Betti number is at most the corresponding \(\mathbb F_2\)-Betti number. In particular all rational Betti numbers outside degrees zero and two vanish; degree-zero rank is one. As the Euler characteristic is \(684\), the remaining rational Betti number is exactly \(683\).

**Complete affine character.** Every \(g_{a,b}(x)=ax+b\), where \(a\in R\) and \(b\in\mathbb F_{19}\), preserves the defining arc relation, yielding \(171\) cellular automorphisms. The trace of \(g\) on the oriented cellular chain group in degree \(d\) is the signed count of its setwise fixed \(d\)-cells, with sign the product of permutation signs in \(A\), \(B\), and \(C\). The exact finite enumeration for every group element gives
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(X;\mathbb Q)\bigr)
=\begin{cases}
683,&a=1,\ b=0,\\
8,&a\in\{7,11\},\\
-1,&\text{otherwise}.
\end{cases}
\]
Indeed, the signed cellular Lefschetz number equals \(1+\operatorname{tr}(g\mid\widetilde H_2)\), because these are the only nonzero rational homology groups.

**Identification of the representation.** The characters of \(\mathbf1\), \(V_3\), \(V_9\), and \(W_{19}\), in the four cases identity, nonidentity translation, dilation of order three, and dilation of order nine, are respectively
\[
\begin{array}{c|rrrr}
&1&V_3&V_9&W_{19}\\\hline
\mathrm{id}&1&2&6&18\\
\mathrm{translation}\ne1&1&2&6&-1\\
\mathrm{order\ }3\ \mathrm{dilation}&1&2&-3&0\\
\mathrm{order\ }9\ \mathrm{dilation}&1&-1&0&0
\end{array}
\]
(the translation and dilation cases allow arbitrary translation terms when \(a\ne1\)). The character of \(5\mathbf1\oplus6V_3\oplus3V_9\oplus36W_{19}\) therefore agrees with the computed homology character on all \(171\) elements. Rational representations of a finite group are semisimple and determined by their characteristic-zero characters, so the displayed module isomorphism follows. The invariant subspace has dimension exactly \(5\); for a finite group action, the rational homology of the geometric orbit space equals the invariant rational homology of the original space, proving the quotient statement.

## Verification
The standalone `verify.py` reconstructs all \(20862\) product cells directly from the nine quadratic residues. It checks the complete face vector, both row and column elimination ranks over \(\mathbb F_2\), the signed chain identity \(\partial^2=0\) on every cell in degrees two through four, and all \(171\) signed cellular Lefschetz calculations. It also compares the character of the proposed direct sum on every element. Run `python3 verify.py` with Python 3.10 or later. The terminal marker is `PALEY19_HOM_C3_RATIONAL_AFFINE_CHARACTER_VERIFY_OK`.

## Relationship to prior work
Dochtermann and Singh (2021 preprint; 2023 journal) introduce directed Hom complexes, treat transitive target tournaments, and highlight the directed triangle as a natural equivariant test object. Their transitive-target collapsibility theorem does not cover the nontransitive Paley target. An earlier published finite calculation of \(\operatorname{Hom}(\overrightarrow C_3,R_9)\simeq S^1\) concerns the different nine-vertex regular cyclic tournament, rather than the nineteen-vertex doubly regular tournament. Govc's classification of the **directed flag** complex of doubly regular tournaments, and its later Paley-19 affine character calculation, use transitive subtournaments rather than directed multihomomorphisms; neither implies the present Hom-complex rational character.

## Limitations
Only rational homology and the affine subgroup's rational character are determined. The result does not determine odd-primary integral torsion, higher homotopy groups, the full simplicial automorphism group, or an equivariant homotopy type. The rank proof uses exact mod-two linear algebra together with Euler characteristic rather than a full integral Smith normal form. Independent external review has not been performed, and an unindexed equivalent result is a bibliographic possibility.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948v1 (first public 2021-08-24), European Journal of Combinatorics 110 (2023), 103704. https://arxiv.org/abs/2108.10948
2. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333v1 (2020-06-09), especially Proposition 3.4. https://arxiv.org/abs/2006.05333
3. *The directed Hom complex of the oriented triangle into the regular cyclic tournament of order nine is a circle*, public research record (2026): https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-directed-hom-complex-operatorname-hom-overrightarrow-c-3-r-9--879b51cbdd1a
4. *Affine symmetry identifies the Paley-19 directed flag complex and its homology character*, public research record (2026): https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-affine-symmetry-identifies-the-paley-19-directed-flag-complex-an--9f50497a76ce
