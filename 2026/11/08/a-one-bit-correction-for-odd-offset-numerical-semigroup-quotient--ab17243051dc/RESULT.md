# A one-bit correction for odd-offset numerical-semigroup quotients

## Finding

Let \(a,p,h,d,k\) be positive integers satisfying \(p\mid a\), \(m=a/p\ge2\), \(\gcd(a,d)=1\), and \(3\le q=2k+1\le a-1\). Write
\[
S=\langle a,\,ha+d,\,ha+3d,\,ha+5d,\ldots,ha+qd\rangle,
\qquad Q=S/p=\{n\ge0:pn\in S\}.
\]
Set
\[
s=\left\lfloor\frac{a-p-1}{q}\right\rfloor,
\qquad t=a-p-sq\in\{1,2,\ldots,q\},
\qquad B=hm\bigl(s+1+\mathbf1_{2\mid t}\bigr)+d(m-1)-m.
\]
Then the Frobenius number of \(Q\) is exactly
\[
\boxed{F(Q)=B+\mathbf1_{\{p\text{ odd},\ t\text{ odd},\ t>p\}}\max\{hm-d,0\}.}
\]
Here \(\mathbf1\) is the indicator, and the Frobenius number means the largest nonnegative integer missing from \(Q\). This formula includes the odd-remainder branch left without an explicit closed Frobenius formula in Theorem 1.6 of Liu's 2023 preprint. It also reproduces the even-remainder formula already given there; only the odd branch is the proposed new contribution.

The correction can be positive and arbitrarily large. For example, \((a,p,h,d,q)=(12,3,2,1,9)\) gives \(B=7\), correction \(7\), and \(F(Q)=14\). The residue attaining the maximum is then the penultimate, not the final, nonzero Apéry residue.

## Assumptions and scope

All generators are positive integers. The hypothesis \(\gcd(a,d)=1\) ensures \(S\) has finite complement; the restriction \(q\le a-1\) is used to prove minimality of its quotient Apéry representatives. We allow \(p=1\), in which case \(Q=S\), and allow arbitrary positive \(h,d\). There is no claim for nondivisor quotients, nonpositive steps, or an arbitrary set of generator offsets.

For \(x\ge0\), let \(\lambda_q(x)\) be the minimum number of summands from \(\{1,3,5,\ldots,q\}\) with sum \(x\), with \(\lambda_q(0)=0\). For \(x\ge1\), write uniquely \(x=uq+v\), where \(u\ge0\) and \(1\le v\le q\). Then
\[
\lambda_q(x)=u+1+\mathbf1_{2\mid v}. \tag{1}
\]
The proof below establishes this formula and directly derives the relevant quotient Apéry set.

## Proof

**1. Odd-coin lengths.** A sum of \(L\) elements of \(\{1,3,\ldots,q\}\) has total between \(L\) and \(qL\) and congruent to \(L\pmod2\). Conversely, every integer in this interval of the same parity can be written as a sum of \(L\) such coins: write it as \(L+2J\), distribute \(J\) among \(L\) places with each place between \(0\) and \((q-1)/2\), and add one to twice each place. Therefore \(\lambda_q(x)\) is the least integer \(L\ge1\) with \(L\le x\le qL\) and \(L\equiv x\pmod2\). For \(x=uq+v\), this is \(u+1\) when \(v\) is odd, and \(u+2\) when \(v\) is even, proving (1).

Two consequences used below are
\[
\lambda_q(x+q)=\lambda_q(x)+1\quad(x\ge0),
\qquad \lambda_q(x+2j)\ge\lambda_q(x)\quad(x,j\ge0). \tag{2}
\]
For the second inequality, if a minimum-length representation of \(x+2\) contains a coin at least three, subtract two from that coin; otherwise all coins are one and a representation of \(x\) has no more coins. Iterate. Equation (1) also gives \(\lambda_q(x+1)\ge\lambda_q(x)-1\). Writing any integer \(a>q\) as \(q+v\) with \(v\ge1\), the preceding inequalities yield
\[
\lambda_q(x+a)=\lambda_q(x+v)+1\ge\lambda_q(x). \tag{3}
\]
For even \(v\) this follows directly from the second inequality in (2), and for odd \(v\) from \(\lambda_q(x+v)\ge\lambda_q(x+1)\ge\lambda_q(x)-1\). Equation (3) remains valid after any number of repetitions of \(a\).

**2. Quotient Apéry representatives.** Because \(m=a/p\) belongs to \(Q\), consider \(\operatorname{Ap}(Q,m)\). Every \(z\in S\) is \(aA+haL+dT\), where \(A,L\ge0\) and \(T\) is a sum of \(L\) odd offsets between 1 and \(q\). Since \(p\mid a\) and \(\gcd(p,d)=1\), membership of \(z=pn\) forces \(p\mid T\). To obtain residue \(dr\pmod m\), with \(0\le r<m\), the nonnegative total offset must be
\[
T=pr+ja\qquad(j\ge0).
\]
For a given \(T\), the smallest corresponding quotient is \(hm\lambda_q(T)+dT/p\), attained with \(A=0\). By (3) this expression is strictly increasing as \(j\) increases, since its second term increases by \(dm>0\). Consequently the Apéry representative in residue \(dr\pmod m\) is
\[
w_{dr}=hm\lambda_q(pr)+dr\qquad(0\le r<m). \tag{4}
\]
The residues \(dr\) are distinct modulo \(m\), because \(\gcd(m,d)=1\). In particular, \(w_0=0\). The standard Apéry identity gives
\[
F(Q)=\max_{1\le r<m}\{hm\lambda_q(pr)+dr\}-m. \tag{5}
\]

**3. Only two candidate residues.** For every \(1\le r\le m-3\), the even-step inequality (2) implies
\[
(hm\lambda_q(p(r+2))+d(r+2))-(hm\lambda_q(pr)+dr)\ge 2d>0.
\]
Thus on each parity of \(r\) the Apéry values increase strictly, and the maximum in (5) is attained at \(r=m-1\) or \(r=m-2\). If \(m=2\), only the first exists and the correction condition below cannot hold.

**4. Evaluate the switch.** Put \(x=a-p=p(m-1)\) and \(y=a-2p=p(m-2)\). The last value in (5), minus \(m\), is precisely \(B\), by (1). If \(p\) is even then \(\lambda_q(y)\le\lambda_q(x)\) by the even-step inequality (2), so the final residue wins. If \(p\) is odd, write \(x=sq+t\), \(1\le t\le q\). When \(p<t\), both \(x\) and \(y=x-p\) occupy the same \(q\)-block; formula (1) gives
\[
\lambda_q(y)-\lambda_q(x)=
\begin{cases}1,&t\text{ odd},\\-1,&t\text{ even}.\end{cases}
\]
When \(p\ge t\), we have \(0\le y\le sq\), so \(\lambda_q(y)\le s+1\le\lambda_q(x)\); this uses (1) and the fact that values below \(sq\) have coin length at most \(s+1\). It follows that \(\lambda_q(y)>\lambda_q(x)\) occurs exactly when \(p\) and \(t\) are odd and \(p<t\), and then the difference is exactly one.

The penultimate Apéry value minus the final one is
\[
hm\bigl(\lambda_q(y)-\lambda_q(x)\bigr)-d.
\]
It is positive only in that exceptional parity case, and then equals \(hm-d\). Taking the maximum of the two candidate values proves the boxed formula. \(\square\)

## Verification

The accompanying `verify_exact.py` computes the theoretical formula using integer arithmetic and independently calculates the complete Apéry set of the original semigroup by Dijkstra shortest paths on residues modulo \(a\). It then extracts the quotient's Frobenius number from those positions that are multiples of \(p\), without using (1) or the two-residue proof. For every \(4\le a<145\), every proper divisor \(p\mid a\), every odd \(3\le q<a\), and every \(h,d\in\{1,2,3\}\) with \(\gcd(a,d)=1\), all 125,586 comparisons agreed. The test includes 73,908 odd-remainder instances and 29,598 instances with a strictly positive correction. The exact program output is in `verification_output.txt`.

This finite test is an independent arithmetic check, not the proof of the assertion for all parameters.

## Relationship to prior work

Feihu Liu's 2023 preprint *On quotients of numerical semigroups for almost arithmetic progressions* (arXiv:2312.06096, first submitted 2023-12-11) proves a quotient-Apéry reduction and, in the proof of Theorem 1.6, gives the odd-coin minimal-cost Apéry coordinates used here. Its displayed Frobenius formula is restricted to an even terminal remainder, and the author explicitly states that an odd terminal remainder is difficult to handle in closed form. The present result is specifically the missing uniform Frobenius evaluation: one last-residue expression plus an explicit, possibly positive, one-bit correction. It does not claim that the general Apéry method or the even-remainder result is new.

Adeniran, Butler, Defant, Gao, Harris, Hettle, Liang, Nam, and Volk, *On the genus of a quotient of a numerical semigroup* (arXiv:1809.09360, first submitted 2018-09-25), study quotient invariants and pose an arithmetic-progression quotient problem. Their full text does not state the odd-offset correction here. The April 2026 paper *The Frobenius problem for a class of quotients of numerical semigroups* (arXiv:2604.26415) treats GCNS offsets satisfying the recursion \(b_{i+1}=s_i b_i+1\) with \(s_i\ge s_{i-1}\ge1\), and its generator coefficients grow with the offsets; the present constant-\(h\) odd offsets do not have that shape. Liu's July 2026 study *On the Frobenius Number of Quotients of Numerical Semigroups* (arXiv:2607.23076) concentrates on two-generated quotients rather than the displayed many-generator family. General semigroup shortest-path and Apéry identities compute these values algorithmically, but the explicit two-candidate reduction and branch rule are additional closed-form information.

## Limitations

The result assumes a divisor \(p\mid a\), a positive step, and \(q<a\). It does not classify pseudo-Frobenius numbers or minimal generators of the quotient. A computational agreement over a finite parameter region does not imply the infinite result without the proof. A later journal version of Liu's paper (2025) was located by bibliographic record but its full text was not separately inspected; it may contain changes relevant to the originality comparison. Other unindexed closed-form specializations are possible. Independent mathematical audit has not been performed.

## References

1. Feihu Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096 (first submitted 2023-12-11), especially Theorem 1.6 and its proof. https://arxiv.org/abs/2312.06096 . Full preprint text inspected at https://www.researchgate.net/publication/403751727_On_quotients_of_numerical_semigroups_for_almost_arithmetic_progressions .
2. A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360 (first submitted 2018-09-25). https://arxiv.org/abs/1809.09360 . Full text inspected at https://www.researchgate.net/publication/327881609_On_the_Genus_of_a_quotient_of_a_numerical_semigroup .
3. Feihu Liu, journal version of reference 1, *International Journal of Algebra and Computation* **35** (2025), 1079–1090, DOI:10.1142/S0218196725500341 (bibliographic abstract examined; journal full text not separately inspected).

4. Feihu Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415 (2026-04-29), especially Definition 1.1 and Sections 2–4. https://arxiv.org/abs/2604.26415 . Full text inspected at https://www.researchgate.net/publication/404308033_The_Frobenius_problem_for_a_class_of_quotients_of_numerical_semigroups .
5. Feihu Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076 (2026-07-28), Theorems 1.2–1.5, https://arxiv.org/abs/2607.23076 . Full text inspected at https://www.researchgate.net/publication/410887700_On_the_Frobenius_Number_of_Quotients_of_Numerical_Semigroups .
