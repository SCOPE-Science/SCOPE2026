# A 76.43 percent lower-density certificate for Zumkeller-plus-square sums

## Finding
A positive integer is **Zumkeller** when its positive divisors can be split into two groups with equal sums. Define
\[
\mathcal R=\{N\in\mathbb Z_{>0}:N=z+x^2,\ z\text{ is Zumkeller},\ x\in\mathbb Z_{>0}\}.
\]
Then
\[
\boxed{\liminf_{X\to\infty}\frac{\#(\mathcal R\cap[1,X])}{X}
\ \ge\ \frac{63520442937841228526}{83108492151210387225}
\ =\ 0.7643074888456645\ldots>0.7643.}
\]
This bound is an **exact rational density of an explicit periodic subset** of \(\mathcal R\) outside a finite initial interval. It is not asserted to be the exact density of \(\mathcal R\). Equivalently, the upper asymptotic density of the nonrepresentable integers is at most \(19588049213369158699/83108492151210387225\). The underlying finite-prime sieve is constructed with precisely the ten odd primes \(3,5,7,11,13,17,19,23,29,31\). Every integer in the specified periodic subset that exceeds \(236421376\) has an explicitly constructible positive-square representation.

## Assumptions and scope
All integers and primes below are ordinary positive rational integers; all congruences use the usual integer residue rings. For each odd prime \(p\le31\), put
\[
a(p)=\min\{a\ge1:p\le2^{a+1}-1\},\qquad M_p=2^{a(p)}p^2.
\]
Define \(E_a\) to be the square residues modulo \(2^a\). Define \(G_p\) to be residues \(r\bmod p^2\) admitting an \(x\) for which \(p\mid r-x^2\) and \(p^2\nmid r-x^2\). Define a periodic subset \(\mathcal C\subset\mathbb Z_{>0}\) by the condition that for **at least one** of the ten primes \(p\) both \(N\bmod 2^{a(p)}\in E_{a(p)}\) and \(N\bmod p^2\in G_p\). The membership test for \(\mathcal C\) depends only on \(N\) modulo \(16\prod_{3\le p\le31}p^2\).

## Proof
**1. A source-backed Zumkeller sufficient condition.** Mahanta, Saikia, and Yaqubi, Theorem 2.6, establish that \(2^ap\) is Zumkeller when \(p\le2^{a+1}-1\); see also their Theorem 2.2. Peng and Bhaskara Rao's coprime-multiplier lemma, recalled as Lemma 2.1 by Somu, Kukla, and Tran, establishes that a coprime multiple of a Zumkeller integer remains Zumkeller. Consequently, for every positive \(z\), if \(v_2(z)\ge a(p)\) and \(v_p(z)=1\), then \(z=2^{v_2(z)}p u\) with \(\gcd(u,2p)=1\) is Zumkeller.

**2. Every certified residue yields a positive-square representation.** Suppose \(N\in\mathcal C\), with witness \(p\). There exists \(u\bmod2^{a(p)}\) such that \(u^2\equiv N\pmod{2^{a(p)}}\). By the definition of \(G_p\), there exists \(v\bmod p^2\) with \(v^2\equiv N\pmod p\) but \(v^2\not\equiv N\pmod{p^2}\). The Chinese remainder theorem supplies a positive integer \(x\le M_p\) satisfying \(x\equiv u\pmod{2^{a(p)}}\) and \(x\equiv v\pmod{p^2}\). Therefore \(z=N-x^2\) has \(2^{a(p)}\mid z\) and \(v_p(z)=1\). If \(N>236421376=15376^2\), then \(N>x^2\), because \(M_p\le16\cdot31^2=15376\). By Step 1, \(z\) is a positive Zumkeller number. Thus every sufficiently large member of \(\mathcal C\) belongs to \(\mathcal R\).

**3. Exact local counts.** For odd \(p\), a residue \(r\bmod p^2\) belongs to \(G_p\) precisely if either (i) \(r\not\equiv0\pmod p\) is a quadratic residue modulo \(p\), or (ii) \(p\mid r\) but \(p^2\nmid r\). For (i), lift a nonzero square root \(v\bmod p\) to one of the \(p\) classes modulo \(p^2\); exactly one lift solves \(v^2\equiv r\pmod{p^2}\), so another has valuation exactly one. For (ii), any \(v\equiv0\pmod p\) works. Conversely, if \(p\mid r-v^2\), either \(r\) is a nonzero square residue or both \(r,v\) vanish modulo \(p\), which forces case (ii) when the valuation is exactly one. Hence
\[
|G_p|=\frac{p(p-1)}2+(p-1)=\frac{(p-1)(p+2)}2,\quad
1-\frac{|G_p|}{p^2}=\frac{p^2-p+2}{2p^2}.
\]
For the binary conditions, \(|E_1|/2=1\), \(|E_2|/4=1/2\), \(|E_3|/8=3/8\), and \(|E_4|/16=1/4\); these are nested as conditions on \(N\), since every square modulo a higher power remains a square modulo a lower power.

**4. Exact CRT density.** For integers \(a\in\{1,2,3,4\}\), let
\[
B_a=\prod_{\substack{3\le p\le31\\p\text{ prime},\ a(p)\le a}}
\frac{p^2-p+2}{2p^2}.
\]
Conditional on \(N\bmod16\), good events attached to distinct odd primes are independent under uniform counting on the odd-prime-square CRT coordinates. The failure probabilities on the four disjoint binary strata \(E_1\setminus E_2\), \(E_2\setminus E_3\), \(E_3\setminus E_4\), \(E_4\) are respectively \(B_1,B_2,B_3,B_4\); their binary densities are respectively \(1/2,1/8,1/8,1/4\). Consequently
\[
\operatorname{dens}(\mathcal C)=1-\frac{B_1}{2}-\frac{B_2}{8}-\frac{B_3}{8}-\frac{B_4}{4}.
\]
Explicitly,
\[
B_1=\frac49,\quad B_2=B_1\frac{11}{25}\frac{22}{49},\quad
B_3=B_2\frac{56}{121}\frac{79}{169},
\]
\[
B_4=B_3\frac{137}{289}\frac{172}{361}\frac{254}{529}\frac{407}{841}\frac{466}{961}.
\]
Exact fraction arithmetic gives
\[
\operatorname{dens}(\mathcal C)
=\frac{63520442937841228526}{83108492151210387225}.
\]
Removing finitely many integers does not affect natural density. Since \(\mathcal C\setminus[1,236421376]\subseteq\mathcal R\), the asserted lower asymptotic density follows.

## Verification
The standalone standard-library script `verify.py` independently enumerates every relevant residue modulo \(p^2\) for each of the ten odd primes, confirming \(G_p\) and its closed count. It checks the square-residue recurrence \(\mu_a=1/8+\mu_{a-2}/4\) for \(3\le a\le13\), exact fraction arithmetic for the ten-prime rational value, an exhaustive \(44100\)-residue CRT calculation for the three-prime subcase, and positive CRT square witnesses for fifty sampled local cases. The claimed density and infinite implication are proved above, not inferred from those finite computations. Run: `python3 verify.py`.

## Relationship to prior work
Somu, Kukla, and Tran (2023), Proposition 4.11, show that ten residue classes modulo \(18\) are eventually representable as a Zumkeller number plus a square, establishing the direct lower-density bound \(5/9\). Their Theorem 4.17 proves infinitely many nonrepresentable integers, and Conjecture 4.21 predicts that the exceptional integers nevertheless have density zero. The present explicit \(0.764307\ldots\) bound improves the quantitative \(5/9\) coverage via additional prime-square congruences, without resolving that conjecture. Mahanta, Saikia, and Yaqubi (2020) supply the two-prime divisor criterion used as a premise; their theorem does not give an additive density bound. The prime-square local count, binary stratification, and resulting global rational constant are the contribution here, not the earlier divisor criterion.

## Limitations
The complement of the periodic certificate set may contain representable numbers; the bound is not the exact density of all sums. No density-zero exceptional-set claim is made. The explicit lower bound could be raised by additional primes, and is not optimal. The first publication of the cited 2023 preprint is verified as 2023-10-22. Independent mathematical validation has not been performed.

## References
1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149 (initial public preprint 2023-10-22), Proposition 4.11, Theorem 4.17, Conjecture 4.21, Lemma 2.1. https://arxiv.org/abs/2310.14149
2. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, arXiv:2008.11096 (2020-08-07), Theorems 2.2 and 2.6; *Journal of Number Theory* 217 (2020), 218–236, DOI:10.1016/j.jnt.2020.05.003. https://arxiv.org/abs/2008.11096
3. Y. Peng, K. P. S. Bhaskara Rao, *On Zumkeller numbers*, *Journal of Number Theory* 133 (2013), 1135–1155, coprime-multiplier theorem as cited by references 1 and 2.
