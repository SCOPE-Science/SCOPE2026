# Klein-bottle singularities and affine homology of the eleven-point Paley tournament flag complex

## Finding
Let \(R=\{1,3,4,5,9\}\) be the subgroup of quadratic residues in \(\mathbb F_{11}^{\times}\). Let \(P_{11}\) be the tournament on \(\mathbb F_{11}\) with \(u\to v\) if and only if \(v-u\in R\), and let \(K=\operatorname{dFl}(P_{11})\) be the simplicial complex whose faces are its transitive subtournaments. The unique transitive order orients each face.

**Theorem.** The three-dimensional complex \(K\) is a normal pseudomanifold with an isolated nonmanifold singularity at each of its eleven vertices. Every vertex link is a triangulation of the Klein bottle. Under the natural action of \(G=\{x\mapsto ax+b:a\in R,b\in\mathbb F_{11}\}\cong C_{11}\rtimes C_5\), the complete reduced rational homology is
\[
\widetilde H_2(K;\mathbb Q)\cong \ker\!\left(\mathbb Q[\mathbb F_{11}]\xrightarrow{\sum}\mathbb Q\right),
\qquad \widetilde H_i(K;\mathbb Q)=0\quad(i\ne2).
\]
Here \(G\) acts on the right-hand permutation module through its natural affine action on eleven points. The degree-two character takes the values \(10\) at the identity, \(-1\) on the ten nonidentity translations, and \(0\) on the other forty-four affine maps. In particular,
\[
\widetilde H_*(|K|/G;\mathbb Q)=\widetilde H_*(|K|/C_{11};\mathbb Q)=0,
\qquad H_2(|K|/C_5;\mathbb Q)\cong\mathbb Q^2.
\]
The subgroup \(C_5\) is the stabilizer of the vertex zero, consisting of nonzero-square dilations.

## Assumptions and scope
All homology representations in this statement use rational coefficients; the local link assertion and pseudomanifold assertion are integral/combinatorial. The directed flag complex is **not** the directed out-neighborhood complex, the full tournament complex, or a directed Hom/multipath complex. A transitive subtournament has exactly one total ordering consistent with its arcs, so every simplex has a canonical orientation.

The complete face vector in dimensions zero through three is \((11,55,110,55)\). There are no simplices of dimension greater than three. The four-subtournament and three-subtournament counts are **already implied** by the published formulas of McCarthy–Springfield, and the nonequivariant homotopy type \(M(\mathbb Z/2,2)\vee\bigvee^{10}S^2\) was already established by Govc. Neither is asserted as a new result here.

## Proof
**1. Exact finite incidence certificate and links.** A subset of a tournament is transitive precisely when its vertices admit outdegrees \(0,1,\ldots,k-1\) within that subset; its descending-outdegree ordering is then the unique transitive order. Enumerating all \(\binom{11}{k}\) subsets for \(1\le k\le5\) by this test gives \(11,55,110,55,0\) for the respective cardinalities. Every triangle lies in exactly two tetrahedra, and the graph connecting tetrahedra along triangular faces is connected. Hence the complex is pure and connected in codimension one.

For reference, the twenty triangles of the link at vertex zero, using the symbol `a` for vertex ten, are

`134, 139, 145, 157, 178, 189, 235, 23a, 257, 267, 268, 28a, 34a, 359, 459, 469, 46a, 67a, 689, 78a`.

They have ten vertices and thirty edges. Each link edge belongs to exactly two triangles; at each link vertex, the triangles form a single six-cycle. The dual triangle-adjacency graph is connected. This proves that the link is a connected closed combinatorial surface. Its Euler characteristic is \(10-30+20=0\). The edge-sign equations for a coherent orientation have a contradiction: writing each triangle in increasing order, adjacent triangles whose common edge is omitted in positions \(i,j\) must have relative orientation signs \((-1)^{i+j+1}\); the finite certificate detects inconsistent propagation around the dual graph. Thus the connected closed surface is nonorientable and of Euler characteristic zero, so it is the Klein bottle. Translation by any element of \(\mathbb F_{11}\) carries this calculation to every other vertex. All vertex links are therefore connected, and the codimension-one incidence and dual-connectivity checks show that \(K\) is a normal three-pseudomanifold with exactly those eleven singular vertices. (The edge links are circles as follows from the vertex-link calculation.)

**2. Rational homology and exact rank bounds.** Orient every face by increasing numerical vertex order to form the usual simplicial chain complex. The boundary matrices in degrees one, two, and three have exact ranks \(10,45,55\) over \(\mathbb F_3\), by exhaustive modular row reduction in `paley11_checker.py`. These are also their ranks over \(\mathbb Q\): the rank of the first boundary is at most ten because its image lies in the augmentation kernel of the eleven-dimensional degree-zero chain group. The degree-two rank is at most \(55-10=45\), because \(\partial_1\partial_2=0\) and \(\operatorname{rank}_{\mathbb Q}\partial_1=10\). The degree-three rank is at most its fifty-five columns. Since rank cannot decrease on passing from \(\mathbb F_3\) to \(\mathbb Q\), all three ranks are exactly as stated over \(\mathbb Q\). The rational Betti vector is therefore \((1,0,10,0)\).

**3. The affine representation.** Multiplication by a quadratic residue and addition by an arbitrary field element preserve the tournament arcs, and hence act simplicially on \(K\). If such an automorphism maps a transitive subtournament to itself, then it restricts to an automorphism of a linearly ordered tournament. Distinct outdegrees force this restriction to be the identity. Consequently every stabilized simplex is fixed pointwise and contributes sign \(+1\) to the cellular Lefschetz number. An affine map has eleven fixed vertices if it is the identity, none if it is a nonzero translation, and exactly one if its multiplier is not one. The corresponding ordinary Lefschetz numbers are \(\chi(K)=11\), \(0\), and \(1\).

Because the only rational homology degrees are zero and two, with trivial degree-zero action, the degree-two traces are those numbers minus one: respectively \(10,-1,0\). But the augmentation submodule of the natural eleven-point permutation representation has precisely the same character, since its trace is the number of fixed points minus one. By Maschke's theorem and equality of rational characters (over characteristic zero), these two \(\mathbb Q[G]\)-modules are isomorphic.

**4. Quotients.** The action has no inversions of simplices, and over \(\mathbb Q\) passing to finite-group coinvariants is exact. Thus the rational homology of each geometric quotient is the invariants in the homology of \(K\). The affine group and its translation subgroup are transitive on eleven vertices; their augmentation module has no invariant vectors. The order-five subgroup of dilations has precisely three vertex orbits, namely \(\{0\},R,-R\); the augmentation condition removes one dimension from the three-dimensional fixed permutation subspace, leaving two invariant degree-two classes. No other positive-degree rational quotient homology can occur.

## Verification
Execute the embedded standalone Python 3 file `paley11_checker.py` using `python3 paley11_checker.py`. It imports only the Python standard library. The checker enumerates every vertex subset of sizes one through five, every incidence in both the complete complex and all eleven links, and all fifty-five affine transformations. It checks the surface, connectedness and nonorientability conditions, exactly reduces all three signed boundary matrices over \(\mathbb F_3\), and verifies character values and three quotient-invariant multiplicities. Its success marker is `PALEY11_LINK_AND_AFFINE_CHARACTER_EXACT_OK`. The finite calculation is exhaustive for this eleven-vertex complex; no infinite-family claim is made. The above rank comparison and Lefschetz argument are independent mathematical proof steps, not assumptions made by the code.

## Relationship to prior work
Govc's Proposition 3.4 already determines the homotopy type of the unique eleven-vertex doubly regular tournament flag complex, including its integral two-torsion and ten rational two-sphere generators. The present tournament is doubly regular (all outdegrees five; every pair has two common outneighbors), so that theorem applies. In particular, no new nonequivariant homotopy classification or first appearance of torsion is claimed. McCarthy and Springfield's Corollaries 2.3 and 2.7 already determine the counts of transitive four- and three-vertex subtournaments; those counts do not determine local surface links or a homology action. The separately studied Paley-tournament *out-neighborhood* complex and *directed Hom* complex are different functorial constructions, not equivalents of this directed flag complex. Prior work on Klein-bottle triangulations likewise does not by itself identify every link of this tournament complex or its affine rational homology module.

The contribution here is the joint local-geometric and equivariant identification: eleven Klein-bottle links in a natural finite tournament pseudomanifold, with complete order-fifty-five symmetry on second rational homology and differing rational quotient homologies. The already-known torsion makes this local geometry especially natural to examine.

## Limitations
The theorem does not determine the full integral equivariant module, the fundamental groups of the quotient spaces, or the actions of automorphisms outside the stated affine subgroup. It does not establish a new nonequivariant homotopy type, new face numbers, or an infinite-family result. The comparison used the named primary papers and indexed records; unindexed equivalent descriptions of this finite complex or its links remain possible. No independent audit or external validation has been performed.

## References
1. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333 (first posted 2020-06-09), especially Proposition 3.4. https://arxiv.org/abs/2006.05333
2. D. McCarthy and M. Springfield, *Transitive subtournaments of k-th power Paley digraphs and improved lower bounds for Ramsey numbers*, arXiv:2311.02135 (first posted 2023-11-03), especially Corollaries 2.3 and 2.7. https://arxiv.org/abs/2311.02135
3. D. Govc, R. Levi, and J. P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, arXiv:2003.00324 (2020). https://arxiv.org/abs/2003.00324
