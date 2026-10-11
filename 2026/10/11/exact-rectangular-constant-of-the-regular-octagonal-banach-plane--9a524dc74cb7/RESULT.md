# Exact rectangular constant of the regular octagonal Banach plane
## Finding
For the real regular-octagonal Banach plane \(X_8=(\mathbb R^2,N)\),
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\},
\]
the rectangular constant
\[
\mu(X)=\sup\left\{\frac{1+\lambda}{\|x+\lambda y\|}:x,y\in S_X,\ x\perp_B y,\ \lambda\ge0\right\}
\]
has the exact value
\[
\mu(X_8)=2\sqrt2-1.
\]
Equality is attained for
\[
x=(\sqrt2-1,1),\qquad y=(1/\sqrt2,-1/\sqrt2),\qquad \lambda=2(\sqrt2-1).
\]

## Assumptions and scope
The space is real and two-dimensional. Birkhoff--James orthogonality means \(x\perp_B y\) when \(\|x\|\le \|x+ty\|\) for every real \(t\). The unit ball of \(X_8\) is the regular octagon
\[
|s|\le1,\qquad |t|\le1,\qquad |s|+|t|\le\sqrt2.
\]
No assertion is made here for other regular polygons or for the generalized constants \(\mu_p\) with \(p\ne1\).

## Proof
A standard support-functional characterization says that \(x\perp_B y\) exactly when some norm-one supporting functional \(f\) at \(x\) satisfies \(f(y)=0\). The dihedral symmetry of the regular octagon reduces all such pairs to one edge and one adjacent vertex.

First suppose the supporting functional exposes an edge. By symmetry take the diagonal edge \(s+t=\sqrt2\), with
\[
x=(a,\sqrt2-a),\qquad \sqrt2-1\le a\le1,
\]
and one tangent unit direction \(y=(1/\sqrt2,-1/\sqrt2)\); the opposite direction is covered by swapping the coordinates. Put \(\lambda_0=\sqrt2(1-a)\). For \(0\le\lambda\le\lambda_0\), the point \(x+\lambda y\) remains on the unit edge, so its norm is \(1\). Hence the quotient is at most \(1+\lambda_0\le1+2(\sqrt2-1)=2\sqrt2-1\). For \(\lambda\ge\lambda_0\),
\[
N(x+\lambda y)\ge a+\lambda/\sqrt2.
\]
The function \((1+\lambda)/(a+\lambda/\sqrt2)\) is monotone on each such ray, so its supremum there is the larger of its value at \(\lambda_0\) and its limit \(\sqrt2\). Both are at most \(2\sqrt2-1\). At \(a=\sqrt2-1\) and \(\lambda=2(\sqrt2-1)\), the denominator is exactly \(1\), proving attainment.

It remains to treat supporting lines through a vertex whose normal lies strictly between the adjacent facet normals. By symmetry take \(x=(1,q)\), where \(q=\sqrt2-1\), and choose the sign of \(y\) so that \(y=(-u,v)\) lies between the vertical and diagonal tangent directions. The unit condition gives exactly two branches:
\[
(v,u)=(1,u),\quad 0\le u\le q,
\]
or
\[
v=\sqrt2-u,\quad q\le u\le1/\sqrt2.
\]
As long as the first coordinate of \(x+\lambda y\) is nonnegative, its norm is the maximum of two affine functions of \(\lambda\); after that point the second coordinate alone supplies a lower bound strong enough to make the quotient decrease. On the first branch these two controlling functions are
\[
1+\frac{1-u}{\sqrt2}\lambda,\qquad q+\lambda.
\]
Their intersection gives the unique maximum. The resulting maximum is an increasing function of \(u\), and at \(u=q\) it equals \(\sqrt2\).

On the second branch the two controlling functions are
\[
1+(1-\sqrt2u)\lambda,\qquad q+(\sqrt2-u)\lambda.
\]
They intersect at \(\lambda=\sqrt2/(1+u)\), and the corresponding quotient simplifies to
\[
R(u)=\frac{u+1+\sqrt2}{1+\sqrt2-u}.
\]
Since
\[
R'(u)=\frac{2(1+\sqrt2)}{(1+\sqrt2-u)^2}>0,
\]
its maximum is at \(u=1/\sqrt2\), where \(R(u)=2\sqrt2-1\). Thus every vertex-supported Birkhoff--James pair obeys the same upper bound, completing the proof.

## Verification
The bundled script `verify_rectangular.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\) to check the critical endpoint identities, the positivity of both one-variable derivatives, and the extremizing triple. These checks support the algebraic reductions above; the continuum argument itself is the displayed proof, not a finite sampling argument.

## Relationship to prior work
Baronti, Casini and Papini restate the rectangular constant and its generalized family \(\mu_p\), together with Hilbert-space, uniform-nonsquareness and hexagonal-norm results, but do not evaluate \(\mu\) on the regular octagonal plane. Paul, Ghosh and Sain prove attainment in finite dimensions and reduce the two-dimensional polyhedral problem to Birkhoff--James pairs based at extreme points; that reduction is compatible with, but does not contain, the exact octagonal value proved here. Del Río and Benítez settle the two-dimensional Hilbert-characterization problem for the rectangular constant and likewise do not give this octagonal evaluation.

A semantic comparison also finds regular-octagon results for other geometric constants, including \(T_G\) and parameterized von Neumann--Jordan quantities. The numerical coincidence \(2\sqrt2-1\) with one such distinct constant is not an implication: the admissible pairs and objective functions are different.

## Limitations
The calculation is specific to the regular octagonal norm. It does not classify all extremizing Birkhoff--James pairs, and it does not determine the full \(\mu_p(X_8)\) profile. Literature searches and inspections cannot exclude an unindexed earlier observation of the same exact value, although the most directly relevant two-dimensional and modern rectangular-constant papers inspected do not state it.

## References
1. M. Baronti, E. Casini, P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124–133. First published online 26 April 2021. DOI: 10.1017/S0004972721000253.
2. K. Paul, P. Ghosh, D. Sain, “On rectangular constant in normed linear spaces,” arXiv:1407.1353 (2014); later *Journal of Convex Analysis* 24 (2017), 917–925.
3. M. del Río, C. Benítez, “The rectangular constant for two-dimensional spaces,” *Journal of Approximation Theory* 19 (1977), 15–21. DOI: 10.1016/0021-9045(77)90025-9.
