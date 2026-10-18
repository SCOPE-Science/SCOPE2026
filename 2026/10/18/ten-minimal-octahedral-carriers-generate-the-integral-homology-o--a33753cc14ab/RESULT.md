# Ten minimal octahedral carriers generate the integral homology of the folded five-cube

## Finding
Let \(G\) be the degree-five Clebsch graph, also called the folded five-cube or Greenwood–Gleason graph. Its vertices are \(V=\mathbb F_2^4\), and two distinct vertices are adjacent precisely when their difference belongs to
\[
S=\{(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,1,1,1)\}.
\]
Write \(K=\operatorname{Ind}(G)\). Exactly ten induced subcomplexes on eight vertices have nonzero third integral homology, and there are no smaller such induced subcomplexes. Each of the ten is the boundary of a four-dimensional cross-polytope, hence an octahedral three-sphere. Their oriented fundamental classes generate the entire group
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^9.
\]
There is exactly one integral relation among these ten classes, and all ten coefficients are units. Consequently, each class is nonzero and primitive, and omitting any one of the ten classes leaves an integral basis.

More explicitly, for each \(s\in S\), let \(\ell_s:V\to\mathbb F_2\) be the unique linear form with \(\ell_s(s)=0\) and \(\ell_s(t)=1\) for the other four \(t\in S\). The ten supports are exactly
\[
W_{s,\epsilon}=\{x\in V:\ell_s(x)=\epsilon\},\qquad (s,\epsilon)\in S\times\mathbb F_2.
\]
Each has eight vertices and \(G[W_{s,\epsilon}]\cong4K_2\). The ten supports form a single orbit under the natural affine graph-automorphism group \(V\rtimes S_5\), of order \(1920\).

## Assumptions and scope
All graphs are finite, simple, and undirected, and all homology is reduced simplicial homology unless otherwise stated. The independence complex is the flag complex of independent vertex sets, and \(K[W]\) denotes its full vertex-induced subcomplex. A carrier means a vertex-induced subcomplex possessing nonzero third integral homology; the stronger assertion that its fundamental class survives the inclusion to \(K\) is proved below. The result concerns this particular sixteen-vertex graph and degree three, not an arbitrary folded cube.

For exact chain-level orientation, encode \(V\) by integers \(0,1,\ldots,15\), with adjacency if the bitwise exclusive-or is in \(\{1,2,4,8,15\}\). Order all simplices increasingly by vertex bit-mask, and order the ten eight-vertex supports lexicographically as tuples of vertices. Within each induced four-edge matching, sort its edges lexicographically and orient the fundamental cycle as the join of the four zero-cycles \((a)-(b)\), where \(a<b\) in each matched pair. In an oriented simplex, restore increasing vertex order with its permutation sign.

## Proof
**Sharp flag-complex support bound.** If a flag simplicial complex \(X\) has \(\widetilde H_d(X;F)\ne0\) over a field \(F\), then \(X\) has at least \(2d+2\) vertices; equality forces \(X\) to be the join of \(d+1\) copies of \(S^0\). To prove this, choose a vertex-minimal induced subcomplex with nonzero degree-\(d\) homology. For \(d=0\), it is disconnected and has at least two vertices. For \(d>0\), removal of any vertex \(v\) kills degree-\(d\) homology; the reduced Mayer–Vietoris sequence for the decomposition into the deletion and the cone on \(\operatorname{lk}(v)\) injects its nonzero \(\widetilde H_d\) into \(\widetilde H_{d-1}(\operatorname{lk}(v);F)\). By induction the link has at least \(2d\) vertices. At least one additional vertex fails to be adjacent to \(v\) in the complex's one-skeleton, or the complex would be a cone. Together with \(v\), this gives at least \(2d+2\) vertices. In the equality case every vertex has exactly one nonneighbor, so the one-skeleton's missing edges form a perfect matching, and flagness gives the cross-polytope boundary. Any nonzero integral homology group is detected over some field in the same degree, so this bound applies to integral carriers as well.

**All ten supports and no others.** The five nonzero elements of \(S\) have just one nontrivial linear dependence: their sum is zero. Suppose two edges in an induced matching have distinct directions \(s,t\in S\). In the quotient by the four-element plane \(\langle s,t\rangle\), the other three generators occupy its three distinct nonzero cosets; consequently every coset intersects \(S\). Among the four cross-differences of the two edges, one must therefore belong to \(S\), a contradiction. Every edge of an induced matching must have the same direction \(s\). Upon contracting the eight \(s\)-edges, the remaining four generators project to the four elements of an affine plane not containing zero in \(V/\langle s\rangle\cong\mathbb F_2^3\). The quotient graph is \(K_{4,4}\). Its only independent four-sets are the two bipartition classes. Therefore exactly two induced four-edge matchings exist in each direction, with supports \(W_{s,0}\) and \(W_{s,1}\). For each support, independence sets choose at most one endpoint of each edge, so
\[
K[W_{s,\epsilon}]=(S^0)^{*4}\cong S^3.
\]
The preceding support bound shows that these are all induced carriers on at most eight vertices. The group generated by translations and permutations of the five directions is transitive on the ten supports.

**Integral spanning and the unique relation.** The exact simplex counts in dimensions \(0\) through \(4\) are \((16,80,160,120,16)\). Let \(B_3:C_3(K;\mathbb Z)\to C_2(K;\mathbb Z)\) and \(B_4:C_4(K;\mathbb Z)\to C_3(K;\mathbb Z)\) be the signed simplicial boundaries with the ordering specified above. Let the ten columns of \(Z\) be the fundamental cycles of the ten induced spheres. Then
\[
B_3B_4=0,\qquad B_3Z=0.
\]
The standalone verifier reconstructs these integer matrices and obtains
\[
\operatorname{rank}_{\mathbb F_2}B_3=95,
\qquad \operatorname{SNF}([B_4\mid Z])=\operatorname{diag}(\underbrace{1,\ldots,1}_{25},0).
\]
The latter is a \(120\)-by-\(26\) matrix of rank \(25\) with all nonzero Smith invariant factors equal to one. Since its image lies in \(\ker B_3\), rational rank of \(B_3\) is at most \(120-25=95\); reduction modulo two supplies the reverse bound. Thus \(\ker B_3\) has rank \(25\). The image of \([B_4\mid Z]\) is a primitive rank-\(25\) sublattice of the free group \(C_3\). Since \(\ker B_3\) has the same rank and contains it, these two lattices coincide. Hence the ten sphere cycles span third integral homology, not merely its rationalization.

The same exact calculation gives \(\operatorname{rank}B_4=16\), \(\operatorname{rank}Z=10\), and \(\operatorname{rank}[B_4\mid Z]=25\). Their sole relation is represented, in lexicographic carrier order, by
\[
q=(1,-1,1,-1,1,1,-1,1,-1,1).
\]
In the ordered basis of the sixteen four-simplices, put
\[
t=(1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,1,-1,-1,1).
\]
Then \(B_4t+Zq=0\) exactly over \(\mathbb Z\). Rank \(25\) shows that any rational relation is proportional to this one; since every entry of \(q\) has absolute value one, the integral relation module is \(\mathbb Z q\). Therefore
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{10}/\mathbb Zq\cong\mathbb Z^9.
\]
For each coordinate, the remaining nine standard generators constitute an integral basis because the omitted coefficient of \(q\) is a unit. This proves primitive survival of every minimum sphere and the generation statement.

## Verification
Execute `python3 verify.py` with the versions listed in `requirements.txt`. The program enumerates the complete simplex set; all \(\binom{16}{8}=12870\) eight-vertex restrictions for induced four-edge matchings; the five pairs of affine hyperplanes; the signed integral matrices \(B_3,B_4,Z\); the exact boundary identities and integral relation; a separate bitset Gaussian elimination computing the mod-two rank \(95\); and the Smith invariants of \([B_4\mid Z]\). Expected final lines include `VERIFY_OK FOLDED5_INDEPENDENCE`, `SHORTEST_SPHERES 10`, and `SMITH_BOUNDARIES_PLUS_SPHERES 25 UNIT_FACTORS`. Each conclusion above follows from the reconstruction and integral algebra, not from an unbounded computation or numerical approximation.

## Relationship to prior work
Barmak's triangle-free-graph suspension theorem applies to the folded five-cube but determines neither its third-homology lattice nor the incidence of smallest carriers. Two previously published exact computations of this very independence complex already prove \(K\simeq\bigvee^9S^3\). That ambient homotopy type is credited here: it is not the new finding and cannot alone determine which induced spheres represent a primitive generating set. A published independent-set table gives the same face numbers and Euler characteristic, again without inclusion maps on homology. Brouwer's graph table describes the equivalent folded-cube construction, automorphism group, and parallel classes but does not determine this integral carrier relation. Cioabă and Mim's Clebsch result concerns the first homology of the clique complex of the degree-ten graph and does not determine these degree-three integral inclusion classes.

The contribution is the exact minimal-support classification, structural hyperplane parametrization, and primitive integral presentation by ten shortest induced spheres. The proof does not assert absolute priority over inaccessible or unindexed literature.

## Limitations
The result applies to a single sixteen-vertex graph and degree-three integral homology. It does not classify minimal representatives of arbitrary linear combinations of the nine classes or extend to all folded cubes. The finite Smith-form computation has been reconstructed and executed but not independently audited by a second research group. The mathematical-record and primary-literature search cannot exclude equivalent statements in unindexed sources.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2010-07-02, especially Theorem 3.4. https://arxiv.org/abs/1007.0418.
2. *The Clebsch independence complex is a wedge of nine 3-spheres*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-clebsch-independence-complex-is-a-wedge-of-nine-3-spheres--344f83b86fa0.
3. *The folded five-cube independence complex is a wedge of nine 3-spheres*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-folded-five-cube-independence-complex-is-bigvee-9-s-3--fb89079b9172.
4. A. E. Brouwer, *Clebsch graph*, graph-description table, https://jaanos.github.io/tables/graphs/Clebsch.html.
5. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1, 2026, Proposition 7.7. https://arxiv.org/abs/2606.27328.
6. OEIS A355227 and A355559, folded-cube independence polynomials and their alternating sums, https://oeis.org/A355227 and https://oeis.org/A355559.
