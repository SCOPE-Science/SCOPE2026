# An exact flag criterion for the cyclic weakly regular torus family
## Finding
For integers \(n\ge 7\) and \(2\le k\le\lfloor(n-3)/2\rfloor\), let \(T_{n,1,k}\) be the cyclic torus triangulation of Datta and Upadhyay. An **empty triangle** is a three-vertex clique in the edge graph that is not a triangular face. Write \(\mathbf 1_P\) for \(1\) when the proposition \(P\) is true and \(0\) otherwise. Then the exact number \(E(n,k)\) of empty triangles is
\[
E(n,k)=n\mathbf 1_{k=2}+\frac n3\left(\mathbf 1_{n=3k}+\mathbf 1_{n=3(k+1)}\right)+n\left(\mathbf 1_{n=3k+1}+\mathbf 1_{n=3k+2}+\mathbf 1_{n=2k+3}\right).
\]
Hence \(T_{n,1,k}\) is flag if and only if none of the six arithmetic conditions
\[
k=2,\qquad n=3k,\qquad n=3(k+1),\qquad n=3k+1,\qquad n=3k+2,\qquad n=2k+3
\]
holds. The first flag member in the canonical range is \(T_{13,1,3}\).

## Assumptions and scope
The triangulation has vertex set \(\mathbb Z/n\mathbb Z\) and triangular faces
\[
\{i,i+k,i+k+1}\},\qquad \{i,i+1,i+k+1}\}
\]
for all \(i\in\mathbb Z/n\mathbb Z\). Datta--Upadhyay show that these complexes triangulate the torus and that \(T_{n,1,k}\cong T_{n,1,n-k-1}\), so restricting to \(2\le k\le\lfloor(n-3)/2\rfloor\) loses no member of this parameter family up to that symmetry.

The statement classifies empty triangles and flagness only inside this cyclic family. It does not classify all flag triangulations of the torus.

## Proof
The edge differences of \(T_{n,1,k}\) are exactly
\[
D=\{\pm1,\pm k,\pm(k+1)\}\}\subset\mathbb Z/n\mathbb Z.
\]
Thus an edge-graph triangle determines oriented steps \(x,y,z\in D\) with \(x+y+z\equiv0\pmod n\). Put \(c=k+1\). In the canonical range, \(c\le(n-1)/2\). Choose each step as an integer in \(\{\pm1,\pm k,\pm c\}\}\). Reversing orientation when necessary, the integer sum is either \(0\) or \(n\).

If the sum is \(0\), cancellation of an opposite pair would force the third step to vanish, so the relation is a signed equality among \(1,k,c\). The universal relation \(1+k=c\) gives precisely the actual triangular faces. The only additional equality is \(1+1=k\), which occurs exactly when \(k=2\); its translates give \(n\) empty triangles.

If the sum is \(n\), no step can be negative: with one negative step the sum is at most \(2c-1=2k+1\le n-2\). Hence all three steps are positive. Enumerating the multisets of three elements of \(\{1,k,c\}\}\), the only ones that can sum to \(n\) in the canonical range are
\[
\{k,k,k\},\quad \{c,c,c\},\quad \{k,k,c\},\quad \{k,c,c\},\quad \{1,c,c\}.
\]
They yield, respectively,
\[
n=3k,\quad n=3(k+1),\quad n=3k+1,\quad n=3k+2,\quad n=2k+3.
\]
The equal-step cases have translation orbit size \(n/3\); each mixed-step case has translation orbit size \(n\). These relation types give disjoint unordered vertex triples, so their contributions add. This proves the displayed formula.

Finally, in a triangulated closed surface, a clique of size at least four would contain an empty triangle unless all of its three-subsets were faces; the latter would contain the tetrahedral sphere as a closed two-dimensional subcomplex, impossible in a connected torus triangulation. Therefore this two-dimensional complex is flag exactly when it has no empty triangle. Substituting the six conditions proves the criterion. Direct inspection of admissible parameters shows that the least \(n\) with a flag member is \(n=13\), attained at \(k=3\).

## Verification
The accompanying verifier independently reconstructs the face and edge sets, enumerates every edge-graph triangle, compares the exact count with the formula, and separately constructs each arithmetic relation family. It checks every admissible pair through \(7\le n\le180\), a total of \(7656\) parameter pairs, and returns:

`VERIFY_OK parameters=7656 range=n7..180 first_flag=13,3 exact_formula=yes relation_families=yes`

This finite computation is a stress test of the universal symbolic proof, not a substitute for its quantifiers.

## Relationship to prior work
Datta and Upadhyay define \(T_{n,1,k}\), prove that it triangulates the torus, and record the parameter symmetry used above. Brehm and Kühnel give a broader lattice-quotient classification of equivelar torus maps. Neither inspected source states the empty-triangle counting formula or the six-condition flag criterion.

Bibby, Odesky, Wang, Wang, Zhang, and Zheng prove that the globally vertex-minimal flag triangulation of the torus has twelve vertices and is unique. The present result instead locates flagness arithmetically inside the Datta--Upadhyay cyclic family: its first flag member occurs at thirteen vertices. Thus this natural cyclic family misses the global flag minimum by one vertex.

## Limitations
The theorem is specific to the family \(T_{n,1,k}\) and to the canonical parameter range, with the complementary range recovered by the published symmetry. It does not assert that every equivelar torus triangulation is flag under an analogous arithmetic test. A residual originality risk is that an older lattice-coordinate treatment of equivelar torus maps may contain an equivalent criterion under different notation; no such statement was found in the inspected primary and closely related full texts or in targeted semantic searches.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, first public version 2004-03-25.
2. U. Brehm and W. Kühnel, *Equivelar maps on the torus*, Stuttgart Mathematical Preprint 2006/013.
3. C. Bibby, A. Odesky, M. Wang, S. Wang, Z. Zhang, and H. Zheng, *Minimal flag triangulations of lower-dimensional manifolds*, arXiv:1909.03303.
