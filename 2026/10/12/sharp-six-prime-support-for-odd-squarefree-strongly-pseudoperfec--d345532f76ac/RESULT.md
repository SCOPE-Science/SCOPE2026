# Sharp six-prime support for odd squarefree strongly pseudoperfect numbers

## Finding
A positive integer \(N\) is **strongly pseudoperfect** if a set \(S\) of its positive divisors satisfies both \(d\in S\iff N/d\in S\) and \(\sum_{d\in S}d=2N\). For a positive integer \(N\), let \(\omega(N)\) be its number of distinct prime factors.

**Theorem.** Every odd squarefree strongly pseudoperfect integer \(N\) has \(\omega(N)\ge 6\). The bound is attained: \(N=937365=3\cdot5\cdot11\cdot13\cdot19\cdot23\) is strongly pseudoperfect. Equivalently, no odd squarefree integer with at most five prime factors satisfies the defining complementary-divisor condition, whereas one with six does.

## Assumptions and scope
All positive integers and divisors are ordinary rational integers. Squarefree means that every prime exponent is at most one. The theorem concerns *odd squarefree* integers only; it makes no claim about odd integers with repeated prime factors, nor about the numerically least odd squarefree example. The verification below combines an infinite elementary reduction with an **exhaustive**, fully bounded integer calculation of 87 cases, not an unbounded numerical search.

## Proof
Let \(N\) be an odd squarefree strongly pseudoperfect integer with \(k\) prime factors \(3\le p_1<\cdots<p_k\). Necessarily \(\sigma(N)\ge2N\), where \(\sigma\) denotes the sum of all positive divisors. Squarefreeness gives
\[
\frac{\sigma(N)}N=\prod_{i=1}^k\left(1+\frac1{p_i}\right).
\]
For \(k\le4\) this ratio is at most
\[
\left(1+\frac13\right)\left(1+\frac15\right)
\left(1+\frac17\right)\left(1+\frac1{11}\right)
=\frac{768}{385}<2,
\]
so \(k\le4\) is impossible. Here a product with fewer than four factors is even smaller.

Now suppose \(k=5\). Comparison with the five least available primes shows that \(p_1=3\), \(p_2=5\), and \(p_3=7\) are forced: otherwise the ratio above is at most one of
\[
\frac{20736}{12155}\quad(p_1\ge5),\qquad
\frac{4608}{2431}\quad(p_1=3,\ p_2\ge7),\qquad
\frac{24192}{12155}\quad(p_1=3,\ p_2=5,\ p_3\ge11),
\]
all strictly less than \(2\). (The displayed comparisons use, respectively, primes \(5,7,11,13,17\), primes \(3,7,11,13,17\), and primes \(3,5,11,13,17\).) Likewise the two remaining primes cannot start at \(23\), because even the product for \(3,5,7,23,29\) is \(9216/4669<2\). Thus
\[
N=105qr,\qquad q\in\{11,13,17,19\},\quad r>q\ \text{prime}.
\]
The inequality \(\sigma(N)\ge2N\) now reads
\[
192(q+1)(r+1)\ge210qr,
\quad\text{whence}\quad
r\le\frac{32(q+1)}{3q-32}.
\]
The integer upper bounds on \(r\), for \(q=11,13,17,19\) in order, are \(384,64,30,25\). Counting primes strictly between \(q\) and these bounds yields, respectively, \(71,12,3,1\) candidates, exactly **87** in total. This mathematically proves that no larger prime pair is relevant.

For any candidate \(N=105qr\), its 32 divisors form exactly 16 complementary pairs \(\{d,N/d\}\), one per divisor \(d<\sqrt N\); none is self-complementary since \(N\) is nonsquare. A reciprocal-closed selection of divisors sums to \(2N\) if and only if the *omitted* complementary pairs have weights \(d+N/d\) summing to
\[
\Delta=\sigma(N)-2N=192(q+1)(r+1)-210qr.
\]
The included standalone program `verify.py` enumerates **all** 87 proven candidate prime pairs; builds each exact set of 16 integer weights; and checks, both by integer bitset subset-sum recurrence and independently by a complete eight-versus-eight meet-in-the-middle enumeration, that \(\Delta\) is absent. The accompanying `cases.csv` contains every candidate, its exact \(\Delta\), and the nearest attainable sums below and above it. Both algorithms independently return the same exhaustive exclusion. Thus no five-prime odd squarefree example exists.

For sharpness set \(N_0=937365=3\cdot5\cdot11\cdot13\cdot19\cdot23\). Its divisor sum is \(\sigma(N_0)=1935360\). Omit from its divisors the five complementary pairs
\[
(55,17043),\ (57,16445),\ (65,14421),\ (143,6555),\ (165,5681).
\]
Every pair multiplies to \(N_0\), the ten omitted divisors are distinct, and their sum is \(60630\). Retaining every other positive divisor therefore gives a set closed under complementation with sum
\[1935360-60630=1874730=2N_0.\]
As the six prime factors of \(N_0\) are distinct, the lower bound is attained. \(\square\)

## Verification
Run `python3 verify.py` in the directory containing `cases.csv`. The program uses only the Python standard library. It cross-checks a prime sieve against independent trial division; confirms the complete case counts \((71,12,3,1)\); constructs all complement pairs algebraically; compares two exact subset-sum algorithms for every one of the 87 cases; checks `cases.csv` field for field; and independently verifies the six-prime omitted-pair witness. The actual output is in `check_output.txt`. Each step computes exact integers. The result for arbitrarily large odd squarefree integers follows only because the proof first restricts every potential five-prime case to these 87 candidates.

## Relationship to prior work
Wang and Zelinsky, *Strongly Pseudoperfect Numbers* (arXiv:2609.36068, first posted September 28, 2026), establish new infinite families and restrictions and explicitly identify \(937365\) as an odd squarefree strongly pseudoperfect number with six prime factors (§4). The present theorem credits that existing witness but adds a sharp **universal lower bound** on the number of prime factors for odd squarefree members. Their Theorems 5–6, Propositions 14–17 and Questions 18–21 do not state an exclusion of every five-prime example. McCormack and Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function* (arXiv:2312.11661, § on strong pseudoperfection), introduce related restrictions but do not supply the bounded 87-case support sieve. A published indexed result ruling out strongly pseudoperfect integers with \(\Omega(N)\le3\) does not cover the five-distinct-prime case. This comparison is not a proof that no equivalent unpublished or unindexed argument exists.

## Limitations
This theorem concerns the **least possible number of distinct prime factors**, not the least integer and not a density. The negative portion uses a small exhaustive exact certificate; its universal scope relies on the displayed inequalities proving the candidate list complete. No conclusion about all odd strongly pseudoperfect numbers or infinite primitive families follows. No independent audit has been performed.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068 (first version September 28, 2026), https://arxiv.org/pdf/2609.36068.
2. Tim McCormack and Joshua Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661, https://arxiv.org/pdf/2312.11661.
3. OEIS A334405, strongly pseudoperfect numbers, https://oeis.org/A334405.
