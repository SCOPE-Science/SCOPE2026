# Exact John and Löwner ellipsoids of the Minkowski sum of two perpendicular disks

## Finding
Let \(a,b>0\), and let \(K_{a,b}\subset\mathbb R^3\) be the Minkowski sum of the two centered, perpendicular filled disks
\[
D_a=\{(x,y,0):x^2+y^2\le a^2\},\qquad
D_b=\{(0,y,z):y^2+z^2\le b^2\}.
\]
The unique maximum-volume inscribed (John) ellipsoid is
\[
J_{a,b}=\left\{(x,y,z):\frac{x^2}{a^2}+\frac{y^2}{(a+b)^2}+\frac{z^2}{b^2}\le1\right\}.
\]
Put \(r=b/a\), and let \(t=t(r)\) be the unique positive root of
\[
2t^2+(r^2-1)t-2r^2=0,
\qquad
 t=\frac{1-r^2+\sqrt{(1-r^2)^2+16r^2}}4.
\]
Define
\[
p=a\sqrt{1+t},\qquad q=\sqrt{a^2(1+t)+b^2(1+t^{-1})},
\qquad h=b\sqrt{1+t^{-1}}.
\]
The unique minimum-volume enclosing (Löwner) ellipsoid among **all** translated and arbitrarily oriented ellipsoids is
\[
L_{a,b}=\left\{(x,y,z):\frac{x^2}{p^2}+\frac{y^2}{q^2}+\frac{z^2}{h^2}\le1\right\}.
\]
There is a finite, explicit, positive contact distribution on \(K_{a,b}\cap\partial L_{a,b}\) whose mean is zero and covariance is \(\operatorname{diag}(p^2,q^2,h^2)/3\); its construction below certifies unrestricted global optimality, not merely optimality within a prescribed family of ellipsoidal bounds.

The body has \(\operatorname{Vol}(K_{a,b})=2\pi ab(a+b)\), and its sharp volume ratios satisfy
\[
\frac{\operatorname{Vol}(J_{a,b})}{\operatorname{Vol}(K_{a,b})}=\frac23,
\qquad
\frac43\le \frac{\operatorname{Vol}(L_{a,b})}{\operatorname{Vol}(K_{a,b})}<\sqrt3.
\]
The lower outer ratio is attained **if and only if** \(a=b\). The upper bound is the sharp unattained supremum, approached as \(b/a\to0\) or \(b/a\to\infty\). The outer ratio decreases strictly for \(0<b/a<1\) and increases strictly for \(b/a>1\).

## Assumptions and scope
All sets are closed and endowed with ordinary Euclidean volume and Euclidean ellipsoids. Each disk is filled, two-dimensional, centered at the origin, and lies in one of the specified perpendicular coordinate planes; their line of intersection is the \(y\)-axis. Both radii are strictly positive and otherwise unrestricted. A translated ellipsoid with positive-definite symmetric shape matrix \(Q\) is written \(c+E(Q)=\{c+v:v^TQ^{-1}v\le1\}\); its volume is \((4\pi/3)\sqrt{\det Q}\). Both extremal problems range over **every** such ellipsoid, without assuming coordinate alignment or centrality.

## Proof
**1. Exact body description and volume.** For every \(|x|\le a\) and \(|z|\le b\), the allowable \(y\)-interval in \(K_{a,b}\) is precisely
\[
|y|\le \sqrt{a^2-x^2}+\sqrt{b^2-z^2}.
\]
Integrating its length over the rectangle yields
\[
\operatorname{Vol}(K_{a,b})=
2\int_{-a}^{a}\!\int_{-b}^{b}
\bigl(\sqrt{a^2-x^2}+\sqrt{b^2-z^2}\bigr)\,dz\,dx
=2\pi ab(a+b).
\]
The support function of \(K_{a,b}\) is
\[
H(u)=a\sqrt{u_x^2+u_y^2}+b\sqrt{u_y^2+u_z^2}.
\]

**2. Exact John ellipsoid, including uniqueness.** The Euclidean triangle inequality gives
\[
\sqrt{a^2u_x^2+(a+b)^2u_y^2+b^2u_z^2}
\le H(u)
\]
for every \(u\in\mathbb R^3\), by decomposing the vector inside the left norm as \((au_x,au_y,0)+(0,bu_y,bu_z)\). Hence \(J_{a,b}\subset K_{a,b}\). Conversely \(K_{a,b}\) lies in the coordinate box with half-side lengths \(a,a+b,b\). For any ellipsoid \(c+E(Q)\) inside this box, its two coordinate support inequalities give
\[
|c_i|+\sqrt{Q_{ii}}\le(a,a+b,b)_i.
\]
Hadamard's determinant inequality implies \(\det Q\le\prod_iQ_{ii}\le a^2(a+b)^2b^2\), attained by \(J_{a,b}\). Equality forces \(c=0\) and \(Q=\operatorname{diag}(a^2,(a+b)^2,b^2)\), proving uniqueness without presupposing symmetry of competitors.

**3. A containing ellipsoid.** For every \(t>0\), write \(A=a\sqrt{u_x^2+u_y^2}\) and \(B=b\sqrt{u_y^2+u_z^2}\). The identity
\[
(1+t)A^2+(1+t^{-1})B^2-(A+B)^2
=(\sqrt t\,A-B/\sqrt t)^2\ge0
\]
shows that \(K_{a,b}\subset E(Q_t)\), with
\[
Q_t=\operatorname{diag}\bigl(a^2(1+t),\;a^2(1+t)+b^2(1+t^{-1}),\;b^2(1+t^{-1})\bigr).
\]
Its squared volume, apart from a positive factor independent of \(t\), is
\[
a^2b^2\frac{(1+t)^3(a^2t+b^2)}{t^2}.
\]
The derivative in \(t\) has the sign of \(2a^2t^2+(b^2-a^2)t-2b^2\), which has one positive root, namely the displayed \(t(r)\). At that root \(1/2<t<2\).

**4. Explicit contact certificate.** Fix this root. Set
\[
s_*=\min\{1,t/r\},\quad \lambda=\frac{2-t}{3s_*^2},\quad
v(s)=\frac{r}{t}s\qquad(0\le s\le s_*).
\]
Both \(s\) and \(v(s)\) lie in \([0,1]\). For independent signs \(\sigma_x,\sigma_y,\sigma_z\in\{-1,+1\}\), form
\[
X_\sigma(s)=\bigl(\sigma_x a\sqrt{1-s^2},\ \sigma_y(as+bv(s)),\ \sigma_z b\sqrt{1-v(s)^2}\bigr).
\]
Each point lies in \(K_{a,b}\), being the sum of one boundary point of each disk. Its squared normalized coordinates satisfy
\[
\frac{X_x(s)^2}{p^2}=\frac{1-s^2}{1+t},\quad
\frac{X_z(s)^2}{h^2}=\frac{t(1-v(s)^2)}{1+t},\quad
\frac{X_y(s)^2}{q^2}=\frac{s^2+t v(s)^2}{1+t}.
\]
The sum is one. Thus **every** \(X_\sigma(s)\) contacts \(L_{a,b}\). The root relation can be rewritten as
\[
r^2(2-t)=t(2t-1).
\]
It implies \(0<\lambda<1\): if \(s_*=1\), then \(\lambda=(2-t)/3<1\); if \(s_*=t/r\), then \(\lambda=(2t-1)/(3t)<1\).

Take \(S=0\) with probability \(1-\lambda\), and \(S=s_*\) with probability \(\lambda\). Independently choose the three signs uniformly, and set \(X=X_\sigma(S)\). Then \(\mathbb E X=0\); sign symmetry removes off-diagonal covariances. The normalized \(x\)-second moment is
\[
\mathbb E(X_x^2/p^2)=\frac{1-\lambda s_*^2}{1+t}
=\frac{1-(2-t)/3}{1+t}=\frac13.
\]
The normalized \(z\)-second moment, using the root relation, is
\[
\mathbb E(X_z^2/h^2)
=\frac{t}{1+t}\left(1-\frac{r^2}{t^2}\frac{2-t}{3}\right)
=\frac13.
\]
The normalized \(y\)-second moment must also equal \(1/3\), since their sum is one on the support. Consequently
\[
\mathbb E X=0,\qquad \mathbb E(XX^T)=Q_t/3.
\]

**5. Unrestricted Löwner optimality.** Let \(c+E(Q)\) be *any* containing ellipsoid, with arbitrary center \(c\) and positive-definite \(Q\). Every contact point above lies in it; integrating its defining quadratic inequality gives
\[
1\ge \mathbb E[(X-c)^TQ^{-1}(X-c)]
=\tfrac13\operatorname{tr}(Q^{-1}Q_t)+c^TQ^{-1}c
\ge\left(\frac{\det Q_t}{\det Q}\right)^{1/3}.
\]
The last step is the arithmetic-geometric mean inequality applied to the positive eigenvalues of \(Q^{-1/2}Q_tQ^{-1/2}\). Thus \(\det Q\ge\det Q_t\). Equality requires \(c=0\) and \(Q=Q_t\), so \(L_{a,b}=E(Q_t)\) is the unique global minimum-volume enclosing ellipsoid. This contact measure also supplies a finite optimality certificate, without assuming that a scalar-parametrized bounding family is globally optimal.

**6. Sharp volume-ratio profile.** With \(r=b/a\) and \(t=t(r)\), put \(R(r)=\operatorname{Vol}(L_{a,b})/\operatorname{Vol}(K_{a,b})\). The formulas above give
\[
R(r)=\frac23\frac{\sqrt{(1+t)^3(t+r^2)/t^2}}{1+r}.
\]
Differentiation along the optimizing root (the \(t\)-derivative vanishes) yields
\[
\frac{d}{dr}\log R(r)
=\frac{r}{t+r^2}-\frac1{1+r}
=\frac{r-t}{(t+r^2)(1+r)}.
\]
The polynomial \(P_r(z)=2z^2+(r^2-1)z-2r^2\) has exactly one positive zero \(t\), while \(P_r(r)=r(r^2-1)\). Hence \(r-t\) has the sign of \(r-1\). The ratio is minimized uniquely at \(r=1\), where \(t=1\) and \(R(1)=4/3\). As \(r\downarrow0\), \(t\to1/2\) and \(R(r)\to\sqrt3\); the interchange symmetry \((a,b,x,z)\leftrightarrow(b,a,z,x)\) gives the same limit as \(r\to\infty\). Neither limiting ratio is reached for \(a,b>0\). Finally, the John ratio is \((4\pi/3)ab(a+b)/(2\pi ab(a+b))=2/3\).

## Verification
Running `python verify_ellipsoids.py` with Python 3 and SymPy checks the exact stationarity and contact-moment polynomial identities, the contact covariance at five nontrivial radius pairs, the two containment inequalities at thousands of independently generated test points, and the announced volume-ratio bounds. It reports 40030 supplementary consistency checks. These finite checks are **not** substitutes for the universal algebraic proof and contact certificate above. In particular, the numerical scans do not establish global ellipsoidal optimality; step 5 does.

## Relationship to prior work
Finch's arXiv preprint [1] studies the **convex hull**, not the Minkowski sum, of two perpendicular disks and focuses on volume, surface area, and mean width; those operations create different bodies. Seeger [2, Theorem 2.3] gives a general intersection representation of Minkowski sums of even singular ellipsoids as a family of enclosing ellipsoids. This establishes the available outer bounds, but the intersection identity alone does not identify the unrestricted minimum-volume member or the optimal inscribed ellipsoid. Halder [3, Sections II–IV] studies determinant minimization **within a parameterized family** of outer ellipsoids for Minkowski sums of positive-definite ellipsoids, including a scalar stationarity method. The scalar family and its determinant optimization are therefore prior art; the claims here are the explicit singular perpendicular-disk specialization **together with** an unrestricted Löwner contact certificate, a simultaneous exact John ellipsoid, and the sharp body-normalized volume-ratio profile. A later treatment [4] also discusses parameterized minimum-volume outer approximations for general positive-definite summands. The specific earlier or equivalent evaluation of this combined perpendicular-disk result has not been excluded beyond the cited search and inspections.

## Limitations
This is a three-dimensional theorem for exactly two disks meeting at a right angle through their centers. It does not give exact ellipsoids for oblique disks, displaced disks, three disks, or arbitrary nonsingular input ellipsoids. The provenance comparison does not constitute independent historical-priority certification. The supporting numerical experiments are finite.

## References
[1] S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first version publicly posted 2012-11-19), https://arxiv.org/abs/1211.4514.

[2] A. Seeger, *Calculus rules for combinations of ellipsoids and applications*, Bulletin of the Australian Mathematical Society **47** (1993), 1–12, https://doi.org/10.1017/S0004972700012211.

[3] A. Halder, *On the Parameterized Computation of Minimum Volume Outer Ellipsoid of Minkowski Sum of Ellipsoids*, arXiv:1803.08157 (2018), https://arxiv.org/abs/1803.08157.

[4] A. Halder, *Smallest Ellipsoid Containing \(p\)-Sum of Ellipsoids with Application to Reachability Analysis*, arXiv:1806.07621 (2018), https://arxiv.org/abs/1806.07621.
