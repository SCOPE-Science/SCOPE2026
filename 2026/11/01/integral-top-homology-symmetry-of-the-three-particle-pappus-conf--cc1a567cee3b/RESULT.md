# Integral top-homology symmetry of the three-particle Pappus configuration space

## Finding
Let \(P\) be the 18-vertex Pappus graph, given by the LCF sequence \([5,7,-7,7,-7,-5]^3\), and put \(X=\operatorname{UConf}_3(|P|)\), the space of unordered triples of distinct points of its graph realization. The full graph automorphism group \(G=\operatorname{Aut}(P)\) has order \(216\). Its action on \(H_3(X;\mathbb Z)\cong\mathbb Z^7\) is determined as an **integral lattice representation** by the explicit basis and exact action algorithm in `verify.py`.

The representation has kernel **exactly** the unique normal order-three subgroup detected by two automorphisms each acting as six disjoint three-cycles on vertices. Hence the induced action of the 72-element quotient is faithful. Over \(\mathbb Q\), its representation splits as a sum of three pairwise inequivalent, absolutely irreducible constituents of dimensions \(1\), \(2\) and \(4\). More canonically, let \(Z\) be the sum in \(\mathbb Q[G]\) of the nine involutions fixing six graph vertices. The constituents are \(\ker(Z-9I)\), \(\ker(Z+9I)\), and \(\ker Z\), respectively.

There are thirteen conjugacy classes; the complete degree-three character table follows. Vertex cycle type is listed with repeated lengths in exponent notation. The two equal-looking order-twelve rows are distinct conjugacy classes with the same trace; `verification_output.json` gives an explicit vertex permutation for every row.

| Class | Size | Element order | Vertex cycle type | \(\operatorname{tr}(g\mid H_3)\) |
| ---: | ---: | ---: | --- | ---: |
| 1 | 1 | 1 | \(1^{18}\) | 7 |
| 2 | 2 | 3 | \(3^{6}\) | 7 |
| 3 | 9 | 2 | \(2^{6}1^{6}\) | -1 |
| 4 | 12 | 3 | \(3^{5}1^{3}\) | 1 |
| 5 | 12 | 3 | \(3^{6}\) | 4 |
| 6 | 18 | 2 | \(2^{7}1^{4}\) | -1 |
| 7 | 18 | 2 | \(2^{9}\) | 3 |
| 8 | 18 | 4 | \(4^{3}2^{3}\) | -1 |
| 9 | 18 | 6 | \(6^{2}3^{2}\) | -1 |
| 10 | 18 | 12 | \(126\) | -1 |
| 11 | 18 | 12 | \(126\) | -1 |
| 12 | 36 | 6 | \(6^{2}321\) | -1 |
| 13 | 36 | 6 | \(6^{3}\) | 0 |

In particular, the invariant subspace \(H_3(X;\mathbb Q)^G\) vanishes, and therefore \(H_3(X/G;\mathbb Q)=0\). This last conclusion is only about degree-three rational homology, not the whole quotient homotopy type. The nonequivariant rank seven was already reported previously; the integral action, its kernel, complete character and irreducible splitting are the contribution here.

## Assumptions and scope
All graphs are undirected and simple. In the LCF notation the vertices are \(0,\ldots,17\), each is adjacent to its two cyclic neighbors and its prescribed chord endpoint. All configuration points are distinct and unordered. Homology coefficients are as indicated, with no assumption about lower-degree torsion. The full automorphism group acts by homeomorphisms of \(X\). This theorem concerns exactly three particles, not an arbitrary number of particles.

## Proof
Use the fully reduced Świątkowski complex of \(P\), which computes the integral homology of the unordered configuration space by the comparison theorem of An, Drummond-Cole and Knudsen (Theorem 4.5 and Proposition 4.9). At each cubic graph vertex \(v\), order its incident graph edges and select the smallest as reference \(e_0(v)\). Use the two degree-one generators \(h_{v,e}-h_{v,e_0(v)}\) for the remaining incident edges. Their differential is \(e-e_0(v)\). In particle weight three, its degree-three group has \(\binom{18}{3}2^3=6528\) generators, while its degree-two group has \(\binom{18}{2}2^2\cdot27=16524\). Degree four is zero.

Order the degree-three generators lexicographically, with increasing vertex indices; order the degree-two generators lexicographically with one remaining edge variable. The standalone exact verifier constructs the complete signed differential. Sparse Gaussian elimination modulo \(101\) yields \(6521\) pivots, a rigorous lower bound on the differential's rank over \(\mathbb Q\). It simultaneously constructs seven sparse vectors with free-coordinate indices \((4641,5841,6217,6353,6360,6481,6512)\). After symmetric integer lifting, **each vector has exactly zero integral boundary**. Their matrix of coefficients on the seven named free coordinates is the identity. Therefore the differential has rational rank at most \(6521\), hence exactly \(6521\), and these seven cycles form a rational kernel basis. Moreover, every integral kernel vector is the integral linear combination of these seven cycles with coefficients given by its seven free coordinates. Thus they form an **integral** basis of \(H_3(X;\mathbb Z)\).

For a graph automorphism \(g\), a local generator transforms to \(h_{g(v)},g(e)}-h_{g(v)},g(e_0(v))}\). Express it in the two chosen generators at \(g(v)\), then reorder the three degree-one factors using the Koszul sign. This defines an exact integer chain action, whose restriction to the seven integral kernel vectors is represented by a \(7\times7\) integer matrix. An exhaustive adjacency-preserving backtracking enumeration gives exactly 216 automorphisms. For all 216, the verifier checks equality of transformed integer chains with their combinations in the seven-element basis, **over \(\mathbb Z\)**. It then computes 13 conjugacy classes and the displayed character, and checks that the identity is the resulting matrix for exactly three group elements.

The character sum is zero, while the character squared-norm is \(\langle\chi,\chi\rangle_G=3\). The central class sum of the nine involutions with six fixed vertices has rational eigenspaces of dimensions \(1,2,4\) at respective eigenvalues \(9,-9,0\), all verified by exact rational matrix ranks. Since the representation contains at least three distinct complex irreducibles and its character squared-norm is exactly three, each eigenspace is absolutely irreducible and no multiplicities occur. The group-average character vanishes, proving the invariant and quotient assertions.

## Verification
Execute `python verify.py` using Python 3.10 or later and only its standard library. Its single JSON result must agree with `verification_output.json`. The calculation includes independent modular-rank lower bounds and exact integer cycle checks; the underlying basis/differential and all automorphisms are regenerated, not imported from a previous calculation. Extra exact reductions at primes \(103\) and \(1009\) also returned rank \(6521\) and the same seven integral cycles. A finite exact calculation is used only for the finite matrix, the group, and the integral certificates; no experimental inference is made about any infinite graph family.

## Relationship to prior work
Abrams established graph configuration-space approaches (2000), and Świątkowski introduced a cellular model (2001). The comparison theorem and reduced model used here are in An–Drummond-Cole–Knudsen (2019); Maciążek–Sawicki (2019) develops computations of graph configuration-space homology, including examples of topological torsion, but does not present this 216-element Pappus top-homology character in its inspected body. A preceding publicly indexed exact calculation gives the rank seven of the top homology, so that rank is explicitly not a novelty assertion. A separate earlier computation concerns the two-particle Pappus space and therefore does not imply the three-particle integral action. The remaining literature risk is an equivalent unindexed or inaccessible equivariant computation.

## Limitations
No assertion is made about all integral homology groups, cup products, braid-group presentations, lower-degree character representations, quotient homotopy types, or the integral module for larger particle numbers. The complete integer matrices are given algorithmically via the canonical basis in the reproducibility code, rather than printed as 216 separate matrices. Priority has not been independently certified.

## References
- A. Abrams, *Configuration spaces and braid groups of graphs*, University of California, Berkeley PhD thesis (public record dated 2000-05-01), https://math.berkeley.edu/publications/configuration-spaces-and-braid-groups-graphs.
- J. Świątkowski, *Estimates for homological dimension of configuration spaces of graphs*, Colloquium Mathematicum 89 (2001), 69–79, DOI 10.4064/cm89-1-5.
- B. H. An, G. C. Drummond-Cole, B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, Documenta Mathematica 24 (2019), 1513–1583, DOI 10.4171/DM/709; especially Theorem 4.5, Definition 4.7 and Proposition 4.9.
- T. Maciążek, A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, DOI 10.1007/s00220-019-03583-5.
- Earlier publicly indexed calculation of the seven-dimensional top homology of three-particle Pappus configurations, scientific record `94f23a73ed7c` (complete text not retrieved).
