# Exact skew constant on the square plane and a sharp-attainment obstruction

## Finding
For the real Banach plane \(X=\ell_\infty^2\) and every \(\alpha,\beta>0\), define
\[
B_{\alpha-\beta}(X)=\sup\left\{\frac{\|\alpha x+\beta y\|_\infty-\|\beta x-\alpha y\|_\infty}{\alpha}:x,y\in S_X,\ x\perp_B y}\right\}.
\]
Then
\[
B_{\alpha-\beta}(\ell_\infty^2)=\min\left\{1,\frac{2\beta}{\alpha}\right\}.
\]
Writing \(r=\beta/\alpha\), the upper bound \(1\) is attained exactly for \(r\ge1/2\). For every \(1/2\le r<1\), this attainment contradicts the necessity direction of Theorem 2 in Zhou--Ni--Liu (2024), which requires two specific boundary segments. On \(\ell_\infty^2\) that two-segment condition is impossible when \(r<1\).

## Assumptions and scope
The scalar field is real. The norm is \(\|(s,t)\|_\infty=\max\{|s|,|t|\}\). Birkhoff orthogonality means \(x\perp_B y\) when \(\|x+\lambda y\|_\infty\ge\|x\|_\infty\) for every \(\lambda\in\mathbb R\). Parameters satisfy \(\alpha,\beta>0\). The claim concerns only this two-dimensional square plane and the constant above; it does not assert a replacement characterization for arbitrary Banach spaces.

## Proof
Set \(r=\beta/\alpha>0\). Homogeneity gives
\[
\frac{\|\alpha x+\beta y\|_\infty-\|\beta x-\alpha y\|_\infty}{\alpha}
=\|x+r y\|_\infty-\|r x-y\|_\infty.
\]
The general estimate in the defining paper gives an upper bound of \(1\). When \(0<r\le1\), the triangle and reverse-triangle inequalities give
\[
\|x+r y\|_\infty\le1+r,
\qquad
\|r x-y\|_\infty\ge1-r,
\]
so the difference is at most \(2r\). Hence
\[
B_{\alpha-\beta}(\ell_\infty^2)\le\min\{1,2r\}.
\]

For \(0<r\le1/2\), take
\[
x=(1,-1),\qquad y=(2r-1,-1).
\]
Both vectors are unit vectors. To verify \(x\perp_B y\), let \(a=2r-1\in[-1,0]\). If \(\lambda\ge0\), then the second coordinate of \(x+\lambda y\) has absolute value \(1+\lambda\). If \(\lambda<0\), then its first coordinate equals \(1+a\lambda\ge1\). Thus \(\|x+\lambda y\|_\infty\ge1\) for every real \(\lambda\). Directly,
\[
\|x+r y\|_\infty=1+r,
\qquad
\|r x-y\|_\infty=1-r,
\]
so the difference is \(2r\).

For \(r\ge1/2\), take
\[
x=(1,-1),\qquad y=(1,0).
\]
Again \(x\perp_B y\), because the second coordinate of \(x+\lambda y\) is always \(-1\). Moreover,
\[
\|x+r y\|_\infty=1+r,
\qquad
\|r x-y\|_\infty=\max\{|r-1|,r\}=r,
\]
where the last equality uses \(r\ge1/2\). The difference is therefore \(1\). This proves the exact formula for all \(r>0\).

It remains to compare with the published boundary-segment criterion. Suppose \(0<r<1\) and both \([x,y]\) and \([x,x-(2/r)y]\) were contained in the unit sphere of \(\ell_\infty^2\). A nontrivial line segment contained in the boundary of the square lies in one of its four faces, so \([x,y]\subset S_X\) forces some coordinate \(j\) to satisfy \(x_j=y_j=s\) with \(s\in\{-1,1\}\). For \(z=x-(2/r)y\), that coordinate is
\[
z_j=s\left(1-\frac2r\right),
\]
and \(0<r<1\) implies \(|z_j|>1\), contradicting \(z\in S_X\). If \(x=y\), the same endpoint calculation gives the same contradiction. Hence the two-segment condition is impossible for \(r<1\). Combining this with the exact formula, every \(1/2\le r<1\) is a counterexample to the necessity direction of the published theorem.

## Verification
The proof is analytic and covers every positive parameter pair. The bundled script `verify.py` checks the two extremizing constructions on a dense rational test set, verifies Birkhoff orthogonality by the same sign split used above, checks the closed form, and tests the boundary-segment endpoint obstruction. These finite checks are regression tests only and are not used to establish the quantified theorem.

## Relationship to prior work
Zhou, Ni, and Liu introduced \(B_{\alpha-\beta}(X)\), proved \(0\le B_{\alpha-\beta}(X)\le1\), and gave a square-plane example only for their skew-orthogonality relation, not an evaluation of \(B_{\alpha-\beta}(\ell_\infty^2)\). Their Theorem 2 states that attainment of the upper bound is equivalent to the existence of two boundary segments \([x,y]\) and \([x,x-(2\alpha/\beta)y]\). The exact formula above shows a parameter interval on the canonical square plane where attainment occurs although that segment condition is impossible. Targeted searches for the exact formula, its normalized form, the square-plane specialization, and a corrigendum did not locate prior coverage.

## Limitations
The result does not classify upper-bound attainment in arbitrary Banach spaces. It identifies the complete parameter profile on \(\ell_\infty^2\) and a concrete failure of one direction of the published criterion. A later correction or poorly indexed equivalent computation could reduce the originality claim; no such source was found in the checked literature.

## References
1. Y. Zhou, Q. Ni, and Q. Liu, “The skew constant and orthogonalities in Banach spaces,” *Open Journal of Mathematical Sciences* 8 (2024), 1–7, DOI 10.30538/oms2024.0219. Published 15 May 2024.
