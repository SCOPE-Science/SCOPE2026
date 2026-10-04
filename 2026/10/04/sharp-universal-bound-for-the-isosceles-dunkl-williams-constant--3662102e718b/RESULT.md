# Sharp universal bound for the isosceles Dunkl–Williams constant
## Finding
For every real Banach space \(X\) with \(\dim X\ge 2\),
\[
DW_I(X)\le \frac94.
\]
The constant is sharp: for \(X=(\mathbb R^2,\|\cdot\|_\infty)\),
\[
DW_I(X)=\frac94.
\]
Thus \(9/4\) is the best universal upper bound for the isosceles Dunkl–Williams constant.

## Assumptions and scope
The scalar field is real. The constant \(DW_I(X)\) is the Dunkl–Williams constant restricted to nonzero isosceles-orthogonal pairs, where \(r\perp_I s\) means \(\|r+s\|=\|r-s\|\). The argument applies in arbitrary dimension at least two and uses no compactness, reflexivity, smoothness, strict convexity, or finite-dimensional assumption.

A useful equivalent form, proved by Fu, Xie and Li as Proposition 3.4, is
\[
DW_I(X)=\sup_{x,y\in S_X,\,x\ne\pm y}
\frac{\|x+y\|+\|x-y\|}{2}
\left\|\frac{x+y}{\|x+y\|}-\frac{x-y}{\|x-y\|}\right\|.
\]
It follows directly from the defining isosceles-orthogonal formulation by setting \(r=(x+y)/2\) and \(s=(x-y)/2\), and conversely normalizing \(r+s\) and \(r-s\).

## Proof
Fix \(x,y\in S_X\) with \(x\ne\pm y\), and put
\[
u=x+y,\qquad v=x-y,\qquad a=\|u\|,\qquad b=\|v\|.
\]
Then \(0<a,b\le2\). The expression inside the supremum is
\[
F=\frac{a+b}{2}\left\|\frac{u}{a}-\frac{v}{b}\right\|
 =\frac{a+b}{2ab}\|bu-av\|.
\]
The formula is symmetric under interchanging \(u,a\) and \(v,b\), so assume \(a\ge b\). Since \(u-v=2y\), the triangle inequality gives
\[
\|bu-av\|
 =\|b(u-v)+(b-a)v\|
 \le b\|u-v\|+(a-b)\|v\|
 =2b+(a-b)b.
\]
Consequently
\[
F\le \frac{a+b}{2a}(2+a-b).
\]
Write \(t=b/a\in(0,1]\). Since \(a\le2\),
\[
F\le \frac{1+t}{2}\bigl(2+a(1-t)\bigr)
\le(1+t)(2-t)
=2+t-t^2
=\frac94-\left(t-\frac12\right)^2
\le\frac94.
\]
Taking the supremum proves \(DW_I(X)\le9/4\).

For sharpness, take \(X=(\mathbb R^2,\|\cdot\|_\infty)\), \(x=(0,1)\), and \(y=(1,1)\). Then \(a=\|x+y\|_\infty=2\), \(b=\|x-y\|_\infty=1\), and
\[
\left\|\frac{x+y}{2}-\frac{x-y}{1}\right\|_\infty=\frac32.
\]
Hence the displayed expression equals \((3/2)(3/2)=9/4\), proving equality.

## Verification
The proof is analytic. Its only external mathematical input is the equivalent formulation of \(DW_I(X)\), whose statement and two-way normalization proof were checked in the full text of Fu–Xie–Li. The bound itself uses only the triangle inequality, \(\|x+y\|\le2\), and the exact identity
\[
\frac94-(2+t-t^2)=\left(t-\frac12\right)^2.
\]
The bundled script `verify.py` rechecks this identity and the \(\ell_\infty^2\) sharpness witness exactly with rational arithmetic; it is supplementary and is not a substitute for the infinite-dimensional proof.

## Relationship to prior work
Fu, Xie and Li introduced \(DW_I(X)\), proved the equivalent formula used above, established the earlier universal upper bound \(\sqrt2+1\), and computed \(DW_I(\ell_\infty^2)=9/4\). Immediately after that computation they explicitly suggested that \(9/4\), rather than \(\sqrt2+1\), should be the best universal upper bound, and stated that they could not prove the conjecture. Their closing discussion again asks for the best upper bound of \(DW_I(X)\). The present estimate closes that precise gap.

Sain, Ghosh and Paul provide closely related background on isosceles orthogonality and geometric constants; their article was published online on 1 September 2022. A later Fu–Xie–Li paper studies the Birkhoff-orthogonal constants \(DW_B(X)\) and \(DW_B^p(X)\), which are different invariants and do not imply the present isosceles-orthogonal bound.

## Limitations
No classification of equality cases is claimed. The argument proves the sharp universal numerical bound but does not characterize all spaces or all unit pairs attaining \(9/4\). Literature searches and citation-network checks cannot logically exclude every unindexed or unpublished duplication; the originality assessment rests on the explicit unresolved statement in the defining paper, targeted searches for equivalent formulations, and comparison with the later adjacent literature listed below.

## References
1. D. Sain, S. Ghosh, K. Paul, “On isosceles orthogonality and some geometric constants in a normed space,” *Aequationes Mathematicae* 97 (2023), 147–160. DOI: 10.1007/s00010-022-00909-y. Published online 1 September 2022.
2. Y. Fu, H. Xie, Y. Li, “The Dunkl-Williams constant related to the Singer orthogonality and red isosceles orthogonality in Banach spaces,” *Filomat* 37(17) (2023), 5601–5622. DOI: 10.2298/FIL2317601F. See Proposition 3.4, Example 3.5, and the discussion following Example 3.5.
3. Y. Fu, H. Xie, Y. Li, “The Dunkl–Williams Constant Related to Birkhoff Orthogonality in Banach Spaces,” *Bulletin of the Iranian Mathematical Society* 50(2) (2024). DOI: 10.1007/s41980-023-00853-w.
