# Two-prime finiteness for even divisor-power integrality

## Finding
For every fixed **even** integer \(k\ge2\), let \(\sigma_k(n)=\sum_{d\mid n}d^k\). For any positive integers \(a,b\) and odd prime \(p\), put \(n=2^a p^b\). Then
\[
n\mid\sigma_k(n)\quad\Longleftrightarrow\quad
2^a\mid b+1\ \text{ and }\ p^b\mid S_{k,a},
\qquad S_{k,a}=\frac{2^{k(a+1)}-1}{2^k-1}.
\]
Every such solution satisfies \(a\le 2k-1\). Thus the solutions with exactly two prime supports, one of them \(2\), form an **effectively computable finite set for each fixed even** \(k\): factor \(S_{k,a}\) for \(1\le a\le2k-1\), and retain precisely the odd prime powers \(p^b\mid S_{k,a}\) with \(2^a\mid b+1\).

At the first even exponent, the complete classification is
\[
\boxed{\bigl\{2^a p^b:a,b\ge1,\ p\text{ odd prime},\ 2^a p^b\mid\sigma_2(2^a p^b)\bigr\}=\{10\}.}
\]

## Assumptions and scope
All variables \(k,a,b,p\) are integers subject to \(k\ge2\) even, \(a,b\ge1\), and \(p\ge3\) prime. The theorem concerns **divisibility of the sum of all divisor powers by the original integer**, not power-harmonic means, equality to a fixed multiple, or divisibility by the square of the integer. The prime-support condition is essential. This claim is not a classification of unrestricted solutions with three or more distinct prime factors, nor does it give a uniform bound in \(k\).

## Proof
**1. Exact local criterion.** Multiplicativity gives
\[
\sigma_k(2^a p^b)=S_{k,a}\bigl(1+p^k+\cdots+p^{kb}\bigr).
\]
Since \(S_{k,a}\) is odd and the second factor is congruent to \(1\pmod p\), the Chinese remainder theorem yields
\[
2^a p^b\mid\sigma_k(2^a p^b)
\iff 2^a\mid(1+p^k+\cdots+p^{kb})\ \text{and}\ p^b\mid S_{k,a}.
\]
For odd \(p\) and even \(k\), put \(u=p^k\). Then \(u\equiv1\pmod8\). For each positive integer \(m\), the geometric sum \(1+u+\cdots+u^{m-1}\) has \(2\)-adic valuation exactly \(\nu_2(m)\). Indeed, write \(m=2^s t\) with \(t\) odd. Factor the sum into \(1+u^{2^s}+\cdots+u^{(t-1)2^s}\), an odd integer, times
\[
\prod_{i=0}^{s-1}(1+u^{2^i}).
\]
Every factor in the product is congruent to \(2\pmod8\), so has valuation exactly one. Taking \(m=b+1\) proves \(\nu_2(1+p^k+\cdots+p^{kb})=\nu_2(b+1)\), and hence the claimed equivalence.

**2. Uniform exponent bound.** The local criterion implies \(b\ge2^a-1\). Since \(p\ge3\),
\[
p^b\ge3^{2^a-1}.
\]
For every integer \(k\ge2\), one has \(2^{2k}-1\ge k(2k+1)\): the initial case \(k=2\) is \(15\ge10\), and multiplying the lower bound by four and adding three proves the next case. Induction on \(a\ge2k\) therefore shows \(2^a-1\ge k(a+1)\). For \(a\ge2k\), this yields
\[
p^b\ge3^{2^a-1}>2^{2^a-1}\ge2^{k(a+1)}>S_{k,a}.
\]
But the local criterion also requires \(p^b\mid S_{k,a}\), impossible for positive \(S_{k,a}\). Thus \(a\le2k-1\); for each of these finitely many exponents there are only finitely many prime-power divisors of the explicit integer \(S_{k,a}\). The stated factorization algorithm is exact in both directions.

**3. Sharp classification for \(k=2\).** Now \(S_{2,a}=(4^{a+1}-1)/3\). If \(a=2\), then \(b\ge3\), so \(p^b\ge27>S_{2,2}=21\), contradicting divisibility. If \(a\ge3\), the inequality
\[
3^{2^a-1}>4^{a+1}>S_{2,a}
\]
holds at \(a=3\) (where \(3^7=2187>256\)) and persists inductively because the left side grows by a factor \(3^{2^a}>4\) when \(a\) increases by one, whereas \(4^{a+1}\) grows by only \(4\). Hence \(a=1\). Now \(S_{2,1}=5\), and \(p^b\mid5\) forces \((p,b)=(5,1)\). Conversely, \(\sigma_2(10)=(1+4)(1+25)=130\), which is divisible by \(10\). This proves the singleton classification. \(\square\)

## Verification
The accompanying `verify.py` uses only Python's standard library. It exactly factors all \(S_{k,a}\) at \(k=2\) and \(k=4\) throughout the proven bound \(1\le a\le2k-1\), independently recomputes the defining divisor-power sums, and compares with direct brute-force calculations of all even integers up to \(10000\) having precisely two prime supports. It also checks the valuation identity on \(2268\) parameter tuples and the exponent inequality at \(120\) pairs. Command: `python3 verify.py`. Expected certificate: `EXACT_CERTIFICATE_OK k2=[10] k4=[34] brute_ceiling=10000 valuation_checks=2268 bound_layers=120`. The general statements are proved above; these finite checks do not substitute for the infinite proof.

## Relationship to prior work
The integer set \(\{n:n\mid\sigma_2(n)\}\) has appeared in OEIS A046762 since at least December 11, 1999, and includes \(10\) together with values having more prime supports, such as \(60\). Luca and Ferdinands' 2006 Problem 11090 establishes infinitely many even solutions of \(n\mid\sigma_k(n)\) for each fixed \(k\ge2\) (as cited in Cai--Chen--Zhang, Lemma 5); the present finiteness assertion is specifically for the two-prime-support family and therefore does not contradict that theorem. Cai, Chen and Zhang's *Perfect numbers and Fibonacci primes* (arXiv:1310.0898, first posted October 3, 2013) proves finiteness for each fixed multiplier in \(\sigma_2(n)-n^2=Bn\) and classifies the multiplier-three case, and treats \(\sigma_3\)-divisibility for certain prime supports. A bound for a **fixed** multiplier \(B\), or classification of the multiplier-three subclass, does not imply finiteness when \(B=\sigma_2(n)/n-n\) varies; their \(\sigma_3\) statements address an odd, not even, exponent. The new statement isolates a bounded-support obstruction across **all even powers** and identifies its first complete case.

## Limitations
The bound \(a\le2k-1\) is not asserted optimal for arbitrary \(k\). The sieve may require factoring very large integers for large \(k\); this is an exact finite mathematical procedure, not a complexity bound. The case \(k=2\) is fully resolved within the specified two-prime-support domain only. No statement is made about unrestricted natural numbers or densities. Earlier uncatalogued literature and the complete text of the 2006 short note may contain related arguments; these have not been excluded by a universal novelty proof.

## References
1. Labos Elemer, OEIS A046762, *Numbers whose squared-divisor sum is divisible by the number*, first historical sequence record December 11, 1999: https://oeis.org/A046762 ; historical record https://oeis.org/history?seq=A046762&start=30 .
2. Florian Luca and John Ferdinands, *Problem 11090: Sometimes n divides sigma_k(n)*, American Mathematical Monthly 113 (2006), 372--373, https://www.jstor.org/stable/27641939 (full text not accessed).
3. Tianxin Cai, Deyi Chen and Yong Zhang, *Perfect numbers and Fibonacci primes*, arXiv:1310.0898 (2013), https://arxiv.org/html/1310.0898v2 (theorem statements, Lemma 5 and proofs examined).
