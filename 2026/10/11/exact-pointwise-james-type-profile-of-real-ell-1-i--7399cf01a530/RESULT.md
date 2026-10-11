# Exact pointwise James type profile of real \(\ell_1(I)\)
## Finding
Let \(I\) be an index set with \(|I|\ge 2\), let \(X=\ell_1(I;\mathbb R)\), and for \(x\in S_X\) put \(m(x)=\inf_{i\in I}|x_i|\). For every \(-\infty\le t<\infty\), the pointwise James type constant is exactly \[J(x,X,t)=2M_t\bigl(1,1-m(x)\bigr),\] where \(M_t\) is the generalized power mean, with the geometric-mean and minimum conventions at \(t=0\) and \(t=-\infty\). Thus, when \(I\) is infinite, \(m(x)=0\) for every \(x\in S_X\) and hence \(J(x,X,t)=2\) for every point and every parameter. When \(I=\{1,\dots,n\}\), the profile depends only on the smallest coordinate modulus: its maximum is \(2\), attained exactly when some coordinate vanishes, and its minimum is \(2M_t(1,1-1/n)\), attained exactly when \(|x_i|=1/n\) for every \(i\).

For finite nonzero \(t\), this can be written as
\[
J(x,X,t)=2\left(\frac{1+(1-m(x))^t}{2}\right)^{1/t}.
\]
At \(t=0\) it becomes \(2\sqrt{1-m(x)}\), and at \(t=-\infty\) it becomes \(2(1-m(x))\).

## Assumptions and scope
The space is real \(\ell_1(I)\) with \(|I|\ge2\). The pointwise James type constant is the quantity introduced by Rincón-Villamizar,
\[
J(x,X,t)=\sup_{y\in S_X} M_t\bigl(\lVert x-y\rVert,\lVert x+y\rVert\bigr),
\]
with the standard continuous extension of the generalized mean when one argument is zero. The claim covers the full parameter range \(-\infty\le t<\infty\). It makes no assertion for complex \(\ell_1\).

## Proof
First suppose \(I=\{1,\dots,n\}\) and write \(m=m(x)\). The case \(m=0\) is immediate from the upper bound \(\lVert x\pm y\rVert_1\le2\) and the witness \(y=\pm e_j\) at a zero coordinate, so assume \(m>0\).

Fix \(y\in S_X\). Put \(A=\lVert x+y\rVert_1\) and \(B=\lVert x-y\rVert_1\). For every coordinate set \(u_i=\min\{|x_i|,|y_i|\}\). When \(y_i\ne0\), let \(\varepsilon_i\in\{-1,1\}\) be the sign of \(x_i y_i\); coordinates with \(y_i=0\) contribute nothing. Define
\[
P=\sum_{\varepsilon_i=1}u_i,\qquad N=\sum_{\varepsilon_i=-1}u_i.
\]
The scalar identities
\[
|x_i+y_i|+|x_i-y_i|=2\max\{|x_i|,|y_i|\},
\]
and
\[
|x_i+y_i|-|x_i-y_i|=2\varepsilon_i u_i
\]
give
\[
A+B=4-2(P+N),\qquad |A-B|=2|P-N|.
\]
Consequently,
\[
\min\{A,B\}=2-(P+N)-|P-N|=2-2\max\{P,N\}.
\]
We claim \(\max\{P,N\}\ge m\). If both \(P<m\) and \(N<m\), then no nonzero coordinate of \(y\) can satisfy \(|y_i|\ge|x_i|\), because then \(u_i=|x_i|\ge m\) would already occur in one of the two sums. Hence \(u_i=|y_i|\) for every nonzero coordinate of \(y\), so \(P+N=\lVert y\rVert_1=1\). But \(P+N<2m\le 2/n\le1\), a contradiction. Therefore
\[
\min\{A,B\}\le2(1-m),\qquad \max\{A,B\}\le2.
\]
The generalized mean is symmetric and increasing in each argument, so
\[
M_t(A,B)\le M_t\bigl(2,2(1-m)\bigr)=2M_t(1,1-m).
\]
Choose an index \(j\) with \(|x_j|=m\) and take \(y=\operatorname{sgn}(x_j)e_j\). Then the two shifted norms are exactly \(2\) and \(2(1-m)\), giving equality.

Now suppose \(I\) is infinite. Every \(x\in\ell_1(I)\) satisfies \(m(x)=0\). Given \(\varepsilon>0\), choose \(i\in I\) with \(|x_i|<\varepsilon\) and take \(y=\operatorname{sgn}(x_i)e_i\), with either sign if \(x_i=0\). The shifted norms are \(2\) and \(2(1-|x_i|)\). Their generalized mean tends to \(2\) as \(|x_i|\to0\), while the triangle inequality gives the universal upper bound \(2\). Hence \(J(x,X,t)=2\) for every \(x\) and every parameter.

For finite \(n\), the constraint \(\sum_i|x_i|=1\) gives \(0\le m(x)\le1/n\). Since \(M_t(1,s)\) is increasing in \(s\), the maximum occurs at \(m=0\), and the minimum occurs at \(m=1/n\). The equality \(m=1/n\) forces and is forced by \(|x_i|=1/n\) for all \(i\).

## Verification
The proof was reconstructed directly from the definition. Its only nontrivial finite-dimensional step is the exact identity \(\min\{A,B\}=2-2\max\{P,N\}\) and the contradiction showing \(\max\{P,N\}\ge m\). Both are algebraic consequences of the coordinate formulas above. The maximizing coordinate vector is explicit. The infinite-dimensional case uses only the fact that an \(\ell_1\) vector on an infinite index set has coordinate infimum zero. No finite enumeration or numerical experiment is used as proof.

## Relationship to prior work
Rincón-Villamizar introduced the pointwise James type constant and proved, among other facts, continuity, a finite-dimensional extreme-point reduction for \(t\ge1\), and constancy on convex-transitive spaces. The same paper records global James type constants for \(\ell_p\) and \(L_p\), but does not give the pointwise \(\ell_1\) profile above. The formula here is stronger than the global equality because it determines every base point and covers \(t<1\), where the paper's extreme-point reduction is not available.

Tang, Ji, and Wang earlier studied pointwise nonsquare constants and reported exact \(\ell_p\) and \(L_p\) values. Only an abstract was available for comparison. That older work may overlap the \(t=-\infty\) specialization, but it predates the full pointwise James type power-mean family; no evidence found in the inspected material covers the unified all-parameter formula stated here.

## Limitations
The claim is restricted to real \(\ell_1(I)\). It does not classify pointwise James type profiles in general \(L_1\) spaces or complex sequence spaces. The full text of the 2004 pointwise-nonsquare paper was unavailable, leaving a residual literature risk specifically around the \(t=-\infty\) endpoint; the novelty assessment is for the unified all-parameter profile and its finite/infinite classification.

## References
1. M. A. Rincón-Villamizar, “The pointwise James type constant,” Analysis Mathematica 49 (2023), 651–659, DOI: 10.1007/s10476-023-0221-7.
2. X. Tang, D. Ji, and S. Wang, “Pointwise nonsquare constant in normed space,” Acta Analysis Functionalis Applicata 6 (2004), 10–15.
