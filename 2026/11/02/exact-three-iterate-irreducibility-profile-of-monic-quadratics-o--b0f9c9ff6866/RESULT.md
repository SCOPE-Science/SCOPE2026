# Exact three-iterate irreducibility profile of monic quadratics over odd finite fields

## Finding

Let \(q\) be an odd prime power. Write \(N_j(q)\) for the number of monic quadratic polynomials \(f\in\mathbb F_q[X]\) for which \(f,f^{\circ2},\ldots,f^{\circ j}\) are all irreducible over \(\mathbb F_q\). Then

\[
N_1(q)=\frac{q(q-1)}2,\qquad
N_2(q)=\frac{q^2-1}4,\qquad
N_3(q)=\frac{(q-1)(q+2+\chi_q(-1))}8.
\]

Here \(\chi_q\) is the quadratic character of \(\mathbb F_q\), extended by \(\chi_q(0)=0\). Consequently,

\[
N_3(q)=\begin{cases}
(q-1)(q+3)/8,&q\equiv1\pmod4,\\
(q^2-1)/8,&q\equiv3\pmod4.
\end{cases}
\]

In particular, the exact number of monic quadratics whose first two iterates are irreducible but whose third iterate is reducible is \((q-1)(q-\chi_q(-1))/8\). This is a finite-depth statement, not a count of polynomials with all iterates irreducible.

## Assumptions and scope

The field is \(\mathbb F_q\) with \(q\) odd, including nonprime prime powers. Composition is taken over that field, so \(f^{\circ j}\) has degree \(2^j\). Every monic quadratic has a unique representation \(f(X)=(X-a)^2+b\) with \(a,b\in\mathbb F_q\). No condition is imposed on iterations after the third.

## Proof

**1. Reduction to a three-character test.** Let \(f(X)=(X-a)^2+b\). Its discriminant is \(-4b\); hence \(f\) is irreducible exactly when \(\chi_q(-b)=-1\). Suppose \(f^{\circ j}\) is irreducible, for \(j\ge1\), and let \(\alpha\) be one root in the degree-\(2^j\) extension of \(\mathbb F_q\). By Capelli's elementary composition criterion, \(f^{\circ(j+1)}=f^{\circ j}(f(X))\) is irreducible if and only if \(f(X)-\alpha=(X-a)^2+(b-\alpha)\) is irreducible over this extension. This happens precisely when \(\alpha-b\) is a nonsquare. Its field norm is \(f^{\circ j}(b)\): indeed the minimal polynomial of \(\alpha\) has even degree \(2^j\), and the product of its conjugate differences \(\alpha'-b\) equals \(f^{\circ j}(b)\). Over finite fields, the quadratic character of an element agrees with the base-field quadratic character of its norm. Thus the first three iterates are irreducible precisely when

\[
\chi_q(-b)=\chi_q(f(b))=\chi_q(f^{\circ2}(b))=-1.
\]

**2. First two counts.** There are \((q-1)/2\) admissible nonzero values of \(b\), and any \(a\) is allowed for the first test: \(N_1=q(q-1)/2\). Put \(t=b-a\), so \(f(b)=b+t^2\). For each admissible \(b\), \(-b\) is a nonsquare and the equation \(t^2+b=0\) has no solution. The standard quadratic-character identity \(\sum_{t\in\mathbb F_q}\chi_q(t^2+b)=-1\) for \(b\ne0\) implies exactly \((q+1)/2\) values of \(t\) make \(\chi_q(t^2+b)=-1\). Hence \(N_2=(q^2-1)/4\).

**3. Three simultaneous characters.** Write \(e=\chi_q(-1)\) and \(s=-e\). Set \(x=b\), \(t=b-a\), and

\[
A=x,\quad B=x+t^2,\quad C=x+t^2(t+1)^2.
\]

These equal \(b\), \(f(b)\), and \(f^{\circ2}(b)\), respectively. The three requirements are \(\chi_q(A)=s\), \(\chi_q(B)=\chi_q(C)=-1\). Define

\[
W(t,x)=(1+s\chi_q(A))(1-\chi_q(B))(1-\chi_q(C)).
\]

This expression is eight exactly at admissible pairs and zero at all other pairs, except \((t,x)=(0,0)\), where it is one. To check the zero cases: if \(A=0\) and \(t\ne0\), then \(B=t^2\) is a square; if \(B=0\) and \(t\ne0\), then \(A=-t^2\) has character \(e\); if \(C=0\) and \(t\ne0,-1\), then \(A=-t^2(t+1)^2\) has character \(e\); and if \(t=-1,C=0\), then \(B=1\). Each forces a zero factor. For \(t=0\), the only remaining zero case is \(x=0\). Therefore

\[
8N_3(q)=\sum_{t,x\in\mathbb F_q}W(t,x)-1.
\]

**4. Exact pair sums.** For \(u\ne v\), the character identity \(\sum_x\chi_q((x+u)(x+v))=-1\) follows by translating and applying the previous quadratic-character sum. For \(u=v\), the sum is \(q-1\). Applying this with the respective shifts of \(A,B,C\) gives

\[
S_{AB}:=\sum_{t,x}\chi_q(AB)=0,\qquad
S_{AC}:=\sum_{t,x}\chi_q(AC)=q,\qquad
S_{BC}:=\sum_{t,x}\chi_q(BC)=q.
\]

For \(AB\), the shifts coincide only at \(t=0\), so the sum is \((q-1)-(q-1)=0\). For \(AC\), they coincide at \(t=0,-1\), giving \(2(q-1)-(q-2)=q\). For \(BC\), the difference of shifts is \(t^3(t+2)\), vanishing at the two distinct points \(t=0,-2\) in every odd characteristic, again giving \(q\).

**5. Exact triple sum.** Set \(T=\sum_{t,x}\chi_q(ABC)\). At \(t=0\), the summand is \(\chi_q(x^3)=\chi_q(x)\) and sums to zero. For \(t\ne0\), write \(x=t^2z\), \(u=t+1\); even powers of \(t\) disappear under \(\chi_q\). Thus

\[
T=\sum_{u\ne1}\sum_z\chi_q\bigl(z(z+1)(z+u^2)\bigr).
\]

Adding the missing \(u=1\) term and subtracting it yields a correction of \(e\), because \(\sum_z\chi_q(z(z+1)^2)=-e\). Reversing the remaining summations,

\[
T=\sum_z\chi_q(z(z+1))\sum_u\chi_q(u^2+z)+e.
\]

The \(z=0\) contribution vanishes, while for every \(z\ne0\), \(\sum_u\chi_q(u^2+z)=-1\). Since \(\sum_z\chi_q(z(z+1))=-1\), this proves \(T=1+e\).

**6. Finish.** Expand the three factors defining \(W\). All single-character sums vanish because, at fixed \(t\), each argument is affine in \(x\). Therefore

\[
\sum_{t,x}W(t,x)
=q^2-sS_{AB}-sS_{AC}+S_{BC}+sT
=q^2+(q-1)(1+e).
\]

Subtract the single zero correction and divide by eight to obtain

\[
N_3(q)=\frac{q^2-1+(q-1)(1+e)}8
=\frac{(q-1)(q+2+e)}8.
\]

This proves the theorem for all odd prime powers without relying on a finite enumeration.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3, without external packages. The provided checker enumerates all \(q^2\) monic quadratic coefficients for ten prime fields and four nonprime fields, verifies every displayed count and all relevant character-correlation sums, and separately uses polynomial gcd tests to verify irreducibility of the degree-two, four, and eight iterates for the prime fields of orders \(3,5,7,11\). It returned \(\texttt{VERIFY\_OK}\) on 14 fields and 7,190 coefficient pairs. The finite tests are corroboration, not a proof of the universal formulas.

## Relationship to prior work

Gómez-Pérez, Nicolás, Ostafe and Sadornil (2012 preprint; 2014 journal article) establish a general stability criterion and estimates for polynomials whose **every** iterate is irreducible. Gómez-Pérez and Nicolás (2010) give lower and upper bounds for indefinitely stable quadratic polynomials with arbitrary nonzero leading coefficient; these bounds do not determine the exact monic three-iterate count. Göksel, Xia and Boston (2013) study factorization patterns for iterates of a fixed quadratic through probabilistic models, not the exact count of monic quadratics satisfying all three initial irreducibility tests. Jones and Boston (2012) investigate settled polynomials and are a residual comparison risk because their full article was not accessible in this review. None of the materially inspected primary results supplies or logically implies the three-stage formula for every odd prime power.

## Limitations

No count is claimed for the fourth or later iterates, for characteristic two, or for nonmonic quadratics. Finite-stage irreducibility must not be confused with dynamical irreducibility of all iterates. There remains a literature-coverage risk that an equivalent formula is hidden in uninspected historical text, in particular the unavailable full text of Jones and Boston. No independent audit has been performed.

## References

1. D. Gómez-Pérez, A. P. Nicolás, A. Ostafe and D. Sadornil, *Stable Polynomials over Finite Fields*, arXiv:1206.4979v1 (public 21 June 2012); Rev. Mat. Iberoam. 30 (2014), 523–535. https://arxiv.org/abs/1206.4979
2. D. Gómez-Pérez and A. P. Nicolás, *An estimate on the number of stable quadratic polynomials*, Finite Fields Appl. 16 (2010), 401–405, DOI:10.1016/j.ffa.2010.06.005. Author manuscript: https://personales.unican.es/gomezd/Articles/Nicolas/critical-orbits.pdf
3. V. Göksel, S. Xia and N. Boston, *A refined conjecture for factoring iterates of quadratic polynomials over finite fields*, arXiv:1312.6767v2 (2013). https://arxiv.org/abs/1312.6767
4. R. Jones and N. Boston, *Settled polynomials over finite fields*, Proc. Amer. Math. Soc. 140 (2012), 1849–1864. DOI:10.1090/S0002-9939-2011-11054-2.
