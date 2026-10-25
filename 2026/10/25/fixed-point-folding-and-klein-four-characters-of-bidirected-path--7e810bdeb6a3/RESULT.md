# Fixed-point folding and Klein-four characters of bidirected-path multipath complexes

## Finding

For each integer \(n\geq2\), let \(B_n\) be the directed path on vertices \(0,1,\ldots,n\) containing both arrows between consecutive vertices. Let \(X_n\) be its multipath simplicial complex: a face is a set of arrows whose spanning directed graph is a disjoint union of directed simple paths and isolated vertices. Set \(X_0\) to be the complex with only the empty face, whose geometric realization is empty. Define commuting involutions \(R\) and \(T\) of \(X_n\) by, respectively, the endpoint reversal \(i\mapsto n-i\) and simultaneous reversal of every arrow. They generate a faithful action of \(C_2\times C_2\) for \(n\geq2\).

**Fixed-point folding theorem.** As geometric polyhedra, not merely up to homotopy,
\[
|X_n|^R\cong |X_{\lfloor(n-1)/2\rfloor}|,\qquad
|X_n|^T=\varnothing,\qquad
|X_n|^{RT}\cong|X_{\lceil n/2\rceil}|.
\]
The homeomorphisms arise from explicit simplicial identifications after replacing each permitted involution orbit of arc-vertices by its barycenter.

**Complete integral character.** Let \(d=\lfloor(n-1)/2\rfloor\). The previously established nonequivariant equivalence \(X_n\simeq S^d\) implies that the only nonzero reduced integral homology group is \(\widetilde H_d(X_n;\mathbb Z)\cong\mathbb Z\). On this lattice,
\[
R_*=(-1)^{\lfloor(n+3)/4\rfloor},\qquad
T_*=(-1)^{d+1},\qquad (RT)_*=R_*T_*.
\]
This determines the whole \(\mathbb Z[C_2\times C_2]\)-module. In particular, the full symmetry quotient is rationally acyclic in reduced homology unless \(n\equiv0,7\pmod8\); in those two classes its unique nonzero reduced rational homology group is \(\mathbb Q\) in degree \(d\).

The new statements are the fixed-point identifications, the integral action, and the quotient criterion. The nonequivariant sphere equivalence is prior work, not a novelty claim.

## Assumptions and scope

Everything is finite and simplicial, with \(n\geq2\) and no multiple arrows in one direction. An allowed multipath component has indegree and outdegree at most one at each vertex and has no directed cycle; in this path family the only potential directed cycles are two-arrow reversals of a single undirected edge. An arc of \(B_n\) is a vertex of \(X_n\). The involution \(T\) is a simplicial symmetry because it reverses each directed path, even though it is an arrow-reversing anti-automorphism of the directed graph. Both involutions preserve allowed arrow sets and commute. Their action on oriented simplicial chains uses the usual vertex-permutation signs. Quotient homology is taken with rational coefficients, while the representation statement is integral.

## Proof

**1. Identify the conflict graph.** Denote the forward and backward arrows on undirected edge \(i\)--\(i+1\) by \(f_i\) and \(b_i\). Two arrows conflict exactly when they form a reverse pair \(\{f_i,b_i\}\) or one of the pairs \(\{f_i,b_{i+1}\}\) and \(\{b_i,f_{i+1}\}\). Indeed, these are precisely the potential two-cycle, double-incoming, and double-outgoing obstructions. No longer directed cycle can occur on an undirected tree; conversely, if all displayed conflicts are absent, every vertex has indegree and outdegree at most one and the selected graph is a disjoint union of directed paths.

For each column \(i\), define two vertices \((i,0),(i,1)\) by \((i,0)=f_i\), \((i,1)=b_i\) when \(i\) is even, and interchange those assignments when \(i\) is odd. Then the conflicts become precisely the rungs \(\{(i,0),(i,1)\}\) and rail edges \(\{(i,a),(i+1,a)\}\). Thus there is an explicit simplicial isomorphism
\[
X_n\cong\operatorname{Ind}(P_n\square K_2),
\]
where \(P_n\) has \(n\) vertices, and \(\operatorname{Ind}\) denotes the ordinary independence complex. In these coordinates, \(T(i,a)=(i,1-a)\), while
\[
R(i,a)=\begin{cases}(n-1-i,a),&n\text{ even},\\(n-1-i,1-a),&n\text{ odd}.
\end{cases}
\]

**2. Fixed-point-orbit complexes.** For a simplicial involution \(g\), every fixed geometric point has equal barycentric coordinates on all vertices of each \(g\)-orbit. A two-element orbit may occur in its support only if the two vertices are nonadjacent. The permitted orbits form a simplicial complex: a collection of permitted orbits is a face exactly when its union is an independent set in the ladder. The barycenter map gives a homeomorphism of this orbit complex onto \(|X_n|^g\).

There are two kinds of column reflection of the ladder. A row-preserving reflection \(c\) reverses the columns but not the lanes. For \(n=2m\), both orbits through the two central adjacent columns contain a rail edge and are excluded; all remaining permitted column-orbits have the rung-and-rail conflicts of a ladder of length \(m-1\). For \(n=2m+1\), the two middle-column vertices are individually fixed and are allowed separately; with the \(m\) paired column-orbits, they form a ladder of length \(m+1\). A row-interchanging column reflection \(s\) has, for \(n=2m\), precisely \(m\) permitted pairs of column-orbits, including the two central diagonally paired orbits, forming a length-\(m\) ladder. For \(n=2m+1\), the middle rung is one invalid swapped orbit and the remaining orbits form a length-\(m\) ladder. These statements follow directly by checking that orbit-pair conflicts are exactly rung conflicts within a quotient column and rail conflicts between adjacent quotient columns; no longer-range conflicts exist.

When \(n\) is even, \(R=c\) and \(RT=s\); when \(n\) is odd, \(R=s\) and \(RT=c\). Hence \(R\) always folds to a ladder of length \(\lfloor(n-1)/2\rfloor\) and \(RT\) to one of length \(\lceil n/2\rceil\). Every \(T\)-orbit is a rung, so no nonempty invariant face exists and \(|X_n|^T\) is empty. Step 1 converts the quotient ladders back into the asserted smaller multipath complexes, establishing all three homeomorphisms, including the empty \(X_0\) boundary case.

**3. Signed fixed-face Lefschetz calculation.** Let \(g\) be any of these involutions, and let \(K_g\) be its orbit complex from Step 2. The reduced Lefschetz number on augmented simplicial chains is
\[
\widetilde L(g;X_n)=-\sum_{F\in K_g}(-1)^{|F|}=\widetilde\chi(K_g).
\]
Here the sum includes the empty face: an invariant face with \(q\) selected vertex-orbits has signed oriented-chain contribution \((-1)^{q-1}\), independently of how many selected orbits have two elements. By Caputi--Collari--Smith, Proposition 2.2, \(X_j\simeq S^{\lfloor(j-1)/2\rfloor}\) for \(j\geq1\), and \(|X_0|\) is empty. Therefore, for all \(j\geq0\), define
\[
E(j)=\widetilde\chi(X_j)=(-1)^{\lfloor(j-1)/2\rfloor};
\]
for \(j=0\) the exponent is \(-1\), giving \(E(0)=-1\), the augmented empty-complex value. Step 2 yields
\[
\widetilde L(R)=E(\lfloor(n-1)/2\rfloor),\qquad
\widetilde L(T)=-1,\qquad
\widetilde L(RT)=E(\lceil n/2\rceil).
\]
The single nonzero reduced integral homology group of \(X_n\) lies in degree \(d\). Thus each signed Lefschetz number equals \((-1)^d\) times the integer degree of the corresponding automorphism. Evaluating the floor functions in the eight residue classes gives \(R_*=(-1)^{\lfloor(n+3)/4\rfloor}\) and \(T_*=(-1)^{d+1}\). The identity \((RT)_*=R_*T_*\) holds integrally because the involutions commute as chain maps. This determines every element of the Klein four action on \(\widetilde H_d(X_n;\mathbb Z)\).

**4. Rational quotients.** After equivariant barycentric subdivision, the rational cellular chains of the quotient of a finite simplicial \(G\)-complex are the coinvariants of the original chains. Averaging over finite \(G\) makes coinvariants and invariants canonically isomorphic over \(\mathbb Q\), with homology commuting with invariants. Consequently
\[
\widetilde H_*(|X_n|/(C_2\times C_2);\mathbb Q)
\cong\widetilde H_*(X_n;\mathbb Q)^{C_2\times C_2}.
\]
The rank-one representation has a nonzero fixed vector exactly when both displayed generators act by \(+1\). The two congruence conditions intersect precisely at \(n\equiv0,7\pmod8\), proving the quotient assertion. In particular, the arrow-reversal action is free on \(|X_n|\), and has the antipodal orientation sign \((-1)^{d+1}\), whether or not any chosen model for \(|X_n|\) is an actual geometric sphere.

## Verification

The accompanying standalone `verify_fold.py` constructs all directed arcs directly, checks the multipath criterion from in/out degrees and opposite arrows, independently constructs the pairwise conflict graph, and verifies its exact isomorphism with a ladder. For each integer \(2\leq n\leq10\), it constructs all involution orbits and their conflict graphs and confirms, for all three nonidentity symmetries, the claimed quotient ladder widths. For \(2\leq n\leq9\), it independently enumerates every arrow subset and directly evaluates the three signed simplicial Lefschetz numbers. For \(2\leq n\leq7\), it calculates full reduced mod-two Betti vectors from exact boundary ranks and checks a single generator in the asserted degree. All finite tests passed; the script output is included separately as `verify_fold_output.txt`. The all-parameter proof is above and uses the established integral homotopy theorem, not an inference from finitely many examples.

## Relationship to prior work

Caputi, Collari and Smith (arXiv:2601.05670v1, first publicly posted 2026-01-09) establish the nonequivariant sphere homotopy type of bidirected linear multipath complexes in Proposition 2.2; their paper does not state the three fixed-point homeomorphisms or the Klein-four action. Their discussion of bidirected polygons concerns different graphs.

Carnero Bravo (arXiv:2505.06457v1) studies independence complexes of graph products and their nonequivariant homotopy types, but does not determine this reflection-and-lane-swap representation. Existing published character computations for *circular* ladder independence complexes concern \(\operatorname{Ind}(C_n\square K_2)\), not the *open* ladder \(\operatorname{Ind}(P_n\square K_2)\); neither a graph isomorphism nor a representation-preserving homology equivalence between those two families has been established, and the sphere-multiplicity patterns differ. Published path-reversal results for **strong discrete Morse matching complexes** concern incidence-matching complexes defined by longer forbidden word patterns, not the multipath complexes here. A published dihedral character computation for bidirected polygons uses folding to paths as an intermediate step but does not state the intrinsic path symmetries or their fixed-point topology.

The general observation that geometric fixed points correspond to permitted vertex-orbits is standard. The claimed contribution is the uniform **identification of all three orbit complexes**, their resulting integral representation, and the exact symmetry-quotient threshold for this natural family.

## Limitations

No new nonequivariant sphere classification is asserted. The result concerns the specified natural \(C_2\times C_2\) action, not the full abstract automorphism group of every exceptional small complex. The quotient result is rational; it does not determine integral homology of the quotient or prove a genuine equivariant sphere equivalence. Finite verification is corroborative only. An unindexed prior calculation of an equivalent symmetry action cannot be categorically excluded.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (2026-01-09), Definitions 1.1--1.2 and Proposition 2.2. https://arxiv.org/abs/2601.05670
2. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v1 (2025-05-09), Sections 1--3. https://arxiv.org/abs/2505.06457
3. *Complete dihedral and layer-swap homology representations of circular ladders*, publicly available mathematical result (2026); the circular graph \(C_n\square K_2\) is not the open ladder in this theorem.
4. *Path reversal has a mod-eight orientation character on strong Morse matching complexes*, publicly available mathematical result (2026); its underlying forbidden-pattern complex differs from the multipath complex.
5. *Dihedral rational homology of bidirectional-polygon multipath complexes*, publicly available mathematical result (2026); its graph is a cycle, not a path.
