# Tangency-chord linearization of the bicentric Poncelet family

Let \(ABCD\) be a convex bicentric quadrilateral. Its incircle has center \(I\) and radius \(r\), its circumradius is \(R\), and the incircle touches \(AB,BC,CD,DA\) at \(W,X,Y,Z\), respectively. Put
\[
k=|WY|,\qquad l=|XZ|,\qquad \Delta=\sqrt{4R^2+r^2}.
\]
The segments \(WY\) and \(XZ\) are the two tangency chords, equivalently the diagonals of the contact quadrilateral \(WXYZ\). In a bicentric quadrilateral they are perpendicular. The two outer diagonals and the two tangency chords are concurrent; denote their common point by \(P\).

The classical perpendicular-chord construction of bicentric quadrilaterals turns the fixed-\((r,R)\) Poncelet family into an elementary one-parameter problem on the incircle. Exploiting that construction gives the following exact profile.

## Theorem

For every convex bicentric quadrilateral as above,
\[
\boxed{IP^2=r^2\frac{\Delta-3r}{\Delta-r}}
\tag{1}
\]
and
\[
\boxed{k^2+l^2=4r^2\frac{\Delta+r}{\Delta-r}}
\tag{2}
\]
(the right side depends only on the two circle radii).

More precisely, for fixed admissible radii \(R\ge \sqrt2\,r\), the image of the complete bicentric Poncelet family under
\[
ABCD\longmapsto (k^2,l^2)
\]
is exactly the line segment
\[
\boxed{
 k^2+l^2=C,
 \qquad
 \frac{8r^3}{\Delta-r}\le k^2,l^2\le 4r^2,
 \qquad
 C=4r^2\frac{\Delta+r}{\Delta-r}.
}
\tag{3}
\]
For \(R=\sqrt2\,r\) this segment collapses to the square point \((4r^2,4r^2)\).

Consequently the circumradius can be recovered from the inradius and the two tangency-chord lengths by
\[
\boxed{R=\frac{2r^2\sqrt{k^2+l^2}}{k^2+l^2-4r^2}}.
\tag{4}
\]

If \(s\) and \(K\) are the semiperimeter and area of \(ABCD\), and \(K_c\) is the area of its contact quadrilateral, then
\[
\boxed{s=\frac{\Delta-r}{2r^2}kl},\qquad
\boxed{K=\frac{\Delta-r}{2r}kl},\qquad
\boxed{K_c=\frac12kl},
\tag{5}
\]
so in particular
\[
\boxed{\frac K{K_c}=\frac{\Delta-r}{r}}.
\tag{6}
\]
Thus the area ratio between a bicentric quadrilateral and its contact quadrilateral is constant along a fixed-circle Poncelet family.

Finally, the two classical Blundon--Eddy semiperimeter bounds admit the exact tangency-chord defect decompositions
\[
\boxed{
(\Delta+r)^2-s^2
=\frac{(\Delta-r)^2}{16r^4}(k^2-l^2)^2
}
\tag{7}
\]
and
\[
\boxed{
s^2-8r(\Delta-r)
=\frac{(\Delta-r)^2}{4r^4}(4r^2-k^2)(4r^2-l^2).
}
\tag{8}
\]
In particular,
\[
\sqrt{8r(\Delta-r)}\le s\le \Delta+r.
\]
For a non-square family, equality in the upper bound occurs exactly at the right-kite member (\(k=l\)); equality in the lower bound occurs exactly at the isosceles tangential-trapezoid members (one of \(k,l\) is an incircle diameter).

Equivalently, if
\[
\delta=\frac{|k^2-l^2|}{k^2+l^2},
\]
then
\[
\boxed{\frac{s}{\Delta+r}=\sqrt{1-\delta^2}},
\qquad
0\le \delta\le \frac{\Delta-3r}{\Delta+r},
\tag{9}
\]
and every value in this interval occurs.

## Proof

### 1. The fixed diagonal point

A standard theorem for tangential quadrilaterals says that the two outer diagonals and the two tangency chords are concurrent. Since a bicentric quadrilateral has perpendicular tangency chords, its contact diagonals are two perpendicular chords of the incircle through the outer diagonal point \(P\).

Write \(p=IP\). Rotate an orthogonal pair of chord lines through \(P\), and at their four endpoints draw tangents to the circle of radius \(r\). The intersections of adjacent tangents form a bicentric quadrilateral. The classical chord-tangent locus calculation (the construction used in treatments of Fuss' problem) gives the circumradius of the resulting quadrilateral as
\[
R^2=\frac{r^4(2r^2-p^2)}{(r^2-p^2)^2}.
\tag{10}
\]
For completeness, set \(u=p^2/r^2\). Equation (10) is
\[
\frac{R^2}{r^2}=\frac{2-u}{(1-u)^2}.
\]
Hence
\[
\frac{\Delta^2}{r^2}=1+4\frac{2-u}{(1-u)^2}
=\frac{(3-u)^2}{(1-u)^2}.
\]
Since \(0\le u<1\),
\[
\frac\Delta r=\frac{3-u}{1-u},
\]
which rearranges to (1).

### 2. The squared-chord line segment

Let one chord line make angle \(\alpha\) with \(IP\); its perpendicular companion then makes angle \(\alpha+\pi/2\). Their distances from \(I\) are \(p|\sin\alpha|\) and \(p|\cos\alpha|\), respectively. Therefore
\[
k^2=4\bigl(r^2-p^2\sin^2\alpha\bigr),
\qquad
l^2=4\bigl(r^2-p^2\cos^2\alpha\bigr).
\tag{11}
\]
Adding and using (1) gives
\[
k^2+l^2=8r^2-4p^2
=4r^2\frac{\Delta+r}{\Delta-r},
\]
which is (2).

As \(\alpha\) ranges through \([0,\pi/2]\), formula (11) traverses every point of a line segment. Its largest coordinate is \(4r^2\); its smallest coordinate is
\[
4(r^2-p^2)=\frac{8r^3}{\Delta-r}.
\]
This proves (3). Conversely, the classical chord-tangent locus construction shows that rotating this perpendicular chord pair generates the fixed-circle bicentric family, so no additional feasibility condition is missing.

Solving (2) for \(R\), with \(C=k^2+l^2\), gives
\[
\Delta=r\frac{C+4r^2}{C-4r^2},
\qquad
R^2=\frac{\Delta^2-r^2}{4}
=\frac{4r^4C}{(C-4r^2)^2},
\]
which yields (4).

### 3. Semiperimeter and area

A known formula for a bicentric quadrilateral with outer diagonals \(d_1,d_2\) and tangency chords \(k,l\) is
\[
K=\frac{kl\,d_1d_2}{k^2+l^2}.
\tag{12}
\]
A standard bicentric diagonal-product identity is
\[
d_1d_2=2r(\Delta+r).
\tag{13}
\]
Substituting (2) and (13) into (12) gives
\[
K=\frac{\Delta-r}{2r}kl.
\]
Since a tangential quadrilateral satisfies \(K=rs\), the first two formulas in (5) follow. The contact quadrilateral has perpendicular diagonals \(k,l\), hence \(K_c=kl/2\). This proves (5) and (6).

### 4. Exact Blundon--Eddy defects

Put \(u=k^2\), \(v=l^2\), and
\[
C=u+v=4r^2\frac{\Delta+r}{\Delta-r}.
\]
From (5),
\[
s^2=\frac{(\Delta-r)^2}{4r^4}uv.
\tag{14}
\]
Using \(4uv=C^2-(u-v)^2\) in (14) gives
\[
s^2=(\Delta+r)^2-
\frac{(\Delta-r)^2}{16r^4}(u-v)^2,
\]
which is (7).

For the lower defect note that
\[
C-4r^2=\frac{8r^3}{\Delta-r}.
\]
Therefore
\[
\begin{aligned}
s^2-8r(\Delta-r)
&=\frac{(\Delta-r)^2}{4r^4}
\left[uv-4r^2(C-4r^2)\right]\\
&=\frac{(\Delta-r)^2}{4r^4}(4r^2-u)(4r^2-v),
\end{aligned}
\]
which is (8).

Both factors in (8) are nonnegative because a chord of the incircle has length at most \(2r\). Equality in (8) means that one tangency chord is a diameter; the two tangents at its endpoints are parallel, so the outer bicentric quadrilateral is a cyclic tangential trapezoid, hence an isosceles tangential trapezoid. Equality in (7) means \(k=l\); the standard tangential-quadrilateral characterization then gives a kite, and a cyclic kite is a right kite.

Finally, divide (7) by \((\Delta+r)^2\) and use (2) to get the first identity in (9). The endpoint of (3) gives the stated sharp range of \(\delta\), completing the proof.

## Relation to prior literature and originality boundary

The perpendicularity of the two tangency chords, the construction of bicentric quadrilaterals from perpendicular chords of the incircle, and the associated chord-tangent locus are classical. Stastna's 2005 exposition of Fuss' problem explicitly develops this construction and the locus argument, following older treatments including Dorrie's 1965 presentation. These ingredients are not claimed as new.

Josefsson (2010, restated in his 2011 area paper) developed formulas for tangency chords of tangential quadrilaterals; the 2011 paper records the bicentric area identity (12). Bencze and Dragan (2021) proved the Blundon--Eddy bounds and obtained exact factorizations of their deficits in terms of side differences. Dragan and Bencze (2023) derived further formulas involving tangent lengths and the sides of the contact quadrilateral, including its orthodiagonality and radius-dependent products. Josefsson (2023) treats the diagonal point and other collinearities in bicentric quadrilaterals.

Searches for the exact formulas above and for synonymous formulations in terms of contact diagonals, tangency chords, orthogonal incircle chords, bicentric Poncelet families, and Blundon--Eddy defects did not locate a source stating (2)--(9), in particular the full line-segment image (3), the radius recovery (4), the fixed area ratio (6), or the two contact-diagonal defect factorizations (7)--(8). Accordingly, originality is claimed only to the best of our knowledge. The main residual risk is older chord-tangent and bicentric-quadrilateral literature in which these short consequences may appear under different notation; Dorrie's full 1965 section, Scherrer's 1933 bicentric-quadrilateral paper, and the full text of Tran Quang Hung's 2024 generalisation of Fuss' theorem were not directly inspected here.

## Limitations

- Only convex Euclidean bicentric quadrilaterals are treated.
- The line-segment statement describes the image in the two squared tangency-chord coordinates; it is not asserted to be a one-to-one parametrization of labeled quadrilaterals.
- The result does not claim a corresponding profile for general tangential quadrilaterals, ex-bicentric quadrilaterals, or higher Poncelet polygons.
- The originality assessment is necessarily to the best of our knowledge; some older sources most plausibly capable of containing equivalent formulas were not fully inspected.

## Verification artifact

`artifacts/verify_identities.py` uses SymPy 1.14.0 to check the algebraic identities (2), (4), (7), and (8), and numerically constructs tangent quadrilaterals from rotating perpendicular chord pairs for representative values of \(IP/r\). The computation is supplementary; the proof above is exact and does not depend on numerical evidence.

## References

1. B. Stastna, *Fuss' Problem of the Chord-Tangent Quadrilateral* (2005), workshop presentation. https://math.fce.vutbr.cz/~pribyl/workshop_2005/prispevky/StastnaPr.pdf
2. J. C. Salazar, *Fuss' theorem*, The Mathematical Gazette 90 (2006), 306--307. https://doi.org/10.1017/S002555720017980X
3. M. Josefsson, *Calculations concerning the tangent lengths and tangency chords of a tangential quadrilateral*, Forum Geometricorum 10 (2010), 119--130.
4. M. Josefsson, *The Area of a Bicentric Quadrilateral*, Forum Geometricorum 11 (2011), 155--164. https://studyres.com/doc/14608666/the-area-of-a-bicentric-quadrilateral
5. M. Bencze and M. Dragan, *A new proof of the Blundon-Eddy inequality and some applications*, Arhimede Mathematical Journal 8(2) (2021), 158--167. https://amj-math.com/wp-content/uploads/2022/01/AMJ2021-vol8iss2.pdf
6. M. Dragan and M. Bencze, *Some relations between the tangent lengths of a bicentric quadrilateral*, Arhimede Mathematical Journal 10(1) (2023), 13--27. https://amj-math.com/wp-content/uploads/2023/07/AMJ2023-vol10iss1.pdf
7. M. Josefsson, *Fifteen collinear points in bicentric quadrilaterals*, International Journal of Geometry 12(4) (2023), 13--27. https://ijgeometry.com/wp-content/uploads/2023/09/2.-13-27.pdf
8. T. Q. Hung, *A generalisation of Fuss' theorem*, The Mathematical Gazette 108 (2024), 532--536. https://doi.org/10.1017/mag.2024.130
