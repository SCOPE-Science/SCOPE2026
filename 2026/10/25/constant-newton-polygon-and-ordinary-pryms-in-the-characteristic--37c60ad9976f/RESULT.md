# Constant Newton polygon and ordinary Pryms in the characteristic-five bielliptic Picard family

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\). For every \(a,b\in k\) satisfying \(b(a^2+b)\ne0\), let \(C_{a,b}\) be the smooth projective plane quartic
\[
C_{a,b}:\quad Y^3Z=X^4+aX^2Z^2+bZ^4.
\]
Then its Jacobian has \(5\)-rank exactly \(2\), \(a\)-number exactly \(1\), and Newton slopes
\[
\boxed{0,0,\tfrac12,\tfrac12,1,1}.
\]
The natural genus-one quotient by \((X,Y,Z)\mapsto(-X,Y,Z)\) is supersingular, while the associated two-dimensional Prym variety is ordinary. In particular, *no smooth member of this one-dimensional family has a Jacobian of \(5\)-rank zero or one*, and the Prym ordinarity does not jump anywhere in the smooth family.

## Assumptions and scope

The claim concerns all geometric parameters over an algebraically closed field of characteristic \(5\), not just finite-field examples. The expression \(b(a^2+b)\) is the squarefreeness condition for \(f(X)=X^4+aX^2+b\): its derivative is \(4X^3+2aX\), so a multiple root occurs precisely when \(b=0\) or \(a^2+b=0\). The point at infinity \([0:1:0]\) is smooth because the derivative of the quartic equation with respect to \(Z\) equals \(Y^3\) there. Thus every admitted \(C_{a,b}\) is a smooth plane quartic of genus \(3\).

Here the \(5\)-rank is the dimension over \(\mathbb F_5\) of the geometric group of \(5\)-torsion points, and the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J(C_{a,b})[5])\). The latter equals the kernel dimension of the Cartier operator on holomorphic differentials. The Prym is the connected kernel of the norm map for the displayed double cover.

## Proof

Put \(F=Y^3Z-X^4-aX^2Z^2-bZ^4\). From the standard cohomology sequence for a smooth plane quartic, \(H^1(C_{a,b},\mathcal O_C)\) identifies with \(H^2(\mathbb P^2,\mathcal O(-4))\). Use the Cech basis represented by the inverse monomials with exponent vectors
\[
\alpha_1=(2,1,1),\qquad \alpha_2=(1,2,1),\qquad \alpha_3=(1,1,2).
\]
For the absolute Frobenius, its Hasse--Witt matrix \(H\) in this basis has entry \(H_{ij}\) equal to the coefficient in \(F^{4}\) of the monomial \(X^{5\alpha_{j,1}-\alpha_{i,1}}Y^{5\alpha_{j,2}-\alpha_{i,2}}Z^{5\alpha_{j,3}-\alpha_{i,3}}\). This follows directly by raising a Cech representative to its fifth power and multiplying by \(F^4\) to return to the degree \(-4\) ambient cohomology group.

The four terms of \(F\) have exponent triples \((0,3,1)\), \((4,0,0)\), \((2,0,2)\), \((0,0,4)\). Comparing their exponents in the fourfold product gives
\[
H=\begin{pmatrix}
0&0&0\\
0&0&3b(a^2+b)\\
0&1&0
\end{pmatrix}.
\]
Indeed, the \((3,2)\) entry comes from selecting three factors \(Y^3Z\) and one \(-X^4\), with coefficient \(-4=1\) in characteristic \(5\). The \((2,3)\) entry comes from selecting either one \(Y^3Z\), one \(-X^4\), and two \(-bZ^4\), or one \(Y^3Z\), two \(-aX^2Z^2\), and one \(-bZ^4\). Each multinomial contribution equals \(-12\) times the relevant parameter product, hence the sum is \(3b(a^2+b)\) modulo \(5\). Every other entry is zero by the required exponent parities or divisibility by \(3\) of the \(Y\)-exponent.

Write \(c=3b(a^2+b)\). The smoothness assumption is exactly \(c\ne0\). Because Frobenius is fifth-power semilinear, its square has matrix
\[
H H^{(5)}=\operatorname{diag}(0,c,c^5).
\]
Thus Frobenius acts bijectively on a stable two-dimensional summand and nilpotently on the remaining one-dimensional summand. Its stable rank, hence the Jacobian \(5\)-rank, equals \(2\). Since \(\operatorname{rank}H=2\), the \(a\)-number equals \(3-2=1\). Polarization symmetry of the Newton polygon, together with two slope-zero and two slope-one terms, forces the remaining two slopes to be \(1/2\) each.

For the quotient by the tame involution \(X\mapsto-X\), set \(u=X^2\). The genus-one quotient has affine equation \(Y^3=u^2+au+b\). Completing the square gives a Weierstrass equation with \(j=0\); in characteristic \(5\) this elliptic curve is supersingular (equivalently the coefficient of the fourth power of the cubic in its quadratic Hasse test vanishes). The usual norm and pullback maps for a tame double cover give an isogeny \(J(C_{a,b})\sim E\times P\), where \(P\) is its Prym abelian surface. Since \(E\) has \(5\)-rank \(0\) and \(J(C_{a,b})\) has \(5\)-rank \(2\), the Prym has \(5\)-rank \(2=\dim P\), hence is ordinary. This completes the assertion for every admitted geometric parameter.

## Verification

The accompanying standalone Python checker expands \(F^4\) exactly in the polynomial ring \(\mathbb F_5[X,Y,Z,a,b]\), extracts all nine cohomological coefficient entries, and compares the resulting matrix with the displayed formula. It also exhaustively counts points on representative smooth fibres over \(\mathbb F_5\) and \(\mathbb F_{25}\), using a direct representation of the latter field. Execute \(\texttt{python3 verify_picard.py}\) with only the Python standard library. The universal conclusion relies on the symbolic polynomial identity and the cohomological proof, not on a finite parameter enumeration.

## Relationship to prior work

Faber--Pagani (arXiv:1206.4301, first publicly posted 2012-06-19) study the genus-three bielliptic moduli locus, rather than the characteristic-five \(5\)-rank of this subfamily. Kazemifard--Tafazolian (DOI:10.1016/j.ffa.2014.12.002, 2015) determine Newton polygons for two *individual* Picard curves, including \(Y^3=X^4-1\); their characteristic-five instance is the parameter \(a=0\) of this theorem up to scaling. The asserted contribution is the **uniform family-wide** stable Frobenius rank, constant Newton polygon, and Prym ordinarity, not the known special instance.

Bouw--Koutsianas--Sijsling--Wewers (DOI:10.1112/jlms.12323, 2020) discuss Picard models and their arithmetic; Laga--Shnidman (arXiv:2308.15297; DOI:10.1112/jlms.70347) develop the geometry and arithmetic of exactly this bielliptic Picard family and its quaternionic-multiplication Pryms. The inspected sections of those works did not give a universal characteristic-five Prym-ordinarity theorem. Estrada-Sarlabous (DOI:10.1002/mana.19911520125, 1991) discusses Hasse--Witt criteria for general Picard Jacobians, but the full text was inaccessible in this investigation; it is an explicit residual risk of prior implication. No independence or global novelty certification is asserted.

## Limitations

The result does not cover singular boundary parameters \(b(a^2+b)=0\), characteristics other than \(5\), or the full three-dimensional moduli of Picard curves. It determines Newton slopes and \(5\)-rank but not the full isomorphism class of each \(5\)-divisible group or its Ekedahl--Oort type beyond the \(a\)-number. Literature overlap remains possible, particularly through early general Hasse--Witt formulas. The arithmetic and geometric arguments have undergone a self-review only; independent validation has not been performed.

## References

- C. Faber and N. Pagani, *The class of the bielliptic locus in genus 3*, arXiv:1206.4301 (2012).
- A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107--122, DOI:10.1016/j.ffa.2014.12.002.
- J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic \(p>0\)*, Mathematische Nachrichten 152 (1991), 329--340, DOI:10.1002/mana.19911520125.
- I. Bouw, A. Koutsianas, J. Sijsling, and S. Wewers, *Conductor and discriminant of Picard curves*, Journal of the London Mathematical Society 102 (2020), 368--404, DOI:10.1112/jlms.12323.
- J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (2023), Journal of the London Mathematical Society 112 (2025), e70347, DOI:10.1112/jlms.70347.
