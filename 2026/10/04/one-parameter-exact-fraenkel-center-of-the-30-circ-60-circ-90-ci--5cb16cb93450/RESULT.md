# One-parameter exact Fraenkel center of the \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle
## Finding
Let
\[
T=\operatorname{conv}\{(0,0),(1,0),(0,\sqrt3)\},\qquad R^2=\frac{\sqrt3}{2\pi}.
\]
There is a unique number \(z_*\in(R^2/8,R^2/4)\) satisfying
\[
2\sqrt{R^2-4z_*}+\sqrt3\sqrt{R^2-3z_*}+\sqrt{R^2-z_*}=\sqrt3.
\]
The equal-area disk minimizing the Fraenkel symmetric difference with \(T\) has the unique center
\[
P=\left(\sqrt{R^2-3z_*},\sqrt{R^2-z_*}\right).
\]
Numerically,
\[
P=(0.3719164279770188862\ldots,0.4794617554511785131\ldots),
\]
which reproduces the numerical center reported by Finch. The corresponding Fraenkel asymmetry is
\[
\alpha(T)=0.5168009538789127383\ldots.
\]

There is also a structural statement behind the reduction. For any triangle, suppose an equal-area disk is at a local Fraenkel optimum in the regular three-cap regime: it meets all three supporting side lines and contains no vertex. If the side lengths are \(a,b,c\), the center-to-side distances are \(d_a,d_b,d_c\), and the disk radius is \(R\), then
\[
\sqrt{R^2-d_a^2}:\sqrt{R^2-d_b^2}:\sqrt{R^2-d_c^2}=a:b:c.
\]
Thus the half-chord cut from the disk by each side is proportional to that side length.

## Assumptions and scope
Fraenkel asymmetry is computed against disks having the same area as the triangle. The structural chord-balance statement is asserted only in the regular three-cap regime described above; no claim is made that every triangle has its optimal disk in that regime. The global conclusion is proved for the displayed \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle.

Write the center as \(P=(s,t)\). The three side lengths opposite \((0,0),(1,0),(0,\sqrt3)\) are respectively \(2,\sqrt3,1\), and the corresponding distances from \(P\) to the side lines are
\[
d_2=\frac{\sqrt3-\sqrt3s-t}{2},\qquad d_{\sqrt3}=s,\qquad d_1=t.
\]

## Proof
For a disk of radius \(R\), the area of the circular cap beyond a line at distance \(d\in(0,R)\) from the center is
\[
C(d)=R^2\arccos\!\left(\frac dR\right)-d\sqrt{R^2-d^2}.
\]
Direct differentiation gives
\[
C'(d)=-2\sqrt{R^2-d^2},\qquad C''(d)=\frac{2d}{\sqrt{R^2-d^2}}>0.
\]
In the regular three-cap regime, the three exterior caps are disjoint, so minimizing symmetric difference is equivalent to minimizing
\[
C(d_a)+C(d_b)+C(d_c).
\]
If \(n_a,n_b,n_c\) are inward unit normals, the stationary equation is
\[
\sqrt{R^2-d_a^2}\,n_a+\sqrt{R^2-d_b^2}\,n_b+\sqrt{R^2-d_c^2}\,n_c=0.
\]
For a triangle, the unique positive linear dependence among inward side normals is
\[
a n_a+b n_b+c n_c=0.
\]
Therefore the three half-chord lengths are proportional to \(a,b,c\). The Hessian is a positive sum of the rank-one matrices \(n_i n_i^{\mathsf T}\), with strictly positive coefficients \(C''(d_i)\); because the side normals span the plane, this Hessian is positive definite.

For the displayed triangle, write the common proportionality factor as \(q>0\) and put \(z=q^2\). The chord balance gives
\[
d_2=\sqrt{R^2-4z},\qquad s=\sqrt{R^2-3z},\qquad t=\sqrt{R^2-z}.
\]
Every interior point of a triangle satisfies the area identity
\[
2d_2+\sqrt3s+t=\sqrt3,
\]
which is exactly the scalar equation in the finding.

Its left side minus \(\sqrt3\) is strictly decreasing on \((0,R^2/4)\). At \(z=R^2/4\) it equals \(\sqrt3(R-1)<0\). At \(z=R^2/8\) it is positive; one elementary verification uses \(\pi<22/7\), \(5/3<\sqrt3<7/4\), and the lower bounds \(\sqrt2>7/5\), \(\sqrt{15/8}>4/3\), \(\sqrt{7/8}>9/10\). Hence there is exactly one \(z_*\in(R^2/8,R^2/4)\).

This solution lies in the regular three-cap regime. It has positive distances strictly below \(R\). The disk excludes the origin because
\[
s^2+t^2-R^2=R^2-4z_*>0.
\]
The bound \(z_*>R^2/8\) implies \(s<1/2\), so the squared distance from \(P\) to \((1,0)\), minus \(R^2\), is
\[
1-2s+(R^2-4z_*)>0.
\]
Finally \(t<R<\sqrt3/2\), so the squared distance from \(P\) to \((0,\sqrt3)\), minus \(R^2\), is
\[
3-2\sqrt3t+(R^2-4z_*)>0.
\]
Thus no vertex is inside the disk and the cap decomposition used above is valid.

It remains to promote the strict local optimum to the global one. For any two disk centers \(p_0,p_1\) and \(0\le\lambda\le1\), convexity gives
\[
(1-\lambda)\bigl(T\cap(B_R+p_0)\bigr)+\lambda\bigl(T\cap(B_R+p_1)\bigr)
\subseteq T\cap\bigl(B_R+(1-\lambda)p_0+\lambda p_1\bigr).
\]
The planar Brunn--Minkowski inequality therefore makes the square root of overlap area a concave function of the disk center. A strict local maximum of overlap is consequently global; a second global maximum would force a segment of maxima and contradict strict local maximality. Hence the center above is the unique global Fraenkel-optimal center.

The exact asymmetry can be evaluated without a two-dimensional integral. With \(q=\sqrt{z_*}\) and side-length parameter \(m\in\{2,\sqrt3,1\}\), the three cap contributions are
\[
R^2\arcsin\!\left(\frac{mq}{R}\right)-mq\sqrt{R^2-m^2q^2}.
\]
Because \(|T|=\sqrt3/2\),
\[
\alpha(T)=\frac4{\sqrt3}\sum_{m\in\{2,\sqrt3,1\}}
\left[
R^2\arcsin\!\left(\frac{mq}{R}\right)-mq\sqrt{R^2-m^2q^2}
\right].
\]

## Verification
A standalone checker recomputes \(z_*\) by bisection, verifies the scalar equation, the chord-balance ratios, the published decimal center, vertex exclusion, and the asymmetry value. It uses finite precision only as a numerical replay of the analytic proof.

An independent geometric stress test evaluated the triangle-disk intersection numerically near the derived center; perturbations in several directions reduced the overlap, and the resulting asymmetry agreed with the cap formula to the expected discretization accuracy. This numerical test is diagnostic and is not used as proof.

## Relationship to prior work
Finch introduced the equiareal disk center through Fraenkel asymmetry and described locating it as a challenging calculus problem. For this same \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle, Finch set up a two-variable partition/integration calculation and reported only the numerical center
\[
(0.3719164279770188862\ldots,0.4794617554511785131\ldots).
\]
The present result gives a geometric stationarity law, reduces the calculation to one monotone scalar equation, proves the resulting point is the unique global optimizer, and gives a direct one-dimensional cap formula for the asymmetry.

The general quantitative-isoperimetric literature defines Fraenkel asymmetry and optimal equal-volume balls, but the inspected sources do not state this triangle side/chord balance or the displayed scalar characterization. Finch's later survey chapter on Fraenkel asymmetry points back to the 2014 triangle-center paper for triangle computations rather than supplying this reduction.

## Limitations
The side/chord balance is a first-order characterization only within the regular three-cap regime. It does not classify which arbitrary triangles fall into that regime. No claim is made about disks constrained by equal perimeter rather than equal area. The originality comparison cannot exclude an unindexed note or an unavailable historical derivation using equivalent cap geometry.

## References
1. S. R. Finch, *In Limbo: Three Triangle Centers*, arXiv:1406.0836, first submitted 3 June 2014.
2. N. Fusco, F. Maggi, A. Pratelli, *The sharp quantitative isoperimetric inequality*, Annals of Mathematics 168 (2008), 941--980, DOI 10.4007/annals.2008.168.941.
3. S. R. Finch, *Mathematical Constants II*, Cambridge University Press, 2019, Section 5.23, Fraenkel Asymmetry.
