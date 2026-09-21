# Exact Zumkeller partition counts for the family \(2^a p\)

Let \(Z(n)\) denote the number of **unordered** partitions of the set of positive divisors of \(n\) into two disjoint subsets with equal sum. This is the counting function recorded as OEIS A083206. A positive integer is Zumkeller exactly when \(Z(n)>0\).

The existence problem for integers with two distinct prime factors is known: in particular, for an odd prime \(p\), \(2^a p\) is Zumkeller exactly when \(p\le 2^{a+1}-1\). The result below refines existence to an exact partition count and then describes its distribution as the prime parameter varies.

## Theorem 1: exact count and an explicit parameterization

Let \(a\ge 1\), let \(p\) be an odd prime, and put
\[
M=2^{a+1}-1.
\]
Then the unordered Zumkeller partitions of \(2^a p\) are in bijection with the positive odd integers \(r\) satisfying
\[
pr\le M.
\]
Consequently
\[
\boxed{
Z(2^a p)=\left\lfloor\frac{M+p}{2p}\right\rfloor.
}
\tag{1}
\]
In particular, \(Z(2^a p)>0\) if and only if \(p\le M\), recovering the known existence criterion in the exponent-one case.

More precisely, for every integer \(k\ge1\),
\[
\boxed{
Z(2^a p)=k
\iff
\frac{M}{2k+1}<p\le\frac{M}{2k-1}.
}
\tag{2}
\]
Thus every fiber of the partition-counting function on this two-prime family is an explicit prime interval.

The case \(k=1\) gives
\[
\frac{M}{3}<p\le M,
\]
which is equivalent, for odd primes, to the previously recorded OEIS A083209 observation that \(p2^a\) has a unique equal-sum divisor partition when \(2^{a+1}/3<p<2^{a+1}\). Formula (2) extends that observation simultaneously to every positive partition count. For example, the exactly-two case is
\[
\frac{M}{5}<p\le\frac{M}{3}.
\]

### Proof

The divisors of \(2^a p\) are
\[
1,2,\ldots,2^a,\qquad p,2p,\ldots,2^a p.
\]
Represent an ordered equal-sum bipartition by signs \(\varepsilon_i,\delta_i\in\{\pm1\}\), where the signs say on which side the divisors \(2^i\) and \(p2^i\) lie. Equality of the two subset sums is equivalent to
\[
A+pB=0,
\qquad
A=\sum_{i=0}^a\varepsilon_i2^i,
\qquad
B=\sum_{i=0}^a\delta_i2^i.
\tag{3}
\]

The signed binary sums have a simple exact description. If
\[
s=\sum_{i=0}^a\eta_i2^i,\qquad \eta_i\in\{\pm1\},
\]
and \(X\) is the set of indices with \(\eta_i=+1\), then
\[
s=2\sum_{i\in X}2^i-M.
\]
Because every integer from \(0\) through \(M\) has a unique binary expansion using \(1,2,\ldots,2^a\), the map from sign vectors to signed sums is a bijection onto the odd integers in \([-M,M]\). Hence every odd integer in this interval has exactly one signed-binary representation.

In (3), \(B\) is odd and therefore nonzero. Interchanging the two blocks of the divisor partition changes all signs simultaneously, so each unordered partition has a unique orientation with \(B>0\). Equation (3) then gives
\[
A=-pB.
\]
By the signed-binary bijection, this is possible exactly when \(B=r\) is a positive odd integer with \(pr\le M\); for every such \(r\), both \(B=r\) and \(A=-pr\) have unique sign vectors. This proves the claimed bijection.

The number of positive odd integers at most \(M/p\) is
\[
\left\lfloor\frac{M/p+1}{2}\right\rfloor
=
\left\lfloor\frac{M+p}{2p}\right\rfloor,
\]
which proves (1). Finally,
\[
\left\lfloor\frac{M+p}{2p}\right\rfloor=k
\]
is equivalent to
\[
2kp\le M+p<2(k+1)p,
\]
or
\[
(2k-1)p\le M<(2k+1)p,
\]
which is exactly (2). \(\square\)

## Theorem 2: a limiting law across the prime parameter

Let \(\pi_o(x)\) denote the number of odd primes at most \(x\). For fixed \(k\ge1\), define
\[
N_{a,k}=\#\{p\le M:\ p\text{ odd prime and }Z(2^a p)=k\}.
\]
Then (2) gives the exact identity
\[
\boxed{
N_{a,k}
=
\pi_o\!\left(\frac{M}{2k-1}\right)
-
\pi_o\!\left(\frac{M}{2k+1}\right).
}
\tag{4}
\]
Therefore, as \(a\to\infty\), the prime number theorem yields
\[
N_{a,k}
\sim
\frac{2M}{(4k^2-1)\log M},
\tag{5}
\]
and among the eligible odd primes \(p\le M\),
\[
\boxed{
\frac{N_{a,k}}{\pi_o(M)}
\longrightarrow
\frac{2}{4k^2-1}.
}
\tag{6}
\]
The limiting masses telescope:
\[
\sum_{k\ge1}\frac{2}{4k^2-1}
=
\sum_{k\ge1}\left(\frac1{2k-1}-\frac1{2k+1}\right)
=1.
\]
Thus the exact partition count has a universal limiting distribution when \(p\) is sampled from the admissible prime parameters.

## Theorem 3: aggregate count and the additive function \(\omega\)

Let \(\omega(m)\) be the number of distinct prime factors of \(m\), and define
\[
T_a=\sum_{\substack{3\le p\le M\\p\text{ prime}}}Z(2^a p).
\]
Then
\[
\boxed{
T_a
=
\sum_{\substack{1\le m\le M\\m\text{ odd}}}\omega(m).
}
\tag{7}
\]
Indeed, by Theorem 1, \(T_a\) counts pairs \((p,r)\) with \(p\) an odd prime, \(r\) a positive odd integer, and \(pr\le M\). Setting \(m=pr\), every odd \(m\le M\) contributes once for each distinct prime divisor of \(m\), which is precisely \(\omega(m)\).

Using the prime Mertens theorem,
\[
\sum_{p\le x}\frac1p=\log\log x+B_1+O\!\left(\frac1{\log x}\right),
\]
where \(B_1\) is the Meissel--Mertens constant for primes, (1) also gives
\[
\boxed{
T_a
=
\frac{M}{2}\left(\log\log M+B_1-\frac12\right)
+O\!\left(\frac{M}{\log M}\right).
}
\tag{8}
\]
In particular,
\[
T_a\sim\frac{M}{2}\log\log M.
\]
Since \(\pi_o(M)\sim M/\log M\), the mean number of Zumkeller partitions over admissible odd primes satisfies
\[
\frac{T_a}{\pi_o(M)}
\sim
\frac12\log M\,\log\log M.
\tag{9}
\]
The growing mean is compatible with the fixed-\(k\) limiting law because the latter has a non-uniformly integrable tail.

## Computational verification

The standalone script `artifacts/verify.py` directly enumerates equal-sum divisor subsets, independently of formula (1), for all
\[
1\le a\le7,
\qquad
3\le p\le199,
\quad p\text{ prime}.
\]
It checks 315 parameter pairs and reports zero mismatches. It also checks identity (7) for \(1\le a\le17\), again with zero mismatches. Representative exact counts include
\[
Z(6)=1,
\quad Z(20)=1,
\quad Z(24)=3,
\quad Z(40)=2,
\quad Z(48)=5.
\]
The proof does not depend on these finite checks.

## Relation to prior work

- Bhaskara Rao and Peng, *On Zumkeller Numbers* (arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135--1155), define Zumkeller partitions and record the classical sufficient condition that \(2^a p\) is Zumkeller for odd prime \(p\le2^{a+1}-1\). Their full arXiv text also develops general structural criteria for \(np\).
- Mahanta, Saikia and Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory 217 (2020), 218--236, Theorem 2.6, completely characterizes the existence of two-prime-support Zumkeller numbers: \(2^a p^b\) is Zumkeller exactly when \(p\le2^{a+1}-1\) and \(b\) is odd.
- OEIS A083206 is the partition-counting function \(Z(n)\) and currently gives generic subset-sum/coefficient formulas. OEIS A083209 records the previously known \(k=1\) interval for \(p2^a\), due to T. D. Noe (2010). OEIS A378652 records the integers with exactly two such partitions.

The contribution here is therefore not the existence criterion and not the already known unique-partition slice. It is the exact all-\(k\) count (1), the bijective parameterization, the complete fiber intervals (2), and the prime-parameter and aggregate distribution laws (4)--(9).

## Originality and limitations

To the best of our knowledge, the exact all-\(k\) formula and its distribution consequences have not previously been stated. Searches were made using the counting-sequence identifier A083206 and synonymous phrases such as “number of Zumkeller partitions”, “equal-sum divisor partitions”, and the family \(2^a p\), with checks against the sources above and current OEIS entries. The known \(k=1\) observation was explicitly excluded from the originality claim.

A residual literature risk remains in older informal or sequence-oriented material. In particular, Reinhard Zumkeller/Peter Luschny web material tabulates Zumkeller partitions for small integers, but the relevant page could not be inspected in full during this check; an unpublished equivalent formula could conceivably have appeared there or in early notes surrounding the sequence. The 2008 Clark et al. announcement cited by later papers was also not inspected in full. No located source stated the arbitrary-\(k\) formula, the limiting law, or identity (7).

## References

1. K. P. S. Bhaskara Rao and Y. Peng, *On Zumkeller Numbers*, arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135--1155. https://arxiv.org/abs/0912.0052
2. P. J. Mahanta, M. P. Saikia and D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory 217 (2020), 218--236. https://doi.org/10.1016/j.jnt.2020.05.003
3. OEIS A083206, number of equal-sum bipartitions of the divisor set. https://oeis.org/A083206
4. OEIS A083209, integers having exactly one such partition. https://oeis.org/A083209
5. OEIS A378652, integers having exactly two such partitions. https://oeis.org/A378652
