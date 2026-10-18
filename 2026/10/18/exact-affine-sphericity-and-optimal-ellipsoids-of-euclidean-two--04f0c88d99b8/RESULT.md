# Exact affine sphericity and optimal ellipsoids of Euclidean two-ball lenses

## Finding

For every integer \(d\ge2\) and every \(0<c<1\), consider the centrally symmetric intersection of two unit balls with center separation \(2c\):
\[
L_c=B_2^d(ce_1,1)\cap B_2^d(-ce_1,1).
\]
The three natural ellipsoidal approximations of this lens can be determined explicitly in every dimension: its unique minimum-volume containing ellipsoid, its unique maximum-volume contained ellipsoid, and an affine-optimally sandwiched ellipsoid attaining the Banach–Mazur distance to the Euclidean ball.

Let \(E(a,b)=\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:x^2/a^2+\|z\|_2^2/b^2\le1\}\), and define
\[
A=1-c,\qquad B=\sqrt{1-c^2},\qquad
\tau=\sqrt{\frac{2+c}{2(1+c)}}.
\]
Then the unique Löwner ellipsoid is
\[
E_{\mathrm{out}}=E(A,B),
\]
and the Banach–Mazur distance is **exactly**
\[
\boxed{d_{\mathrm{BM}}(L_c,B_2^d)=\tau^{-1}=\sqrt{\frac{2(1+c)}{2+c}}.}
\]
An ellipsoid attaining this optimum is \(E_{\mathrm{BM}}=E(\tau A,\tau B)\); in particular \(E_{\mathrm{BM}}\subset L_c\subset\tau^{-1}E_{\mathrm{BM}}\). The distance formula is independent of \(d\), increases strictly with \(c\), tends to \(1\) as \(c\downarrow0\), and tends to \(2/\sqrt3\) as \(c\uparrow1\).

The unique John ellipsoid is \(E_J=E(a_J,b_J)\), where \(a_J\) is the unique positive root of
\[
\boxed{a_J^2+\frac{d+1}{\sqrt d}\,c a_J+c^2=1,\qquad
b_J^2=a_J^2+c\sqrt d\,a_J.}
\]
For an explicit expression free of subtraction cancellation, put \(q=(d+1)c/\sqrt d\); then \(a_J=2(1-c^2)/(\sqrt{q^2+4(1-c^2)}+q)\). Every John contact lies at one of the two axial latitudes \(x=\pm a_J/\sqrt d\).

For every \(d\ge2\) and \(0<c<1\), the canonical John and Banach–Mazur ellipsoids are different. The Löwner, John and affine-distance ellipsoids therefore solve genuinely different optimization problems in this family.

## Assumptions and scope

The balls are closed Euclidean unit balls in \(\mathbb R^d\); their centers are \(\pm ce_1\) with \(0<c<1\), ensuring nonempty interior. Coordinates are written \((x,z)\in\mathbb R\times\mathbb R^{d-1}\). The lens is given exactly by
\[
L_c=\{(x,z): (|x|+c)^2+\|z\|_2^2\le1\}.
\]
The Banach–Mazur distance here is the infimum of \(\lambda\ge1\) for which an affine ellipsoid \(F\) satisfies \(F\subset L_c\subset\lambda F\); since \(L_c\) is centrally symmetric, translations can be eliminated (see the centering argument below). Uniqueness of the John and Löwner ellipsoids is classical. Uniqueness of a general nonsymmetric-orientation distance ellipsoid is *not* part of the claim. Endpoints \(c=0\) (the ball) and \(c=1\) (a degenerate singleton) are excluded; only limits are asserted.

## Proof

**1. Minimum-volume containing ellipsoid.** The uniqueness theorem for minimum-volume containing ellipsoids implies that the outer ellipsoid inherits the symmetries \((x,z)\mapsto(\pm x,Uz)\), \(U\in O(d-1)\), and so equals \(E(a,b)\) for some \(a,b>0\). The lens contains its axial endpoints \((\pm A,0)\) and transverse equator \((0,Bv)\), \(v\in\mathbb S^{d-2}\); hence \(a\ge A\) and \(b\ge B\). On the boundary of \(E(A,B)\), for \(0\le x\le A\), the available transverse squared radius minus the lens radius squared is
\[
B^2\bigl(1-x^2/A^2\bigr)-\bigl(1-(c+x)^2\bigr)=2cx(1-x/A)\ge0.
\]
Thus \(L_c\subset E(A,B)\), whose volume is minimal among rotation-symmetric containing ellipsoids by the independent lower bounds on both semiaxes; uniqueness finishes the claim.

**2. Maximum-volume inscribed ellipsoid.** The unique John ellipsoid likewise must be of the form \(E(a,b)\) and centered at the origin. For its boundary write \(x=ay\), \(\|z\|=b\sqrt{1-y^2}\) with \(0\le y\le1\). The inclusion condition is exactly
\[
\max_{0\le y\le1}\bigl[c^2+b^2+2cay+(a^2-b^2)y^2\bigr]\le1. \tag{1}
\]
Let \(a=a_J\), \(b=b_J\) as in the statement. Then \(b^2-a^2=c a\sqrt d>0\), so the bracket is strictly concave, with its unique maximum at \(y=1/\sqrt d\). At this point it equals
\[
c^2+a^2+\frac{d+1}{\sqrt d}ca=1.
\]
Hence \(E(a_J,b_J)\subset L_c\), with contact orbit
\[
p_\pm(v)=\left(\pm\frac{a_J}{\sqrt d},\ b_J\sqrt{\frac{d-1}{d}}v\right),\quad v\in\mathbb S^{d-2}.
\]
Under the diagonal linear change of variables taking \(E(a_J,b_J)\) to \(B_2^d\), the contacts become \((\pm d^{-1/2},\sqrt{(d-1)/d}\,v)\). Give each sign equal probability and choose \(v\) uniformly on \(\mathbb S^{d-2}\). The contact distribution has mean zero and second moment \(I_d/d\). Multiplying its weights by \(d\) yields the John decomposition \(\int uu^{\mathsf T}d\mu(u)=I_d\), proving that the contained ellipsoid is the unique volume-maximizer. For \(d=2\), the transverse sphere is the two-point set \(\mathbb S^0\), and the same covariance computation applies.

**3. Centering and symmetrization of the affine sandwich.** Suppose an ellipsoid \(F=v+E(Q)\), with positive-definite squared-shape matrix \(Q\), obeys \(F\subset L_c\subset\lambda F\) for some homothetic containment centered at \(v\). By central symmetry, \(-F\subset L_c\subset\lambda(-F)\). The centered ellipsoid \(E(Q)\), the Minkowski midpoint of \(F\) and \(-F\), is contained in \(L_c\); the midpoint of the two containing ellipsoids contains \(L_c\) and is exactly \(\lambda E(Q)\). Thus it suffices to consider centered sandwiches. This also agrees with the standard centrally symmetric definition of the Banach–Mazur distance.

For a centered squared-shape matrix \(Q\), the constraint \(E(Q)\subset L_c\) can be written as \(u^{\mathsf T}Qu\le h_{L_c}(u)^2\) for every vector \(u\), which is *linear* in \(Q\). The constraint \(L_c\subset\lambda E(Q)\) is \(x^{\mathsf T}Q^{-1}x\le\lambda^2\) for every \(x\in L_c\), which is *convex* in \(Q\) on the positive-definite cone. Consequently averaging \(Q\) over the compact symmetry group of \(L_c\) preserves both inclusions. The averaged squared-shape matrix is diagonal with one axial and one transverse eigenvalue, so an optimal sandwich can be chosen to use a centered ellipsoid \(E(a,b)\).

**4. Exact optimal distortion.** For such a rotational ellipsoid, the outer containment \(L_c\subset\lambda E(a,b)\) implies, using the axial endpoints and equator, \(\lambda a\ge A\) and \(\lambda b\ge B\). Therefore \(\lambda^{-1}E(A,B)\subset E(a,b)\subset L_c\). Hence its distortion cannot be smaller than \(1/\tau_*\), where \(\tau_*\) is the largest positive homothety factor for which \(\tau_*E(A,B)\subset L_c\).

For \(0<t\le1\) the maximum of the left-hand side of the lens inequality over \(tE(A,B)\) is
\[
\max_{0\le y\le1}\left[c^2+t^2(1-c^2)+2cA(ty-t^2y^2)\right]. \tag{2}
\]
If \(t\ge1/2\), the quadratic maximizer is \(y=1/(2t)\), so (2) equals
\[
c^2+t^2(1-c^2)+\frac{cA}{2}.
\]
It is at most one exactly when \(t^2\le(2+c)/(2(1+c))\). The resulting \(\tau\in(\sqrt3/2,1)\) is greater than \(1/2\). Because scaling preserves inclusion in a convex body containing the origin, all smaller \(t\) are feasible. Thus \(\tau_*=\tau\). Taking \(F=\tau E(A,B)\) gives \(F\subset L_c\subset E(A,B)=\tau^{-1}F\), proving both matching bounds.

**5. Difference between John and distance ellipsoids.** Their inner tangency orbits occur respectively at normalized axial latitudes \(1/\sqrt d\) and \(1/(2\tau)\). If the ellipsoids coincided, the tangency latitudes would coincide, forcing \(d=4\tau^2=2(2+c)/(1+c)\in(3,4)\), impossible for an integer \(d\ge2\). Thus the two canonical ellipsoids differ. The distortion limit and strict increase follow by differentiating its exact elementary expression.

## Verification

The self-contained program `check_lens_geometry.py` checks the analytic parameter equations, the exact one-variable boundary maximizations, John contact covariances, and strict containment failure for perturbations above the optimal homothety. It uses only the Python standard library. It passes for 64 combinations of dimensions and separations, including \(d=2\) and \(d=101\). The mathematical conclusion rests on the proof above, not on finite tests. A reader can reproduce the numerical checks by running `python check_lens_geometry.py` next to this document.

## Relationship to prior work

John's contact decomposition and the uniqueness of minimum-volume containing ellipsoids are classical and *not new*. Todd's 2007 lecture notes explicitly state that the minimum-volume ellipsoid of an intersection of two balls can be derived using optimal-design methods; thus the outer ellipsoid alone is not claimed as an original contribution. Grundbacher and Kobos (first public arXiv version 16 February 2026, primary MSC2020 52A40) provide a general characterization of Banach–Mazur-optimal ellipsoid positions (their Theorems 1.2, 1.5 and Section 5); their inspected full text does not supply the present lens-specific sharp distance formula. The central claimed contribution is the exact dimension-free lens distance, its explicit optimizing sandwich, and its distinction from the dimension-dependent John ellipsoid. The survey by Bezdek, Lángi and Naszódi gives context for intersections of balls without determining this affine-distance invariant. Historical novelty requires the usual caution about literature not discoverable through indexing.

## Limitations

The calculation requires equal ball radii and two centers on a common axis. The sharp Banach–Mazur value does not imply a classification of all possibly non-rotational distance ellipsoids, nor does it extend to intersections of three or more balls. The endpoint \(c\uparrow1\) is only a limit of full-dimensional bodies. Classical John/Löwner theory and their uniqueness are used without independent reinvention. The historical priority of the exact lens distance is not independently certified.

## References

1. Florian Grundbacher and Tomasz Kobos, *John-type decompositions for affinely-optimal positions of convex bodies*, arXiv:2602.14847v1, publicly posted 16 February 2026, https://arxiv.org/html/2602.14847.
2. Mike Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, lecture slides, 6 July 2007, p. 14 (two-ball intersection mentioned explicitly), https://people.orie.cornell.edu/~miketodd/ublndetz.pdf.
3. Károly Bezdek, Zsolt Lángi and Márton Naszódi, *Selected topics from the theory of intersections of balls*, arXiv:2411.10302, https://arxiv.org/abs/2411.10302.
4. Fritz John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant*, Interscience (1948), 187–204.
