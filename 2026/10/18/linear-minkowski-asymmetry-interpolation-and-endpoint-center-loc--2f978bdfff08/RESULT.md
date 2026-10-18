# Linear Minkowski-asymmetry interpolation and endpoint center-locus jump for homothetic frusta

## Finding
Let \(B\subset\mathbb R^{d-1}\) be an arbitrary convex body, \(d\ge2\), and let \(0\le\theta\le1\). Form the homothetic frustum
\[
K_\theta(B)=\operatorname{conv}(B\times\{0\},\ \theta B\times\{1\}).
\]
Write \(q=s(B)\) for the Minkowski asymmetry of the base and \(M(B)\) for its complete set of Minkowski centers (defined below). Then
\[
\boxed{s(K_\theta(B))=q+1-\theta.}
\]
Moreover, the **entire locus of minimizing centers** is
\[
\boxed{M(K_\theta(B))=\left\{\left(\frac{q+1}{q+2-\theta}b,\frac{1}{q+2-\theta}\right):b\in M(B)\right\}\quad(0\le\theta<1),}
\]
whereas at the prism endpoint it is
\[
\boxed{M(K_1(B))=M(B)\times\left[\frac1{q+1},\frac q{q+1}\right].}
\]
In particular, \(s(K_0(B))=q+1\) and \(s(K_1(B))=q\). For \(q>1\), the center locus gains **exactly one affine dimension** at the prism endpoint: all proper frusta have the same center-locus dimension as the base, but the limiting prism has a vertical interval of centers. For \(q=1\), no such jump occurs.

## Assumptions and scope
A convex body is a compact convex set with nonempty interior in its ambient Euclidean space. The Minkowski asymmetry is the affine-invariant quantity
\[
s(B)=\min\{r\ge1:\exists b\in\mathbb R^{d-1},\ -B+(r+1)b\subseteq rB\}.
\]
The points \(b\) achieving the minimum form \(M(B)\). Such points belong to \(B\): the inclusion implies \(b=(x+r y)/(r+1)\) for suitable \(x,y\in B\). No symmetry, smoothness, polyhedrality, or dimension-specific structure is required of \(B\). The formula is unchanged under invertible affine transformations, so allowing the homothetic top copy to have a different center or placing the planes at other positive separation gives an affinely equivalent situation. The cases \(\theta=0\) and \(\theta=1\) are included.

## Proof
Put \(\delta=1-\theta\). At height \(v\in[0,1]\), the horizontal section of the frustum is precisely \(r(v)B\), where \(r(v)=1-\delta v\).

**Lower bound and equality cases.** Suppose \(-(K_\theta-c)\subseteq \lambda(K_\theta-c)\), with \(c=(u,z)\) and \(\lambda\ge1\). Equivalently,
\[
-K_\theta+(\lambda+1)c\subseteq\lambda K_\theta. \tag{1}
\]
Reflecting a point of the upper face at height one and imposing the lower height bound yields
\[
z\ge\frac1{\lambda+1}.\tag{2}
\]
Reflecting the entire lower face \(B\times\{0\}\) through (1) produces points at height \((\lambda+1)z/\lambda\); comparison with the corresponding horizontal section of \(\lambda K_\theta\) yields
\[
-B+(\lambda+1)u\subseteq\bigl[\lambda-\delta(\lambda+1)z\bigr]B.\tag{3}
\]
By the definition of \(q\), the scalar coefficient in brackets must be at least \(q\). Combining (2) and (3) gives
\[
\lambda\ge q+\delta(\lambda+1)z\ge q+\delta.
\]
If \(\theta<1\) and \(\lambda=q+\delta\), all inequalities are equalities. Thus \(z=1/(q+2-\theta)\), and (3) says
\[
(q+2-\theta)u=(q+1)b\quad\text{for some }b\in M(B).\tag{4}
\]
If \(\theta=1\), the same argument gives \(\lambda\ge q\) and, at equality, \(u\in M(B)\). The upper and lower face heights under (1) then additionally force
\[
\frac1{q+1}\le z\le\frac q{q+1}.\tag{5}
\]

**Construction of every center for a proper frustum.** Fix \(b\in M(B)\), put \(\lambda=q+\delta\), and select
\[
c=\left(\frac{q+1}{\lambda+1}b,\frac1{\lambda+1}\right).
\]
For an arbitrary point \((r(v)y,v)\in K_\theta\), \(y\in B\), its reflected and \(\lambda\)-scaled image in (1) has height \(1-v\), and horizontal coordinate
\[
(q+1)b-r(v)y
=r(v)\bigl((q+1)b-y\bigr)+(1-r(v))(q+1)b.
\]
Since \((q+1)b-B\subseteq qB\) and \(b\in B\), convexity puts the right-hand side in
\[
\bigl[r(v)q+(1-r(v))(q+1)\bigr]B
=\bigl[q+\delta v\bigr]B
=\lambda r\!\left(\frac{1-v}{\lambda}\right)B.
\]
This is exactly the horizontal section of \(\lambda K_\theta\) at height \(1-v\), so (1) holds for all original points. Every center in (4) is therefore optimal and the formula for \(0\le\theta<1\) follows.

**Prism endpoint and jump.** If \(\theta=1\), every horizontal section is \(B\). For any \(b\in M(B)\), the horizontal part of (1) with \(\lambda=q\) is valid at every height. Its height part is valid precisely on interval (5). Consequently these, and only these, are the optimizing centers. Their affine dimension equals \(\dim\operatorname{aff}M(B)+1\) when \(q>1\), and equals that of \(M(B)\) when \(q=1\), proving the endpoint claim.

## Verification
The accompanying `verify.py` minimizes asymmetry **independently** for convex hulls by solving the vertex-facet containment linear program, with unknown center and asymmetry coefficient. The test cases are a scalene triangle, a generic quadrilateral, a square, and a pentagon, each with six top-to-bottom scale ratios, including both endpoints. The 24 independent three-dimensional optimization checks all pass (`VERIFY_OK 24 independent three-dimensional LP tests`). The script requires the packages in `requirements.txt` and can be run with `python verify.py`. Its numerical tolerance is \(10^{-7}\). These finite diagnostic checks are not a substitute for the preceding proof for every convex body and dimension.

## Relationship to prior work
Brandenberg, von Dichter and González Merino (2023, arXiv:2306.11460) study the classical Minkowski asymmetry and relations to symmetrizations and width/diameter, but their stated results do not give the full homothetic-frustum formula or its center-locus jump. Pavlov and Telen (2024, arXiv:2402.18955) study Santaló centers and polar-volume geometry, a different center functional. The publicly indexed study *Universal Santaló and volume-product laws for homothetic frusta* determines a universal Santaló center and volume product for precisely the present geometric construction, but its full examined proof concerns polar-volume minimizers, not minimal negative homothetic containment. Existing special cases for simplices, pyramids, centrally symmetric prisms, and regular bodies are subsumed without novelty claims for those special cases. A general older result hidden under 'Minkowski center of a cone', 'homothetic prismatoid', or 'asymmetry of a truncation' terminology cannot be ruled out; the originality assessment is subject to that risk.

## Limitations
The two parallel bases are homothetic and nested with common affine-center scaling, not arbitrary nonhomothetic prismatoids. The interpolation concerns Minkowski asymmetry, not Santaló displacement or Mahler volume product. Independent historical verification is not claimed, and the possibility that earlier textbooks contain an equivalent general containment observation remains. This is an exact self-contained structural lemma, not a claim of an independent external audit.

## References
1. R. Brandenberg, K. von Dichter and B. González Merino, *From inequalities relating symmetrizations of convex bodies to the diameter-width ratio for complete and pseudo-complete convex sets*, arXiv:2306.11460v1 (first public 2023-06-20); https://arxiv.org/html/2306.11460v2 .
2. D. Pavlov and S. Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955v1 (first public 2024-02-29); https://arxiv.org/html/2402.18955v2 .
3. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305v1 (2006), especially the classical pyramid Santaló endpoint; https://arxiv.org/abs/math/0606305 .
4. *Universal Santaló and volume-product laws for homothetic frusta*, publicly indexed mathematical result, 2026; distinct polar-volume invariant.
