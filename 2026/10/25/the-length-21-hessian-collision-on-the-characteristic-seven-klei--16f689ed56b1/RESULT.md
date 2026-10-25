# The length-\(21\) Hessian collision on the characteristic-seven Klein quartic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\), and let \(C\subset\mathbb P^2_k\) be the plane quartic
\[
F=X^3Y+Y^3Z+Z^3X=0.
\]
Define its **classical Hessian intersection** \(D=V(F,\det(\partial_i\partial_j F))\), as a projective scheme. Then \(D\) is supported at exactly four \(\mathbb F_7\)-rational points:
\[
P=[1:2:4],\quad Q_X=[1:0:0],\quad Q_Y=[0:1:0],\quad Q_Z=[0:0:1].
\]
The scheme has total length \(24\); the three coordinate points are reduced of length \(1\), whereas \(D\) has local length **\(21\)** at the unique singular point \(P\). The maximal-ideal Hilbert function of the local Artin algebra \(\mathcal O_{D,P}\), including degree zero, is
\[
(1,2,2,2,2,2,2,2,1,1,1,1,1,1).
\]
Thus the singular contribution is noncurvilinear. All three smooth points on the Hessian intersection are ordinary flexes of contact order \(3\) with their respective coordinate-line tangents; no other smooth points of \(C\) lie on its classical Hessian.

## Assumptions and scope
All assertions are for the indicated coefficientwise reduction of the Klein quartic in characteristic \(7\), with the **ordinary formal-second-derivative Hessian**. The reduced special fiber is singular, so this is **not** an assertion about a smooth-fiber inflection divisor, a positive-characteristic Wronskian, or an inflection-limit scheme. The singular point \(P\) was previously established as a type-\(A_6\) singularity by Martin--Stadlmayr; neither the singularity type nor the classical Klein equation is new here. The local Hilbert function is taken with respect to the intrinsic maximal ideal of the zero-dimensional local ring, not with respect to an arbitrary global filtration.

## Proof
Direct integer differentiation followed by reduction modulo \(7\) yields the Hessian identity
\[
\det(\partial_i\partial_jF)=-54h,
\qquad h=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5.
\]
Since \(-54\) is invertible modulo \(7\), the Hessian ideal is \((F,h)\). For the affine chart \(X=1\), put \(y=Y/X\), \(z=Z/X\); then
\[
f=y+y^3z+z^3,\qquad h=z-5y^2z^2+y^5+yz^5.
\]
The reduced lexicographic Gröbner basis of \((f,h)\) over \(\mathbb F_7[y,z]\), with \(y>z\), is
\[
\begin{split}
g_1&=y^2+3yz^3-2z^{13}-2z^6,\\
g_2&=yz^7+3y-2z^{10}+z^3,\\
g_3&=z^{15}-z^8+2z=z(z-4)^{14}.
\end{split}
\]
Its initial monomials are \(y^2,yz^7,z^{15}\). The standard monomials are \(1,z,\ldots,z^{14}\) and \(y,yz,\ldots,yz^6\), so this affine intersection has length \(22\). Its support has \(z=0\) or \(z=4\). For \(z=0\), \(f=y\) so only \(Q_X\) occurs. For \(z=4\), \(f\) vanishes only at \(y=2\) or \(y=3\), but \(h(3,4)\ne0\); hence the only intersection point there is \(P\). The point \(Q_X\) has local intersection length \(1\): on \(C\), the relation \(f=0\) gives \(y\in(z^3)\) in the completed local ring, and then \(h\equiv z\pmod{(z^2)}\). Consequently the length at \(P\) is \(22-1=21\).

For the intrinsic local Hilbert function translate to \(u=y-2\), \(v=z-4\) and work modulo \(7\). The length of
\[
k[u,v]/(f(u+2,v+4),h(u+2,v+4),(u,v)^m)
\]
for \(m=1,\ldots,14\) is successively
\[
1,3,5,7,9,11,13,15,16,17,18,19,20,21.
\]
These lengths follow from an explicit zero-dimensional Gröbner-basis computation over the prime field (replayable in `verify.py`), not a numerical approximation. Consecutive differences give the stated Hilbert function; its first two values \(1,2\) prove noncurvilinearity. The stabilized length \(21\) also matches the independent affine colength calculation.

On the line \(X=0\), the curve equation reduces to \(Y^3Z=0\). Thus the only points at infinity are \(Q_Y,Q_Z\). On the \(Y=1\) chart the first-order terms of \(F\) and \(h\) at \(Q_Y\) are respectively \(z\) and \(x\); on the \(Z=1\) chart they are \(x\) and \(y\). Both intersections are transverse, of length \(1\). Therefore the whole Hessian scheme consists exactly of the four points and its total length is \(21+1+1+1=24=4\cdot6\), agreeing with Bézout.

The curve has no singularities beyond \(P\): if \(X=0\), the two points on \(C\) have nonzero gradient; if \(X=1\), simultaneous vanishing of \(F_X,F_Y,F_Z\) forces \(y^2z=2\), \(y^3=4z^2\), hence \(y^7=2\), and in characteristic \(7\) the unique solution is \(y=2,z=4\). Finally the three tangents are \(Y=0\) at \(Q_X\), \(Z=0\) at \(Q_Y\), and \(X=0\) at \(Q_Z\). Their restrictions to \(C\) are respectively \(XZ^3\), \(X^3Y\), and \(Y^3Z\), giving intersection multiplicity \(3\) at the indicated smooth points. There are no other smooth Hessian points, proving the final assertion.

## Verification
Run `python verify.py` with Python and SymPy installed. The script recomputes the polynomial Hessian, the claimed exact reduced Gröbner basis, the finite affine support, the entire list of truncated local colengths, and the three tangent-contact identities. Expected output begins `VERIFY_OK`. The standard-monomial count explicitly proves affine exhaustion, and the two remaining projective-chart calculations prove exhaustion at infinity. This exact computation proves the finite Artin-algebra claim; merely sampling \(\mathbb F_7\)-points would not.

## Relationship to prior work
The Klein quartic and its reduction at \(7\) are classical. Dolgachev--Kanev (1993, Example 6.1.1) already give the full classical Klein Hessian equation over characteristic zero; its explicit polynomial is **not** claimed as new. Poonen--Schaefer--Stoll's 2005 preprint treats the Klein quartic from a different arithmetic perspective. Martin--Stadlmayr (2024), Section 8.1, analyze the characteristic-\(7\) plane quartic, prove that the displayed point is its unique \(A_6\) singularity and relate it to del Pezzo geometry. Iadarola--Ritzenthaler (2019), Example 1.1, discuss the bad reduction of this Klein model. Those results do not state the four-point Hessian intersection, the local length \(21\), or its intrinsic Artin Hilbert function in the inspected material. A possible unlocated treatment of osculation at the bad prime remains an originality risk.

## Limitations
The assertion is about the classical Hessian at the specific singular reduction, not all projective models, not degeneration of the complete smooth-fiber flex scheme, and not the positive-characteristic Hasse-Wronskian. No independent scientific audit has been performed. Identifying the \(A_6\) singularity alone would not establish the Hilbert function or the complete scheme, and is not presented as new.

## References
1. B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, arXiv:math/0508174v1, first posted 2005-08-10, https://arxiv.org/abs/math/0508174.
2. G. Martin and C. Stadlmayr, *RDP del Pezzo surfaces with global vector fields in odd characteristic*, Algebraic Geometry (2024), Section 8.1, https://api.algebraicgeometry.nl/Article/20460/2024-3-012.pdf.
3. A. Iadarola and C. Ritzenthaler, *Primes of bad reduction of CM curves of genus 3*, Example 1.1 (2019), https://www.rnta.eu/4MSRNTA/Ritzenthaler-Iadarola.pdf.
4. I. Dolgachev and V. Kanev, *Polar Covariants of Plane Cubics and Quartics*, Advances in Mathematics 98 (1993), Example 6.1.1, https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/advances93.pdf.
5. N. D. Elkies, *The Klein Quartic in Number Theory* (1999), historical background; full source text could not be inspected in this run, https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b.
