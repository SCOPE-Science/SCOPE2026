# Sharp dyadic floors and the complete sub-five spectrum of the two-block odd partition function

## Finding

Let \(a(n)\) denote the signed two-block odd partition coefficient
\[
\sum_{n\ge1} a(n)q^n
=
\sum_{1\le x<y}
\frac{q^{x+y}}{(1+q^{2x})(1+q^{2y})}.
\]
Write \(n=2^k m\) with \(m\) odd. For every \(k\ge2\),
\[
a(2^k m)\ge 2^{k-1}-1,
\]
with equality exactly for \(m=1\). If \(m>1\), then the stronger sharp bound
\[
a(2^k m)\ge 2^{k+1}-3
\]
holds, with equality exactly for \(m=3\).

As a consequence, the entire coefficient spectrum below \(5\) is
\[
\begin{aligned}
a(n)=0&\iff n\in\{1,2\},\\
a(n)=1&\iff n\in\{3,4,5,6,10\},\\
a(n)=2&\iff n\in\{7,14\},\\
a(n)=3&\iff n\in\{8,9,11,13,18,22,26\},\\
a(n)=4&\iff n\in\{17,34\}.
\end{aligned}
\]
The first line is the known zero-set theorem of Merca; the layer minima and the fibers \(1\) through \(4\) are the additional conclusions proved here.

## Assumptions and scope

For positive integers \(r\), let
\[
\sigma(r)=\sum_{d\mid r}d,
\qquad
\lambda(r)=\sum_{d\mid r}\chi_4(d),
\]
where \(\chi_4\) is the nonprincipal character modulo \(4\). Let \(\tau(r)\) be the number of positive divisors of \(r\).

The proof uses two published identities. The first is
\[
a(n)=\frac{\sigma(n)-\lambda(n)}4
-\frac{\sigma(n/2)}2
+\sigma(n/4),
\]
with the usual convention that \(\sigma(x)=0\) when \(x\) is not a positive integer. The second, for odd \(m\) and \(k\ge1\), is
\[
a(2^k m)
=
\frac{(2^{k+1}-3)\sigma(m)-\lambda(m)}4.
\]

The result concerns exact lower envelopes on fixed dyadic layers and the exact fibers with coefficient less than \(5\). It makes no assertion about a complete classification of larger coefficient values.

## Proof

For an odd prime power \(p^\alpha\), multiplicativity of \(\lambda\) gives
\[
\lambda(p^\alpha)=
\begin{cases}
\alpha+1,&p\equiv1\pmod4,\\
1,&p\equiv3\pmod4\text{ and }\alpha\text{ is even},\\
0,&p\equiv3\pmod4\text{ and }\alpha\text{ is odd}.
\end{cases}
\]
Hence, for every odd \(m\),
\[
0\le \lambda(m)\le \tau(m).
\]

Fix \(k\ge2\) and put \(C_k=2^{k+1}-3\). If \(m=1\), then
\[
a(2^k)=\frac{C_k-1}4=2^{k-1}-1.
\]
If \(m=3\), then \(\sigma(3)=4\) and \(\lambda(3)=0\), so
\[
a(3\cdot2^k)=C_k.
\]
Now suppose that \(m>3\) is odd. Since
\[
\sigma(m)-\tau(m)=\sum_{d\mid m}(d-1)\ge m-1\ge4,
\]
we have \(\lambda(m)\le\sigma(m)-4\). Therefore
\[
\begin{aligned}
4a(2^k m)
&=C_k\sigma(m)-\lambda(m)\\
&\ge C_k\sigma(m)-(\sigma(m)-4)\\
&=4C_k+(C_k-1)(\sigma(m)-4)
>4C_k.
\end{aligned}
\]
This proves both sharp dyadic bounds and their equality cases.

It remains to determine the values below \(5\). For odd \(m\), define
\[
\Delta(m)=\sigma(m)-\lambda(m)=4a(m).
\]
If \(m=p\) is an odd prime, then
\[
\Delta(p)=
\begin{cases}
p-1,&p\equiv1\pmod4,\\
p+1,&p\equiv3\pmod4.
\end{cases}
\]
Thus the prime arguments with \(\Delta(p)\le16\) are
\[
p=3,5,7,11,13,17,
\]
with respective values
\[
\Delta(p)=4,4,8,12,12,16.
\]

Suppose next that \(m=p^\alpha\) with \(\alpha\ge2\). If \(p\equiv1\pmod4\), then \(p\ge5\) and
\[
\Delta(p^\alpha)
=
1+p+\cdots+p^\alpha-(\alpha+1)
\ge31-3=28.
\]
If \(p\equiv3\pmod4\) and \(\alpha\) is even, then
\[
\Delta(p^\alpha)=\sigma(p^\alpha)-1\ge13-1=12,
\]
with equality exactly at \(p^\alpha=9\). If \(p\equiv3\pmod4\) and \(\alpha\ge3\) is odd, then
\[
\Delta(p^\alpha)=\sigma(p^\alpha)\ge40.
\]
Finally, if \(m\) has at least two distinct odd prime divisors \(p<q\), then \(p\ge3\), \(q\ge5\), and the divisors \(p,q,pq\) alone give
\[
\Delta(m)
\ge \sigma(m)-\tau(m)
=
\sum_{d\mid m}(d-1)
\ge (p-1)+(q-1)+(pq-1)
\ge20.
\]
Therefore the odd arguments with \(a(m)\le4\) are exactly
\[
\begin{array}{c|ccccc}
a(m)&0&1&2&3&4\\ \hline
m&1&3,5&7&9,11,13&17.
\end{array}
\]

For \(k=1\), the published dyadic identity gives \(a(2m)=a(m)\). For \(k\ge2\), the sharp layer bounds show that the only additional arguments with value below \(5\) are \(4\), where \(a(4)=1\), and \(8\), where \(a(8)=3\). Combining these cases yields the five stated fibers.

## Verification

The proof is symbolic and covers every positive integer. The included script `artifacts/verify.py` is only a corroborating normalization check. It compares the divisor-sum formula against the defining signed enumeration through \(n=120\), verifies the five fibers through \(n=20000\), and stress-tests the dyadic bounds for \(2\le k\le12\) and odd \(m<1000\). No finite computation is used to infer an infinite statement.

## Relationship to prior work

Merca's first paper introduces \(a(n)\), proves the divisor-sum formula, proves \(a(n)\ge0\), and proves that equality occurs exactly at \(n=1,2\). The later dyadic paper proves
\[
a(2^k m)=a(m)+(2^{k-1}-1)\sigma(m)
\]
and the equivalent divisor-sum expression for odd \(m\). The inspected sources use these identities for positivity, signed representation structure, and congruences; they do not state the sharp minimum on each dyadic layer, the sharp minimum after removing the pure power of two, or the complete fibers \(a(n)=1,2,3,4\).

The threshold \(5\) is structural rather than an arbitrary finite cutoff: on the first nontrivial dyadic layer \(k=2\), every odd part \(m>1\) already satisfies \(a(4m)\ge5\). Thus the theorem classifies the full spectrum strictly below the first non-power value on that layer.

## Limitations

The theorem does not classify all fibers \(a(n)=r\) for \(r\ge5\), nor does it provide asymptotic information about the distribution of the coefficients. The originality check is limited by ordinary literature-indexing coverage for a function introduced only recently; the two directly relevant primary full texts were inspected in full or in their relevant complete sections.

## References

1. M. Merca, *The two-block odd partition function*, arXiv:2609.33770v1, first posted 27 September 2026; *The Ramanujan Journal* 71 (2026), article 23, DOI 10.1007/s11139-026-01426-1.
2. M. Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for \(\operatorname{pod}(n)\)*, arXiv:2610.05020v1, first posted 4 October 2026.
