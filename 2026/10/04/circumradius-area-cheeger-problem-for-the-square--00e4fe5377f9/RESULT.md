# Circumradius–area Cheeger problem for the square

## Finding

Let
\[
Q_a=[-a,a]^2,\qquad a>0,
\]
and for every measurable set \(E\subseteq Q_a\) of positive area let \(R(E)\) denote its Euclidean circumradius. Define the circumradius–area Cheeger-type constant
\[
\mathcal C_R(Q_a)
=
\inf_{\substack{E\subseteq Q_a\\ A(E)>0}}
\frac{R(E)}{A(E)}.
\]

Let \(\alpha\in(0,\pi/2)\) be the unique solution of
\[
\alpha=\cos\alpha,
\]
and put
\[
\theta_*=\frac{\pi}{4}-\frac{\alpha}{2}.
\]
Then
\[
\boxed{
\mathcal C_R(Q_a)
=
\frac{\cos\theta_*}{4a\alpha}
}.
\]

The infimum is attained by the centered disk–square intersection
\[
E_*
=
Q_a\cap B\!\left(0,a\sec\theta_*\right).
\]
Its circumradius is exactly
\[
R(E_*)=a\sec\theta_*
\approx
1.093169744985017\,a.
\]
Thus the optimal set is strictly larger than the inscribed disk and strictly smaller than the square.

For the square \(Q_1=[-1,1]^2\),
\[
\mathcal C_R(Q_1)
\approx
0.309426809058386.
\]

## Assumptions and scope

The admissible class consists of all measurable subsets of \(Q_a\) with positive planar Lebesgue area; convexity of the admissible set is not assumed. The circumradius \(R(E)\) is the infimum of radii of Euclidean disks containing \(E\).

The motivating source explicitly asks for Cheeger-type problems obtained by replacing perimeter with classical geometric magnitudes, including circumradius, and minimizing \(F(E)/A(E)\) over subsets of a fixed planar convex body. The present result solves that circumradius variant exactly for the canonical square domain.

## Proof

For \(r>0\) and \(c\in\mathbb R^2\), write
\[
K_c(r)=Q_a\cap B(c,r).
\]
Because both \(Q_a\) and the Euclidean disk are centrally symmetric,
\[
K_{-c}(r)=-K_c(r).
\]
Moreover,
\[
\frac12K_c(r)+\frac12K_{-c}(r)\subseteq K_0(r).
\]
Indeed, the midpoint of one point in \(Q_a\cap B(c,r)\) and one point in \(Q_a\cap B(-c,r)\) lies in \(Q_a\) by convexity, and after subtracting the opposite centers its disk component lies in \(B(0,r)\).

The planar Brunn–Minkowski inequality therefore gives
\[
A(K_0(r))^{1/2}
\ge
\frac{A(K_c(r))^{1/2}+A(K_{-c}(r))^{1/2}}2
=
A(K_c(r))^{1/2}.
\]
Hence among all radius-\(r\) disks, the centered disk captures the largest area of the square.

Now let \(E\subseteq Q_a\) have positive area and circumradius \(R(E)=r\). For every \(\varepsilon>0\), \(E\) lies in some disk of radius \(r+\varepsilon\), so
\[
A(E)
\le
A(K_0(r+\varepsilon)).
\]
Letting \(\varepsilon\downarrow0\) yields
\[
A(E)\le A(K_0(r)).
\]
Consequently,
\[
\frac{R(E)}{A(E)}
\ge
\frac{r}{A(K_0(r))}.
\]
It is therefore enough to minimize the one-variable function
\[
f(r)=\frac{r}{A(K_0(r))},
\qquad
0<r\le\sqrt2\,a.
\]

For \(0<r\le a\), the centered disk lies inside the square, so
\[
A(K_0(r))=\pi r^2,
\qquad
f(r)=\frac1{\pi r},
\]
which is strictly decreasing.

For \(a\le r\le\sqrt2\,a\), set
\[
\theta=\arccos\!\left(\frac ar\right).
\]
Removing the four circular segments outside the square gives
\[
A(K_0(r))
=
\pi r^2
-
4\left(
r^2\theta
-
a\sqrt{r^2-a^2}
\right).
\]
Differentiation gives the exact cancellation
\[
A'(K_0(r))
=
2r(\pi-4\theta).
\]
Hence the sign of \(f'(r)\) is the sign of
\[
H(r)
=
A(K_0(r))-rA'(K_0(r))
=
4a\sqrt{r^2-a^2}
-
r^2(\pi-4\theta).
\]

Write \(r=a\sec\theta\) and define
\[
x=\frac{\pi}{2}-2\theta.
\]
Then
\[
\cos^2\theta\,\frac{H(r)}{a^2}
=
2(\cos x-x).
\]
The function \(x\mapsto\cos x-x\) is strictly decreasing on \([0,\pi/2]\), positive at \(0\), and negative at \(\pi/2\). Thus it has one zero \(\alpha\in(0,\pi/2)\), characterized by
\[
\alpha=\cos\alpha.
\]
Since \(x\) decreases strictly as \(r\) increases, \(f\) decreases before the corresponding radius and increases after it. The unique minimizing radius is therefore
\[
r_*
=
a\sec\!\left(\frac{\pi}{4}-\frac{\alpha}{2}\right).
\]

At the critical point,
\[
\pi-4\theta_*=2\alpha,
\]
and the stationarity equation \(A=rA'\) gives
\[
A(K_0(r_*))
=
4\alpha r_*^2.
\]
Therefore
\[
\mathcal C_R(Q_a)
=
\frac{r_*}{4\alpha r_*^2}
=
\frac{\cos\theta_*}{4a\alpha}.
\]

Finally, \(r_*<\sqrt2\,a\), so the two opposite points
\[
\pm
\left(
\frac{r_*}{\sqrt2},
\frac{r_*}{\sqrt2}
\right)
\]
belong to \(Q_a\cap B(0,r_*)\). Their distance is \(2r_*\), forcing the circumradius of \(E_*\) to be at least \(r_*\); the defining disk gives the reverse inequality. Hence \(R(E_*)=r_*\), completing the proof.

## Verification

The proof is analytic and does not depend on numerical search. The accompanying `verify.py` independently checks the defining fixed-point equation, the critical-radius area identity
\[
A(E_*)=4\alpha R(E_*)^2,
\]
the closed-form value, and a dense one-dimensional scan of the centered-intersection objective. It also checks that perturbing the radius to either side raises the objective.

The checker prints:

`VERIFY_OK square circumradius-area constant`

The numerical scan is only a consistency check; the global minimization over all measurable subsets follows from the Brunn–Minkowski centering argument and the exact derivative analysis.

## Relationship to prior work

Cañete explicitly proposed replacing perimeter in the Cheeger problem by other classical geometric magnitudes and minimizing \(F(E)/A(E)\) over subsets of a fixed planar convex body. Circumradius is named as one of the proposed functionals, and the paper states that no related reference was found there.

Ftouhi, Masiello, and Paoli later developed sharp inequalities linking the ordinary Cheeger constant to area, inradius, circumradius, width, diameter, and perimeter. Their problem keeps the ordinary perimeter-based Cheeger constant and varies global shape constraints. It does not replace perimeter by circumradius in the subset functional, and its full text does not state the square optimization solved here.

Targeted searches of the research index and the web for circumradius–area Cheeger problems, square subsets, disk–square intersections, the fixed-point constant \(\alpha=\cos\alpha\), and equivalent radius/area formulations did not locate the theorem above.

## Limitations

The result treats the circumradius functional and a square domain. It does not solve the corresponding problem for rectangles, general centrally symmetric convex bodies, minimal width, or inradius. The centering lemma extends to any centrally symmetric convex domain, but the subsequent one-dimensional area profile is square-specific.

The originality search is targeted rather than exhaustive. The 2021 source itself reported no related literature for this variant, but an older treatment may exist under different terminology, especially in classical isoperimetric problem collections.

## References

A. Cañete, “Cheeger Sets for Rotationally Symmetric Planar Convex Bodies,” Results in Mathematics 77 (2022), article 9, DOI 10.1007/s00025-021-01539-7. Published online 2021-11-06.

I. Ftouhi, A. L. Masiello, and G. Paoli, “Sharp inequalities involving the Cheeger constant of planar convex sets,” arXiv:2206.13158, first submitted 2022-06-27.

H. T. Croft, K. J. Falconer, and R. K. Guy, Unsolved Problems in Geometry, Springer, 1991, Problem A23, as cited in Cañete’s Remark 11.
