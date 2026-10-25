# Full tetrahedral-symmetry and exchange characters of two-point graph configurations

## Finding
Let \(T\) be the truncated-tetrahedral graph, with twelve vertices \((i,j)\) for distinct \(i,j\in\{0,1,2,3\}\); connect two vertices when they have the same first coordinate, or when they are reversals of one another. Set
\[
X=F_2(|T|)=\{(x,y)\in |T|^2:x\ne y\}.
\]
The symmetric group \(S_4\) permutes the four labels simultaneously, and the commuting involution \(\tau(x,y)=(y,x)\) exchanges the two particles. Let \(V\) denote the three-dimensional standard rational representation of \(S_4\), \(V'=V\otimes\operatorname{sgn}\) its sign twist, \(W\) the two-dimensional irreducible of partition \((2,2)\), and \(\mathbf1\) the trivial representation. **The complete second rational homology module, split by particle exchange, is**
\[
H_2(X;\mathbb Q)^{\tau=+1}\cong\mathbf1\oplus2V\oplus V',
\qquad
H_2(X;\mathbb Q)^{\tau=-1}\cong2\mathbf1\oplus2V\oplus W.
\]
Both exchange eigenspaces have dimension ten. For the \(S_4\) conjugacy classes \((1^4),(2,1,1),(2,2),(3,1),(4)\) in that order, their respective characters are
\[
\chi_+=(10,2,-2,1,0),\qquad\chi_-=(10,4,2,1,0).
\]
Equivalently the traces of \(g\) and of \(g\tau\) on all twenty dimensions are \((20,6,0,2,0)\) and \((0,-2,-4,0,0)\), respectively. The subspace fixed by the whole \(S_4\times C_2\) has dimension one. This is a statement about **ordinary singular homology of the ordered configuration space**, not Borel–Moore homology or an unordered configuration space.

## Assumptions and scope
The realization \(|T|\) is the standard one-dimensional graph CW complex. Four disjoint triangles correspond to the first coordinate, and six reversal edges join these triangles, so \(T\) has twelve vertices and eighteen edges. The graph has girth three; every path between distinct vertices of degree at least three contains at least one edge. For two labeled particles these are the standard sufficient-subdivision conditions for the ordered Abrams cubical discrete-configuration complex to be homotopy equivalent to \(F_2(|T|)\). The graph's label-permutation action and particle exchange preserve the cell model, so the equivalence is compatible with these finite symmetries at the level of induced homology. The result is over \(\mathbb Q\); integral representation lattices and higher-particle spaces are not asserted.

## Proof
**1. Finite cubical model and cellular boundary.** Lexicographically index the twelve graph vertices and eighteen undirected edges, and orient each graph edge from its lower index to its higher index. Disjoint closed cells in the ordered product give \(132\) ordered vertex–vertex zero-cells, \(360\) ordered edge–vertex or vertex–edge one-cells, and \(234\) ordered edge–edge two-cells. There are no higher-dimensional cells. The oriented square \([a,b]\times[c,d]\), with \(a<b\) and \(c<d\), has boundary
\[
\partial_2([a,b]\times[c,d])
=(b\times[c,d])-(a\times[c,d])-([a,b]\times d)+([a,b]\times c).
\]
The packaged `verify.py` reconstructs every cell and every signed boundary coefficient.

**2. Exact rank from complementary certificates.** Modular row reduction of this integer \(360\)-by-\(234\) matrix modulo the prime \(1000003\) has exactly \(214\) pivots, proving that its rational rank is **at least** \(214\). The verifier independently enumerates all simple graph cycles (\(84\) in its deterministic orientation convention), forms product cycles from disjoint pairs of cycles, verifies that each resulting signed integer \(2\)-chain has exactly zero boundary, and finds \(20\) independent such chains (independence checked modulo the same prime). Therefore its rational nullity is at least \(20\), so rank is **at most** \(234-20=214\). Together the two inequalities establish precisely
\[
\dim_{\mathbb Q}H_2(X;\mathbb Q)=234-214=20,
\]
with no third cellular differential. Because the integral top homology is a kernel between free abelian groups, it is torsion-free of rank twenty. No claim about torsion in lower homology follows from this observation.

**3. The signed group action.** Relabeling \(g\in S_4\) acts by a signed permutation of the oriented graph edges and hence of ordered product squares. Particle exchange interchanges the square factors and contributes a minus sign from reversing product orientation. Both actions preserve the integer kernel, and exchange commutes with relabeling. The verifier constructs a twenty-vector basis of the kernel modulo \(1000003\) by reduced row-echelon form, then computes the trace of each signed cell permutation on the kernel from its free-coordinate projection. It checks **every one of the twenty-four label permutations with and without exchange**. The five classwise trace pairs \((\operatorname{tr}g,\operatorname{tr}g\tau)\) are
\[
(20,0),\quad(6,-2),\quad(0,-4),\quad(2,0),\quad(0,0).
\]
Each rational trace is an integer with absolute value at most twenty, because it is the character of a finite-order operator on a twenty-dimensional space. Thus reducing modulo \(1000003\) uniquely determines its **exact** rational character: no unproved rational-rank inference from a single prime is used. Half-sums and half-differences yield the characters \(\chi_+\) and \(\chi_-\) above.

**4. Rational irreducibles.** The five standard rational \(S_4\) character rows, in the stated class order, are \((1,1,1,1,1)\), \((1,-1,1,1,-1)\), \((3,1,-1,0,-1)\), \((3,-1,-1,0,1)\), and \((2,0,2,-1,0)\). Taking class-size-weighted inner products, with conjugacy class sizes \((1,6,3,8,6)\), gives multiplicities \((1,0,2,1,0)\) in the exchange-even sector and \((2,0,2,0,1)\) in the exchange-odd sector. These prove exactly the decompositions claimed. The invariant dimension is the multiplicity one of \(\mathbf1\) in the exchange-even sector.

## Verification
Execute `python3 verify.py` with Python 3's standard library. It reconstructs all cells, verifies the signed product boundary, obtains the 214-pivot rank lower bound, produces twenty independent exact integral product cycles for the complementary rank upper bound, computes all forty-eight symmetry traces on the reduced kernel, checks the five class patterns and rational irreducible multiplicities, and prints `VERIFY_OK`. `verification_output.txt` records the actual execution result. Modular computations are used only with the stated rank sandwich and bounded integer trace argument; **a modular calculation alone would not have established these integral or rational facts**.

## Relationship to prior work
Barnett and Farber (2009), *Topology of Configuration Space of Two Particles on a Graph, I*, study ordered configurations on planar graphs and give general nonequivariant topology and Betti-number results. The second part by Farber and Hanbury (2010) develops the same subject further. In the present example the graph cycle rank is seven, so their planar formula yields a twenty-dimensional second homology group, consistent with the rank calculation; it does not specify its decomposition under the tetrahedral relabelings or the particle-exchange involution.

A previously available cuboctahedral two-particle result computes automorphism modules for **a different graph** (the twelve-vertex twenty-four-edge line graph of the cube), and its unordered configuration space is different from \(X\). A separate result gives the exchange-sign **Borel–Moore** homology of two-point configurations of arbitrary graphs; its relative/local-system groups cannot be identified with the ordinary singular homology of \(X\) used here. Another result concerns the **matching complex** of the truncated tetrahedron, a distinct simplicial construction on the same graph, and supplies no graph-configuration representation. The full texts of these close results were compared by object, coefficient theory, and implications. The described exact equivariant character was not present in the inspected sources.

## Limitations
The computation treats the ordered two-particle configuration of this particular graph and rational second homology; it gives neither a classification over all graph families nor an integral automorphism-module normal form. The enumerated character may in principle be derivable indirectly by applying a suitably strengthened natural version of classical planar-graph formulas, so mathematical novelty is asserted only relative to the exact statements and implications inspected, not as a guarantee of publication priority. An unindexed equivalent specialized calculation remains possible. No independent scientific audit has been performed.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first publicly submitted 2009-03-12; https://arxiv.org/abs/0903.2180.
2. M. Farber and E. Hanbury, *Topology of Configuration Space of Two Particles on a Graph, II*, arXiv:1005.2300; https://arxiv.org/abs/1005.2300.
3. *Full symmetry modules of the cuboctahedral two-particle configuration space*, published-finding corpus, record `2026/10/11/SCOPE-full-symmetry-modules-of-the-cuboctahedral-two-particle-configur--5d6ece5c784b`, particularly its `RESULT.md`.
4. *Exchange-sign Borel–Moore homology of two-point graph configurations*, published-finding corpus, record `2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285`, particularly its `RESULT.md`.
5. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published-finding corpus, record `2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83`, particularly its `RESULT.md`.
