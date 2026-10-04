# Exact remainder and global quadratic stability for Fagnano's theorem

## Finding
Let \(ABC\) be an acute Euclidean triangle with side lengths \(a=BC\), \(b=CA\), \(c=AB\), area \(\Delta\), and angles \(A,B,C\). Choose \(X\in BC\), \(Y\in CA\), \(Z\in AB\), and put \(x=BX\), \(y=CY\), \(z=AZ\). Define
\[
egin{aligned}
u&=x\cos A+(c-z)\cos C,& p&=x\sin A-(c-z)\sin C,\
v&=y\cos B+(a-x)\cos A,& q&=y\sin B-(a-x)\sin A,\
w&=z\cos C+(b-y)\cos B,& r&=z\sin C-(b-y)\sin B.
\end{aligned}
\]
Then
\[
XY=\sqrt{v^2+q^2},\qquad YZ=\sqrt{w^2+r^2},\qquad ZX=\sqrt{u^2+p^2},
\]
and the perimeter excess over the Fagnano minimum has the exact decomposition
\[
P(XYZ)-rac{8\Delta^2}{abc}
=igl(\sqrt{u^2+p^2}-uigr)+igl(\sqrt{v^2+q^2}-vigr)+igl(\sqrt{w^2+r^2}-wigr).
\]
Each summand is nonnegative. Thus this is an exact remainder formula, not only an inequality.

Let \(D=\max\{a,b,c\}\) and let
\[
x_0=c\cos B,\qquad y_0=a\cos C,\qquad z_0=b\cos A,
\]
which are the side coordinates of the altitude feet. The exact remainder yields
\[
P(XYZ)-rac{8\Delta^2}{abc}\ge rac{p^2+q^2+r^2}{2D}
\ge rac{\sin^2A\,(x-x_0)^2+\sin^2B\,(y-y_0)^2+\sin^2C\,(z-z_0)^2}{2D}.
\]
Hence Fagnano's theorem admits a global quadratic stability estimate in the natural side coordinates.

## Assumptions and scope
The ambient geometry is Euclidean and \(ABC\) is acute. The points \(X,Y,Z\) may lie anywhere on the three closed sides, including endpoints. The result concerns the ordinary perimeter \(P(XYZ)=XY+YZ+ZX\). The factor \(D\) is the diameter of \(ABC\), which for a triangle equals its longest side. No claim is made that the coefficient \(1/(2D)\) in the stability corollary is sharp.

## Proof
The cosine rule gives, for \(ZX\),
\[
ZX^2=x^2+(c-z)^2-2x(c-z)\cos B.
\]
Since \(B=\pi-(A+C)\), expanding the two squares shows
\[
ZX^2=igl(x\cos A+(c-z)\cos Cigr)^2+igl(x\sin A-(c-z)\sin Cigr)^2=u^2+p^2.
\]
The same calculation on the other two vertex angles gives \(XY^2=v^2+q^2\) and \(YZ^2=w^2+r^2\).

The linear parts telescope:
\[
u+v+w=a\cos A+b\cos B+c\cos C.
\]
Using the cosine rule and Heron's identity,
\[
a\cos A+b\cos B+c\cos C
=rac{2a^2b^2+2b^2c^2+2c^2a^2-a^4-b^4-c^4}{2abc}
=rac{8\Delta^2}{abc}.
\]
Therefore
\[
P(XYZ)-rac{8\Delta^2}{abc}
=\sum_{(s,t)\in\{(u,p),(v,q),(w,r)\}}igl(\sqrt{s^2+t^2}-sigr),
\]
which is the asserted exact decomposition. Each term is nonnegative because \(\sqrt{s^2+t^2}\ge s\).

If the total remainder vanishes, then each summand vanishes. Hence \(p=q=r=0\) and the corresponding linear component is nonnegative. The equations \(p=q=r=0\) are equivalent, by the sine rule, to
\[
ax+cz=c^2,\qquad ax+by=a^2,\qquad by+cz=b^2.
\]
Their unique solution is
\[
x=c\cos B,\qquad y=a\cos C,\qquad z=b\cos A.
\]
Because \(ABC\) is acute, these are interior side coordinates and describe the three altitude feet. Conversely, at those coordinates \(p=q=r=0\) and the three linear components are positive, so equality holds. Thus the orthic triangle is the unique equality case.

For stability, write \(L=\sqrt{s^2+t^2}\). If \(L+s>0\), then
\[
L-s=rac{t^2}{L+s}\ge rac{t^2}{2L}.
\]
If \(L+s=0\), then \(t=0\) and the same lower bound is trivial. Each of \(XY,YZ,ZX\) is at most the diameter \(D\), so summing gives
\[
P(XYZ)-rac{8\Delta^2}{abc}\ge rac{p^2+q^2+r^2}{2D}.
\]
Now set
\[
U=\sin A\,(x-x_0),\quad V=\sin B\,(y-y_0),\quad W=\sin C\,(z-z_0).
\]
Since the orthic coordinates annihilate \(p,q,r\), one has
\[
p=U+W,\qquad q=U+V,\qquad r=V+W.
\]
Consequently
\[
p^2+q^2+r^2=(U+V+W)^2+U^2+V^2+W^2\ge U^2+V^2+W^2,
\]
which proves the second stability inequality.

## Verification
The bundled `verify_fagnano_defect.py` evaluates the exact identity and both stability inequalities on deterministic grids for several acute triangles and on 5000 seeded random acute triangles. It separately checks that the orthic coordinates give zero deficit. The worst numerical discrepancy in the exact identity was \(6.661	imes10^{-15}\). These finite checks only guard against algebraic or transcription mistakes; the universal result is proved above.

## Relationship to prior work
Fagnano's theorem is classical: the orthic triangle uniquely minimizes perimeter among triangles inscribed in an acute triangle. Holland's 2007 trigonometric verification writes each side length as the square root of a sum of two squares of exactly the linear forms used here and then discards the transverse squares to prove the lower bound. The present statement keeps those discarded components and records the full perimeter deficit as an exact sum of three nonnegative terms, then derives a global quadratic displacement bound. The inspected Holland article does not state either the exact remainder formula or the stability inequality.

Alkoumi and Schlenk use the uniqueness and minimality of the Fagnano triangle in their 2014 work on shortest closed billiard orbits. Their inspected arXiv text treats the optimizer as a qualitative ingredient and does not give a quantitative perimeter remainder. Thus the stability statement is compatible with, but not contained in, the inspected billiard formulation.

## Limitations
The historical search cannot exclude an equivalent remainder identity in older books, olympiad notes, or papers indexed under different terminology. The closest inspected proof already contains the algebraic ingredients, so the originality claim is specifically for the explicit exact remainder and its global quadratic corollary, not for Fagnano minimality or for the side-length decompositions themselves. The displayed quadratic coefficient is explicit and global but is not asserted to be optimal.

## References
1. Finbarr Holland, "Another Verification of Fagnano's Theorem," *Forum Geometricorum* 7 (2007), 207--210. Publication date recorded as 2007-12-05 in the inspected full-text index.
2. Naeem Alkoumi and Felix Schlenk, "Shortest closed billiard orbits on convex tables," arXiv:1408.5255v1, first posted 2014-08-22; later *manuscripta mathematica* 147 (2015), 365--380, DOI 10.1007/s00229-014-0724-4.
3. H. S. M. Coxeter and S. L. Greitzer, *Geometry Revisited*, Mathematical Association of America, 1967, Section 4.5.
