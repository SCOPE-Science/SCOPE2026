# Prime-residue density and sharp low-index classifications for Schemmel iterate sums

## Finding

**Theorem.** Fix an even integer \(m\ge2\). Set
\[
P_m=\prod_{\substack{q\le m\\q\text{ prime}}}q,
\qquad
\delta_m=\prod_{\substack{q\le m\\q\nmid m\\q\text{ prime}}}\frac{q-2}{q-1},
\]
where an empty product is \(1\). For each fixed integer \(a\ge1\), the primes \(p\) for which \(D_m(p^a)>p^a\) have relative natural density \(\delta_m\). The same density holds for primes \(p\) for which this strict inequality holds **simultaneously for every** \(a\ge1\). Indeed, outside a finite set of prime bases, simultaneously for all exponents, the criterion is exactly
\[
D_m(p^a)>p^a\quad\Longleftrightarrow\quad\gcd(p-m,P_m)=1;
\]
if the gcd is greater than one, every power is strictly deficient. Thus only finitely many prime bases can underlie a perfect prime power. In particular \(\delta_2=1\), \(\delta_4=1/2\), \(\delta_6=3/4\), and \(\delta_8=5/16\).

For the two smallest even parameters there is an exact description **with no exceptional prime bases**:
\[
\begin{aligned}
D_2(p^a)>p^a&\quad\Longleftrightarrow\quad p\ge7,\\
D_4(p^a)>p^a&\quad\Longleftrightarrow\quad p\ge17\ \text{and}\ p\equiv2\pmod3,
\end{aligned}
\qquad(p\text{ prime},\ a\ge1).
\]
In both cases every prime power not satisfying the displayed condition is strictly deficient. Hence neither \(D_2\) nor \(D_4\) has a perfect prime power.

## Assumptions and scope

For every positive integer \(m\), the Schemmel totient is multiplicative, with \(L_m(0)=0\), \(L_m(1)=1\), and
\[
L_m(n)=0\ \text{if a prime }q\le m\text{ divides }n;
\qquad L_m(n)=\prod_{q^b\parallel n}q^{b-1}(q-m)
\quad\text{otherwise}\quad(n>1).
\]
For \(n>1\), iterate \(L_m\) until the first occurrence of \(0\) or \(1\) and define \(D_m(n)\) to be the sum of the iterates, **including** that terminal value once. An integer \(n>1\) is \(D_m\)-abundant, deficient or perfect according as \(D_m(n)\) is greater than, less than or equal to \(n\). The theorem concerns prime powers \(p^a\) with unrestricted exponent \(a\ge1\), fixed even \(m\), and relative natural densities **among primes**, not densities among all integers or all prime powers ordered numerically. The classical prime number theorem for arithmetic progressions, stronger than Dirichlet's infinitude theorem, is used. No hypothesis on unproved prime conjectures is made.

## Proof

**1. A uniform lower bound for rough inputs.** Define the strictly positive rational constant
\[
c_m=\prod_{\substack{m<q\le2m\\q\text{ prime}}}\left(1-\frac{m}{q}\right).
\]
For any integer \(u\ge1\) with no prime divisor \(\le m\), we have
\[
L_m(u)\ge c_m\sqrt{u}.\tag{1}
\]
Indeed, if \(q^b\parallel u\) with \(m<q\le2m\), then
\(q^{b-1}(q-m)\ge[(q-m)/q]q^{b/2}\) for \(b\ge1\). If \(q>2m\), then \(q\ge5\) and \(q-m>q/2\ge\sqrt q\), whence \(q^{b-1}(q-m)\ge q^{b/2}\). Multiply these local inequalities and note that the product of factors \((q-m)/q\) over the prime divisors of \(u\) in the short interval is at least their product over **all** primes in that interval. The case \(u=1\) is immediate.

**2. Every sufficiently large prime base is decided by a finite congruence condition.** Take a prime \(p>m\), write \(u=p-m\), and let \(a\ge1\). If some prime \(q\le m\) divides \(u\), then \(q\) also divides \(L_m(p^a)=p^{a-1}u\). The very next iterate vanishes, so
\[
D_m(p^a)=p^{a-1}u<p^a\qquad\text{for every }a\ge1.\tag{2}
\]
If instead \(\gcd(u,P_m)=1\), assume \(u\ge m\) and \(c_m\sqrt{u}>2m\). By (1), \(L_m(u)>2m\). For \(a=1\), the first two iterates sum to \(u+L_m(u)>p\). For \(a\ge2\), multiplicativity and \(\gcd(p,u)=1\) give
\[
L_m(p^a)=p^{a-1}u,\qquad L_m^{(2)}(p^a)=p^{a-2}uL_m(u).
\]
Their sum exceeds \(p^a\) precisely when \(uL_m(u)>mp\). Here \(uL_m(u)>2mu\ge m(u+m)=mp\), proving the strict inequality. Every subsequent iterate is nonnegative. Since the two assumed inequalities hold for all sufficiently large \(p\), with a threshold depending on \(m\) but **not** on \(a\), the announced simultaneous dichotomy follows.

**3. Exact prime density.** For primes \(p>m\), their residue modulo \(P_m\) is reduced. At any prime \(q\mid m\), the condition \(p\not\equiv m\pmod q\) is automatic. At each prime \(q\le m\) not dividing \(m\), it excludes exactly one of the \(q-1\) reduced residue classes. The Chinese remainder theorem therefore gives \(\prod_{q\le m,\,q\nmid m}(q-2)\) favorable reduced-residue choices in the nontrivial factors, out of \(\prod_{q\le m,\,q\nmid m}(q-1)\) such choices. The prime number theorem for arithmetic progressions gives relative prime density \(\delta_m\). The finite exceptional bases of Step 2 have no effect on this density. A prime power can be perfect only at one of these exceptional bases; this does not assert any bound on their possible exponents.

**4. The exact \(m=2\) criterion.** For primes \(p\le2\), the first iterate is zero. For \(p=3\), successive iterates of \(3^a\) are \(3^{a-1},\ldots,1\), so \(D_2(3^a)=(3^a-1)/2<3^a\). For \(p=5\), successive iterates are \(3\cdot5^{a-1},\ldots,3,1\), so \(D_2(5^a)=(3\cdot5^a+1)/4<5^a\). If \(p\ge7\), then \(u=p-2\) is odd and at least \(5\); for every such \(u\), \(L_2(u)\ge3\). This last fact follows because a prime factor \(\ge5\) gives a local factor \(\ge3\), while if all prime factors are \(3\), then \(u\ge9\) and \(L_2(u)\ge3\). For \(a=1\), \(D_2(p)\ge u+3>p\). For \(a\ge2\), \(uL_2(u)\ge3u>2(u+2)=2p\), since \(u\ge5\). Step 2's two-iterate formula proves abundance.

**5. The exact \(m=4\) criterion.** Every prime \(p\le4\) has zero first iterate. If \(p>4\) and \(p\equiv1\pmod3\), then \(3\mid p-4\), so (2) gives deficiency. The remaining primes are \(p\equiv2\pmod3\). At \(p=5\), \(D_4(5^a)=(5^a-1)/4<5^a\). At \(p=11\), the first two iterates for \(a=1\) are \(7,3\), giving \(D_4(11)=10<11\); for \(a\ge2\), they are \(7\cdot11^{a-1}\) and \(21\cdot11^{a-2}\), after which the next iterate is zero because a factor \(3\) appears. Thus \(D_4(11^a)=98\cdot11^{a-2}<11^a\).

If \(p\ge17\) and \(p\equiv2\pmod3\), put \(u=p-4\ge13\). Its prime divisors are all at least \(5\). For such integers the only \(u\) with \(L_4(u)<5\) are \(1,5,7,35\): any local factor from a prime \(q\ge11\) or from an exponent at least two is at least \(5\), while the squarefree products of \(5\) and \(7\) are the displayed four possibilities. Of these, \(u=1,5,7,35\) give \(p=5,9,11,39\), none an eligible prime \(\ge17\). Therefore \(L_4(u)\ge5\). If \(u>16\), this yields \(uL_4(u)\ge5u>4(u+4)=4p\). The only eligible \(u\) in \([13,16]\) is \(u=13\) (\(p=17\)), for which \(L_4(13)=9\) and \(13\cdot9>4\cdot17\). For \(a\ge2\) the exact two-iterate criterion from Step 2 proves abundance, and for \(a=1\) it follows from \(L_4(u)\ge5>4\). This completes both classifications.

## Verification

The standalone file `verify.py` uses integer factorization and exact rational arithmetic, independently evaluating \(L_m\), the finite iterate sum, and the constant \(c_m\). Running `python3 verify.py` produces the status `FINITE_CHECKS_OK` and checks 1,565 instances of (1), 609 prime-power instances of the general sufficient/necessary branches, and 488 instances of the full \(m=2,4\) classification. It also checks \(c_2=1/3\), \(c_4=3/35\), and \(c_6=5/77\). These finite checks are diagnostic; the claims for all primes and all exponents depend on Steps 1–5 and Dirichlet equidistribution.

## Relationship to prior work

Defant (2015), Theorem 18, proves infinitely many prime bases yielding abundance for every exponent and provides the key first-two-iterate identity. The proof chooses one reduced residue class and gives no exact density or eventual classification of **all** reduced classes. The present theorem determines the asymptotic share of favorable prime bases, the uniform exponent-independent congruence dichotomy, and the exact no-exception \(m=2,4\) strata. The preceding first-two-iterate identity and Dirichlet theorem are acknowledged foundations, not claimed as new. OEIS A241667 and A241668 tabulate the underlying iterate sums for \(m=2\) and \(m=4\), respectively; the inspected entries do not state this classification or the prime-density formula. No priority claim is made beyond the comparison of inspected sources.

## Limitations

The density is **relative to prime bases**, not the density of abundant integers. No effective least-threshold formula is optimized for general \(m\), and finitely many exceptional prime bases may have mixed outcomes across exponents for \(m\ge6\). The finiteness assertion for possible perfect prime-power bases does **not** bound the number of exponents above such bases. The theorem does not establish abundance or deficiency for general composite integers with multiple distinct prime factors, nor an infinitude theorem for perfect iterate sums. The cited literature may contain unindexed equivalent arguments not located by the searches.

## References

1. C. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, Journal of Integer Sequences **18** (2015), Article 15.2.1; first publicly published 13 January 2015. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.html ; https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.pdf . See especially Definition 11, Theorem 18, and Corollary 19.
2. OEIS A241667, iterate sums of the second Schemmel totient: https://oeis.org/A241667 .
3. OEIS A241668, iterate sums of the fourth Schemmel totient: https://oeis.org/A241668 .
4. OEIS A241663, values of the fourth Schemmel totient: https://oeis.org/A241663 .
5. Dirichlet equidistribution theorem for primes in fixed reduced residue classes, used in its standard form.
