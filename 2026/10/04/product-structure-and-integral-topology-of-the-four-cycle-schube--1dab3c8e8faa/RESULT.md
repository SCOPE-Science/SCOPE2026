# Product structure and integral topology of the four-cycle Schubert complement

## Finding
Let \(X_{\square}\) be the specific four-cycle Schubert complement singled out by Mazzucchelli--Pavlov--Wang,
\[
X_{\square}=\operatorname{Gr}_{\mathbb C}(2,4)\setminus\bigl(V(p_{12})\cup V(p_{14})\cup V(p_{23})\cup V(p_{34})\bigr).
\]
Then there is an algebraic isomorphism
\[
X_{\square}\cong (\mathbb C^*)^2\times\{(x,y)\in\mathbb C^2:xy\ne1\}.
\]
Indeed, the condition \(p_{12}\ne0\) places every point in the standard big cell. With \(p_{12}=1\), write the unique row-reduced representative as
\[
\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.
\]
Its Pluecker coordinates satisfy \(p_{14}=d\), \(p_{23}=-a\), \(p_{34}=ad-bc\). Since \(a,d\ne0\) on \(X_{\square}\), the regular coordinate change \(x=b/a\), \(y=c/d\) gives \(p_{34}=ad(1-xy)\), proving the product decomposition with regular inverse \((a,d,x,y)\mapsto(a,b=ax,c=dy,d)\).

Consequently the integral homology is torsion-free and has ranks
\[
(b_0,b_1,b_2,b_3,b_4)=(1,3,4,3,1),
\]
so the ordinary Poincare polynomial is
\[
P_{X_{\square}}(t)=(1+t)^2(1+t+t^2)=1+3t+4t^2+3t^3+t^4.
\]
Moreover, in the Grothendieck ring of complex varieties,
\[
[X_{\square}]=(\mathbb L-1)^2(\mathbb L^2-\mathbb L+1),
\]
and therefore its compactly supported Hodge--Deligne polynomial is \((q-1)^2(q^2-q+1)\) with \(q=uv\). In particular \(\chi(X_{\square})=0\), refining and geometrically explaining the value reported for \(d=4\) in Example 4.12 and Table 5 of the source.

## Assumptions and scope
Work over \(\mathbb C\). The object is only the explicit four-positroid-hyperplane instance
\[
V(p_{12})\cup V(p_{14})\cup V(p_{23})\cup V(p_{34})
\]
of the cycle arrangement in \(\operatorname{Gr}_{\mathbb C}(2,4)\) described in Example 4.12 of [1]. No statement is made for every four-cycle configuration up to projective equivalence, for larger \(d\), or for the real complement. The Poincare polynomial is for ordinary singular homology with integral coefficients; the Hodge--Deligne polynomial is the compactly supported convention.

## Proof
Because \(V(p_{12})\) is removed, \(p_{12}\ne0\) everywhere on \(X_{\square}\). Thus the standard \(p_{12}\)-chart covers the whole complement. After setting \(p_{12}=1\), each point has a unique row-reduced representative
\[
M=\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.
\]
The relevant maximal minors are
\[
p_{14}=d,\qquad p_{23}=-a,\qquad p_{34}=ad-bc.
\]
Therefore the four-divisor complement is exactly
\[
\{(a,b,c,d)\in\mathbb C^4:a\ne0,\ d\ne0,\ ad-bc\ne0\}.
\]
Set \(x=b/a\) and \(y=c/d\). These are regular on this open set, and
\[
ad-bc=ad(1-xy).
\]
Hence
\[
(a,b,c,d)\longmapsto(a,d,x,y)
\]
is a regular map into \((\mathbb C^*)^2\times\{xy\ne1\}\). Its inverse is the polynomial map
\[
(a,d,x,y)\longmapsto(a,ax,dy,d),
\]
so it is an algebraic isomorphism.

Let \(U=\mathbb C^2\setminus H\), where \(H=\{xy=1\}\cong\mathbb C^*\). Alexander duality in \(\mathbb R^4\) gives
\[
\widetilde H_i(U;\mathbb Z)\cong H_c^{3-i}(H;\mathbb Z).
\]
Since \(H\cong S^1\times\mathbb R\), its compactly supported cohomology is \(\mathbb Z\) in degrees \(1\) and \(2\), and zero otherwise. Thus \(H_0(U)=H_1(U)=H_2(U)=\mathbb Z\) and all higher homology vanishes. Because \(H_*((\mathbb C^*)^2;\mathbb Z)\) is torsion-free with Poincare polynomial \((1+t)^2\), the integral Kunneth theorem yields
\[
P_{X_{\square}}(t)=(1+t)^2(1+t+t^2)=1+3t+4t^2+3t^3+t^4.
\]

Finally, additivity in \(K_0(\operatorname{Var}_{\mathbb C})\) gives
\[
[U]=\mathbb L^2-[\mathbb C^*]=\mathbb L^2-\mathbb L+1,
\]
so
\[
[X_{\square}]=(\mathbb L-1)^2(\mathbb L^2-\mathbb L+1).
\]
Applying the compactly supported Hodge--Deligne realization gives \((q-1)^2(q^2-q+1)\), and evaluating at \(q=1\) gives \(\chi(X_{\square})=0\).

## Verification
The accompanying `verify.py` checks the Pluecker relation under the displayed parametrization, the factorization of \(p_{34}\), the Poincare-polynomial convolution, the Hodge--Deligne expansion, and the source's polynomial value \(\chi(X_4)=0\) by exact integer arithmetic. These computations support the displayed identities; the algebraic isomorphism and the homology computation are proved above rather than inferred from finite experimentation.

## Relationship to prior work
Mazzucchelli--Pavlov--Wang identify the four hyperplanes \(p_{12}=p_{14}=p_{23}=p_{34}=0\) as an instance of their cycle arrangement and compute the Euler characteristic of the complement family. Their formula gives \(\chi(X_4)=0\) and Table 5 reports the same value [1]. The inspected source section does not state an algebraic product decomposition, integral Betti numbers, or a motivic/Hodge--Deligne refinement. The standard all-Pluecker-coordinate open Grassmannian and torus-quotient descriptions concern a different open set, because here \(p_{13}\) and \(p_{24}\) are allowed to vanish. published-finding corpus searches for the exact four-coordinate complement, its product form, its Betti polynomial, and its Hodge polynomial returned no covering statement.

## Limitations
The decomposition is for this labeled four-coordinate instance only. It does not classify arbitrary cycle arrangements, and it does not determine the cohomology ring or mixed Hodge structure beyond the stated Hodge--Deligne polynomial. A residual literature risk is that an equivalent product chart may be implicit in general complexity-one torus-action descriptions of \(\operatorname{Gr}(2,4)\); no explicit statement of this complement or its Betti polynomial was located in the inspected sources.

## References
[1] E. Mazzucchelli, D. Pavlov, K. Wang, *Hyperplane Arrangements in the Grassmannian*, arXiv:2409.04288v1 (2024-09-06), especially Section 4.3, Example 4.12 and Table 5; journal version in *Le Matematiche* 80 (2025), 387--408.

[2] K. Devriendt, H. Friedman, B. Reinke, B. Sturmfels, *The Two Lives of the Grassmannian*, arXiv:2401.03684. This is used only as broader background on \(\operatorname{Gr}(2,4)\), not as evidence for the product claim.
