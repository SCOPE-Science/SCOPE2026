# Exact Euclidean Banach--Mazur distance of the cubic Day--James \(\ell_1-\ell_3\) plane
## Finding
Let \(X\) be the real Day--James plane
\[
\|(x,y)\|_X=
\begin{cases}
|x|+|y|,&xy\ge0,\\
\bigl(|x|^3+|y|^3\bigr)^{1/3},&xy\le0.
\end{cases}
\]
Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=1+2^{-4/3}.
\]
An optimal Euclidean pullback is
\[
H_*(x,y)^2=(x+y)^2+2^{-4/3}(x-y)^2.
\]
Equivalently,
\[
d_{\mathrm{BM}}(X,\ell_2^2)=\sqrt{1+2^{-4/3}}
=1.181884200331001\ldots .
\]

The sign change \((x,y)\mapsto(x,-y)\) is an isometry from this \(\ell_1-\ell_3\) Day--James plane onto the reversed \(\ell_3-\ell_1\) presentation, so the same value holds for either ordering convention.

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The Day--James convention is that the first norm is used on the same-sign quadrants and the second on the opposite-sign quadrants. The theorem concerns the cubic member \(\ell_1-\ell_3\); it does not assert a formula for every \(\ell_1-\ell_p\) plane.

For a positive-definite quadratic form \(Q\), put
\[
m(Q)=\inf_{\|w\|_X=1}Q(w),\qquad
M(Q)=\sup_{\|w\|_X=1}Q(w).
\]
Then the squared distortion of the corresponding Euclidean pullback is \(M(Q)/m(Q)\).

## Proof
The norm of \(X\) is invariant under the coordinate swap
\[
S(x,y)=(y,x).
\]
If
\[
m\|w\|_X^2\le Q(w)\le M\|w\|_X^2
\]
for every \(w\), then the same inequalities hold for \(Q\circ S\). Hence the averaged quadratic form
\[
\overline Q=\frac{Q+Q\circ S}{2}
\]
has distortion no larger than that of \(Q\). Therefore the Banach--Mazur infimum may be taken over swap-invariant positive-definite quadratic forms.

Write
\[
U=x+y,\qquad V=x-y.
\]
Every swap-invariant positive-definite quadratic form is, after a positive scalar rescaling,
\[
H_t(x,y)^2=U^2+tV^2,\qquad t>0.
\]

On the same-sign sector \(xy\ge0\), one has \(|U|\ge|V|\) and
\[
\|(x,y)\|_X=|x|+|y|=|U|.
\]
With
\[
s=\frac{|V|}{|U|}\in[0,1],
\]
the squared comparison ratio is
\[
R_1(s;t)=\frac{H_t(x,y)^2}{\|(x,y)\|_X^2}=1+ts^2.
\]
Thus this sector contributes all values from \(1\) to \(1+t\).

On the opposite-sign sector \(xy\le0\), one has \(|V|\ge|U|\). Put
\[
r=\frac{|U|}{|V|}\in[0,1],\qquad u=r^2.
\]
Since
\[
|x|^3+|y|^3
=
\frac{|V|^3}{8}\bigl((1+r)^3+(1-r)^3\bigr)
=
\frac{|V|^3}{4}(1+3u),
\]
one obtains
\[
R_3(u;t)
=
\frac{H_t(x,y)^2}{\|(x,y)\|_X^2}
=
2^{4/3}\frac{t+u}{(1+3u)^{2/3}},
\qquad 0\le u\le1.
\]
Its logarithmic derivative is
\[
\frac{\partial}{\partial u}\log R_3(u;t)
=
\frac{1+u-2t}{(t+u)(1+3u)}.
\]

Suppose first that \(0<t\le1/2\). Then this derivative is nonnegative on the entire interval, so \(R_3\) is increasing and
\[
R_3(0;t)=2^{4/3}t,\qquad
R_3(1;t)=1+t.
\]
Consequently the global maximum is \(1+t\), while the global minimum is
\[
\min\{1,2^{4/3}t\}.
\]
Hence the squared distortion is
\[
D(t)=
\begin{cases}
\dfrac{1+t}{2^{4/3}t},&0<t\le2^{-4/3},\\[2mm]
1+t,&2^{-4/3}\le t\le1/2.
\end{cases}
\]
The first branch is strictly decreasing and the second strictly increasing. Their unique junction is
\[
t_*=2^{-4/3},
\]
where
\[
D(t_*)=1+2^{-4/3}.
\]

If \(t\ge1/2\), the same-sign sector alone contains the values \(1\) and \(1+t\), so
\[
D(t)\ge1+t\ge\frac32>1+2^{-4/3}.
\]
Thus \(t_*\) is the unique minimizing parameter among the swap-invariant quadratic forms. The averaging argument gives the global optimum:
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=1+2^{-4/3}.
\]

## Verification
The two sign sectors exhaust \(\mathbb R^2\), and their common boundary \(xy=0\) is consistent because the \(\ell_1\) and \(\ell_3\) norms agree on coordinate axes. The opposite-sign profile has an explicit derivative whose sign is globally controlled in the only parameter interval that can contain the optimum. The remaining interval \(t\ge1/2\) is eliminated by the two same-sign contact values.

At the optimum
\[
t_*=2^{-4/3}=0.3968502629920499\ldots,
\]
the global minimum of \(H_{t_*}^2/\|\cdot\|_X^2\) is \(1\) and the global maximum is
\[
1+t_*=1.3968502629920498\ldots.
\]
Thus
\[
d_{\mathrm{BM}}(X,\ell_2^2)
=
1.181884200331001\ldots .
\]
These decimals are consistency checks only; the proof is symbolic.

## Relationship to prior work
Nilsrakoo and Saejung's 2006 paper is an archival source for generalized Day--James norms and computes James-type constants rather than Euclidean Banach--Mazur distance. Alonso's 2011 paper gives the explicit \(\ell_p-\ell_q\) Day--James definition and a general representation theorem for normed planes, but no object-specific distance formula.

Mizuguchi's 2016 paper studies the same \(\ell_1-\ell_p\) Day--James family in its section on differences between Birkhoff and isosceles orthogonalities. The inspected proposition gives estimates for orthogonality-related constants; it does not state a Euclidean Banach--Mazur distance for the cubic member.

The closest exact Euclidean-distance comparisons located are the isolated \(\ell_2-\ell_1\) Day--James plane, the \(\ell_\infty-\ell_1\) endpoint, the conjugate \(\ell_3-\ell_{3/2}\) plane, and the different family \(\ell_p-\ell_\infty\) for \(p>2\). None implies the present \(\ell_1-\ell_3\) value. In particular, changing the sign of one coordinate interchanges the two Day--James exponents, so the \(\ell_p-\ell_\infty\) family is isometric to \(\ell_\infty-\ell_p\), not to \(\ell_1-\ell_3\).

## Limitations
The theorem is for the cubic member only. The algebraic simplification
\[
(1+r)^3+(1-r)^3=2(1+3r^2)
\]
is what makes the opposite-sign comparison profile rational in \(u=r^2\) and gives a one-sign derivative. A complete \(\ell_1-\ell_p\) phase diagram is not claimed.

The literature comparison cannot rule out an older equivalent computation under a different affine-geometric notation. No such statement was located in the checked same-family sources or exact-formula searches.

## References
1. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2006, Article ID 26265, DOI 10.1155/JIA/2006/26265; published 2006-05-04.
2. J. Alonso, “Any two-dimensional Normed space is a generalized Day-James space,” *Journal of Inequalities and Applications* 2011, Article 2, DOI 10.1186/1029-242X-2011-2.
3. H. Mizuguchi, “The Constants to Measure the Differences Between Birkhoff and Isosceles Orthogonalities,” *Filomat* 30 (2016), 2761--2770, DOI 10.2298/FIL1610761M.
