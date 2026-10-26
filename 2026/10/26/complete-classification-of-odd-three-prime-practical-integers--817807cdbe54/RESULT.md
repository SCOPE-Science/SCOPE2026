# Complete classification of odd three-prime \(\varphi\)-practical integers

## Finding
A positive integer \(n\) is **\(\varphi\)-practical** when the polynomial \(X^n-1\) possesses a monic divisor in \(\mathbb Z[X]\) of every integer degree from \(0\) to \(n\). For odd \(n\) with exactly three distinct prime divisors, this holds **if and only if**
\[
n=3^a5^bq^c\quad(a,b,c\ge1,\ q\in\{7,11,13\}\text{ prime}),
\]
or \(n=255=3\cdot5\cdot17\). No numerical bounds on the exponents are assumed.

## Assumptions and scope
Let \(\varphi\) be Euler's totient. For \(m\ge1\), define the finite subset-sum set
\[
S(m)=\left\{\sum_{d\mid m}\epsilon_d\varphi(d):\epsilon_d\in\{0,1\}\right\},
\]
and let \(\Delta(m)\) be the largest difference between consecutive elements of \(S(m)\) in increasing order. Since \(X^m-1=\prod_{d\mid m}\Phi_d(X)\), with irreducible pairwise distinct integral cyclotomic factors, \(m\) is \(\varphi\)-practical precisely when \(S(m)=\{0,\ldots,m\}\).

All primes and exponents in this proof are ordinary positive integers; \(q\) always denotes a prime \(\ge7\).

## Proof
**1. A subset-sum gap lemma.** Order the positive coins \(w_1\le\cdots\le w_t\) and put \(P_{i-1}=\sum_{j<i}w_j\). If \(w_1=1\), the maximal gap between consecutive subset sums of all coins is at most
\[
\max\left(1,\max_{1\le i\le t}(w_i-P_{i-1})\right).
\]
Indeed, adjoining coin \(w_i\) unions the previous subset-sum set with its translate by \(w_i\); previous gaps do not increase and the joining gap is at most \(w_i-P_{i-1}\). For any *odd* divisor \(d>1\), every strict divisor \(e\mid d\) satisfies \(\varphi(e)<\varphi(d)\). Consequently the coins preceding \(\varphi(d)\) include all strict-divisor coins, giving \(P_{i-1}\ge d-\varphi(d)\). It follows that the maximal gap for odd \(m\) is at most
\[
\max\left(1,\max_{d\mid m}(2\varphi(d)-d)\right).
\]
Conversely, if \(2\varphi(m)>m\), the largest coin \(\varphi(m)\) exceeds the sum of all others, \(m-\varphi(m)\). Hence \(\Delta(m)\ge2\varphi(m)-m\).

**2. Three exact two-prime gap identities.** For all \(a,b,c\ge1\) and every prime \(q\ge7\),
\[
\begin{aligned}
\Delta(3^a5^b)&=3^{a-1}5^{b-1},\\
\Delta(3^aq^c)&=(q-4)3^{a-1}q^{c-1},\\
\Delta(5^bq^c)&=(3q-8)5^{b-1}q^{c-1}.
\end{aligned}
\]
The lower bounds are exactly \(2\varphi(m)-m\), from part 1. For the third upper bound, inspect the proper-divisor defects \(2\varphi(d)-d\): they are \(3\cdot5^{i-1}\) for \(d=5^i\), \((q-2)q^{j-1}\) for \(d=q^j\), and \((3q-8)5^{i-1}q^{j-1}\) for \(d=5^iq^j\). Each is at most the claimed top defect, as \(q\ge7\); the unit coin has defect \(1\).

For \(3^a5^b\) with \(a\ge2\), the corresponding defects are \(3^{i-1}\), \(3\cdot5^{j-1}\), and \(3^{i-1}5^{j-1}\), bounded by \(3^{a-1}5^{b-1}\). For \(3^aq^c\) with \(a\ge2\), they are \(3^{i-1}\), \((q-2)q^{j-1}\), and \((q-4)3^{i-1}q^{j-1}\); here \(q-2\le3(q-4)\). The gap lemma completes these two cases.

For the exceptional \(a=1\) cases, write \(r=5\) or \(r=q\) and inspect the coins of \(3r^j\). In nondecreasing order they occur as \(1,2\), followed for \(i=1,\ldots,j\) by the pair \((r-1)r^{i-1},\ 2(r-1)r^{i-1}\). The sum of all coins before the first coin of each pair is \(3r^{i-1}\). Each coin of this pair exceeds the preceding coin-prefix sum by exactly \((r-4)r^{i-1}\). Thus the gap lemma gives \(\Delta(3r^j)\le(r-4)r^{j-1}\), matching the largest-coin lower bound. The three identities follow.

**3. Necessary prime support and exceptional exponent pattern.** Let odd \(n\) have precisely three distinct prime divisors and be \(\varphi\)-practical. To represent degree \(2\), a totient coin of value \(2\) is necessary (the only smaller coin is \(\varphi(1)=1\)); among odd divisors this requires \(3\mid n\). To represent degree \(4\), a coin of value \(4\) is necessary: before introducing \(5\), the only coins smaller than \(4\) are \(1\) and \(2\), whose sum is \(3\), while other odd divisor totients are at least \(6\). Thus \(5\mid n\). Hence \(n=3^a5^bq^c\), where \(a,b,c\ge1\) and \(q\ge7\) prime.

Put \(T=3^{a-1}5^{b-1}q^{c-1}\). Then \(n=15qT\) and \(\varphi(n)=8(q-1)T\). The largest coin \(\varphi(n)\) must not leave an unattainable integer between the sum of other coins and itself, so \(2\varphi(n)-n\le1\). Thus \((q-16)T\le1\). This excludes \(q\ge19\). For \(q=17\), it forces \(T=1\), hence \(a=b=c=1\). The only remaining primes are \(7,11,13\) and the exceptional \(17\).

**4. Base examples.** For \(m=15\), the coins are \(1,2,4,8\), whence \(S(15)=[0,15]\cap\mathbb Z\). For \(q\in\{7,11,13,17\}\), the new coins in \(15q\) are \((q-1)\) times the old four. Therefore
\[
S(15q)=\bigcup_{t=0}^{15}\left([0,15]\cap\mathbb Z+(q-1)t\right),
\]
which equals \([0,15q]\cap\mathbb Z\) because \(q-1\le16\). This includes \(255\).

**5. Closure under all three prime-power extensions.** Suppose \(n=p^e m\), \(\gcd(p,m)=1\), and \(S(n)=[0,n]\cap\mathbb Z\). When the exponent of \(p\) rises from \(e\) to \(e+1\), exactly the coins \(p^e(p-1)\varphi(d)\), \(d\mid m\), are added. Thus \(S(pn)\) contains an interval of length \(n\) starting at each \(p^e(p-1)t\), \(t\in S(m)\). These intervals cover every degree from \(0\) to \(pn\), provided
\[
(p-1)\Delta(m)\le m.
\]
For \(n=3^a5^bq^c\), \(q\in\{7,11,13\}\), the three exact gap identities from part 2 reduce this sufficient condition respectively to
\[
2(3q-8)\le5q\quad(p=3),\qquad
4(q-4)\le3q\quad(p=5),\qquad
q-1\le15\quad(p=q).
\]
All hold for \(q\le13\). Starting from the base case \(15q\), increase the three exponents in any order to obtain all positive triples \((a,b,c)\). This completes sufficiency and the theorem. \(\square\)

## Verification
The standalone `verify.py` builds every divisor-totient coin by exact integer arithmetic, computes the subset-sum generating bitset, checks the claimed three-prime classification for eight values of \(q\) and all eight exponent triples with exponents in \(\{1,2\}\), and checks the exact two-prime gap formulae in a separate finite grid. This is a diagnostic and not a substitute for the preceding universal proof.

## Relationship to prior work
Thompson (2011) introduced \(\varphi\)-practical integers and studied adjoining prime factors. Pomerance, Thompson and Weingartner (2015), especially their lemmas on two-prime totient subset sums, provide closely related groundwork. The present result is a *complete odd three-distinct-prime classification, including all powers of all three primes and the isolated squarefree \(255\)*. Its three exact two-prime gap identities and all-exponent extension step are supplied above. The earlier papers' general growth and counting results do not explicitly state this complete classification. An equivalent result derivable or recorded elsewhere remains possible.

## Limitations
The classification applies only to **odd** integers with exactly three **distinct** prime factors. It makes no claim about all \(\varphi\)-practical integers, even integers, or odd integers with at least four prime factors. Finite verification checks only the stated finite grid. Publication priority has not been independently established.

## References
1. L. Thompson, *Polynomials with divisors of every degree*, arXiv:1111.5401v1 (publicly submitted 2011-11-23), https://arxiv.org/abs/1111.5401.
2. C. Pomerance, L. Thompson, A. Weingartner, *On integers n for which X^n-1 has a divisor of every degree*, arXiv:1511.03357v1 (publicly submitted 2015-11-11), https://arxiv.org/abs/1511.03357.
