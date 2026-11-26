# The first prime-square collision in squarefree-plus-power-of-two progressions

## Finding

Let \(E=\{0,1,2,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20\}\). Let \(\Theta\) be the relative density, among primes \(p\equiv7\pmod{36}\), of those for which all eighteen remainders \(p-2^a\), \(a\in E\), are non-squarefree; take \(p>2^{20}\), which does not affect density. Define the all-distinct benchmark
\[
H_j=\prod_{q\ge5\atop q\ \mathrm{prime}}\left(1-\frac{j}{q(q-1)}\right),\qquad
\Theta^{\rm dis}=\sum_{j=0}^{18}(-1)^j\binom{18}{j}H_j.
\]
The benchmark treats the eighteen forbidden residue classes as distinct at every prime square \(q^2\) with \(q\ge5\). For each prime \(q\ge7\), independently choose a uniform reduced class modulo \(q^2\) and mark every label \(a\in E\) whose \(2^a\) represents that class. Write \(U\) for the labels never marked. Then
\[
\boxed{\displaystyle
\Theta-\Theta^{\rm dis}=\frac1{20}\Pr(U=\{0,20\})>0.}
\]
In particular, although the distinct-class approximation is not valid for this window, it errs strictly downwards. The same correction in Euler-product form is \(\sum_{j=2}^{18}(-1)^j\binom{16}{j-2}H_j/(20-j)\). The existence and exact inclusion–exclusion expression for \(\Theta\) specialize the general finite-set law of Harman–Paquin; the result here is the positive-event interpretation and strict sign of its discrepancy from the benchmark.

## Assumptions and scope

The relative density uses denominator \(\pi(X;36,7)\) as \(X\to\infty\). Squarefreeness is considered only for positive remainders. The exponents \(a\equiv4\pmod6\) are excluded because \(2^a\equiv7\pmod9\). For \(p\equiv7\pmod{36}\), no admissible remainder is divisible by four: modulo four the cases \(a=0,1,\ge2\) give residues \(2,1,3\), respectively. The collision and benchmark above concern the remaining primes \(q\ge5\). No claim is made about representations without a bound on the exponent.

## Proof

**Local classes.** Two labels collide at \(q^2\) exactly when \(q^2\mid 2^{|a-b|}-1\). For \(1\le d\le20\), prime trial division through \(\lfloor\sqrt{2^{20}-1}\rfloor=1023\) shows that the only pair \((d,q)\) with \(q\ge5\) and \(q^2\mid2^d-1\) is \((20,5)\). This is the bounded computation in `verify.py`. Thus for \(T\subseteq E\) with \(j=|T|\), the number \(r_q(T)\) of distinct classes from \(T\) is \(j\) for all \(q\ge7\) and \(j-\mathbf 1_{\{0,20\}\subseteq T}\) for \(q=5\).

**Prime densities and the local model.** For any fixed upper bound \(Y\) on \(q\), the prime number theorem in arithmetic progressions and the Chinese remainder theorem make the reduced residue choices modulo the squares of primes \(5\le q\le Y\) independent and uniform in the relative limit. Indeed the moduli are coprime to each other and to 36, and each reduced tuple gives one reduced class when combined with \(7\bmod36\). To remove \(Y\), fix one shift \(c=2^a\). For \(Y<q\le X^{1/4}\), Brun–Titchmarsh applied to \(p\equiv c\pmod{q^2}\) bounds the count of such primes by \(4X/[\varphi(q^2)\log X]\) for each \(q\); here \(\gcd(c,q)=1\). For \(X^{1/4}<q\le\sqrt X\), count integers in the class instead: summing \(X/q^2+1\) gives \(O(X^{3/4}+\sqrt X)\). Larger primes cannot square-divide a positive remainder at most \(X\). Dropping the progression restriction for these bounds only increases the count. After division by \(\pi(X;36,7)\sim X/(12\log X)\), the tail has limsup bounded by a constant times \(\sum_{q>Y}1/\varphi(q^2)\), also after taking the union over the fixed set of shifts. This tends to zero. The same summable local probabilities bound the tail in the independent product model. Therefore the density of full failure is the probability in that model that every label is marked, while the density of simultaneous squarefreeness for a set \(T\) is
\[
\delta(T)=\prod_{q\ge5\atop q\ \mathrm{prime}}\left(1-\frac{r_q(T)}{q(q-1)}\right).
\]
The all-distinct benchmark can also be modeled by independent choices, each marking any particular singleton with probability \(1/\varphi(q^2)\), or none with the remaining probability. Its full-coverage probability is \(\Theta^{\rm dis}\) by inclusion–exclusion. All the products converge, since the omitted probability mass is bounded by \(18\sum_q1/\varphi(q^2)\) and each avoidance factor is positive.

**Positive difference.** The actual and benchmark laws agree at every \(q\ge7\) and hence have the same distribution of \(U\). The actual \(q=5\) marking law chooses the pair \(\{0,20\}\) with probability \(1/20\), each of the other sixteen singletons with probability \(1/20\), and no mark with probability \(3/20\). The benchmark can instead choose each of eighteen singletons with probability \(1/20\) and no mark with probability \(2/20\). If \(U\) is empty, both laws complete coverage; if \(U\) is a singleton, both succeed with probability \(1/20\). If \(U\) contains two or more labels, only \(U=\{0,20\}\) can be covered at this prime and only under the actual law. This proves the probability identity. To see strictness, assign sixteen distinct primes \(q_a\ge7\) to mark the sixteen ordinary labels, forcing the original reduced class \(2^a\bmod q_a^2\). These forced classes do not mark either special label. Require all other primes \(q\ge7\) to avoid both special classes. The resulting event has positive probability, the product of sixteen positive probabilities and a product of factors \(1-2/\varphi(q^2)\) that converges to a positive number. On this event \(U=\{0,20\}\).

**Euler-product expression.** The factor at \(q=5\) changes from \(1-j/20\) to \(1-j/20+\mathbf 1_{\{0,20\}\subseteq T}/20\). Thus \(\delta(T)-H_j=\mathbf 1_{\{0,20\}\subseteq T} H_j/(20-j)\). Inclusion–exclusion for full coverage gives the correction sum by counting the \(\binom{16}{j-2}\) such subsets of cardinality \(j\). For \(p>2^{20}\), failure for the eighteen admissible exponents rules out any squarefree remainder at exponent at most twenty, because the intervening inadmissible exponents are already obstructed by nine.

## Verification

The accompanying `verify.py` bounds and checks all possible square-dividing primes for the twenty differences, checks every subset for the modulus 25 factor, and compares the two coverage laws with exact rational arithmetic in the finite model with sixteen other primes. That check illustrates the identity but does not establish the infinite density or its strict comparison; these follow from the proof above.

## Relationship to prior work

Harman and Paquin, *The One-Power Erdős Conjecture for Primes \(p\equiv7\pmod{36}\)*, arXiv:2610.07214v1 (5 October 2026), identify the order-twenty collision and give the distinct-class density law for shorter windows (Proposition 2, Theorem 4, and Remark 4). More generally, p. 13 states the arbitrary finite set law with local factor \(1-r_q(T)/\varphi(q^2)\) and its application to the density of complete failure. In particular the exact density for this set, including its specialized Euler-product correction term, follows from their general law. The comparison here identifies the correction with the probability of a particular uncovered pair and proves it strictly positive. This is not a new general squarefree-density or collision theorem.

## Limitations

There is no numerical approximation to the density or the correction, error term for the density, or conclusion about all exponents. The sign comparison concerns the first collision window and the stated all-distinct benchmark.
