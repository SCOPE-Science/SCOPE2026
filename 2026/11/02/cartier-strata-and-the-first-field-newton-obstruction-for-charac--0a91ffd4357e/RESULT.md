# Cartier strata and the first-field Newton obstruction for characteristic-two cyclic trigonal genus-four curves

## Finding
Let \(k\) be any perfect field of characteristic \(2\). For each squarefree monic quintic \(f\in k[x]\), the smooth projective curve \(C_f:y^3=f(x)\) has genus four and a distinguished totally ramified rational point at infinity. After the unique translation eliminating its fourth-degree coefficient, write
\[
f(x)=x^5+A x^3+B x^2+C x+D.
\]
**The complete geometric \(2\)-rank and \(a\)-number stratification** of this natural family is
\[
a(\operatorname{Jac} C_f)=2,\qquad
f_2(\operatorname{Jac} C_f)=\begin{cases}0&A=0,\\2&A\ne0.\end{cases}
\]
No smooth member is ordinary or superspecial. On the open \(A\ne0\) stratum its Newton slopes are \(0^{\times2},(1/2)^{\times4},1^{\times2}\). No all-field Newton polygon is asserted for \(A=0\).

Over any finite field \(\mathbb F_q\) with \(q=2^m\), the numbers of smooth **marked monic normal-form coefficient quadruples** are exactly
\[
N_{\mathrm{total}}=q^3(q-1),\quad N_{f_2=0}=q^2(q-1),\quad N_{f_2=2}=q^2(q-1)^2.
\]
These count equations rather than isomorphism classes.

There is also a precise first-field obstruction. Over \(\mathbb F_4\), **none** of the \(48\) smooth rank-zero normalized models is supersingular: every one has Newton slopes \((1/4)^{\times4},(3/4)^{\times4}\). The other \(144\) smooth models all have slopes \(0^{\times2},(1/2)^{\times4},1^{\times2}\). There are respectively \(15\) and \(51\) distinct Weil polynomials represented by those two strata. This is a finite, exact statement for the natural monic normal form over \(\mathbb F_4\), **not** a claim that the rank-zero locus has that Newton polygon over every extension or over an algebraic closure.

## Assumptions and scope
All fields have characteristic \(2\). The cover \(y^3=f(x)\) is separable and tame because \(3\) is invertible. A monic degree-five polynomial is assumed squarefree. There are five simple finite branch points and the single branch point at infinity, yielding genus \(4\) by Riemann--Hurwitz. Here \(f_2\) means the geometric \(2\)-rank of the Jacobian, \(a\) the dimension of its \(\alpha_2\)-subgroup, and Newton slopes are normalized by \(v_2(q)\). The monic normal form has its \(x^4\)-coefficient zero and is not a moduli quotient. A nonmonic degree-five model over \(\mathbb F_4\) may be made monic using an \(\mathbb F_4\)-rational scaling of \(x\), and any monic model has a unique translation killing its fourth-degree coefficient.

## Proof
**Normal form and smoothness.** In characteristic two, replacing \(x\) by \(x+\lambda_4\) removes the \(x^4\)-coefficient of a monic quintic. Its \(x^3\)-coefficient \(A\) is unchanged. As every element of a perfect field has a unique square root, write the normalized polynomial uniquely as
\[
f(x)=xg(x)^2+h(x)^2,\quad g=x^2+u x+v,\quad h=w x+z,
\]
so \(A=u^2\), \(B=w^2\), \(C=v^2\), \(D=z^2\). Because \(f'=g^2\), the curve is smooth if and only if \(\gcd(g,h)=1\); infinity is smooth since the degree is five and coprime to three.

**Cartier operator.** A basis for the holomorphic differentials is
\[
\omega_0=dx/y,\quad\omega_1=dx/y^2,\quad
\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2.
\]
The valuations at infinity of these four forms are respectively \(1,6,3,0\); they are independent and their number equals the genus. For the characteristic-two Cartier operator \(\mathcal C\), the rules \(\mathcal C(v^2\eta)=v\mathcal C(\eta)\) and \(\mathcal C(x^{2r+1}dx)=x^r dx\) yield
\[
\mathcal C(\omega_0)=\omega_3+u\omega_2+v\omega_1,\quad
\mathcal C(\omega_1)=0,\quad
\mathcal C(\omega_2)=\omega_0,\quad
\mathcal C(\omega_3)=0.
\]
Indeed, \(dx/y=f\,dx/y^4=(1/y^2)^2 f\,dx\), and \(\mathcal C(f\,dx)=g\,dx\). The Cartier image has dimension exactly \(2\) for all smooth curves, giving \(a=4-2=2\). Its stable semilinear rank is \(2\) if \(u\ne0\): the span of \(\omega_0\) and \(\omega_3+u\omega_2+v\omega_1\) is Cartier-stable with invertible semilinear action. If \(u=0\), the operator is nilpotent, hence the stable rank is \(0\). This proves the geometric \(2\)-rank dichotomy. For rank two, the remaining four slopes form the nonordinary part of an abelian surface; the symmetry of Newton slopes forces all four to equal \(1/2\) (the only slope-zero-rank Newton polygon of an abelian surface).

**Every-field coefficient counts.** Fix \(q=2^m\). If \(w=0\), coprimality holds exactly when \(z\ne0\), giving \(q^2(q-1)\) choices for \((u,v,w,z)\). If \(w\ne0\), its unique root \(r=z/w\) must avoid \(g(r)=0\); for each \(w,r,u\) exactly \(q-1\) values of \(v\) are allowed. This contributes \(q^2(q-1)^2\). Restricting to \(u=0\) gives \(q(q-1)\) choices for \((u,v,w,z)\) when \(w=0\) and \(q(q-1)^2\) when \(w\ne0\), hence \(q^2(q-1)\) total. Subtraction gives the rank-two total. All arguments work for every extension of \(\mathbb F_2\).

**Exact \(\mathbb F_4\) Newton obstruction.** The preceding equations reduce the test to exactly \(48\) smooth quadruples with \(u=0\). For every quadruple, a standalone program enumerates all \(\mathbb F_{4^j}\)-points for \(j=1,2,3,4\) using explicit irreducible binary polynomial representations of the four fields. The four counts determine all coefficients of the degree-eight Weil polynomial by Newton identities and its functional equation. In each of these \(48\) cases, the middle coefficient \(c_4\) satisfies \(c_4\equiv4\pmod 8\), and the lower Newton polygon has vertices \((0,0),(4,2),(8,8)\) in ordinary \(2\)-adic valuations. Normalizing by \(v_2(4)=2\), this gives the asserted slopes \(1/4\) and \(3/4\), each repeated four times. The program separately verifies that the \(144\) rank-two cases have the predicted Newton polygon and counts exactly \(15\) and \(51\) different Weil polynomials. This finite enumeration is exhaustive in the specified normalized parameter set; it does **not** extrapolate to larger coefficient fields.

## Verification
Run the complete standalone standard-library script `python3 verify.py`; its packaged output is in `verification_output.txt`. It checks all \(2^4\) and \(4^4\) normal-form coefficient tuples, the smoothness predicate and ranks, and the exact point counts for every smooth \(\mathbb F_4\) model over the four extensions up to \(\mathbb F_{256}\). Each coefficient is embedded in those fields through a root of \(t^2+t+1\). The corresponding Weil polynomials, their \(2\)-adic Newton hulls, the count of distinct polynomials, and all finite-field census formulas are checked with exact integers. Execution ends with `VERIFY_OK`. The all-field claims are proved symbolically in the preceding paragraphs; the finite script certifies only the finite-field census.

## Relationship to prior work
Baldwin--Eilbeck--Gibbons--Ônishi initiated the full cyclic trigonal \((3,5)\) family and computed holomorphic differentials and complex Abelian functions (arXiv:math/0612654, first posted 21 December 2006). Their treatment is characteristic zero and gives no characteristic-two Cartier stratification. Kudo--Harashita (arXiv:1607.01114) study superspecial genus-four curves in small characteristics, chiefly through canonical complete-intersection models. General trielliptic moduli results of Bouw, and the later work on Newton strata of the special family \(M[10]\) by Li--Mantovan--Pries--Tang and Achter--Pries, establish abstract rank restrictions, generic Newton polygons, and dimensions; they do not give the coefficientwise Cartier criterion, the exact all-\(q\) marked-model counts, or the stated complete \(\mathbb F_4\) obstruction. The 2020 census by Xarles concerns genus-four curves over \(\mathbb F_2\), rather than a census of every marked cyclic trigonal model over \(\mathbb F_4\). The relation to these wider results is explicit; historical priority for the precise finite-field exclusion is provisional.

## Limitations
The point-count obstruction concerns the monic normalized cyclic degree-three polynomial family over \(\mathbb F_4\), with a chosen rational ramification point at infinity, not every genus-four curve or every cyclic triple cover with a nonrational branch divisor. It does not determine the rank-zero Newton polygon over arbitrary perfect characteristic-two fields. Counts are of marked polynomial equations, not distinct isomorphism classes. The exhaustive script is a finite proof of the \(\mathbb F_4\) statements only. Published wider moduli and isogeny classifications may imply portions of the results by additional computation; this historical-priority risk requires independent review.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654v1 (21 December 2006), https://arxiv.org/html/math/0612654v1.
2. M. Kudo, S. Harashita, *Superspecial Curves of Genus 4 in Small Characteristic*, arXiv:1607.01114v1 (5 July 2016), https://arxiv.org/html/1607.01114v2.
3. W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, arXiv:1805.06914 (2018), https://arxiv.org/abs/1805.06914.
4. J. Achter, R. Pries, *The boundary of the \(p\)-rank \(0\) stratum of the moduli space of cyclic covers of the projective line*, Nagoya Mathematical Journal (2022), https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/boundary-of-the-prank-0-stratum-of-the-moduli-space-of-cyclic-covers-of-the-projective-line/02D5FFF8FB89AC671E0F637D48BB1613.
5. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822 (2020), https://arxiv.org/abs/2007.07822.
