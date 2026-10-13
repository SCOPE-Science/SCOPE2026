# Exact classification of unitary half-Zumkeller numbers of the form \(4pq\)
## Finding
Let \(p<q\) be distinct odd primes. Then
\[
4pq\text{ is unitary half-Zumkeller}
\quad\Longleftrightarrow\quad
(p,q)\in\{(3,5),(3,7),(5,11),(7,13),(7,19)\}.
\]
Equivalently, the only unitary half-Zumkeller integers in this family are
\[
60,\ 84,\ 220,\ 364,\ 532.
\]

## Assumptions and scope
A divisor \(d\mid n\) is unitary when \(\gcd(d,n/d)=1\). A positive integer is unitary half-Zumkeller when its proper positive unitary divisors admit a partition into two nonempty subsets having equal sums. The theorem concerns exactly the family \(n=4pq\) with distinct odd primes \(p<q\). It does not classify higher powers of \(2\), repeated odd-prime factors, or arbitrary three-prime-support integers.

For \(n=4pq\), the proper positive unitary divisors are exactly
\[
1,\ 4,\ p,\ q,\ 4p,\ 4q,\ pq.
\]
This is the first dyadic three-prime-support layer in which the unitary divisor set differs from the ordinary divisor set: the squarefree layer \(2pq\) has every divisor unitary, whereas \(4pq\) does not.

## Proof
An equal-sum partition of the seven proper unitary divisors is equivalent to signs \(\varepsilon_d\in\{-1,1\}\) satisfying
\[
\varepsilon_1+4\varepsilon_4+p\varepsilon_p+q\varepsilon_q
 +4p\varepsilon_{4p}+4q\varepsilon_{4q}+pq\varepsilon_{pq}=0.
\]
Reversing all signs if necessary, assume \(\varepsilon_{pq}=1\). Put
\[
u=\varepsilon_q+4\varepsilon_{4q},\qquad
v=\varepsilon_p+4\varepsilon_{4p},\qquad
w=\varepsilon_1+4\varepsilon_4.
\]
Then \(u,v,w\in S:=\{-5,-3,3,5\}\), and the partition equation is
\[
q(p+u)=-(vp+w). \tag{1}
\]

Suppose first that \(p\ge11\). Since \(u\ge-5\), the factor \(p+u\) is positive. Equation (1) and \(|vp+w|\le5p+5\) give
\[
q\le \frac{5p+5}{p-5}.
\]
For \(p\ge11\),
\[
p^2-10p-5>0,
\]
so
\[
\frac{5p+5}{p-5}<p,
\]
contradicting \(q>p\). Hence \(p\in\{3,5,7\}\).

For each of these three values, equation (1) has only \(4^3=64\) sign triples \((u,v,w)\). Exhaustive exact evaluation gives the possible integers \(q>p\):

| \(p\) | possible \(q>p\) from (1) | prime possibilities |
| --- | --- | --- |
| \(3\) | \(5,6,7,9,10\) | \(5,7\) |
| \(5\) | \(6,9,10,11,14,15\) | \(11\) |
| \(7\) | \(8,9,10,12,13,15,16,19,20\) | \(13,19\) |

There is no identity lost through a zero denominator: when \(p=3\) and \(u=-3\), the equation \(3v+w=0\) has no solution in \(S^2\); when \(p=5\) and \(u=-5\), the equation \(5v+w=0\) has no solution in \(S^2\). Thus the only prime pairs allowed by (1) are
\[
(3,5),\ (3,7),\ (5,11),\ (7,13),\ (7,19).
\]

Each surviving pair has an explicit equal-sum partition of the proper unitary divisors:

| \((p,q)\) | one side | other side | common sum |
| --- | --- | --- | --- |
| \((3,5)\) | \(\{3,12,15\}\) | \(\{1,4,5,20\}\) | \(30\) |
| \((3,7)\) | \(\{1,4,12,21\}\) | \(\{3,7,28\}\) | \(38\) |
| \((5,11)\) | \(\{4,11,55\}\) | \(\{1,5,20,44\}\) | \(70\) |
| \((7,13)\) | \(\{7,91\}\) | \(\{1,4,13,28,52\}\) | \(98\) |
| \((7,19)\) | \(\{1,133\}\) | \(\{4,7,19,28,76\}\) | \(134\) |

This proves both directions.

## Verification
The supplied `verify.py` independently performs the complete \(64\)-triple evaluation for each of \(p=3,5,7\), checks that no zero-denominator identity occurs, checks the five explicit partitions, and performs a regression scan over all distinct odd-prime pairs with \(q\le1000\). Its supplied output is `VERIFY_OUTPUT.txt` and begins with `VERIFY_OK`.

The finite scan through \(q\le1000\) is not used to prove the infinite theorem. The unbounded part of the proof is the symbolic inequality excluding every prime \(p\ge11\); after that reduction, the \(64\)-triple evaluations are exhaustive finite proof steps.

## Relationship to prior work
Das defines unitary half-Zumkeller numbers, gives examples including \(60\) and \(84\), proves a necessary-and-sufficient subset-sum criterion, and proves that the only unitary half-Zumkeller integer with exactly two distinct prime factors is \(72\). The paper does not state a classification of the three-prime family \(4pq\). It also emphasizes that a unitary half-Zumkeller number need not be unitary Zumkeller, so a classification of unitary Zumkeller numbers does not settle the present family.

The published sequence OEIS A290467 lists unitary half-Zumkeller numbers and contains all five values above among its tabulated terms. Its displayed table and membership code provide finite data, not a proof excluding all other values of \(4pq\).

A published published-finding corpus record classifies even unitary Zumkeller numbers having exactly three distinct prime factors. That result is not implication-equivalent: unitary Zumkeller is a different property, and the present theorem classifies the larger unitary-half condition within the fixed family \(4pq\). ## Limitations
The classification is restricted to distinct odd primes \(p<q\) and dyadic exponent exactly two. It does not assert a classification for \(2^a pq\) with \(a\ne2\), for \(4p^bq^c\) with repeated odd-prime exponents, or for arbitrary unitary half-Zumkeller numbers. The literature comparison cannot exclude an obscure unindexed source, although the focal full text, the exact OEIS table, published result records, and targeted equivalent/broader searches were checked.

## References
1. B. Das, “On unitary Zumkeller numbers,” *Notes on Number Theory and Discrete Mathematics* 30(2) (2024), 436–442. DOI: https://doi.org/10.7546/nntdm.2024.30.2.436-442
2. OEIS A290467, “Unitary half-Zumkeller numbers.” https://oeis.org/A290467
3. “Three-prime-support classification of even unitary Zumkeller numbers,” published published-finding corpus record `2026/10/4/SCOPE-three-prime-support-classification-of-even-unitary-zumkeller-num--cd908a294237`.
