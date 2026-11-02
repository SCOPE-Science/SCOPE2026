# Rotation-trivial integral homology of the seven-cycle four-color independence complex

## Finding

Let \(G=C_7\times K_4\) be the categorical graph product, with vertex set \(\mathbb Z/7\mathbb Z\times\{0,1,2,3\}\), and edges between \((i,a)\) and \((j,b)\) exactly when \(i-j\equiv\pm1\pmod 7\) and \(a\ne b\). Write \(X=\operatorname{Ind}(G)\). The cycle rotation \(r(i,a)=(i+1,a)\) generates an order-seven action on \(X\).

**Theorem.** The entire rotation subgroup acts as the identity on integral homology. More explicitly,
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&j=3,\\
\mathbb Z^6,&j=4,\\
0,&j\notin\{3,4\},
\end{cases}
\qquad
r_*|_{\widetilde H_j(X;\mathbb Z)}=\operatorname{id}
\quad\text{for all }j.
\]
Consequently \(X/C_7\) has the same *rational* Betti numbers as \(X\):
\[
\widetilde H_j(X/C_7;\mathbb Q)\cong
\begin{cases}
\mathbb Q^3,&j=3,\\
\mathbb Q^6,&j=4,\\
0,&\text{otherwise.}
\end{cases}
\]

## Assumptions and scope

The independence complex contains one simplex for every nonempty independent vertex set; the augmented simplicial chain complex additionally has its empty face in degree \(-1\). Homology is simplicial homology of its geometric realization. The symmetry considered is the cyclic order-seven rotation of the first graph coordinate, **not** the full dihedral/color-permutation automorphism group. The action is not assumed free on the realization.

## Proof

**Integral homology.** Enumerate the independent sets of the explicitly defined graph by including the least remaining candidate vertex and deleting its graph neighbors. There are exactly \(36,069\) faces including the empty face, with counts by cardinality \(0,\ldots,12\) equal to
\[
(1,28,294,1512,4291,7420,8680,7228,4270,1764,490,84,7).
\]
In the augmented face poset, sequentially for vertex indices \(0,1,\ldots,27\), match each still-unmatched face not containing that vertex with its still-unmatched coface obtained by adding it. The result has \(18,024\) matched pairs and exactly nine critical dimension-three cells and twelve critical dimension-four cells, with no other critical cells. This is an acyclic matching: orient every unmatched cover relation downward and every matched one upward; an exhaustive topological ordering of all \(36,069\) faces and all \(218,036\) cover relations exists, as reproduced by the accompanying checker. Hence integral algebraic discrete Morse theory applies.

To compute its differential, if a three-face \(\sigma\) is the lower member of a matched pair \((\sigma,\tau)\), replace it by \(-[\tau:\sigma]^{-1}\sum_{\sigma'\ne\sigma}[\tau:\sigma']\sigma'\), where the coefficients are the usual signed simplicial incidence numbers. Critical three-faces project to their own basis vectors and upper-matched three-faces project to zero. Acyclicity makes this recursion well-defined. Applying it to each of the twelve critical four-cell boundaries gives the exact \(12\times9\) integer Morse boundary matrix. Its Smith normal form has six unit diagonal entries and three zero entries; in particular it has rank six and no torsion invariant factors. Therefore the only reduced integral homology is free of ranks \(9-6=3\) and \(12-6=6\), in degrees three and four, respectively.

**Rotation characters.** For any nonidentity \(r^s\) with \(1\le s\le6\), every vertex orbit has seven elements, consisting of all seven cycle positions in one fixed color. An invariant nonempty independent set is necessarily a union of these color orbits, and two distinct color orbits cannot coexist in an independent set because they include adjacent cycle positions of unequal colors. Thus there are exactly four \(r^s\)-invariant nonempty simplices: the seven vertices of each individual color. Each has dimension six and its induced vertex permutation is a seven-cycle, which is orientation preserving. The reduced simplicial Lefschetz number is therefore \(4-1=3\).

The rational irreducible representations of \(C_7\) consist of the one-dimensional trivial module and a single six-dimensional cyclotomic module, whose trace at any nonidentity element is \(-1\). Since \(\widetilde H_3(X;\mathbb Q)\) has dimension three, it must be three trivial copies. The Lefschetz identity then forces the nonidentity trace on degree-four homology to equal six, ruling out the cyclotomic six-dimensional module. Hence \(r^s\) acts identically in both rational homology degrees. Both integral groups are free, and \(\operatorname{GL}_d(\mathbb Z)\hookrightarrow\operatorname{GL}_d(\mathbb Q)\) is injective, so the integral action is also the identity.

Finally, for a finite group acting simplicially on a finite complex, rational homology of the geometric quotient equals the invariant rational homology of the original complex (for example, by barycentric subdivision and averaging). The asserted quotient groups follow.

## Verification

Run `python CHECKER.py` with Python 3 and SymPy available. The standalone script constructs the graph and all independent sets, checks all cover relations and the global matching acyclicity, computes the full reduced integral Morse boundary and its Smith normal form, and independently enumerates rotation-invariant oriented simplices for each of the six nonidentity rotations. Expected final status: `C7_K4_ROTATION_INTEGRAL_MORSE_OK`. Exact arithmetic, not floating-point ranks, is used throughout.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (2023) study the homotopy types and homology of categorical products of cycles with complete graphs; their Section 3 includes the seven-cycle, four-color case and reports nontrivial free homology in two neighboring degrees, but does not identify the cyclic action on these groups. A later publicly indexed calculation establishes the integral nonequivariant sphere-wedge decomposition \(\bigvee^3S^3\vee\bigvee^6S^4\) for the same complex. The assertion here concerns the **integral rotation representation**, determined by an oriented fixed-face Lefschetz computation and exact torsion-free Morse calculation; neither the nonequivariant homology ranks nor a wedge decomposition by themselves imply that representation.

## Limitations

The theorem concerns this single natural graph and this specific cyclic symmetry group; it does not establish actions of color permutations or reflections, integral quotient homology, integral quotient torsion, or equivariant homotopy triviality. The exact finite Morse certificate is a proof for the stated finite complex, not a parameter-uniform classification of all cycle/complete-graph products. An unindexed equivalent symmetry computation remains a bibliographic possibility.

## References

1. O. Antolín Camarena and A. Carnero Bravo, Homotopy type of the independence complex of some categorical products of graphs, arXiv:2307.12401, version 1, July 23, 2023.
2. Public mathematical record, *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors* (2026), establishing the nonequivariant homotopy type.
3. Standard simplicial Lefschetz trace identity, algebraic discrete-Morse cancellation, and rational transfer for finite group quotients.
