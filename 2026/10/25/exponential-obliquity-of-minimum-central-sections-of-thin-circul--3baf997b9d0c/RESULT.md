# Exponential obliquity of minimum central sections of thin circular double cones

## Finding
For \(k>0\), consider the convex solid right circular double cone
\[
C_k=\{(x,y,z)\in\mathbb R^3:\sqrt{x^2+y^2}+|z|/k\le1\}.
\]
Its equatorial disk has radius one and its two axial apices are at heights \(\pm k\). For any central plane with unit normal \(u\), put \(c=|u_z|\) and let \(S_k(c)\) denote the area of its section. The exact angular profile is
\[
S_k(c)=4\sqrt{k^2+\xi^2}\,F(\xi),\qquad
\xi=\frac{kc}{\sqrt{1-c^2}},\qquad
F(\xi)=\int_\xi^\infty\frac{\sqrt{t^2-\xi^2}}{(1+t)^3}\,dt,
\]
for \(0\le c<1\), completed continuously by \(S_k(1)=\pi\). In particular \(S_k(0)=2k\), the area of an axial-containing section, but
\[
\min_{0\le c\le1}S_k(c)<2k\qquad\text{for every }k>0.
\]
For all sufficiently small \(k>0\), there is exactly one minimizing value \(c_k\in(0,1)\); rotational symmetry makes the complete family of minimizers one orbit about the symmetry axis. Its obliquity and the strictly positive area gain satisfy
\[
\boxed{c_k\sim\frac{2e^{-3/2}}{k}\exp\!\left(-\frac1{2k^2}\right)},\qquad
\boxed{2k-\min_cS_k(c)\sim 4ke^{-3}\exp\!\left(-\frac1{k^2}\right)}
\qquad(k\downarrow0).
\]
Thus the apparently optimal axial-containing plane misses the true minimum by an exponentially small amount, and the optimal tilt is itself exponentially small in the inverse squared aspect ratio.

## Assumptions and scope
Only Euclidean area and central two-dimensional plane sections of the **solid** circular double cone are considered. The parameter \(k\) is the positive apex half-height divided by the equatorial radius. The plane normal is Haar-uniform only if one chooses to randomize; no distributional assumption is needed here. Because the body is axially rotationally symmetric and centrally symmetric, the area depends solely on \(c=|u_z|\in[0,1]\). A minimizing value of \(c\) represents all planes obtained by rotation around the common axis. The uniqueness conclusion is asserted for all sufficiently small positive \(k\), **not** uniformly over all positive aspect ratios. For general equatorial radius \(r\), section areas acquire a multiplier \(r^2\) after setting \(k=h/r\).

## Proof
**Area reduction.** By axial symmetry rotate the normal to \(u=(\sqrt{1-c^2},0,c)\). Parametrize its plane orthonormally as \((x,y,z)=(cs,t,-\sqrt{1-c^2}\,s)\). The double-cone inequality on that plane is
\[
\sqrt{c^2s^2+t^2}+\frac{\sqrt{1-c^2}}{k}|s|\le1.
\]
Put \(a=\sqrt{1-c^2}/k\) and \(b=c\). Symmetry over the two planar coordinate axes gives exactly
\[
S_k(c)=4\int_0^{1/(a+b)}\sqrt{(1-as)^2-b^2s^2}\,ds.
\tag{1}
\]
For \(c<1\) set \(\xi=b/a\) and first replace \(s\) by \(v=as\), then by \(t=(1-v)/v\). This yields
\[
S_k(c)=\frac4a\int_\xi^\infty\frac{\sqrt{t^2-\xi^2}}{(1+t)^3}\,dt
=4\sqrt{k^2+\xi^2}\,F(\xi),
\]
using \(a=1/\sqrt{k^2+\xi^2}\). At \(c=0\), elementary integration gives \(F(0)=1/2\) and \(S_k(0)=2k\). At \(c=1\), the section is the equatorial unit disk and has area \(\pi\).

**Closed form and differentiation.** An elementary integration, valid for positive \(\xi\), gives
\[
F(\xi)=
\begin{cases}
\displaystyle \frac1{2(1-\xi^2)}-\frac{\xi^2\operatorname{artanh}\sqrt{1-\xi^2}}{2(1-\xi^2)^{3/2}},&0<\xi<1,\\[4pt]
1/3,&\xi=1,\\[4pt]
\displaystyle\frac{\xi^2\arctan\sqrt{\xi^2-1}/\sqrt{\xi^2-1}-1}{2(\xi^2-1)},&\xi>1.
\end{cases}
\tag{2}
\]
Differentiation of the absolutely convergent defining integral, with \(t=\xi\cosh v\), shows
\[
F'(\xi)=-\xi I(\xi),\qquad
I(\xi)=\int_0^\infty(1+\xi\cosh v)^{-3}\,dv>0.
\tag{3}
\]
Consequently
\[
\frac{d}{d\xi}\bigl(4\sqrt{k^2+\xi^2}F(\xi)\bigr)
=\frac{4\xi}{\sqrt{k^2+\xi^2}}\bigl(F(\xi)-(k^2+\xi^2)I(\xi)\bigr).
\tag{4}
\]
Both \(F\) and \(I\) are positive and smooth on \((0,\infty)\).

**Logarithmic boundary layer.** Write \(L=\log(2/\xi)\). Expanding (2) directly as \(\xi\downarrow0\), and differentiating the explicit expression (not an uncontrolled remainder), gives
\[
F(\xi)=\frac12-\frac{\xi^2}{2}(L-1)+O(\xi^4L),\quad
I(\xi)=L-\frac32+O(\xi^2L),\quad
I'(\xi)=-\frac1\xi+O(\xi L).
\tag{5}
\]
For every fixed \(k>0\), (4) is strictly negative for all sufficiently small positive \(\xi\), because \(I(\xi)\to\infty\) while \(F(\xi)\to1/2\). Hence the axial-containing plane, at \(\xi=0\), is never a global minimizer: some arbitrarily slightly oblique central plane has strictly smaller area. The endpoint \(\xi=\infty\) has area \(\pi\), and the area profile extends continuously to the compact orientation interval, so a global minimum always exists.

**Uniqueness for thin cones.** For sufficiently small \(k\), \(2k<\pi\), so the global minimum is attained at an interior parameter \(\xi_k>0\). As \(k\downarrow0\), any such minimizer satisfies \(S_k(\xi_k)\le2k\to0\). But \(S_k(\xi)\ge4\xi F(\xi)\), and the continuous positive function \(4\xi F(\xi)\) stays bounded away from zero on every \([\delta,\infty)\), since it tends to \(\pi\) at infinity. Thus **every** minimizing parameter has \(\xi_k\to0\). The same area inequality gives
\[
\sqrt{1+(\xi_k/k)^2}\le\frac1{2F(\xi_k)}\to1,
\]
so \(\xi_k/k\to0\). Every interior minimizing point satisfies the exact stationary equation
\[
k^2=Q(\xi_k),\qquad Q(\xi)=\frac{F(\xi)}{I(\xi)}-\xi^2.
\tag{6}
\]
By (3) and (5),
\[
Q'(\xi)=-3\xi-\frac{F(\xi)I'(\xi)}{I(\xi)^2}
\sim\frac1{2\xi[\log(2/\xi)]^2}>0
\qquad(\xi\downarrow0).
\tag{7}
\]
There is therefore a fixed punctured interval near zero on which \(Q\) is strictly increasing. All global minimizers eventually lie in that interval and satisfy (6); strict monotonicity forces **one** minimizing parameter for every sufficiently small \(k>0\). The rotational orbit is then unique.

**Sharp exponent and prefactor.** From (5) and (6), \(Q(\xi)\sim[2\log(2/\xi)]^{-1}\), hence \(L_k:=\log(2/\xi_k)\sim1/(2k^2)\). In particular \(\xi_k\) is exponentially small, making its products with every fixed power of \(1/k\) negligible. Replacing \(I\) and \(F\) in the stationary equality \(I(\xi_k)=F(\xi_k)/(k^2+\xi_k^2)\) by the quantitative expansions in (5) now gives
\[
L_k=\frac1{2k^2}+\frac32+o(1).
\]
Therefore
\[
\xi_k=2e^{-3/2}e^{-1/(2k^2)}(1+o(1)),\qquad
c_k=\frac{\xi_k}{\sqrt{k^2+\xi_k^2}}
\sim\frac{2e^{-3/2}}{k}e^{-1/(2k^2)}.
\]
Finally, inserting (5) into the exact area expression and using \(\xi_k/k\to0\),
\[
2k-S_k(c_k)=\xi_k^2\left[2k(L_k-1)-\frac1k\right]
+O\!\left(\frac{\xi_k^4}{k^3}+k\xi_k^4L_k\right)
=k\xi_k^2(1+o(1))
=4ke^{-3}e^{-1/k^2}(1+o(1)).
\]
This completes both assertions. All limits use real positive \(k\downarrow0\).

## Verification
The accompanying ordinary-Python checker `verify.py` recomputes the integral in (2) independently from its positive integral definition, checks (3) by a separate cosh-integral, directly evaluates nine plane sections through (1), and solves (6) at seven small aspect ratios. It reproduces the predicted obliquity and deficit constants across decreasing \(k\). A passing numerical checker establishes neither global uniqueness nor an asymptotic limit; those follow from the analytic compactness, strict-local-monotonicity, and expansion arguments above.

## Relationship to prior work
Saroglou's 2014 work on double cones and second projection bodies uses the circular double cone as a sharp equality body for a **projection-body quotient** and studies integrals of powers of parallel section areas. Its Theorems 1.4–1.5 and Section 5 do not establish the present *pointwise minimization of central section area* as a function of the plane normal. A publicly archived study of bisector sections of affine double cones evaluates the **offset-section profile in one fixed bisector direction** and a normalized integral functional, but does not minimize central sections over every direction or analyze the thin-aspect exponential shift. A separate study of canonical cuts of *oblique one-apex circular cones* minimizes ratios of curved surface areas, not central plane-sectional areas of a symmetric bicone. The mathematical objects, optimized quantities, and implications were compared; the new result is not asserted to be implied merely by the classical cone section formula.

## Limitations
The global uniqueness theorem is established only when the half-height-to-radius ratio is sufficiently small; it does not classify global minimizing directions at arbitrary aspect ratios. The exact profile holds for every positive ratio. This is an asymptotic deterministic section-area result, not a theorem on random or offset sections. The exact smallest height threshold for uniqueness is not found. An equivalent classical calculation of tilted sections might exist under different terminology; historical priority is not definitively certified. Independent mathematical validation has not been performed.

## References
1. Christos Saroglou, *On the shape of a convex body with respect to its second projection body*, arXiv:1409.4347v1, first posted 15 September 2014; particularly Theorems 1.4–1.5 and Section 5. https://arxiv.org/abs/1409.4347.
2. *Bisector sections of affine double cones and a strict section-root gap*, publicly archived research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-bisector-sections-of-affine-double-cones-and-a-strict-section-ro--f83ae948e0d8.
3. *Global surface-ratio minima for bisected oblique circular cones*, publicly archived research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-global-surface-ratio-minima-for-bisected-oblique-circular-cones--7a73be4946e2.
