# Homological rigidity of the 13-point projective-plane models
## Finding
For either of the two opposite 13-point minimal finite models \(P\) of \(\mathbb{RP}^2\), a continuous self-map \(f:P\to P\) acts nontrivially on \(H_1(P;\mathbf F_2)\) exactly when \(f\) is a homeomorphism. Thus every non-homeomorphism kills the unique nonzero mod-2 first-homology class. Exactly 24 self-maps have nonzero action, and \(\operatorname{Aut}(P)\cong S_4\). A complete enumeration contains 562333 continuous self-maps.

## Assumptions and scope
Use the standard 13-point model in the following self-contained form. Let the four elements \(a_1,\ldots,a_4\) index the vertices of \(K_4\), let six middle elements index its edges, and let three upper elements index its perfect matchings. Put \(a_i<b_e\) exactly when vertex \(i\) is incident with edge \(e\), and put \(b_e<c_M\) exactly when \(e\notin M\). Its opposite is the other minimal model. A function is order-preserving on this poset exactly when it is order-preserving after reversing both orders, so one calculation covers both models.

The checker verifies that the order complex has 13 vertices, 36 edges and 24 triangles; every edge belongs to two triangles; every vertex link is a connected cycle; and the Euler characteristic is \(1\). Hence its realization is the closed connected surface \(\mathbb{RP}^2\). It also recomputes \(\dim_{\mathbf F_2}H_1=1\).

## Proof
Continuous maps between finite \(T_0\)-spaces are order-preserving maps of their associated posets. The checker reconstructs the transitive order from the cover relations and exhaustively enumerates every self-map satisfying the cover inequalities. Checking covers suffices because they generate the order by transitivity. The exact count is 562333.

Over \(\mathbf F_2\), the checker builds the order-complex chain complex, computes a non-coboundary cocycle \(w\in H^1(P;\mathbf F_2)\), and verifies that the six-edge cycle
\[
a_1<b_{12}>a_2<b_{23}>a_3<b_{13}>a_1
\]
pairs with \(w\) as \(1\). Since \(H_1(P;\mathbf F_2)\) is one-dimensional, this cycle generates it. For each order-preserving \(f\), the induced simplicial map sends a comparable edge to the corresponding comparable edge, or to zero when its endpoints coalesce. Thus \(f_*\) is nonzero exactly when \(\langle w,f_*z\rangle=1\).

Exactly 24 maps pass that test. Every one is bijective, and the checker verifies directly that each inverse is also order-preserving; therefore they are homeomorphisms. Conversely a homeomorphism induces an isomorphism on the one-dimensional group \(H_1(P;\mathbf F_2)\), hence acts nontrivially.

The four \(a_i\) determine the six middle elements as their two-element subsets, and the three upper elements are determined by the perfect matchings. Every permutation of the four \(a_i\) therefore extends uniquely to an automorphism, and every automorphism is so obtained. Hence \(\operatorname{Aut}(P)\cong S_4\), with 24 elements.

## Verification
Run `python3 artifacts/verify.py`. The committed `artifacts/verification_output.txt` ends with `VERIFY_OK`. The verifier is deterministic, uses only the Python standard library, reconstructs the poset and homology detector from scratch, enumerates all isotone self-maps without symmetry pruning, and tests every induced action and every inverse among the bijections.

## Relationship to prior work
Barmak's 2011 monograph gives the 13-point finite model of \(\mathbb{RP}^2\). Cianci and Ottina prove that 13 points are minimal and that the only minimal finite models are this model and its opposite. The inspected material fixes the object and its extremality but does not classify its endomorphisms or identify the self-maps preserving mod-2 first homology.

Targeted published-finding corpus and literature searches used finite-space, poset-endomorphism, order-preserving-map, automorphism, projective-plane and homology formulations. The closest database record concerns torsion in a six-vertex simplicial triangulation of \(\mathbb{RP}^2\), not self-maps of the 13-point finite-space model. An earlier own finding on minimal sphere models does not imply this result: the present model is nonsimply connected and has a different incidence structure, and its proof is a separate complete endomorphism census.

## Limitations
The result concerns direct continuous self-maps of the two 13-point minimal finite models. It does not classify maps after subdivision or enlargement, nor all homotopy classes of self-maps of the classical surface. The number 562333 is supporting reproducibility data rather than the primary value claim. Targeted search cannot exclude an obscure equivalent statement under different terminology.

## References
1. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011. DOI `10.1007/978-3-642-22003-6`.
2. N. Cianci and M. Ottina, *Poset splitting and minimality of finite models*, arXiv `1512.06088` (first public version 2015-12-18).
