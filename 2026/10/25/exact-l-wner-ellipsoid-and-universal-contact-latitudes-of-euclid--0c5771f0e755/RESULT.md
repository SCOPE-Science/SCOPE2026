# Exact Löwner ellipsoid and universal contact latitudes of Euclidean capsules

## Finding
For every integer \(d\ge2\) and \(h>0\), the minimum-volume enclosing ellipsoid of the convex hull of two congruent translated Euclidean balls has explicit semiaxes. Its tangencies are two latitude orbits. In Löwner coordinates the absolute axial coordinate of *every* contact equals \(1/\sqrt d\), irrespective of the ball separation. The ellipsoid-to-unit-ball volume ratio has a sharp transition on the scale \(h\asymp d^{-1/2}\).

Define
\[
 t=\frac{2}{\sqrt{(d-1)^2h^2+4d}+(d-1)h},\qquad
 B=1+ht,\qquad A=(1+ht)(1+h/t).
\]
The unique global minimum-volume circumscribed ellipsoid is
\[
 E_{d,h}=\left\{(x_1,x_\perp):\frac{x_1^2}{A}+\frac{\|x_\perp\|^2}{B}\le1\right\}.
\]
Exactly the points
\[
 (\pm(h+t),\sqrt{1-t^2}\,w),\qquad w\in S^{d-2},
\]
on the two rounded cap portions of the capsule touch the ellipsoid. In particular the extreme axial tips \(\pm(h+1)e_1\) are not contacts for any \(h>0\).

## Assumptions and scope
\(B_2^d\) means the Euclidean unit ball, \(e_1\) the first coordinate vector, and
\[
 K_{d,h}:=B_2^d+[-h,h]e_1
   =\operatorname{conv}(B_2^d(he_1,1)\cup B_2^d(-he_1,1)).
\]
The dimension is any integer \(d\ge2\), and the half-separation is any real \(h>0\); no overlap of the generating balls is required. The volume is ordinary \(d\)-dimensional Lebesgue measure. We minimize over *all* translated and rotated nondegenerate ellipsoids, not only axis-symmetric ellipsoids. For \(d=2\), \(S^0=\{-1,1\}\). The limiting case \(h=0\) is a ball, treated only as a limit, not as part of the strict-contact assertion.

## Proof
**Step 1: Exact candidate and support certificate.** The quadratic equation \(dt^2+(d-1)ht=1\) has exactly one positive root, whose displayed expression is positive and less than one. For a unit normal \(u=(u_1,u_\perp)\), write \(s=|u_1|\in[0,1]\). The capsule support function is
\[
 h_K(u)=1+hs,
\]
while the ellipsoid support function is \(h_E(u)=\sqrt{As^2+B(1-s^2)}\). Direct substitution gives the exact identity
\[
 h_E(u)^2-h_K(u)^2=\frac{h}{t}(s-t)^2\ge0.
\]
Both support functions are nonnegative, so \(K_{d,h}\subseteq E_{d,h}\). Equality holds if and only if \(s=t\), yielding precisely the two contact orbits stated above. Their boundary inclusion follows also from uniqueness of support points of the strictly convex ellipsoid. The tips fail to touch because
\[
 A-(1+h)^2=\frac{h}{t}(1-t)^2>0.
\]

**Step 2: Isotropic contact design and global uniqueness.** Let \(T=\operatorname{diag}(A^{-1/2},B^{-1/2},\ldots,B^{-1/2})\) and put \(L=T K_{d,h}\subseteq B_2^d\). The algebraic identity
\[
 \frac{(h+t)^2}{A}=\frac{t(h+t)}{1+ht}=\frac1d
\]
follows from \(dt^2+(d-1)ht=1\); likewise \((1-t^2)/B=(d-1)/d\). Thus the transformed contact points have the form
\[
 z=\left(\frac{\varepsilon}{\sqrt d},\sqrt{\frac{d-1}{d}}\,w\right),
\]
where \(\varepsilon\) takes signs \(\pm1\) equally and \(w\) is uniform on \(S^{d-2}\). This probability measure satisfies \(\mathbb E[z]=0\) and \(\mathbb E[zz^\top]=I_d/d\), including in dimension two. It is supported in \(L\cap S^{d-1}\).

Consider *any* ellipsoid \(F=\{z:(z-c)^\top Q^{-1}(z-c)\le1\}\) containing \(L\), with \(Q\) positive definite. Taking expectations over the contact measure gives
\[
 \frac1d\operatorname{tr}(Q^{-1})+c^\top Q^{-1}c\le1.
\]
By the arithmetic–geometric mean inequality for positive eigenvalues,
\[
 (\det Q^{-1})^{1/d}\le\frac1d\operatorname{tr}(Q^{-1})\le1.
\]
Hence \(\det Q\ge1\); the volume of \(F\) cannot be smaller than the unit ball's. Equality forces \(Q=I_d\) and \(c=0\), so the unit ball uniquely minimizes. Applying \(T^{-1}\) proves the asserted *global* uniqueness of \(E_{d,h}\).

**Step 3: Volume and both dimensional limits.** The axial and transverse semiaxes of \(E_{d,h}\) are \(\sqrt A\) and \(\sqrt B\), the latter with multiplicity \(d-1\). Thus
\[
 R_d(h):=\frac{\operatorname{vol}_d(E_{d,h})}{\operatorname{vol}_d(B_2^d)}
   =(1+ht)^{d/2}\sqrt{1+h/t}.
\]
Put \(\tau_d=h_d\sqrt d\) and \(u_d=t_d\sqrt d\). Their defining equation is
\[
 u_d^2+(1-1/d)\tau_du_d=1.
\]
If \(\tau_d\to\tau\in[0,\infty)\), then \(u_d\to u_\tau\), where
\[
 u_\tau=\frac{\sqrt{\tau^2+4}-\tau}{2},\qquad
 u_\tau^2+\tau u_\tau=1.
\]
Moreover \((1+\tau_du_d/d)^{d/2}\to\exp(\tau u_\tau/2)\), and \(\sqrt{1+\tau_d/u_d}\to1/u_\tau\), proving the stated finite-\(\tau\) crossover. As \(\tau\) increases, \(u_\tau\) strictly decreases, and
\[
 \log\left(\frac{e^{\tau u_\tau/2}}{u_\tau}\right)
 =\frac{1-u_\tau^2}{2}-\log u_\tau
\]
is therefore strictly increasing from zero. Finally if \(\tau_d\to\infty\), then \(u_d\to0\), \(\tau_du_d\to1\), and
\[
 (1+\tau_du_d/d)^{(d-1)/2}\to\sqrt e,
 \qquad \frac{\sqrt{(1+ht)(1+h/t)}}{h\sqrt d}\to1.
\]
This proves \(R_d(h_d)/(h_d\sqrt d)\to\sqrt e\). In particular this latter asymptotic holds for each fixed \(h>0\).

## Verification
A separate standard-library script `verify_capsule.py` recomputes the quadratic root, checks the exact support identity on multiple dimensions, positive separations and unit-normal latitudes, tests contact covariance, and compares finite-dimensional volume factors with both limiting regimes. Run `python3 verify_capsule.py`; the recorded successful run reported 8,442 support comparisons, 42 isotropy/contact checks, 15 finite-crossover comparisons and 3 wide-separation checks (maximum support residual below \(8\cdot10^{-12}\)). These finite arithmetic checks do **not** constitute a proof for all dimensions or continuous parameters; the exact identity, contact-design argument and limits above do.

## Relationship to prior work
The general contact characterization and uniqueness of extremal-volume ellipsoids are classical and appear in Güler–Gürtuna (2007, Section 2) and in Henk (2012). Güler–Gürtuna computes special cases for ball slabs, truncated second-order cones and cylinders (Sections 6–8); a capsule, which has two spherical endcaps and an intervening cylindrical hull, is not one of those solved bodies. Yıldırım (2006) discusses covering ellipsoids for unions of given ellipsoids in algorithmic form; no explicit two-ball capsule formula was verified in accessible material. Halder (2018) treats \(p\)-sums including convex hulls of ellipsoids, but explicitly restricts the summand centers to zero for the outer-ellipsoid parameterization (Assumption 1), whereas our two generating balls have distinct centers. The result here is the explicit entire-dimensional capsule solution, its rigid normalized latitude contacts and crossover limits, rather than the established general criterion itself.

## Limitations
The formulas concern congruent balls translated along one line, not unequal balls, arbitrary ellipsoids, or non-Euclidean norms. They do not describe the maximum-volume inscribed ellipsoid of a two-ball intersection (a different convex body and extremal problem). The sharp asymptotics are for \(d\to\infty\) under precisely the stated scaling assumptions. Literature priority remains provisional: an exact equivalent may exist in uninspected specialized sources, including the inaccessible complete text of Yıldırım (2006). Independent scientific review has not occurred.

## References
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first posted 2007-09-05), especially Sections 2 and 6–8.
- M. Henk, *Löwner–John Ellipsoids* (2012), survey, contact criterion.
- E. A. Yıldırım, *On the Minimum Volume Covering Ellipsoid of Ellipsoids*, SIAM J. Optim. (2006), doi:10.1137/050622560.
- A. Halder, *Smallest Ellipsoid Containing p-Sum of Ellipsoids with Application to Reachability Analysis*, arXiv:1806.07621 (2018), especially Assumption 1 and Sections III–IV.
