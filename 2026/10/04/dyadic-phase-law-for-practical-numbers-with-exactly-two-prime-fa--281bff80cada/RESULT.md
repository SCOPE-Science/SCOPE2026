# Dyadic phase law for practical numbers with exactly two prime factors
## Finding
Let \(P_2(X)\) count practical integers \(n\le X\) with exactly two distinct prime factors. Define
\[
m=\left\lfloor\frac{\log_2 X-1}{2}\right\rfloor,
\qquad
s=\frac{X}{2^{2m+1}}\in[1,4).
\]
Then, uniformly for the resulting dyadic phase \(s\),
\[
P_2(X)=\frac{\sqrt X}{\log X}
\left(\frac{8+4s}{\sqrt{2s}}+o(1)\right)
\qquad(X\to\infty).
\]
Hence the normalized count has no single limiting constant:
\[
\liminf_{X\to\infty}\frac{P_2(X)\log X}{\sqrt X}=8,
\qquad
\limsup_{X\to\infty}\frac{P_2(X)\log X}{\sqrt X}=6\sqrt2.
\]

## Assumptions and scope
An integer is practical when every integer from \(1\) through \(n\) is a sum of distinct positive divisors of \(n\). The count here is restricted to integers with exactly two distinct prime factors; multiplicities are unrestricted. Logarithms without a subscript are natural logarithms.

The classical Stewart--Sierpiński criterion is used as an input. In the two-prime case it says that a practical integer has the form \(2^a p^b\), where \(a,b\ge1\), \(p\) is odd prime, and
\[
p\le 1+\sigma(2^a)=2^{a+1}.
\]
The prime number theorem is the only asymptotic prime-distribution input. No assertion is made here about the full set of practical numbers.

## Proof
Write \(P_2(X)=A_1(X)+R(X)\), where \(A_1(X)\) counts the terms \(2^a p\) and \(R(X)\) counts those \(2^a p^b\) with \(b\ge2\). By the two-prime specialization of the Stewart--Sierpiński criterion,
\[
A_1(X)=\sum_{a\ge1}
\left(\pi\!\left(\min\left\{2^{a+1},X2^{-a}}\right\}\right)-1\right)_+,
\]
where the subtraction removes the prime \(2\).

With \(m\) and \(s\) as above, the two arguments in the minimum cross exactly between \(a=m\) and \(a=m+1\). Thus
\[
A_1(X)=
\sum_{a=1}^m\bigl(\pi(2^{a+1})-1\bigr)
+
\sum_{j\ge0}\bigl(\pi(s2^m2^{-j})-1\bigr)_+.
\]
The prime number theorem, applied to fixed-length tails of these dyadic sums and then followed by a geometric-tail estimate, gives uniformly for \(1\le s<4\),
\[
\sum_{a=1}^m\pi(2^{a+1})
=\frac{4\,2^m}{m\log2}(1+o(1)),
\]
and
\[
\sum_{j\ge0}\pi(s2^m2^{-j})
=\frac{2s\,2^m}{m\log2}(1+o(1)).
\]
The accumulated subtractions of \(1\) contribute only \(O(\log X)\). Hence
\[
A_1(X)=\frac{(4+2s)2^m}{m\log2}(1+o(1)).
\]

It remains to show that higher odd-prime exponents do not affect the leading term. For \(b\ge2\), every admissible prime satisfies
\[
p\le\min\left\{2^{a+1},\sqrt{X2^{-a}}}\right\}.
\]
There are at most \(O(\log X)\) possible exponents \(b\), so even after replacing primes by all integers,
\[
R(X)\ll (\log X)
\sum_{a\ge1}
\min\left\{2^{a+1},X^{1/2}2^{-a/2}}\right\}
\ll X^{1/3}\log X.
\]
The last sum is split at its balancing index and is a pair of geometric sums. Therefore
\[
R(X)=o\left(\frac{\sqrt X}{\log X}\right).
\]

Finally, \(\sqrt X=2^m\sqrt{2s}\) and
\[
\log X=(2m+1+\log_2 s)\log2=2m\log2\,(1+o(1)).
\]
Substitution yields
\[
\frac{P_2(X)\log X}{\sqrt X}
=\frac{8+4s}{\sqrt{2s}}+o(1).
\]
The phase function can be written as
\[
2\sqrt2\left(\sqrt s+\frac{2}{\sqrt s}\right).
\]
Its minimum on \([1,4]\) is \(8\) at \(s=2\), while its endpoint value is \(6\sqrt2\). Taking integer sequences with phase tending to any prescribed point of \([1,4]\) proves the stated liminf and limsup.

## Verification
The accompanying `verify.py` performs two independent finite checks. First, for every integer through \(500000\) with exactly two distinct prime factors, it tests practicality directly from the sorted divisor list by the complete-subset interval criterion and compares the result with the condition \(n=2^a p^b\) and \(p\le2^{a+1}\). It checked \(150785\) such integers and found \(847\) practical ones, with no disagreement.

Second, the script evaluates exact counts at nine dyadic phase samples with \(m\in\{12,15,18}\) and \(s\in\{1,2,3.5}\), and compares their normalized values with the displayed phase function. It returned
`VERIFY_OK bound=500000 support_two_checked=150785 practical_support_two=847 phase_samples=9`.
These finite computations are corroborative only; the infinite asymptotic is proved above from the exact criterion and the prime number theorem.

## Relationship to prior work
Weingartner's full-text treatment states the Stewart--Sierpiński characterization of practical numbers and proves the global asymptotic \(P(X)\sim cX/\log X\) for all practical numbers. Melfi's survey likewise records the structural criterion and the classical global distribution problem. These sources supply the structural input but do not state the fixed-two-prime phase law above.

The present theorem is also distinct from results for related notions such as \(\lambda^*\)-practical numbers. A focused database search for practical numbers with exactly two prime factors found the classical practical-number sequence and criterion but not the \(\sqrt X/\log X\) phase profile or the constants \(8\) and \(6\sqrt2\).

## Limitations
No effective numerical error term is claimed, and convergence of the normalized finite counts is slow because the proof uses the prime number theorem at dyadic scales. The original 1954 Stewart article was identified bibliographically but its full text was not directly inspected here; the exact criterion used in the proof was independently checked in later full-text sources. A differently phrased older derivation of the same fixed-support phase law could still have escaped the focused literature searches.

## References
1. A. Weingartner, *Practical numbers and the distribution of divisors*, arXiv:1405.2585v1, first public version 2014-05-11.
2. B. M. Stewart, *Sums of Distinct Divisors*, American Journal of Mathematics 76 (1954), 779--785, DOI 10.2307/2372651.
3. G. Melfi, *A survey on practical numbers* (1995), open-access full text inspected.
4. OEIS A005153, *Practical numbers*.
