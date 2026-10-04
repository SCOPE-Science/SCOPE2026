# The first 49 exponent layers of the unitary–exponential divisor-sum equality

## Finding
Let \(\sigma^*(n)\) be the sum of the unitary divisors of \(n\), and let \(\sigma^{(e)}(n)\) be the sum of the exponential divisors. If \(p,q\) are distinct primes and \(2\le a\le49\), then
\[
\sigma^*(p^a q)=\sigma^{(e)}(p^a q)
\]
holds exactly for
\[
(a,p,q)\in\{(2,2,5),(2,3,5),(6,2,5),(49,2,4363953127297)\}.
\]
Thus the corresponding integers are \(20,45,320\), and
\[
2456687209744634987008753664=2^{49}\cdot4363953127297.
\]
In particular, the exponent-\(49\) example recorded in the motivating literature is the first new singleton-cofactor exponent layer after \(a=6\).

## Assumptions and scope
An exponential divisor of \(p^a\) has exponent \(d\) with \(d\mid a\), so \(\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\). A unitary divisor of a prime power is either \(1\) or the whole prime power, so \(\sigma^*(p^a)=1+p^a\). The theorem concerns only numbers \(p^a q\) with one exponent equal to \(1\), where \(2\le a\le49\).

## Proof
By multiplicativity,
\[
\sigma^*(p^a q)=(p^a+1)(q+1),\qquad
\sigma^{(e)}(p^a q)=q\sum_{d\mid a}p^d.
\]
Therefore equality is equivalent to
\[
p^a+1=qR_a(p),\qquad
R_a(X)=\sum_{d\mid a,\ d<a}X^d-1. \tag{1}
\]
For each fixed \(a\), the polynomial \(R_a\) is monic. Let \(B_a(X)\) be the Euclidean remainder of \(X^a+1\) on division by \(R_a(X)\), and put
\[
C_a=\sum_j\left|[X^j]B_a\right|.
\]
If (1) holds, then \(R_a(p)\mid B_a(p)\).

For every \(2\le a\le49\), exact integer polynomial division gives \(B_a(p)\ne0\) for every integer \(p\ge2\). The packaged verifier checks this with the rational-root theorem: any integer root must divide the nonzero constant term of \(B_a\), and every positive divisor at least \(2\) is tested exactly. Writing \(m=\deg R_a\),
\[
R_a(p)\ge p^m-1,\qquad |B_a(p)|\le C_a p^{m-1}.
\]
If \(p\ge C_a+2\), then \(R_a(p)>|B_a(p)|>0\), contradicting \(R_a(p)\mid B_a(p)\). Hence
\[
p\le C_a+1.
\]
Across \(2\le a\le49\), the exact maximum is \(\max C_a=1082\), attained at \(a=35\). It is therefore enough to test primes \(p\le1083\), using the sharper bound \(p\le C_a+1\) in each layer.

Exact enumeration produces 34 pairs \((a,p)\) for which \(R_a(p)\mid p^a+1\). For each pair set \(q=(p^a+1)/R_a(p)\). Thirty quotients have an explicit proper factor in `candidates.tsv`; the other four are prime and are exactly the four triples displayed above. Direct substitution verifies the divisor-sum equality in all four cases.

## Verification
Run `python verify.py`. The script uses only the Python standard library. It rebuilds every \(R_a\) and \(B_a\), verifies the rational-root exclusions and prime bounds, enumerates every admissible prime, checks all 34 divisibility pairs, proves primality of the four surviving quotients by direct trial division, and recomputes both divisor sums.

Expected final line:

`VERIFY_OK exponents=2..49 max_C=1082 divisibility_pairs=34 solutions=[(2, 2, 5), (2, 3, 5), (6, 2, 5), (49, 2, 4363953127297)]`

## Relationship to prior work
Trudgian's paper compares \(\sigma^*\) and \(\sigma^{(e)}\), asks whether equality occurs infinitely often, reports five equality values up to \(10^9\), and records the much larger example \(2^{49}\cdot4363953127297\). It does not state an exhaustive theorem by exponent layer for the two-prime singleton-cofactor family. OEIS A236474 collects known equality values and the same large example, but likewise does not state that the four triples above exhaust all \(p^a q\) solutions through \(a=49\).

## Limitations
The cutoff \(49\) is tied to the first remote two-prime example explicitly highlighted in the motivating literature. The theorem is exhaustive only for \(2\le a\le49\) and singleton cofactor exponent \(1\). It makes no claim for \(a\ge50\) or for numbers \(p^a q^b\) with \(b>1\), and it does not resolve the global infinitude question.

## References
Tim Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first submitted 2013-12-17; *Publications de l'Institut Mathématique* 97(111) (2015), 175–180, DOI 10.2298/PIM140617001T.

OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*.
