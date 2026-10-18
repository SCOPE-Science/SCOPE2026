# Exact John ellipsoids and a sharp aperture transition for spherical sectors

## Finding

Fix an integer \(d\ge2\) and an aperture \(0<\theta\le\pi/2\). Write \((x,y)\in\mathbb R\times\mathbb R^{d-1}\), and consider the unit spherical sector
\[
K_{d,\theta}=\{(x,y):x^2+\|y\|_2^2\le1,\quad x\ge\cot(\theta)\|y\|_2\}.
\]
It has a unique largest-volume inscribed ellipsoid among **all** ellipsoids, without an a priori alignment or center assumption. This is the ellipsoid
\[
E_{d,\theta}=\left\{(x,y):\frac{(x-c)^2}{a^2}+\frac{\|y\|_2^2}{b^2}\le1\right\}
\]
with the following explicit parameters. At the critical aperture \(\theta_*=\arcsin(d^{-1/2})\), the two branches coincide:
\[
\begin{array}{c|ccc}
& a&b&c\\\hline
0<\theta\le\theta_*&\displaystyle\frac1{d+1}&\displaystyle\sqrt{\frac{d-1}{d+1}}\tan\theta&\displaystyle\frac d{d+1}\\[7pt]
\theta_*\le\theta\le\pi/2&\displaystyle\frac{\sqrt d\sin\theta}{d+1}&\displaystyle\sqrt{\frac d{d+1}}\sin\theta&\displaystyle\frac{\sqrt d}{d+1}\sqrt{1+d\cos^2\theta}
\end{array}
\]
Writing \(\omega_d\) for the volume of the unit Euclidean \(d\)-ball, the maximum inscribed-ellipsoid volume is \(\omega_d F_d(\theta)\), where
\[
F_d(\theta)=\begin{cases}
\displaystyle\frac{1}{d+1}\left(\frac{d-1}{d+1}\right)^{(d-1)/2}\tan^{d-1}\theta,&0<\theta\le\theta_*,\\[7pt]
\displaystyle\frac{d^{d/2}}{(d+1)^{(d+1)/2}}\sin^d\theta,&\theta_*\le\theta\le\pi/2.
\end{cases}
\]
The contact geometry changes sharply at \(\theta_*\). For smaller apertures the only spherical-boundary contact of the ellipsoid is the axial tip \((1,0)\); for larger apertures its spherical contacts are a nonaxial latitude sphere. The cone boundary is touched in a transverse latitude sphere in both regimes (at \(\theta=\pi/2\), this cone-contact orbit degenerates to one point). The function \(\log F_d(\theta)\) is continuously differentiable across \(\theta_*\), but its right second derivative minus its left second derivative equals \(-2d\).

## Assumptions and scope

All norms are standard Euclidean norms. The aperture lies in \((0,\pi/2]\), so \(K_{d,\theta}\) is a full-dimensional, compact, convex intersection of a Euclidean ball and a circular cone. At \(\theta=\pi/2\) it is a half-ball. The limiting case \(\theta=0\) is excluded: the sector then has zero \(d\)-volume and no full-dimensional inscribed ellipsoid. The result concerns maximum **inscribed** ellipsoids; it does not concern minimum covering ellipsoids. At every finite positive aperture the center \(c\), axial semiaxis \(a\), and transverse semiaxis \(b\) are strictly positive.

## Proof

**1. Containment in the cone.** Put \(k=\cot\theta\). For any ellipsoid of the stated axial form, write a boundary point as \((c+au,b\sqrt{1-u^2}\,\omega)\), where \(-1\le u\le1\) and \(\|\omega\|_2=1\). The condition for all its points to lie in the cone is
\[
c\ge\max_{-1\le u\le1}\{k b\sqrt{1-u^2}-au\}=\sqrt{a^2+k^2b^2}.
\]
Both formula branches satisfy the exact equality \(c^2=a^2+k^2b^2\). Thus the ellipsoids lie in the cone and touch its boundary at the normalized axial coordinate \(u=-t\), where \(t=a/c\).

**2. Containment in the ball.** The squared Euclidean norm of a point on the ellipsoid boundary with normalized axial coordinate \(u\) equals
\[
q(u)=c^2+b^2+2cau+(a^2-b^2)u^2.
\]
For the first branch, \(b^2-a^2\le ca\) is exactly equivalent to \(\tan^2\theta\le1/(d-1)\). Therefore \(q\) attains its maximum at \(u=1\), where \(q(1)=(c+a)^2=1\). For the second branch define
\[
\gamma=\sqrt{1+(d+1)\cot^2\theta}=\frac{c}{a}.
\]
Then \(b^2=(d+1)a^2\), so \(q\) has its maximum at \(u=v=\gamma/d\), which satisfies \(0<v\le1\) precisely for \(\sin^2\theta\ge1/d\). Direct substitution gives
\[
q(v)=\frac{d+1}{d}c^2+b^2=1.
\]
Consequently the proposed ellipsoid is contained in the ball. Equality occurs only at the tip in the strict first regime and along the transverse latitude \(u=v\) in the strict second regime; the latitude collapses to the tip when \(v=1\) at the threshold.

**3. Global optimality, with an explicit finite John certificate.** Normalize the constructed ellipsoid to the unit ball using the invertible affine map \((x,y)\mapsto((x-c)/a,y/b)\). A standard sufficient optimality criterion for a unit ball inscribed in a convex body is the existence of boundary contacts \(z_i\) and positive weights \(\lambda_i\) with
\[
\sum_i\lambda_i z_i=0,\qquad\sum_i\lambda_i z_i z_i^{\mathsf T}=I_d.
\]
For completeness, this criterion yields the volume bound by applying the contact supporting halfspaces to any competing ellipsoid: represent it as \(h+TB_2^d\) with \(T\) symmetric positive definite. Because the transformed convex body contains the unit ball, its common boundary contact \(z_i\) has the supporting halfspace \(z_i\cdot x\le1\), whence \(z_i\cdot h+\|Tz_i\|_2\le1\). Since \(z_i\cdot Tz_i\le\|Tz_i\|_2\), weighted summation gives \(\operatorname{tr}T\le d\). Arithmetic–geometric mean on the positive eigenvalues gives \(\det T\le(\operatorname{tr}T/d)^d\le1\). The usual Fritz John theorem also gives uniqueness of the maximal ellipsoid.

Let \(e_1,\ldots,e_{d-1}\) be the standard basis of the transverse coordinate space. The normalized cone contacts are
\[
z_{j,\pm}=(-t,\ \pm\sqrt{1-t^2}\,e_j),\qquad 1\le j\le d-1.
\]
For \(0<\theta\le\theta_*\), set \(t=1/d\), \(W=d^2/(d+1)\), and \(D=d/(d+1)\). Give each cone contact weight \(W/[2(d-1)]\), and give the tip contact \((1,0)\) weight \(D\). The weighted first moment vanishes because \(-Wt+D=0\). The axial second moment is \(Wt^2+D=1\); the transverse second-moment coefficient is \(W(1-t^2)/(d-1)=1\). All cross moments vanish by pairing signs. Hence the John criterion holds.

For \(\theta_*\le\theta\le\pi/2\), keep the cone contacts with \(t=1/\gamma\), and use additional spherical contacts
\[
z'_{j,\pm}=(v,\ \pm\sqrt{1-v^2}\,e_j),\qquad v=\gamma/d.
\]
These are real contacts because \(tv=1/d\), \(0<t\le1\), and \(0<v\le1\). Assign equal weights within each orbit with respective total orbit weights
\[
W=\frac{dv}{t+v}=\frac{d\gamma^2}{d+\gamma^2},\qquad
D=\frac{dt}{t+v}=\frac{d^2}{d+\gamma^2}.
\]
Then \(W+D=d\), \(-Wt+Dv=0\), and \(Wt^2+Dv^2=1\). Subtracting the axial second moment from the trace \(d\) shows that the transverse second moment has coefficient one; sign symmetry kills off-diagonal moments. The John criterion again holds. At \(\theta=\theta_*\), the spherical orbit is a repeated tip, and at \(\theta=\pi/2\), the cone orbit is a repeated axial point. Combining coincident points preserves positivity and both moment identities. Therefore the displayed ellipsoid is **globally** maximal among all translated and rotated ellipsoids in every stated case. Uniqueness is the usual uniqueness part of the John ellipsoid theorem.

**4. Volume and transition regularity.** The volume of the axial ellipsoid is \(\omega_d a b^{d-1}\), yielding the two stated formulas by substitution. Their values and first derivatives agree at \(\sin^2\theta_*=1/d\). Direct differentiation gives
\[
(\log F_d)'=\begin{cases}
(d-1)/(\sin\theta\cos\theta),&\theta<\theta_*,\\
d\cot\theta,&\theta>\theta_*.
\end{cases}
\]
The one-sided second derivatives at the critical angle are respectively \(-d(d-2)\) and \(-d^2\). Thus the second-derivative jump is exactly \(-2d\), proving the stated sharp transition.

## Verification

The standalone file `check_spherical_sector.py` checks the exact rational identities for cone and ball containment at rational values of \(\sin^2\theta\) in dimensions \(2,3,5,9\), verifies the normalized weighted-contact first and second moments, and independently optimizes the three axial parameters numerically in ten cases. It can be executed with `python3 check_spherical_sector.py` using Python with NumPy and SciPy installed. All ten specified cases passed in the recorded run. The analytical containment and John-certificate arguments, not these finite computations, prove the result for every integer \(d\ge2\) and every allowed real \(\theta\).

## Relationship to prior work

Güler and Gürtuna (2007), arXiv:0709.0707, explain Fritz John's optimality conditions and derive extremal ellipsoids for ellipsoidal *slabs* and flat truncated second-order cones. Their detailed introduction, inscribed-ellipsoid section and cone section give no formula for the present intersection of a Euclidean ball with a circular cone. In particular, the curved sphere plus sloping conic side here cannot be recovered from a parallel-plane slab or a flat truncation by a mere parameter substitution. Ivanov, Lángi, Naszódi and Sagmeister (2025), arXiv:2507.06947, develop necessary conditions for ellipsoids of revolution, not this explicit all-dimensional John ellipsoid with a two-regime contact transition. Published related results about half-cones and capped hypercubes concern different boundary geometries. John optimality itself is classical and is **not** asserted to be new. The asserted new content is the spherical-sector formula, sharp critical aperture, contact classification, and differentiability jump.

## Limitations

No formula is claimed for apertures larger than \(\pi/2\), where the conic description changes, or for affine deformations with a ball no longer Euclidean. The theorem addresses ellipsoid volume rather than filling fraction by the sector, and is not an independent verification of every possible historical priority claim. A particularly related independently indexed result on the John ellipsoid of a *flat* circular half-cone was available only in indexed summary form during comparison; hidden implications in inaccessible supporting documents cannot be excluded by keyword searches. Independent audit has not been performed.

## References

1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, first public version 5 September 2007, arXiv:0709.0707, https://arxiv.org/abs/0709.0707 .
2. G. Ivanov, Z. Lángi, M. Naszódi and Á. Sagmeister, *John Ellipsoids of Revolution*, first public version 9 July 2025, arXiv:2507.06947, https://arxiv.org/abs/2507.06947 .
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday*, 1948, pp. 187–204 (classical contact criterion).
