# The full symmetric-group homology character of the Petersen neighborhood complex

## Finding
Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph, with vertices the two-element subsets of \([5]=\{1,2,3,4,5\}\) and edges joining disjoint subsets. Let \(K=\mathcal N(P)\) denote the *ordinary open-neighborhood complex*: a nonempty set of graph vertices is a face precisely when it has a common neighbor in \(P\). Relabeling the five underlying points gives the full natural \(S_5\)-action. The rational first-homology representation is
\[
\boxed{\widetilde H_1(K;\mathbb Q)\cong_{\mathbb Q[S_5]}S^{(3,1,1)}\oplus S^{(2,2,1)}.}
\]
Here \(S^\lambda\) is the irreducible rational Specht module indexed by partition \(\lambda\) of five. These constituents have dimensions six and five respectively; they are absolutely irreducible and nonisomorphic. The complete character on cycle classes \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\) is
\[
\boxed{\chi_{\widetilde H_1}=(11,-1,-1,-1,-1,1,1).}
\]
The entire reduced integral homology is \(\widetilde H_1(K;\mathbb Z)\cong\mathbb Z^{11}\), and all other reduced integral homology vanishes. The integral homotopy type, namely a wedge of eleven circles, is not presented as new: the contribution is the **complete natural rational symmetry representation**. In particular \(\widetilde H_1(K;\mathbb Q)^{S_5}=0\).

## Assumptions and scope
The graph is the ten-vertex Petersen graph in its Kneser-duad model, not the complement (triangular graph), not a line graph, and not a stable Kneser cycle. All simplicial chains use the increasing lexicographic order of the ten duads for orientations. The \(S_5\)-action on an oriented simplex permutes duads and includes the induced orientation sign. A degree-one homology module is considered over characteristic zero; the integral assertion concerns only the underlying free abelian group, not an integral decomposition into Specht lattices. No assertion is made about any larger Kneser family.

## Proof
**1. Exact simplicial structure and homology concentration.** Every vertex of \(P\) is a duad \(u\), and its open neighborhood contains exactly the three duads inside the complementary three-element subset \(A=[5]\setminus u\). Thus the facets of \(K\) are the ten triangles
\[
T_A=\big\{\{a,b\}:a,b\in A,\ a\ne b\big\},\qquad A\subset[5],\ |A|=3.
\]
Two different such triangles share at most one vertex: sharing two duads forces the three-point union to be the same subset \(A\). Hence every one of the thirty edges belongs to exactly one triangle. Each triangle has three free edges. Choose the lexicographically first edge from each triangle and perform ten elementary simplicial collapses. The result is a graph on ten vertices and twenty edges. It is connected: the original one-skeleton of \(K\) is the distance-two graph of \(P\), which is the complement of \(P\), and is connected; removal of a triangle edge preserves connectedness through the other two edges of that triangle. Therefore
\[
K\simeq\bigvee^{11}S^1,\qquad 11=20-10+1.
\]
In particular \(H_0(K;\mathbb Q)\) is the one-dimensional trivial \(S_5\)-representation, and positive reduced homology occurs only in degree one. Although the described collapse need not preserve all \(S_5\) symmetries, homology and Euler characters remain equivariant.

**2. Identify the actual chain representations.** Write \(S^\lambda\) for ordinary rational Specht modules. The ten vertices of \(K\) are duads, so
\[
C_0(K;\mathbb Q)=\operatorname{Ind}_{S_2\times S_3}^{S_5}(\mathbf 1\boxtimes\mathbf 1)
\cong S^{(5)}\oplus S^{(4,1)}\oplus S^{(3,2)}.
\]
Each oriented edge of \(K\) joins two duads sharing one point, for example \(\{a,b\}\) and \(\{a,c\}\). Thus its underlying support is a triple with one distinguished common point. The edge stabilizer permutes \(b,c\) with **negative** orientation character, permutes the two points outside the triple trivially, and fixes \(a\). Consequently
\[
C_1(K;\mathbb Q)=\operatorname{Ind}_{S_1\times S_2\times S_2}^{S_5}
(\mathbf1\boxtimes\operatorname{sgn}_{S_2}\boxtimes\mathbf1)
\cong S^{(4,1)}\oplus S^{(3,2)}\oplus 2S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}.
\]
The ten oriented triangles correspond to three-element subsets. Permutations within a triple act on its three duads through the natural three-point permutation, so their orientation sign is exactly \(\operatorname{sgn}_{S_3}\). Hence
\[
C_2(K;\mathbb Q)=\operatorname{Ind}_{S_3\times S_2}^{S_5}
(\operatorname{sgn}_{S_3}\boxtimes\mathbf1)
\cong S^{(3,1,1)}\oplus S^{(2,1,1,1)}.
\]
All displayed decompositions follow directly from the horizontal-strip (Pieri) rule. In particular the middle induced representation can be computed by \(s_{(1,1)}h_2h_1=(s_{(3,1)}+s_{(2,1,1)})h_1\). Their dimensions respectively total \(10,30,10\), agreeing with the simplex counts.

**3. Equivariant Euler character.** Since \(K\) is connected and has no positive homology except \(H_1\), the Hopf trace identity holds in the rational representation ring:
\[
[\widetilde H_1(K;\mathbb Q)]=[H_0]-[C_0]+[C_1]-[C_2].
\]
Substituting the three exact decompositions cancels all constituents except one copy each of \(S^{(3,1,1)}\) and \(S^{(2,2,1)}\). Semisimplicity of \(\mathbb Q[S_5]\) yields the asserted actual module decomposition, not just a virtual identity. The two modules are nonisomorphic absolutely irreducible rational Specht modules.

**4. Closed character expression.** Let \(f(g)\) count fixed points of \(g\in S_5\) on \([5]\); let \(d(g)\) count fixed two-element subsets. If \(V\) is the four-dimensional standard module, then \(S^{(3,1,1)}\cong\bigwedge^2 V\), and \(S^{(2,2,1)}\cong\operatorname{sgn}\otimes S^{(3,2)}\). The character of \(V\) is \(f(g)-1\), while the character of \(S^{(3,2)}\) is \(d(g)-f(g)\), obtained from the permutation modules on duads and on points. Therefore for every \(g\in S_5\),
\[
\chi(g)=\frac{(f(g)-1)^2-(f(g^2)-1)}2
+\operatorname{sgn}(g)\bigl(d(g)-f(g)\bigr).
\]
Evaluating this formula on the seven classes gives the stated character vector. The average of \(\chi\) over all 120 permutations is zero; this independently confirms that there are no globally invariant first-homology classes.

## Verification
The self-contained `verify.py` (standard-library Python 3) independently reconstructs every face from the graph's common-neighbor definition, checks every free triangle-edge pair and connectedness of the resulting graph, enumerates all 120 coordinate permutations and their signed simplex traces, and checks the formula and character inner products. It prints the exact class sizes \((1,10,15,20,20,30,24)\), verifies the identity trace eleven, and checks that both six- and five-dimensional constituents have character norm one and are orthogonal. Run `python3 verify.py`; successful execution ends in `PASS`. The proof of the equivariant representation rests on the explicit chain-module inductions and Pieri rule above; the exhaustive finite script is an independent, reproducible check, not a substitute for those arguments.

## Relationship to prior work
Nilakantan–Singh's general nonequivariant theorem (arXiv:1802.05848, Theorem 1.3) gives \(\mathcal N(\mathrm{KG}(5,2))\simeq\bigvee^{11}S^1\). It neither identifies the action of all underlying-coordinate permutations on the eleven generators nor implies the irreducible splitting. Kozlov's survey (arXiv:math/0505563) explains the topological role and definitions of neighborhood complexes in graph coloring, without this Petersen character. Schultz (arXiv:1003.5688) analyzes equivariance for *stable* Kneser graphs and their dihedral actions; those are different graphs and different group actions. A previously published complete character calculation for \(\mathcal N(\mathrm{KG}(6,2))\) identifies representations of \(S_6\) on **second** homology. Restricting that representation does not compute first homology for \(\mathrm{KG}(5,2)\): neither a homology-equivalence comparison between the two complexes nor a degree-shifting map is supplied. Results for the Petersen matching, three-cut, or unordered-configuration complexes concern different simplicial or topological objects. The novelty claim is specifically the full rational \(S_5\) action in degree one for the **ordinary** Petersen neighborhood complex.

## Limitations
This result does not determine the integral \(\mathbb Z[S_5]\)-lattice isomorphism class, an equivariant homotopy type, or a formula for all Kneser graphs. The known eleven-circle wedge is not new. A computationally identical or equivalent character calculation might exist outside the indexed material; the literature comparison cannot prove universal nonexistence. No independent mathematical audit is claimed.

## References
1. D. N. Kozlov, *Chromatic numbers, morphism complexes, and Stiefel-Whitney characteristic classes*, arXiv:math/0505563v1, first publicly submitted 2005-05-26. https://arxiv.org/abs/math/0505563.
2. C. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1, first publicly submitted 2010-03-29. https://arxiv.org/abs/1003.5688.
3. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(\mathrm{KG}_{2,k}\)*, arXiv:1802.05848v1, first publicly submitted 2018-02-16, especially Theorem 1.3. https://arxiv.org/abs/1802.05848.
