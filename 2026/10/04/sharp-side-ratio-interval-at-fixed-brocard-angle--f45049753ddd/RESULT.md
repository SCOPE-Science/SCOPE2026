# Sharp side-ratio interval at fixed Brocard angle
## Finding
Let \(T\) be a nondegenerate Euclidean triangle with side lengths \(a,b,c\), Brocard angle \(\omega\in(0,\pi/6]\), and
\[
N=a^2+b^2+c^2,\qquad
q^2=\frac{(a^2-b^2)^2+(b^2-c^2)^2+(c^2-a^2)^2}{N^2}.
\]
The cone-angle identity of Bényi and Ćurgus implies
\[
q^2=\frac{1-3\tan^2\omega}{2},\qquad 0\le q<\frac1{\sqrt2}.
\]
If \(\kappa=\max(a,b,c)/\min(a,b,c)\), then the complete sharp interval at fixed \(\omega\) is
\[
\boxed{\sqrt{\frac{1+\sqrt2 q}{1-q/\sqrt2}}
\le \kappa \le
\sqrt{\frac{1+q^2+q\sqrt{3(2-q^2)}}{1-2q^2}}}.
\]
For \(q=0\) both endpoints are \(1\), corresponding to the equilateral triangle. For \(q>0\), the lower endpoint is attained exactly by the isosceles class with the two shorter sides equal. The upper endpoint is attained exactly, up to relabeling, by one scalene similarity class. Every value between the endpoints is attained.

## Assumptions and scope
The triangle is ordinary Euclidean and nondegenerate. Side labels are immaterial because both \(q\) and \(\kappa\) are symmetric. Normalize the squared side lengths by
\[
x=\frac{a^2}{N},\qquad y=\frac{b^2}{N},\qquad z=\frac{c^2}{N},
\]
then relabel so that \(x\ge y\ge z>0\). Thus \(\kappa^2=x/z\).

The result is a profile theorem for a fixed Brocard angle, not a new definition or formula for the Brocard angle itself. The relation between the Brocard angle and the cone angle of the squared-side vector is taken from Bényi--Ćurgus and is reproduced below in the normalization needed for the proof.

## Proof
Because \(x+y+z=1\),
\[
(x-y)^2+(y-z)^2+(z-x)^2=3(x^2+y^2+z^2)-1.
\]
Let \(\gamma\) be the angle between \((a^2,b^2,c^2)\) and \((1,1,1)\). Then
\[
\cos^2\gamma=\frac{1}{3(x^2+y^2+z^2)},
\]
so
\[
\tan^2\gamma=3(x^2+y^2+z^2)-1=q^2.
\]
Bényi--Ćurgus Proposition 4.1 states
\[
3\tan^2\omega+2\tan^2\gamma=1,
\]
which yields the displayed formula for \(q\). Their cone description of triangle squared-side vectors gives \(q<1/\sqrt2\) precisely for nondegenerate triangles.

Fix \(q\). The normalized triples lie on the circle
\[
x+y+z=1,\qquad x^2+y^2+z^2=\frac{1+q^2}{3}.
\]
Intersect this circle with the ordering chamber \(x\ge y\ge z\). The intersection is a compact connected arc, so the continuous function \(x/z\) has an interval as its image.

At one chamber endpoint \(y=z\). Solving the two displayed constraints gives
\[
x=\frac{1+\sqrt2 q}{3},\qquad
 y=z=\frac{1-q/\sqrt2}{3},
\]
hence
\[
\frac{x}{z}=\frac{1+\sqrt2 q}{1-q/\sqrt2}.
\]
At the other endpoint \(x=y\), one obtains
\[
\frac{x}{z}=\frac{1+q/\sqrt2}{1-\sqrt2 q},
\]
and direct cross multiplication shows that this is no smaller than the first endpoint value for \(0\le q<1/\sqrt2\). An interior stationary point of \(x/z\) under the two circle constraints satisfies the Lagrange equations. Eliminating the multipliers gives
\[
x(x-y)=z(y-z),
\]
hence \(x^2+z^2=y(x+z)\). Together with \(x+y+z=1\), this says \(x^2+y^2+z^2=y\), so every interior stationary point must have \(y=(1+q^2)/3\). The constraints then determine a unique interior point. As the calculation below shows, it is the global upper extremizer. Consequently the minimum occurs at a chamber endpoint, and the first endpoint is the global minimum.

For the maximum, write \(r=x/z\ge1\), \(x=rz\), and \(y=1-(r+1)z\). Put
\[
s=1-\frac{1+q^2}{3}=\frac{2-q^2}{3}.
\]
Substitution into the quadratic constraint gives a quadratic equation for \(z\). Its discriminant is nonnegative exactly when
\[
(1-2q^2)(r^2+1)-2(1+q^2)r\le0.
\]
Since \(1-2q^2>0\), the largest feasible \(r\) is the larger root,
\[
r_{\max}=\frac{1+q^2+q\sqrt{3(2-q^2)}}{1-2q^2}.
\]
Equality in the discriminant condition gives the unique interior extremizer. There
\[
y=\frac{1+q^2}{3},\qquad
x,z=\frac{s\pm q\sqrt{s}}{2},
\]
so for \(q>0\) the extremizer is scalene. Taking square roots of the sharp bounds for \(x/z\) proves the claimed interval for \(\kappa\). Connectedness of the chamber arc proves that no values between the endpoints are missed.

## Verification
The accompanying deterministic checker parameterizes the fixed-\(q\) circle directly, samples all ordering chambers densely for a grid of \(q\)-values, checks both closed-form endpoint classes, reconstructs \(q\) from the Brocard-angle identity, and checks that every sampled squared-side triple gives a strict triangle. The numerical checks supplement, but do not replace, the algebraic proof above.

## Relationship to prior work
Bényi and Ćurgus represent a triangle by its squared-side vector and prove that the angle \(\gamma\) of this vector from the diagonal axis determines the Brocard angle through \(3\tan^2\omega+2\tan^2\gamma=1\). Their paper also characterizes when two triangles have the same Brocard angle. The fixed-\(\omega\) side-ratio optimization above starts from that cone geometry but adds an extremal analysis of the ordered circular section.

A targeted comparison also considered literature on triangles sharing Brocard data and modern shape invariants. Ben-Israel and Foldes study stability of Brocard points under nested similar polygons, while general references record the standard identity \(\cot\omega=\cot A+\cot B+\cot C\). These are adjacent facts but do not supply the two sharp side-ratio endpoints proved here.

## Limitations
The originality check was targeted rather than exhaustive. The Bényi--Ćurgus full text was inspected around its cone geometry and Brocard-angle results and searched for longest/shortest-side or condition-number formulations; no equivalent fixed-angle profile was located. An equivalent optimization could nevertheless exist in older triangle-geometry literature under different terminology. The theorem concerns Euclidean side ratios only; it does not assert analogous formulas in spherical, hyperbolic, or normed geometries.

## References
1. Á. Bényi and B. Ćurgus, *Triangles and groups via cevians*, arXiv:1109.0557v1, first public 2 September 2011; Proposition 4.1 and the surrounding cone description.
2. A. Ben-Israel and S. Foldes, *Stability of Brocard points of polygons*, Rocky Mountain Journal of Mathematics 30 (2000), 411--434, DOI:10.1216/rmjm/1022009273.
