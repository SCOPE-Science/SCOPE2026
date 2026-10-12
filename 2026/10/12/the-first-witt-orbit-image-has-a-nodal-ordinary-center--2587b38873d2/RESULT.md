# The first Witt orbit image has a nodal ordinary center

## Finding
Let \(k\) be an uncountable algebraically closed field of characteristic \(0\), let \(W_{\ge -1}=k[t]\partial\), and let \(B_1\subseteq T_1=A_1\otimes k[v]\) be the image of the first orbit homomorphism \(\Psi_1\) of Pham. Put \(w=v(v-1)\) and \(z=wv\). Then the ordinary center is exactly \(Z(B_1)=k+w k[v]=k[w,z]\), with presentation \(Z(B_1)\cong k[W,Z]/(Z^2-WZ-W^3)\). Hence \(\operatorname{Spec} Z(B_1)\) is a rational affine nodal curve, its normalization is \(\mathbb A^1_k=\operatorname{Spec}k[v]\), and the normalization map identifies precisely the two points \(v=0\) and \(v=1\) over the node.

Thus the exceptional two-to-one behavior at \(v=0\) and \(v=1\) in the restriction picture has a commutative shadow: those two normalization points are glued into the unique node of the ordinary center.

## Assumptions and scope
The ground field \(k\) is uncountable, algebraically closed, and of characteristic \(0\), matching the standing hypotheses of the motivating source. Let \(A_1=k\langle t,\partial\rangle/(\partial t-t\partial-1)\). For the one-dimensional abelian Lie algebra \(\mathfrak g_1=kv\), one has \(T_1=A_1\otimes k[v]\). The orbit homomorphism is
\[
\Psi_1(f\partial)=f(t)\partial+f'(t)v,
\]
and \(B_1=\Psi_1(U(W_{\ge -1}))\).

The claim concerns the ordinary center \(Z(B_1)\), not the extended center of the Goldie quotient ring and not the centers of \(B_n\) for \(n\ge2\).

## Proof
Pham proves that, after localizing at products of positive powers of \(v\) and \(v-1\),
\[
B_1X_1^{-1}=T_1X_1^{-1}=A_1\otimes k[v,v^{-1},(v-1)^{-1}].
\]
Because \(Z(A_1)=k\) in characteristic \(0\), the center of this localization is
\[
k[v,v^{-1},(v-1)^{-1}].
\]
Therefore every \(c\in Z(B_1)\) belongs to this Laurent coefficient ring. But \(c\in B_1\subseteq T_1=A_1\otimes k[v]\), so PBW uniqueness in the Weyl factor gives
\[
c\in k[v].
\]
Hence \(Z(B_1)=B_1\cap k[v]\).

Now set \(w=v(v-1)\). Pham's explicit \(n=1\) prime-spectrum argument identifies the kernel of the projection \(\Pi_{1,0}:B_1\to B_0\) with \(T_1w\), and in particular \(T_1w\subseteq B_1\). If \(p(v)\in B_1\cap k[v]\), then
\[
p(v)-p(0)\in\ker(\Pi_{1,0}|_{B_1})=T_1w.
\]
Since the left side lies in \(k[v]\), it is divisible by \(w=v(v-1)\). Thus \(p(1)=p(0)\). Conversely, if \(p(1)=p(0)\), then \(p(v)-p(0)\) is divisible by \(w\), so \(p(v)\in k+T_1w\subseteq B_1\). Consequently
\[
Z(B_1)=B_1\cap k[v]=\{p(v)\in k[v]:p(0)=p(1)\}=k+w k[v].
\]

Put \(z=wv\). Since \(v^2=v+w\), every \(wv^m\) reduces recursively to an element of \(k[w]+z k[w]\). Hence
\[
k+w k[v]=k[w,z].
\]
Moreover
\[
z^2=w^2v^2=w^2(v+w)=wz+w^3,
\]
so there is a surjection \(k[W,Z]/(Z^2-WZ-W^3)\to Z(B_1)\). It is injective because \(k[v]\) is free of rank \(2\) over \(k[w]\) with basis \(1,v\), so \(1,z\) are linearly independent over \(k[w]\). This proves the presentation.

Finally, the plane curve \(Z^2-WZ-W^3=0\) has tangent cone \(Z(Z-W)\) at \((0,0)\), so the singularity is an ordinary node. The inclusion \(k[w,z]\hookrightarrow k[v]\), given by \(w=v(v-1)\) and \(z=v^2(v-1)\), is finite because \(v\) satisfies \(v^2-v-w=0\), and it is birational because \(v=z/w\) in the fraction field. Since \(k[v]\) is normal, it is the normalization. Away from \(w=0\) one recovers \(v=z/w\); over \(w=z=0\), the equation \(v(v-1)=0\) gives exactly \(v=0\) and \(v=1\).

## Verification
The proof uses only the displayed orbit-map realization, the localization identity, and the exact kernel \(\ker(\Pi_{1,0}|_{B_1})=T_1v(v-1)\) from the motivating source, followed by elementary Weyl-algebra and commutative-algebra arguments. No finite experiment is used to infer an infinite statement.

The presentation can be checked directly from \(w=v(v-1)\) and \(z=wv\): \(z^2-wz-w^3=0\), and \(k+w k[v]=k[w]+z k[w]\). The normalization and node statements then follow from the quadratic equation for \(v\) and the tangent cone.

## Relationship to prior work
Pham's 2026 paper introduces and studies the orbit images \(B_n\), proves ACC on two-sided ideals, classifies their prime and primitive spectra, proves the localization identity above, and for \(B_1\) proves \(\ker(\Pi_{1,0}|_{B_1})=T_1v(v-1)\). The paper emphasizes extended centers in the Dixmier--Moeglin analysis, but the inspected full text does not state the ordinary-center description or the nodal normalization above.

Sierra and Walton's 2016 paper studies the earlier homomorphic image underlying the first orbit construction and determines kernels, images, and Noetherian properties. Its searchable full text was inspected for ordinary-center statements; no covering center computation was found. The new claim is therefore a structural corollary of the newer localization and kernel information rather than a restatement of the older image calculations.

## Limitations
The argument is stated only under the characteristic-zero standing hypotheses of the motivating paper. It does not determine \(Z(B_n)\) for \(n\ge2\), nor does it classify the extended center of quotient rings beyond what is already in the source. The originality comparison is limited by terminology: an equivalent center computation could conceivably be hidden in older work under a different presentation of the same image, although targeted searches and the most relevant primary full texts inspected here did not reveal one.

## References
1. T. A. Pham, *Ideals of homomorphic images of the enveloping algebra of the Witt algebra*, arXiv:2610.01913v1 (2026), especially Proposition 2.5, Lemma 4.2, Proposition 4.10, and the proof of Theorem 4.16.
2. S. J. Sierra and C. Walton, *Maps from the enveloping algebra of the positive Witt algebra to regular algebras*, Pacific J. Math. 284 (2016), 475--509, doi:10.2140/pjm.2016.284.475.
