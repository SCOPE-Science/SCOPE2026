# The characteristic-five bielliptic genus-two Hasse crossing and its exact arithmetic strata

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). On the two-parameter normalized family of genus-two curves
\[
C_{a,b}:\quad y^2=x^6+a x^4+b x^2+1,
\]
put
\[
\Delta=a^2b^2-4a^3-4b^3+18ab-27,\qquad
H_1=a^2+2b,\quad H_2=b^2+2a
\]
with coefficients interpreted in characteristic \(5\). Write \(U=\{(a,b):\Delta\ne0\}\). Then the Jacobian's \(5\)-rank and \(a\)-number for every \((a,b)\in U(k)\) are
\[
f_5(J(C_{a,b}))=\mathbf1_{H_1\ne0}+\mathbf1_{H_2\ne0},
\qquad a(J(C_{a,b}))=2-f_5(J(C_{a,b})).
\]
The two smooth Hasse divisors \(H_1=0\) and \(H_2=0\) intersect transversely in \(U\) at exactly \((0,0)\); the other three geometric intersections occur on the singular-curve boundary, where the cubic \(u^3+a u^2+b u+1\) has a triple root. Thus precisely one normalized smooth parameter is superspecial, namely \((0,0)\), and the nonordinary locus has two geometrically irreducible components meeting normally at that point.

For every \(n\ge1\), write \(q=5^n\) and \(\varepsilon=(-1)^n\). The exact number of smooth *marked coefficient pairs* in each rank stratum is
\[
N_0(q)=1,\qquad N_1(q)=2q-6-2\varepsilon,\qquad
N_2(q)=q^2-3q+6+2\varepsilon.
\]
In particular, \(\#U(\mathbb F_q)=q^2-q+1\). These are not counts of geometric isomorphism classes. The rank-one stratum consists of two disjoint smooth affine curves, each the affine line minus the origin and the three roots of \(z^3=2\) over an algebraic closure.

As a compact equivalent accounting of all extension counts, the Hasse--Weil zeta functions of the three constructible rank strata, with variable \(T\), are
\[
Z_0(T)=\frac1{1-T},\qquad
Z_1(T)=\frac{(1-T)^6(1+T)^2}{(1-5T)^2},
\qquad
Z_2(T)=\frac{(1-5T)^3}{(1-25T)(1-T)^6(1+T)^2}.
\]

## Assumptions and scope
The coefficient field is any perfect extension of \(\mathbb F_5\), and geometric assertions are taken over its algebraic closure. The displayed sextic has constant coefficient and leading coefficient equal to one; the coordinates and the involution \(x\mapsto-x\) are marked. The nonvanishing discriminant condition \(\Delta\ne0\) is essential. At \(\Delta=0\) the indicated plane model is singular and is excluded from all Jacobian-rank claims. Ranks are geometric invariants of the smooth Jacobians. The finite-field census counts ordered pairs \((a,b)\), with no quotient by automorphisms or quadratic twists.

## Proof
**1. Smoothness.** Let \(g(u)=u^3+a u^2+b u+1\); the sextic is \(g(x^2)\). Since the characteristic is odd and \(g(0)=1\), the sextic is squarefree exactly when \(g\) is squarefree. The standard cubic discriminant is \(\Delta\), hence \(U=\{\Delta\ne0\}\). Every such curve has genus two.

**2. Cartier and stable rank.** Write \(f(x)=x^6+a x^4+b x^2+1\) and expand \(f(x)^{(5-1)/2}=f(x)^2=\sum_i c_i x^i\). In the regular-differential basis \(dx/y,x\,dx/y\), the genus-two Cartier--Manin matrix has entries \(c_{5i-j}\) for \(1\le i,j\le2\), up to entrywise fifth roots according to the semilinear convention. Direct multiplication gives
\[
c_4=b^2+2a=H_2,\quad c_3=0,\quad c_9=0,\quad c_8=a^2+2b=H_1.
\]
Thus its matrix is diagonal \(\operatorname{diag}(H_2,H_1)\) (up to entrywise Frobenius inverse). Every nonzero diagonal entry remains nonzero under each Frobenius iterate; therefore the stable Hasse--Witt rank, i.e. the \(5\)-rank, is the number of nonzero entries, and the Cartier cokernel dimension, i.e. the \(a\)-number, is the number of zero entries. At \((0,0)\) the Cartier matrix vanishes, so the genus-two Jacobian is superspecial.

**3. Intersection and boundary.** The equation \(H_1=0\) is the parabola \(b=2a^2\). Substitution into \(H_2\) gives \(4a(a^3-2)\), so the intersections are \((0,0)\) and \((a,2a^2)\) for the three distinct geometric solutions of \(a^3=2\). Direct substitution into the discriminant yields the exact characteristic-five polynomial identity
\[
\Delta(a,2a^2)=2(a^3-2)^2.
\]
Thus only the origin lies in \(U\). For \(a^3=2\), the cubic is the cube \((u-r)^3\), with \(r=a/2\) and \(r^3=-1\). The gradients \((2a,2)\) and \((2,2b)\) of \(H_1,H_2\) have determinant \(4(ab-1)\), equal to \(-4\ne0\) at the origin and \(2\ne0\) at the other three points. All four intersections are transverse. Each Hasse curve is an affine line with the three discriminant points removed, so the smooth nonordinary divisor has exactly two irreducible components with a single normal crossing.

**4. All-extension counting.** For \(q=5^n\), there are \(q^2\) pairs. A singular \(g\) has a unique repeated root \(r\), which must be fixed by Frobenius since it is unique, hence lies in \(\mathbb F_q^\times\). The factorization \(g(u)=(u-r)^2(u+r^{-2})\) determines the pair uniquely from \(r\). Thus exactly \(q-1\) pairs are singular and \(\#U(\mathbb F_q)=q^2-q+1\).

Let \(t_n\) be the number of roots of \(a^3=2\) in \(\mathbb F_q\). Since \(5\equiv-1\pmod3\) and \(2\) has a cube root already in \(\mathbb F_5\), \(t_n=1\) for odd \(n\) and \(t_n=3\) for even \(n\), or \(t_n=2+(-1)^n\). Each Hasse parabola contains \(q\) rational pairs, precisely \(t_n\) of which lie on the discriminant. Their sole intersection in \(U\) is \((0,0)\). Inclusion--exclusion gives
\[
N_0=1,\quad N_1=2(q-t_n-1),\quad
N_2=(q^2-q+1)-N_0-N_1,
\]
which simplifies to the asserted formulas. Finally, exponentiating \(\sum_{n\ge1}N_f(5^n)T^n/n\) proves the three displayed zeta identities.

## Verification
The accompanying standalone `check.py` uses exact polynomial arithmetic modulo five, checks the discriminant restriction identity coefficient by coefficient, constructs \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\) using explicit irreducible polynomials, recomputes the relevant Cartier--Manin coefficients from the sextic square, and enumerates every coefficient pair over each field. It checks the discriminant, intersection, and rank-count formulas independently for these fields. Execute `python3 check.py`. Expected successful final line: `VERIFY_OK`. The algebraic argument above proves the result for all \(n\), independently of these finite experiments.

## Relationship to prior work
Shaska--Völklein established the general genus-two extra-involution normal form and its two elliptic quotient subfields, together with moduli and elliptic \(j\)-invariant formulas. Gutierrez--Shaska developed the analogous normal form and dihedral parameters in general genus. These results explain why this two-dimensional family is natural. Their general elliptic-quotient formulas, together with the classical classification of supersingular elliptic curves in characteristic five, furnish a separate route to individual rank conditions. The present specific statement additionally determines, at the coefficient-scheme level, the four Hasse intersections, which three specialize to singular triple-root cubics, and the exact all-extension marked-point census and zeta functions. Zobernig's small-characteristic genus-two calculations concern the full coarse moduli space by geometric isomorphism class, not this normalized extra-involution coefficient surface. Thus the general results are acknowledged as covering the underlying normal form and Hasse--Witt method; the claimed addition is limited to the explicit geometric boundary and arithmetic stratification given above.

## Limitations
The calculation concerns normalized *marked parameters* only and does not count isomorphism classes, account for stabilizer weighting, or classify all genus-two curves. It excludes the singular discriminant curve. Zeta functions refer to constructible parameter strata, not the Jacobians or the genus-two curves themselves. Prior literature could contain an equivalent specialized arithmetic census not located in the targeted comparison. No independent expert review has been undertaken.

## References
1. T. Shaska and H. Völklein, *Elliptic subfields and automorphisms of genus 2 function fields*, arXiv:math/0107142, first posted 19 July 2001, https://arxiv.org/abs/math/0107142 .
2. J. Gutierrez and T. Shaska, *Hyperelliptic curves with extra involutions*, arXiv:math/0601456, first posted 18 January 2006, https://arxiv.org/abs/math/0601456 .
3. L. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270, first posted 14 November 2021, https://arxiv.org/html/2111.07270v1 .
