# The exact area–orientation envelope for rectangles in a regular pentagon

## Finding
Let \(P_R\) be a regular pentagon of circumradius \(R>0\). Fix one vertex on the positive horizontal axis, and measure an unoriented rectangle side by its angle with the horizontal, modulo \(\pi/2\). The pentagon's rotations identify equal-area orientation classes modulo \(\pi/10\). For a representative \(0\leq\theta\leq\pi/10\), put \(\alpha=\pi/5\). The greatest area of a rectangle contained in \(P_R\), **with this prescribed orientation**, is exactly
\[
F_R(\theta)=\frac{5R^2}{4\cos(\alpha-\theta)\sin(2\alpha-\theta)}.
\]
For each actual direction pair (angle modulo \(\pi/2\)), there is precisely one maximizing geometric rectangle, before identifying rotated copies. The unrestricted **global** maximizers have two corners at the endpoints of one pentagon edge and their other two corners on the two edges incident to the opposite vertex.

In particular, without any restriction on orientation,
\[
\boxed{\max_{Q\subseteq P_R,\,Q\text{ a rectangle}}\operatorname{area}(Q)
=R^2(5-\sqrt5)\sin(\pi/5).}
\]
Exactly five geometric rectangles attain this maximum, one for each pentagon edge. The orientation-specific area is smallest at \(\theta=\pi/20\) in the representative interval and largest only at its two endpoints.

## Assumptions and scope
A rectangle is nondegenerate, has four right angles, and may be placed at any location in the closed pentagon; no vertex or symmetry-axis restriction is imposed. The orientation angle identifies the two perpendicular side directions. All formulas scale with the square of circumradius. The phrase 'unique at a fixed orientation' refers to the geometric subset, not to a choice of a labeled side or vertex order.

It suffices to take \(R=1\). Set
\[
\alpha=\pi/5,\quad p=\cos\alpha,\quad q=\sin\alpha,\quad
r=\cos(2\alpha),\quad s=\sin(2\alpha),\quad k=\sqrt5/4,
\quad \rho=(3-\sqrt5)/2.
\]
The five outer unit normals, in cyclic order, are
\[
(p,q),\ (-r,s),\ (-1,0),\ (-r,-s),\ (p,-q).
\]
The pentagon consists precisely of points whose dot products with these normals do not exceed \(p\).

## Proof
**1. Orientations and half-edge coordinates.** A rectangle's two side directions are unchanged by a quarter-turn or a sign reversal. Rotating the regular pentagon by \(2\pi/5\), then taking side directions modulo \(\pi/2\), generates orientation shifts of \(\pi/10\). Thus every rectangle may be rotated by a symmetry of the pentagon so that the orientation of one pair of sides is \(0\leq\theta\leq\pi/10\). Put \(t=\tan\theta\), and write its four corners as
\[
c\pm U\pm V,\qquad U=(A,At),\qquad V=(-Bt,B),\qquad A,B>0.
\]
Here \(U\perp V\), and the area is \(4AB(1+t^2)\). This describes every rectangle in the chosen orientation class.

**2. Four support inequalities and a positive dual certificate.** Containment implies, for the first four normals listed above,
\[
\begin{aligned}
(p,q)\cdot c+(p+qt)A+(q-pt)B&\leq p,\\
(-r,s)\cdot c+(r-st)A+(s+rt)B&\leq p,\\
(-1,0)\cdot c+A+tB&\leq p,\\
(-r,-s)\cdot c+(r+st)A+(s-rt)B&\leq p.
\end{aligned}
\]
The sign choices are valid throughout \(0\leq t\leq\tan(\pi/10)=r/s\): for instance \(r-st\geq0\), \(q-pt>0\), and \(s-rt>0\). All terms arise from the exact rectangle support function \(n\cdot c+|n\cdot U|+|n\cdot V|\).

Multiply the first and fourth inequalities by \(1/2\) and the second and third by \(\rho/2\). The center terms cancel. The elementary pentagonal trigonometric identities
\[
q/s=1-\rho,\qquad p-r=(1+r)\rho,\qquad p(1+\rho)=\sqrt5/2
\]
reduce the sum to the **sharp support inequality**
\[
(p+qt)A+(s-rt)B\leq\sqrt5/2=2k.\tag{1}
\]
By the arithmetic–geometric mean inequality, with both coefficients positive,
\[
AB\leq \frac{k^2}{(p+qt)(s-rt)}
=\frac{5}{16(p+qt)(s-rt)}.\tag{2}
\]
Since \((p+qt)\cos\theta=\cos(\alpha-\theta)\) and
\((s-rt)\cos\theta=\sin(2\alpha-\theta)\), this gives
\[
\operatorname{area}(Q)\leq
\frac{5}{4\cos(\alpha-\theta)\sin(2\alpha-\theta)}.\tag{3}
\]
No assumption about contact points or the location of the center was used.

**3. Exact attainment for every orientation.** Equality in (1) and (2) prescribes
\[
A=\frac{k}{p+qt},\qquad B=\frac{k}{s-rt},\qquad
c=\left(A+tB-p,\ tA-\frac rs tB\right).\tag{4}
\]
Using the pentagonal identities \(p(1-r)=k\) and \(p(1+p)-(q/s)k=2k\), direct substitution into the four displayed support inequalities gives equality in each. The fifth support inequality has nonnegative slack, exactly
\[
\frac{(5-\sqrt5)\,t\left(1-t/\tan(\pi/10)\right)}
{8(p+qt)(s-rt)}\geq0.\tag{5}
\]
This identity follows by expanding the dot product with \((p,-q)\), substituting (4), and using \(q/s=(\sqrt5-1)/2\) and \(\tan(\pi/10)=r/s\). Hence the rectangle (4) is contained in the whole pentagon, and equality holds in (3). This proves the orientation profile.

All four weights used in step 2 are strictly positive. Equality in the weighted sum forces all four corresponding facet constraints to be tight; equality in the arithmetic–geometric mean step fixes \(A,B\) as in (4). The constraints with normals \((-1,0)\), \((-r,s)\), and \((-r,-s)\) then determine \(c\) uniquely. Thus there is exactly one maximizing rectangle for each prescribed orientation.

**4. Global maximum and equality cases.** The denominator of (3) is
\[
\cos(\alpha-\theta)\sin(2\alpha-\theta)
=\tfrac12\left[\sin(3\alpha-2\theta)+\sin\alpha\right].
\]
For \(0\leq\theta\leq\alpha/2\), the first sine has argument in \([2\alpha,3\alpha]\), namely \([72^\circ,108^\circ]\); it is at least \(\sin(2\alpha)\), with equality only when \(\theta=0\) or \(\theta=\alpha/2\). These endpoints are equivalent under a pentagon rotation and a swap of the two perpendicular side directions. The maximum area is therefore \(5/(4ps)=(5-\sqrt5)q\).

For the zero-orientation representative, (4) reads
\[
A=(5-\sqrt5)/4,\quad B=q,\quad c=(A-p,0).
\]
Its left edge joins the two pentagon vertices with angles \(4\alpha\) and \(6\alpha\), and its right edge meets the two pentagon edges incident to the vertex at angle zero. Its rotations through multiples of \(2\pi/5\) are five distinct maximizing rectangles. The orientation and fixed-orientation uniqueness arguments exclude all others. The same sine identity shows that the orientation profile is uniquely minimal at \(\theta=\alpha/4\) within the fundamental interval. Restoring \(R\) completes the proof.

## Verification
The accompanying standalone `verify.py` uses Python's standard library and 85-digit decimal arithmetic to check the exact-radical coefficients and support identities on 1,001 orientations, the fifth-facet slack factorization, and the analytic area envelope. It also performs 50,000 seeded randomized rectangle tests, of which 27,961 were contained in the pentagon and respected the sharp bound. The recorded execution returned `DECIMAL_SUPPORT_CHECKS 12012` followed by `VERIFY_OK sampled_rectangles=50000 feasible=27961`.

These calculations are finite diagnostics only. The all-orientation theorem and uniqueness follow from the positive-weight support certificate, explicit feasible construction, and trigonometric comparison above.

## Relationship to prior work
Cabello, Cheong, Knauer, and Schlipf (2014) give an exact general algorithm for maximal-area rectangles in convex polygons. Their full-text Sections 1–4 establish computability but do not state this regular-pentagon orientation envelope or its five equality cases. The March 2017 mathematical discussion of this same regular-pentagon problem already suggests a side-supported optimum and its numerical value (after unit-side normalization), but its proposed solutions explicitly assume contact and/or symmetry without proving the unrestricted optimum. The present result does not claim novelty for that guessed configuration or its numerical approximation: its content is the global unconditioned proof, exact orientation profile, and uniqueness.

Sroysang (2015) treats a regular pentagon as a *cover* for all rectangles of prescribed perimeter, an inverse quantifier problem rather than maximizing the area of an arbitrary rectangle in one fixed pentagon. A published result for regular **even** polygons uses central symmetry and does not apply to the odd-sided pentagon. None of the examined statements implies the displayed formula by specialization alone without further optimization or the support certificate.

## Limitations
The theorem addresses Euclidean rectangles in regular pentagons, not general odd regular polygons, parallelograms, or arbitrary convex pentagons. The cited 2014 algorithm can in principle independently compute this example; the contribution is an analytic closed profile and rigidity, not the existence of an exact computational procedure. Public informal discussions contain the correct candidate and approximate area, so no priority is asserted for those parts. Other historical sources may contain an equivalent analytic proof; no exhaustive priority claim is made. There is no independent mathematical audit.

## References
1. S. Cabello, O. Cheong, C. Knauer, and L. Schlipf, *Finding Largest Rectangles in Convex Polygons*, arXiv:1405.1223, first submitted 2014-05-06. https://arxiv.org/html/1405.1223v2.
2. B. Sroysang, *Regular Pentagon Cover for Isoperimetric Rectangles*, Global Journal of Pure and Applied Mathematics **11** (2015), 319–322. https://www.ripublication.com/gjpam%202015/gjpamv11n1_33.pdf.
3. *How to find the maximum area of a rectangle within a pentagon*, Mathematics Stack Exchange question and two responses, 2017-03-01 through 2017-03-06. https://math.stackexchange.com/questions/2166282/how-to-find-the-maximum-area-of-a-rectangle-within-a-pentagon.
4. *Exact maximum-area rectangles in every regular even polygon*, publicly indexed mathematical finding, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-maximum-area-rectangles-in-every-regular-even-polygon--10bad5e59427.
