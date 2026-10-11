# Sharp Dragomir approximate-symmetry parameter of the Day--James ell_2--ell_1 plane
## Finding
Let \(X=\ell_2-\ell_1\) be the real Day--James plane with
\[
\|(s,t)\|_X=
\begin{cases}
\sqrt{s^2+t^2},&st\ge0,\\
|s|+|t|,&st\le0.
\end{cases}
\]
For \(\varepsilon\in[0,1)\), write \(u\perp_D^\varepsilon v\) when
\[
\|u+\lambda v\|_X\ge\sqrt{1-\varepsilon^2}\,\|u\|_X
\qquad(\lambda\in\mathbb R).
\]
Then the least \(\varepsilon\) for which
\[
x\perp_B y\Longrightarrow y\perp_D^\varepsilon x
\qquad(x,y\in X)
\]
is
\[
\varepsilon_D(X)=\frac1{\sqrt2}.
\]
Equivalently,
\[
\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\inf_{\lambda\in\mathbb R}\|y+\lambda x\|_X
=
\frac1{\sqrt2}.
\]
Equality is attained by
\[
x=(1,0),
\qquad
y=\frac{(1,1)}{\sqrt2},
\]
and by the norm symmetries.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|_X\ge\|x\|_X
\qquad(\lambda\in\mathbb R).
\]
The approximate relation is the modified Dragomir relation
\[
u\perp_D^\varepsilon v
\quad\Longleftrightarrow\quad
\|u+\lambda v\|_X\ge\sqrt{1-\varepsilon^2}\,\|u\|_X
\qquad(\lambda\in\mathbb R).
\]
Only the real two-dimensional Day--James space \(\ell_2-\ell_1\) is treated.

## Proof
For a unit Birkhoff pair define
\[
d(x,y)=\inf_{\lambda\in\mathbb R}\|y+\lambda x\|_X.
\]
Then
\[
\sqrt{1-\varepsilon_D(X)^2}
=
\inf_{\substack{x,y\in S_X\\x\perp_B y}}d(x,y).
\]

The dual norm is
\[
\|(p,q)\|_{X^*}
=
\begin{cases}
\sqrt{p^2+q^2},&pq\ge0,\\
\max\{|p|,|q|\},&pq\le0.
\end{cases}
\]
This follows by maximizing a functional over the Euclidean quarter-disks and the opposite-sign taxicab simplices forming the unit ball.

The unit sphere has three strata: smooth Euclidean arcs, smooth taxicab facets, and the four coordinate-axis junctions.

First take a smooth Euclidean-arc point. By symmetry,
\[
x=(\cos\theta,\sin\theta),
\qquad
0<\theta<\frac{\pi}{2}.
\]
Its unique norming functional is \((\cos\theta,\sin\theta)\), so the unit Birkhoff direction is
\[
y=
\frac{(-\sin\theta,\cos\theta)}
{\sin\theta+\cos\theta}.
\]
The functional \(\phi=(-\sin\theta,\cos\theta)\) annihilates \(x\). Hence
\[
d(x,y)
=
\frac{|\phi(y)|}{\|\phi\|_{X^*}}
=
\frac1{(\sin\theta+\cos\theta)\max\{\sin\theta,\cos\theta\}}
\ge\frac1{\sqrt2}.
\]

Next take a smooth point on an opposite-sign taxicab facet. By symmetry,
\[
x=(-a,b),
\qquad
a,b>0,
\qquad
a+b=1.
\]
Its unique norming functional is \((-1,1)\), so the unit Birkhoff direction is
\[
y=\frac{(1,1)}{\sqrt2}.
\]
The annihilator \(\phi=(b,a)\) satisfies
\[
\|\phi\|_{X^*}=\sqrt{a^2+b^2},
\qquad
\phi(y)=\frac1{\sqrt2}.
\]
Thus
\[
d(x,y)
=
\frac1{\sqrt2\,\sqrt{a^2+b^2}}
\ge
\frac1{\sqrt2},
\]
since \(a+b=1\) implies \(a^2+b^2\le1\).

Finally take an axis junction. By symmetry,
\[
x=(1,0).
\]
The complete set of norming functionals at \(x\) is
\[
f_\tau(s,t)=s-\tau t,
\qquad
0\le\tau\le1.
\]
James' support-functional characterization therefore gives, up to sign,
\[
y=
\frac{(\tau,1)}{\sqrt{1+\tau^2}},
\qquad
0\le\tau\le1.
\]
The functional \((0,1)\) annihilates \(x\) and has dual norm \(1\), so
\[
d(x,y)=\frac1{\sqrt{1+\tau^2}}\ge\frac1{\sqrt2}.
\]
At \(\tau=1\), the pair
\[
x=(1,0),
\qquad
y=\frac{(1,1)}{\sqrt2}
\]
attains equality.

All unit-sphere strata have been covered. Hence the sharp reverse line distance is \(1/\sqrt2\), and
\[
\varepsilon_D(X)=\sqrt{1-\frac12}=\frac1{\sqrt2}.
\]

## Verification
For a two-dimensional normed space, if a nonzero functional \(\phi\) annihilates \(x\), then
\[
\inf_{\lambda\in\mathbb R}\|y+\lambda x\|
=
\frac{|\phi(y)|}{\|\phi\|_*}.
\]
The proof uses this quotient-space identity in every stratum, so the reverse distances are exact rather than merely bounded by test translates.

The sphere decomposition is exhaustive, and the axis analysis uses the entire norming-functional segment. No numerical optimization, finite sampling, or external certificate is used as proof.

## Relationship to prior work
Yang and Li study the complete \(\ell_p-\ell_1\) Day--James family and explicitly define the same piecewise norm. Their article was published on 4 March 2015 and computes James-type and von Neumann--Jordan-type constants rather than approximate Birkhoff--James symmetry.

Chmieliński, Khurana, and Sain define the modified Dragomir approximate relation, recall James' support-functional characterization, and prove that every finite-dimensional Banach space is globally D-approximately symmetric. Their inspected full text does not contain an \(\ell_2-\ell_1\) example and does not determine this sharp parameter.

Targeted searches using the Day--James and \(\ell_2-\ell_1\) names, modified Dragomir terminology, reverse Birkhoff line distance, and the value \(1/\sqrt2\) did not locate an equivalent exact evaluation.

## Limitations
The theorem concerns the modified Dragomir relation on the real plane \(\ell_2-\ell_1\). It does not compute the distinct Chmieliński approximate-symmetry parameter or an all-\(p\) formula for \(\ell_p-\ell_1\).

A differently notated exact calculation outside the checked sources remains a bibliographic risk.

## References
1. C. Yang and H. Li, “On the James type constant of \(\ell_p-\ell_1\),” *Journal of Inequalities and Applications* 2015, Article 79, DOI 10.1186/s13660-015-0598-3; published 2015-03-04.
2. J. Chmieliński, D. Khurana, and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162, first posted 2020-12-15.
