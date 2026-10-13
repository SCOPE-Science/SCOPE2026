# The \(A_4\) Demazure model is not weak Fano
## Finding
Let \(Y(A_4)\) be the smooth projective four-dimensional toric Demazure model constructed by Nicole Lemire for the torus with character lattice and splitting group \((\Lambda(A_4),\operatorname{Aut}(A_4))\). Then
\[
-K_{Y(A_4)}\ \text{is not nef}.
\]
Consequently \(Y(A_4)\) is not weak Fano, and in particular it is not Fano.

More precisely, the fan contains a torus-invariant curve \(C_\tau\) with
\[
(-K_{Y(A_4)})\cdot C_\tau=-1.
\]

## Assumptions and scope
The statement concerns the smooth projective toric variety defined by Lemire's final fan in Proposition 7.6 of arXiv:2609.30482v1. The positivity assertion is geometric, so it may be checked after base change to an algebraic closure of the splitting field.

For the path \(C_1=\{(2,3),(2,4),(2,5),(1,5)\}\), Lemire labels the primitive generators of the corresponding multiplicity-three cone by \(\gamma_1,\ldots,\gamma_4\). The source gives
\[
v_1=\frac{\gamma_3+\gamma_4}{3}
=e_1+2e_2-e_3-e_4-e_5
\]
and replaces that cone by the two smooth maximal cones
\[
\sigma_+=\operatorname{Cone}(\gamma_1,\gamma_2,\gamma_3,v_1),
\qquad
\sigma_-=\operatorname{Cone}(\gamma_1,\gamma_2,v_1,\gamma_4).
\]
Proposition 7.6 records these two cones as part of the final smooth fan.

## Proof
The two maximal cones \(\sigma_+\) and \(\sigma_-\) share the codimension-one cone
\[
\tau=\operatorname{Cone}(\gamma_1,\gamma_2,v_1).
\]
Since the final fan is smooth and complete, \(\tau\) determines a complete torus-invariant curve \(C_\tau\).

The source's identity \(v_1=(\gamma_3+\gamma_4)/3\) is exactly the wall relation
\[
\gamma_3+\gamma_4-3v_1=0.
\]
For a smooth projective toric variety, if the primitive generators around a wall satisfy a wall relation, the coefficients are the intersection numbers of the corresponding invariant divisors with the invariant curve. Hence
\[
D_{\gamma_3}\cdot C_\tau=1,
\qquad
D_{\gamma_4}\cdot C_\tau=1,
\qquad
D_{v_1}\cdot C_\tau=-3,
\]
while the two wall-ray divisors have coefficient zero in this relation and every other invariant divisor misses the wall relation.

Because the anticanonical divisor of a smooth toric variety is the sum of its torus-invariant prime divisors,
\[
(-K_{Y(A_4)})\cdot C_\tau=1+1-3=-1.
\]
Thus \(-K_{Y(A_4)}\) is not nef. Weak Fano varieties require the anticanonical divisor to be nef and big, so \(Y(A_4)\) is not weak Fano.

## Verification
The source was inspected at the full construction of the \(C_1\)-subdivision. It proves that the original cone has multiplicity \(3\), identifies the nontrivial interior lattice point as \(v_1=(\gamma_3+\gamma_4)/3\), and displays the two smooth maximal cones sharing \(\tau\). Proposition 7.6 confirms that these subdivided cones occur in the final smooth projective fan.

The toric intersection rule was checked against the standard wall-relation formula: for a smooth projective toric variety, coefficients in the wall relation are the intersections with the corresponding invariant divisors, and the anticanonical degree is the sum of those coefficients. Substitution gives the exact integer \(-1\), with no numerical approximation or finite experiment.

## Relationship to prior work
Lemire constructs \(Y(A_4)\) and analyzes the fan, ray orbits, and the resulting flasque resolution, but the paper does not discuss nefness or anticanonical positivity: searches of the full text for “nef” and “anticanonical” return no occurrence, and “Fano” appears only in bibliographic material.

A previously published calculation from the same source determines the numbers of rays and maximal cones, the Picard rank, and the Betti numbers of \(Y(A_4)\). Those topological invariants do not determine anticanonical nefness and do not imply the negative wall degree above.

Targeted searches for the exact weak-Fano statement, the anticanonical degree \(-1\), the \(C_1\) wall relation, and equivalent Mori-cone formulations found no covering statement. The present conclusion is the direct birational-positivity consequence of the index-three star subdivision that is not extracted in the initiating paper.

## Limitations
The claim is only a negativity witness for the anticanonical divisor; it does not determine the full Mori cone, nef cone, effective cone, anticanonical Iitaka dimension, or the complete list of negative invariant curves. It also does not assert an analogous statement for every Demazure model or for the lower-dimensional constructions in the paper.

## References
N. Lemire, “Demazure Models of Algebraic Tori in Dimension 4,” arXiv:2609.30482v1, first public 2026-09-24; especially Section 7.3 and Proposition 7.6.

B. Skauli, “Curve classes on Calabi–Yau complete intersections in toric varieties,” Bulletin of the London Mathematical Society 55 (2023), 1050–1064, DOI 10.1112/blms.12758; see the wall-relation intersection formula in Section 2.
