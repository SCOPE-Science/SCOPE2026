# No reciprocal sixth-cyclotomic divisibility and a sharp squarefree gcd-sum support bound

## Finding

Let \(g(t)=t^{2}-t+1\). There do not exist integers \(a,b\ge 2\) such that both \(a\mid g(b)\) and \(b\mid g(a)\). Equivalently, the directed graph on integers at least two, with \(u\to v\) when \(u\mid g(v)\), has neither loops nor directed two-cycles.

For any positive integer \(n\), put
\[
\mathcal H(n)=\sum_{j=1}^{n}\frac{1}{\gcd(n,j)}.
\]
If \(n>1\) is squarefree and \(\mathcal H(n)\) is an integer, then \(\omega(n)\ge3\), where \(\omega\) counts the distinct prime factors. This bound is sharp: the three primes \(349,121453,9710803\) have product \(411612748708891\), with
\[
\mathcal H(411612748708891)=410433300314317.
\]

## Assumptions and scope

The mutual-divisibility theorem holds for all integers \(a,b\ge2\), with neither a primality nor a coprimality hypothesis. An edge means divisibility of \(g(u)\) by the *destination* \(v\); the edge direction is fixed throughout. The integrality corollary assumes \(n\) is squarefree and \(n>1\). No assertion is made for arbitrary prime-power exponents or for three-cycles other than the explicit witness.

## Proof

**Absence of loops.** For any integer \(a\ge2\), \(g(a)\equiv1\pmod a\). Therefore \(a\nmid g(a)\).

**Absence of two-cycles.** Suppose that \(a,b\ge2\) satisfy both divisibilities. Equality of the two integers is excluded by the loop observation, so after interchanging them let \(2\le a<b\). Set
\[
z=\frac{g(a)}{b}.
\]
The second divisibility ensures that \(z\) is a positive integer. Since \(g(a)=a^{2}-a+1<a^{2}\) for \(a\ge2\), the inequality \(b>a\) implies \(1\le z<a\).

From \(bz=g(a)\equiv1\pmod a\), calculate
\[
z^{2}g(b)=(bz)^{2}-z(bz)+z^{2}
\equiv1-z+z^{2}=g(z)\pmod a.
\]
The original assumption \(a\mid g(b)\) now implies \(a\mid g(z)\); also \(z\mid g(a)\) follows from the definition of \(z\). If \(z=1\), the first implication says \(a\mid g(1)=1\), a contradiction. Otherwise \((z,a)\) is another admissible pair, both entries at least two, and its maximum \(a\) is strictly smaller than the maximum \(b\) of the original pair. Choosing a counterexample of least maximum gives a contradiction. This proves the claim without a primality assumption.

**Reciprocal-gcd sum.** Reindexing by \(d=\gcd(n,j)\) gives
\[
\mathcal H(n)=\sum_{d\mid n}\frac{\varphi(n/d)}{d},
\]
where \(\varphi\) is Euler's totient. This divisor sum is multiplicative in \(n\). Consequently, for squarefree \(n=\prod_{p\mid n}p\),
\[
\mathcal H(n)=\prod_{p\mid n}\left(p-1+\frac1p\right)
=\frac{\prod_{p\mid n}g(p)}{n}.
\]
Suppose this value is integral. For each prime \(p\mid n\), the divisibility \(p\mid\prod_{q\mid n}g(q)\) implies that \(p\mid g(q)\) for some prime \(q\mid n\). The loop observation forces \(q\ne p\). Choose such a \(q\) for each \(p\), directing an edge from \(p\) to \(q\). We obtain a nonempty finite directed graph in which every vertex has one chosen outgoing edge. Following edges must eventually enter a directed cycle. Its length is neither one nor two by the preceding arguments. Hence there are at least three distinct primes dividing \(n\).

**Sharpness.** Define \(p_1=349\), \(p_2=121453\), \(p_3=9710803\). Each is prime, as can be checked by trial division up to its integer square root. Exact arithmetic yields
\[
g(p_1)=p_2,\qquad p_3\mid g(p_2),\qquad p_1\mid g(p_3).
\]
Thus \(N=p_1p_2p_3\) divides \(g(p_1)g(p_2)g(p_3)\). The exact quotient is \(410433300314317\), as asserted. This demonstrates attainability of the lower bound three; it is not presented as a new minimality classification.

## Verification

A standalone Python 3 program, `verify.py`, uses only the standard library. It tests all possible larger divisors \(b\mid g(a)\) for \(2\le a\le5000\), checks the modular descent identity and the absence of a reciprocal divisibility pair in those cases, verifies the three witness integers are prime by exact trial division, and checks the directed three-cycle and the reciprocal-gcd quotient using integer arithmetic. Its observed result is:

```
VERIFY_OK quotient_divisor_cases 17642 three_cycle (349, 121453, 9710803) value 410433300314317
```

The infinite statements rely on the descent and graph proofs, not on finite exhaustion.

## Relationship to prior work

De Koninck and Letendre (2026), Section 5, Proposition 1, analyze the system \(ap=g(q)\), \(bq=g(p)\) for distinct odd primes \(p,q\) and bound the number of solutions up to a height. The mutual-divisibility theorem here establishes that their first-power/first-power two-cycle system has **no** solutions, a logically stronger conclusion than that bound. Their Section 5 also allows cycles involving squared-prime factors; those cases are not ruled out here. Their Section 1 notes the general lower bound \(\omega(n)\ge2\) for nontrivial integral values. The theorem above strengthens the bound to three specifically for squarefree inputs.

OEIS A317480 lists integers with integral reciprocal-gcd sum and the corresponding computational formula; the present contribution is an all-integer reciprocal-divisibility obstruction, not a new sequence value. The descent is an instance of classical integer descent/Vieta-jumping techniques, but the precise cyclotomic no-two-cycle statement and its implication for this reciprocal-gcd problem were not found in the inspected relevant sources.

## Limitations

This does not forbid two-cycles of the *prime-power* divisibility graphs when at least one vertex carries exponent two. It does not classify non-squarefree integers with integral reciprocal-gcd sums or establish infinitude of such integers. It does not determine whether all such squarefree integers arise from simple directed cycles instead of more general functional graphs. The finite checker does not certify the infinite theorem. Earlier or unindexed proofs of the same elementary descent could exist; no independent audit has been performed.

The polynomial's negative linear term matters: for \(t^{2}+t+1\), the integers \(3\) and \(13\) do form a reciprocal divisibility pair, since \(3^{2}+3+1=13\) and \(13^{2}+13+1=183\) is divisible by \(3\).

## References

1. Jean-Marie De Koninck and Patrick Letendre, *The Integer Values of* \(\sum_{i=1}^{n}1/\gcd(n,i)\), arXiv:2610.10572v1 (publicly available 2026-10-04), especially Sections 1, 2 and 5. https://arxiv.org/html/2610.10572v1
2. OEIS A317480, *Numbers \(m\) such that \(\sum_{k=1}^{m}1/\gcd(k,m)\) is an integer*, including its references and formula. https://oeis.org/A317480
