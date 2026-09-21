# Same-model review

## Verdict

**PASS.** The classification closes the complete prime-support-\(\{2,p\}\) case for admirable numbers and converts several known sufficient constructions into an exhaustive converse theorem.

## Correctness

The proof was rederived directly from
\[
E=\sigma(2^a p^b)-2^{a+1}p^b
=(2^{a+1}-1)(1+p+\cdots+p^{b-1})-p^b.
\]

The main stress tests were:

- **Parity:** \(E\) is even only for odd \(b\), immediately excluding every even odd-prime exponent.
- **\(b=1\):** every possible subtracted divisor is either \(2^s\) or \(2^s p\). The first gives the binary-deviation family. The second forces \(2^{s+1}+1\mid2^{a+1}-1\); the exact order of \(2\) modulo \(2^{s+1}+1\) reduces the prime quotient to the Mersenne/perfect-divisor family plus the isolated case \(40\).
- **\(b\ge3\), low \(p\)-adic valuation:** splitting by \(u=v_p(2^{a+1}-1)\) gives contradictions for \(u=0\), while \(1\le u<b\) leaves only \(b=3\), \(u=1\), and \(p=2^{a+1}-1\).
- **\(b\ge3\), high \(p\)-adic valuation:** if \(u\ge b\), the admirable equation implies
  \[
  C(1+p+\cdots+p^{b-1})=2^h+1
  \]
  and
  \[
  h=v_2(1+p+\cdots+p^b)
   =v_2(p+1)+v_2(b+1)-1.
  \]
  The resulting upper bound on \(2^h+1\) is strictly smaller than the geometric sum, a contradiction.
- Each converse is checked by direct substitution.

Exact integer verification over 366,282 triples with \(1\le a\le18\), odd prime \(p<20000\), and \(1\le b\le9\) produced zero classification mismatches. A separate targeted scan of 22 high-\(p\)-adic-valuation candidates with \(a\le300\) produced no admirable hits. These checks support but do not replace the proof.

## Originality

The closest primary source is Firoozbakht--Hasler (2010), whose full paper was inspected. It supplies the main sufficient constructions:

- Theorem 1.1 gives \(2^{k-1}p\) solutions of \(\sigma(x)=2(x+m)\);
- Remark 1.4 identifies the proper-divisor case with admirable numbers;
- Proposition 1.6 gives the Mersenne-cube family;
- Theorem 1.14 contains the perfect-divisor construction.

Those known constructions are explicitly excluded from novelty. The proposed contribution is the converse statement that, among integers \(2^a p^b\), no other admirable numbers exist.

Searches covered `admirable numbers`, `2^a p`, `2^a p^b`, `p^3`, Mersenne formulations, the defining equation \(\sigma(n)=2(n+d)\), OEIS A111592 and related entries, and the current SCOPE archive. No exact or stronger two-prime-support converse was located.

The original J. M. Sachs article (The Arithmetic Teacher 7 (1960), 293--295, JSTOR 41184328) was not inspected in full text. Bibliographic information and later expository summaries were available. Since it is the original source of the terminology, it is the most concrete residual originality risk, though the much more structurally relevant 2010 paper does not state this converse. Originality is therefore only to the best of our knowledge.

## Value

The result closes a natural minimal-support slice completely. It explains why the conspicuous higher-power examples \(54,1372,476656,\ldots\) stop at odd-prime exponent \(3\), and why that exponent can occur only for a Mersenne prime. It also shows that the older construction families are not merely examples but exhaust all admirable numbers supported on one even prime and one odd prime.

The proof has a reusable mechanism: compare the \(p\)-adic valuation of the divisor-sum excess with the maximum \(p\)-exponent available in a divisor, and in the high-valuation branch convert the remaining equation into a sharp \(2\)-adic valuation identity for a geometric sum.

## Status

Same-model review: passed. Independent audit: not yet performed.
