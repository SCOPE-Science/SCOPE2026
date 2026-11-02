# Uniform local Dold classification for normalized Pell-type traces

## Finding
For every integer \(u\geq1\), define the positive integers \(T_0=1\), \(T_1=u\), and
\[
T_{n+2}=2uT_{n+1}+T_n\qquad(n\geq0).
\]
For any prime \(p\), let \(A^{(p)}_n=p^{\nu_p(T_n)}\) for \(n\geq1\). A sequence \(A\) is **Dold** if \(n\mid\mathcal L_n(A)\) for every \(n\geq1\), where \(\mathcal L_n(A)=\sum_{d\mid n}\mu(n/d)A_d\). Its **repair multiplier** \(F_p(u)\) is the least positive integer \(F\) for which \(F A^{(p)}\) is Dold.

**Theorem.** The repair multiplier exists for all \(u\geq1\) and primes \(p\). At \(p=2\),
\[
F_2(u)=\begin{cases}1,&u\text{ odd},\\2,&u\text{ even}.\end{cases}
\]
For odd \(p\), set \(D=u^2+1\). If \(p\mid D\), then \(F_p(u)=1\). Otherwise, in \(\mathbb F_{p^2}\) let \(\alpha=u+\sqrt D\) and \(x=-\alpha^2\), and put \(m=\operatorname{ord}(x)\). If \(m\) is odd then \(F_p(u)=1\). If \(m\) is even, set \(r=m/2\). Then
\[
\boxed{F_p(u)=\frac{2r}{\gcd(2r,p-1)}.}
\]
In particular, for every odd prime \(p\) the unmodified sequence \(A^{(p)}\) is Dold **if and only if**
\[
\boxed{\text{not}\bigl[p\equiv3\pmod4\ \text{and}\ \left(\frac{u^2+1}{p}\right)=-1\bigr].}
\]
The Dold-good primes have natural density \(3/4\) and the Dold-bad primes density \(1/4\), **for every fixed integer \(u\geq1\)**. The exceptional prime \(2\) is Dold-good precisely when \(u\) is odd.

Moreover the local sequence is (almost) realizable, meaning its Möbius transforms are nonnegative and it is (almost) Dold, precisely if \(p\nmid T_n\) for all \(n\geq1\). When \(p\) divides some \(T_n\), a negative Möbius transform rules out realizability even after multiplication by any positive integer.

## Assumptions and scope
Here \(u\) is any fixed positive integer, \(p\) is any rational prime, \(\nu_p\) is the ordinary nonnegative valuation, \(\mu\) is the number-theoretic Möbius function, and the local sequences are indexed by positive integers. The quadratic roots satisfy \(\alpha=u+\sqrt{u^2+1}\), \(\beta=u-\sqrt{u^2+1}=-\alpha^{-1}\), and
\[
T_n=(\alpha^n+\beta^n)/2.
\]
The radicand \(u^2+1\) is strictly between \(u^2\) and \((u+1)^2\); therefore it is a positive nonsquare integer. The theorem is about these normalized even-trace recurrences, not arbitrary Lucas parameters or the unnormalized classical Lucas sequence.

## Proof
**Odd-prime divisibility.** Fix an odd prime \(p\) and write \(D=u^2+1\). If \(p\mid D\), reduction modulo \(p\) makes both roots equal to \(u\), and \(T_n\equiv u^n\not\equiv0\pmod p\), because \(p\nmid u\). Thus the local sequence is constantly one.

Suppose \(p\nmid D\). The roots are units in the split or unramified quadratic \(p\)-adic algebra. Since \(\beta=-\alpha^{-1}\),
\[
p\mid T_n\ \Longleftrightarrow\ \bigl(-\alpha^2\bigr)^n=-1\text{ in }\mathbb F_{p^2}.
\]
Write \(m=\operatorname{ord}(-\alpha^2)\). The order divides \(p-1\) in the split case, and \(p+1\) in the inert case: in the latter \(\alpha^p=\beta\), so \((-\alpha^2)^{p+1}=1\). Hence \(p\nmid m\). If \(m\) is odd, no term is divisible by \(p\). If \(m=2r\), exactly the indices \(n=rk\) with \(k\) odd are divisible by \(p\), and \(p\nmid2r\). Put \(c=\nu_p(T_r)\geq1\). Standard odd-exponent lifting for a sum of two \(p\)-adic units yields, for every odd \(k\),
\[
\nu_p(T_{rk})=c+\nu_p(k).
\]
Thus the normalized local sequence has the exact pattern
\[
A^{(p)}_n=\begin{cases}p^{c+\nu_p(k)},&n=rk,\ k\text{ odd},\\1,&\text{otherwise}.\end{cases}
\]

**Exact Möbius transform and optimal repair.** Put \(B_n=A^{(p)}_n-1\). For every positive integer \(n\), \(\mathcal L_n(B)\) vanishes unless \(n\) belongs to one of the following four disjoint families:
\[
\begin{array}{c|c}
n&\mathcal L_n(B)\\ \hline
r&p^c-1\\
2r&-(p^c-1)\\
rp^j\ (j\geq1)&p^{c+j-1}(p-1)\\
2rp^j\ (j\geq1)&-p^{c+j-1}(p-1).
\end{array}
\]
This follows directly by Möbius inversion of the indicator of odd multiples of \(r\): on odd quotients, the constant term \(p^c-1\) contributes at quotient one, the \(p\)-valuation term contributes exactly at positive powers of \(p\), and multiplying the quotient by two changes the sign. Terms of the constant-one sequence have zero transform for \(n>1\), so \(\mathcal L_n(A^{(p)})=\mathcal L_n(B)\) for \(n\geq2\). Even when \(r=1\), the difference at \(n=1\) does not affect any Dold divisibility condition.

The denominator of \(\mathcal L_n(A^{(p)})/n\), for every \(n\geq2\), divides \(2r/\gcd(2r,p-1)\): the factors \(p^j\) are absorbed by \(p^{c+j-1}\) since \(c\geq1\). Conversely, the transform at \(2r\) requires \(2r\mid F(p^c-1)\), while the transforms at \(2rp^j\) require \(2r\mid F(p-1)\); these have gcd \(p-1\), because \(\gcd(p^c-1,p-1)=p-1\). Thus the least possible multiplier is exactly \(2r/\gcd(2r,p-1)\). The transform at \(2r\) is \(1-p^c<0\), proving nonrealizability whenever a term is divisible by \(p\).

**Which primes are already Dold?** If \(\left(\frac{D}{p}\right)=1\), then the root ratio lies in \(\mathbb F_p^\times\), so \(m\mid p-1\) and the repair multiplier is one. If the Legendre symbol is zero, all local terms are one, as already shown. Suppose \(\left(\frac{D}{p}\right)=-1\). Frobenius interchanges the roots and \(\alpha^{p+1}=-1\). Therefore
\[
\bigl(-\alpha^2\bigr)^{(p+1)/2}=(-1)^{(p+1)/2+1}.
\]
For \(p\equiv1\pmod4\), the exponent \((p+1)/2\) is odd and the right side is one, so \(m\) is odd and no local term is divisible by \(p\). For \(p\equiv3\pmod4\), the right side is minus one, so \(m\) is even; moreover \(m>2\), since \(m=2\) would force \(\alpha^2=1\), hence \(p\mid u\), contradicting inertness. Since \(m\mid p+1\), \(m>2\), and \(\gcd(p-1,p+1)=2\), \(m\nmid p-1\) and the repair factor is greater than one. This proves the claimed equivalence.

**Density.** The two nontrivial quadratic Dirichlet characters \(p\mapsto(-1/p)\) and \(p\mapsto(D/p)\) are distinct and independent: \(D=u^2+1\) is positive nonsquare, so its quadratic field is real, whereas the field for \((-1/p)\) is imaginary. By orthogonality and Dirichlet's theorem with prime-number-theorem equidistribution for reduced residue classes, each of the four joint signs occurs among primes with density \(1/4\), excluding finitely many ramified primes. Exactly the simultaneous \((-1,-1)\) sign produces Dold-bad primes. Hence their density is \(1/4\), and the good density is \(3/4\).

**The prime two.** Write \(c=\nu_2(u)\) if \(u\) is even. From \(T_{n+2}-T_n=2uT_{n+1}\), all odd-index values satisfy \(T_{2j+1}\equiv u\pmod{2^{c+1}}\), while all even-index values satisfy \(T_{2j}\equiv1\pmod{2^{c+1}}\). Thus for even \(u\), \(A^{(2)}_n=2^c\) at odd indices and one at even indices. Its only Möbius transforms above index one occur at \(n=2\), where \(\mathcal L_2=1-2^c\), an odd negative integer. The optimal repair is therefore two, and almost realizability fails. For odd \(u\), every \(T_n\) is odd, the local sequence is constantly one, and it is Dold and realizable. This proves all assertions.

## Verification
The self-contained `verify.py` checks the defining integer recurrence, exact p-parts, Dold Möbius sums, their minimal repair denominators, the Legendre-symbol good-prime criterion, predicted support of the nonzero Möbius transforms, and negative realizability witnesses. The reproducible command is `python3 verify.py`. It checks ten parameters and fourteen primes through 43, using every index through 120, for 16,800 exact Möbius computations, without third-party dependencies. These finite tests supplement the infinite proof, rather than establish density or prove all-parameter claims.

## Relationship to prior work
Chuysurichay, Jaidee, Panraksa and Ward (arXiv:2609.24544v1, 21 September 2026) classify local Dold, realizable and repair primes for the **classical** Fibonacci and Lucas sequences. Their explicit prime-rank and Möbius-transform method motivates this investigation, and Section 4 expressly asks how the congruence and sign arguments extend to general companion Lucas sequences. They do not state the result for the normalized Pell-type family \(T_n\) with parameter \(2u\), and in particular do not give its uniform-in-parameter quadratic-character bad-prime criterion or its density \(1/4\).

The published finding *All local prime parts are Dold for split companion Lucas sequences* proves a different statement for **positive square discriminant**, i.e. integral roots. Here the discriminant \(4(u^2+1)\) is **always nonsquare** and there are genuinely inert primes, exactly accounting for the nontrivial bad-prime density. A separate published finding about even-parameter Lucas period equality concerns a different invariant and does not imply the local Dold classification. Standard lifting-the-exponent lemmas and quadratic character orthogonality are used, not claimed as new.

## Limitations
This theorem treats the entire normalized even-parameter Pell-type trace family for positive integer \(u\), but does not classify all Lucas pairs \((P,Q)\) or calculate the density of the local realizability primes. The numerical verifier has a finite scope; the density proof uses standard prime-equidistribution theory. Prior art may contain implicit specializations of broader results, so bibliographic priority is not independently certified.

## References
1. S. Chuysurichay, S. Jaidee, C. Panraksa and T. Ward, *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (first posted 21 September 2026), https://arxiv.org/abs/2609.24544.
2. *All local prime parts are Dold for split companion Lucas sequences*, published research note (4 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-local-prime-parts-are-dold-for-split-companion-lucas-sequenc--82bcde83c42e.
3. *Even-even period equality for Lucas pairs with \(q=-1\)*, published research note (4 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-even-even-period-equality-for-lucas-pairs-with-q-1--c698969a6a49.
4. J. Byszewski, G. Graff and T. Ward, *Dold sequences, periodic points, and dynamics*, Bull. Lond. Math. Soc. 53 (2021), 1263–1298, DOI 10.1112/blms.12531.
