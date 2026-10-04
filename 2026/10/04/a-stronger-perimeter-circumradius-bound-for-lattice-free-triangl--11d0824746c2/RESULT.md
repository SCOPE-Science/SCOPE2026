# A stronger perimeter–circumradius bound for lattice-free triangles
## Finding
Let \(T\subset\mathbb R^2\) be a nondegenerate Euclidean triangle whose interior contains no point of the standard lattice \(\mathbb Z^2\). Write \(p\) for its perimeter, \(R\) for its circumradius, and \(r\) for its inradius. Then
\[
p-4R\le (6\sqrt3-8)r\le 3\sqrt6-4\sqrt2\approx1.691615<2.
\]
Consequently, the perimeter–circumradius conjecture \(p-4R\le2\) proposed for lattice-free planar convex sets holds for the full triangle subclass, with a stronger absolute constant.

## Assumptions and scope
A triangle is lattice-free here when \(\operatorname{int}T\cap\mathbb Z^2=\varnothing\). Boundary lattice points are allowed. The lattice is the standard unit square lattice. The triangle is assumed nondegenerate, so \(r>0\) and \(R>0\). No assertion is made that \(3\sqrt6-4\sqrt2\) is the optimal constant for lattice-free triangles.

## Proof
Let \(s=p/2\) be the semiperimeter. Gerretsen's upper inequality gives
\[
s^2\le4R^2+4Rr+3r^2.
\]
Euler's inequality gives \(R\ge2r\). Put \(t=r/R\), so \(0<t\le1/2\). Then
\[
p-4R=2s-4R\le 2R\!\left(\sqrt{4+4t+3t^2}-2\right)=r\,\Phi(t),
\]
where
\[
\Phi(t)=\frac{2(\sqrt{4+4t+3t^2}-2)}{t}=\frac{2(4+3t)}{\sqrt{4+4t+3t^2}+2}.
\]
Set \(S(t)=\sqrt{4+4t+3t^2}\). Differentiating the last expression, the sign of \(\Phi'(t)\) is the sign of
\[
6S(t)(S(t)+2)-2(4+3t)(2+3t)=8-12t+12S(t).
\]
For \(0<t\le1/2\), this is positive. Hence \(\Phi\) is increasing and
\[
\Phi(t)\le\Phi(1/2)=6\sqrt3-8.
\]
This proves the first inequality.

It remains to use lattice-freeness. Every point of \(\mathbb R^2\) is at distance at most \(\sqrt2/2\) from some point of \(\mathbb Z^2\): translate the point into a unit lattice square and choose a nearest corner. If the inradius satisfied \(r>\sqrt2/2\), the open incircle would contain a lattice point, and therefore so would \(\operatorname{int}T\), contradicting lattice-freeness. Thus \(r\le\sqrt2/2\), and
\[
p-4R\le(6\sqrt3-8)\frac{\sqrt2}2=3\sqrt6-4\sqrt2<2.
\]
This completes the proof.

## Verification
The algebraic reduction was checked independently from the displayed formulas: rationalizing \(\Phi\) gives the stated expression, differentiating gives the numerator \(8-12t+12S(t)\), and substituting \(t=1/2\) gives \(6\sqrt3-8\). The accompanying `verify.py` performs deterministic numerical checks of the universal triangle inequality over a dense parameter grid and randomized nondegenerate triangles, and separately checks lattice-free triangles contained in a unit lattice square. These computations are consistency checks only; the proof above establishes the infinite statement.

## Relationship to prior work
González Merino and Henze introduced the lattice-free perimeter–diameter and perimeter–circumradius problems and conjectured \(p(K)-4R(K)\le2\) for every planar lattice-free convex set. Their triangle theorem treats the other functional \(p(T)-2D(T)\); their full text does not state the triangle result proved here for \(p(T)-4R(T)\). Their paper also cites earlier lattice inequalities involving inradius and circumradius. The present argument combines the classical Gerretsen triangle inequality with the square lattice covering radius to close the conjectured perimeter–circumradius bound on the natural triangle subclass.

Targeted searches for the exact functional, the triangle subclass, the Gerretsen formulation, and the constant \(6\sqrt3-8\) found the 2013/2015 source and older component inequalities but no statement implying this lattice-free triangle conclusion. This is evidence of non-coverage, not a proof that no equivalent formulation exists in the historical literature.

## Limitations
The absolute constant \(3\sqrt6-4\sqrt2\) is not claimed sharp for lattice-free triangles. The argument uses the square lattice covering radius only at the final step, so it intentionally leaves room for improvement from triangle-specific lattice geometry. The result does not settle the conjecture for arbitrary lattice-free convex bodies. Historical synonym or reformulation risk remains because older convex-geometry literature can encode the same functionals in different notation.

## References
1. B. González Merino and M. Henze, “A remark on perimeter-diameter and perimeter-circumradius inequalities under lattice constraints,” arXiv:1310.6534v1, first posted 2013-10-24; later Journal of Geometry 106 (2015), 75–83.
2. P. R. Scott and P. W. Awyong, “Inradius and circumradius for planar convex bodies containing no lattice points,” Bulletin of the Australian Mathematical Society 59 (1999), 163–168, DOI: 10.1017/S000497270003272X.
3. D. S. Mitrinović, J. E. Pečarić, and V. Volenec, Recent Advances in Geometric Inequalities, Kluwer, 1989; Gerretsen inequalities for triangle semiperimeter, circumradius, and inradius.
