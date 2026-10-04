# Two-point configurations of finite crowns retain the circle weak type
## Finding
For every integer \(n\ge 2\), let \(C_n\) be the \(2n\)-point crown with minimal points \(a_i\), maximal points \(b_i\), and strict relations \(a_i<b_i\) and \(a_i<b_{i-1}\), where indices lie in \(\mathbb Z/n\mathbb Z\). Define the ordered two-point configuration finite space
\[
F_2(C_n)=\{(x,y)\in C_n\times C_n:x\ne y\}
\]
with the subspace order inherited from the product. Then the first-coordinate projection
\[
\pi_1:F_2(C_n)\longrightarrow C_n
\]
is a weak homotopy equivalence. In particular, \(F_2(C_n)\) has \(2n(2n-1)\) points, is a finite model of \(S^1\), and its order complex satisfies
\[
|\mathcal K(F_2(C_n))|\simeq S^1.
\]

## Assumptions and scope
The statement is about ordered configurations of exactly two distinct points in the Alexandrov topology of the finite crown itself. It is not a statement that configuration spaces preserve arbitrary weak homotopy equivalences, and it does not identify \(F_2(C_n)\) up to finite-space homotopy equivalence. The conclusion is a weak homotopy equivalence supplied by the explicit projection \(\pi_1\).

## Proof
For a point \(z\in C_n\), write \(U_z\) for its minimal open set. The minimal open sets form a basis-like open cover of a finite space. We verify that every inverse image \(\pi_1^{-1}(U_z)\) is contractible and then apply McCord's local weak-equivalence theorem.

If \(z=a_i\) is minimal, then \(U_{a_i}=\{a_i\}\), so
\[
\pi_1^{-1}(U_{a_i})=\{a_i\}\times(C_n\setminus\{a_i\}).
\]
The Hasse diagram of \(C_n\setminus\{a_i\}\) is an alternating path. Each endpoint is a beat point, and successively removing endpoints reduces the space to one point. Hence this inverse image is contractible.

Now let \(z=b_i\) be maximal. Cyclic symmetry reduces the argument to \(i=0\). Then
\[
U_{b_0}=\{a_0,a_1,b_0\}.
\]
Inside \(\pi_1^{-1}(U_{b_0})\), perform the following beat-point deletions. First delete \((a_0,b_0)\) as a down beat point with witness \((a_0,a_1)\). For each \(k=1,\ldots,n-1\), delete \((a_0,b_k)\) and then \((a_0,a_k)\); these are up beat points with witnesses \((b_0,b_k)\) and \((b_0,a_k)\), respectively. Next delete \((a_1,b_0)\) as a down beat point with witness \((a_1,a_0)\). Delete \((a_1,b_1)\) as an up beat point with witness \((b_0,b_1)\). For each \(k=2,\ldots,n-1\), delete \((a_1,b_k)\) and then \((a_1,a_k)\), with witnesses \((b_0,b_k)\) and \((b_0,a_k)\). Finally delete \((a_1,a_0)\) as an up beat point with witness \((b_0,a_0)\).

After these deletions the remaining subspace is
\[
\{b_0\}\times(C_n\setminus\{b_0\}),
\]
which is homeomorphic to \(C_n\setminus\{b_0\}\). Its Hasse diagram is again an alternating path, so endpoint beat-point deletion contracts it to one point. Therefore \(\pi_1^{-1}(U_{b_0})\) is contractible, and by symmetry the same holds for every maximal point.

Each \(U_z\) is itself contractible because it has maximum \(z\). Thus every restriction
\[
\pi_1^{-1}(U_z)\longrightarrow U_z
\]
is a weak homotopy equivalence between contractible spaces. McCord's theorem now implies that \(\pi_1\) is a weak homotopy equivalence.

Finally, the order complex \(\mathcal K(C_n)\) is the \(2n\)-cycle, hence its realization is homeomorphic to \(S^1\). McCord's weak equivalence from the order complex of a finite space to that space, together with the weak equivalence \(\pi_1\), gives a weak equivalence \(|\mathcal K(F_2(C_n))|\to S^1\). Both are CW complexes, so Whitehead's theorem upgrades this to a homotopy equivalence.

## Verification
The symbolic proof above is independent of finite enumeration. A standalone checker, `verify.py`, constructs the crowns and deleted-product posets for \(2\le n\le 12\). It checks that \(\pi_1\) is order preserving, that every inverse image of a minimal open set beat-reduces to one point, and that the mod-two Betti vector of the order complex is \((1,1,0)\) in every tested case. The finite computation is a stress test only; the quantified theorem is proved by the uniform beat-point argument and McCord's theorem.

## Relationship to prior work
Barmak and Minian develop finite models, the order-complex correspondence, beat points, and the McCord local criterion in the finite-space setting; their paper also identifies the four-point model of the circle as the minimal finite model of \(S^1\). Barnett and Farber study classical deleted products \(F(\Gamma,2)\) of geometric graphs and emphasize that such configuration spaces have their own topology rather than being determined merely by the homotopy type of \(\Gamma\). The present statement concerns a different object: the deleted diagonal inside the product of the finite Alexandrov crown \(C_n\) itself. The proof therefore verifies the forgetful projection directly rather than transferring a result from the geometric circle.

A later combinatorial-model paper of Wiltshire-Gordon concerns configuration spaces of geometric realizations of simplicial complexes and deleted subcomplex models. Its constructions do not identify the Alexandrov deleted product \(F_2(C_n)\) or imply that the coordinate projection above is a weak equivalence.

## Limitations
No claim is made for three or more particles, unordered configurations, arbitrary finite models of the circle, or arbitrary finite graphs. The result also does not assert that \(F_2(C_n)\) is homotopy equivalent to \(C_n\) as finite spaces; only weak homotopy equivalence is proved. The checker samples \(2\le n\le 12\) and is not part of the proof of the universal statement.

## References
J. A. Barmak and E. G. Minian, “Minimal Finite Models,” arXiv:math/0611156v1, 2006.

K. Barnett and M. Farber, “Topology of Configuration Space of Two Particles on a Graph, I,” arXiv:0903.2180v1, 2009.

J. D. Wiltshire-Gordon, “Models for Configuration Space in a Simplicial Complex,” arXiv:1706.06626v1, 2017.
