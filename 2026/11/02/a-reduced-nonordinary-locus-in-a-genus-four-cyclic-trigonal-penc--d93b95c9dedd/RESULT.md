# A reduced nonordinary locus in a genus-four cyclic trigonal pencil for \(p\equiv1\pmod3\)

## Finding

**Theorem.** Let \(p\ge7\) be prime with \(p\equiv1\pmod3\), let \(k=\overline{\mathbb F}_p\), and consider the smooth projective model of
\[
C_a:\quad y^3=x^6+a x^3+1,\qquad a\in k,\quad a^2\ne4.
\]
Put \(r=(p-1)/3\), \(m=r/2=(p-1)/6\), and
\[
H_r(a)=[t^r](t^2+at+1)^r
=\sum_{j=0}^{\lfloor r/2\rfloor}\frac{r!}{j!^2(r-2j)!}\,a^{r-2j}\in\mathbb F_p[a].
\]
The Jacobian \(p\)-rank \(f_p(C_a)\) and \(a\)-number \(a(C_a)\) are exactly
\[
(f_p(C_a),a(C_a))=
\begin{cases}
(2,2),&H_r(a)=0,\\
(4,0),&H_r(a)\ne0.
\end{cases}
\]
The polynomial \(H_r\) is monic, separable of degree \(r\), and \(H_r(2)H_r(-2)\ne0\). Consequently the smooth pencil has precisely \((p-1)/3\) geometric nonordinary **marked parameters**, all reduced; its Jacobian never has rank zero, one, or three.

The order-three quotient induced by \(x\mapsto\zeta_3 x\) is the elliptic curve \(D_a:y^3=t^2+at+1\) with \(t=x^3\). Its Jacobian is ordinary for every smooth parameter. The connected Prym threefold of \(C_a\to D_a\) has \(p\)-rank \(1\) and \(a\)-number \(2\) at the exceptional parameters and \(p\)-rank \(3\) and \(a\)-number \(0\) elsewhere. The parameter counts are not asserted to be counts of geometric isomorphism classes.

## Assumptions and scope

All fields and ranks in the theorem are geometric; the base field is algebraically closed of prime characteristic \(p\equiv1\pmod3\). Since the derivative of \(x^6+ax^3+1\) has a common root with that polynomial precisely when \(a^2=4\), the stated domain is exactly its squarefree locus. It has six distinct finite branch points for the tame cyclic triple cover of \(\mathbb P^1_x\), unramified at infinity. Riemann–Hurwitz gives \(2g-2=-6+6\cdot2=6\), so \(g(C_a)=4\).

The \(p\)-rank is the stable rank of Cartier/Frobenius on the genus-four Hodge space, and the \(a\)-number is \(4-\operatorname{rank}(\mathcal C)\). Cartier is \(p^{-1}\)-semilinear. When its coefficient matrix is diagonal, its stable rank is simply the number of nonzero diagonal entries.

## Proof

**1. Cartier basis and coefficients.** Write \(g(t)=1+at+t^2\), so the equation is \(y^3=g(x^3)\). A basis of holomorphic differentials is
\[
\omega_1=dx/y,\quad\omega_2=dx/y^2,\quad
\omega_3=x\,dx/y^2,\quad\omega_4=x^2\,dx/y^2.
\]
At a finite simple branch point \(y\) is a uniformizer and \(dx\) vanishes to order two; at each of the three unramified points at infinity, \(x\) and \(y\) have pole orders one and two. These facts verify regularity of the displayed independent forms, and Riemann–Hurwitz proves completeness.

For \(j=1,2\), write \(q_j=j(p-1)/3=jr\). The elementary Cartier coefficient rule applied to
\(x^i g(x^3)^{q_j}dx/y^{pj}\) shows that the matrix of \(\mathcal C\), up to applying the field's inverse Frobenius to each coefficient, is
\[
\operatorname{diag}(A,B,C,B),\qquad
A=[t^r]g(t)^r=H_r(a),\quad
B=[t^r]g(t)^{2r},\quad
C=[t^{2r}]g(t)^{2r}.
\]
Indeed the coefficient contributing from input \(x^i dx/y^j\) to output \(x^s dx/y^j\) is that of \(x^{p(s+1)-1-i}\) in \(g(x^3)^{jr}\). Since \(p\equiv1\pmod3\), it can be nonzero only when \(s\equiv i\pmod3\). All allowed indices lie in \(\{0,1,2\}\) (or just \(\{0\}\) for \(j=1\)), hence the matrix is diagonal. Palindromicity of \(g^{2r}\) makes the first and last \(j=2\) entries equal.

**2. Two coefficient identities.** Put \(p=6m+1\), so \(r=2m\) and \(2r=4m\). In \(\mathbb F_p[a]\), the following identities hold:
\[
B=\binom{4m}{2m}(a^2-4)^m,\qquad
C=(a^2-4)^m H_r(a).
\]
For the first identity, the coefficient of \(a^{2m-2j}\) in \(B\) is
\[
\beta_j=\frac{(4m)!}{j!(2m-2j)!(2m+j)!},\qquad0\le j\le m.
\]
Its consecutive ratio equals \(-4(m-j)/(j+1)\) modulo \(p\), since
\(2m-2j-1\equiv-2(2m+j+1)\pmod p\). These are exactly the coefficient ratios of \((a^2-4)^m\), starting from \(\beta_0=\binom{4m}{2m}\). All denominators are nonzero modulo \(p\), and the scalar is a unit.

For the second identity, define over the integers
\(H_n(a)=[t^n](t^2+at+1)^n\). Direct differentiation of its multinomial sum gives
\[
L_n(H_n)=0,\qquad
L_n(F)=(a^2-4)F''+(1-2n)aF'+n^2F.
\]
Set \(\Delta=a^2-4\). Applying \(L_{2r}\) to \(\Delta^{r/2}H_r\), using \(L_r(H_r)=0\), gives the *integer polynomial identity*
\[
L_{2r}(\Delta^{r/2}H_r)
=-4r(1+3r)\Delta^{r/2-1}H_r.
\]
Since \(1+3r=p\), the right side vanishes modulo \(p\). Thus \(\Delta^{r/2}H_r\) and \(H_{2r}=C\) both solve \(L_{2r}(F)=0\) over \(\mathbb F_p\). They are even polynomials of degree \(2r<p\) with nonzero constant terms: respectively \((-4)^{r/2}\binom r{r/2}\) and \(\binom{2r}{r}\). At \(a=0\) the leading ODE coefficient is \(-4\ne0\), so among such even polynomials solutions are determined up to scale by their value at zero (Taylor recursion uses only integers less than \(p\)). The two monic polynomials are therefore identical: \(C=\Delta^{r/2}H_r\).

**3. Rank and reduced exceptional divisor.** On the smooth locus \(\Delta\ne0\), the formula for \(B\) shows that both copies of \(B\) are nonzero. Moreover \(C\) vanishes precisely when \(A=H_r\) vanishes. Thus the diagonal Cartier operator has rank four outside \(H_r=0\), and rank two on that locus. Every diagonal nonzero component remains nonzero under arbitrary Frobenius-semilinear iteration, whereas zero components stay zero. The stable ranks are consequently four and two, respectively, proving both invariants.

The defining multinomial sum makes \(H_r\) monic of degree \(r\). At \(a=\pm2\), the quadratic \(g(t)\) is a square, hence \(H_r(\pm2)=\binom{2r}{r}(\pm1)^r\ne0\) because \(2r<p\). If a root away from \(a=\pm2\) were multiple, \(H_r=H_r'=0\) there. The differential equation \(L_r(H_r)=0\) would successively force all derivatives through order \(r\) to vanish, a contradiction since \(r!\ne0\pmod p\). Hence \(H_r\) has exactly \(r\) simple geometric roots, none singular.

**4. Quotient and Prym.** Taking the invariant \(t=x^3\) under the order-three automorphism yields the smooth genus-one quotient \(D_a:y^3=t^2+at+1\). Its differential \(dt/y^2\) pulls back (up to the nonzero scalar three) to \(x^2dx/y^2=\omega_4\), whose Cartier coefficient is \(B\ne0\). Thus \(D_a\) is ordinary. The standard quotient-norm decomposition \(\operatorname{Jac}(C_a)\sim\operatorname{Jac}(D_a)\times P_a\) has kernel killed by a power of three. Because \(p\ne3\), it preserves \(p\)-divisible groups and hence both invariants. Subtracting the ordinary elliptic factor gives the stated invariants of the Prym threefold.

## Verification

Run `python3 verify_coefficients.py` and `python3 verify_cartier.py` in this directory with a standard Python 3 interpreter. The first program independently evaluates multinomial coefficients modulo thirteen primes \(p\in\{7,13,19,31,37,43,61,67,73,79,97,103,109\}\), checking the two coefficient identities, simplicity, and exclusion of the singular boundary. The second constructs the Cartier matrix directly from monomials of \((x^6+ax^3+1)^{jr}\) and checks all smooth prime-field parameter values for \(p\in\{7,13,19,31,37,43\}\).

The recorded successful terminal markers are `COEFFICIENT_IDENTITIES_OK` and `CARTIER_EXTRACTION_OK`. These finite tests are supplementary; the characteristic-uniform proof is the symbolic coefficient and differential-equation argument above. For example, \(H_2(a)=a^2+2\) in characteristic seven has two exceptional geometric roots and none rational over \(\mathbb F_7\); in characteristic thirteen, \(H_4(a)=(a^2-9)(a^2-5)\) has two rational exceptional parameters and two conjugate parameters of degree two.

## Relationship to prior work

The classical Cartier method, and the distinction between Cartier and Hasse–Witt semilinear iteration, are treated by Achter–Howe (arXiv:1710.10726). Obus–Shaska (arXiv:2006.12685) classifies superelliptic curves with many automorphisms over characteristic zero and studies CM Jacobians. Kudo (arXiv:1804.09063) constructs a different genus-four complete-intersection curve that is superspecial precisely for primes \(p\equiv2\pmod3\). The exact reduced \((p-1)/3\)-point nonordinary locus in the present varying cyclic trigonal family, its two-component diagonal Cartier degeneration, and its Prym ranks are not stated in those inspected works. The two coefficient identities and reducedness argument give the additional specialization needed here; general Cartier theory alone does not enumerate this divisor.

Targeted record, exact-equation, reciprocal-factor, and related-curve searches did not locate an earlier statement of this classification. This is a best-knowledge originality assessment, not a guarantee of priority. A specialized older treatment of the same pencil or its equivalent branch-point parameterization could still cover this theorem.

## Limitations

The theorem covers only primes \(p\equiv1\pmod3\), not primes \(p\equiv2\pmod3\), and only the smooth coefficient-marked family. It does not classify geometric isomorphism classes among parameters, Newton polygons beyond \(p\)-rank, all genus-four curves, or all cyclic trigonal curves. Computations of finitely many primes do not prove uniform identities; those identities are proved independently in the preceding argument. No external independent validation is claimed.

## References

1. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, arXiv:1710.10726 (first public 2017-10-30), especially Sections 1–2; https://arxiv.org/abs/1710.10726.
2. M. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4*, arXiv:1804.09063 (first public 2018-04-24), especially Theorem 3.1; https://arxiv.org/abs/1804.09063.
3. A. Obus and T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685 (first public 2020-06-23), especially Sections 3–5; https://arxiv.org/abs/2006.12685.
