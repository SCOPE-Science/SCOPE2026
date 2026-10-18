# Sharp least-prime strata of Schreier numbers

## Finding

For a positive integer \(n\), write
\[
S'(n)=\{d\mid n:1<d\leq\sqrt n\}.
\]
Call \(n\) a *Schreier number* when \(S'(n)\) is empty or its smallest element is at least its cardinality. For any fixed prime \(p\), let \(N_p(X)\) count Schreier integers \(n\leq X\) whose least prime factor is \(p\). Define the positive integers
\[
u_p=\left\lfloor\log_2(p+1)\right\rfloor,\qquad
E_p=\left\lfloor\frac{p+1}{2^{u_p-1}}\right\rfloor-1,
\qquad C_p=\sum_{e=1}^{E_p}\frac1{p^e}.
\]
Then \(E_p\in\{1,2\}\), and for every fixed prime \(p\),
\[
\boxed{N_p(X)\sim \frac{C_p}{(u_p-1)!}\frac{X(\log\log X)^{u_p-1}}{\log X}\qquad(X\to\infty).}
\]
The entire leading term comes from integers
\[
n=p^e q_1q_2\cdots q_{u_p},\quad 1\le e\le E_p,\quad p<q_1<\cdots<q_{u_p}\text{ prime}.
\]
Every integer of this form is Schreier, and all other Schreier integers with least prime factor \(p\) have smaller counting order. In particular, \(N_2(X)\sim 3X/(4\log X)\), whereas \(N_3(X)\sim X\log\log X/(3\log X)\). The extra \(p^2\)-layer contributes to the leading constant exactly when \(p+1\ge 3\cdot 2^{u_p-1}\). As another consequence, for any two fixed primes \(p,q\) with \(u_p<u_q\), one has \(N_p(X)=o(N_q(X))\): the local strata exhibit successive powers of \(\log\log X\).

## Assumptions and scope

The prime \(p\) is fixed before taking \(X\to\infty\); the asymptotic is not claimed uniform as \(p\) varies. Natural logarithms are used, \(\tau(n)\) counts all positive divisors, and \(\omega(n)\) counts distinct prime divisors. Empty small-divisor sets are Schreier by definition. Prime powers and perfect squares are included in the count, but cannot affect the leading term.

## Proof

**Small-divisor criterion.** For composite \(n\), the least member of \(S'(n)\) is its least prime divisor \(p\). Pairing divisors around \(\sqrt n\) gives
\[
|S'(n)|=\begin{cases}(\tau(n)-2)/2,&n\text{ nonsquare},\\
(\tau(n)-1)/2,&n\text{ square}.
\end{cases}
\]
Consequently, a composite nonsquare with least prime factor \(p\) is Schreier if and only if \(\tau(n)\le 2(p+1)\); for a composite square the corresponding exact threshold is \(\tau(n)\le 2p+1\). The finitely many prime integers \(n=p\) are harmless. All squares \(\le X\) number only \(O(\sqrt X)\), so restrict henceforth to nonsquares.

Factor each integer with least prime \(p\) uniquely as
\[
n=p^e\prod_{j=1}^{m}q_j^{a_j},\qquad e\ge1,\quad p<q_1<\cdots<q_m,\quad a_j\ge1.
\]
The criterion becomes
\[
(e+1)\prod_{j=1}^{m}(a_j+1)\le2(p+1).
\]
In particular, \(2^{m+1}\le 2(p+1)\), so \(m\le u_p=\lfloor\log_2(p+1)\rfloor\). Also each exponent is bounded in terms of \(p\), so only finitely many exponent patterns are possible.

**Leading exponent patterns.** To obtain the maximal number \(m=u_p\) of additional distinct prime factors with all their exponents one, the divisor condition reduces to
\[
(e+1)2^{u_p}\le2(p+1),
\]
which is equivalent to \(1\le e\le E_p\). Since \(2^{u_p}\le p+1<2^{u_p+1}\), the integer \(E_p\) is either one or two. Every integer of one of these prescribed forms is nonsquare and Schreier, regardless of the sizes of the primes \(q_j\). For each fixed exponent \(e\), the classical fixed-factor Landau asymptotic for products of \(u_p\) distinct primes, excluding any fixed finite set of primes, yields
\[
\#\{p^e q_1\cdots q_{u_p}\le X:p<q_1<\cdots<q_{u_p}\}
\sim\frac{1}{p^e(u_p-1)!}\frac{X(\log\log X)^{u_p-1}}{\log X}.
\]
For \(u_p=1\), this is simply the prime number theorem. For larger \(u_p\), excluding primes \(\le p\) does not alter Landau's leading coefficient, since products containing a fixed small prime have one fewer unrestricted prime factor. Summing over the finite range \(1\le e\le E_p\) gives the asserted main term.

**All omitted exponent patterns are smaller.** The same fixed-factor Landau bounds give, for any fixed \(r\ge1\),
\[
\#\{q_1\cdots q_r\le Y:q_1<\cdots<q_r\text{ prime}\}
=O_r\!\left(\frac{Y(\log\log(3Y))^{r-1}}{\log(2Y)}\right).
\]
An exponent pattern with \(r\) freely occurring primes to the first power and \(s\ge1\) distinct primes to powers at least two has \(r+s\le u_p\). Summing the reciprocals of those higher prime powers converges. Split their product \(D\) at \(\sqrt X\). For \(D\le\sqrt X\), the displayed Landau bound shows a contribution \(O_p(X(\log\log X)^{r-1}/\log X)\). For \(D>\sqrt X\), one of the \(s\) higher prime-power factors exceeds \(X^{1/(2s)}\); since the exponents and \(s\) are bounded in terms of \(p\), a union bound on multiples of these prime powers gives \(O_p(X^{1-c_p})\) for some \(c_p>0\). Patterns with \(r=0\) contribute \(O_p(\sqrt X)\) up to a harmless polylogarithmic factor, by the standard parametrization of squarefull numbers. Thus every pattern with a repeated additional prime has \(o_p(X(\log\log X)^{u_p-1}/\log X)\) elements.

If all \(m\le u_p-1\) additional primes have exponent one, their contribution is \(O_p(X(\log\log X)^{u_p-2}/\log X)\) when \(u_p\ge2\), by Landau; when \(u_p=1\), the only such integers are powers of \(p\), of which there are \(O_p(\log X)\). For patterns with repeated additional primes, the preceding paragraph applies. It follows that none of the omitted forms changes the leading constant. This proves the theorem.

## Verification

The accompanying standalone Python script `verify.py` enumerates \(2\le n\le250000\), independently constructs each small-divisor set, and compares its Schreier verdict with the exact divisor-count criterion (including the square correction). It then checks that every number belonging to a displayed leading exponent layer is Schreier, and reports the actual layer counts alongside the asymptotic *predictions*. All exhaustive comparisons passed. Asymptotic predictions converge slowly, especially for larger fixed \(p\); no finite experiment is used to prove the limiting formula. Run `python3 verify.py` from the package directory.

## Relationship to prior work

Nataraj's 2022 paper establishes zero ordinary density for Schreier numbers and, in its Corollary 1 discussion, bounds the number of additional prime factors using the smallest prime \(p\) and Landau's theorem. The present theorem determines an exact leading coefficient in every fixed least-prime stratum, including the second \(p\)-power layer when allowed. It therefore distinguishes fixed-prime strata that the zero-density conclusion alone cannot distinguish. Chu's earlier project note formulates the Schreier density question and proves elementary facts about small divisors and gaps; it gives no fixed-least-prime leading constants. The analytic input is the classical fixed-prime-factor theorem of Landau, not a new prime-distribution theorem.

## Limitations

The result does not give a global asymptotic for all Schreier numbers, uniformity in growing \(p\), or rates of convergence in the displayed limits. Landau's theorem is used as a cited classical input. An equivalent local asymptotic outside the inspected sources cannot be excluded. No independent mathematical audit is claimed.

## References

1. K. Nataraj, *Schreier Numbers and Nontrivial Small Divisors Satisfying Linear Recurrence of Order at Most Two* (2022), arXiv:2209.06900, first posted 2022-09-14. https://arxiv.org/abs/2209.06900 . See Theorem 1 and Corollary 1.
2. H. V. Chu, *Numbers with Small/Large Divisors Satisfying Some Recurrence Relation*, project note, Section 3. https://web.williams.edu/Mathematics/sjmiller/public_html/polymathreumiller/ChuPossibleProjects.pdf .
3. E. Landau, *Handbuch der Lehre von der Verteilung der Primzahlen* (1909), pp. 203–211, classical asymptotics for integers with a fixed number of prime factors; cited as reference [14] in Nataraj (2022).
