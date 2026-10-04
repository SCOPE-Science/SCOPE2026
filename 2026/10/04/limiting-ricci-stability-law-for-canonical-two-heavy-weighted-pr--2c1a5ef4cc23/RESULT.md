# Limiting Ricci-stability law for canonical two-heavy weighted projective spaces
## Finding
For every integer \(r\ge2\), consider the canonical weighted projective spaces
\[
X_{r,a,b}=\mathbb P(1^r,a,b),\qquad 1\le a\le b.
\]
Let \(R(X)\) be the greatest lower bound on Ricci curvature in the anticanonical class, interpreted for the singular toric Fano variety by the log-Fano extension of the toric continuity invariant. Then
\[
R(X_{r,a,b})=\frac{r+2}{r+a+b}.
\]
If every canonical pair \((a,b)\) is given equal weight, these values have a nondegenerate limiting distribution. Writing \(d=b-a\), scale \(x=d/r\) and \(y=a/r\). The empirical laws converge weakly to the push-forward of normalized area \((2/3)\,dx\,dy\) on
\[
D=\{(x,y):0\le x\le1,\ 0\le y\le1+x\}
\]
under
\[
f(x,y)=\frac1{1+x+2y}.
\]
Thus the limiting support is \([1/6,1]\). If \(R_\infty\) denotes the limiting random variable and \(L=t^{-1}-1\), then
\[
\Pr(R_\infty\ge t)=
\begin{cases}
1,&0<t\le1/6,\\
(-L^2+10L-7)/18,&1/6<t\le1/3,\\
(2L-1)/6,&1/3<t\le1/2,\\
L^2/6,&1/2<t\le1,\\
0,&t>1.
\end{cases}
\]
The limiting mean is
\[
\mathbb E(R_\infty)=\frac{\log3}{3}.
\]
For finite \(r\), the sharp range is
\[
\frac{r+2}{6r}\le R(X_{r,a,b})\le1,
\]
with the lower equality unique at \((a,b)=(2r,3r)\) and the upper equality unique at \((a,b)=(1,1)\).

## Assumptions and scope
Weights are positive integers with \(r\ge2\) and \(1\le a\le b\). The coarse weighted projective space is Fano and toric. Only members with at worst canonical singularities are included in the empirical measure; hence they are klt, so the singular log-Fano Ricci invariant of Berman--Berndtsson applies with boundary divisor zero. The limiting probability measure is the uniform counting measure on weight pairs, not a moduli-theoretic or volume-weighted measure.

The canonical range is rederived here rather than assumed. Put \(d=b-a\). The two nontrivial quotient charts are the \(a\)- and \(b\)-coordinate charts. Reid--Tai gives the ages
\[
\operatorname{age}_a(k)=\frac{rk+(kd\bmod a)}a,
\qquad
\operatorname{age}_b(k)=\frac{rk+(ka\bmod b)}b.
\]
Checking all nonidentity elements shows that canonicity is equivalent to
\[
0\le d\le r,\qquad 1\le a\le r+d.
\]

## Proof
First derive the Ricci invariant from the canonical toric simplex. Let the ray generators be \(v_0,\ldots,v_{r+1}\), and let the weights be \(q_i\), so the weighted-projective fan relation is
\[
\sum_i q_i v_i=0.
\]
For the anticanonical simplex \(P\), every facet has equation \(\langle u,v_i\rangle\ge-1\). If \(p_i\) is the vertex opposite the \(i\)-th facet and \(S=\sum_iq_i\), pairing the fan relation with \(p_i\) gives
\[
\langle p_i,v_i\rangle=\frac{S}{q_i}-1.
\]
Consequently the barycentric coordinate of the origin with respect to the vertices \(p_i\) is \(q_i/S\), whereas the barycenter \(B\) of the simplex has every barycentric coordinate equal to \(1/N\), where \(N=r+2\) is the number of rays.

Parametrize the line from \(B\) through the origin by \(Q(t)=(1-t)B\), so the origin occurs at \(t=1\). Along this line the \(i\)-th barycentric coordinate is
\[
\lambda_i(t)=\frac{1-t}{N}+\frac{tq_i}{S}.
\]
The first boundary hit beyond the origin occurs for a minimum weight. Here the minimum weight is \(1\). If \(S>N\), the corresponding parameter is \(t_*=S/(S-N)\), and the convex-body formula of Li, extended to singular toric log Fano varieties by Berman--Berndtsson, gives
\[
R(X)=\frac{|OQ|}{|BQ|}=\frac{t_*-1}{t_*}=\frac NS.
\]
When all weights are \(1\), the barycenter is the origin and the same expression gives \(R=1\). Thus for \(q=(1^r,a,b)\),
\[
R(X_{r,a,b})=\frac{r+2}{r+a+b}=\frac{r+2}{r+2a+d}.
\]

For completeness, the canonical lattice region follows directly from the two age tests. If \(d=0\), both heavy charts have age \(rk/a\), so canonicity is equivalent to \(a\le r\). Assume \(d>0\). In the \(b\)-chart, the element \(k=1\) forces \(d\le r\). Conversely, if \(d\le r\) and \(b\nmid kd\), then
\[
\operatorname{age}_b(k)=\frac{rk}{b}+1-\left\{\frac{kd}{b}\right\}\ge1+\frac{k(r-d)}b\ge1.
\]
If \(b\mid kd\), writing \(g=\gcd(b,d)\) gives \(k\ge b/g\), hence \(\operatorname{age}_b(k)\ge r/g\ge1\). In the \(a\)-chart, when \(d\ge a\) the condition \(d\le r\) already gives every age at least one. When \(0<d<a\), the element \(k=1\) forces \(a\le r+d\); under this inequality, if \(kd<a\) then \(k(r+d)/a\ge1\), while if \(kd\ge a\), the bound \(r\ge d\) gives \(rk/a\ge1\). Hence the unified region is exactly
\[
0\le d\le r,\qquad1\le a\le r+d.
\]
Its cardinality is \(\sum_{d=0}^{r}(r+d)=3r(r+1)/2\).

Now scale \(x=d/r\) and \(y=a/r\). The normalized lattice points form Riemann sums on \(D\), whose area is \(3/2\), while
\[
\frac{r+2}{r+2a+d}\longrightarrow\frac1{1+x+2y}.
\]
Therefore the empirical measures converge weakly to the stated push-forward measure.

For the survival function, \(f(x,y)\ge t\) is equivalent to \(x+2y\le L\), where \(L=t^{-1}-1\). Intersecting this half-plane with \(D\) gives area
\[
A(L)=
\begin{cases}
L^2/4,&0\le L\le1,\\
L/2-1/4,&1\le L\le2,\\
-L^2/12+5L/6-7/12,&2\le L\le5,\\
3/2,&L\ge5.
\end{cases}
\]
Multiplication by the normalizing density \(2/3\) gives the displayed survival function. Finally,
\[
\frac23\int_0^1\int_0^{1+x}\frac{dy\,dx}{1+x+2y}
=\frac23\int_0^1\frac{\log3}{2}\,dx
=\frac{\log3}{3}.
\]
The finite extrema follow because \(r+2a+d\) is strictly increasing in \(a\) and \(d\) on the canonical lattice region. Its minimum is \(r+2\) uniquely at \((d,a)=(0,1)\), and its maximum is \(6r\) uniquely at \((d,a)=(r,2r)\).

## Verification
The accompanying checker independently evaluates the Reid--Tai ages by integer residues and compares them with the closed canonical region on a finite exact test box. It also checks the canonical count, the unique finite extrema, continuity of the three nontrivial survival pieces at their breakpoints, and numerical convergence of the empirical mean toward \(\log(3)/3\). These computations are consistency checks only; the infinite statement is proved above by the age inequalities and Riemann-sum argument.

## Relationship to prior work
Li proved the barycenter-to-boundary formula for the greatest lower Ricci bound of smooth toric Fano manifolds. Berman--Berndtsson generalized that convex-body invariant to toric log Fano varieties and identified it with the singular Ricci lower-bound invariant. Rossi--Terracini give the weighted-projective fan relation \(\sum q_i v_i=0\), which specializes the convex-body formula to weighted projective simplices.

Those general results account for the single-space formula \(R=(r+2)/(r+a+b)\); that specialization is not claimed as a new theorem by itself. The result here is the exact limiting law, sharp finite range, and mean for the complete canonical two-heavy family after an independent Reid--Tai description of its lattice region. The inspected sources do not state this family-level distribution.

## Limitations
The probability law uses uniform counting of integer weight pairs. A different weighting, such as anticanonical-volume weighting or a stack/moduli measure, would lead to a different distribution. The result concerns the two-heavy family \(\mathbb P(1^r,a,b)\) and does not assert an analogous law for arbitrary weighted projective spaces. The literature comparison cannot exclude an equivalent calculation hidden under substantially different terminology; the strongest nearby published inputs located were the general toric formula and the weighted-projective fan description cited below.

## References
1. C. Li, *Greatest lower bounds on Ricci curvature for toric Fano manifolds*, arXiv:0909.3443, first public 2009-09-18. Theorem 1 gives the barycenter-to-boundary formula in the smooth toric Fano case.
2. M. Rossi and L. Terracini, *Weighted Projective Spaces from the toric point of view with computational applications*, arXiv:1112.1677, first public 2011-12-07. Proposition 2.5 gives the fan relation \(\sum q_i v_i=0\).
3. R. J. Berman and B. Berndtsson, *Real Monge-Ampère equations and Kähler-Ricci solitons on toric log Fano varieties*, arXiv:1207.6128, first public 2012-07-25. Section 2.10 defines \(R_P\), and Theorems 3.7--3.8 identify it with the toric log-Fano continuity/Ricci invariant.