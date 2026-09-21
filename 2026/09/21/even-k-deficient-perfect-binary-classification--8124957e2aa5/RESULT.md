# Binary classification of even exactly \(k\)-deficient-perfect numbers with two prime factors

## Statement

For a positive integer \(n\), write \(\sigma(n)\) for the sum of its positive divisors. Following Chen and Aursukaree--Pongsriiam, call \(n\) **exactly \(k\)-deficient-perfect** if there are \(k\) distinct proper divisors \(d_1,\dots,d_k\) such that
\[
\sigma(n)=2n-(d_1+\cdots+d_k).
\]

Let
\[
n=2^a p^b,\qquad a,b\ge 1,
\]
where \(p\) is an odd prime, and put
\[
M=2^{a+1}-1,\qquad t=p-M.
\]
For a nonnegative integer \(u\), let \(s_2(u)\) denote the number of \(1\)'s in its binary expansion.

### Theorem

The integer \(2^a p^b\) is exactly \(k\)-deficient-perfect for some \(k\) if and only if
\[
\boxed{\,M<p<2M\,}.
\]
When this occurs, the deficient-divisor set is unique. It is
\[
\mathcal D=
\{2^i:\text{the \(i\)-th binary digit of }t\text{ is }1\}
\;\cup\;
\{2^i p^j:1\le j\le b-1,\ \text{the \(i\)-th binary digit of }t-1\text{ is }1\},
\]
and hence the unique value of \(k\) is
\[
\boxed{\quad k=s_2(t)+(b-1)s_2(t-1).\quad}
\]

Thus every even exactly \(k\)-deficient-perfect number having exactly two distinct prime factors is classified by one prime in the interval
\[
2^{a+1}-1<p<2^{a+2}-2
\]
and a binary-weight formula.

## Proof

Set
\[
\Delta=2n-\sigma(n).
\]
Since
\[
\sigma(2^a p^b)=
(2^{a+1}-1)(1+p+\cdots+p^b)
=M(1+p+\cdots+p^b)
\]
and \(M+1=2^{a+1}\), direct cancellation gives
\[
\Delta
=p^b-M(1+p+\cdots+p^{b-1}).
\]
With \(t=p-M\), this becomes
\[
\boxed{\quad
\Delta=t+(t-1)(p+p^2+\cdots+p^{b-1}).
\quad} \tag{1}
\]

Suppose first that \(n\) is exactly \(k\)-deficient-perfect. Then \(\Delta>0\). If \(p\le M\), the displayed formula before (1) is nonpositive, so necessarily \(p>M\). Also \(\Delta<p^b\).

Every chosen deficient divisor is positive and at most their sum \(\Delta\), hence is \(<p^b\). Therefore no chosen divisor is divisible by \(p^b\). Group the chosen divisors according to their \(p\)-adic exponent. For \(0\le j\le b-1\), let
\[
A_j=\sum 2^i,
\]
where the sum runs over those selected divisors of the form \(2^i p^j\). Since \(0\le i\le a\),
\[
0\le A_j\le 1+2+\cdots+2^a=M<p.
\]
The deficient-divisor equation is therefore a genuine base-\(p\) expansion:
\[
\Delta=A_0+A_1p+\cdots+A_{b-1}p^{b-1}.
\]
Equation (1) is another base-\(p\) expansion, because
\[
0\le t-1<t<p.
\]
Uniqueness of base-\(p\) digits forces
\[
A_0=t,\qquad A_j=t-1\quad(1\le j\le b-1). \tag{2}
\]
In particular \(t=A_0\le M\), so \(p\le2M\). Since \(p\) is odd whereas \(2M\) is even, this is
\[
M<p<2M.
\]

Conversely, assume \(M<p<2M\). Then
\[
0<t<M,\qquad 0\le t-1<M.
\]
Both \(t\) and \(t-1\) have unique binary expansions using the powers
\[
1,2,\ldots,2^a.
\]
Choose the divisors specified in the theorem: the binary digits of \(t\) in the \(p^0\)-layer and the binary digits of \(t-1\) in every layer \(p^j\), \(1\le j\le b-1\). They are distinct proper divisors of \(n\), and by (1) their sum is exactly \(\Delta\). Thus \(n\) is exactly \(k\)-deficient-perfect.

Finally, (2) plus uniqueness of binary expansion shows that no other deficient-divisor set is possible, and counting its elements gives
\[
k=s_2(t)+(b-1)s_2(t-1).
\]
This proves the theorem.

## Consequences

Because \(p\) and \(M\) are odd, \(t\) is a positive even integer. Hence
\[
1\le s_2(t),s_2(t-1)\le a,
\]
so every qualifying number satisfies the sharp range
\[
\boxed{b\le k\le ab.}
\]

For \(b=1\), exact \(1\)-deficient-perfectness is equivalent to \(s_2(t)=1\), hence
\[
p=M+2^s=2^{a+1}+2^s-1,\qquad 1\le s\le a,
\]
which recovers the two-prime even deficient-perfect family classified by Tang--Ren--Li.

For \(b\ge2\), the lower endpoint \(k=b\) occurs exactly when \(t=2\), i.e.
\[
p=2^{a+1}+1.
\]
The upper endpoint \(k=ab\) occurs exactly when \(t=M-1\), i.e.
\[
p=2M-1=2^{a+2}-3.
\]

Bertrand's postulate supplies a prime \(p\) with \(M<p<2M\) for every \(M>1\). Therefore, for every pair \(a,b\ge1\), there is at least one odd prime \(p\) such that \(2^a p^b\) is exactly \(k\)-deficient-perfect for the uniquely determined \(k\) above.

The theorem also gives compact fixed-\(k\) slices. For exactly \(2\)-deficient-perfect numbers of this form:
- \(b=1\): \(t\) has binary weight \(2\);
- \(b=2\): \(t=2\), equivalently \(p=2^{a+1}+1\);
- \(b\ge3\): impossible.

For exactly \(3\)-deficient-perfect numbers of this form:
- \(b=1\): \(t\) has binary weight \(3\);
- \(b=2\): \(t=4\), equivalently \(p=2^{a+1}+3\);
- \(b=3\): \(t=2\), equivalently \(p=2^{a+1}+1\);
- \(b\ge4\): impossible.

Examples include
\[
50=2\cdot5^2\quad(k=2),\qquad
52=2^2\cdot13\quad(k=2),
\]
\[
232=2^3\cdot29\quad(k=3),\qquad
484=2^2\cdot11^2\quad(k=3).
\]

## Exact bounded verification

The standalone script `artifacts/verify.py` independently computes
\[
\Delta=2n-\sigma(n)
\]
and performs exact subset-sum dynamic programming over all proper divisors not exceeding \(\Delta\). It checks both the possible subset cardinalities and uniqueness of the representation.

For
\[
1\le a\le6,\qquad 1\le b\le4,\qquad p<200,\qquad 2^ap^b\le2{,}000{,}000,
\]
it tested 672 triples. Exactly 92 triples qualified, and every one had exactly one deficient-divisor representation with the cardinality predicted by the theorem. There were zero mismatches. The finite computation is supporting evidence; the theorem itself is proved above without a cutoff.

## Literature context and originality

Tang, Ren, and Li classified all deficient-perfect numbers with at most two distinct prime factors, i.e. the case \(k=1\). Their even two-prime family is recovered by the \(b=1,\ s_2(t)=1\) specialization above.

Chen introduced a systematic treatment of exactly \(k\)-deficient-perfect numbers and completely classified the **odd** exactly \(2\)-deficient-perfect numbers with two distinct prime divisors. Aursukaree and Pongsriiam subsequently proved that \(1521=3^2\cdot13^2\) is the only **odd** exactly \(3\)-deficient-perfect number with at most two distinct prime factors. OEIS A331627, A331628, and A331629 record the general, exactly-2, and exactly-3 sequences and point to these works.

Targeted searches for even exactly \(k\)-deficient-perfect numbers, the form \(2^a p^b\), two-prime-support classifications, and equivalent subset-sum/divisor formulations did not locate the theorem above, the base-\(p\)/binary uniqueness mechanism, or an arbitrary-\(k\) classification of this even two-prime slice. The current SCOPE archive was also checked for semantic overlap. Accordingly, originality is claimed only **to the best of our knowledge**. The main residual risk is poorly indexed divisor-partition literature or a later paper using different terminology.

## Limitations

The result classifies the even case with exactly two distinct prime factors. It does not classify odd exactly \(k\)-deficient-perfect numbers, integers with at least three distinct prime factors, or determine which fixed values of \(k\) occur infinitely often. The bounded computation is not used as a substitute for proof.

## References

1. M. Tang, X.-Z. Ren, M. Li, *On near-perfect and deficient-perfect numbers*, Colloquium Mathematicum 133 (2013), 221--226. DOI: 10.4064/cm133-2-8. https://doi.org/10.4064/cm133-2-8
2. F.-J. Chen, *On exactly k-deficient-perfect numbers*, Integers 19 (2019), Article A37. https://math.colgate.edu/~integers/t37/t37.pdf
3. S. Aursukaree, P. Pongsriiam, *On Exactly 3-Deficient-Perfect Numbers*, Fibonacci Quarterly 59 (2021), 33--46. https://doi.org/10.1080/00150517.2021.12427539
4. OEIS A331627, *Integers that are (exactly) k-deficient-perfect numbers*. https://oeis.org/A331627
5. OEIS A331628, *Integers that are exactly 2-deficient-perfect numbers*. https://oeis.org/A331628
6. OEIS A331629, *Integers that are exactly 3-deficient-perfect numbers*. https://oeis.org/A331629

## Reproducibility

Run
```text
python artifacts/verify.py
```
from the record directory. The expected deterministic output is stored in `artifacts/verification.txt`.
