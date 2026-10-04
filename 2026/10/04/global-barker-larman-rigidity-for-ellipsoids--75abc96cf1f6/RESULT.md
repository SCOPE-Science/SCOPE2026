# Global Barker–Larman rigidity for ellipsoids
## Finding
Let \(n\ge 3\) and let the Euclidean ball \(B_r(0)\), with \(r>0\), lie in the interiors of two ellipsoids \(E_1,E_2\subset\mathbb R^n\). For every \(u\in S^{n-1}\), write
\[
H_u=\{x\in\mathbb R^n:u\cdot x=r\}.
\]
If
\[
\operatorname{vol}_{n-1}(E_1\cap H_u)=\operatorname{vol}_{n-1}(E_2\cap H_u)
\quad\text{for every }u\in S^{n-1},
\]
then \(E_1=E_2\). Hence the Barker–Larman data from the supporting hyperplanes of one fixed inner ball are globally injective on the complete ellipsoid class in every dimension \(n\ge3\).

## Assumptions and scope
After translation, the common inner ball is \(B_r(0)\). Write an arbitrary ellipsoid as
\[
E(c,Q)=\{c+Q^{1/2}z:\lVert z\rVert\le1\},
\]
where \(Q\) is real symmetric positive definite. Put
\[
s(u)=u^TQu,\qquad y(u)=u\cdot c,\qquad D=\det Q.
\]
The strict inclusion \(B_r(0)\subset\operatorname{int}E(c,Q)\) guarantees \(s(u)-(r-y(u))^2>0\) for every unit \(u\). No concentricity, common principal axes, or small-perturbation hypothesis is assumed.

## Proof
Let \(\kappa_{n-1}=\pi^{(n-1)/2}/\Gamma((n+1)/2)\) be the volume of the unit ball in \(\mathbb R^{n-1}\). Under the affine map \(z\mapsto c+Q^{1/2}z\), the plane \(H_u\) becomes
\[
(Q^{1/2}u)\cdot z=r-y(u).
\]
The unit-ball slice has radius \(\sqrt{1-(r-y(u))^2/s(u)}\). The \(n-1\)-dimensional Jacobian of \(Q^{1/2}\) on that slice is \(\sqrt D/\sqrt{s(u)}\). Therefore
\[
V_E(u):=\operatorname{vol}_{n-1}(E\cap H_u)
=\kappa_{n-1}\sqrt D\,
\frac{[s(u)-(r-y(u))^2]^{(n-1)/2}}{s(u)^{n/2}}.
\]
Define the data transform
\[
F_E(u)=\left(\frac{V_E(u)}{\kappa_{n-1}}\right)^{2/(n-1)}
=D^{1/(n-1)}\frac{s(u)-(r-y(u))^2}{s(u)^{n/(n-1)}}.
\]
For two ellipsoids with identical section data, \(F_E=F_{E'}\). Their odd parts satisfy
\[
F_E(u)-F_E(-u)=4rD^{1/(n-1)}\frac{y(u)}{s(u)^{n/(n-1)}}.
\]
If \(c=0\), this odd part vanishes identically, so the same identity forces \(c'=0\). Assume first that \(c,c'\neq0\). For arbitrary \(x\in\mathbb R^n\), set \(s(x)=x^TQx\), \(s'(x)=x^TQ'x\), \(\ell(x)=c\cdot x\), and \(\ell'(x)=c'\cdot x\). Homogenizing the odd-part equality and raising it to the integer power \(n-1\) gives the polynomial identity
\[
D\,\ell(x)^{n-1}s'(x)^n
=D'\,\ell'(x)^{n-1}s(x)^n.
\]
A positive-definite quadratic form in at least three variables is irreducible over \(\mathbb R\). Since \(s\) cannot divide the nonzero linear form \(\ell\), unique factorization forces \(s'=\lambda s\) for some \(\lambda>0\). Thus \(Q'=\lambda Q\) and \(D'=\lambda^nD\). Substitution back into the unpowered odd identity cancels all powers of \(\lambda\) and yields \(\ell'=\ell\), hence \(c'=c\).

Now compare the even parts:
\[
\frac{F_E(u)+F_E(-u)}2
=D^{1/(n-1)}\frac{s(u)-r^2-y(u)^2}{s(u)^{n/(n-1)}}.
\]
With \(Q'=\lambda Q\) and \(c'=c\), equality of the even parts reduces to
\[
s(u)-r^2-y(u)^2=\lambda s(u)-r^2-y(u)^2,
\]
so \(\lambda=1\). Hence \(Q'=Q\).

It remains to treat the centered case \(c=c'=0\). Let \(h(x)=x^Tx\). Homogenizing the equality of the transforms and raising to \(n-1\) gives
\[
D[s(x)-r^2h(x)]^{n-1}s'(x)^n
=D'[s'(x)-r^2h(x)]^{n-1}s(x)^n.
\]
Because the inner ball lies strictly inside the centered ellipsoid, both \(s\) and \(s-r^2h\) are positive-definite quadratic forms. If \(Q\) is not a scalar matrix, these two irreducible quadratics are not associates. Unique factorization again forces \(s'=\lambda s\), and substitution in the original transform gives \(\lambda=1\).

If instead \(Q=\alpha I\), then \(F_E\equiv\alpha-r^2\). Were \(Q'\) nonscalar, the Rayleigh quotient \(s'(u)\) would fill a nontrivial interval, while
\[
t\longmapsto D'^{1/(n-1)}(t-r^2)t^{-n/(n-1)}
\]
has derivative zero at only \(t=nr^2\) and therefore cannot be constant on an interval. Thus \(Q'=\alpha'I\), and equality of the constant transforms gives \(\alpha'=\alpha\). In every case \(c'=c\) and \(Q'=Q\), proving \(E_1=E_2\).

## Verification
The derivation uses only affine slice geometry, parity of the explicit data transform, and unique factorization of real polynomials. The bundled `verify.py` independently checks the slice formula against direct affine-hyperplane Jacobians for several nonconcentric positive-definite examples in dimensions \(3\) through \(6\), and checks the odd/even identities numerically to tight tolerance. These finite checks are diagnostic only; the proof above is the infinite-dimensional statement.

## Relationship to prior work
Barker and Larman asked whether supporting-hyperplane section volumes relative to one inner body determine the outer convex body. Yaskin and Zhang restated the one-inner-ball problem in 2015 and recorded that it was open even in the plane, while noting positive cases such as polytopes. Makai and Martini's 2016 full text explicitly describes the original hyperplane problem as unsolved and proves only a local first-order determination theorem for small smooth perturbations. Matthews' 2026 open-access polygon theorem gives global determination for polygons in the planar setting and explicitly points to extensions beyond the polyhedral class as a further direction. The present theorem is different: it is a global, nonperturbative injectivity result for all ellipsoids in every dimension \(n\ge3\), with arbitrary centers and principal axes.

## Limitations
The theorem is restricted to ellipsoids and does not solve the Barker–Larman problem for general smooth or strictly convex bodies. It also does not claim a stability estimate, reconstruction algorithm under noisy data, or a minimal finite set of supporting directions. The original 2001 Barker–Larman article was not available in full through the bounded lawful-access checks performed here; later full-text surveys summarize its relevant partial results, but an unindexed or differently phrased ellipsoid-specific argument in older literature remains a residual originality risk.

## References
1. V. Yaskin and N. Zhang, *Non-central sections of convex bodies*, arXiv:1509.08174v1, first public version 2015-09-28, MSC 52A20, 52A38.
2. E. Makai, Jr. and H. Martini, *Unique local determination of convex bodies*, arXiv:1602.00959v1, 2016.
3. J. A. Barker and D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79–96, DOI:10.1016/S0012-365X(01)00111-X.
4. B. Matthews, *Hedgehog reconstruction of polygons: Non-central sections and slabs*, Canadian Mathematical Bulletin, 2026, DOI:10.4153/S0008439526102355.
