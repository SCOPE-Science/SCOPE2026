# Sharp off-diagonal \(\ell_p\) Hausdorff convexification for planar Minkowski sums

## Finding
For every real \(p>2\) and every pair \(a,b\geq0\), define the convex-hull deficiency of a nonempty compact set \(S\subset\mathbb R^2\) by
\[
 d_p(S)=\sup_{x\in\operatorname{conv}S}\inf_{s\in S}\|x-s\|_p.
\]
Then the sharp two-radius Minkowski-sum envelope is
\[
 \boxed{\sup_{d_p(A)=a,\ d_p(B)=b}d_p(A+B)^p
 =\tfrac12\bigl((a+b)^p+|a-b|^p\bigr).}
\]
The supremum runs over all nonempty compact \(A,B\subset\mathbb R^2\) and is attained for every \(a,b\), including zero values, by two sets each containing at most two points. Unlike the sharp coefficient for an unrestricted ratio, this profile resolves the unequal-deficiency case.

## Assumptions and scope
The norm is the standard coordinate \(\ell_p\)-norm in the Euclidean plane, \(2<p<\infty\). Minkowski sums are ordinary pointwise sums. There are no symmetry or dimension-of-affine-hull assumptions on \(A,B\). All suprema and infima are attained for compact sets in finite dimension. The theorem does not claim the analogous optimal profile for an arbitrary norm or in three or more dimensions.

## Proof
**1. A uniform triangle estimate.** Consider any triangle with vertices \(0,u,v\in\mathbb R^2\) and put \(U=(u+v)/2\), \(V=(u-v)/2\), \(r=\|u\|_p\), \(s=\|v\|_p\). For every \(z=\lambda u+\mu v\) with \(\lambda,\mu\ge0\), \(\lambda+\mu\le1\), set \(h=\lambda+\mu\), \(k=\lambda-\mu\). Thus \(z=hU+kV\), \(0\le h\le1\), \(|k|\le h\). If \(k\ge0\), comparing \(z\) to vertices \(0\) and \(u=U+V\), the triangle inequality gives
\[
 d_p(z,\{0,u,v\})\le\min\{h\|U\|_p+k\|V\|_p,
 (1-h)\|U\|_p+(1-k)\|V\|_p\}
 \le\tfrac12(\|U\|_p+\|V\|_p).
\]
If \(k\le0\), compare vertices \(0\) and \(v=U-V\) instead and obtain the same bound. Convexity of the scalar \(p\)-th power yields
\[
 d_p(\{0,u,v\})^p\le\tfrac12(\|U\|_p^p+\|V\|_p^p)
 =2^{-p-1}(\|u+v\|_p^p+\|u-v\|_p^p).
\]
Hanner's classical inequality for \(p\ge2\) now gives
\[
 \|u+v\|_p^p+\|u-v\|_p^p
 \le(r+s)^p+|r-s|^p,
\]
so that
\[
 \boxed{d_p(\{0,u,v\})^p\le2^{-p-1}\bigl((r+s)^p+|r-s|^p\bigr).} \tag{1}
\]
Translations do not change this estimate.

**2. Reduction to the triangle estimate.** Fix compact \(A,B\) and set \(a=d_p(A)\), \(b=d_p(B)\). The function
\[
 F_p(x,y)=\tfrac12\bigl((x+y)^p+|x-y|^p\bigr),\qquad x,y\ge0,
\]
is nondecreasing in each argument: at every differentiability point, its first partial derivative is \(\tfrac p2((x+y)^{p-1}+\operatorname{sgn}(x-y)|x-y|^{p-1})\ge0\); symmetry gives the second. Also \(F_p(a,b)\ge\max\{a^p,b^p\}\), by the convexity of the \(p\)-th power applied to \(\max\{a,b\}\pm\min\{a,b\}\).

Take any \(z\in\operatorname{conv}(A+B)\). If \(z\in A+\operatorname{conv}B\) or \(z\in\operatorname{conv}A+B\), then \(d_p(z,A+B)\le\max\{a,b\}\), so the desired upper bound follows.

Otherwise, apply the **planar parallelogram reduction theorem**, proved as Lemma 2.4 of Meyer [1]. It provides distinct \(a_1,a_2\in A\) and \(b_1,b_2\in B\) such that
\[
 z\in[a_1,a_2]+[b_1,b_2],\quad
 \|a_2-a_1\|_p\le2a,\qquad\|b_2-b_1\|_p\le2b.
\]
The four vertices of this parallelogram lie in \(A+B\). One of the two triangles cut along the diagonal joining \(a_1+b_2\) and \(a_2+b_1\) contains \(z\). Both sides of that triangle issuing from its appropriate corner are parallel to the two segment vectors, and have lengths \(r\le2a\), \(s\le2b\). Equation (1) and monotonicity of \(F_p\) imply
\[
 d_p(z,A+B)^p\le2^{-p-1}((r+s)^p+|r-s|^p)
 \le2^{-p-1}((2a+2b)^p+|2a-2b|^p)
 =F_p(a,b).
\]
Taking the supremum over \(z\) proves the universal inequality.

**3. Sharpness for every pair of radii.** Let \(c=2^{1-1/p}\), \(u=(ca,ca)\), \(v=(cb,-cb)\) and define \(A=\{0,u\}\), \(B=\{0,v\}\). The segment-midpoint formula gives \(d_p(A)=\|u\|_p/2=a\) and \(d_p(B)=\|v\|_p/2=b\), including degeneracies. The midpoint \(m=(u+v)/2\) belongs to the convex hull of the four-point sum \(A+B=\{0,u,v,u+v\}\). Its distances to the four points are all equal, since
\[
 \|u+v\|_p^p=\|u-v\|_p^p
 =c^p((a+b)^p+|a-b|^p).
\]
Consequently,
\[
 d_p(m,A+B)^p=2^{-p}\|u+v\|_p^p=F_p(a,b).
\]
This matches the proved universal upper bound and establishes the claim. \(\square\)

## Verification
The proof has been reconstructed separately for the triangle lemma, the two trivial Minkowski-sum regions, the imported planar parallelogram-reduction theorem, the monotonicity step, and exact attainment. The needed Hanner inequality is the standard direction for \(p\ge2\), not its reverse. A standalone checker `CHECK.py` verifies a rational fourth-power identity and the equality constructions for 216 parameter/exponent combinations, with 121 additional grid points per combination. Finite checks are illustrative and do not replace the analytic argument.

## Relationship to prior work
Meyer [1, Introduction and Proposition 1.1] proves the sharp coefficient \(\max\{1,2^{p-2}\}\), and realizes it with equal nonzero deficiency radii when \(p>2\). The introduction explicitly raises the possibility of a sharper bound **away from that diagonal**. His Lemma 2.4 is used without modification here. His Lemma 2.5 applies Clarkson's inequality to obtain the coefficient bound; keeping his preceding triangle inequality but substituting Hanner's stronger, radii-sensitive inequality [2] and appropriately scaling the extremal directions produces the present complete off-diagonal profile. The improvement is genuinely strict for positive unequal radii when \(p>2\), because the diagonal sharpness coefficient only saturates the Hanner envelope when the two radii agree. For \(p=2\), the formula reduces to the previously known Euclidean \(a^2+b^2\) bound [1,3]. No result in the inspected material states the sharp off-diagonal formula.

## Limitations
The new theorem depends on Meyer's published geometric reduction and on the classical Hanner inequality; it is a precise new synthesis, not an independent reproof of these ingredients. No complete uniqueness classification of equality cases is asserted, and the theorem does not generalize to arbitrary normed planes or higher dimensions. Literature coverage cannot certify absence of all unpublished or unindexed formulations; the novelty claim is restricted to the inspected sources and targeted searches. Independent mathematical audit has not been performed.

## References
[1] M. Meyer, *A sharp \(p\)-subadditive bound for the \(\ell_p\) Hausdorff distance from convex hull*, arXiv:2604.20387v2 (first posted 2026-04-22), especially Proposition 1.1, Lemmas 2.4–2.5 and the introduction. https://arxiv.org/html/2604.20387v2

[2] O. Hanner, *On the uniform convexity of \(L^p\) and \(\ell^p\)*, Arkiv för Matematik 3 (1956), 239–244, DOI 10.1007/BF02589410. The \(p\ge2\) form of Hanner's inequality is used above.

[3] M. Meyer, *The Dyn–Farkhi conjecture and the convex hull of a sumset in two dimensions*, Proceedings of the American Mathematical Society 153 (2025), 4889–4901; initial arXiv version 2024-07-09, arXiv:2407.07033.
