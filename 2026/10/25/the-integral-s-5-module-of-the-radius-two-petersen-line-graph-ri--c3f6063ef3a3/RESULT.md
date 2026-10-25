# The integral \(S_5\)-module of the radius-two Petersen line-graph Rips complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph on the ten two-subsets of \(\{1,2,3,4,5\}\), with disjointness as adjacency, and let \(L(P)\) be its fifteen-vertex line graph, equipped with shortest-path distance. At inclusive Rips radius two, \(K=\operatorname{VR}_{\leq 2}(L(P))\), the canonical action of \(\operatorname{Aut}(P)=S_5\) has the following **integral equivariant description**. For each \(c\in\{1,\ldots,5\}\), let \(B_c\) be the three Petersen edges whose two endpoints omit \(c\), and put \(U_c=\ker(\mathbb Z[B_c]\to\mathbb Z)\). Then
\[
 K\cong B_1*B_2*B_3*B_4*B_5,\qquad
 \widetilde H_4(K;\mathbb Z)\cong\bigotimes_{c=1}^5 U_c\cong\mathbb Z^{32}.
\]
Here the equivariance on the tensor product includes the Koszul sign of the permutation of the five join factors. In particular, for \(g\in S_5\), let \(g_c:U_c\to U_{g(c)}\) be the restriction of its permutation of Petersen edges. The top-homology action is the tensor permutation \(\operatorname{sgn}(g)\bigotimes_c g_c\). In the cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), its character is
\[
 \chi=(32,0,8,2,0,0,2).
\]
As a rational \(S_5\)-representation it decomposes as
\[
 2S^{(5)}\oplus S^{(4,1)}\oplus2S^{(3,2)}\oplus2S^{(2,2,1)}\oplus S^{(2,1,1,1)}\oplus2S^{(1^5)}.
\]
The **integral** coinvariant quotient also has no torsion:
\[
 \widetilde H_4(K;\mathbb Z)_{S_5}\cong\mathbb Z^2.
\]
Consequently the top reduced rational homology of \(K/S_5\) has dimension two.

## Assumptions and scope
All complexes are abstract finite simplicial complexes. Vietoris–Rips is defined inclusively by pairwise graph distances at most the integer scale. The symmetric group acts by permutations of \(\{1,\ldots,5\}\) on the vertices of \(P\), hence on edges of \(P\) and vertices of \(L(P)\). All homology and coinvariants are over \(\mathbb Z\) unless a field is specified. No statements are made about the integral homology of the quotient space \(K/S_5\).

## Proof
**1. An exact five-part partition.** Each edge of \(P\) is an unordered pair \(e=\{A,B\}\) of disjoint two-subsets of \([5]\). Exactly one element \(c(e)\in[5]\) lies outside \(A\cup B\). For fixed \(c\), the other four elements admit exactly three pair partitions, so \(|B_c|=3\).

If \(e\ne f\) have the same missing element \(c\), they are different pairings of the same four-set. No endpoints coincide and every endpoint of \(e\) intersects every endpoint of \(f\), so their line-graph distance is at least three. Choosing any endpoints \(A\) of \(e\) and \(C\) of \(f\), they meet in exactly one element, and \([5]\setminus(A\cup C)\) is a two-set disjoint from each. This gives a length-three walk from \(e\) to \(f\) in \(L(P)\), so their distance is exactly three.

For distinct missing elements \(c(e)=x\ne y=c(f)\), select the endpoint \(A\) of \(e\) containing \(y\) and the endpoint \(C\) of \(f\) containing \(x\). Write \(A=\{y,u\}\) and \(C=\{x,v\}\). If \(u\ne v\), these are disjoint, so the Petersen edge \(\{A,C\}\) supplies a path of length at most two in \(L(P)\). If \(u=v\), the other endpoints of \(e,f\) are the same two-set \([5]\setminus\{x,y,u\}\), so \(e,f\) are adjacent in the line graph. Therefore distance three occurs **exactly** for different members of a common \(B_c\).

This identifies the radius-two adjacency graph as \(K_{3,3,3,3,3}\). Its clique complex is the join of the five three-point sets. A three-point discrete complex has reduced degree-zero integral homology \(U_c\cong\mathbb Z^2\); the augmented-chain Eilenberg–Zilber join identification gives reduced degree-four homology \(U_1\otimes\cdots\otimes U_5\), free of rank \(2^5=32\), with no other nonzero reduced homology. More strongly, each three-point set is a wedge of two zero-spheres and the iterated join is homotopy equivalent to \(\bigvee^{32}S^4\). Its face vector in dimensions zero through four is \((15,90,270,405,243)\).

**2. The signed integral action.** Take the chain-level join basis \([b_1]*\cdots*[b_5]\) in that order of color indices. An automorphism \(g\) reorders the five selected vertices by the permutation of color classes; its induced sign on the oriented four-simplex is \(\operatorname{sgn}(g)\). It simultaneously sends each difference \([b]-[b']\in U_c\) to \([g(b)]-[g(b')]\in U_{g(c)}\). This proves the stated \(S_5\)-lattice structure, not merely an equality of Betti numbers.

For a cycle \(C=(c_1,\ldots,c_t)\) of \(g\) on the five colors, the trace of the corresponding tensor-factor cyclic operator equals the trace of the induced return map \(g^t\) on \(U_{c_1}\). Since \(U_{c_1}\) is the augmentation kernel of a three-element permutation module, that trace equals \(\#\operatorname{Fix}_{B_{c_1}}(g^t)-1\). Multiplying these factors over color cycles and applying \(\operatorname{sgn}(g)\) gives
\[
 \chi(g)=\operatorname{sgn}(g)\prod_{C\text{ color cycle}}\bigl(\#\operatorname{Fix}_{B_{c(C)}}(g^{|C|})-1\bigr).
\]
Enumerating the seven conjugacy types using the explicit three pairings gives \(\chi=(32,0,8,2,0,0,2)\). Independently, the oriented-simplex Lefschetz trace \(\sum_{\varnothing\ne\sigma\in K,\,g\sigma=\sigma}(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)-1\) agrees for all 120 automorphisms. Taking inner products with the irreducible \(S_5\) character table (constructed by the Jacobi–Trudi identity) gives multiplicities \((2,1,2,0,2,1,2)\), ordered by partitions \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\).

**3. Integral coinvariants.** Fix for each \(c\) an ordering \(B_c=(b_{c,0},b_{c,1},b_{c,2})\) and an integral basis \(u_{c,0}=[b_{c,0}]-[b_{c,2}]\), \(u_{c,1}=[b_{c,1}]-[b_{c,2}]\) of \(U_c\). Their 32 tensor products give a complete free integral basis. For the four adjacent transpositions \(s_i=(i,i+1)\), build their signed \(32\times32\) action matrices \(R_i\) by image expansion in this basis. The exact integer matrix
\[
 A=[R_1-I\mid R_2-I\mid R_3-I\mid R_4-I]\in M_{32\times128}(\mathbb Z)
\]
presents the integral coinvariants, because these four transpositions generate \(S_5\). The attached standalone Smith-form verifier reconstructs all 128 columns, checks Coxeter relations, and obtains 30 nonzero Smith invariant factors, **all equal to one**, leaving exactly two free generators and no torsion. Hence \(\operatorname{coker}(A)=\mathbb Z^2\). Over characteristic zero, transfer for a finite simplicial group action identifies \(\widetilde H_4(K/S_5;\mathbb Q)\) with \(\widetilde H_4(K;\mathbb Q)^{S_5}\cong\mathbb Q^2\).

## Verification
Run `python3 verify_petersen_line_square.py` with the Python standard library, then `python3 verify_integral_coinvariants.py` with SymPy 1.14. The former independently checks graph distances, all 1023 nonempty simplices, all 120 group actions, the signed simplicial Lefschetz character and the Specht decomposition; the latter checks the integral 32-dimensional action and an exact 32-by-128 Smith computation. `verification_output.txt` contains the actual outputs. The abstract join identification and chain-level signs supply the mathematical proof; finite code supplies exact reproducibility of the specified matrices and invariants.

## Relationship to prior work
Adamaszek [1, Theorem 5.2] proves that for a graph \(G\), the ordinary clique complex of \(L(G)\) has the graph's relevant one-dimensional homotopy, and develops results about graph powers, but does not give the radius-two \(L(P)\) representation. Lužar–Máčajová–Škoviera–Soták [2, Section 2] describe the canonical strong five-edge coloring of the Petersen graph by its missing symbol. Their coloring, combined with elementary graph reasoning, **already accounts for the five-color partition and immediately suggests the nonequivariant 32-sphere join**; neither that partition nor the nonequivariant Betti number is asserted to be new in isolation. The subject of this finding is the precise **integral equivariant refinement**, its full seven-value \(S_5\) character, all irreducible multiplicities, and the torsion-free rank-two integral coinvariant lattice. Prior comparisons with published Petersen matching, graph-configuration, and three-cut homology concern distinct functors and do not imply those representations. No claim of exhaustive bibliographic novelty is made.

## Limitations
The finding concerns the fifteen edge-vertices of the Petersen line graph at inclusive graph scale two, not configurations on the graph or its ordinary matching complex. It calculates integral homology as an \(S_5\)-module and its coinvariants, but not the integral homology or equivariant stable homotopy type of the orbit space. The source comparison cannot exclude unindexed treatments of the same action. The exact Smith computation uses SymPy, in addition to the explicit theoretical finite presentation.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, first public arXiv posting 2011-04-03, arXiv:1104.0433, https://arxiv.org/abs/1104.0433.

[2] B. Lužar, E. Máčajová, M. Škoviera, R. Soták, *Strong edge colorings of graphs and covers of Kneser graphs*, arXiv:2101.04768, 2021, https://arxiv.org/abs/2101.04768.
