# An effective criterion for Zumkeller numbers of the form \(2^a p q\)

## Statement

A positive integer is **Zumkeller** if its positive divisors can be partitioned into two sets having equal sum. Let
\[
n=2^a p q,\qquad a\ge 1,
\]
where \(p<q\) are distinct odd primes, and put
\[
M=2^{a+1}-1.
\]

The following gives an explicit criterion for this three-prime squarefree-odd-part family.

### Theorem

1. If \(p\le M\), then \(2^a p q\) is Zumkeller for every odd prime \(q>p\).

2. Suppose \(p>M\), and set
\[
u=p-M,\qquad v=q-M,
\]
and
\[
D=\frac{M(M+1)-uv}{2}.
\]
Then \(2^a p q\) is Zumkeller if and only if
\[
uv\le M(M+1)
\]
and there exist integers \(x,y,z\) with
\[
0\le x,y,z\le M,
\qquad
D=x+py+qz.
\]
Equivalently, it is enough to test
\[
0\le D-py-qz\le M
\]
for \(0\le y,z\le M\).

Consequently, for each fixed \(a\), all cases with \(p>M\) reduce to a finite computation. Indeed abundance forces
\[
1\le u<\sqrt{M(M+1)},
\qquad
q\le M+\left\lfloor\frac{M(M+1)}{u}\right\rfloor.
\]
Thus the infinite family is split into an automatic region \(p\le M\) and a rigorously bounded exceptional region.

### Complete low-exponent classifications

For \(1\le a\le 4\), a number \(2^a p q\) is Zumkeller exactly when it is abundant, except for the abundant non-Zumkeller pairs in the following table.

| \(a\) | \(M=2^{a+1}-1\) | abundant non-Zumkeller pairs \((p,q)\) |
|---:|---:|---|
| 1 | 3 | none |
| 2 | 7 | \((11,17)\) |
| 3 | 15 | \((19,67),(23,41)\) |
| 4 | 31 | \((37,173),(43,101),(43,107),(47,83),(47,89),(53,67),(53,73)\) |

In particular,
\[
2pq\text{ is Zumkeller}\iff p=3\text{ or }(p,q)=(5,7).
\]

## Proof

Bhaskara Rao and Peng proved the following facts for classical Zumkeller numbers:

- \(N\) is Zumkeller if and only if \((\sigma(N)-2N)/2\) is zero or is a sum of distinct proper divisors of \(N\);
- if \(N\) is Zumkeller and \(r\nmid N\) is prime, then \(Nr^\ell\) is Zumkeller for every \(\ell\ge1\);
- if \(r\le 2^{a+1}-1\), then \(2^a r\) is Zumkeller.

These are respectively Fact 3, Fact 6, and Fact 10 in their paper.

If \(p\le M\), Fact 10 gives that \(2^a p\) is Zumkeller, and Fact 6 then gives that \(2^a p q\) is Zumkeller. This proves part 1.

Now assume \(p>M\). Since
\[
\sigma(2^a)=M,
\]
we have
\[
\sigma(n)=M(p+1)(q+1),
\qquad
2n=(M+1)pq.
\]
Hence
\[
\frac{\sigma(n)-2n}{2}
=\frac{M(p+q+1)-pq}{2}.
\]
Writing \(p=M+u\) and \(q=M+v\) gives the exact cancellation
\[
M(p+q+1)-pq=M(M+1)-uv,
\]
so the excess in the Bhaskara Rao--Peng criterion is exactly
\[
D=\frac{M(M+1)-uv}{2}.
\]
Therefore abundance is equivalent to \(D\ge0\), or \(uv\le M(M+1)\).

Assume this abundance inequality. Since \(M\ge3\),
\[
0\le D\le \frac{M(M+1)}2<M^2<pq.
\]
Every divisor of \(n\) that contains both \(p\) and \(q\) is at least \(pq\), so none can occur in a sum equal to \(D\). The only usable divisors are therefore
\[
2^i,\qquad p2^i,\qquad q2^i,
\qquad 0\le i\le a.
\]
A subset of \(1,2,4,\ldots,2^a\) has every possible sum from \(0\) through
\[
1+2+\cdots+2^a=M
\]
exactly via binary expansion. Choices from the three divisor blocks are independent. Thus a sum of distinct usable divisors has the form
\[
x+py+qz,
\qquad 0\le x,y,z\le M,
\]
and every such triple is realized by distinct divisors. Fact 3 now gives precisely the stated equivalence.

Finally, if \(p>M\), then \(u,v\) are positive and \(u<v\). The abundance condition gives
\[
u^2<uv\le M(M+1),
\]
so \(u<\sqrt{M(M+1)}\), and for a fixed \(u\),
\[
v\le\left\lfloor\frac{M(M+1)}u\right\rfloor.
\]
This proves the finite reduction.

The low-exponent table is obtained by exhaustively enumerating exactly this finite abundance region, applying the coefficient criterion, and independently checking each candidate by an exact subset-sum calculation over all divisors. The accompanying verification artifact performs both calculations. There is no numerical cutoff in the \(p>M\) classification for \(a\le4\); the displayed bounds make each enumeration exhaustive.

## Context and relation to prior work

Bhaskara Rao and Peng developed the foundational divisor-partition criterion and general product criteria for Zumkeller numbers. Mahanta, Saikia, and Yaqubi later completely characterized the case with two distinct prime factors, in particular numbers \(2^\alpha p^\beta\), and studied bounds and layered-number questions when more distinct primes occur. Their Theorem 3.3 concerns \(k\)-layered numbers of the form \(2^\alpha p q\) for \(k\ge3\), rather than a classical Zumkeller classification for this family.

The theorem above specializes the divisor-partition problem to the next squarefree odd-support family and collapses it to a bounded three-coefficient equation, with a finite exceptional search for every fixed binary exponent. To the best of our knowledge, the explicit criterion, the fixed-\(a\) finite reduction, and the listed complete classifications for \(a\le4\) have not appeared previously.

## Verification

`artifacts/verify.py` uses exact integer arithmetic only. For \(a=1,2,3,4\), it:

1. derives the full finite set of \(p>M\) abundant candidates from the proved bounds;
2. applies the theorem's coefficient criterion;
3. independently applies exact subset-sum over the complete divisor set of \(2^a p q\);
4. asserts zero discrepancies and checks the displayed exception lists.

It also performs supplementary direct checks in the automatic region \(p\le M\) for primes \(q<500\). The general automatic-region theorem does not rely on this sample.

The deterministic output is recorded in `artifacts/verification.txt`.

## Limitations

The theorem treats the squarefree odd part \(pq\); it does not classify \(2^a p^b q^c\) when \(b>1\) or \(c>1\), nor families with four or more distinct prime factors. For general \(a\), the criterion is effective but is not replaced here by a closed-form list of all exceptional pairs. Originality is asserted only to the best of our knowledge; a residual risk is that an equivalent specialization of a more general divisor-partition criterion appears under different terminology or in literature not surfaced by the searches described in `REVIEW.md`.

## References

1. K. P. S. Bhaskara Rao and Yuejian Peng, *On Zumkeller Numbers*, Journal of Number Theory 133 (2013), 1135--1155. Preprint: https://arxiv.org/abs/0912.0052
2. Pankaj Jyoti Mahanta, Manjil P. Saikia, and Daniel Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory 217 (2020), 218--236. https://doi.org/10.1016/j.jnt.2020.05.003 ; preprint: https://arxiv.org/abs/2008.11096
3. Sai Teja Somu, Andrzej Kukla, and Duc Van Khanh Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149 (2023). https://arxiv.org/abs/2310.14149
4. OEIS A083207, *Zumkeller numbers*. https://oeis.org/A083207
