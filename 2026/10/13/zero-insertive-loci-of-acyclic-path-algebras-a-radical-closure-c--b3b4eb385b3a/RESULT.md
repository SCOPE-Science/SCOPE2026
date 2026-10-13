# Zero-insertive loci of acyclic path algebras: a radical-closure criterion and sharp deficit

## Finding
For any finite acyclic quiver \(Q\) and field \(K\), let \(A=KQ\) and define the zero-insertive locus
\[
Z_i(A)=\{arb:a,b,r\in A,\ ab=0\}.
\]
If \(J=J(A)\) denotes the Jacobson radical, then
\[
Z_i(A)\subseteq J,\qquad \operatorname{span}_K Z_i(A)=J.
\]
Moreover, the following are equivalent:

1. \(Z_i(A)\) is closed under addition (equivalently, is a \(K\)-subspace).
2. \(Z_i(A)=J\).
3. \(J^2=0\).
4. \(Q\) has no oriented path of length two.

If \(K=\mathbb F_q\), \(d=\dim_K J\), and \(Q\) has an oriented path of length two, then
\[
|Z_i(A)|\le q^d-(q-1)^2q^{d-2}.
\]
This universal bound is sharp. For the oriented three-vertex line, whose path algebra is \(T_3(K)\),
\[
Z_i(T_3(K))=
\left\{
\begin{pmatrix}0&a&b\\0&0&c\\0&0&0\end{pmatrix}:ac=0
\right\},
\qquad |Z_i(T_3(\mathbb F_q))|=q(2q-1).
\]

## Assumptions and scope
A quiver is finite as a directed multigraph, with a finite vertex and arrow set. It is acyclic if it has no directed cycle; parallel arrows and isolated vertices are allowed. Its path algebra has as a basis all directed paths, including length-zero vertex paths, and uses left-to-right concatenation when endpoints match. The arrow ideal \(J\) is spanned by positive-length paths. Because \(Q\) is finite and acyclic, \(J\) is nilpotent and \(A/J\cong K^{Q_0}\), hence \(J\) is the Jacobson radical. No assumptions on the characteristic or perfection of \(K\) are imposed. The finite-field bound is asserted only when a two-arrow path exists, so \(d\ge3\).

## Proof
**Containment and span.** The quotient map \(A\to A/J\cong K^{Q_0}\) sends any triple \(a,b,r\) with \(ab=0\) to a triple with zero first–third product. The componentwise-commutative algebra \(K^{Q_0}\) has \(\bar a\bar r\bar b=\bar r\bar a\bar b=0\). Thus \(Z_i(A)\subseteq J\). Every positive-length path \(p\) has distinct initial and terminal vertices \(s(p)\ne t(p)\); otherwise it would be a directed cycle. Hence \(p=e_{s(p)}p e_{t(p)}\) and \(e_{s(p)}e_{t(p)}=0\), so \(p\in Z_i(A)\). Such paths are a basis of \(J\), proving its span assertion. Scalar multiples of zero-insertive elements are again zero-insertive.

**No composable arrows.** Suppose no two arrows compose. Let \(S\) be the set of arrow sources and \(T\) the set of arrow targets. They are disjoint. With \(e_S=\sum_{s\in S}e_s\) and \(e_T=\sum_{t\in T}e_t\), one has \(e_Se_T=0\). Every element \(x\in J\) is a combination of arrows, and all arrows go from \(S\) to \(T\); hence \(x=e_Sxe_T\in Z_i(A)\). Consequently \(Z_i(A)=J\). Conversely, \(J^2=0\) holds exactly when no length-two paths exist, because the concatenated paths form linearly independent basis elements of \(KQ\).

**Composable arrows obstruct additivity.** Suppose there are arrows \(\alpha:u\to v\) and \(\beta:v\to w\). Acyclicity makes \(u,v,w\) distinct. There is a surjective algebra homomorphism \(\pi:KQ\to T_3(K)\) sending the selected vertices to \(E_{11},E_{22},E_{33}\), the selected arrows \(\alpha,\beta\) to \(E_{12},E_{23}\), and every other vertex and arrow to zero. Its action on paths is determined by multiplication; the selected path \(\alpha\beta\) maps to \(E_{13}\). For any \(U,V,R\in M_3(K)\) with \(UV=0\), the inclusion \(\operatorname{im}(V)\subseteq\ker(U)\) gives \(\operatorname{rank}(U)+\operatorname{rank}(V)\le3\). Thus
\[
\operatorname{rank}(URV)\le\min(\operatorname{rank}(U),\operatorname{rank}(V))\le1.
\]
But \(\pi(\alpha+\beta)=E_{12}+E_{23}\) has rank two. Since zero-insertive elements map to zero-insertive elements under algebra homomorphisms, \(\alpha+\beta\notin Z_i(A)\). Each arrow separately lies in \(Z_i(A)\); therefore \(Z_i(A)\) is not additive. Together with the previous steps, this proves all equivalences.

**A sharp quantitative obstruction.** Assume \(K=\mathbb F_q\), and fix \(\alpha,\beta\) as above. In the path basis of \(J\), every element whose coefficients of \(\alpha\) and \(\beta\) are both nonzero maps to a matrix of the form
\[
aE_{12}+bE_{13}+cE_{23}\qquad(a,c\ne0).
\]
This matrix has rank two regardless of \(b\), so none of those elements belongs to \(Z_i(A)\). There are \((q-1)^2q^{d-2}\) such elements because all other \(d-2\) path coefficients are unrestricted. This gives the bound.

**Sharpness and exact three-vertex locus.** For the line quiver, the positive-length paths correspond to \(E_{12},E_{13},E_{23}\). The earlier rank obstruction shows that \(aE_{12}+bE_{13}+cE_{23}\) cannot be zero-insertive if \(ac\ne0\). If \(a=0\), then the same matrix \(X\) equals \((E_{11}+E_{22})X E_{33}\), with the two outer idempotents having zero product. If \(c=0\), then \(X=E_{11}X(E_{22}+E_{33})\), again with zero product of outer factors. Thus \(ac=0\) is necessary and sufficient. There are \(q\) choices for \(b\) and \(2q-1\) for \((a,c)\) with \(ac=0\), yielding the stated count and equality in the universal bound.

## Verification
The accompanying standard-library script `verify.py` exhaustively computes all zero-product triples in the binary path algebras of the three-vertex line and the source–sink fork. It finds respectively six of eight radical elements and four of four radical elements in the zero-insertive locus. It checks both exact locus descriptions coefficientwise. Independent finite enumeration of coefficient triples confirms \(q(2q-1)\) for \(q=2,3,5\). The all-quiver theorem and the arbitrary-field claim are proved algebraically above, not inferred from these examples. Reproduce the checks with `python3 verify.py`.

## Relationship to prior work
Subba and Subedi (2026, arXiv:2609.24439v1, Section 2) introduced the path-algebra setting for zero-insertive elements and exhibited the zero-insertive nature of individual non-loop paths. Their paper classifies semicommutativity and nil-clean phenomena, but does not state the radical-wide additive-closure criterion or the sharp finite-field deficiency bound established here. Their earlier 2025 paper introduces the zero-insertive and ZINC terminology. The published full-matrix half-rank characterization concerns the larger ring \(M_n(K)\), not its upper-triangular path subalgebras; it provides the necessary rank obstruction in the three-vertex quotient, not this quiver-wide if-and-only-if result.

## Limitations
The theorem is restricted to finite acyclic **ordinary path algebras**, without additional path relations. Quivers with oriented cycles and general quotient algebras may exhibit different behavior. The finite-field inequality is a sharp universal lower bound on the deficit, not an exact enumeration of \(Z_i(A)\) for all quivers with composable arrows. Historical coverage cannot be conclusively excluded by database searches alone; the assessed novelty is the combined radical-closure classification and sharp deficit, not the zero-insertiveness of individual paths or the standard rank inequality.

## References
1. S. Subba and T. Subedi, *Semicommutativity via Zero-Insertive Elements: Insights from Path and Leavitt Path Algebras*, arXiv:2609.24439v1, publicly posted 2026-09-21. Full text: https://arxiv.org/html/2609.24439v1 .
2. S. Subba and T. Subedi, *Zero Insertive Nil Clean Rings*, arXiv:2508.01333, first posted 2025-08-02. https://arxiv.org/abs/2508.01333 .
3. *Zero-insertive matrices are exactly the half-rank locus*, previously indexed mathematical result, opaque record identifier 8052759f-e4ed-4dc3-914a-95c8a5352fd2.
