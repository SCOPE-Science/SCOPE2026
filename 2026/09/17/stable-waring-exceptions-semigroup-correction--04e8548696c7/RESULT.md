# Stable Waring exceptions as numerical-semigroup gaps: correcting Theorem 10.7 and extending its modular obstruction

## Summary

Benfield and Lippard, *Integers that are not the sum of positive powers* (arXiv:2404.08193v2), define stable offset-exception sets \(\mathbf B^k\) for representations by exactly \(j\) positive \(k\)-th powers. Their Theorem 10.7 states that for every odd prime \(p\),
\[
|\mathbf B^{p-1}|\ge p^{p-1}\frac{p-1}{2}.
\]
As stated this is false at \(p=3\): the same paper's Table 2 gives \(|\mathbf B^2|=7\), whereas the theorem gives \(9\).

The stable-offset problem has a direct numerical-semigroup formulation. Let
\[
S_k=\langle a^k-1:a\ge2\rangle\subseteq\mathbb N_0.
\]
The permanent offset exceptions are exactly the positive gaps of \(S_k\). This reformulation exposes the off-by-one threshold in the modular count and gives a corrected explicit family of gaps. It also shows that the published lower bound remains valid for every odd prime \(p\ge5\), so Corollary 10.8 for \(p=11\) survives with a repaired proof. More generally, the same argument works modulo prime powers.

## Definitions and the semigroup translation

Fix \(k\ge2\). For \(j\ge1\), let
\[
E_{j,k}=\{c\in\mathbb N: j+c\text{ is not a sum of exactly }j\text{ positive }k\text{-th powers}\}.
\]
Padding a representation by \(1^k\) shows \(E_{j+1,k}\subseteq E_{j,k}\). Define the permanent offset-exception set
\[
P_k=\bigcap_{j\ge1}E_{j,k}.
\]
Whenever the offset sets stabilize, as in the definition of \(\mathbf B^k\) used by Benfield--Lippard, the stable value is precisely \(P_k\).

### Proposition 1

For every \(k\ge2\),
\[
P_k=\mathbb N\setminus S_k,
\qquad
S_k=\langle a^k-1:a\ge2\rangle.
\]
Moreover, \(S_k\) is a numerical semigroup.

### Proof

If
\[
j+c=x_1^k+\cdots+x_j^k,
\]
then
\[
c=\sum_{i=1}^j(x_i^k-1),
\]
so \(c\in S_k\); terms with \(x_i=1\) contribute zero. Conversely, if
\[
c=\sum_{i=1}^t(a_i^k-1),
\]
then for every \(j\ge t\),
\[
j+c=a_1^k+\cdots+a_t^k+(j-t)1^k,
\]
so \(c\notin P_k\). Hence \(P_k=\mathbb N\setminus S_k\).

To see that \(S_k\) is numerical, suppose a prime \(\ell\) divided every generator \(a^k-1\). Taking \(a=\ell\) would give \(\ell\mid \ell^k-1\), impossible because \(\ell^k-1\equiv-1\pmod\ell\). Thus the gcd of all generators is 1. A finite subset already has gcd 1, and the submonoid it generates is cofinite in \(\mathbb N_0\); therefore so is \(S_k\). \(\square\)

## A prime-power modular gap theorem

Let \(q=p^e\) be a prime power and let \(\lambda(q)\) be the Carmichael exponent of \((\mathbb Z/q\mathbb Z)^\times\).

### Theorem 2

Suppose
\[
e\le k,\qquad \lambda(q)\mid k.
\]
Put \(M=p^k/q\). Then the following explicit set consists entirely of permanent offset exceptions:
\[
\mathcal G_{k,q}
=
\bigcup_{r=1}^{q-1}
\{qt-r:1\le t\le rM-1\}
\subseteq P_k.
\]
Consequently,
\[
|P_k|\ge \frac{p^k(q-1)}2-(q-1).
\tag{1}
\]
If in addition
\[
q(q-1)<2^k-1,
\tag{2}
\]
then
\[
|P_k|\ge \frac{p^k(q-1)}2.
\tag{3}
\]

### Proof

For a generator \(a^k-1\) of \(S_k\):

- if \(p\nmid a\), then \(a^k\equiv1\pmod q\) because \(\lambda(q)\mid k\), so \(a^k-1\equiv0\pmod q\);
- if \(p\mid a\), then \(a^k\equiv0\pmod q\) because \(k\ge e\), so \(a^k-1\equiv-1\pmod q\).

The smallest generator of the second kind is \(p^k-1\). Suppose \(c\in S_k\) and \(c\equiv-r\pmod q\), where \(1\le r\le q-1\). In any expression of \(c\) as a sum of generators, let \(u\) be the number whose bases are divisible by \(p\). Then
\[
u\equiv r\pmod q,
\]
so \(u\ge r\), and therefore
\[
c\ge r(p^k-1).
\]
Thus every positive integer \(c\equiv-r\pmod q\) with \(c<r(p^k-1)\) is a gap.

Writing such an integer as \(c=qt-r\), the strict inequality becomes
\[
qt-r<r(p^k-1)
\iff
t<r\frac{p^k}{q}=rM.
\]
Hence exactly \(rM-1\) integers occur in residue class \(-r\). The classes are disjoint, so
\[
|\mathcal G_{k,q}|=
\sum_{r=1}^{q-1}(rM-1)
=
\frac{p^k(q-1)}2-(q-1),
\]
proving (1).

If (2) holds, then the additional \(q-1\) integers
\[
q,2q,\ldots,(q-1)q
\]
are all positive and smaller than \(2^k-1\), the smallest positive generator of \(S_k\). They are therefore gaps. They lie in residue class 0 modulo \(q\), while \(\mathcal G_{k,q}\) uses only nonzero residue classes, so the sets are disjoint. Adding them gives (3). \(\square\)

## Correction of Benfield--Lippard Theorem 10.7

The current arXiv v2 states on pp. 10--11:
\[
|\mathbf B^{p-1}|\ge p^{p-1}\frac{p-1}{2}
\quad\text{for every odd prime }p.
\]
But Table 2 on p. 10 records \(|\mathbf B^2|=7\). At \(p=3\), the theorem's right-hand side is \(9\), an immediate contradiction.

This can also be checked without trusting the table. For \(k=2\), the first two generators of \(S_2\) are 3 and 8. The semigroup \(\langle3,8\rangle\) has gaps
\[
\{1,2,4,5,7,10,13\}
\]
and contains every integer at least 14. Every further generator \(a^2-1\) is at least 15. Hence
\[
P_2=\{1,2,4,5,7,10,13\},
\qquad |P_2|=7.
\]
Therefore the quantifier "for any odd prime" in Theorem 10.7 cannot be correct.

### Corrected prime theorem

For every odd prime \(p\ge5\), the numerical lower bound asserted in Theorem 10.7 is nevertheless true:
\[
|P_{p-1}|\ge p^{p-1}\frac{p-1}{2}.
\tag{4}
\]

For \(p\ge7\), apply Theorem 2 with \(q=p\) and \(k=p-1\). Fermat gives \(\lambda(p)=p-1\mid k\). Also
\[
p(p-1)<2^{p-1}-1
\]
for \(p\ge7\): it holds at 7, and the inequality propagates by doubling the exponential side. Thus (3) gives (4).

For \(p=5\), Theorem 2 first gives
\[
|P_4|\ge 5^4\cdot2-4=1246.
\]
The four residue-zero integers
\[
5,10,20,25
\]
are also gaps of \(S_4\): the positive generators begin \(15,80,255,\ldots\), and 20 or 25 is neither below 15 nor a multiple of 15 before the next generator 80. These four gaps are disjoint from the modular family, giving
\[
|P_4|\ge1250=5^4\frac{4}{2}.
\]
This proves (4) for all odd primes \(p\ge5\).

### Corollary 10.8 remains valid

For \(p=11\), condition (2) holds because \(11\cdot10<2^{10}-1\). Hence the repaired argument gives
\[
|P_{10}|\ge 11^{10}\cdot5=129687123005.
\]
Thus the paper's Corollary 10.8 retains its stated numerical lower bound even though Theorem 10.7 is false as universally quantified.

## Extension beyond exponent \(p-1\)

Theorem 2 is not restricted to \(k=p-1\). For example, with \(k=8\), \(p=q=5\), one has \(4\mid8\) and \(20<2^8-1\), hence
\[
|P_8|\ge5^8\cdot2=781250.
\]
Benfield--Lippard Table 2 gives \(|\mathbf B^8|=945121\), consistent with this new general-purpose bound.

Prime-power moduli are also available: for example \(q=8\), \(k=4\) satisfies \(\lambda(8)=2\mid4\) and \(e=3\le4\), so (1) certifies 49 explicit gaps of \(P_4\). The prime-power statement can be combined over different moduli when their explicit gap families are tracked rather than merely their cardinalities.

## Why the original count loses the small case

The semigroup formulation shows the relevant threshold exactly. In residue class \(-r\pmod p\), the forced gaps satisfy
\[
c<r(p^k-1),
\]
not a non-strict block endpoint at a multiple of \(p^k\). For \(q=p\), this produces \(rp^{k-1}-1\), rather than \(rp^{k-1}\), gaps in the class. Summing the missing "\(-1\)" over the \(p-1\) nonzero residue classes is precisely the deficit \(p-1\) in (1). For \(p\ge7\), small residue-zero gaps restore that deficit; for \(p=5\), four explicit residue-zero gaps do so; for \(p=3\), they do not, and the theorem fails.

## Reproducibility

`artifacts/verify_waring_semigroup.py` uses only the Python standard library. It:

1. computes the numerical semigroup generated by \(a^k-1\) far enough to certify the conductor for \(k=2,4,6,8\), reproducing the Table 2 values \((|\mathbf B^k|,\max\mathbf B^k)\) for those exponents;
2. confirms the \(p=3\) contradiction \(9>7\);
3. generates the explicit modular gap families for several prime and prime-power cases and verifies they are subsets of the computed gap sets;
4. checks the repaired \(p=5,7,11\) numerical bounds and the \(k=8,p=5\) extension.
Run with:

```bash
python artifacts/verify_waring_semigroup.py
```

## Limitations

- The result corrects the domain and proof mechanism of Theorem 10.7; it does not claim exact values of \(|\mathbf B^k|\) for new large exponents.
- The prime-power theorem gives explicit lower bounds, not a characterization of all gaps.
- The identification with \(\mathbf B^k\) uses the stable-offset meaning of that notation; the permanent set \(P_k\) is defined independently and the semigroup theorem does not require an a priori stabilization theorem.
- Originality is reported only to the best of our knowledge; older generalized-Waring literature may contain equivalent formulations not surfaced by the searches documented in `REVIEW.md`.

## References

1. Brennan Benfield and Oliver Lippard, *Integers that are not the sum of positive powers*, arXiv:2404.08193v2 (31 March 2025), especially Table 2 and Theorem 10.7/Corollary 10.8. https://arxiv.org/abs/2404.08193
2. A. A. Zenkin, *The generalized Waring problem: A new property of positive integers*, Mathematical Notes 58 (1995), 933--937. DOI: 10.1007/BF02304770.
3. H. J. H. Tuenter, *The Frobenius problem, sums of powers of integers, and recurrences for the Bernoulli numbers*, Journal of Number Theory 117 (2006), 376--386. DOI: 10.1016/j.jnt.2005.06.015. (General Frobenius/numerical-semigroup context; its "sums of powers" concern power sums over Frobenius gaps, not this generator family.)
4. Z. Gu, *On the Numerical Semigroup Generated by {(2^k-m)2^{n+i}-1 | i in N}*, Journal of Mathematics (2022), Article 6590211. DOI: 10.1155/2022/6590211. (Nearby literature on structured numerical-semigroup generator families.)
