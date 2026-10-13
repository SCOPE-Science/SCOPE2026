# A sharp dyadic threshold for two-layered numbers \(2^a p^2\)

## Finding
Let \(a\ge 1\) be an integer and let \(p\) be an odd prime. Then
\[
2^a p^2\text{ is two-layered}\quad\Longleftrightarrow\quad p<2^a.
\]

Here “two-layered” means that the positive divisors other than \(1\) can be partitioned into two disjoint sets having equal sum. Thus the first possible two-prime-support stratum allowed by the even-exponent condition on odd prime factors has a complete, sharp threshold: the odd prime must lie below the dyadic factor.

## Assumptions and scope
Write \(h=2^a\) and \(n=hp^2\). The result is only about the exponent pattern \((a,2)\) on support \(\{2,p\}\); it does not classify two-layered integers with larger odd-prime exponents or with more prime supports.

Behzadipour's criterion says that \(n\) is two-layered exactly when
\[
T(n)=\frac{\sigma(n)-1}{2}-n
\]
is a sum of distinct proper positive divisors of \(n\), excluding \(1\). For \(n=hp^2\),
\[
T(n)=p\left(h-\frac{p+1}{2}\right)+(h-1).
\]

## Proof
Assume first that \(p<h\). Define
\[
A=h-\frac{p-1}{2},\qquad B=h-1-p.
\]
Then \(0<A<h\), while \(B\) is even and \(0\le B<h\). A direct calculation gives
\[
T(n)=pA+B.
\]
Every integer in \([0,h-1]\) has a binary expansion using the powers
\[
1,2,\ldots,\frac h2.
\]
Use the binary digits of \(A\) to express \(pA\) as a sum of distinct divisors \(p2^i\), and use the binary digits of the even integer \(B\) to express \(B\) as a sum of distinct divisors \(2^i\) with \(i\ge1\). These two divisor families are disjoint; all of their members are proper divisors of \(hp^2\), and none equals \(1\). Hence \(T(n)\) has the required representation, so \(n\) is two-layered.

Conversely, suppose \(p>h\). Since \(p\) is odd and \(h\) is a power of two, equality cannot occur. If \(p\ge2h+1\), then
\[
T(n)=\frac{p(2h-1-p)}2+h-1<0,
\]
so Behzadipour's criterion is impossible.

It remains to consider
\[
h<p\le2h-1.
\]
Put
\[
A_0=h-\frac{p+1}{2},
\]
so that
\[
T(n)=pA_0+h-1.
\]
Here \(T(n)<p^2\). Therefore no divisor divisible by \(p^2\) can occur in a representation of \(T(n)\). Any such representation would consequently have the form
\[
T(n)=pC+D,
\]
where \(C\) is a subset sum of \(1,2,\ldots,h\) through powers of two, and \(D\) is a subset sum of
\[
2,4,\ldots,h.
\]
In particular, \(D\) is even and
\[
0\le D\le2h-2.
\]
Reducing modulo \(p\) gives
\[
D\equiv h-1\pmod p.
\]
Because \(p>h\), the interval \([0,2h-2]\) contains at most the two integers congruent to \(h-1\) modulo \(p\): namely \(h-1\) and possibly \(h-1+p\). The first is odd, so it cannot equal \(D\); the second is larger than \(2h-2\). This contradiction rules out the remaining range. Therefore \(p<h\) is necessary.

## Verification
The accompanying `verify.py` independently applies the exact subset-sum criterion to every odd prime \(p\le300\) and every \(1\le a\le9\). It constructs the proper divisors of \(2^a p^2\), performs an exact bitset subset-sum test at the target \(T(n)\), and checks agreement with the condition \(p<2^a\).

The replay covers \(549\) parameter pairs and reports no discrepancy. This finite computation is a regression test only; the proof above is unbounded in both \(a\) and \(p\).

## Relationship to prior work
Behzadipour introduced two-layered numbers and proved three facts directly relevant here: every odd-prime exponent in a two-layered number is even; \(36,72,144,200\) are examples; and Theorem 1.5 gives the exact subset-sum criterion used above. The paper also gives closure constructions that manufacture new two-layered numbers from known ones. These results do not state or imply a closed-form classification of the entire family \(2^a p^2\): applying Theorem 1.5 to this family still leaves an infinite subset-sum problem, resolved here by the binary construction and the modular obstruction.

OEIS A322657 tabulates two-layered numbers. Its early terms are consistent with the threshold: for example \(36,72,144,200,392,400,784,1936,2704\) all arise from primes below the relevant power of two. The entry gives a membership algorithm and table, not an infinite parameter classification of \(2^a p^2\).

Targeted semantic searches for the exact family, prime-square support, the dyadic threshold, and equivalent formulations found no result covering the theorem. The closest returned results concern different notions on two-prime support, such as practical, strong Achilles, Egyptian-fraction, or Tian-type conditions, and do not imply two-layeredness.

## Limitations
The theorem is confined to the minimal odd-prime exponent \(2\). It makes no claim about \(2^a p^{2b}\) for \(b>1\), where the extra \(p\)-power divisor layers change the subset-sum geometry.

The originality search cannot exclude unindexed notes or unpublished observations. The main residual risk is that the sharp threshold may have been noticed informally from OEIS A322657 without appearing in the inspected literature.

## References
1. Hussein Behzadipour, “Two-layered numbers,” arXiv:1812.07233, first submitted 18 December 2018.
2. OEIS Foundation Inc., OEIS A322657, “Integers whose set of divisors, excluding 1, can be partitioned into two nonempty subsets having equal sum.”
