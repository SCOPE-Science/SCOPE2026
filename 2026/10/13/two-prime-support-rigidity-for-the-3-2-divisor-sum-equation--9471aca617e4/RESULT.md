# Two-prime-support rigidity for the \(3/2\) divisor-sum equation

## Finding
Let \(\sigma(m)=\sum_{d\mid m}d\) denote the ordinary sum of positive divisors, and let \(\omega(m)\) count distinct prime divisors, with \(\omega(1)=0\). For **every** positive integer \(m\) with \(\omega(m)\le2\),
\[
2\sigma(m)=3(m+1)
\quad\Longleftrightarrow\quad
m=3^a\bigl(3^{a+1}-4\bigr)
\quad\text{for an integer }a\ge1\text{ with }3^{a+1}-4\text{ prime}.
\]
Consequently each such solution has exactly two distinct prime factors, one of which is \(3\), and its other prime occurs with exponent one. Examples are \(15\), \(207\), \(19359\) and \(36472996363223648799\).

## Assumptions and scope
The equality is considered over all positive integers, without an upper bound. The symbol \(\omega\) counts **distinct** prime factors, not prime factors with multiplicity. No requirement is imposed on the primality of \((m-1)/2\). The theorem addresses the natural low-prime-support layer of the equation underlying OEIS A063906; integers having three or more distinct prime factors are outside its scope.

## Proof
Suppose \(m\ge1\), \(\omega(m)\le2\), and \(2\sigma(m)=3(m+1)\). The integer \(m\) is odd: for even \(m\), the right-hand side is odd and the left-hand side even. Also \(m\ne1\), because \(2\sigma(1)=2\ne6\).

If \(m=p^e\) for an odd prime \(p\) and \(e\ge1\), then
\[
\frac{\sigma(m)}m=\sum_{j=0}^{e}p^{-j}
<\frac{p}{p-1}\le\frac32,
\]
whereas the defining equality requires \(\sigma(m)/m=3(m+1)/(2m)>3/2\). Thus \(m\) has exactly two distinct odd prime factors, say
\[
m=p^a q^b,\qquad 3\le p<q,\qquad a,b\ge1.
\]
If \(p\ge5\), then \(q\ge7\) and multiplicativity gives
\[
\frac{\sigma(m)}m<\frac{p}{p-1}\frac{q}{q-1}
\le\frac54\frac76=\frac{35}{24}<\frac32,
\]
again contradicting the equation. Therefore \(p=3\), and \(q\ge5\).

Put \(T=3^{a+1}\). The exact divisor-sum formula is
\[
\sigma(3^a q^b)=\frac{T-1}{2}\cdot\frac{q^{b+1}-1}{q-1}.
\]
Substitution into \(2\sigma(m)=3(m+1)\), followed by multiplication by \(q-1\), yields the identity
\[
(T-q)(q^b-1)=4(q-1).\tag{1}
\]
In particular \(T-q\) is a positive integer. Dividing (1) by \(q^b-1\) and using
\[
\frac{q^b-1}{q-1}=1+q+\cdots+q^{b-1}
\]
shows that \(T-q=4/(1+q+\cdots+q^{b-1})\). If \(b\ge2\), its denominator is at least \(1+q\ge6\), making this positive integer strictly less than one. Hence \(b=1\), and (1) reduces to \(T-q=4\), or
\[
q=3^{a+1}-4.
\]
The integer \(q\) is prime by hypothesis on the prime factorization, proving necessity.

Conversely, take any \(a\ge1\) such that \(q=3^{a+1}-4\) is prime. Here \(q\ge5\), so \(q\ne3\) and \(m=3^a q\) has exactly two distinct prime divisors. Multiplicativity gives
\[
2\sigma(m)=(3^{a+1}-1)(q+1)
=3^{a+1}(q+1)-(q+1)
=3^{a+1}q+3
=3(m+1),
\]
using \(q+1=3^{a+1}-3\). This proves sufficiency and completes the classification. \(\square\)

## Verification
The accompanying standalone `verify.py` uses exact integer arithmetic to compute \(\sigma(m)\) and \(\omega(m)\) by independent divisor and prime sieves, enumerates both sides of the classification, and checks equality through an inclusive user-selected bound. Reproduce the stated default check with:

```text
python verify.py 1000000
```

The executed check examined every \(1\le m\le1000000\) with \(\omega(m)\le2\), finding exactly \(15,207,19359\) in both sets. There were \(367461\) integers in that layer in this interval. Separately, exhaustive trial division up to \(\lfloor\sqrt{10460353199}\rfloor\) certifies that \(q=3^{21}-4=10460353199\) is prime, giving the larger exact solution \(m=36472996363223648799\); the neighboring integer \((m-1)/2\) is divisible by \(102461\). The checks corroborate the algebraic proof; they do not replace it.

## Relationship to prior work
OEIS A063906 defines the exact equation and records the numbers \(3^a(3^{a+1}-4)\) when the cofactor is prime as an **included** family; it does not state that this family exhausts all solutions with at most two distinct prime factors. Guy and Shanks (1974) construct a special family of adjacent equal-divisor-sum integers with \(n=2r\) and \(n+1=3^a q\), where both \(r=(3^a q-1)/2\) and \(q=3^{a+1}-4\) must be prime. The present result concerns the standalone divisor-sum equation and imposes no condition on \(r\). The larger witness above has composite \(r\), demonstrating that this extra condition is not harmless.

Bege and Fogarasi (2009), section 3.4, list solutions to this exact divisor-sum equation, including \(15,207,19359\), without a classification by distinct prime-factor count. Benito (2007) studies \(\sigma(n)=\sigma(n+1)\) and documents the Guy–Shanks constructions, not a necessary-and-sufficient statement for arbitrary \(m\). A published classification of simultaneous equal-divisor-sum neighbors with at most two prime factors **counted with multiplicity** concerns a narrower, different pair problem and does not imply the result here.

## Limitations
The primality of \(3^{a+1}-4\) is an explicit necessary and sufficient condition, not a claim that infinitely many such primes exist. Solutions with \(\omega(m)\ge3\) are not classified; OEIS A063906 exhibits many of them. The result does not establish the Erdős–Sierpiński equation for any given \(m\), since that additionally requires the relevant neighbor to be prime in the Guy–Shanks construction. The cited older journal source is dated to a year and issue rather than a verified exact public day; the exact-date metadata uses the original OEIS entry dated 30 August 2001. Absence of a stronger result in the sources inspected is not a guarantee against unindexed earlier work.

## References
1. OEIS Foundation, A063906, “Numbers \(m\) such that \(m=2\sigma(m)/3-1\),” originally authored by Jason Earls, 30 August 2001; https://oeis.org/A063906.
2. R. K. Guy and D. Shanks, “A Constructed Solution of \(\sigma(n)=\sigma(n+1)\),” *Fibonacci Quarterly* 12 (1974), 299; https://www.fq.math.ca/Scanned/12-3/guy.pdf; DOI 10.1080/00150517.1974.12430740.
3. A. Bege and K. Fogarasi, “Generalized perfect numbers,” *Acta Universitatis Sapientiae, Mathematica* 1 (2009), 73–82; arXiv:1008.0155v1, https://arxiv.org/pdf/1008.0155.
4. L. Benito, “Solutions of the problem of Erdős–Sierpiński: \(\sigma(n)=\sigma(n+1)\),” arXiv:0707.2190v1 (15 July 2007), https://arxiv.org/pdf/0707.2190.
5. “Unique two-almost-prime solution of the Erdős–Sierpiński equation,” published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-unique-two-almost-prime-solution-of-the-erd-s-sierpi-ski-equatio--1ea62e4a9301.
