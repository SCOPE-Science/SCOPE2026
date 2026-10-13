# Connected closure of reciprocal-square bi-unitary divisor sums

## Finding
For each integer \(n\ge1\), put
\[
F(n)=\sum_{d\mid_{**}n}\frac{1}{d^2},
\]
where \(d\mid_{**}n\) means that \(d\) is a **bi-unitary divisor** of \(n\), as defined below. Then
\[
\boxed{\overline{\{F(n):n\in\mathbb Z_{\ge1}\}}=[1,\zeta(2)]=[1,\pi^2/6].}
\]
The closure is taken in the real line. In particular its range closure has exactly one connected component. The theorem does not assert that every point in the interval is itself attained.

## Assumptions and scope
A divisor \(e\) of a positive integer \(u\) is *unitary* if \(\gcd(e,u/e)=1\). A divisor \(d\mid n\) is *bi-unitary* when the largest common unitary divisor of \(d\) and \(n/d\) is \(1\): that is, no integer greater than \(1\) is a unitary divisor of both \(d\) and \(n/d\). For a prime power \(p^a\) with \(a\ge1\), the admissible divisors \(p^j\), \(0\le j\le a\), exclude only the central divisor \(p^{a/2}\) when \(a\) is even. The bi-unitary divisor sum is multiplicative, and
\[
F(p^a)=\sum_{j=0}^{a}p^{-2j}-\mathbf{1}_{2\mid a}\,p^{-a},\qquad F(1)=1.
\]
Every \(p\) below denotes a rational prime. Define \(C_p=(1-p^{-2})^{-1}=p^2/(p^2-1)\).

## Proof
**1. Local limit factors and a prime-tail interval.** For any prime \(p\), the factors \(1\) and \(C_p\) belong to the closure of \(\{F(p^a):a\ge0\}\): choose \(a=0\), or let \(a\) tend to infinity through odd integers. Therefore finite products of arbitrarily selected factors \(C_p\) belong to the closure of \(\{F(n)\}\) with the corresponding finite prime support, by taking independently large odd prime-power exponents.

Let \(p_1=5<p_2=7<\cdots\) enumerate the primes at least \(5\), and put \(a_i=\log C_{p_i}>0\). These numbers have finite sum because \(\sum_p p^{-2}<\infty\). We verify the *no-gap inequalities*
\[
C_p\le\prod_{q>p}C_q\qquad\text{for every prime }p\ge5.
\tag{1}
\]
For the ten primes \(5\le p\le37\), each product below is strictly greater than \(C_p\), by rational arithmetic:

| \(p\) | Finite witness primes \(q>p\) |
| --- | --- |
| \(5\) | \(7,11,13,17,19\) |
| \(7\) | \(11,13,17,19,23\) |
| \(11\) | \(13,17\) |
| \(13\) | \(17,19\) |
| \(17\) | \(19,23\) |
| \(19\) | \(23,29\) |
| \(23\) | \(29,31\) |
| \(29\) | \(31,37\) |
| \(31\) | \(37,41\) |
| \(37\) | \(41,43\) |

For any prime \(p\ge41\), Ramanujan's fifth-prime bound \(R_5=41\) states that \(\pi(x)-\pi(x/2)\ge5\) whenever \(x\ge41\). Applying this to \(x=2p\), obtain five distinct primes \(p<q<2p\). For each such \(q\),
\[
C_q=1+\frac1{q^2-1}>1+\frac1{4p^2}.
\]
Hence
\[
\prod_{q>p}C_q\ge\prod_{p<q<2p}C_q
>\left(1+\frac1{4p^2}\right)^5
\ge1+\frac5{4p^2}
>1+\frac1{p^2-1}=C_p,
\]
where the last inequality holds because \(p^2>5\). This completes (1), without truncating the infinite prime range.

We use the elementary binary-series interval lemma: if \(b_i>0\), \(\sum_i b_i=B<\infty\), and \(b_i\le\sum_{j>i}b_j\) for all \(i\), then every \(t\in[0,B]\) equals \(\sum_i\epsilon_i b_i\), with \(\epsilon_i\in\{0,1\}\). Indeed, starting with residual \(t\), at stage \(i\) subtract \(b_i\) if the residual is greater than the remaining tail; otherwise subtract \(0\). The hypothesis guarantees a nonnegative new residual at most the remaining tail. The residual tends to zero because the tails do. Applying this lemma to \(b_i=\log C_{p_i}\) and exponentiating shows that *all* products \(\prod_{p\ge5}C_p^{\epsilon_p}\) fill the interval
\[
[1,T],\qquad T=\prod_{p\ge5}C_p
=\zeta(2)(1-2^{-2})(1-3^{-2})=\frac{\pi^2}{9}.
\tag{2}
\]
Finite truncations approximate each infinite product, and finite products are limits of actual bi-unitary divisor sums of integers coprime to \(6\). Thus \([1,T]\) lies in the closure of those values.

**2. Eight overlapping small-prime layers.** The local factor at \(2\) can take or approach \(1\), \(17/16=F(2^2)\), \(5/4=F(2)\), and \(4/3=C_2\). At \(3\), it can take or approach \(1\) and \(9/8=C_3\). By multiplying the interval in (2) by these independently realized or limiting factors, the full range closure contains each of eight intervals \([s,sT]\), for
\[
s\in\left\{1,\frac{17}{16},\frac98,\frac{153}{128},\frac54,\frac43,\frac{45}{32},\frac32\right\}.
\]
The multipliers are listed increasingly. Their largest consecutive ratio is exactly \(16/15\), and
\[
T=\frac{\pi^2}{9}>\frac{16}{15}
\]
by the elementary lower bound \(\pi>223/71\). Therefore the eight intervals overlap consecutively; their union is
\[
[1,(3/2)T]=[1,\pi^2/6].
\]
Finally, every bi-unitary divisor is an ordinary divisor, so for every \(n\ge1\),
\[
1\le F(n)\le\sum_{d\mid n}d^{-2}\le\sum_{d\ge1}d^{-2}=\zeta(2).
\]
This gives the reverse inclusion and the asserted equality of closures. \(\square\)

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The program independently enumerates bi-unitary divisors for all integers up to 256 and performs all 26 exact rational witness-factor checks for the ten initial primes, validates the local prime-power deletion law, evaluates the eight scale factors, verifies their sharp maximum ratio \(16/15\), and checks the rational Archimedean bound. Its output is:

`EXACT_CERTIFICATE_OK definition_checks=256 finite_tail_primes=10 witness_factors=26 boundary_intervals=8 max_ratio=16/15 endpoint=pi^2/6`

The infinite-prime assertion \(R_5=41\), the Euler product for \(\zeta(2)\), and the binary-series interval lemma are used mathematically in the proof; the finite program is not a proof of an infinite prime-distribution statement.

## Relationship to prior work
Tóth (2009) treats bi-unitary Euler and gcd-sum analogues, not the closure of this reciprocal divisor sum. The OEIS entry for the bi-unitary sum of divisors supplies arithmetic-function context and prime-power structure, not a negative-power range theorem. Defant (2015, arXiv:1507.02654) finds a disconnection transition for the **unitary** divisor sum at the reciprocal-square exponent, and Sanna (2015, arXiv:1507.08091) obtains three components for the closure of the **ordinary** reciprocal-square divisor sum. These results do not imply the present bi-unitary connectedness, because the allowed local factors differ. The bi-unitary exponent-two factor \(17/16\) is decisive in bridging the small-prime layers. The result is presented as a self-contained range classification, without claiming that the underlying divisor system or the no-gap lemma is new.

## Limitations
The theorem concerns the closure of the range, not whether every interval point is attained, and only the exponent \(2\) is addressed. Its analytic input is the unconditional classical Ramanujan fifth-prime bound; the finite certificate checks rational inequalities only. Earlier unindexed computations or classifications of this particular bi-unitary range may exist.

## References
1. L. Tóth, *On the Bi-Unitary Analogues of Euler's Arithmetical Function and the Gcd-Sum Function*, Journal of Integer Sequences **12** (2009), Article 09.5.2, https://cs.uwaterloo.ca/journals/JIS/VOL12/Toth2/toth5.pdf (published 2009-06-23).
2. OEIS A188999, *Bi-unitary sum of divisors of n*, https://oeis.org/A188999 (initial entry 2011-04-15).
3. C. Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654v1 (2015-07-09), https://arxiv.org/abs/1507.02654.
4. C. Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091v1 (2015-07-29), https://arxiv.org/abs/1507.08091.
5. S. Ramanujan, *A Proof of Bertrand's Postulate*, Journal of the Indian Mathematical Society **11** (1919), 181–182; the fifth Ramanujan prime is \(R_5=41\). See https://mathworld.wolfram.com/RamanujanPrime.html.
