# A strict parity-frequency separation for unitary and exponential divisor sums

## Finding
Let \(\sigma^*(n)\) be the sum of unitary divisors and \(\sigma^{(e)}(n)\) the sum of exponential divisors of the positive integer \(n\). For real \(X\ge1\), put
\[
G_{\mathrm{odd}}(X)=\frac2X\#\{n\le X:n\text{ odd},\ \sigma^*(n)>\sigma^{(e)}(n)\},
\]
\[
G_{\mathrm{even}}(X)=\frac2X\#\{n\le X:n\text{ even},\ \sigma^*(n)>\sigma^{(e)}(n)\}.
\]
Then
\[
\boxed{\liminf_{X\to\infty}G_{\mathrm{odd}}(X)>\frac{17}{20},\qquad
\limsup_{X\to\infty}G_{\mathrm{even}}(X)<\frac34.}
\]
In particular, the lower asymptotic success frequency among odd integers exceeds the upper asymptotic success frequency among even integers by more than \(1/10\). This is a quantitative parity separation, not a claim to determine either exact limiting frequency.

## Assumptions and scope
For a prime \(p\), let \(v_p(n)\) be its exponent in \(n\). Define
\[
\rho_p(0)=1,\qquad
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}\quad(a\ge1).
\]
Multiplicativity implies
\[
\frac{\sigma^*(n)}{\sigma^{(e)}(n)}
=\prod_p\rho_p(v_p(n)).
\]
For \(a=1\), \(\rho_p(1)=1+1/p>1\). For every \(a\ge2\), \(\rho_p(a)<1\). All inequalities below are unconditional, over all positive integers, and use natural (rather than logarithmic) frequencies. The displayed finite exponent cutoffs are certificate parameters, not bounds on exponents of all possible solutions.

## Proof
**1. A certified family of odd successes.** Set
\[
P=(3,5,7,11,13,17,19),\qquad E_o=(9,5,4,3,3,2,2).
\]
For each vector \(\mathbf a=(a_p)_{p\in P}\) with \(0\le a_p\le E_{o,p}\), write \(R(\mathbf a)=\prod_{p\in P}\rho_p(a_p)\). Select the vectors with \(R(\mathbf a)>1\), together with the all-zero vector. Require each remaining prime \(q>19\) to have exponent zero or one. Every such odd integer except \(n=1\) satisfies \(\sigma^*(n)>\sigma^{(e)}(n)\): each tail prime that occurs raises the ratio, and the all-zero vector requires at least one such prime.

The exact natural probability of the small-prime exponent vector, conditioned on the integer being odd, is
\[
w(\mathbf a)=\prod_{p\in P}\frac{p-1}{p^{a_p+1}}.
\]
Exact finite enumeration gives \(18058\) selected vectors and
\[
W_o=\sum_{\mathrm{selected}}w(\mathbf a)
=\frac{31076642675170427132493824}{35968987080950832137604375}.
\]
The tail squarefreeness probability is
\[
\prod_{q>19}(1-q^{-2})
=\frac{8}{\pi^2\prod_{p\in P}(1-p^{-2})},
\qquad \prod_{p\in P}(1-p^{-2})=
\frac{12230590464}{14933966047}.
\]
The density of the resulting disjoint cylinders exists: first impose squarefreeness up to a finite prime cutoff and then let that cutoff grow; the omitted integers have upper density at most \(\sum_{q>Y}q^{-2}\to0\). The single exceptional integer \(1\) does not affect density. Using the strict classical bound \(\pi<22/7\),
\[
\liminf_{X\to\infty}G_{\mathrm{odd}}(X)
\ge W_o\frac8{\pi^2\prod_{p\in P}(1-p^{-2})}
>\frac{1896767741404445015411}{2219932798988224320000}
>\frac{17}{20}.
\]
All displayed finite rational identities and comparisons are reproduced by the attached exact-arithmetic script.

**2. A certified family of even failures.** Keep \(P\) but take exponent maxima
\(E_e=(7,4,3,2,2,1,1)\). Restrict \(2\le a=v_2(n)\le14\), and select small-prime vectors for which
\[
\rho_2(a)\prod_{p\in P}\rho_p(a_p)<\frac{11}{12}.
\]
Among even integers the exact probability of \(v_2(n)=a\) is \(2^{-a}\). The probability of each specified odd-prime exponent is \((p-1)/p^{a_p+1}\). Enumerating the \(13\cdot5760=74880\) possible vectors finds \(32591\) selected vectors of total conditional even mass
\[
W_e=\frac{38646621072482317819}{148330460379458857500}
>\frac{13}{50}.
\]
The tail ratio at primes \(q>19\) is bounded by
\[
\prod_{q>19}\rho_q(v_q(n))\le
T(n):=\prod_{\substack{q>19\\q\mid n}}(1+q^{-1}),
\]
because every positive local exponent has ratio at most \(1+1/q\). Thus a selected vector with \(T(n)<12/11\) is a strict **failure** of \(\sigma^*(n)>\sigma^{(e)}(n)\).

For \(s=100\), put \(g(q)=(1+1/q)^{100}-1\) for primes \(q>19\). On every fixed permissible small-prime valuation cylinder, the conditional mean of \(T(n)^{100}\) tends to
\[
M=\prod_{q>19}\left(1+\frac{g(q)}q\right)<\infty.
\]
Indeed \(T(n)^{100}=\sum_{d\mid n}g(d)\), where \(d\) ranges over squarefree integers supported on primes greater than \(19\) and \(g\) is multiplicative. For a fixed modulus encoding the small valuations, a term \(d\) coprime to that modulus occurs with relative frequency \(1/d\). The sum \(\sum_d g(d)/d\) converges because \(g(q)=O(1/q)\). The finite-range CRT counting errors are \(o(X)\): for some fixed \(C\), \(g(d)\le C^{\omega(d)}/d\) and \(\sum_{d\le X}g(d)=O((\log X)^C)=o(X)\). This justifies passage to the infinite moment and its independence of the fixed small-prime cylinder.

By Markov's inequality, the asymptotic conditional upper frequency of \(T(n)\ge12/11\) is at most \((11/12)^{100}M\). For \(q>1000\),
\[
\frac{g(q)}q\le\frac{100}{q(q-100)},\qquad
\sum_{q>1000}\frac{100}{q(q-100)}<\frac19.
\]
Here \(\sum_{m>1000}m^{-2}<1/1000\), while \(e^{1/9}<9/8\). Consequently
\[
B:=\left(\frac{11}{12}\right)^{100}\frac98
\prod_{19<q\le1000}\left(1+\frac{(1+q^{-1})^{100}-1}{q}\right)
<\frac1{70},
\]
where the finite product over \(160\) primes was checked exactly as a rational number. Therefore the lower asymptotic conditional frequency of strict **failures** among even integers exceeds
\[
W_e(1-B)>\frac{13}{50}\frac{69}{70}=\frac{897}{3500}>\frac14.
\]
Taking complements gives
\[
\limsup_{X\to\infty}G_{\mathrm{even}}(X)
<1-\frac{897}{3500}=\frac{2603}{3500}<\frac34.
\]
Combining both parts proves the finding.

## Verification
Execute `python3 verify_parity.py` with Python 3; it uses only `fractions.Fraction` and other standard-library modules. It recomputes the local ratios, all \(43200\) odd exponent vectors, all \(74880\) even vectors, the two rational masses, the strict \(\pi\)-bound calculation, and the finite rational \(100\)-th moment product. Its output begins `EXACT_CERTIFICATE_OK`, with selected counts \(18058\) and \(32591\). The infinite-cylinder and conditional-mean arguments in the proof are mathematical deductions, not assertions inferred from finite enumeration.

## Relationship to prior work
Trudgian (2013) introduced the comparison-density question, gave the squarefree lower bound \(6/\pi^2\), and reported the empirical overall proportion about \(0.778307\). A later published finite-cylinder computation gives an unconditional **overall** lower bound \(0.753659844\ldots\), without deriving these strict odd-versus-even conditional bounds. Earlier work on exponential divisor functions and the numerical sequence of comparison counts likewise does not, in the material inspected, give a parity-separated theorem. The present proof establishes different directional inequalities in two conditional populations; neither overall bound implies them.

## Limitations
No exact odd conditional density, exact even conditional density, or optimal parity gap is claimed. The chosen exponent cutoffs and moment \(s=100\) produce convenient sufficient cylinders; they are not extremal. The original overall density problem is not resolved. Previously unindexed or inaccessible works may contain comparable estimates.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (first public 2013-12-17), *Publ. Inst. Math.* 97 (111) (2015), 175–180. DOI: 10.2298/PIM140617001T.
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, published-finding corpus research archive (2026), published comparison-density calculation, identifier `831dd476bf82`.
3. N. Minculete, *On certain inequalities about arithmetic functions which use the exponential divisors*, *International Journal of Number Theory* (2012), DOI: 10.1142/S1793042112500923.
4. A. V. Lelechenko, *Exponential divisor functions*, arXiv:1307.3683 (2013).
5. OEIS A322446, empirical counts of integers satisfying the comparison at powers-of-ten cutoffs; numerical evidence only.
