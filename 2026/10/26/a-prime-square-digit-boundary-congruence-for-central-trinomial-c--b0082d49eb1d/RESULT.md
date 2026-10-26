# A prime-square digit-boundary congruence for central trinomial coefficients

## Finding

Define the central trinomial coefficients by
\[
T_n=\operatorname{CT}_{x}(1+x+x^{-1})^n
=\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n}{2j}\binom{2j}{j},\qquad n\ge0.
\]
Let \(p\ge5\) be prime, let \(m\ge1\) be an integer, and put \(\varepsilon_p=1\) for \(p\equiv1\pmod3\) and \(\varepsilon_p=-1\) for \(p\equiv2\pmod3\). Then the precise first-order digit-boundary identity is
\[
T_{pm-1}\equiv
\bigl[\varepsilon_p+m(T_{p-1}-\varepsilon_p)\bigr]T_{m-1}
\pmod{p^2}.
\tag{1}
\]
Using the established prime-index congruence of Cao and Sun [1] gives the explicit uniform evaluation
\[
\boxed{T_{pm-1}\equiv
\varepsilon_p\,3^{m(p-1)}T_{m-1}\pmod{p^2}.}
\tag{2}
\]
In particular, for every integer \(r\ge1\), iteration gives
\[
T_{p^r-1}\equiv\varepsilon_p^{\,r}3^{p^r-1}\pmod{p^2}.
\tag{3}
\]
The three congruences constitute a single prime-square digit-boundary theorem and its consequence.

## Assumptions and scope

All coefficients are ordinary integers. Congruences are in \(\mathbb Z/p^2\mathbb Z\); no invertibility assumption on \(m\) or \(T_{m-1}\) is imposed. The primes \(2\) and \(3\) are excluded because divisibility of the cubic cyclotomic polynomial used below requires \(p\ne3\), and the cited base-index evaluation assumes \(p>3\). The statement does not assert a congruence modulo \(p^3\), nor one for arbitrary indices outside the residue class \(-1\pmod p\).

## Proof

Set \(Q(x)=1+x+x^{-1}\) and work in the integral Laurent polynomial ring \(R=\mathbb Z[x,x^{-1}]\). For \(p\ne3\), every primitive cubic root \(\omega\) is mapped by \(\omega\mapsto\omega^p\) to another primitive cubic root. Consequently \(1+x+x^2\) divides \(1+x^p+x^{2p}\) over \(\mathbb Z[x]\), and
\[
B_p(x):=\frac{Q(x^p)}{Q(x)}
=x^{1-p}\frac{1+x^p+x^{2p}}{1+x+x^2}\in R.
\]
Its Laurent support lies in \([-(p-1),p-1]\), and both endpoint coefficients are \(1\). Its constant term is the coefficient of \(x^{p-1}\) in the polynomial quotient. Since \(p-1<p\), that coefficient equals the coefficient of \(x^{p-1}\) in
\[
\frac1{1+x+x^2}=\frac{1-x}{1-x^3}
=\sum_{h\ge0}(x^{3h}-x^{3h+1}),
\]
which is \(\varepsilon_p\). Thus \(\operatorname{CT}B_p=\varepsilon_p\).

The freshman's-dream congruence \(Q(x)^p\equiv Q(x^p)\pmod p\) implies
\[
Q(x)\bigl(Q(x)^{p-1}-B_p(x)\bigr)\equiv0\pmod p.
\]
The ring \(\mathbb F_p[x,x^{-1}]\) is an integral domain, hence
\[
A_p(x):=\frac{Q(x)^{p-1}-B_p(x)}p\in R.
\]
The Laurent support of \(A_p\) is contained in \([-(p-2),p-2]\): both terms before subtraction have support in \([-(p-1),p-1]\), and their two extreme coefficients agree and cancel. Taking constant terms gives
\[
p\operatorname{CT}A_p=T_{p-1}-\varepsilon_p.
\tag{4}
\]
By construction, \(Q(x)^p=Q(x^p)+pQ(x)A_p(x)\). Raise this exact identity to the \(m\)-th power and divide its exact binomial expansion by \(Q(x)\). Each term is still a Laurent polynomial: the term with zero factors \(pQA_p\) contains \(Q(x^p)=QB_p\), and every other term contains at least one explicit factor \(Q\). After the division, terms with at least two factors of \(p\) remain divisible by \(p^2\), giving
\[
Q(x)^{pm-1}\equiv
B_p(x)Q(x^p)^{m-1}+mpA_p(x)Q(x^p)^{m-1}
\pmod{p^2}.
\tag{5}
\]
This division is legitimate without inverting \(Q(x)\): the initial term has the factor \(Q(x^p)=Q(x)B_p(x)\), and the second term visibly has a factor \(Q(x)\). Every monomial of \(Q(x^p)^{m-1}\) has an exponent divisible by \(p\). The exponents of \(B_p\) and \(A_p\) are both strictly between \(-p\) and \(p\), so a product on the right side of (5) has exponent zero only when each factor separately has exponent zero. Consequently
\[
T_{pm-1}=\operatorname{CT}Q(x)^{pm-1}
\equiv \bigl(\operatorname{CT}B_p+mp\operatorname{CT}A_p\bigr)
\operatorname{CT}Q(x^p)^{m-1}
\pmod{p^2}.
\]
Using \(\operatorname{CT}Q(x^p)^{m-1}=T_{m-1}\) and (4) yields (1) for every \(m\ge1\).

Cao and Sun [1, Theorem 1.1(i)] proved
\[
T_{p-1}\equiv\varepsilon_p3^{p-1}\pmod{p^2}.
\]
Fermat's theorem gives \(3^{p-1}\equiv1\pmod p\). Therefore the binomial expansion yields
\[
3^{m(p-1)}=(3^{p-1})^m
\equiv1+m(3^{p-1}-1)\pmod{p^2}
\]
for every integer \(m\ge1\), proving (2). Finally, substitute \(m=p^{r-1}\) in (2), and iterate for \(r-1,r-2,\dots,1\). The signs multiply to \(\varepsilon_p^r\) and the exponents add as
\[
(p-1)(1+p+\cdots+p^{r-1})=p^r-1,
\]
giving (3). \(\square\)

## Verification

The proof is algebraic for all primes \(p\ge5\) and integers \(m\ge1\); finite checks are not a substitute for it. The standalone \(\texttt{verify.py}\) uses the exact integral recurrence
\[
nT_n=(2n-1)T_{n-1}+3(n-1)T_{n-2},\quad T_0=T_1=1,
\]
with integral division and checks (1) and (2) for \(p\in\{5,7,11,13,17,19,23,29,31,37,41,43\}\) and \(1\le m\le31\). It separately checks prime-power cases of (3), including \(p=5,7,11,13\) and every \(r\le3\) whose index is in the computed range. This checks \(372\) prime/multiplier pairs, as well as the iterated cases. Reproduce with \(\texttt{python3 verify.py}\); a successful run prints \(\texttt{VERIFY_OK}\).

## Relationship to prior work

Cao and Sun [1, Theorem 1.1(i)] evaluated only the isolated base index \(T_{p-1}\) modulo \(p^2\), now recovered by (2) with \(m=1\). Equations (1) and (2) describe the entire infinite family \(T_{pm-1}\), including multipliers divisible by \(p\), through a cyclotomic-quotient support argument. Sun [2] gives systematic congruences for generalized central trinomial coefficients but the checked theorem statements concern different sums and indices. Mellit and Vlasenko [3, Theorem 1 and Eq. (3)] establish general constant-term congruences and a modulo-\(p\) digit-factor relation, but the statements checked do not give this explicit modulo-\(p^2\) value along the \(-1\pmod p\) index class. Pan and Sun [4, Theorem 1.1] prove substantially stronger prime-adic congruences for the different indices \(T_{pn}-T_n\), not the individual boundary terms \(T_{pn-1}\). The exact congruence here was not located by the targeted source and database comparisons; failure to locate a result does not establish exhaustive novelty.

## Limitations

The structural lifting identity (1) relies on the special cubic-cyclotomic quotient of \(Q\); it is not claimed for arbitrary Laurent polynomials or primes \(2,3\). The explicit value (2) depends on the published base-index congruence [1]. The result does not determine residues modulo \(p^3\), nor give a complete residue classification for all trinomial indices. An unindexed or differently normalized existing formula could in principle subsume this identity; no independent literature audit has been performed.

## References

[1] H.-Q. Cao and Z.-W. Sun, *Some congruences involving binomial coefficients*, Colloquium Mathematicum 139 (2015), 127–136; arXiv:1006.3069 (first posted 2010-06-15); DOI: 10.4064/cm139-1-8. Theorem 1.1(i).

[2] Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, Science China Mathematics 57 (2014), 1375–1400; arXiv:1008.3887 (first posted 2010-08-23).

[3] A. Mellit and M. Vlasenko, *Dwork's congruences for the constant terms of powers of a Laurent polynomial*, International Journal of Number Theory 12 (2016), 313–321; arXiv:1306.5811 (first posted 2013-06-24). Theorem 1 and Eq. (3).

[4] H. Pan and Z.-W. Sun, *Supercongruences for central trinomial coefficients*, arXiv:2012.05121 (2020); subsequently published in 2026. Theorem 1.1.
