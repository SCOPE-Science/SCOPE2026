# Sharp fixed-angle profile near minimal regular-simplex sections

## Finding
Let
\[
T_{n-1}=\operatorname{conv}\{e_1,\ldots,e_n\}\subset\mathbb R^n,\qquad n\ge3,
\]
and for every unit vector \(a\perp(1,\ldots,1)\) put
\[
V(a)=\operatorname{Vol}_{n-2}(T_{n-1}\cap a^\perp).
\]
Fix the facet-parallel minimizing normal
\[
a_*=\left(\sqrt{\frac{n-1}{n}},-\frac1{\sqrt{n(n-1)}},\ldots,-\frac1{\sqrt{n(n-1)}}\right)
\]
and write
\[
V_{\min}=\frac{\sqrt n}{(n-2)!}\left(\frac{n-1}{n}\right)^{n-\frac32}.
\]
Consider the open sign chamber consisting of normals whose first coordinate is positive and all remaining coordinates are negative. If \(a\) lies in this chamber and its spherical angle from \(a_*\) is \(\theta\), then for
\[
0<\theta<\theta_n:=\arctan\sqrt{\frac{n-2}{n}}
\]
one has the sharp fixed-angle inequality
\[
\frac{V(a)}{V_{\min}}\ge F_n(\theta):=
\frac{\sec\theta}{
\left(1+\sqrt{\frac{n-2}{n}}\tan\theta\right)
\left(1-\frac{\tan\theta}{\sqrt{n(n-2)}}\right)^{n-2}}.
\]
For each such \(\theta\), equality is attained exactly, up to permutation of the last \(n-1\) coordinates, on the geodesics
\[
a(\theta)=a_*\cos\theta+v_*\sin\theta,
\]
where
\[
v_*=\left(0,-\sqrt{\frac{n-2}{n-1}},\frac1{\sqrt{(n-1)(n-2)}},\ldots,\frac1{\sqrt{(n-1)(n-2)}}\right).
\]
Thus the previously available chamber estimate \(V(a)/V_{\min}\ge\sec\theta\) is not sharp away from \(\theta=0\); the exact radial lower envelope is \(F_n(\theta)>\sec\theta\). In particular,
\[
F_n(\theta)=1+\frac{2n-1}{2n}\theta^2-
\frac{(n-1)(n-3)}{3n^{3/2}\sqrt{n-2}}\theta^3+O_n(\theta^4).
\]

## Assumptions and scope
The statement concerns central hyperplane sections of the standard regular simplex and a fixed facet-parallel minimizer. The angle is the ordinary spherical angle on the unit sphere inside \((1,\ldots,1)^\perp\). The optimization is over the specified one-positive sign chamber. The interval \(0<\theta<\theta_n\) is exactly the range on which the displayed equality geodesics remain inside that open chamber. No claim is made about the sharp radial envelope after those equality geodesics meet a chamber wall.

## Proof
Every unit normal at spherical angle \(\theta\in(0,\pi/2)\) from \(a_*\) has a unique representation
\[
a=a_*\cos\theta+v\sin\theta,
\]
where \(v\) is a unit tangent vector at \(a_*\) in the admissible normal sphere. The equations \(v\perp a_*\) and \(\sum_jv_j=0\) imply
\[
v_1=0,\qquad \sum_{j=2}^n v_j=0,\qquad \sum_{j=2}^n v_j^2=1.
\]

Assume that \(a\) remains in the one-positive chamber. Put
\[
A=\sqrt{\frac{n-1}{n}},\qquad c=\frac1{\sqrt{n(n-1)}}.
\]
Then \(a_1=A\cos\theta>0\), while \(a_j=-c\cos\theta+v_j\sin\theta<0\) for \(j\ge2\). If \(X_1,\ldots,X_n\) are independent exponential random variables of mean one, the standard simplex-section density formula gives
\[
V(a)=\frac{\sqrt n}{(n-2)!}
 f_{\sum_j a_jX_j}(0).
\]
Conditioning on the unique positive summand yields
\[
f_{\sum_j a_jX_j}(0)
=\frac1{a_1}\prod_{j=2}^n\frac1{1+(-a_j)/a_1}.
\]
After normalization by the value at \(a_*\), this simplifies exactly to
\[
\frac{V(a)}{V_{\min}}
=\frac{\sec\theta}{\prod_{j=2}^n(1-\kappa v_j)},
\qquad
\kappa=\sqrt{\frac{n-1}{n}}\tan\theta.
\tag{1}
\]

It remains to maximize the denominator under the two moment constraints on the last \(n-1\) tangent coordinates. Write \(m=n-1\). Every real vector \((x_1,\ldots,x_m)\) with
\[
\sum_i x_i=0,\qquad \sum_i x_i^2=1
\]
satisfies
\[
-\sqrt{\frac{m-1}{m}}\le x_i\le\sqrt{\frac{m-1}{m}},
\]
by Cauchy--Schwarz applied to the other \(m-1\) coordinates. Set
\[
b=-\sqrt{\frac{m-1}{m}},\qquad
r=\frac1{\sqrt{m(m-1)}}.
\]
For \(f(x)=\log(1-\kappa x)\), the chamber condition makes every factor positive and
\[
f'''(x)=-\frac{2\kappa^3}{(1-\kappa x)^3}<0.
\]
Let \(Q\) be the quadratic Hermite interpolant satisfying
\[
Q(b)=f(b),\qquad Q(r)=f(r),\qquad Q'(r)=f'(r).
\]
The Hermite remainder formula gives, for every admissible coordinate \(x\),
\[
f(x)-Q(x)=\frac{f'''(\xi_x)}6(x-b)(x-r)^2\le0.
\]
Because \(Q\) is quadratic, \(\sum_iQ(x_i)\) depends only on \(\sum_i x_i\) and \(\sum_i x_i^2\). Hence it equals its value on \((b,r,\ldots,r)\), and therefore
\[
\prod_{i=1}^{m}(1-\kappa x_i)
\le(1-\kappa b)(1-\kappa r)^{m-1}.
\tag{2}
\]
For \(\kappa>0\), equality in the Hermite remainder forces every coordinate to belong to \(\{b,r\}\). The zero-sum condition then forces exactly one coordinate to equal \(b\), so equality in (2) is precisely the stated permutation orbit.

Substituting \(m=n-1\) and \(\kappa=\sqrt{(n-1)/n}\tan\theta\) into (1)--(2) gives
\[
1-\kappa b=1+\sqrt{\frac{n-2}{n}}\tan\theta,
\qquad
1-\kappa r=1-\frac{\tan\theta}{\sqrt{n(n-2)}},
\]
which proves the displayed formula for \(F_n\).

For the equality vector, the \(n-2\) tangent coordinates equal to \(r\) remain on negative simplex-normal coordinates exactly while
\[
\tan\theta<\frac{c}{r}=\sqrt{\frac{n-2}{n}}.
\]
This gives the claimed angular interval. Finally, strict concavity of \(x\mapsto\log(1-\kappa x)\) and the zero mean of the tangent coordinates imply that the denominator in (1) is strictly smaller than one whenever \(\theta>0\), so \(F_n(\theta)>\sec\theta\). Taylor expansion of the closed formula gives the stated local series.

## Verification
The analytic proof uses only the exact exponential-density section formula, Cauchy--Schwarz, a quadratic Hermite remainder with a sign-controlled third derivative, and elementary algebra. The accompanying `verify.py` independently checks the closed equality formula and tests the inequality on deterministic pseudorandom tangent vectors for \(3\le n\le10\) and several angles inside the stated range. Running

`python verify.py`

prints `VERIFY_OK`. These finite checks are consistency tests only; the universal statement follows from the proof above.

## Relationship to prior work
Ambrus and Gárgyán proved in 2026 that facet-parallel central sections are the global minimizers and classified equality. Their theorem supplies the newly settled extremal context but does not state a fixed-angle radial minimum. König's earlier work provides explicit formulas and local variational information for simplex sections, while Dirksen gave a partial minimum result.

A subsequent quantitative note proves, throughout the same one-positive chamber, the lower bound
\[
V(a)/V_{\min}\ge\sec\theta
\]
and computes the isotropic Hessian at the minimizer. The present result compares directly with that statement: it solves the remaining fixed-angle optimization inside the chamber, replaces \(\sec\theta\) by the strictly larger sharp function \(F_n(\theta)\), and classifies all equality directions for the explicit interval above. Its quadratic term agrees with the known Hessian, providing an independent normalization check.

## Limitations
The result is chamber-specific and does not determine the sharp fixed-angle envelope after the equality geodesics hit a coordinate wall. The primary minimum theorem is recent, so an unindexed simultaneous derivation of the same fixed-angle product extremum remains a residual originality risk. The numerical verifier does not certify the infinite family; it only checks algebraic and finite-instance consistency.

## References
1. G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714, first public 2026-09-11.
2. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, Adv. Math. 376 (2021), 107458; arXiv:2002.10743.
3. H. Dirksen, *Sections of the regular simplex -- Volume formulas and estimates*, Math. Nachr. 290 (2017), 2567--2584, DOI 10.1002/mana.201600109.
4. *Quantitative stability and exact Hessian for minimal central simplex sections*, public finding 47a8f9f119ab (2026-09-19).
