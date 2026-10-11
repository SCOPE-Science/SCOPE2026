# Thirteen of fifteen empty-triangle orbits are mod-three systolic in the 14-vertex cyclic lens space

## Finding

In the 14-vertex transitive cyclic triangulation \(K\) of \(L(3,1)\) with difference cycles \((1:1:1:11),(1:2:4:7),(1:4:2:7),(1:4:7:2),(2:4:4:4),(2:5:2:5)\), the 210 empty triangles split into 15 cyclic translation orbits. Exactly 13 orbits, containing 182 triangles, represent nonzero classes in \(H_1(K;\mathbf F_3)\); exactly two orbits, represented by cyclic gap triples \((1:5:8)\) and \((3:6:5)\), are null-homologous. Thus the 182 essential empty triangles are precisely the length-three simple cycles with nonzero mod-three homology, so the mod-three combinatorial homology systole is 3. Translation by one vertex acts as multiplication by \(-1\) on \(H_1(K;\mathbf F_3)\), and every essential 14-orbit contains seven cycles in each of the two nonzero homology classes.

## Assumptions and scope

Vertices are \(\mathbb Z/14\mathbb Z\). A four-entry difference cycle \((a:b:c:d)\), with entries summing to 14, denotes the translation orbit of the tetrahedron \(\{0,a,a+b,a+b+c}\). The six published difference cycles generate a simplicial complex \(K\) with face vector \((14,91,154,77)\). The cited classification identifies this complex as a triangulation of \(L(3,1)\).

An empty triangle is a three-vertex set whose three edges occur in \(K\) but which is not itself a two-simplex. Because the one-skeleton is complete, every three-vertex set is a three-edge simple cycle, and exactly 210 of the \(\binom{14}{3}=364\) triples are empty.

The homological statements use coefficients in \(\mathbf F_3\). The claimed systole is therefore the minimum number of edges in a simple cycle representing a nonzero class in \(H_1(K;\mathbf F_3)\); no claim is made about weighted metrics or about other coefficient fields.

## Proof

Orient each edge from \(i\) to \(j\) and define an \(\mathbf F_3\)-valued one-cochain by
\[
w(i,j)=(-1)^i q_{j-i\bmod 14},
\]
where
\[
(q_1,\ldots,q_{13})=(1,0,1,1,0,1,0,2,0,2,1,0,1).
\]
Antisymmetry holds, and direct substitution on all 154 triangular faces gives zero coboundary. Hence \(w\) is a cocycle. The boundary of the empty triangle \(\{0,1,4}\) evaluates to \(2\), so \(w\) is not a coboundary.

Exact row reduction of the simplicial boundary maps over \(\mathbf F_3\) gives
\[
\operatorname{rank}\partial_1=13,\qquad
\operatorname{rank}\partial_2=77,
\]
and therefore
\[
\dim_{\mathbf F_3}H_1(K;\mathbf F_3)=91-13-77=1.
\]
Thus \(w\) detects the unique nonzero one-dimensional mod-three homology direction.

Evaluating \(w\) on all 210 empty triangles gives 28 with value zero, 91 with value one, and 91 with value two. Translation partitions the empty triangles into 15 orbits of size 14. The 28 null-homologous triangles are exactly two full orbits, represented by the cyclic gap triples \((1:5:8)\) and \((3:6:5)\). Each of the remaining 13 orbits has seven evaluations equal to one and seven equal to two.

Finally,
\[
w(i+1,j+1)=-w(i,j)
\]
for every oriented edge, with indices taken modulo 14. Since \(H^1(K;\mathbf F_3)\) is one-dimensional, translation acts by \(-1\) on cohomology and therefore also by \(-1\) on \(H_1(K;\mathbf F_3)\). A simple cycle in a simplicial one-skeleton has at least three edges, and the 182 detected empty triangles attain this lower bound. They are therefore exactly the shortest mod-three homologically nontrivial simple cycles.

## Verification

The accompanying `verify.py` reconstructs the complex solely from the six difference cycles, checks the face vector and the two boundary ranks over \(\mathbf F_3\), verifies the displayed cocycle on all triangular faces, enumerates all 210 empty triangles, constructs all cyclic translation orbits, checks the two null-orbit gap types, and verifies the translation sign action. Its expected final line is:

`VERIFY_OK f=14,91,154,77 H1_F3=1 empty3=210 essential3=182 null3=28 essential_orbits=13 null_orbits=2 null_gaps=1:5:8,3:6:5 classes=91,91 translation=-1 systole=3`

## Relationship to prior work

Spreer's classification gives this 14-vertex cyclic triangulation, its six difference cycles, its topological type \(L(3,1)\), and primary classification 57Q15. The paper attributes the complex to the earlier Kühnel--Lassmann classification. The inspected full text does not state an empty-triangle homology decomposition, a count of shortest mod-three cycles, or the two exceptional null-homologous triangle orbits.

Kowalick, Lafont, and Minemyer define the broader notion of combinatorial systole as the length of a shortest homotopically nontrivial loop in a triangulation. That framework motivates the invariant but does not determine the object-specific 182-cycle spectrum above.

## Limitations

The result concerns one named 14-vertex cyclic triangulation and mod-three homology. It does not classify shortest cycles in every triangulation of \(L(3,1)\), and it does not assert an analogous orbit decomposition over other coefficient fields. The 1985 Kühnel--Lassmann article is a plausible place for older object-specific computations; available bibliographic material was inspected, but its full text was not available in the materials checked here. This leaves a residual originality risk, although no searched statement or indexed result was found that gives the 13-versus-2 orbit decomposition or the 182-cycle count.

## References

1. Jonathan Spreer, “Combinatorial 3-manifolds with transitive cyclic symmetry,” arXiv:1112.0940, first submitted 2011-12-05; later published in *Discrete & Computational Geometry* 51 (2014), 394–426.
2. Wolfgang Kühnel and Gunter Lassmann, “Neighborly combinatorial 3-manifolds with dihedral automorphism group,” *Israel Journal of Mathematics* 52 (1985), 147–166, DOI 10.1007/BF02776088.
3. Ryan Kowalick, Jean-François Lafont, and Barry Minemyer, “Combinatorial systolic inequalities,” arXiv:1506.07121.
