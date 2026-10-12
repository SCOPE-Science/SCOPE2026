# The Drell–Yan Nikulin involution has a four-plus-four fixed-point split
## Finding
Let \(S\) be the Drell–Yan K3 surface and consider the genus-one fibration of Besier–Festi–Harrison–Naskręcki, Proposition 4.13, with quartic fiber model
\[
t y^2=F_t(x).
\]
Their Remark 4.14 gives a Nikulin involution \(\iota\) by
\[
t\longmapsto t^{-1},\qquad x\longmapsto\alpha x+\beta,
\qquad y\longmapsto-\gamma y,
\]
where
\[
\alpha=t^{-2}\frac{t+e}{et+1},\qquad
\beta=\frac{3035-1302\sqrt5}{38}\,
\frac{(t-1)(t^2+ft+1)}{t^2(et+1)},\qquad
\gamma=t\alpha^2,
\]
with \(e=(138+67\sqrt5)/19\) and \(f=(2770+1324\sqrt5)/355\).

The eight fixed points of \(\iota\) lie exactly on the two smooth fibers \(t=1\) and \(t=-1\), four on each.

On \(t=1\), one has \(\alpha=1\), \(\beta=0\), \(\gamma=1\), so \(\iota(x,y)=(x,-y)\). Its fixed points are the four finite points with \(y=0\), where
\[
F_1(x)=
\bigl(x^2+(66-24\sqrt5)x-1803+820\sqrt5\bigr)
\bigl(x^2+(134-60\sqrt5)x+10101-4520\sqrt5\bigr).
\]
Both quadratic factors are separable and coprime.

On \(t=-1\),
\[
\alpha=-1,\qquad \beta=-248+108\sqrt5,\qquad \gamma=-1,
\]
so \(\iota(x,y)=(-x-248+108\sqrt5,y)\). The two affine fixed points are
\[
x=-124+54\sqrt5,
\qquad
y^2=3567475528-1595423560\sqrt5.
\]
The compactified quartic fiber sits in \(\mathbf P(1,2,1)_{[X:Y:Z]}\). At \(t=-1\) its two points at infinity are
\[
[1:i:0],\qquad[1:-i:0],
\]
and each is fixed because \([X:Y:0]\mapsto[-X:Y:0]\), which is the same weighted-projective point under scaling by \(-1\). These give the other two fixed points on that fiber.

Thus the fixed locus has the exact split \(4+4\). For the quotient-base coordinate \(s=t+t^{-1}-2\), the two fixed fibers map to \(s=0\) and \(s=-4\). Consequently the eight ordinary double points of the singular Nikulin quotient occur four over each of those two base values.

## Assumptions and scope
All fixed-point statements are over \(\mathbf C\); the formulas are written over \(\mathbf Q(\sqrt5)\) and its algebraic closure. The quartic model is compactified in the standard weighted projective plane \(\mathbf P(1,2,1)\). The claim concerns the explicit Nikulin involution in Remark 4.14, not every automorphism or every elliptic/genus-one fibration of the surface.

## Proof
A fixed point must lie over a fixed point of the base involution \(t\mapsto1/t\). Hence \(t=1\) or \(t=-1\). The bad-fiber polynomial printed in Proposition 4.13 is nonzero at both values, so these fibers are smooth.

Substitution into the explicit formulas for \(\alpha,\beta,\gamma\) gives the two fiber actions above. At \(t=1\), fixed affine points satisfy \(y=0\). Substituting \(t=1\) in the source quartic gives the displayed factorization of \(F_1\); exact discriminants and the resultant are nonzero, so it contributes four distinct fixed points. The two points at infinity are exchanged by \(Y\mapsto-Y\), so there are no further fixed points on this fiber.

At \(t=-1\), the affine fixed equation is \(x=(-x-248+108\sqrt5)\), giving \(x=-124+54\sqrt5\). Substitution in the quartic gives the displayed nonzero value of \(y^2\), hence two affine fixed points. The two weighted-projective points at infinity satisfy \(-Y^2=X^4\), so they are \([1:\pm i:0]\), and each is fixed as explained above. Thus this fiber also contributes four points.

No other fibers can contain fixed points because the base coordinate would move. The resulting total of eight agrees with the general Nikulin fixed-point theorem and therefore exhausts the fixed locus.

## Verification
The included `verify.py` transcribes the quartic of Proposition 4.13 exactly over \(\mathbf Q(\sqrt5)\). It verifies smoothness of the fibers \(t=\pm1\) from the source bad-fiber polynomial, the specializations of \(\alpha,\beta,\gamma\), the factorization and separability of \(F_1\), and the affine fixed-point equation and \(y^2\)-value at \(t=-1\).

## Relationship to prior work
The source gives the complete quartic fiber equation and the explicit Nikulin involution, and recalls the general fact that a Nikulin involution has eight isolated fixed points. It does not locate those eight points in its genus-one fibration. The calculation here identifies their exact distribution and coordinates and, equivalently, localizes the eight quotient nodes over the two special quotient-base values. Published-literature searches for the exact source, involution formula, fixed-fiber formulation, and eight-point localization found no covering statement.

A previously known localization for a different canonical K3 family places six fixed points on a genus-two curve and two on an ADE resolution component. That mechanism does not apply here: the present involution exchanges the two \(II^*\) fibers and its fixed locus is instead controlled by the two fixed values of the base inversion.

## Limitations
The square roots of the four \(t=1\) roots and of the two \(t=-1\) affine \(y\)-coordinates are not expanded into radicals because the polynomial equations already determine the points exactly. The claim does not determine the full automorphism group or the complete singular-fiber structure of the quotient fibration.

## References
1. M. Besier, D. Festi, M. Harrison, B. Naskręcki, *Arithmetic and geometry of a K3 surface emerging from virtual corrections to Drell–Yan scattering*, arXiv:1908.01079; DOI:10.4310/CNTP.2020.v14.n4.a4.
