# Exact Fraenkel asymmetry of regular polygons

## Finding

Let \(P_n\) be a regular Euclidean \(n\)-gon, \(n\ge3\). Its Fraenkel asymmetry is
\[
\mathcal A_F(P_n)
=
\inf_{x\in\mathbb R^2}
\frac{|P_n\mathbin{\triangle}(x+B_s)|}{|P_n|},
\]
where \(B_s\) is a Euclidean disk with \(\pi s^2=|P_n|\).

Put
\[
t=\frac{\pi}{n},\qquad
q_n=\sqrt{\frac{\sin(2t)}{2t}},\qquad
\beta_n=\arccos\!\left(\frac{\cos t}{q_n}\right).
\]
Then \(0<\beta_n<t\), the centered equal-area disk is optimal, and
\[
\boxed{
\mathcal A_F(P_n)
=
\frac{2n}{\pi}
\left(\beta_n-\sin\beta_n\cos\beta_n\right)
}.
\]

As \(n\to\infty\),
\[
\mathcal A_F(P_n)
=
\frac{4\pi^2}{9\sqrt3}\frac1{n^2}
+O\!\left(\frac1{n^4}\right).
\]
For the unit-area regular polygons \(S_n\),
\[
P(S_n)-2\sqrt\pi
=
\frac{\pi^{5/2}}{3}\frac1{n^2}
+O\!\left(\frac1{n^4}\right),
\]
so the constant appearing without a value in the published asymptotic relation
\[
P(S_n)-P(B)\sim\mu_2\mathcal A_F(S_n)
\]
is
\[
\boxed{\mu_2=\frac{3\sqrt{3\pi}}4}.
\]

## Assumptions and scope

The polygon is a filled planar regular polygon, and the comparison disks in the Fraenkel asymmetry have the same area as the polygon but may be translated arbitrarily. The formula is invariant under similarities, so the circumradius can be normalized in the proof.

The motivating literature uses regular polygons to calibrate quantitative isoperimetric and spectral inequalities. Ftouhi and Lamboley state the proportional asymptotic relation above with an unspecified positive constant. Paoli later verifies the same order of magnitude for regular polygons in a sharpness argument for a reverse quantitative inequality. The result here supplies the full finite-\(n\) profile and the exact limiting proportionality constant.

## Proof

Normalize the circumradius of \(P_n\) to \(R=1\). Its inradius is
\[
r=\cos t,
\]
and its area is
\[
|P_n|=\frac n2\sin(2t).
\]
Hence the equal-area disk has radius
\[
s=q_n=\sqrt{\frac{\sin(2t)}{2t}}.
\]
Since \(\sin(2t)<2t\), one has \(s<1\). Also
\[
s^2-r^2
=
\cos t\left(\frac{\sin t}{t}-\cos t\right)>0
\]
because \(\tan t>t\) for \(0<t<\pi/2\). Thus
\[
r<s<1.
\]
Consequently \(\beta=\arccos(r/s)\) lies in \((0,t)\).

It remains first to prove that translating the equal-area disk cannot improve the overlap. For a disk center \(x\), write
\[
K_x=P_n\cap(x+B_s)
\]
and let \(\rho\) be rotation by \(2\pi/n\) about the polygon center. Rotational invariance gives
\[
|K_{\rho^j x}|=|K_x|.
\]
Moreover,
\[
\frac1n\sum_{j=0}^{n-1}K_{\rho^j x}
\subseteq
P_n\cap B_s=K_0.
\]
Indeed, convexity keeps the Minkowski average inside \(P_n\), while the disk components average into \(B_s\); the orbit average of the centers is zero. The planar Brunn--Minkowski inequality therefore yields
\[
|K_0|^{1/2}
\ge
\frac1n\sum_{j=0}^{n-1}|K_{\rho^j x}|^{1/2}
=|K_x|^{1/2}.
\]
Thus the centered equal-area disk maximizes intersection area and hence minimizes symmetric difference.

Because \(s<1\), the portions of the centered disk lying beyond distinct side-supporting lines do not overlap: the nearest intersection of two adjacent exterior side half-planes occurs at a polygon vertex, at distance \(1\) from the center. Each of the \(n\) excluded circular caps has area
\[
C=s^2\left(\beta-\sin\beta\cos\beta\right).
\]
Therefore
\[
|P_n\cap B_s|=\pi s^2-nC.
\]
The two sets have equal area, so
\[
|P_n\mathbin{\triangle}B_s|
=2nC.
\]
Dividing by \(|P_n|=\pi s^2\) proves the exact formula.

For the asymptotics,
\[
q_n^2
=
1-\frac23t^2+O(t^4),
\qquad
\frac{\cos t}{q_n}
=
1-\frac16t^2+O(t^4),
\]
whence
\[
\beta_n=\frac{t}{\sqrt3}+O(t^3).
\]
Since
\[
\beta-\sin\beta\cos\beta
=
\frac23\beta^3+O(\beta^5),
\]
substitution with \(t=\pi/n\) gives
\[
\mathcal A_F(P_n)
=
\frac{4\pi^2}{9\sqrt3}n^{-2}+O(n^{-4}).
\]
For a unit-area regular \(n\)-gon,
\[
P(S_n)=2\sqrt{n\tan(\pi/n)},
\]
and Taylor expansion gives the displayed perimeter deficit. Taking the ratio gives
\[
\mu_2=\frac{3\sqrt{3\pi}}4.
\]

## Verification

The proof is exact and does not depend on numerical enumeration. The accompanying `verify.py` independently integrates the radial function of the centered polygon--disk intersection for several values of \(n\), compares those areas to the closed formula, and checks the two asymptotic constants at large finite \(n\). It prints

`VERIFY_OK regular polygon Fraenkel asymmetry`

The numerical integration is only a replay check. The all-\(n\) result follows from the rotational Brunn--Minkowski centering argument and the exact circular-cap computation.

## Relationship to prior work

Ftouhi and Lamboley use unit-area regular polygons in their study of the planar Blaschke--Santaló diagram. In Remark 4.1 they state, after “straightforward computations,” that
\[
P(S_n)-P(B)\sim\mu_2\mathcal A_F(S_n)
\]
for a positive constant \(\mu_2\), but do not give its value or a finite-\(n\) expression for \(\mathcal A_F(S_n)\).

Paoli defines the Fraenkel asymmetry through translated equal-area balls and, in Remark 3.2, computes the regular-polygon sharpness scale \(\mathcal A_F(S_n)\asymp n^{-2}\). That discussion is asymptotic and does not establish the finite-\(n\) formula above or the global optimality of the centered comparison disk by a translation argument.

Alvino, Ferone, and Nitsch solve a different extremal problem: among convex planar sets with a prescribed Fraenkel asymmetry, they determine the smallest isoperimetric deficit and characterize the extremizing family. Their result does not determine the Fraenkel asymmetry of a prescribed regular polygon.

Targeted searches for exact regular-polygon Fraenkel asymmetry, equal-area disk symmetric difference, centered-disk formulas, and equivalent \(L^1\)-asymmetry terminology did not locate the stated profile.

## Limitations

The theorem concerns regular polygons and equal-area Euclidean disks. It does not classify all translating disks that may tie the centered one, nor does it treat arbitrary cyclic or equiangular polygons. The literature search was targeted rather than exhaustive, and an older elementary overlap computation under different terminology remains a residual originality risk.

## References

I. Ftouhi and J. Lamboley, “Blaschke--Santaló Diagram for Volume, Perimeter, and First Dirichlet Eigenvalue,” SIAM Journal on Mathematical Analysis 53 (2021), 1670--1710, DOI 10.1137/20M1345396.

G. Paoli, “A reverse quantitative isoperimetric type inequality for the Dirichlet Laplacian,” arXiv:2105.03243, first submitted 2021-05-07.

A. Alvino, V. Ferone, and C. Nitsch, “A sharp isoperimetric inequality in the plane,” Journal of the European Mathematical Society 13 (2011), 185--206, DOI 10.4171/JEMS/248.
