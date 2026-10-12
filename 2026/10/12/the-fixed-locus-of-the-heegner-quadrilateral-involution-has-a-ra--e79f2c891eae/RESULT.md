# The fixed locus of the Heegner quadrilateral involution has a rational conic component
## Finding
For Patterson's Heegner involution on nonzero rational distance sextuples, a sextuple is fixed exactly when it can be written as \(\mathbf d=(su^2,sv^2,suv,r,uz,vz)\) with nonzero rational \(s,u,v,z,r\). On this fixed locus the Cayley--Menger polynomial factors as \[CM(\mathbf d)=-u^2v^2\bigl(r-s(u^2-v^2)\bigr)\bigl(r+s(u^2-v^2)\bigr)\bigl(r^2s^2-2s^2(u^2+v^2)z^2+z^4\bigr).\] Hence, for positive distances with the \(123\)-triangle nondegenerate, the rational-quadrilateral equation \(CM=0\) is equivalent, after \(X=z/s\) and \(Y=r/z\), to the rational conic \(X^2+Y^2=2(u^2+v^2)\). This conic is rationally parametrized from \((u+v,u-v)\); for example \(s=25,u=2,v=1,t=-4/3\) gives the fixed nondegenerate rational quadrilateral distance sextuple \((100,25,50,117,90,45)\). Because all triangle inequalities are strict at this point, an open rational-parameter interval around it supplies infinitely many distinct geometric rational quadrilaterals fixed by the Heegner involution.

A convenient explicit parametrization of the nondegenerate conic component is obtained from the rational point \((u+v,u-v)\). For \(t\in\mathbb Q\), put
\[
X_t=\frac{(t^2-1)(u+v)-2t(u-v)}{1+t^2},\qquad
Y_t=\frac{(1-t^2)(u-v)-2t(u+v)}{1+t^2}.
\]
Then \(X_t^2+Y_t^2=2(u^2+v^2)\). Taking \(z=sX_t\) and \(r=zY_t\) gives the corresponding fixed Cayley--Menger solution whenever the displayed quantities are nonzero.

## Assumptions and scope
The Heegner involution is the birational map on a nonzero distance sextuple \(\mathbf d=(d_{12},d_{13},d_{14},d_{23},d_{24},d_{34})\)
\[
i_H(\mathbf d)=\left(d_{12},d_{13},\frac{d_{12}d_{13}}{d_{14}},d_{23},\frac{d_{12}d_{34}}{d_{14}},\frac{d_{13}d_{24}}{d_{14}}\right),
\]
as in Patterson's preprint. The Cayley--Menger normalization is Patterson's \(CM=CM_0/2\), where \(CM_0\) is the standard \(5\times5\) determinant. The algebraic fixed-locus statement is over \(\mathbb Q\) with all six coordinates nonzero. The geometric conclusion uses positive distances and strict triangle inequalities; no claim is made about zero-coordinate boundary strata.

## Proof
The equations \(i_H(\mathbf d)=\mathbf d\) reduce to
\[
d_{14}^2=d_{12}d_{13},\qquad d_{14}d_{24}=d_{12}d_{34},
\]
because the remaining transformed-coordinate equation follows from these two when the coordinates are nonzero. Every rational solution of the first relation has the form
\[
d_{12}=su^2,\qquad d_{13}=sv^2,\qquad d_{14}=suv.
\]
Indeed, given a fixed triple one may take \(s=d_{13},v=1,u=d_{14}/d_{13}\). The second fixed-point relation then says \(v d_{24}=u d_{34}\), so \(d_{24}=uz\) and \(d_{34}=vz\) for a rational \(z\); write \(d_{23}=r\).

Substituting
\[
(d_{12},d_{13},d_{14},d_{23},d_{24},d_{34})=(su^2,sv^2,suv,r,uz,vz)
\]
into the Cayley--Menger determinant and factoring gives
\[
CM=-u^2v^2\bigl(r-s(u^2-v^2)\bigr)\bigl(r+s(u^2-v^2)\bigr)
\bigl(r^2s^2-2s^2(u^2+v^2)z^2+z^4\bigr).
\]
For positive distances, the first two factors give \(r=|s(u^2-v^2)|=|d_{12}-d_{13}|\), exactly the degenerate boundary of the \(123\)-triangle. Thus a fixed point with a nondegenerate \(123\)-triangle and \(CM=0\) lies on the final factor. Dividing that equation by \(s^2z^2\) and setting \(X=z/s\), \(Y=r/z\) gives
\[
X^2+Y^2=2(u^2+v^2).
\]
The point \((u+v,u-v)\) lies on this conic. Intersecting it with a line of rational slope \(t\) yields the displayed formulas for \(X_t,Y_t\), proving rational parametrizability.

For \(s=25,u=2,v=1,t=-4/3\), the parametrization gives \(X=9/5\), \(Y=13/5\), hence \(z=45\), \(r=117\), and
\[
\mathbf d=(100,25,50,117,90,45).
\]
The four face triples are \((100,25,117)\), \((100,50,90)\), \((25,50,45)\), and \((117,90,45)\); every triangle inequality is strict. Also \(CM(\mathbf d)=0\). Equivalently, the Gram matrix based at vertex \(1\) has determinant zero and positive principal minors of orders one and two, so it is positive semidefinite of rank two and realizes the sextuple by four coplanar points. Since strict inequalities persist under sufficiently small changes of \(t\), and rational numbers are dense, infinitely many nearby rational \(t\) give distinct geometric fixed rational quadrilaterals.

## Verification
The standalone verifier `verify_heegner_fixed_locus.py` constructs Patterson's Cayley--Menger determinant symbolically, verifies the complete factorization exactly, checks the conic parametrization as a polynomial identity, and replays the fixed geometric witness with exact rational arithmetic. Its recorded output is in `verification_output.txt`. The computation verifies algebraic identities and the explicit witness; the infinitude statement additionally uses the proved rational parametrization and openness of strict triangle inequalities.

## Relationship to prior work
Patterson's 2026 preprint defines the Heegner involution explicitly and proves its covariance with the Cayley--Menger polynomial, but the inspected full text does not classify the fixed distance sextuples or factor \(CM\) on that locus. Its stated purpose is to develop involutions acting on rational quadrilaterals and tetrahedra, making the fixed locus a natural structural question. Patterson's 2019/2021 predecessor studies the Cayley--Menger variety and a Weddle-surface involution; the inspected passages concerning a fixed-point locus refer to that different geometric involution, not to the distance-coordinate Heegner map above. Targeted published-finding and web searches for the fixed equations, their Cayley--Menger factorization, and the conic reduction found no statement implying this result.

## Limitations
The complete algebraic description here excludes coordinate hyperplanes because Patterson's displayed Heegner map itself divides by \(d_{14}\). The conic component includes parameter values that fail positivity or geometric inequalities; the proof asserts geometry only where those inequalities hold and establishes a nonempty open rational family via the explicit witness. No classification is claimed modulo the full Heegner group or the \(S_4\) relabeling action. Unpublished historical manuscript material could contain related calculations; no such unpublished material is used as evidence of originality.

## References
1. S. J. Patterson, *Rational quadrilaterals and tetrahedra -- the involutions of Kummer, Heegner and Regge*, arXiv:2609.40101v1, 30 September 2026.
2. S. J. Patterson, *On a question of H. A. Schwarz*, arXiv:1912.06807v1; later published in *Stochastics and Dynamics* 21 (2021), Article 2140004.
