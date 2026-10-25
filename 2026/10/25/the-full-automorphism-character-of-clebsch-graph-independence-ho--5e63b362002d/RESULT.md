# The full automorphism character of Clebsch-graph independence homology

## Finding
Let \(E=\{a\in\mathbb F_2^5:\sum_{i=1}^5a_i=0\}\). Define the 5-regular Clebsch graph \(G\) with vertices \(E\), joining distinct \(x,y\) when their Hamming distance is four. Let \(K=\operatorname{Ind}(G)\) be its ordinary simplicial independence complex. Its full graph automorphism group is \(H=E\rtimes S_5\), with even translations and coordinate permutations.

Write \(\mathrm{Std}=\{(z_1,\ldots,z_5)\in\mathbb Q^5:\sum_i z_i=0\}\) for the standard four-dimensional \(S_5\)-module, \(\mathrm{sgn}\) for the permutation sign module, and \(W=\mathbb Q^5\) with basis \(u_1,\ldots,u_5\) on which \((a,\sigma)\in H\) acts by
\[
(a,\sigma)u_i=\mathrm{sgn}(\sigma)(-1)^{a_{\sigma(i)}}u_{\sigma(i)}.
\]
Here \(E\) acts trivially on \(\mathrm{sgn}\otimes\mathrm{Std}\). Then, as rational representations of the *full* graph automorphism group,
\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong (\mathrm{sgn}\otimes\mathrm{Std})\oplus W.}
\]
All other reduced rational homology groups vanish. Equivalently, for every \(a\in E\) and \(\sigma\in S_5\), letting \(f(\sigma)\) be the number of fixed coordinate positions,
\[
\boxed{\operatorname{tr}((a,\sigma)\mid\widetilde H_3(K;\mathbb Q))
=\mathrm{sgn}(\sigma)\left(f(\sigma)-1+\sum_{i:\sigma(i)=i}(-1)^{a_i}\right).}
\]
In particular, the 16 translation character values are \(9\) at zero, \(5\) for the ten weight-two elements, and \(1\) for the five weight-four elements. The \(E\)-invariant third homology has dimension four, and \(S_5\) acts on it as \(\mathrm{sgn}\otimes\mathrm{Std}\); the full automorphism group fixes no nonzero rational homology class.

## Assumptions and scope
All simplicial complexes are finite and abstract. Coordinates and vector sums in \(E\) are modulo two, and \(\mathbb Q\) has characteristic zero. The semidirect product has multiplication \((a,\sigma)(b,\tau)=(a+\sigma b,\sigma\tau)\). The stated graph is the degree-five Clebsch graph, not the degree-ten complementary graph, which is sometimes given the same name. The underlying nonequivariant homotopy equivalence \(K\simeq\bigvee^9 S^3\) was established previously; it is used as a premise, not claimed here as new. The new assertion is the explicit nine-dimensional representation and full character.

## Proof
**1. Complete symmetry group.** Translations by \(E\) and permutations of the five coordinates preserve the distance-four adjacency relation and form a subgroup \(E\rtimes S_5\) of order \(16\cdot120=1920\). Every vertex has five neighbors. The graph has parameters \((16,5,0,2)\): each pair of distinct nonadjacent vertices has exactly two common neighbors. Once an automorphism fixes the zero vertex, its permutation of those five neighbors determines the other ten vertices, since they correspond bijectively to the ten unordered pairs of zero's neighbors through their respective two common neighbors. Hence the vertex stabilizer has order at most \(5!\), so the exhibited subgroup is the whole group.

**2. Homological concentration.** Enumerating all \(2^{16}-1\) nonempty subsets of \(E\) and rejecting those containing a distance-four pair gives the complete face vector \((16,80,160,120,16)\), totaling 392 simplices. Label the even-weight five-bit vectors numerically in increasing order. Repeatedly toggle the smallest available vertex in this order, pairing each remaining face not containing that vertex with its extension when both remain unmatched, and remove the pair. This deterministic rule creates exactly 191 disjoint cover pairs. Of the ten critical faces, one is a vertex and nine are tetrahedra (three-dimensional simplices). Directing matched covers upwards and all unmatched covers downwards yields a directed graph on 392 simplices with exactly 1,200 incidences. An exhaustive topological sort visits every simplex and proves acyclicity. Discrete Morse theory gives \(K\simeq\bigvee^{9}S^3\), thereby establishing \(\widetilde H_j(K;\mathbb Q)=0\) for \(j\ne3\) and \(\dim\widetilde H_3(K;\mathbb Q)=9\). This recovers the previously known nonequivariant prerequisite by an executable check.

**3. Character calculation.** For any group element \(g=(a,\sigma)\), the signed simplicial Lefschetz formula gives
\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=1+\sum_{\varnothing\ne F\in K:\,gF=F}(-1)^{|F|}\,\operatorname{sgn}(g\mid F),
\]
where \(\operatorname{sgn}(g\mid F)\) is the sign of the permutation induced by \(g\) on the vertices of a setwise invariant face \(F\). The extra \(1\) accounts for the empty face in the reduced chain complex; the overall sign is fixed by degree-three homology occurring in odd dimension. Every invariant face is a union of entire orbits of \(g\) on the graph vertices, and each included orbit contributes \(-1\) to the summand after incorporating its simplex sign. Thus the same trace equals the independence polynomial at \(-1\) of the graph of admissible vertex orbits, with edges representing conflicts between two orbits.

The standalone verifier performs two logically different finite calculations for **each of the 1,920 elements**: (i) the signed fixed-face sum above and (ii) independent-set deletion recursion on the orbit-conflict graph. It finds equality of these quantities with the explicit formula
\[
\mathrm{sgn}(\sigma)\left(f(\sigma)-1+\sum_{i:\sigma(i)=i}(-1)^{a_i}\right)
\]
for each element, not merely for a sample of conjugacy classes. Consequently this is the full character of the third reduced rational homology representation.

**4. Identification of the representation.** The \(S_5\)-module \(\mathrm{sgn}\otimes\mathrm{Std}\), inflated to \(H\), has trace \(\mathrm{sgn}(\sigma)(f(\sigma)-1)\). The signed coordinate module \(W\) has trace \(\mathrm{sgn}(\sigma)\sum_{i:\sigma(i)=i}(-1)^{a_i}\). Their direct sum therefore has the observed character on every group element. Since finite-dimensional rational representations of a finite group in characteristic zero are semisimple, equality of characters proves the displayed isomorphism. The \(E\)-fixed submodule is precisely \(\mathrm{sgn}\otimes\mathrm{Std}\), since the five distinct coordinate characters of \(E\) occurring in \(W\) are all nontrivial. The standard \(S_5\)-module has no sign subrepresentation, hence there are no \(H\)-fixed vectors.

## Verification
Execute `python3 verify.py` using Python 3 with no nonstandard packages. The program constructs the entire graph and all faces, checks the strongly regular parameters, validates the matching and directed acyclicity, and independently checks mod-two simplicial boundary ranks \((15,65,95,16)\). It then enumerates all \(120\) coordinate permutations and all \(16\) translations, recomputing each homological trace in two different ways and comparing it with the formula. The supplied `verification_output.txt` records an actual successful execution ending in `VERIFY_OK`. Reexecuting the file in the embedded package reproduces this output.

## Relationship to prior work
J. A. Barmak's *Star clusters in independence complexes of graphs* proves that the independence complex of a triangle-free graph is a suspension; it does not compute the automorphism action on homology for the Clebsch graph. Two existing exact-graph homotopy calculations establish the nonequivariant equivalence \(\operatorname{Ind}(G)\simeq\bigvee^9 S^3\) (and the known face vector), but neither gives the \(1920\)-element group character or the decomposition above. Previously determined translation characters for *neighborhood complexes* of odd folded cubes address a different complex and do not imply this independence-complex representation. The original Greenwood–Gleason graph construction and work on automorphisms of folded cubes identify the object and symmetry, not its homological action. Targeted literature and indexed-result comparisons under Clebsch, Greenwood–Gleason, folded five-cube, projective cube, translation, and full-equivariant character aliases uncovered no implication covering the character formula. An unindexed equivalent remains a potential risk.

## Limitations
The proof is a finite exact enumeration for the degree-five Clebsch graph. It neither asserts a uniform formula for higher folded cubes nor determines integral equivariant stable homotopy, fixed-point spaces or equivariant cellular attaching maps. The rational representation assertion rests on standard semisimplicity and the fully enumerated simplicial character. Computational checks are reproducible but have not undergone independent external audit. Search results cannot rule out an equivalent calculation in unindexed sources.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, publicly posted 2010-07-02, especially Theorem 3.4. https://arxiv.org/abs/1007.0418
2. R. E. Greenwood and A. M. Gleason, *Combinatorial Relations and Chromatic Graphs*, Canadian Journal of Mathematics 7 (1955), 1–7, DOI 10.4153/CJM-1955-001-4.
3. S. Schmidt, *Quantum automorphisms of folded cube graphs*, arXiv:1810.11284, especially the folded-cube Cayley-graph construction. https://arxiv.org/abs/1810.11284
4. *The Clebsch independence complex is a wedge of nine 3-spheres*, published mathematical research record, identifier `2026/10/11/SCOPE-the-clebsch-independence-complex-is-a-wedge-of-nine-3-spheres--344f83b86fa0`.
5. *The folded five-cube independence complex is a wedge of nine 3-spheres*, published mathematical research record, identifier `2026/10/11/SCOPE-the-folded-five-cube-independence-complex-is-bigvee-9-s-3--fb89079b9172`.
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI 10.1006/aima.1997.1650.
