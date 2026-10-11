# The two exceptional five-vertex blocks of \(Q_{5,3}\) are its unique square-nonzero cosystolic carriers
## Finding
Let \(K=Q_{{5,3}}\) be the 15-vertex degree-regular triangulation of the Klein bottle defined by Datta--Upadhyay. For each nonzero class \(\xi\in H^1(K;\mathbf F_2)\), define
\[
w(\xi)=\min\{{|\operatorname{{supp}} z|:z\in Z^1(K;\mathbf F_2),\ [z]=\xi\}},
\]
let \(m(\xi)\) count the minimizing cocycles, and set
\[
q(\xi)=\langle\xi\smile\xi,[K]\rangle\in\mathbf F_2.
\]
The three nonzero classes have exactly the profiles
\[
(w,m,q)=(5,1,1),\qquad(5,1,1),\qquad(10,1,0).
\]
The unique nonzero class with square zero is the first Stiefel--Whitney class \(w_1(K)\). Its unique minimum representative has ten edges and is the disjoint union of the two unique weight-five representatives.

The two weight-five supports are the simple edge cycles
\[
u_{{1,1}}-v_{{1,1}}-u_{{2,1}}-v_{{2,1}}-u_{{3,1}}-u_{{1,1}}
\]
and
\[
u_{{1,3}}-v_{{1,2}}-u_{{2,3}}-v_{{2,2}}-u_{{3,3}}-u_{{1,3}}.
\]
Their vertex carriers are precisely the two five-vertex sets that Datta--Upadhyay single out as the two \(C_5\) components of \(G_4(\mathrm{{EG}}(Q_{{5,3}}))\).

## Assumptions and scope
The complex is the specialization \(m=2,n=3\) of Datta--Upadhyay Example 7. Their formula gives 15 vertices, 45 edges, and 30 triangles, and their paper identifies this complex as a degree-regular Klein-bottle triangulation. All cochains and cup products here use coefficients in \(\mathbf F_2\). Edge-support weight means ordinary Hamming weight on the 45 simplicial edges.

The statement is about this labeled simplicial complex and its intrinsic cohomology classes. It does not assert a formula for all \(Q_{{2m+1,n}}\), nor does it identify a geometric metric systole.

## Proof
Reconstruct the 30 facets directly from Example 7. Every edge occurs in exactly two triangles. The 30 triangle cocycle equations over \(\mathbf F_2\) have rank 29, so
\[
\dim Z^1(K;\mathbf F_2)=45-29=16.
\]
The vertex coboundaries have rank 14 because the one-skeleton is connected. Therefore
\[
\dim H^1(K;\mathbf F_2)=16-14=2.
\]

There are exactly \(2^{{16}}=65{,}536\) simplicial one-cocycles. Exhausting all of them and reducing modulo the rank-14 coboundary space gives four cohomology classes, each with \(2^{{14}}\) representatives. The three nonzero classes have minimum-support data
\[
(5,1),\qquad(5,1),\qquad(10,1).
\]
Thus all three minima and their uniqueness are exhaustive statements, not sampling results.

For increasing vertices \(a<b<c\), use the Alexander--Whitney formula
\[
(\alpha\smile\beta)(abc)=\alpha(ab)\beta(bc)
\]
and evaluate on the mod-two fundamental cycle given by the sum of all 30 triangles. The two weight-five classes have cup square 1, while the weight-ten class has cup square 0. For a closed surface, the degree-one Wu identity is
\[
\langle w_1(K)\smile x,[K]\rangle=\langle x\smile x,[K]\rangle
\]
for every \(x\in H^1(K;\mathbf F_2)\). Checking the four cohomology classes against this identity selects the weight-ten class uniquely as \(w_1(K)\).

The two weight-five supports are disjoint, their sum is exactly the unique minimizing cocycle in the \(w_1(K)\) class, and each support is a simple five-cycle. Their vertex sets are
\[
\{{u_{{1,1}},u_{{2,1}},u_{{3,1}},v_{{1,1}},v_{{2,1}}\}}
\]
and
\[
\{{u_{{1,3}},u_{{2,3}},u_{{3,3}},v_{{1,2}},v_{{2,2}}\}}.
\]
Datta--Upadhyay list exactly these two sets as the vertex sets of the two \(C_5\) components in \(G_4(\mathrm{{EG}}(Q_{{5,3}}))\).

## Verification
Run `python3 verify.py`. The checker uses only the Python standard library. It reconstructs the facet set from the published all-parameter formula, verifies the closed-surface incidence condition, performs exact mod-two row reduction, exhausts all 65,536 one-cocycles, computes every class minimum and cup square, identifies \(w_1(K)\) from the Wu identity, and checks the two five-cycle supports and their carrier sets.

The packaged replay reports `VERIFY_OK`, with cocycle-equation rank 29, coboundary rank 14, \(\dim H^1=2\), nonzero profile `(5,1,1),(5,1,1),(10,1,0)`, and `w1_is_disjoint_union_of_weight5_supports=yes`.

## Relationship to prior work
Datta--Upadhyay define \(Q_{{5,3}}\), prove that it triangulates the Klein bottle, and use two distinguished five-vertex blocks to analyze its failure of weak regularity. Their exact-object discussion gives the two \(C_5\) carrier sets used above, but it does not compute simplicial cohomology support minima, cup-square strata, or the first Stiefel--Whitney cosystole. Full-text searches of the source for `cohomology`, `cocycle`, `Stiefel`, and `dual` return no such treatment.

Targeted searches under the exact \(Q_{{5,3}}\) label, degree-regular Klein-bottle terminology, cocycle-support/cosystole terminology, cup-square language, and first Stiefel--Whitney language found no publication stating this profile or the carrier identification. The closest general literature on triangulation width concerns noncontractible primal cycles rather than minimum supports of cohomology representatives.

## Limitations
The exhaustive result is finite and specific to \(Q_{{5,3}}\); it does not prove an all-parameter formula for the Datta--Upadhyay family. The identification of the complex and of the two distinguished five-vertex carrier sets relies on the published source, while the cohomology computation is independently reconstructed from its facet formula. As with any literature search, an obscure or unindexed historical computation under different terminology remains a residual originality risk.

## References
B. Datta and A. K. Upadhyay, “Degree-regular triangulations of torus and Klein bottle,” arXiv:math/0403433v1, first submitted 25 March 2004. Example 7 defines \(Q_{{2m+1,n}}\); the discussion following it identifies the two exceptional five-vertex blocks of \(Q_{{5,3}}\).
