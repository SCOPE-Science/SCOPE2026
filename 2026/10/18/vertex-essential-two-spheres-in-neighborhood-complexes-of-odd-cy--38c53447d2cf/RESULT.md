# Vertex-essential two-spheres in neighborhood complexes of odd-cycle Mycielskians

## Finding

For every odd integer \(n\geq5\), let \(G_n=\mu(C_n)\) be the ordinary Mycielskian of the cycle on \(n\) vertices and let \(K_n=\mathcal N(G_n)\) be its **open** Lovász neighborhood complex. Then \(K_n\simeq S^2\), but deleting **any one of its \(2n+1\) vertices produces a contractible induced subcomplex**:
\[
 K_n[V(G_n)\setminus\{v\}]\simeq *\qquad(v\in V(G_n)).
\]
Consequently, for every proper vertex subset \(W\subsetneq V(G_n)\), the inclusion-induced map
\[
\widetilde H_2(K_n[W];\mathbb Z)\longrightarrow\widetilde H_2(K_n;\mathbb Z)\cong\mathbb Z
\]
is zero. The unique nontrivial ambient second-homology class therefore has minimum induced **ambient carrier** support exactly \(2n+1\) vertices. This is an unbounded sequence of vertex-essential representatives of the same sphere homotopy type.

The natural dihedral subgroup \(D_n\) acting simultaneously on the original and twin cycle labels acts on \(\widetilde H_2(K_n;\mathbb Z)\) by the orientation character: rotations act as \(+1\) and reflections as \(-1\). No claim is made about the action of any larger automorphism group.

## Assumptions and scope

Take subscripts modulo the odd integer \(n\geq5\). The graph has original vertices \(x_i\), twin vertices \(y_i\), and root \(z\). Its edges are \(x_ix_{i+1}\), \(x_i y_{i+1}\), \(x_i y_{i-1}\), and \(zy_i\) for all \(i\). The neighborhood complex has a nonempty simplex \(\sigma\) exactly when some graph vertex is adjacent to every vertex of \(\sigma\). An induced subcomplex \(K_n[W]\) is formed from those original simplices entirely supported in \(W\); it is not silently identified with the neighborhood complex of the induced graph. Coefficients in the result are integral. The carrier assertion concerns the **image in ambient homology**, not all intrinsic homology groups of proper induced subcomplexes.

## Proof

**1. Three kinds of neighborhoods.** Directly from the graph definition,
\[
F_i=\{x_{i-1},x_{i+1},y_{i-1},y_{i+1}\},\quad
T_i=\{x_{i-1},x_{i+1},z\},\quad
Y=\{y_j: j\in\mathbb Z/n\mathbb Z\}
\]
are the complete list of vertex-neighborhood sets. Write \(U\) for the union of the simplices on \(F_i\) and \(Y\), and \(Z\) for the union of the simplices on \(T_i\). Then \(K_n=U\cup Z\). Define \(C\) as the graph on the original vertices with edges \(E_i=\{x_{i-1},x_{i+1}\}\). As \(n\) is odd, addition by two runs through all indices, so \(C\) is an \(n\)-cycle. The intersections are \(U\cap Z=C\), while \(Z=z*C\) is its cone.

**2. The contractible part \(U\).** Cover \(U\) by the \(n+1\) simplices \(F_i,Y\). Every nonempty intersection is a simplex. For distinct \(i,j\), the simplices on \(F_i,F_j\) intersect precisely when \(j=i\pm2\), in the edge \(\{x_{(i+j)/2},y_{(i+j)/2}\}\), with the shared index understood as the unique common index of \(\{i-1,i+1\}\) and \(\{j-1,j+1\}\). Each \(F_i\) meets \(Y\) in the edge \(\{y_{i-1},y_{i+1}\}\). The only nonempty triple intersections are \(F_i\cap F_{i+2}\cap Y=\{y_{i+1}\}\). Higher intersections are empty. Thus the nerve is the cone on the cycle with vertices indexed by \(i\), consecutive when their indices differ by two. By the simplicial nerve theorem \(U\) is contractible.

**3. Full homotopy.** Both \(U\) and \(Z\) are contractible subcomplexes, while their intersection \(C\) is a circle. The homotopy-pushout (cofibration) form of Mayer–Vietoris for spaces gives \(K_n\simeq\Sigma C\simeq S^2\). The integral connecting map \(\widetilde H_2(K_n;\mathbb Z)\to\widetilde H_1(C;\mathbb Z)\) is an isomorphism.

**4. Delete the root or an original vertex.** Removing \(z\) leaves \(U\), already contractible. For any \(x_k\), the cover \(\{F_i\setminus\{x_k\},Y\}\) of \(U-x_k\) has exactly the same nerve as in step 2: any former edge intersection involving \(x_k\) still contains \(y_k\), and every triple intersection with \(Y\) remains nonempty. Thus \(U-x_k\) is contractible. Its intersection with \(Z-x_k=z*(C-x_k)\) is \(C-x_k\), a path, so \(K_n-x_k\) is contractible by the homotopy-pushout lemma for three contractible CW subcomplexes.

**5. Delete a twin vertex.** Fix \(y_k\), and put \(U'=U-y_k\). The simplex cover \(\{F_i\setminus\{y_k\},Y\setminus\{y_k\}\}\) has the former nerve with **exactly one triangle removed**, namely the triangle on nerve vertices \(F_{k-1},F_{k+1},Y\). Its edges remain because \(F_{k-1}\cap F_{k+1}\) still contains \(x_k\). The resulting nerve deformation retracts onto its boundary cycle on the \(F_i\): remove its \(n-1\) fan triangles successively along free spokes, then remove the last spoke and apex. On the other hand, the edge cover \(\{E_i\}\) of \(C\) has exactly this boundary-cycle nerve. Every nonempty intersection in both covers is a simplex, and the inclusion of the edge cover into the \(F_i\) cover respects intersections. Naturality of the nerve equivalence for these compatible simplex covers shows that the inclusion \(C\hookrightarrow U'\) is a homotopy equivalence. Because \(K_n-y_k=U'\cup_C(z*C)\) is its mapping cone up to homotopy, \(K_n-y_k\) is contractible.

**6. Vertex support and symmetry.** Any proper \(W\) omits some vertex \(v\), so its inclusion into \(K_n\) factors through the contractible \(K_n-v\); hence its induced map on \(H_2\) is zero. Full support carries the nonzero generator from step 3. The dihedral action on the decomposition \(U\cup Z\) preserves \(C\), making the connecting isomorphism in step 3 equivariant. Rotations preserve the orientation of the step-two cycle \(C\), and reflections reverse it. Their scalar actions on integral second homology are therefore \(+1\) and \(-1\), respectively.

## Verification

The symbolic nerve calculation proves the theorem for **every** odd \(n\geq5\); it does not extrapolate from computation. The accompanying `verify.py` independently enumerates simplices, computes exact mod-two boundary ranks, verifies the three representative deletion types, and tests the cone/one-missing-triangle nerve structures for \(n=5,7,9,11\). Its output ends with `VERIFY_OK ODD_CYCLE_NERVE_AND_HOMOLOGY_SAMPLES`. The finite checks are consistency checks, not the proof of the universal quantifier.

## Relationship to prior work

Csorba's 2008 work on Mycielskians and homomorphism complexes establishes foundational suspension behavior. The sphere homotopy type in step 3 is an instance of this known general phenomenon and is **not** asserted to be new. The added result is the universal contractibility of every induced one-vertex deletion and the consequent exact, unbounded minimum ambient vertex support, with the natural dihedral orientation character. Shukla's neighborhood-complex classification addresses degree-at-most-three graphs and a restricted class of four-regular circulants rather than these varying-degree Mycielskians. Kahle's vertex-support lemmas address clique complexes of random graphs and do not imply this exact neighborhood-complex carrier threshold.

## Limitations

An equivalent vertex-deletion theorem could exist in less-indexed literature. Full text of Csorba's highly relevant original article was not accessible in this review; its abstract and publication record were inspected, so an unobserved remark within the paper remains a bibliographic risk. The result is about the ordinary one-step Mycielskian of **odd cycles**, induced restrictions of its **open neighborhood complex**, and the indicated dihedral subgroup. It does not describe intrinsic homology of every proper induced subcomplex, the full automorphism group, or even-cycle analogues. Independent review has not been performed.

## References

1. Péter Csorba, *Fold and Mycielskian on homomorphism complexes*, Contributions to Discrete Mathematics 3(2) (2008), 1–8, DOI: 10.55016/ojs/cdm.v3i2.61954. Public version dated 2008-09-11.
2. Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, Electronic Journal of Combinatorics 26(2) (2019), P2.4, arXiv:1802.04526.
3. Matthew Kahle, *Topology of random clique complexes*, Discrete Mathematics 309 (2009), 1658–1671 (particularly Section 5, vertex supports).
