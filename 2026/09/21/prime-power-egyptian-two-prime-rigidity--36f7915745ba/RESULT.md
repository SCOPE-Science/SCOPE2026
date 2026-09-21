# Two-prime rigidity for prime-power pseudoperfect and prime-power Giuga numbers

## Statement

For an integer \(n>1\), write
\[
E_+(n)=\sum_{r^j\mid n}\frac1{r^j}+\frac1n,
\qquad
E_-(n)=\sum_{r^j\mid n}\frac1{r^j}-\frac1n,
\]
where each sum is over all prime-power divisors \(r^j\) of \(n\), with \(j\ge1\).
Following Machacek, \(n\) is **prime-power pseudoperfect** when \(E_+(n)=1\), and a composite \(n\) is **prime-power Giuga** when \(E_-(n)\) is a positive integer.

Let
\[
n=p^a q^b,\qquad p<q\text{ primes},\qquad a,b\ge1.
\]
Then the following classifications hold.

**Theorem A (pseudoperfect side).**
\[
\boxed{E_+(n)=1\iff p=2\text{ and }q=2^a+1.}
\]
Thus the prime-power pseudoperfect integers with exactly two distinct prime factors are precisely
\[
\boxed{2^a(2^a+1)^b}
\]
with \(a,b\ge1\) and \(2^a+1\) prime. Necessarily \(a\) is a power of two, so the odd prime is a Fermat prime. The exponent \(b\) is unrestricted.

**Theorem B (Giuga side).**
\[
\boxed{E_-(n)\in\mathbb Z_{>0}\iff p=2,\ b=1,\ q=2^a-1.}
\]
Thus the prime-power Giuga integers with exactly two distinct prime factors are precisely
\[
\boxed{2^a(2^a-1)}
\]
where \(2^a-1\) is prime. Necessarily \(a\ge2\), and such an exponent \(a\) is prime. In particular, every two-prime-support prime-power Giuga number satisfies the stronger equation \(E_-(n)=1\).

Together, these results show that the Fermat- and Mersenne-prime constructions appearing as sufficient families in Machacek's 2018 paper are exhaustive at prime-support size two. They also expose an asymmetry: the Fermat-side odd prime may occur to any positive exponent, while the Mersenne-side odd prime is forced to occur exactly once.

## Proof

### Theorem A

Suppose first that \(p\ge3\). Then \(q\ge5\), and
\[
\sum_{i=1}^a\frac1{p^i}<\frac1{p-1}\le\frac12,
\qquad
\sum_{j=1}^b\frac1{q^j}<\frac1{q-1}\le\frac14,
\]
while
\[
\frac1n\le\frac1{pq}\le\frac1{15}.
\]
Hence
\[
E_+(n)<\frac12+\frac14+\frac1{15}=\frac{49}{60}<1,
\]
so a two-prime-support prime-power pseudoperfect number must have \(p=2\).

Now put \(n=2^a q^b\). The equation \(E_+(n)=1\) becomes
\[
1-2^{-a}+\frac{1-q^{-b}}{q-1}+2^{-a}q^{-b}=1.
\]
Therefore
\[
\frac{1-q^{-b}}{q-1}=2^{-a}(1-q^{-b}).
\]
Since \(b\ge1\), the factor \(1-q^{-b}\) is nonzero, so cancellation gives
\[
q-1=2^a.
\]
This proves necessity. Conversely, if \(q-1=2^a\), reversing the same identity gives \(E_+(2^a q^b)=1\) for every \(b\ge1\).

If \(2^a+1\) is prime, then \(a\) must be a power of two: if \(a=2^r m\) with odd \(m>1\), then \(2^a+1=(2^{2^r})^m+1\) is divisible by \(2^{2^r}+1\).

### Theorem B

Let \(T=E_-(n)\). Since \(n\) has at least two distinct prime divisors, \(T>0\) whenever it is an integer: already \(1/p-1/n>0\), and all other summands are positive.

If \(p\ge3\), then \(q\ge5\) and
\[
0<T<\frac1{p-1}+\frac1{q-1}\le\frac34,
\]
which is incompatible with \(T\in\mathbb Z_{>0}\). Hence \(p=2\).

For \(n=2^a q^b\),
\[
T=1-2^{-a}+\frac{1-q^{-b}}{q-1}-2^{-a}q^{-b}.
\]
Also
\[
0<T<1+\frac1{q-1}\le\frac32,
\]
so integrality forces \(T=1\). Thus
\[
\frac{1-q^{-b}}{q-1}=2^{-a}(1+q^{-b}),
\]
and clearing denominators gives
\[
2^a(q^b-1)=(q-1)(q^b+1).
\]
Equivalently,
\[
q^b(2^a-q+1)=2^a+q-1.
\]
Set
\[
c=2^a-q+1.
\]
The right side is positive, so \(c>0\). Since \(q\) is odd, \(c\) is even, hence \(c\ge2\). Substituting \(2^a=c+q-1\) into the previous equation yields
\[
c(q^b-1)=2(q-1),
\]
so
\[
c(1+q+\cdots+q^{b-1})=2.
\]
Both factors are positive integers and \(c\ge2\). Consequently
\[
c=2,\qquad 1+q+\cdots+q^{b-1}=1.
\]
Thus \(b=1\) and \(q=2^a-1\). Conversely, direct substitution shows that every \(2^a(2^a-1)\) with \(2^a-1\) prime has \(E_-(n)=1\).

## Consequences

1. Including one-prime support, every prime-power pseudoperfect number with at most two distinct prime divisors is either \(2^a\) or a number \(2^a(2^a+1)^b\) from Theorem A. There is no one-prime-support prime-power Giuga number.

2. Machacek proved that every term of OEIS A073935 greater than one is prime-power pseudoperfect, while the converse fails in general. His Lemma 2 characterizes A073935 by a recursive prime-factor condition. On exactly two-prime support, that condition reduces to \(q-1=2^a\). Theorem A therefore shows that the converse *does* hold on support size two. Hence any counterexample to the converse must have at least three distinct prime factors.

3. The known example pattern is explained exactly. On the pseudoperfect side, \(6,18,54,\ldots\), \(20,100,500,\ldots\), and \(272,4624,\ldots\) arise from the Fermat primes \(3,5,17,\ldots\). On the Giuga side, \(12,56,992,\ldots\) arise from the Mersenne primes \(3,7,31,\ldots\).

## Verification

`artifacts/verify.py` performs exact rational arithmetic over every ordered pair of distinct primes \(p<q\le200\) and every \(1\le a,b\le6\). It checks the definitions directly against both classifications. Across 37,260 parameter tuples it finds 18 pseudoperfect hits, 3 Giuga hits, and zero mismatches. The finite check is supporting evidence only; the theorems are proved above without a cutoff.

## Relation to prior literature and originality boundary

Machacek introduced prime-power pseudoperfect and prime-power Giuga numbers and proved several sufficient constructions. In particular, Proposition 5 produces prime-power pseudoperfect numbers by adjoining powers of a prime one above a known example, and produces a prime-power Giuga number when adjoining a prime one below. The paper then notes the special families \(2^k(2^k+1)\) for Fermat primes and \(2^k(2^k-1)\) for Mersenne primes. Current OEIS entries A283423 and A286497 likewise record these as sufficient families.

The present contribution is the converse at the smallest nontrivial prime support: no other two-prime-support solutions exist, the pseudoperfect odd-prime exponent is completely free, and the Giuga odd-prime exponent is forced to one. This also gives the support-two converse to Machacek's A073935 inclusion.

Originality is asserted only **to the best of our knowledge**. Targeted searches for the exact two-prime classifications, synonymous formulations, Fermat/Mersenne converses, and subsequent work citing the 2018 paper did not locate an equivalent theorem or a stronger result implying it. The closest later line located was work on \(\mu\)-Sondow numbers, whose reciprocal condition sums over distinct prime divisors rather than all prime-power divisors and therefore does not subsume these statements. The principal residual risk is an unindexed or differently phrased elementary observation in problem literature or sequence commentary.

## References

1. John Machacek, *Egyptian Fractions and Prime Power Divisors*, Journal of Integer Sequences 21 (2018), Article 18.3.7. https://cs.uwaterloo.ca/journals/JIS/VOL21/Machacek/mach4.pdf
2. OEIS A283423, *Prime power pseudoperfect numbers*. https://oeis.org/A283423
3. OEIS A286497, *Prime power Giuga numbers*. https://oeis.org/A286497
4. J. M. Grau, A. M. Oller-Marcén, and D. Sadornil, *On μ-Sondow numbers*, Acta Mathematica Hungarica 168 (2022/2023), 292–307; preprint https://arxiv.org/abs/2111.14211
