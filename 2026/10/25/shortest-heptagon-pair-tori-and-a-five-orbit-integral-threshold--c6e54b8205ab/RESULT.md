# Shortest heptagon-pair tori and a five-orbit integral threshold for the McGee configuration space

## Finding
Let \(G\) be the McGee graph, presented by the Hamiltonian LCF sequence \([12,7,-7]^8\) on \(24\) vertices, and let \(X=\operatorname{UConf}_2(|G|)\) be the space of unordered distinct pairs of points on its geometric realization. For each unordered pair of vertex-disjoint simple seven-cycles, take the oriented embedded product torus in \(X\). Then:

1. The graph contains exactly \(32\) simple seven-cycles and exactly \(152\) unordered vertex-disjoint pairs. Their tori generate the complete integral group \(H_2(X;\mathbb Z)\cong\mathbb Z^{54}\), with \(54\) tori constituting an integral basis.
2. The \(32\)-element automorphism group has precisely seven orbits on these \(152\) geometric tori, of sizes \(16,32,16,8,32,32,16\), in the canonical order defined below.
3. **No union of four or fewer of these orbits generates integral second homology; a union of five does.** For the five orbits indexed \(0,1,2,3,5\), the generated sublattice equals all of \(H_2(X;\mathbb Z)\).
4. The three orbits indexed \(1,3,4\) already span \(H_2(X;\mathbb Q)\) but generate a proper integral sublattice with quotient
\[
H_2(X;\mathbb Z)/L_{\{1,3,4\}}\cong (\mathbb Z/2)^2\oplus\mathbb Z/4.
\]
Thus their index is \(16\). The five-orbit threshold is genuinely integral, not a rational rank threshold.

## Assumptions and scope
Vertices are \(0,1,\ldots,23\). Begin with the Hamiltonian edges joining successive vertices modulo \(24\); for every vertex \(i\), add the chord joining \(i\) to \(i+s_i\) modulo \(24\), where \((s_0,\ldots,s_{23})=(12,7,-7)^8\). Duplicate undirected chords are included only once. This gives a simple connected cubic graph with \(24\) vertices and \(36\) edges and girth \(7\).

Each seven-cycle is represented canonically as a tuple whose first entry is its smallest vertex, with second entry smaller than its last. Order these tuples lexicographically, obtaining indices \(0,\ldots,31\). Order pairs of disjoint cycle indices lexicographically, obtaining torus indices \(0,\ldots,151\). The automorphism orbits are indexed in order of their smallest unassigned torus index. Orient every graph edge from its smaller to its larger vertex, orient every cycle according to its canonical tuple, and orient a product torus by the ordered factors with increasing cycle index. Reversing a torus orientation does not alter its generated lattice.

All statements are about the ordinary unordered configuration space of **exactly two distinct particles**, not an ordered configuration space, sink variant, or graph with additional subdivision. The standard equivariant deformation retraction onto the discrete deleted product for two points makes the finite cubical calculation valid for \(X\).

## Proof
**Cubical model.** The unordered deleted-product cubical complex \(Y\) has zero-cells \(\{v,w\}\) for different vertices, one-cells \((v,e)\) for a graph edge \(e\) not incident to \(v\), and two-cells \((e,f)\) for vertex-disjoint edges, with an ordering of the edge factors used only to orient the square. The chain ranks are
\[
(c_0,c_1,c_2)=(276,792,558).
\]
For oriented \(e_i=[a_i,b_i]\) and \(e_j=[a_j,b_j]\) with \(i<j\), the exact signed boundary is
\[
\partial_2[e_i,e_j]=[(b_i,e_j)]-[(a_i,e_j)]-[(b_j,e_i)]+[(a_j,e_i)].
\]
Also \(\partial_1[(v,e_i)]=[\{v,b_i\}]-[\{v,a_i\}]\). The program checks the full identity \(\partial_1\partial_2=0\).

**Shortest geometric cycles.** Enumerate all oriented simple cycles with smallest vertex first and second vertex less than the final one. There are none of lengths \(3\) through \(6\); there are exactly \(32\) of length \(7\). For each unordered disjoint pair \((C_i,C_j)\), form the signed exterior product of their oriented cellular one-cycles. Its image in the unordered square basis has coefficient \(\epsilon_i(e)\epsilon_j(f)\) or its negative according as the index of \(e\) precedes or follows the index of \(f\). All \(152\) resulting integer columns have vanishing \(\partial_2\).

**Integral generation certificate.** The matrix \(\partial_2\), with \(792\) rows and \(558\) columns, has rank \(504\) modulo \(101\). The \(558\)-by-\(152\) torus matrix contains \(54\) columns and \(54\) rows whose exact integer determinant is \(+1\). The deterministic column and row indices appear in the output of `verify_mcgee.py`; the script constructs all entries and evaluates the integer determinant, rather than trusting stored numerical output. The nonzero minor proves that \(54\) torus columns are rationally independent and, in fact, form a primitive rank-\(54\) direct summand of the ambient square-chain lattice.

Because these \(54\) columns lie in the rational kernel of \(\partial_2\), the rational rank of \(\partial_2\) is at most \(558-54=504\). Its rank modulo \(101\) is a lower bound for its rational rank, so that rank is exactly \(504\). Consequently the rational second homology has dimension exactly \(54\). For any integral two-cycle \(z\), write it uniquely over \(\mathbb Q\) in the selected torus columns. Projection to the \(54\) selected square coordinates makes the coefficient vector integral, because the projected \(54\)-by-\(54\) torus matrix is unimodular. Thus every integral two-cycle lies in their \(\mathbb Z\)-span, proving the asserted integral basis and torsion-free \(H_2\).

**Automorphism-orbit and quotient certificates.** Exhaustive graph isomorphism backtracking produces exactly \(32\) automorphisms. Their action on the \(152\) underlying unoriented cycle pairs produces seven orbits of sizes \(16,32,16,8,32,32,16\). Because orientation changes only signs, orbit-generated integral lattices are well-defined. The selected square-coordinate projection gives an explicit isomorphism from \(H_2(Y;\mathbb Z)\) to \(\mathbb Z^{54}\), so Smith normal forms of projected torus columns are exact homology-lattice quotient invariants.

The maximum rank modulo \(2\) of the lattice generated by a union of exactly \(k\) orbits, for \(k=1,2,3,4\), is respectively \(31,46,51,53\). All \(35\) four-orbit combinations are checked; each proper smaller combination extends to one of them. Therefore at least five orbits are needed for integral generation. The \(54\)-by-\(104\) coordinate matrix for orbits \(\{0,1,2,3,5\}\) has \(54\) unit Smith factors, proving that five suffice. The \(54\)-by-\(72\) coordinate matrix for orbits \(\{1,3,4\}\) has Smith factors \(1\) repeated \(51\) times, followed by \(2,2,4\), proving its rational spanning and exact index-\(16\) integral obstruction.

## Verification
Run `python verify_mcgee.py` with the versions or compatible versions in `requirements.txt`. The program constructs the graph and both boundary operators; tests the chain identity and every torus boundary; enumerates all shortest cycles, disjoint pairs, and automorphisms; calculates modular ranks and an **exact** integer unimodular determinant; and performs integral Smith reductions on the two stated orbit unions. It prints `VERIFY_OK_MCGEE_SHORTEST_CYCLE_TORI_FIVE_ORBIT_THRESHOLD` only after all assertions pass. The primary exact certificates are the determinant \(+1\), the \(54\) unit Smith factors for the five-orbit matrix, and the three nonunit factors \(2,2,4\) for the rationally spanning three-orbit matrix.

## Relationship to prior work
Barnett and Farber, *Topology of configuration space of two particles on a graph, I* (2009), develop the equivariant deleted-product model and intersection theory, with their explicit geometric basis assertions made for planar graphs and ordered two-point spaces. Farber and Hanbury, *Part II* (2010), obtain general ordered configuration homology expressions for mature graphs. Neither source identifies the integral shortest-cycle orbit lattices for the nonplanar \(24\)-vertex McGee graph. An and Knudsen, *On the second homology of planar graph braid groups* (2020), prove a geometric-generation theorem explicitly restricted to planar graphs, with nonplanar counterexamples. Thus that theorem cannot imply the present finite nonplanar shortest-heptagon conclusion.

The McGee graph's uniqueness as the \((3,7)\)-cage and its nonvertex-transitive symmetry group are classical, as surveyed in the 2015 McGee-graph note by John Baez. A published computation that the **McGee independence complex** is a five-sphere concerns a different topological construction, while a published shortest-cycle calculation for the \(28\)-vertex **Coxeter graph** concerns a nonisomorphic graph and does not establish these McGee lattice invariants. The complete available primary papers and targeted mathematical-record searches yielded no assertion of the \(152\)-torus basis, seven orbit sizes, or five-orbit integer threshold for the McGee graph. This comparison is evidence of non-coverage, not a claim of exhaustive literature search.

## Limitations
The theorem does not calculate the lower homology, fundamental group, representations on other homology degrees, or spaces of three or more particles. It does not claim any uniform theorem for all cubic cages. The calculations are exhaustive for the explicitly defined \(24\)-vertex graph and \(152\) shortest-cycle product tori; they do not establish any property of arbitrary larger graphs. A potentially relevant 2010 doctoral thesis on two-point graph configurations was located and its abstract examined, but full-text access was unavailable; possible equivalent unpublished or poorly indexed calculations remain a bibliographic risk. Independent validation has not been performed.

## References
1. Kathryn Barnett and Michael Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180, publicly posted 2009-03-12. https://arxiv.org/abs/0903.2180
2. Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, publicly posted 2010-05-13. https://arxiv.org/abs/1005.2300
3. Byung Hee An and Ben Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, publicly posted 2020-08-24. https://arxiv.org/abs/2008.10371
4. John Baez, *McGee Graph*, AMS Visual Insight, 2015-09-15. https://blogs.ams.org/visualinsight/2015/09/15/mcgee-graph/
5. Kathryn Barnett, *The Configuration Space of Two Particles Moving on a Graph*, Durham University doctoral thesis (2010), abstract available. https://etheses.durham.ac.uk/id/eprint/293/
