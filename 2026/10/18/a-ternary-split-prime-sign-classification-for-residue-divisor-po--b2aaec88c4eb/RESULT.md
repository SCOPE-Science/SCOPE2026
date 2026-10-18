# A ternary split-prime sign classification for residue divisor-power sums

## Finding
For a real exponent \(s\) and an integer \(n\ge1\), set
\[
D_s(n)=\sum_{\substack{d\mid n\\3\mid d}}d^s-\sum_{\substack{d\mid n\\d\equiv1\pmod3}}d^s.
\]
There is a sharp transition at \(s=-1\): \(D_s(n)<0\) for **every** positive integer \(n\) exactly when \(s\le-1\); for each \(s>-1\), there are infinitely many adjacent pairs \((n,n+1)\) with \(D_s(n)>0>D_s(n+1)\).

More precisely, write \(n=3^tm\), where \(t\ge0\) and \(3\nmid m\), and put
\[
T_t(s)=\sum_{j=1}^{t}3^{js},\quad S_s(m)=\sum_{d\mid m}d^s,\quad C_s(m)=\sum_{d\mid m}\chi_3(d)d^s,
\]
where \(\chi_3(d)=1\) if \(d\equiv1\pmod3\) and \(-1\) if \(d\equiv2\pmod3\). Then
\[
\boxed{D_s(3^tm)=\bigl(T_t(s)-\tfrac12\bigr)S_s(m)-\tfrac12 C_s(m).}
\]
For \(-1<s<0\), the exact sign classification at **each fixed valuation** \(t\) is:

* \(T_t(s)\le1/2\): all values are strictly negative.
* \(1/2<T_t(s)<1\): both positive and negative values occur for infinitely many \(m\) coprime to \(3\). Their individual signs are determined by \(C_s(m)/S_s(m)<2T_t(s)-1\) (strictly positive), equality (zero), or the reversed inequality (strictly negative).
* \(T_t(s)=1\): the value is zero exactly when every prime factor of \(m\) is congruent to \(1\pmod3\); otherwise it is strictly positive.
* \(T_t(s)>1\): all values are strictly positive.

Thus the **least valuation supporting a positive value** is exactly
\[
\boxed{a(s)=\min\{t\ge1:T_t(s)>1/2\}},\qquad -1<s<0.
\]
For \(s>0\), the sign is strictly positive exactly when \(3\mid n\); otherwise negative. At \(s=0\), the sign is negative if \(3\nmid n\), positive if \(9\mid n\), and, for \(n=3m\) with \(3\nmid m\), zero precisely when every prime divisor of \(m\) is \(1\pmod3\), positive otherwise.

For all fixed \(s<0\), despite the infinite sign reversals when \(-1<s<0\), the cumulative sum has the strictly negative linear bias
\[
\boxed{\sum_{n\le X}D_s(n)=c_sX+o(X),\quad c_s=\tfrac12\bigl((3^s-1)\zeta(1-s)-L(1-s,\chi_3)\bigr)<0.}
\]
In fact the error is \(O_s(X^{1+s})\) for \(-1<s<0\), \(O(\log X)\) for \(s=-1\), and \(O_s(1)\) for \(s<-1\).

## Assumptions and scope
All parameters are as indicated: \(s\in\mathbb R\), \(n\in\mathbb N\), and \(t=v_3(n)\). The Dirichlet character \(\chi_3\) is the real nonprincipal character modulo \(3\), extended by zero on multiples of \(3\). The series \(\zeta(1-s)\) and \(L(1-s,\chi_3)\) converge absolutely for \(s<0\). When \(t=0\), \(T_t=0\). Adjacent sign reversal means one strictly positive value immediately followed by one strictly negative value, not merely infinitely many values of each sign.

## Proof
**The exact factorization.** Each divisor of \(3^tm\) is uniquely \(3^jd\), where \(d\mid m\), \(0\le j\le t\). The divisors divisible by \(3\) have total \(s\)-power \(T_t(s)S_s(m)\). Among the divisors of \(m\), the sum on the residue \(1\pmod3\) is \((S_s(m)+C_s(m))/2\). Subtraction proves the boxed identity, including the case \(t=0\).

**The split-prime ratio.** If \(s<0\), then \(0<p^s<1\) for every prime \(p\). For \(p\equiv1\pmod3\), the Euler factors of \(C_s(m)\) and \(S_s(m)\) agree. For \(p\equiv2\pmod3\) appearing to exponent \(e\ge1\), the character factor is \(1-p^s+p^{2s}-\cdots+(-p^s)^e=(1-(-p^s)^{e+1})/(1+p^s)>0\), whereas the ordinary factor is \(1+p^s+\cdots+p^{es}>0\). Thus \(0<C_s(m)\le S_s(m)\), with equality exactly when \(m\) has no prime factor \(2\pmod3\). If such a prime occurs with exponent one, its ratio factor is \((1-p^s)/(1+p^s)<1\).

**Uniform negativity and its sharpness.** For \(s\le-1\), \(T_t(s)<\sum_{j\ge1}3^{-j}=1/2\) for every finite \(t\); the exact identity and \(C_s(m)>0\) give \(D_s(n)<0\). If \(-1<s<0\), then \(\sum_{j\ge1}3^{js}=3^s/(1-3^s)>1/2\); therefore some finite \(t\) has \(T_t(s)>1/2\). Write \(\rho=2T_t(s)-1>0\). The ratio \(C_s(m)/S_s(m)\) can be made smaller than \(\rho\): take \(m\) to be a product of distinct primes \(p\equiv2\pmod3\). The product of \((1-p^s)/(1+p^s)\) tends to zero because \(\sum_{p\equiv2\ (3)}p^s\) diverges for \(-1<s<0\) (for example by divergence of reciprocal primes in this Dirichlet progression). Such an \(m\) gives \(D_s(3^tm)>0\). Multiplication of \(m\) by any new prime \(1\pmod3\) preserves the ratio, yielding infinitely many positive values in that valuation fiber.

For \(1/2<T_t(s)<1\), infinitely many negative values in the same fiber arise by taking \(m\) to be a prime \(1\pmod3\), for which \(C_s(m)=S_s(m)\) and \(D_s(3^tm)=(T_t(s)-1)S_s(m)<0\). The sign conditions for every valuation follow directly from \(0<C_s(m)\le S_s(m)\). At \(T_t=1\), equality is equivalent to \(C_s(m)=S_s(m)\), as characterized above.

If \(s>0\), then \(D_s(n)<0\) for \(3\nmid n\), because the divisor \(1\) occurs in the negative class. For \(3\mid n\), \(T_t(s)\ge3^s>1\) and \(\sum_{d\mid m,d\equiv1\ (3)}d^s\le S_s(m)\), so \(D_s(n)>0\). At \(s=0\), \(T_t(0)=t\); for \(t=1\), \(D_0(3m)=(S_0(m)-C_0(m))/2\), the number of divisors of \(m\) congruent to \(2\pmod3\). This number vanishes exactly when \(m\) has no prime factor \(2\pmod3\). The cases \(t=0\) and \(t\ge2\) are immediate.

**Adjacent reversals.** For \(s\ge0\), infinitely many multiples of \(9\) are positive, and their successors, not divisible by \(3\), are negative. For \(-1<s<0\), choose the infinitely many positive multiples of \(3\) built above; each immediate successor is coprime to \(3\) and hence negative.

**Negative cumulative bias.** Define \(w(d)=1\) if \(3\mid d\), \(-1\) if \(d\equiv1\pmod3\), and \(0\) otherwise. Then \(D_s(n)=\sum_{d\mid n}w(d)d^s\), so
\[
\sum_{n\le X}D_s(n)=\sum_{d\le X}w(d)d^s\lfloor X/d\rfloor.
\]
For \(s<0\), absolute convergence yields the leading constant \(\sum_{d\ge1}w(d)d^{s-1}\). The multiples of \(3\) contribute \(3^{s-1}\zeta(1-s)\). The class \(1\pmod3\) contributes \(\tfrac12((1-3^{s-1})\zeta(1-s)+L(1-s,\chi_3))\). Subtraction gives \(c_s\). Since \(3^s-1<0\), \(\zeta(1-s)>0\), and \(L(1-s,\chi_3)>0\) by its Euler product, \(c_s<0\). Applying \(\lfloor X/d\rfloor=X/d+O(1)\) and bounding \(\sum_{d\le X}d^s\) and the tail \(X\sum_{d>X}d^{s-1}\) gives the three stated error bounds. This concludes the theorem.

## Verification
The standalone `verify.py` compares independent direct divisor enumeration and the character-factorization formula for all \(1\le n\le2000\) with exact rational arithmetic at exponents \(-2,-1,0,1,2\), and for all \(1\le n\le2500\) at exponents \(-0.95,-0.75,-0.5,-0.25\) with numerical tolerances. It also verifies the stated sign classes at integer exponents and checks that at \(s=-3/4\) the two integers \(18\) and \(63\), both with \(v_3=2\), have opposite signs: \(D_{-3/4}(18)>0>D_{-3/4}(63)\). Such finite checks support but do not replace the infinite proofs.

## Relationship to prior work
Pongsriiam and Vaughan (2015) establish a general framework for divisor functions distributed in arithmetic progressions; their focus is the *argument* of the divisor function, not residue-restricted divisors of a fixed integer. Pongsriiam (2021), Problem 15, explicitly asks about sign changes in \(\sigma_s(n,q,a)\); that source is later than the archival motivating paper but directly frames the residue-divisor problem. A published result for modulus \(2\) classifies the odd-versus-even divisor-power difference using only the \(2\)-adic valuation. It does **not** imply the ternary classification here: in particular, when \(1/2<T_t(s)<1\), the two signs coexist at the *same* \(3\)-adic valuation, and the cumulative bias has a nontrivial \(L\)-value correction. Targeted searches did not find an equivalent ternary statement, but search non-detection alone cannot prove novelty.

## Limitations
The exact sign condition for \(-1<s<0\) uses the multiplicative ratio \(C_s(m)/S_s(m)\), not a finite congruence classification. The cumulative asymptotic is asserted only for \(s<0\); no exact density formula for positive values at \(-1<s<0\) is claimed. A related theorem in unindexed literature remains a residual originality risk. No independent assessment is asserted.

## References
1. P. Pongsriiam and R. C. Vaughan, “The divisor function on residue classes I,” *Acta Arithmetica* 168 (2015), 369–381, DOI 10.4064/aa168-4-3; public journal record dated 21 May 2015.
2. P. Pongsriiam, “Sums of divisors on arithmetic progressions,” arXiv:2110.00237v1, first posted 1 October 2021; especially Problem 15 and the primary classification MSC 11A25.
3. “Parity-resolved divisor-power sums for \(q=2\),” published mathematical-results record (2026), identifier 2026/10/4/SCOPE-parity-resolved-divisor-power-sums-for-q-2--4f1aac33584e. Its result and proof were compared for scope rather than assumed to imply the ternary case.
4. Classical Dirichlet-prime harmonic divergence in nonzero residue classes, standard consequence of the nonvanishing of Dirichlet \(L\)-functions at \(1\).
