# Near F-perfect numbers do not exist

## Result

Let
\[
\sigma_2(n)=\sum_{d\mid n} d^2.
\]
A positive integer \(n\) is called **near \(F\)-perfect** if there is a proper positive divisor \(d<n\) such that
\[
\sigma_2(n)-n^2-d^2=3n.
\]

**Theorem. There are no near \(F\)-perfect numbers.**

This closes the existence question for the \([2,3]\)-near-perfect specialization introduced in the recent near-\(F_k\)-perfect literature.

## Reciprocal-divisor reformulation

Let \(d\) be a proposed redundant divisor and put
\[
q=\frac nd>1.
\]
Using the divisor involution \(e\mapsto n/e\),
\[
\frac{\sigma_2(n)}{n^2}=\sum_{e\mid n}\frac1{e^2}.
\]
Hence the near \(F\)-perfect equation is equivalent to
\[
\boxed{\sum_{\substack{e\mid n\\ e>1,\ e\ne q}}\frac1{e^2}=\frac3n.}\tag{1}
\]
The proof is a consequence of the positivity of every term in (1).

## Proof

We separate the odd part and the 2-adic valuation of \(n\).

### 1. Odd \(n\)

If \(n\) is odd, then every divisor of \(n\), including \(d\), is odd. From
\[
\sigma_2(n)=n^2+d^2+3n
\]
we see that \(\sigma_2(n)\) is odd. Since each divisor square is odd, this means that \(\tau(n)\) is odd. Therefore \(n\) is a perfect square.

Suppose first that \(n\) has at least two distinct prime divisors \(p<r\). Because \(n\) is a square,
\[
p^2r^2\mid n.
\]
Among the two divisors \(p,r\), at most one can equal \(q\), so at least one of the terms \(1/p^2,1/r^2\) occurs in (1). But
\[
 n\ge p^2r^2\ge 9r^2>3r^2
\]
and, a fortiori, \(n>3p^2\). Thus either surviving term is strictly larger than \(3/n\), contradicting (1).

It remains to consider \(n=p^{2a}\) for an odd prime \(p\). If \(a\ge2\) and \(q\ne p\), then \(1/p^2\) occurs in (1), whereas
\[
p^{2a}>3p^2,
\]
a contradiction. Hence \(q=p\). If \(a\ge3\), the term \(1/p^4\) then survives, but \(p^{2a}>3p^4\), again impossible. The two remaining exponents are immediate:

- If \(n=p^2\), then \(q\in\{p,p^2\}\). Equation (1) becomes respectively \(p^{-4}=3p^{-2}\) or \(p^{-2}=3p^{-2}\), both impossible.
- If \(n=p^4\), the preceding argument forces \(q=p\), and (1) gives
  \[
  p^{-4}+p^{-6}+p^{-8}=3p^{-4},
  \]
  i.e. \(1+p^{-2}+p^{-4}=3\), impossible for \(p\ge3\).

Thus no odd near \(F\)-perfect number exists.

### 2. Exactly one factor of 2

Write \(n=2m\) with \(m\) odd. If \(n>12\) and \(q\ne2\), the term \(1/4\) occurs in (1), which would give
\[
\frac14\le\frac3n<\frac14,
\]
a contradiction. Therefore for \(n>12\) we must have \(q=2\).

Assume first that \(m\) has two distinct prime divisors \(p<r\). Then both \(1/p^2\) and \(1/r^2\) occur in (1), while \(m\ge pr\). Hence
\[
\frac1{p^2}+\frac1{r^2}\le \frac3{2m}\le\frac3{2pr}.
\]
After multiplying by \(2p^2r^2\), this requires
\[
2(p^2+r^2)\le3pr,
\]
contradicting \(p^2+r^2\ge2pr\).

So \(m=p^a\). The surviving term \(1/p^2\) in (1) yields
\[
\frac1{p^2}\le\frac3{2p^a},
\]
so \(a\le2\). For \(a=1\), equation (1) is
\[
\frac1{p^2}+\frac1{(2p)^2}=\frac3{2p},
\]
which gives \(5=6p\). For \(a=2\), it is
\[
\frac54\left(\frac1{p^2}+\frac1{p^4}\right)=\frac3{2p^2},
\]
which gives \(p^2=5\). Neither is possible.

The only cases with \(n\le12\) and \(v_2(n)=1\) are \(n=2,6,10\). Direct substitution gives
\[
\sigma_2(n)-n^2-3n=-5,-4,0,
\]
respectively, so none is the square of a positive proper divisor.

### 3. At least two factors of 2

Now assume \(4\mid n\). If \(q\ne2\), then \(1/4\) survives in (1), so \(n\le12\). If \(q=2\), then the divisor \(4\ne q\) survives and
\[
\frac1{16}\le\frac3n,
\]
so \(n\le48\). Therefore every remaining possibility is among the multiples of four up to 48.

For these twelve integers, the quantity that would have to equal \(d^2\) is:

| \(n\) | \(\sigma_2(n)-n^2-3n\) |
|---:|---:|
| 4 | -7 |
| 8 | -3 |
| 12 | 30 |
| 16 | 37 |
| 20 | 86 |
| 24 | 202 |
| 28 | 182 |
| 32 | 245 |
| 36 | 507 |
| 40 | 490 |
| 44 | 494 |
| 48 | 962 |

None is the square of a positive divisor. This exhausts the case \(4\mid n\), and proves the theorem. \(\square\)

## Context

Cai, Chen and Zhang introduced \(F\)-perfect numbers through
\[
\sigma_2(n)-n^2=3n
\]
and classified them as products of two adjacent odd-index Fibonacci primes when both factors are prime. Their theorem motivates asking how stable this equation is under deleting one proper-divisor square.

Jeba, Roy, Mahanta and Saikia later formalized exactly that deletion as a near \(F\)-perfect number, and more generally introduced \([k,\ell]\)-near-perfect numbers. Their 2025 paper proves nonexistence for several substantial families, including prime powers, \(2^a p\), \(2p^a\), \(2^a p^b\) with even \(b\), and several odd two-prime or squarefree configurations. Its concluding remarks specifically leave broader characterizations with more than two prime factors as a direction for further work. The theorem above removes all remaining cases when \((k,\ell)=(2,3)\).

The reciprocal identity (1) also supplies a general elementary mechanism: for any \([2,\ell]\)-near-perfect number with the same notation,
\[
\sum_{\substack{e\mid n\\e>1,\ e\ne q}}e^{-2}=\frac\ell n.
\]
In particular, if \(4\mid n\), then either \(q\ne2\) and \(n\le4\ell\), or \(q=2\) and \(n\le16\ell\). For \(\ell=3\), this is exactly the finite reduction used above.

## Verification

`artifacts/verify.py` independently evaluates the finite core \(4\mid n\le48\) by exact integer arithmetic and also performs a direct exact sieve scan through \(10^6\). The finite core has no candidate redundant divisor, and the larger scan finds zero near \(F\)-perfect numbers. The theorem itself does not depend on the \(10^6\) scan.

## Originality and limitations

To the best of our knowledge, the global nonexistence theorem and the reciprocal-divisor proof mechanism have not previously been stated for near \(F\)-perfect numbers. The complete 2025 paper was checked against the claim, including its theorems on prime-power and two-prime forms and its concluding remarks. Searches for the exact equation, the names “near \(F\)-perfect” and “\([2,3]\)-near-perfect”, synonymous divisor-deletion formulations, and stronger nonexistence statements did not locate an equivalent or stronger result. The current SCOPE archive was also checked for semantic overlap.

The main residual originality risk is terminology: an equivalent elementary observation could occur in older divisor-sum literature without the later near-\(F\)-perfect name. No concrete source suggesting such prior coverage was found. No inaccessible primary source was identified that materially threatens the claim.

## References

1. T. Cai, D. Chen, Y. Zhang, “Perfect numbers and Fibonacci primes (I),” *International Journal of Number Theory* 11 (2015), 159–169. DOI: 10.1142/S1793042115500098. Preprint: https://arxiv.org/abs/1310.0898
2. F. Jeba S., A. Roy, P. J. Mahanta, M. P. Saikia, “On near \(F_k\)-perfect and deficient \(F_k\)-perfect numbers,” *INTEGERS* 25 (2025), #A86. https://math.colgate.edu/~integers/z86/z86.pdf
3. F. Jeba S., A. Roy, M. P. Saikia, “Deficient and near \(F_k\)-perfect numbers,” conference abstract, RMS 2023. https://event.iitg.ac.in/rms2023/abs_contri/Number-Theory-All.pdf
