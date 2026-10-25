# The sharp six-prime lower bound for odd squarefree strongly pseudoperfect integers

## Finding
Let \(n\) be a positive odd squarefree integer. Call \(n\) *strongly pseudoperfect* when some set \(S\) of positive divisors is invariant under \(d\mapsto n/d\) and satisfies \(\sum_{d\in S}d=2n\). Then
\[
\boxed{\ n\text{ strongly pseudoperfect and odd squarefree}\ \Longrightarrow\ \omega(n)\ge 6.\ }
\]
The bound on the number \(\omega(n)\) of distinct prime factors is attained by \(n=937365=3\cdot5\cdot11\cdot13\cdot19\cdot23\). This is a *sharp necessary lower bound*, not a characterization of all six-prime integers.

## Assumptions and scope
All variables denote positive integers. Squarefree means no squared prime divides \(n\). For squarefree \(n>1\), complementary divisors \(d,n/d\) form disjoint two-element pairs. If \(n\) is strongly pseudoperfect, then necessarily \(\sigma(n)\ge 2n\), where \(\sigma(n)\) is the sum of all positive divisors. The case \(n=1\) does not satisfy the defining sum.

## Proof
**Step 1: Reduce five-prime support to four choices.** Write the distinct odd primes dividing a squarefree \(n\) in increasing order. For at most four primes, \(\sigma(n)/n\le (4/3)(6/5)(8/7)(12/11)=2304/1155<2\), and so no such \(n\) is strongly pseudoperfect. For exactly five primes, the factor \((p+1)/p\) decreases as \(p\) increases. The following upper bounds are each strictly below two:
\[
\begin{gathered}
\prod_{p\in\{5,7,11,13,17\}}(1+1/p),\qquad
\prod_{p\in\{3,7,11,13,17\}}(1+1/p),\\
\prod_{p\in\{3,5,11,13,17\}}(1+1/p),\qquad
\prod_{p\in\{3,5,7,23,29\}}(1+1/p).
\end{gathered}
\]
Consequently a five-prime candidate satisfying \(\sigma(n)\ge2n\) must be \(n=3\cdot5\cdot7\cdot s\cdot t=105st\), where \(s\in\{11,13,17,19\}\) is prime and \(t>s\) is prime. Here \(\sigma(n)=192(s+1)(t+1)\). The necessary inequality \(\sigma(n)\ge2n\) becomes
\[
(18s-192)t\le192(s+1),
\]
and its coefficient is positive for all four choices of \(s\). Thus \(t\) is bounded respectively by \(384,64,30,25\), leaving \(71,12,3,1\) prime choices: exactly \(87\) integers.

**Step 2: Exhaust the exact complement-pair equation.** Put \(m=105s\), so \(n=mt\) and \(\gcd(m,t)=1\). Each of the \(16\) complementary divisor pairs of \(n\) is uniquely of the form \(\{d,(m/d)t\}\), for one \(d\mid m\), and has sum
\[
w_d=d+(m/d)t.
\]
A complement-closed divisor set of total sum \(2n\) exists **if and only if** \(2mt\) is a subset sum of the \(16\) integers \(w_d\), with each pair selected at most once. For all \(87\) admissible \((s,t)\), the exact subset-sum test returns false. This is a *finite exhaustive proof*, not extrapolation from a bounded search over arbitrary integers: Step 1 proves that the \(87\) cases exhaust the entire five-prime domain. The standalone `verify.py` provides two exact independent subset-sum implementations, a meet-in-the-middle algorithm and integer-bitset dynamic programming, with explicit candidate enumeration and assertions.

**Step 3: Exhibit six-prime attainment.** For \(n=937365\), the complete divisor sum is \(\sigma(n)=1935360\). Omit the following five complementary divisor pairs:
\[
(55,17043),\ (57,16445),\ (65,14421),\ (143,6555),\ (165,5681).
\]
Every pair has product \(937365\), and their ten members are distinct. Their sum is \(60630=1935360-2\cdot937365\). Retaining every other divisor yields a complement-closed set summing to \(2n\). Thus the lower bound six is attained.

## Verification
Execute `python3 verify.py` with the standard-library Python interpreter. Successful output begins `VERIFY_OK` and reports \(87\) five-prime candidates, grouped as \(71+12+3+1\), and the five omitted pairs in the six-prime witness. The checker independently compares the complement-pair formula with direct divisor enumeration and tests both exact subset-sum methods on every candidate. A separate check verifies the six-prime witness by explicitly summing its retained divisor set. Its candidate-table digest is `b065650fcef91db28f601f96cbbac340a0773aa72abd5d5068ebb84da8b23636` (SHA-256 of the checker's ordered Python tuple-list representation). The finite computation is exhaustive only **after** Step 1's unbounded mathematical reduction.

## Relationship to prior work
Wang and Zelinsky, *Strongly Pseudoperfect Numbers* (first public preprint September 28, 2026, arXiv:2609.36068v1), introduce restrictions and constructions and explicitly record the six-prime squarefree example \(937365\). Their analyzed propositions and data do not state that fewer than six distinct factors are impossible for odd squarefree integers. McCormack and Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function* (arXiv:2312.11661), introduce the complement-closed definition and congruence obstructions but do not state the sharp five-prime exclusion. OEIS A334405 lists strongly pseudoperfect integers and a general coefficient method; its displayed finite table does not by itself imply an unbounded prime-support lower bound. The additional contribution here is the sharp lower bound, via a complete necessary-condition reduction to \(87\) checked cases; the six-prime example itself is prior work.

## Limitations
Only **odd squarefree** integers are addressed; odd integers with repeated primes and even integers are excluded. A specific six-prime example attains the bound, but not every six-prime product is strongly pseudoperfect. The exclusion of five-prime products uses a short, explicitly reproducible exact finite calculation. Published priority has not been independently established against every possible equivalently formulated older theorem.

## References
1. A. Wang and J. Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v1, September 28, 2026. https://arxiv.org/html/2609.36068v1
2. T. McCormack and J. Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661. https://arxiv.org/abs/2312.11661
3. OEIS A334405, strongly pseudoperfect integers. https://oeis.org/A334405
