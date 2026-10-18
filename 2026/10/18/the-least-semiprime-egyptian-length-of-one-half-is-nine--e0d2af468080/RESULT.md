# The least semiprime Egyptian length of one half is nine

## Finding

Let \(\mathcal S=\{pq: p<q\text{ are distinct primes}\}\). The minimum cardinality of a finite set \(D\subset\mathcal S\) for which
\[
\sum_{d\in D}\frac1d=\frac12
\]
is exactly \(9\). An explicit, strictly increasing nine-term representation is
\[
\frac12=\frac16+\frac1{10}+\frac1{15}+\frac1{21}+\frac1{26}
+\frac1{35}+\frac1{39}+\frac1{65}+\frac1{91}.
\]

## Assumptions and scope

Every denominator must be the product of **two distinct primes**; repeated denominators are forbidden. No restriction is placed on the size of a denominator, on the primes used, or on sharing a prime between denominators. The length means the number of denominators in a representation, not the largest denominator. All fractions are exact rational numbers.

## Proof

Write \(6=s_1<s_2<\cdots\) for all squarefree semiprimes in increasing order. The first six are \(6,10,14,15,21,22\), with
\[
\sum_{i=1}^{6}\frac1{s_i}=\frac{115}{231}<\frac12,
\quad
\sum_{i=1}^{4}\frac1{s_i}=\frac{17}{42},
\quad
\sum_{i=1}^{5}\frac1{s_i}=\frac{19}{42}.
\]
Thus no representation can have at most six summands.

If a seven-term representation exists, write its denominators \(n_1<\cdots<n_7\). The residual after the first four satisfies
\[
\sum_{i=5}^{7}\frac1{n_i}\ge\frac12-\frac{17}{42}=\frac2{21}.
\]
Since each of these three summands is at most \(1/n_5\), necessarily \(n_5\le31\). Accordingly the first five denominators must be chosen from the **complete** list
\[
\mathcal S\cap[6,31]=\{6,10,14,15,21,22,26\}.
\]
There are only \(\binom75=21\) candidate increasing prefixes. If an eight-term representation exists, the same argument applied after five denominators gives
\[
\sum_{i=6}^{8}\frac1{n_i}\ge\frac12-\frac{19}{42}=\frac1{21},
\qquad n_6\le63.
\]
The first six are among the \(18\) elements of
\[
\mathcal S\cap[6,63]=\{6,10,14,15,21,22,26,33,34,35,38,39,46,51,55,57,58,62\},
\]
which has \(\binom{18}{6}=18564\) candidate increasing six-term prefixes.

For either length, subtract the prefix to obtain a reduced positive rational residual \(r=a/b\). The last two denominators \(x<y\) must exceed the last denominator \(t_0\) of the prefix, so \(0<r<2/t_0\). There is an *exact finite parametrization* of all integer solutions of the remaining equation:
\[
\frac1x+\frac1y=\frac ab
\quad\Longleftrightarrow\quad
(ax-b)(ay-b)=b^2.
\]
Consequently \(t=ax-b\) is a positive divisor of \(b^2\), and
\[
 x=\frac{b+t}{a},\qquad
 y=\frac{b+b^2/t}{a}.
\]
Conversely every positive divisor \(t\mid b^2\) for which the two displayed expressions are integers with \(t_0<x<y\) yields an integer pair solving the residual equation. Testing whether both are products of distinct primes completes the check; **no bound on** \(x\) **or** \(y\) **is imposed**.

The accompanying exact-arithmetic certificate enumerates all \(21\) seven-term prefixes and all \(18564\) eight-term prefixes. Respectively \(6\) and \(74\) prefixes pass \(0<r<2/t_0\). Exhaustive enumeration of the divisors of each reduced \(b^2\) yields **zero** admissible last pairs in both cases. Thus no seven- or eight-term representation exists. Finally, the displayed nine-term identity sums to \(1/2\) exactly and all its denominators belong to \(\mathcal S\), proving the theorem.

## Verification

Run `python3 certificate.py` with Python 3.9 or later; only the standard library is used. The program exactly evaluates the witness and initial reciprocal sums, generates every admissible bounded prefix, factors the residual denominator by trial division, generates **all** divisors of its square, and checks integer/order/prime-factor conditions for the last two denominators. Expected output: \(21\) prefixes and \(6\) live residuals for seven terms, \(18564\) prefixes and \(74\) live residuals for eight terms, with zero completions in each case. Run `python3 independent_check.py` for a second depth-first recursion using denominator bounds at every stage; its terminal state counts are \(6\) and \(74\), and both searches return no solution.

## Relationship to prior work

Li's 2026 theorem on semiprime unit fractions (arXiv:2609.32140v1, Theorem 1.1) establishes existence for all positive rationals with squarefree reduced denominator; its proof is a large-prime construction and contains no sharp minimal-term statement for the target \(1/2\). Li's earlier arXiv:2606.15159v2 proves the integer case and a rational range beginning below \(1/5\), again without classifying the least length at \(1/2\). Martin and Shi (arXiv:2107.05076, Theorem 3.2) give a general algorithm that finds all representations **within a prescribed finite multiset** of permitted denominators. The present proof adds a global lower bound on length by reducing the unrestricted final pair to a divisor equation; merely running that finite-input algorithm does not imply the global bound. The prime-support-restricted Egyptian fraction rank bound and the three-term prime-reciprocal classification in the published related-record search address different target/restriction combinations.

## Limitations

The result concerns exactly the target \(1/2\) and denominators that are products of distinct primes. It gives neither a uniform minimal length for other rational targets nor a classification of all nine-term representations. The exhaustive portion depends on reproducibility of the included finite arithmetic certificate, not on an independent audit. A search of available records cannot rule out a previously unindexed computation of the same sharp value.

## References

- S. Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306*, arXiv:2609.32140v1, September 26, 2026, https://arxiv.org/html/2609.32140v1.
- S. Li, *Every natural number is a sum of distinct semiprime unit fractions*, arXiv:2606.15159v2, June 17, 2026, https://arxiv.org/html/2606.15159v2.
- G. Martin and Y. Shi, *An algorithm for Egyptian fraction representations with restricted denominators*, *Involve* 18 (2025), 1–23, DOI:10.2140/involve.2025.18.1; https://personal.math.ubc.ca/~gerg/papers/downloads/AEFRRD.pdf.
- OEIS A006881, integers with exactly two distinct prime factors, https://oeis.org/A006881.
