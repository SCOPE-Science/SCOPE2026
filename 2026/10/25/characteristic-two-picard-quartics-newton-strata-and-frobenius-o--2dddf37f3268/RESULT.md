# Characteristic-two Picard quartics: Newton strata and Frobenius-orbit zeta factors

## Finding

**Theorem.** Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(C\) denote the smooth projective model of
\[
 C_{a,b,c,d}:\qquad y^3=x^4+a x^3+b x^2+c x+d,
\]
where \(a,b,c,d\in k\). Set \(\Delta=c^2+abc+a^2d\). The affine equation defines a smooth genus-three Picard curve exactly when \(\Delta\ne0\). For every such curve the Jacobian has \(a\)-number \(1\), and its complete Newton slopes are
\[
\begin{array}{c|c|c}
 &\text{2-rank}&\text{Newton slopes (multiplicities included)}\\
 a=0&0&(\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12)\\
 a\ne0&2&(0,0,\tfrac12,\tfrac12,1,1).
\end{array}
\]
In particular the supersingular coefficient locus is exactly \(a=0,\ c\ne0\), a smooth geometrically irreducible divisor in the smooth-model parameter space.

There is also an **explicit arithmetic factorization** on that divisor. Suppose the coefficients lie in \(\mathbb F_q\), where \(q\) is any power of \(2\), and \(a=0\), \(c\ne0\). Let
\[
 T=\{t\in\overline{\mathbb F}_q:t^4+b t^2+c t=0\}.
\]
Then \(T\) is an elementary abelian four-element additive group. For each \(0\ne t\in T\) put
\[
 E_t:\qquad z^2+\frac ct z=y^3+d.
\]
These are supersingular elliptic curves, and \(C\to E_t\) is the degree-two quotient for the involution \((x,y)\mapsto(x+t,y)\), with \(z=x^2+t x\). Moreover, over the algebraic closure the three quotient maps induce an isogeny
\[
\prod_{t\in T\setminus\{0\}} E_t\ \longrightarrow\ \operatorname{Jac}(C).
\]
Let \(\mathcal O\) range over orbits of \(t\mapsto t^q\) on \(T\setminus\{0\}\). Set \(e_{\mathcal O}=|\mathcal O|\), choose \(t_{\mathcal O}\in\mathcal O\), and define
\[
 u_{\mathcal O}=q^{e_{\mathcal O}}+1-
 \#E_{t_{\mathcal O}}(\mathbb F_{q^{e_{\mathcal O}}}).
\]
Then the complete genus-three Hasse--Weil numerator is
\[
\boxed{\displaystyle L(C/\mathbb F_q,T)=
\prod_{\mathcal O}\left(1-u_{\mathcal O}T^{e_{\mathcal O}}+q^{e_{\mathcal O}}T^{2e_{\mathcal O}}\right).}
\]
This applies even when none of the three nonzero translations is rational over \(\mathbb F_q\); the orbit lengths belong to \(\{1,2,3\}\). Thus the numerator and all extension-field point counts reduce to at most three elliptic-curve point counts over explicitly bounded extensions.

The arithmetic descent types themselves have **exact counts**. Among the \(q(q-1)\) pairs \((b,c)\in\mathbb F_q\times\mathbb F_q^\times\), the cubic \(t^3+bt+c\) has the following splitting types:
\[
\begin{array}{c|c|c}
\text{Frobenius orbit pattern on }T\setminus\{0\}&\text{number of }(b,c)&\text{shape of }L(C/\mathbb F_q,T)\\
(1,1,1)&\frac{(q-1)(q-2)}6&\text{product of three quadratic factors}\\
(1,2)&\frac{q(q-1)}2&\text{quadratic factor times a quartic factor}\\
(3)&\frac{q^2-1}3&\text{one sextic factor of the form }1-uT^3+q^3T^6.
\end{array}
\]
Every choice of \(d\in\mathbb F_q\) leaves the indicated orbit pattern unchanged, so each count is multiplied by \(q\) for complete smooth monic quartic equations. These are **counts of coefficient models, not isomorphism classes**.

## Assumptions and scope

The field \(k\) is algebraically closed of characteristic \(2\) for geometric assertions. The arithmetic formula is over an arbitrary finite field \(\mathbb F_q\) of characteristic \(2\), without assuming that the translation subgroup is rational. The polynomial is monic of degree four. All parameter equalities refer to the displayed affine model; a change of Picard coordinates can alter the coefficients. The moduli-level classification of supersingular nonhyperelliptic genus-three curves and the general decomposition theorem for curves admitting three involutions are prior results, not claims of novelty here.

## Proof

**Smoothness and genus.** In characteristic \(2\), the derivative of the branch polynomial is \(f'(x)=a x^2+c\). If \(a=0\), squarefreeness is equivalent to \(c\ne0\). If \(a\ne0\), the unique critical point \(r\) satisfies \(r^2=c/a\), and
\[
 a^2 f(r)=c^2+abc+a^2d=\Delta.
\]
Thus \(f\) is squarefree precisely when \(\Delta\ne0\). The degree-three tame map \(C\to\mathbb P^1_x\) is branched at the four simple zeros of \(f\) and at infinity, with ramification index three each. Riemann--Hurwitz gives \(2g-2=-6+5\cdot2=4\), so \(g=3\). The unique point above infinity is smooth in the projective quartic model.

**Cartier operator.** A basis of regular differentials is
\[
\omega_0=dx/y^2,\qquad \omega_1=x\,dx/y^2,\qquad \omega_2=dx/y.
\]
The characteristic-two Cartier identities \(\mathcal C(h^2\eta)=h\mathcal C(\eta)\), \(\mathcal C(dx)=0\), and \(\mathcal C(x\,dx)=dx\), together with \(y^3=f(x)\), yield
\[
 \mathcal C(\omega_0)=0,\qquad
 \mathcal C(\omega_1)=\omega_2,\qquad
 \mathcal C(\omega_2)=\sqrt c\,\omega_0+\sqrt a\,\omega_1.
\]
Indeed \(dx/y=f(x)dx/y^4\), and only the coefficients of the odd powers \(x\) and \(x^3\) of \(f\) contribute to \(\mathcal C(f(x)dx)\). The rank of this semilinear operator is always two, proving \(a(C)=g-\operatorname{rank}\mathcal C=1\). If \(a=0\), smoothness gives \(c\ne0\) and \(\mathcal C^3=0\), so the stable rank is zero. If \(a\ne0\), the induced Cartier operator on the two-dimensional quotient by \(k\omega_0\) is invertible; the stable rank is two. Stable Cartier rank equals the Jacobian's \(2\)-rank. When it is two, symmetry of the six Newton slopes and the multiplicity-divisibility constraint on a rational slope force precisely the listed slopes \((0,0,\tfrac12,\tfrac12,1,1)\).

**Additive automorphisms, elliptic quotients and supersingularity.** On \(a=0\) the polynomial \(L(x)=x^4+b x^2+c x\) is additive. As \(c\ne0\), it is separable, so its kernel \(T\) has four elements. For each \(t\in T\) the map \((x,y)\mapsto(x+t,y)\) preserves \(C\). Conversely, if a nonzero translation preserves the displayed equation with \(y\) fixed, the coefficient of \(x^2\) in \(f(x+t)-f(x)\) is \(a t\), so \(a=0\). For \(t\ne0\), \(t^3+b t+c=0\), whence \(b=t^2+c/t\). Setting \(z=x^2+t x\) gives
\[
 z^2+(c/t)z=x^4+b x^2+c x=y^3+d.
\]
The fixed field of \(x\mapsto x+t\) is \(k(z,y)\), hence the quotient is \(E_t\). Because \(c/t\ne0\), the change \(U=(t/c)z\) puts it into the Artin--Schreier form
\[
 U^2+U=(t/c)^2(y^3+d).
\]
This is a smooth genus-one curve with a rational point at infinity and \(j=0\), hence is supersingular in characteristic two.

For any prime \(\ell\ne2\), the \(\ell\)-adic cohomology \(H^1(C,\mathbb Q_\ell)\) is a semisimple \(\mathbb Q_\ell[T]\)-module. Its \(T\)-invariants vanish because \(C/T\cong\mathbb P^1_y\). For each nonzero \(t\), invariants under \(\langle t\rangle\) identify with the two-dimensional \(H^1(E_t,\mathbb Q_\ell)\). The three distinct nontrivial characters of \(T\) therefore each occupy dimension two, filling \(H^1(C,\mathbb Q_\ell)\). The quotient pullbacks induce an isogeny from the product of the three \(E_t\)'s to \(\operatorname{Jac}(C)\), and every Newton slope is \(1/2\). This proves the supersingular part, not just zero \(2\)-rank.

**Frobenius-orbit numerator.** Over \(\mathbb F_q\), Frobenius permutes the three two-dimensional cohomology summands along its orbits on the nonzero translations. For an orbit of size \(e\), the \(e\)-th Frobenius power returns to the chosen summand, where its characteristic polynomial agrees with that of the quotient \(E_t/\mathbb F_{q^e}\), namely \(X^2-u X+q^e\). The determinant of \(1-T\operatorname{Frob}\) on that induced orbit block is therefore \(1-uT^e+q^eT^{2e}\). Multiplication over all orbits proves the formula. The formula is independent of the chosen orbit representative because Frobenius conjugates the corresponding elliptic curves.

**Parameter locus and descent census.** In the smooth parameter space \(U=\operatorname{Spec}k[a,b,c,d,1/\Delta]\), the subscheme \(a=0\) has coordinate ring \(k[b,c,c^{-1},d]\). It is a smooth, geometrically irreducible divisor. For finite \(q\), it contains \(q^2(q-1)\) monic smooth models, while the other Newton stratum contains \(q^2(q-1)^2\); these are counts of equations, not isomorphism classes.

For the displayed splitting-type census, the cubic \(t^3+bt+c\) has separable roots because \(c\ne0\), and its three distinct roots sum to zero. The number of unordered three-element root sets contained in \(\mathbb F_q^\times\) and summing to zero is \((q-1)(q-2)/6\): choose an ordered pair of distinct nonzero elements and divide by the six orderings of its three-element \(\mathbb F_2\)-plane. Every nonzero \(t\in\mathbb F_q\) is a root of exactly \(q-1\) admissible cubics (all \(b\) except \(b=t^2\)). Therefore \((q-1)^2=3N_{111}+N_{12}\) counts rational-root incidences and gives \(N_{12}=q(q-1)/2\). Subtracting these two types from \(q(q-1)\) yields \(N_3=(q^2-1)/3\), as claimed. Thus all three Frobenius descent patterns are classified over every \(q\), not only the rational-involution case.

## Verification

A standalone pure-Python checker, `verify.py`, is provided. It exhaustively tests the smoothness criterion over \(\mathbb F_2\) and \(\mathbb F_4\), computes genus-three degree-six \(L\)-polynomials from point counts of all eight smooth \(\mathbb F_2\)-models, verifies all three arithmetic splitting-type counts for \(q=2,4,8\), and tests the predicted \(2\)-rank. For all four supersingular \(\mathbb F_2\)-models it also independently constructs the Frobenius orbits of three translations inside \(\mathbb F_{64}\), counts points on the elliptic quotients in their minimal fields of definition, and checks the product formula against the directly counted genus-three \(L\)-polynomial. Successful execution prints `VERIFY_OK`. None of these finite tests is used to replace the universal algebraic proof.

For example, the smooth models \(y^3=x^4+x\) and \(y^3=x^4+x+1\) over \(\mathbb F_2\) have numerators \(1+8T^6\) and \(1+4T^2+8T^4+8T^6\), respectively. For \(y^3=x^4+x^2+x\), the three nonzero translations form one Frobenius orbit of length three and the numerator is \(1+8T^6\).

## Relationship to prior work

Nart and Ritzenthaler (arXiv:math/0312366, first circulated December 18, 2003) give a complete geometric and arithmetic classification of characteristic-two nonhyperelliptic genus-three curves, including supersingular moduli strata. They therefore already establish the broad Newton-polygon possibilities; these are not claimed as new. Their 2009 study (arXiv:0905.0546), especially **Proposition 2.5**, states the same elliptic quotient equations for their supersingular normal form; specializing its quadratic-cubic coefficient gives our equation \(E_t\). Thus **the elliptic quotient equations and the geometric product-isogeny mechanism themselves are established prior work, not claimed as new here**. Their statement assumes three roots defined in the ground field. Matsutani--Previato (arXiv:1312.4107) discuss the cyclic trigonal genus-three model and its regular differential basis in characteristic zero.

The narrower result presented here is the **single-coefficient criterion and explicit parameter-space stratification in the monic Picard chart, the exact three-way arithmetic descent census, and the Frobenius-orbit factorization of the complete zeta numerator for every characteristic-two finite field, including nonrational translations**. The elliptic models \(E_t\), the field of definition \(\mathbb F_{q^e}\) of each quotient, and the induced zeta factors are all expressed directly from the original four coefficients. The general moduli-level classification, explicit rational-split elliptic models, and split-Jacobian theorems should not be construed as independent new discoveries in this note.

## Limitations

The result concerns the displayed monic degree-four Picard chart, not arbitrary genus-three curves. Parameter counts count equations rather than isomorphism classes. The formula does not classify all possible isogeny classes or automorphism groups beyond the explicitly exhibited additive subgroup. Prior literature classifying characteristic-two genus-three curves and decompositions is substantially stronger in other directions. An equivalent coefficientwise Frobenius-orbit factorization may exist in older work or in another coordinate system; the cited general papers overlap structurally and independent priority verification has not been performed. The original full text of Bouw's general cyclic-cover \(p\)-rank paper was not available for complete comparison.

## References

1. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (first publicly circulated 2003-12-18). https://arxiv.org/abs/math/0312366
2. E. Nart and C. Ritzenthaler, *Genus 3 curves with many involutions and application to maximal curves in characteristic 2*, arXiv:0905.0546 (2009-05-05). https://arxiv.org/abs/0905.0546
3. S. Matsutani and E. Previato, *The al function of a cyclic trigonal curve of genus three*, arXiv:1312.4107 (2013-12-15). https://arxiv.org/abs/1312.4107
4. W. Castryck, M. Streng and D. Testa, *On the non-existence of certain curves over finite fields*, arXiv:1402.3241 (2014-02-13). https://arxiv.org/abs/1402.3241
5. I. Bouw, *The \(p\)-rank of ramified covers of curves*, DOI:10.1023/A:1017513122376 (general cyclic-cover setting; full text not inspected).
