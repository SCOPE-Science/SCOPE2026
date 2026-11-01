# Full affine symmetry of the Clebsch neighborhood complex

## Finding
Let \(A=\mathbb F_2^4\), let \(s_1,s_2,s_3,s_4\) be its standard basis, and set \(s_5=s_1+s_2+s_3+s_4\). Let \(C=\operatorname{Cay}(A,\{s_1,\dots,s_5\})\) be the **5-regular** Clebsch graph, and let \(K=\mathcal N(C)\) be its open-neighborhood simplicial complex. Its full graph automorphism group is \(G=A\rtimes\mathfrak S_5\), of order \(1920\).

The rational reduced homology vanishes except in degree two, and \(\dim_{\mathbb Q}\widetilde H_2(K;\mathbb Q)=31\). The new classification is the following exact \(G\)-module decomposition:
\[
\boxed{\begin{aligned}
\widetilde H_2(K;\mathbb Q)\cong{}&
\operatorname{Inf}_{\mathfrak S_5}^{G}\!\left(\bigwedge^2 V_5\right)\\
&\oplus\operatorname{Ind}_{A\rtimes(\mathfrak S_2\times\mathfrak S_3)}^{G}
\left(\lambda_{\{1,2\}}\otimes(\mathbf1\boxtimes\varepsilon_3)\right)\\
&\oplus\operatorname{Ind}_{A\rtimes\mathfrak S_4}^{G}
\left(\lambda_{\{1,2,3,4\}}\otimes(\varepsilon_4\otimes V_4)\right).
\end{aligned}}
\]
Here \(V_m\) is the \((m-1)\)-dimensional standard rational representation of \(\mathfrak S_m\), \(\varepsilon_m\) is its sign character, and \(\lambda_J\in\widehat A\) is characterized by \(\lambda_J(s_i)=-1\) if \(i\in J\) and \(+1\) otherwise (for even-cardinality \(J\subseteq\{1,2,3,4,5\}\)). These characters extend to the stated stabilizers because their indexing subsets are invariant there. The dimensions of the three summands are \(6,10,15\).

In particular, under the translation subgroup \(A\), the multiplicities of the trivial character, the ten characters indexed by two-subsets, and the five characters indexed by four-subsets are respectively \(6,1,3\). Thus the translation quotient has \(\dim H_2(K/A;\mathbb Q)=6\), but the full-symmetry quotient is rationally acyclic: \(\widetilde H_*(K/G;\mathbb Q)=0\). Both quotient statements concern ordinary orbit spaces.

## Assumptions and scope
All groups act by simplicial coordinate permutations on the indicated complex; all homology representations are over \(\mathbb Q\), and the graph uses the 5-regular convention for Clebsch rather than its 10-regular complement. For a simple graph \(C\), the nonempty faces of \(\mathcal N(C)\) are precisely the finite sets of vertices having a common neighbor. The formula uses inflation along \(G\twoheadrightarrow\mathfrak S_5\), subgroup induction, and the usual sign-twisted standard representation. No integral \(G\)-lattice classification is claimed.

## Proof
**1. Graph, group and chain groups.** Encode \(A\) by integers \(0,\ldots,15\), with the five generators represented by \(1,2,4,8,15\). Every vertex \(v\) has open neighborhood \(v+\{s_i\}\). Translation and permutation of the five generators produce \(A\rtimes\mathfrak S_5\); each permutation is realized by a unique linear map on \(A\). Conversely, an automorphism fixing zero permutes its five neighbors, which determine the ten distance-two vertices through their uniquely shared additional neighbor. Hence every automorphism lies in this semidirect product.

The complex has face vector \((16,80,160,80,16)\). Every face of cardinality at least three lies in **exactly one** neighborhood: two distinct neighborhoods intersect in at most two vertices, because the graph has common-neighbor parameters zero for adjacent pairs and two for nonadjacent pairs. Its one-skeleton is the connected 10-regular complement of \(C\), so \(\operatorname{rank}\partial_1=15\). Splitting the degree-three and degree-four chain groups over the 16 distinct 4-simplex neighborhoods shows \(\operatorname{rank}\partial_3=16\cdot4=64\) and \(\operatorname{rank}\partial_4=16\): these are the standard degree-three and degree-four boundary ranks for one 4-simplex, and the 2-faces of distinct neighborhoods are disjoint. Since \(\partial_1\partial_2=0\), \(\operatorname{rank}_{\mathbb Q}\partial_2\le 80-15=65\). A fully specified exhaustive rank computation over \(\mathbb F_2\), supplied in `verify.py`, finds 65 linearly independent columns of \(\partial_2\). This certifies \(\operatorname{rank}_{\mathbb Q}\partial_2\ge65\), and hence equality. The resulting rational Betti numbers are \((1,0,31,0,0)\).

**2. Two independent character computations.** Let \(g=(a,p)\in G\) act by \(x\mapsto a+L_p(x)\), where \(L_p(s_i)=s_{p(i)}\). By the Hopf trace formula and rational homology concentration, the degree-two character \(\chi(g)\) equals the reduced alternating simplicial-chain trace. If \(g\) has vertex orbits \(O_1,\ldots,O_t\), a stabilized face is a union of whole orbits; its signed alternating trace contribution is \((-1)^{j+1}\) when it uses \(j\) orbits. Therefore
\[
\chi(g)=-\sum_{J\subseteq\{1,\ldots,t\}:\,\cup_{j\in J} O_j\in K}(-1)^{|J|},
\]
including the empty face. This formula is independently checked against a second implementation that computes the sign of the permutation on each individually stabilized oriented simplex. Both evaluations agree on **all 1920 group elements**.

**3. Fourier decomposition and stabilizer characters.** For every \(\lambda\in\widehat A\), define its multiplicity by the exact Fourier projector
\[
m_\lambda=\frac1{16}\sum_{a\in A}\lambda(a)\chi(a).
\]
The character of the identity translation is \(31\); for the five generating translations it is \(-1\); for the ten other nonzero translations it is \(7\). Consequently, \(m_{\mathbf1}=6\), while characters with negative values on two of the five \(s_i\) have multiplicity one and those negative on four have multiplicity three. These are precisely the three \(\mathfrak S_5\)-orbits on \(\widehat A\), with stabilizers \(\mathfrak S_5\), \(\mathfrak S_2\times\mathfrak S_3\), and \(\mathfrak S_4\).

For a character \(\lambda_J\) fixed by \(p\), the trace of \(p\) on its multiplicity space is
\[
\chi_J(p)=\frac1{16}\sum_{a\in A}\lambda_J(a)\chi(a,p).
\]
The resulting seven \(\mathfrak S_5\)-class values on the \(A\)-invariant six-space, in cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), are \((6,0,-2,0,0,0,1)\). They are the character of \(\bigwedge^2 V_5\), since the exterior-square character of \(V_5\) is \((\chi_{V_5}(p)^2-\chi_{V_5}(p^2))/2\). For \(|J|=2\), the six stabilizer values are the sign character of the complementary \(\mathfrak S_3\), independent of the \(\mathfrak S_2\) factor. For \(|J|=4\), the five stabilizer values in cycle-type order \((1^4),(2,1^2),(2^2),(3,1),(4)\) are \((3,-1,-1,0,1)\): the character of \(\varepsilon_4\otimes V_4\). By character decomposition for a finite group with an abelian normal subgroup, these three little-group modules induce the three claimed summands. As an independent global check, the direct induced-character formula in `verify.py` agrees with the alternating-chain character for every group element.

**4. Quotients.** Averaging the character over \(A\) gives \(6\), while averaging over all \(1920\) elements gives \(0\). For a finite group action on a finite simplicial complex, rational cohomology of its ordinary quotient identifies with the invariant rational cohomology (use barycentric subdivision, with orbit cells). This proves the quotient assertions.

## Verification
Run `python3 verify.py` with the Python standard library. It exhaustively generates 353 faces including the empty simplex; confirms every face-count and incidence condition; computes the 65-column binary independence certificate for \(\partial_2\); enumerates all 1920 affine automorphisms; compares an oriented-face trace, an orbit-subset trace, and the explicit induced-representation trace separately for **every** automorphism; and checks the translation Fourier multiplicities and quotient-invariant dimensions. The expected output is in `verify_output.txt` and ends in `VERIFY_OK`. The calculation is finite and exhaustive, while the argument that a mod-two rank lower bound gives a rational rank lower bound is proved in the text.

## Relationship to prior work
Lovász introduced neighborhood complexes as topological graph-coloring obstructions. Kozlov (first submitted March 28, 2005) proves a simple-homotopy comparison of neighborhood and graph-Hom complexes but gives no Clebsch-specific full automorphism representation. Csorba proves related natural \(\mathbb Z_2\)-homotopy equivalences, not this \(A\rtimes\mathfrak S_5\)-action.

A previously published complete calculation for this **same 5-regular Clebsch neighborhood complex** establishes the nonequivariant homotopy type \(\bigvee^{31}S^2\) by an acyclic discrete-Morse matching; that result is fully acknowledged, and the 31-dimensional homology itself is **not** claimed as new. Its stated scope does not determine the 1920-element character, the three little-group summands, or the different rational homology of the translation and full-affine quotients. The present result determines these exact equivariant invariants. The general graph-Hom equivalences do not imply a particular finite-group homology character without extra computation.

## Limitations
The theorem classifies a rational representation, not an integral module or equivariant homotopy type. It does not classify other folded cubes. As with any bounded literature and database search, unindexed equivalent character calculations may exist. The direct rank computation and character calculation are short exact finite algorithms; no independent external validation is asserted.

## References
1. L. Lovász, “Kneser's conjecture, chromatic number, and homotopy,” *J. Combin. Theory Ser. A* 25 (1978), 319–324, DOI: 10.1016/0097-3165(78)90022-5.
2. D. N. Kozlov, “Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes,” arXiv:math/0503613, first submitted 2005-03-28; *Topology Appl.* 153 (2006), 2445–2454.
3. P. Csorba, “On the simple \(\mathbb Z_2\)-homotopy types of graph complexes and their simple \(\mathbb Z_2\)-universality,” *Canad. Math. Bull.* 51 (2008), 535–544, DOI: 10.4153/CMB-2008-053-9.
4. “The \(5\)-regular Clebsch neighborhood complex is a wedge of \(31\) \(2\)-spheres,” publicly indexed published-finding corpus research record, 2026-10-11, identifier `1dc11cc6574a`. Its nonequivariant homotopy calculation precedes the present representation result.
