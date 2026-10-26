# The \(3\)-rank jump and elliptic quotient in a characteristic-three cyclic Klein quartic pencil

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). Consider the cyclic plane quartic pencil
\[
C_\lambda:\quad X^3Y+Y^3Z+Z^3X+\lambda XYZ(X+Y+Z)=0,
\qquad \lambda\in k.
\]
It is nonsingular exactly for \(\lambda\notin\{1,-1\}\). On each smooth member the cyclic coordinate permutation defines a wild degree-three cover of the elliptic curve
\[
E_\lambda:\quad (1+\lambda)d^2+d+(1+\lambda)r^3-\lambda r^2+r=0.
\]
Its elliptic \(j\)-invariant, and the complete \(3\)-rank classification, are
\[
\boxed{j(E_\lambda)=\frac{\lambda^6}{\lambda^2-1}},\qquad
\boxed{f_3(C_\lambda)=\begin{cases}0&\lambda=0,\\3&\lambda\ne0,\pm1.\end{cases}}
\]
The affine Galois equation is \(t^3-t=-d\). There is just one branch point, with lower ramification jump \(1\), different exponent \(4\). Thus every smooth noncentral member is ordinary while the central Klein quartic has \(3\)-rank zero.

## Assumptions and scope
All assertions are geometric over an algebraically closed field of characteristic \(3\). The \(3\)-rank of a smooth projective curve means the \(\mathbb F_3\)-dimension of the geometric \(3\)-torsion points of its Jacobian. The assertion excludes the two singular parameters. \(\lambda=0\) is the classical Klein plane-quartic equation, but its already-known supersingularity is not itself proposed as new. The contribution is the complete pencil-wide quotient and rank-jump formula.

## Proof
**1. Invariant coordinates and the quotient.** Write \(s=X+Y+Z\), \(e_2=XY+YZ+ZX\), and \(\Delta=(X-Y)(X-Z)(Y-Z)\). On \(s\ne0\), normalize \(s=1\) and set \(r=e_2\), \(d=\Delta\), \(t=X-Y\). In characteristic \(3\), exact polynomial identities give
\[
 t^3-t=-d,\quad
 X=-r-t^2-t,\quad Y=-r-t^2+t,\quad Z=1-r-t^2.
\]
Substitution into the defining quartic yields *exactly*
\[
 (1+\lambda)d^2+d+(1+\lambda)r^3-\lambda r^2+r=0.
\]
This is an isomorphism of affine coordinate rings, with \(d=-(t^3-t)\). Under the coordinate cycle, \(t\) maps to \(t-1\), whereas \(r,d\) are invariant. Therefore the displayed curve is the function-field quotient and the cover has Artin–Schreier equation \(t^3-t=-d\).

**2. Smoothness.** On \(s=0\), substituting \(Z=-X-Y\) into the quartic gives \(-(X-Y)^4\). Its only geometric point is \(P=[1:1:1]\), and the line meets the quartic there with multiplicity \(4\). In chart \(Z=1\), put \(X=1+u\), \(Y=1+w-u\); at \(P\) the equation begins \((1+\lambda)w-u^4+\text{terms of order at least two involving }w\). Hence \(P\) is smooth precisely if \(1+\lambda\ne0\). For that case, the affine curve above is smooth precisely if \(E_\lambda\) is smooth, because an Artin–Schreier polynomial has derivative \(-1\) in \(t\). Completing the square and scaling (possible for \(1+\lambda\ne0\)) gives the Weierstrass equation
\[
 y^2=r^3-\frac{\lambda}{1+\lambda}r^2+\frac{r}{1+\lambda}-\frac1{(1+\lambda)^2}.
\]
Its discriminant in characteristic \(3\) is \((\lambda-1)/(1+\lambda)^5\). It is nonsingular exactly for \(\lambda\ne1,-1\). If \(\lambda=1\), the affine quotient and its finite étale cover are singular. This proves the complete smoothness assertion. A smooth degree-four plane curve has genus \(3\).

**3. Ramification and connectedness.** The order-three coordinate permutation has a unique projective fixed point in characteristic \(3\), namely \(P\). In the local parameter \(u\) above, \(w=u^4/(1+\lambda)+O(u^5)\). Its action satisfies
\[
 \sigma(u)-u=\frac{w-u^2}{1+u}=-u^2+O(u^3).
\]
The lower ramification jump is therefore \(1\), giving different exponent \(4\). It is the unique ramification point. Alternatively the elliptic function \(d\) has a single pole of order \(3\) at infinity; it cannot be an Artin–Schreier coboundary because an elliptic curve has no rational function with a unique simple pole. Hence the cover is connected. The genus formula \(2g(C)-2=3(2g(E)-2)+4\) gives genus \(3\), consistent with the plane model.

**4. The \(j\)-invariant and \(3\)-rank.** For the displayed monic cubic, the characteristic-three Weierstrass invariant \(c_4\) is \(\lambda^2/(1+\lambda)^2\), and the discriminant is \((\lambda-1)/(1+\lambda)^5\). Therefore
\[
 j(E_\lambda)=\frac{c_4^3}{\Delta}=\frac{\lambda^6}{\lambda^2-1}.
\]
A smooth characteristic-three elliptic curve has \(3\)-rank zero exactly when \(j=0\), and otherwise \(3\)-rank one. Applying the Deuring–Shafarevich formula to this cyclic degree-three cover, with exactly one totally ramified point, gives
\[
 f_3(C_\lambda)-1=3(f_3(E_\lambda)-1)+(3-1),
 \qquad f_3(C_\lambda)=3f_3(E_\lambda).
\]
Consequently \(f_3(C_0)=0\), and all other smooth members are ordinary of rank \(3\).

## Verification
The accompanying executable \(verify.py\) checks the universal polynomial identities over \(\mathbb F_3[\lambda,r,t]\), verifies the algebraic smoothness-discriminant numerator, and confirms the characteristic-three \(j\)-formula by exact polynomial arithmetic. These computations are auxiliary to the geometric proof; they do not replace the ramification and Deuring–Shafarevich arguments. The package includes no finite-field census and asserts no classification beyond this pencil.

## Relationship to prior work
Elkies, *The Klein Quartic in Number Theory* (1999), treats the central Klein quartic, its classical order-three quotient, and its characteristic-three behavior; these facts are not new here. The characteristic-zero genus-three automorphism literature, including Bars' survey, concerns related automorphisms but does not imply the present characteristic-three wild quotient with an explicit varying \(j\)-invariant and complete \(3\)-rank divisor. Tafazolian's later analysis of characteristic-three Klein/Hermitian quartics likewise treats the special zero-rank curve, not the displayed one-parameter family. The actual comparison is between statements, not merely titles: none of these inspected passages supplies the family-wide formulas \(j=\lambda^6/(\lambda^2-1)\) and \(f_3(C_\lambda)\in\{0,3\}\). An equivalent parametrization of this family in specialized literature remains a residual originality risk.

## Limitations
The claim is confined to the specified cyclic pencil over algebraically closed characteristic-three fields. No identification of full automorphism groups, moduli-theoretic universal property, theta structures, or reduction over mixed-characteristic DVRs is asserted. The classical Klein quartic case and the general Deuring–Shafarevich formula are acknowledged prior results. Independent audit or external replication is not claimed.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), 51–102. https://library.slmath.org/books/Book35/files/elkies.pdf
2. G. Egan, *Klein's Quartic Equation*, public page dated 2 August 2006. https://www.gregegan.net/SCIENCE/KleinQuartic/KleinQuarticEq.html
3. F. Bars, *On the automorphism groups of genus 3 curves* (seminar, 2005). https://stnb.cat/media/xerrades/presentacions/gen3talk.pdf
4. S. Tafazolian, *A classification of zero p-rank curves with large automorphism groups in odd characteristic* (2026), Section 9, Klein quartic discussion. https://arxiv.org/html/2609.33185v2
5. Deuring–Shafarevich p-rank formula for Galois p-group covers (standard theorem).
