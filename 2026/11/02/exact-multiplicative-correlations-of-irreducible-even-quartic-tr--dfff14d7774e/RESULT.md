# Exact multiplicative correlations of irreducible even quartic trinomials

## Finding

Let \(q\) be any odd prime power, and let \(\chi:\mathbb F_q\to\{-1,0,1\}\) denote the quadratic character. Fix \(u,b\in\mathbb F_q^\times\), and define the simultaneous-irreducibility count

\[
C_q(u;b)=\#\{a\in\mathbb F_q:\ X^4+aX^2+b\text{ and }X^4+aX^2+ub\text{ are irreducible in }\mathbb F_q[X]\}.
\]

For \(u\ne1\), define the nonsingular Legendre-type elliptic curve \(E_u:\ y^2=x(1-x)(1-ux)\) and write \(a_q(E_u)=q+1-\#E_u(\mathbb F_q)\). Then the **complete formula, including the diagonal and impossible cases**, is

\[
\boxed{
C_q(u;b)=
\begin{cases}
0,&\chi(b)=1\text{ or }\chi(u)=-1,\\
(q+1)/2,&\chi(b)=-1,\ u=1,\\
(q+1+a_q(E_u))/4,&\chi(b)=-1,\ \chi(u)=1,\ u\ne1.
\end{cases}}
\]

For every nontrivial square \(u\), every nonsquare \(b\) yields at least one common irreducible quartic. The exact total over all nontrivial square multipliers, independent of the chosen nonsquare \(b\), is

\[
\boxed{
\sum_{\substack{u\in\mathbb F_q^\times\\\chi(u)=1,\ u\ne1}}C_q(u;b)=
\begin{cases}
(q^2-2q-7)/8,&q\equiv1\pmod4,\\
(q+1)(q-3)/8,&q\equiv3\pmod4.
\end{cases}}
\]

Equivalently, these elliptic traces satisfy the exact square-parameter first-moment relation

\[
\sum_{\substack{u\in\mathbb F_q^\times\\\chi(u)=1,\ u\ne1}}a_q(E_u)=-1-\chi(-1).
\]

## Assumptions and scope

The finite field has odd characteristic; \(q\) may be a nonprime odd prime power. All coefficients \(a\), including zero, are counted. The fixed constants \(u,b\) are nonzero. In the displayed elliptic formula, \(u\ne1\) ensures three distinct roots of the cubic, so \(E_u\) is nonsingular. The character is defined by \(\chi(0)=0\). The elliptic curve includes its unique point at infinity in \(\#E_u(\mathbb F_q)\). For \(\chi(u)=1\), the curve is isomorphic over \(\mathbb F_q\) to the usual Legendre curve with parameter \(u^{-1}\): its cubic is \(u x(x-1)(x-u^{-1})\), and \(u\) is a square.

This is an exact simultaneous count, not an estimate inferred from independent events. The elliptic deviation is uniformly bounded by \(\lvert a_q(E_u)\rvert\le2\sqrt q\) (Hasse).

## Proof

**1. Single-quartic irreducibility criterion.** Let \(f_{a,b}(X)=X^4+aX^2+b\), and put \(g(Y)=Y^2+aY+b\). If \(g\) is reducible over \(\mathbb F_q\), then \(f_{a,b}=g(X^2)\) is reducible. If \(g\) is irreducible, a root \(\alpha\) lies in \(\mathbb F_{q^2}\), and \(f_{a,b}\) is irreducible over \(\mathbb F_q\) precisely when \(X^2-\alpha\) is irreducible over \(\mathbb F_{q^2}\). The norm \(N_{\mathbb F_{q^2}/\mathbb F_q}(\alpha)=b\), and

\[
\chi_{q^2}(\alpha)=\alpha^{(q^2-1)/2}=N(\alpha)^{(q-1)/2}=\chi(b).
\]

The quadratic discriminant of \(g\) is \(a^2-4b\). Therefore, for all \(a\in\mathbb F_q\) and \(b\ne0\),

\[
\boxed{f_{a,b}\text{ irreducible}\iff\chi(b)=\chi(a^2-4b)=-1.}
\tag{1}
\]

**2. Reduction to a three-character pattern.** If \(\chi(b)=1\), the first quartic is reducible. If \(\chi(u)=-1\), the square classes of \(b\) and \(ub\) differ, so the two quartics cannot both be irreducible. Assume henceforth \(\chi(b)=-1\), \(\chi(u)=1\), and \(u\ne1\). For \(a\ne0\), set \(t=4b/a^2\). It is a nonsquare, and (1) becomes

\[
\chi(t)=\chi(1-t)=\chi(1-ut)=-1.
\tag{2}
\]

Every \(t\) satisfying (2) arises from exactly two nonzero coefficients \(a\), because \(4b/t\) is a nonzero square. At \(a=0\), the conditions in (1) hold exactly when \(\chi(-1)=1\). With \(\varepsilon=\chi(-1)\) and \(N_u\) the number of \(t\) satisfying (2), we have

\[
C_q(u;b)=2N_u+\frac{1+\varepsilon}{2}.
\tag{3}
\]

**3. Exact elliptic evaluation.** When \(\chi(t)=0\), we have \(\chi(1-t)=1\). When \(\chi(1-t)=0\), we have \(\chi(t)=1\). When \(\chi(1-ut)=0\), we have \(t=u^{-1}\) and \(\chi(t)=1\) because \(u\) is square. Hence the product of the three \(1-\chi\) factors vanishes at all exceptional zeros and is exactly eight times the indicator in (2). Thus

\[
8N_u=\sum_{t\in\mathbb F_q}(1-\chi(t))(1-\chi(1-t))(1-\chi(1-ut)).
\tag{4}
\]

Each of the three linear character sums vanishes. For \(u\ne1\) and \(\chi(u)=1\), the standard quadratic-character identity for a squarefree quadratic polynomial \(A t^2+B t+C\) gives a sum of \(-\chi(A)\). Applying it to the three pair products yields

\[
\sum_t\chi(t(1-t))=-\varepsilon,\quad
\sum_t\chi(t(1-ut))=-\varepsilon,\quad
\sum_t\chi((1-t)(1-ut))=-1.
\]

Finally, the cubic-character sum equals \(-a_q(E_u)\), since \(\#E_u(\mathbb F_q)=q+1+\sum_t\chi(t(1-t)(1-ut))\). Expanding (4) therefore gives

\[
8N_u=q-2\varepsilon-1+a_q(E_u).
\]

Substitution into (3) gives \(C_q(u;b)=(q+1+a_q(E_u))/4\). This derivation also proves integrality of the displayed quotient. Hasse's bound implies \(C_q(u;b)\ge(q+1-2\sqrt q)/4=(\sqrt q-1)^2/4>0\).

**4. Diagonal case.** If \(u=1\) and \(\chi(b)=-1\), the polynomial \(a^2-4b\) has no zero and is a squarefree monic quadratic. Thus \(\sum_a\chi(a^2-4b)=-1\), so exactly \((q+1)/2\) values of \(a\) have character \(-1\). Equation (1) proves the remaining case of the formula.

**5. Exact sum over all multipliers.** Fix one nonsquare \(b\) and write \(r_a\) for the number of nonsquares \(c\) making \(f_{a,c}\) irreducible. Let \(m=(q-1)/2\). For \(a\ne0\), the substitution \(t=4c/a^2\) and the same zero-safe two-character indicator show

\[
r_a=\frac14\sum_t(1-\chi(t))(1-\chi(1-t))=\frac{q-\varepsilon}{4}=:r.
\]

For \(a=0\), we have \(r_0=m\) when \(\varepsilon=1\), and \(r_0=0\) otherwise. Each ordered pair of distinct nonsquares \((c,c')\) has a unique nontrivial square ratio \(u=c'/c\). The count \(C_q(u;c)\) is independent of the chosen nonsquare \(c\): if \(c'/c=s^2\), replacing \(a\) by \(sa\) preserves both discriminant square classes. Double counting ordered pairs gives

\[
\sum_{\substack{\chi(u)=1\\u\ne1}} C_q(u;b)
=\frac{\sum_{a\in\mathbb F_q}r_a(r_a-1)}{m}
=2r(r-1)+\frac{1+\varepsilon}{2}(m-1).
\]

Substituting \(r=(q-\varepsilon)/4\) yields the two exact formulas in the Finding. Combining the result with the elliptic individual-count formula, and observing that there are \((q-3)/2\) nontrivial square ratios, gives \(\sum a_q(E_u)=-1-\varepsilon\). This completes the proof.

## Verification

Run `python3 verification/check.py` with the Python standard library. The script creates finite fields of orders \(3,5,7,9,11,13,17,19,23,25,29\), independently decides quartic irreducibility using polynomial arithmetic and the Frobenius criterion \(\gcd(f,X^{q^2}-X)=1\), verifies (1) for each tested pair, and compares the exact character/elliptic formula with direct simultaneous counts for all nonzero \(u,b\) in each field. The recorded run returned `VERIFY_OK`, tested 2,788 ratio/constant pairs, and performed 125,336 irreducibility decisions. These finite checks are independent corroboration, not the proof for arbitrary fields.

## Relationship to prior work

The irreducibility factorization and character-sum components belong to classical finite-field theory. The work of von zur Gathen develops irreducible-trinomial criteria and small-field distributions; Auer and Top develop the Legendre family, including an **unrestricted** first moment of its rational point counts in Proposition 4.1. That proposition is acknowledged as related coverage of elliptic trace averages, but does not count paired irreducible quartics at a prescribed square ratio or state the above square-restricted first moment. Cesaratto–Matera–Pérez provide asymptotic factorization-pattern estimates for different linear families, not the exact correlated constrained pair. Kelley–Owen bound rational roots of trinomials; Ding–Zieve study value sets of the same quartic shape and two-character residue conditions, not its irreducibility or the three-condition intersection. The complete coefficientwise pair-count classification and its local square-ratio interpretation were not located in those inspected sources.

## Limitations

The formula concerns even monic quartics of the displayed shape over fields of odd order. It does not cover characteristic two, arbitrary quartic coefficients, or simultaneous families with independently varying quadratic terms. The use of an elliptic point count is an exact reformulation, not a new algorithm for evaluating general elliptic traces. The identity uses classical character sums; priority remains at risk from unlocated older work on triple quadratic-character patterns or a stronger general specialization. Independent mathematical validation has not been performed.

## References

1. R. Auer and J. Top, *Legendre elliptic curves over finite fields*, arXiv:math/0106273v1 (2001), especially Sections 1, 2 and Proposition 4.1. https://arxiv.org/html/math/0106273v1
2. J. von zur Gathen, *Irreducible trinomials over finite fields*, Math. Comp. 72 (2003), 1987–2000, DOI 10.1090/S0025-5718-03-01515-1. Author's lawful open-access manuscript: https://cosec.bit.uni-bonn.de/fileadmin/user_upload/publications/pubs/gat03a.pdf
3. E. Cesaratto, G. Matera and M. Pérez, *The distribution of factorization patterns on linear families of polynomials over a finite field*, arXiv:1408.7014v1 (2014). https://arxiv.org/html/1408.7014v2
4. Z. Kelley and S. Owen, *Estimating the Number Of Roots of Trinomials over Finite Fields*, arXiv:1510.01758v1 (2015). https://arxiv.org/html/1510.01758v4
5. Z. Ding and M. E. Zieve, *On sums of powers of consecutive squares over finite fields, and sums of distinct values of polynomials*, arXiv:2309.14979v1 (2023). https://arxiv.org/abs/2309.14979
