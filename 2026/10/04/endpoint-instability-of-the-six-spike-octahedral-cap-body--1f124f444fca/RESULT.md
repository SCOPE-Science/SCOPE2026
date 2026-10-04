# Endpoint instability of the six-spike octahedral cap body
## Finding
For \(1<r\le\sqrt2\), define
\[
K_r=\operatorname{conv}\left(\mathbb B^3\cup\{\pm r e_1,\pm r e_2,\pm r e_3\}\right)\subset\mathbb R^3,
\]
where \(\mathbb B^3\) is the Euclidean unit ball and \(e_1,e_2,e_3\) are the coordinate unit vectors. Then
\[
I(K_r)=
\begin{cases}
4,&1<r<\sqrt2,\\
6,&r=\sqrt2.
\end{cases}
\]
More explicitly, for every \(1<r<\sqrt2\), put \(c_r=\sqrt{1-r^{-2}}\), choose
\[
c_r<x<\frac1{\sqrt2},\qquad x\ne\frac1{\sqrt3},
\]
and put \(s=\sqrt{1-2x^2}\). The four unit directions
\[
u_1=(x,x,s),\quad
u_2=(-x,s,x),\quad
u_3=(s,-x,-x),\quad
u_4=\frac{(-1,-1,-1)}{\sqrt3}
\]
illuminate \(K_r\). Thus the six-direction regular-octahedral sharp example at \(r=\sqrt2\) is an endpoint phenomenon: every common inward radial perturbation of its six spikes drops the illumination number to the three-dimensional minimum.

## Assumptions and scope
The assertion concerns ordinary one-fold illumination by directions. The parameter range is exactly \(1<r\le\sqrt2\). In this range \(K_r\) is a cap body of the unit ball: opposite axial spike segments pass through the origin, while a segment joining two nonopposite axial spikes contains their midpoint of norm \(r/\sqrt2\le1\).

For an exterior point \(v\) of the unit ball, the standard cap-body vertex criterion says that a unit direction \(u\) illuminates \(v\) precisely when
\[
\langle v,u\rangle<-\sqrt{\lVert v\rVert^2-1}.
\]
For \(v=\sigma r e_i\), with \(\sigma\in\{-1,1\}\), this becomes
\[
\sigma u_i<-c_r,\qquad c_r=\sqrt{1-r^{-2}}.
\]
A finite family of directions illuminates the whole cap body once its positive hull is \(\mathbb R^3\) and every spike vertex is illuminated by at least one member of the family.

## Proof
Assume first that \(1<r<\sqrt2\). Then \(c_r<1/\sqrt2\), so an \(x\) satisfying the displayed conditions exists, and \(s>0\). Each of \(u_1,u_2,u_3,u_4\) has Euclidean norm one.

The six spike vertices are covered by strict coordinate inequalities. Namely, \(+r e_1\) is illuminated by \(u_2\), \(-r e_1\) by \(u_1\), \(+r e_2\) by \(u_3\), \(-r e_2\) by \(u_1\), \(+r e_3\) by \(u_3\), and \(-r e_3\) by \(u_2\). In every case the relevant signed coordinate equals \(-x<-c_r\).

The directions positively span \(\mathbb R^3\). Indeed,
\[
u_1+u_2+u_3+\sqrt3\,s\,u_4=0
\]
with all four coefficients positive. Moreover,
\[
\det\begin{pmatrix}
x&x&s\\
-x&s&x\\
s&-x&-x
\end{pmatrix}
=s(x^2-s^2)=s(3x^2-1)\ne0,
\]
so \(u_1,u_2,u_3\) span \(\mathbb R^3\). The positive dependence then implies that the positive hull of all four directions is all of \(\mathbb R^3\): express any vector in the basis \(u_1,u_2,u_3\) and add a sufficiently large positive multiple of the displayed zero relation. The cap-body illumination criterion therefore gives \(I(K_r)\le4\). Every three-dimensional convex body needs at least four illumination directions, because an illuminating family must positively span \(\mathbb R^3\); hence \(I(K_r)=4\).

Now let \(r=\sqrt2\). Then \(c_r=1/\sqrt2\). If one unit direction illuminated two distinct axial spike vertices, it would have two distinct coordinates with absolute value strictly larger than \(1/\sqrt2\), forcing the sum of their squares to exceed one. This is impossible; opposite spikes on a common axis also cannot be illuminated by the same direction. Hence each direction illuminates at most one of the six spikes, so \(I(K_{\sqrt2})\ge6\). Conversely, the six coordinate directions \(\{\pm e_1,\pm e_2,\pm e_3\}\) positively span \(\mathbb R^3\), and each spike is illuminated by its opposite coordinate direction. Therefore \(I(K_{\sqrt2})\le6\), proving equality.

## Verification
The proof is analytic and does not depend on finite enumeration. The accompanying checker replays the unit-length identities, the positive dependence, the determinant formula, the six strict spike inequalities for representative subcritical radii, and the endpoint square-sum obstruction. Those finite checks are consistency tests only; the quantified theorem follows from the inequalities and algebra in the proof.

## Relationship to prior work
Ivanov and Strachan introduced the relevant centrally symmetric cap-body framework in dimension three, proved the class bound \(I(K)\le6\), and showed sharpness. Their vertex criterion gives exactly the inequality used above for each axial spike. Later treatments of spiky balls and cap bodies restate the positive-hull plus spike-coverage criterion.

The known sharp octahedral example uses the six axial spikes whose spherical base caps have angular radius \(\pi/4\), which is exactly \(r=\sqrt2\). The inspected sources establish the endpoint value \(6\) and the class-wide upper bound, but they do not state the subcritical formula \(I(K_r)=4\) for every \(1<r<\sqrt2\), nor the explicit four-direction family above. The result therefore identifies the exact instability of that sharp example under its natural one-parameter radial deformation.

## Limitations
This is an exact statement only for the common-radius axial family \(K_r\) and only for ordinary illumination. It does not classify arbitrary centrally symmetric cap bodies, unequal axial radii, or multiple illumination numbers. The literature comparison cannot exclude an isolated unindexed observation under different terminology, although no covering statement appeared in the targeted searches or inspected primary sources.

## References
1. I. Ivanov and C. Strachan, *On the illumination of centrally symmetric cap bodies in small dimensions*, arXiv:2007.09765 (first public version 2020-07-19); published in *Journal of Geometry* 112 (2021). Primary MSC: 52A20.
2. K. Bezdek, I. Ivanov, and C. Strachan, *Illuminating spiky balls and cap bodies*, arXiv:2204.04561; *Discrete Mathematics* 346 (2023), 113135.
3. A. Arman, A. Kaire, and A. Prymak, *Illumination number of 3-dimensional cap bodies* (2026), for the class maximum and the regular-octahedral sharp example.
