# Squarefree three-prime exactly \(3\)-deficient-perfect numbers

## Finding
Let \(p<q\) be odd primes and put
\[
n=2pq.
\]
Then \(n\) is exactly \(3\)-deficient-perfect if and only if
\[
n\in\{130,154,170,182,290,434\}.
\]
Equivalently, the complete list of prime pairs is
\[
(p,q)\in
\{(5,13),(7,11),(5,17),(7,13),(5,29),(7,31)\}.
\]

One may take the three deficient divisors as follows:
\[
\begin{array}{c|c}
n&\{d_1,d_2,d_3\}\\ \hline
130&\{1,2,5\}\\
154&\{2,7,11\}\\
170&\{1,5,10\}\\
182&\{1,13,14\}\\
290&\{1,10,29\}\\
434&\{7,31,62\}.
\end{array}
\]

## Assumptions and scope
An integer \(n\) is exactly \(3\)-deficient-perfect when there are three distinct proper divisors \(d_1,d_2,d_3\) such that
\[
\sigma(n)=2n-(d_1+d_2+d_3).
\]

The theorem classifies the natural squarefree even slice with exactly three prime factors, namely \(n=2pq\) with odd primes \(p<q\). It does not classify nonsquarefree three-prime-support integers, nor arbitrary exactly \(3\)-deficient-perfect numbers.

## Proof
For
\[
n=2pq
\]
one has
\[
\sigma(n)=3(p+1)(q+1),
\]
hence the deficiency is
\[
\Delta=2n-\sigma(n)=pq-3p-3q-3.
\]
If \(n\) is exactly \(3\)-deficient-perfect, then
\[
\Delta=d_1+d_2+d_3>0.
\]
In particular \(p\ne3\), so \(p\ge5\).

The proper divisors of \(n\) are
\[
1,\ 2,\ p,\ 2p,\ q,\ 2q,\ pq.
\]
Since
\[
\Delta<pq,
\]
no deficient-divisor triple can contain \(pq\). Thus the three divisors must be chosen from
\[
\{1,2,p,2p,q,2q\}.
\]

For any chosen triple, write its sum uniquely in the form
\[
c+ap+bq,
\]
where \(a,b,c\) are nonnegative integers determined by the selected divisors. Then
\[
pq-3p-3q-3=c+ap+bq,
\]
so
\[
\bigl(p-(b+3)\bigr)\bigl(q-(a+3)\bigr)
=(a+3)(b+3)+c+3.
\]
Because \(q\ge7\) and \(a\le3\), the second factor on the left is positive. The right side is positive, so the first factor is also positive. Therefore each of the twenty possible triples reduces to a positive divisor factorization of an integer between \(18\) and \(33\).

The complete finite reduction is:
\[
\begin{array}{c|c|c}
\text{selected divisors}&(a,b,c)&\text{prime solutions }(p,q)\\ \hline
\{1,2,p\}&(1,0,3)&(5,13)\\
\{1,2,2p\}&(2,0,3)&\varnothing\\
\{1,2,q\}&(0,1,3)&\varnothing\\
\{1,2,2q\}&(0,2,3)&\varnothing\\
\{1,p,2p\}&(3,0,1)&(5,17)\\
\{1,p,q\}&(1,1,1)&\varnothing\\
\{1,p,2q\}&(1,2,1)&\varnothing\\
\{1,2p,q\}&(2,1,1)&(5,29),(7,13)\\
\{1,2p,2q\}&(2,2,1)&\varnothing\\
\{1,q,2q\}&(0,3,1)&\varnothing\\
\{2,p,2p\}&(3,0,2)&\varnothing\\
\{2,p,q\}&(1,1,2)&(7,11)\\
\{2,p,2q\}&(1,2,2)&\varnothing\\
\{2,2p,q\}&(2,1,2)&\varnothing\\
\{2,2p,2q\}&(2,2,2)&\varnothing\\
\{2,q,2q\}&(0,3,2)&\varnothing\\
\{p,2p,q\}&(3,1,0)&\varnothing\\
\{p,2p,2q\}&(3,2,0)&\varnothing\\
\{p,q,2q\}&(1,3,0)&(7,31)\\
\{2p,q,2q\}&(2,3,0)&\varnothing.
\end{array}
\]

For completeness, if
\[
C=(a+3)(b+3)+c+3,
\]
then every solution in a row is obtained by choosing a positive divisor \(u\mid C\) and setting
\[
p=b+3+u,\qquad
q=a+3+\frac{C}{u},
\]
then retaining only odd primes with \(p<q\). Thus the table is exhaustive and contains no search bound.

Substituting the six surviving prime pairs gives exactly
\[
130,154,170,182,290,434,
\]
and the divisor triples listed in the finding satisfy
\[
d_1+d_2+d_3=2n-\sigma(n)
\]
in each case. This proves both necessity and sufficiency.

## Verification
The accompanying `verify.py` independently enumerates all twenty divisor triples, forms the factorization constant
\[
C=(a+3)(b+3)+c+3,
\]
enumerates every positive divisor of \(C\), and retains exactly the prime pairs satisfying the defining equation.

It also checks each of the six final integers directly from its prime factorization, recomputes \(\sigma(n)\), verifies that the displayed deficient divisors are distinct proper divisors, and verifies the exact deficient-perfect identity.

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Aursukaree and Pongsriiam introduced the exact \(3\)-deficient-perfect problem in this form and proved that the only odd example with at most two distinct prime factors is
\[
1521=3^2\cdot13^2.
\]
Their introduction explicitly describes the literature as largely focused on smaller prime support and states that their own paper treats the odd \(\omega(n)\le2\) case.

Chen's earlier work determines exactly \(2\)-deficient-perfect numbers with at most two distinct prime factors. That result concerns a different value of the deficient-divisor count and does not classify the three-prime squarefree slice here.

OEIS A331629 lists exactly \(3\)-deficient-perfect numbers computationally and contains all six values above among its initial terms, but it does not state that these are the complete squarefree numbers of the form \(2pq\).

A published published-finding corpus finding classifies ordinary deficient-perfect numbers of the form \(2^a pq\), where a single deficient divisor is allowed. Its statement does not cover sums of three distinct deficient divisors and therefore does not imply the classification proved here.

Exact searches for “\(2pq\) exactly \(3\)-deficient-perfect,” “squarefree exactly \(3\)-deficient-perfect,” the six-number list, and the prime-pair list did not locate a prior complete classification.

## Limitations
The theorem is restricted to squarefree numbers with prime support \(\{2,p,q\}\). It gives no classification for \(2^a p^b q^c\) once any exponent exceeds one.

Search non-detection is not a proof of novelty. An unindexed or unpublished treatment of this exact slice could exist.

## References
1. Saralee Aursukaree and Prapanpong Pongsriiam, “On Exactly \(3\)-Deficient-Perfect Numbers,” arXiv:2001.06953v1, first posted 20 January 2020; *The Fibonacci Quarterly* 59 (2021), no. 1, 33–46.
2. Feng-Juan Chen, “On exactly \(k\)-deficient-perfect numbers,” *Integers* 19 (2019), Article A37.
3. OEIS A331629, “Integers that are exactly \(3\)-deficient-perfect numbers.”
