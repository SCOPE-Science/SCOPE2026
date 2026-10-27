# The characteristic-two Fricke cubic has a split \(D_4\) resolution and an exact zeta function

## Finding
Let \(\mathcal X\subset\mathbb P^3_{\mathbb Z}\) be defined by
\[
W(X_0^2+X_1^2+X_2^2)-X_0X_1X_2-4W^3=0.
\]
Its characteristic-two fibre \(X=\mathcal X\otimes\mathbb F_2\) is geometrically integral and normal, with a unique geometric singular point \(O=[0:0:0:1]\). Its local Jacobian (equivalently Tjurina) algebra has length \(6\). The minimal desingularization \(\pi:Y\to X\) has a split \(D_4\) exceptional divisor: four smooth rational \((-2)\)-curves meeting as a three-legged star. For every integer \(r\ge1\), with \(q=2^r\),
\[
\#X(\mathbb F_q)=q^2+3q+1,\qquad
\#Y(\mathbb F_q)=q^2+7q+1,
\]
so that
\[
Z(Y/\mathbb F_2,T)=\frac{1}{(1-T)(1-2T)^7(1-4T)}.
\]
The standard characteristic-zero Fricke cubic has four ordinary nodes; the displayed integral model instead has a single wild singularity in characteristic two.

## Assumptions and scope
The statement concerns exactly the displayed integral equation and its special fibre over \(\mathbb F_2\). All geometric singularity assertions are over an algebraic closure of \(\mathbb F_2\); the exceptional curves and their intersections are already defined over \(\mathbb F_2\). The term split \(D_4\) describes the exceptional intersection diagram and does not require choosing an Artin characteristic-two subtype. The zeta function is the Hasse–Weil zeta function of the **minimal resolution** over \(\mathbb F_2\), not a claim about another integral model.

## Proof
**1. Integrality, normality and singular scheme.** In characteristic two put \(x=X_0,y=X_1,z=X_2,w=W\). The defining polynomial is
\[
f=w(x+y+z)^2+xyz.
\]
It is primitive and linear as a polynomial in \(w\): the coprime coefficients \((x+y+z)^2\) and \(xyz\) rule out a nonconstant factor over any extension of the base field. Thus the surface is geometrically integral. Its homogeneous derivatives are \(yz,xz,xy,(x+y+z)^2\); their common vanishing on the surface forces \(x=y=z=0\), hence the unique singular point \(O\). A hypersurface is Cohen–Macaulay, and an isolated singularity on a surface has codimension two, so Serre's criterion gives normality.

In \(w=1\), the local Jacobian quotient is
\[
A=k[x,y,z]_{(x,y,z)}/(xy,xz,yz,x^2+y^2+z^2).
\]
The equation \(f\) itself belongs to this derivative ideal; this is also the Tjurina quotient. A Gröbner reduction (or direct multiplication reduction) gives the basis \(1,x,y,z,y^2,z^2\). In particular \(\dim_k A=6\). This length does not assert a Milnor number in characteristic two.

**2. Explicit blowup and the exceptional diagram.** Set \(s=x+y+z\) in the affine chart \(w=1\). Then
\[
f=s^2+xy(s+x+y).
\]
Blow up the origin. In the chart \(y=xt,\ s=xr\), the strict-transform equation after dividing by \(x^2\) is
\[
g=r^2+xt(r+1+t)=0.
\]
The reduced exceptional component is \(E_0=V(x,r)\), parametrized by \(t\). The Jacobian derivatives of \(g\) show precisely two singularities on this chart, at \(t=0\) and \(t=1\). The symmetric \(y\)-chart supplies the third singularity, at \(t=\infty\). No other singularities occur, since the blowup is an isomorphism away from \(O\). At \(t=0\), \(g=r^2+x't\) with \(x'=x(1+r+t)\) a local coordinate. At \(t=1\), writing \(u=t+1\), the same equation becomes \(r^2+x'v\) where \(x'=xt\) and \(v=r+u\). The third point is equivalent by swapping \(x,y\). Each is an ordinary \(A_1\) rational double point \(UV+R^2=0\), resolved by one blowup, with smooth split exceptional conic \(UV+R^2=0\subset\mathbb P^2\). The strict transform of the reduced \(E_0\) meets each new exceptional curve once, transversely, and the three new curves are disjoint. Every component is \(\mathbb P^1\) over \(\mathbb F_2\).

The total resulting resolution is crepant: the first blowup of a multiplicity-two Gorenstein hypersurface surface point has discrepancy zero, and the three ordinary nodes have crepant resolutions. Adjunction therefore gives self-intersection \(-2\) for every exceptional rational curve. The intersection matrix is the negative \(D_4\) Cartan matrix, so no exceptional \((-1)\)-curve remains, proving minimality. This also avoids identifying the specific wild \(D_4\) subtype from a characteristic-zero normal form.

**3. Point counts.** Write \(q=2^r\). The plane at infinity \(w=0\) is the union of the three coordinate lines \(xyz=0\) in \(\mathbb P^2\), with exactly \(3q\) rational points. In \(w=1\), solve
\[
z^2+xyz+x^2+y^2=0.
\]
If \(xy=0\), the square map is bijective and there is one solution for each of \(2q-1\) ordered pairs \((x,y)\). If \(xy\ne0\), dividing after putting \(u=z/(xy)\) gives
\[
u^2+u=x^{-2}+y^{-2}.
\]
There are two solutions exactly when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(x^{-1}+y^{-1})=0\). Among nonzero field elements, \(q/2-1\) have inverse of absolute trace zero, and \(q/2\) have inverse of trace one. The number of qualifying ordered pairs is therefore \((q/2-1)^2+(q/2)^2\). Counting the two roots for each qualifying pair gives
\[
(2q-1)+2\bigl((q/2-1)^2+(q/2)^2\bigr)=q^2+1
\]
affine points and consequently \(q^2+3q+1\) projective points.

Replacing the rational singular point by four split rational projective lines with three rational transverse intersection points adds
\[
4(q+1)-3-1=4q
\]
points. Thus \(\#Y(\mathbb F_q)=q^2+7q+1\). Finally \(\exp(\sum_{r\ge1}\#Y(\mathbb F_{2^r})T^r/r)\) is the announced zeta function.

## Verification
An independent exact finite-field enumerator in `checker.py` verifies the affine/projective point counts for \(q=2,4,8,16\), the characteristic-two Jacobian equations and the length-six local quotient. It also checks the displayed blowup identity and its two finite exceptional singular locations. These finite checks corroborate, but do not substitute for, the arbitrary-\(r\) trace-count argument or the geometric blowup proof.

## Relationship to prior work
Cantat–Loray, *Holomorphic dynamics, Painlevé VI equation and Character Varieties* (arXiv:0711.1579, original public posting 2007-11-10), discuss the characteristic-zero Fricke/Cayley cubic and its four nodes and torus quotient. Goldman, *Trace Coordinates on Fricke spaces of some simple hyperbolic surfaces* (arXiv:0901.1404, original public posting 2009-01-11), develops the classical trace-coordinate identity. Those complex-geometric statements supply the natural arithmetic model but do not assert the displayed wild special-fibre resolution or its exact zeta function. The present result is restricted to the precise reduction, the Jacobian length, split \(D_4\) resolution and arithmetic count. Other descriptions of quotients in characteristic two may imply portions of the result; exhaustive historical priority is not asserted.

## Limitations
The construction makes no claim about arbitrary alternative integral models, moduli interpretations at the bad prime, Artin's finer characteristic-two \(D_4\) subclass, or a complete classification of all characteristic-two cubic surfaces. Historical coverage may exist under equivalent quotient presentations. The finite checker uses small fields only; universal point counts follow from the written proof. Independent external mathematical validation has not occurred.

## References
1. S. Cantat and F. Loray, *Holomorphic dynamics, Painlevé VI equation and Character Varieties*, arXiv:0711.1579 (first posted 2007-11-10), https://arxiv.org/abs/0711.1579.
2. W. M. Goldman, *Trace Coordinates on Fricke spaces of some simple hyperbolic surfaces*, arXiv:0901.1404 (first posted 2009-01-11), https://arxiv.org/abs/0901.1404.
