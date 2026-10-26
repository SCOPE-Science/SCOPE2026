# Prime-power layers of the unitary–exponential divisor-sum comparison

## Finding
For an integer \(a\ge2\), define
\[
N_a(X)=\#\{n\le X:n=p^a q,\ p,q\text{ distinct primes},\ \sigma^*(n)>\sigma^{(e)}(n)\}.
\]
Here \(\sigma^*\) sums unitary divisors, and \(\sigma^{(e)}\) sums exponential divisors. Let \(d(a)\) be the largest proper positive divisor of \(a\), and set \(b=a-d(a)\). For every **fixed** \(a\ge2\), as the real parameter \(X\to\infty\),
\[
\boxed{N_a(X)\sim K_a\frac{X^{(b+1)/(a+b)}}{(\log X)^2},\qquad
K_a=\frac{(a+b)^2}{b}\left(\frac1{b+1}+\frac1{a-1}\right).}
\]
The comparison has the following exact prime-pair criterion, also valid for every prime and every \(a\ge2\):
\[
\boxed{\sigma^*(p^a q)>\sigma^{(e)}(p^a q)
\iff q\left(\sum_{\substack{d\mid a\\d<a}}p^d-1\right)\le p^a.}
\]
Thus the smallest prime factor of \(a\) determines the growth exponent in the first non-squarefree, two-prime-support layers. In particular, \(N_2(X)\sim (27/2)X^{2/3}/(\log X)^2\), \(N_3(X)\sim (125/12)X^{3/5}/(\log X)^2\), and \(N_4(X)\sim12X^{1/2}/(\log X)^2\).

## Assumptions and scope
The variable \(a\) is fixed before taking \(X\to\infty\); no estimate uniform in growing \(a\) is asserted. All primes are ordinary positive rational primes. For \(a\ge2\), exponential divisors of \(p^a\) have exponents \(d\mid a\), so \(\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\). Unitary divisors of \(p^a\) are \(1\) and \(p^a\). For \(q\) to exponent one, \(\sigma^{(e)}(q)=q\) whereas \(\sigma^*(q)=1+q\). Both divisor functions are multiplicative. Each integer \(p^a q\) with \(p\ne q\) has exactly one such representation.

## Proof
**1. Exact reduction.** Put
\[
\Delta_a(p)=\sum_{\substack{d\mid a\\d<a}}p^d-1>0.
\]
Multiplicativity yields
\[
\sigma^*(p^a q)=(1+p^a)(1+q),\qquad
\sigma^{(e)}(p^a q)=q(p^a+\Delta_a(p)+1).
\]
Their difference is \(1+p^a-q\Delta_a(p)\). Since it is integral, strict positivity is equivalent to \(q\Delta_a(p)\le p^a\), proving the exact criterion. Consequently, for any real \(X\ge1\),
\[
N_a(X)=\sum_{\substack{p\text{ prime}\\2p^a\le X}}
\left[\pi\!\left(\min\!\left(\left\lfloor\frac X{p^a}\right\rfloor,\left\lfloor\frac{p^a}{\Delta_a(p)}\right\rfloor\right)\right)
-\mathbf1_{\{p\le\min(\lfloor X/p^a\rfloor,\lfloor p^a/\Delta_a(p)\rfloor)\}}\right].
\]
This exact finite sum is also the basis of the verifier.

**2. Prime threshold.** Let \(d=d(a)\), the maximal proper divisor of \(a\), and \(b=a-d\ge1\). All other proper divisors are at most \(d-1\); hence, for fixed \(a\),
\[
\Delta_a(p)=p^d(1+O_a(p^{-1})),\qquad
B_a(p):=\frac{p^a+1}{\Delta_a(p)}=p^b(1+O_a(p^{-1})).
\]
For each fixed \(a\), the count differs from
\[
A_a(X)=\sum_{p\text{ prime}}\pi\left(\min\left(p^b,\frac X{p^a}\right)\right)
\]
by \(o\bigl(X^{(b+1)/(a+b)}/(\log X)^2\bigr)\). Indeed let \(T=X^{1/(a+b)}\). For sufficiently large primes \(p>2T\), both minima use \(X/p^a\), since \(B_a(p)\ge p^b/2\) and \(X/p^a\le p^b/2^{a+b}\). For \(p\le2T\), the change in the cutoff is at most \(O_a(p^{b-1})\); the change in the prime count is at most this cutoff difference plus one. Summing even over all integers \(p\le2T\) costs only \(O_a(T^b+T)\), negligible against \(T^{b+1}/(\log T)^2\). The finitely many exceptional small primes affect this estimate by at most a constant. The excluded diagonal \(q=p\) has at most \(\pi(X^{1/(a+1)})\) elements, also negligible because \((b+1)/(a+b)>1/(a+1)\).

**3. Small first prime.** For \(p\le T\), the minimum defining \(A_a\) is \(p^b\). The prime number theorem and partial summation imply
\[
\sum_{p\le T}\pi(p^b)
\sim\frac{T^{b+1}}{b(b+1)(\log T)^2}.
\]
The formula remains valid for \(b=1\), where the summand counts the primes up to \(p\).

**4. Large first prime.** For \(T<p\le UT\) with any fixed \(U>1\), the prime number theorem, uniformly on the fixed scaled interval, gives
\[
\sum_{T<p\le UT}\pi(X/p^a)
\sim\frac{T^{b+1}}{b(\log T)^2}\int_1^Uu^{-a}\,du.
\]
To control the remaining primes, choose fixed \(0<\varepsilon<b/a\). In the range \(UT<p\le T^{1+\varepsilon}\), the quantity \(X/p^a\ge T^{b-a\varepsilon}\), so \(\pi(X/p^a)\ll_a X/(p^a\log T)\). Partial summation from the prime number theorem gives \(\sum_{p>V}p^{-a}\ll_a V^{1-a}/\log V\). This tail is therefore \(O_a(U^{1-a}T^{b+1}/(\log T)^2)\). For \(p>T^{1+\varepsilon}\), the crude bound \(\pi(y)\le y\) and the integer-series tail give \(O_a(T^{b+1-\varepsilon(a-1)})\), which is negligible. Sending \(U\to\infty\) yields
\[
\sum_{p>T}\pi(X/p^a)\sim\frac{T^{b+1}}{b(a-1)(\log T)^2}.
\]

**5. Combining the ranges.** Adding steps 3 and 4 and substituting \(\log T=(\log X)/(a+b)\) gives the stated \(K_a\). The formulas use no unproved distribution hypothesis beyond the classical prime number theorem.

For context, the total number \(T_a(X)\) of integers \(p^a q\le X\), with \(p\ne q\) prime and without the divisor-sum comparison, satisfies \(T_a(X)\sim P(a)X/\log X\), where \(P(a)=\sum_{p\text{ prime}}p^{-a}\). This follows by fixing \(p\), using the prime number theorem for \(q\), and bounding the large-\(p\) tail via \(\sum_{p>Y}p^{-a}\). Thus the comparison-positive members have relative proportion tending to zero in every fixed exponent layer \(a\ge2\), despite being infinite in number.

## Verification
The standalone `verify.py` uses only the Python standard library. It independently checks the exact multiplicative formulas and comparison cutoffs by enumerating distinct prime pairs with \(p^a q\le X\), for every \(2\le a\le6\) and \(X\in\{10^4,10^5,10^6\}\). It separately recomputes the finite prime-counting formula and checks exact rational expressions for \(K_a\) for the five tested exponents. From the actual packaged script the expected final line is:

`VERIFY_OK exponents=2..6 X=10000,100000,1000000 counts_at_1000000={2: 861, 3: 261, 4: 63, 5: 124, 6: 28}`

The finite checks do not establish the asserted limit; that is the analytic argument in the proof.

## Relationship to prior work
Trudgian's *The sum of the unitary divisor function* (first public 2013-12-17, arXiv:1312.4615) asks about the natural density of \(\sigma^*(n)>\sigma^{(e)}(n)\), records that all squarefree integers satisfy it, and asks about equal values. Its Section 4 does not give layer-wise power-law asymptotics for \(p^a q\). A published finite-layer treatment of the **equality** \(\sigma^*=\sigma^{(e)}\) exhausts \(2\le a\le49\) for \(p^a q\); that equality classification does not determine the number satisfying the strict inequality. A separate finite-cylinder bound for the full natural density is also not an asymptotic in the zero-density \(p^a q\) family. Decker–Moree's RSA-prime counting treats \(pq\) with bounded prime ratio, rather than \(p^a q\) with the exponent-dependent inequality cutoff. The prime-pair estimation method here is elementary and standard; the claim is the divisor-comparison-induced, exponent-dependent asymptotic and constant, not a new general theorem about primes.

## Limitations
The result does not solve Trudgian's overall density or equality-infinitude problems. No uniformity in \(a\) is proved, and only numbers with precisely two distinct prime factors and exponent pattern \((a,1)\) are counted. A comparable formula may be implicit in an unlocated general prime-pair counting result; no independent mathematical audit has been performed.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first submitted 2013-12-17, especially Section 4; *Publ. Inst. Math.* 97(111) (2015), 175–180.
2. A. Decker and P. Moree, *Counting RSA-Integers*, arXiv:0801.1451, first submitted 2008-01-09; *Results in Mathematics* 52 (2008), 35–39.
3. Prime number theorem and its elementary partial-summation consequences (classical).
