# Exact prime-power factorization of the binomial progression gcd

## Finding

For every integer \(k\ge2\), define \(n=k+1\) and
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
For every prime \(p\mid n\), let \(p^a\parallel n\), \(b=n/p^a\), and \(t=\lfloor\log_p b\rfloor\). Then
\[
\boxed{\nu_p(D(k))=\max\{0,a-t\}},
\]
and \(\nu_p(D(k))=0\) when \(p\nmid n\). In particular,
\[
\boxed{D(k)=\prod_{p^a\parallel k+1}
 p^{\max\{0,a-\lfloor\log_p((k+1)/p^a)\rfloor\}}}.
\]
If \(a>t\), a specific factor of the defining gcd realizes the minimum valuation: take \(q=p\) for \(b=1\) and
\[
q=1+p^a(b-p^t)
\]
for \(b>1\). The latter witness satisfies \(2\le q\le k+1\).

## Assumptions and scope

The gcd is over the full finite progression of upper binomial indices in Guo–Qiu–Cao–Feng–Gao, with the lower index fixed and \(k\ge2\). All binomial coefficients and the gcd are positive integers. Valuations are normalized by \(\nu_p(p)=1\). The integer \(t\) is characterized without approximation by \(p^t\le b<p^{t+1}\). The displayed formula is exact for every permitted \(k\), not just for prime powers or a bounded computational range.

## Proof

**Only primes dividing \(k+1\) can occur, with bounded exponents.** Set \(F(x)=\binom{xk}{k}\), a polynomial of degree \(k\) with \(F(0)=0\) and \(F(1)=1\). Interpolation at the consecutive integers \(1,2,\ldots,k+1\) gives
\[
0=F(0)=\sum_{q=1}^{k+1}(-1)^{q-1}\binom{k+1}{q}F(q).
\]
Modulo \(D(k)\), all terms with \(q\ge2\) vanish. Therefore \(D(k)\mid k+1\). This shows that no other prime occurs and that \(\nu_p(D(k))\le a\).

Fix a prime-power component \(p^a\parallel n\), with \(b=n/p^a\) coprime to \(p\), and \(p^t\le b<p^{t+1}\).

**Case \(a\le t\).** Here \(b\ge p^a\). Because \(a\ge1\) and \(p\nmid b\), equality is impossible. Thus \(b>p^a\). Lemma 9 of Guo–Qiu–Cao–Feng–Gao (the proved local prime-divisibility criterion) states precisely that \(p\mid D(k)\) if and only if \(b\le p^a\). Consequently \(\nu_p(D(k))=0\), agreeing with the formula.

**Case \(a>t\): the universal lower bound.** For any \(q\) in the defining range, put \(d=q-1\) and \(s=\nu_p(d)\). Kummer's carry theorem counts \(\nu_p\binom{qk}{k}\) as the number of carries in the base-\(p\) sum \(k+dk\). A carry through the first \(j\) digits occurs exactly when
\[
(k\bmod p^j)+(dk\bmod p^j)\ge p^j.
\]
For \(1\le j\le a\), since \(k=p^ab-1\), the residues are \(-1\) and \(-d\) modulo \(p^j\). Every \(j>s\) in this interval yields a carry; hence there are at least \(\max\{0,a-s\}\) such carries. When \(s\le t\), this is at least \(a-t\).

When \(s>t\), consider also the distinct digit boundaries
\[
a+t+1\le j\le a+s.
\]
Since \(n=p^ab<p^{a+t+1}\le p^j\) and \(0<d\le n-1<p^j\), we have \(k\bmod p^j=n-1\). Moreover \(p^j\mid dn\) and \(dk=d(n-1)\equiv-d\pmod{p^j}\), so \(dk\bmod p^j=p^j-d\). The residues sum to \(p^j+n-1-d\ge p^j\). These give an additional \(s-t\) carries beyond the first \(a\) digit boundaries. If \(t<s\le a\), the total is at least \((a-s)+(s-t)=a-t\); if \(s>a\), the high boundaries alone give \(s-t\ge a-t\). Thus in every case
\[
\nu_p\binom{qk}{k}\ge a-t.
\]

**A matching witness when \(b=1\).** Then \(t=0\), and choose \(q=p\). The base-\(p\) addition \(k+(p-1)k=pk\) has exactly \(a\) carries at boundaries \(1,\ldots,a\), and none later: both terms are smaller than \(p^{a+1}\), and so is their sum. Hence \(\nu_p\binom{pk}{k}=a=a-t\).

**A matching witness when \(b>1\).** Put \(u=b-p^t\) and \(q=1+p^au\). Because \(p\nmid b\), we have \(1\le u<p^a\), \(p\nmid u\), and \(2\le q\le p^ab=n\). The lower \(a\) digits of \((q-1)k=p^auk\) are zero, so no carry occurs in those digits. The remaining carries are precisely those obtained by adding \(b-1\) and \(uk\). Let \(s_p(v)\) denote the base-\(p\) digit sum. Since
\[
uk=p^a(ub-1)+(p^a-u),
\qquad
(b-1)+uk=p^aub+(p^t-1),
\]
and \(p\nmid ub\), the following digit-sum identities hold:
\[
\begin{aligned}
s_p(ub-1)&=s_p(ub)-1,\\
s_p(p^a-u)&=a(p-1)-s_p(u-1),\\
s_p(b-1)&=s_p(u-1)+1,\\
s_p(p^t-1)&=t(p-1).
\end{aligned}
\]
For the third identity, \(b-1=p^t+(u-1)\) with \(0\le u-1<(p-1)p^t\), so adding \(p^t\) increases the digit sum by one without carrying. Using the standard digit-sum form of Kummer's theorem,
\[
\begin{aligned}
(p-1)\nu_p\binom{(b-1)+uk}{b-1}
&=s_p(b-1)+s_p(uk)-s_p((b-1)+uk)\\
&=(a-t)(p-1).
\end{aligned}
\]
Therefore this allowed \(q\) satisfies \(\nu_p\binom{qk}{k}=a-t\). The universal lower bound is attained; together with the zero case and the exclusion of other primes, this proves the full factorization.

## Verification

The companion file `artifacts/verify.py` gives an integer-arithmetic check of this theorem's finite boundary cases and its explicit witnesses. It computes the defining binomial gcd directly for every \(2\le k\le160\), checks the formula and the minimum prime-adic valuations throughout \(3\le n\le1200\), and independently tests the explicit witness for every qualifying prime-power component up to \(n=12000\). It also verifies \(D(k)\mid k+1\) and the published prime-divisibility criterion in the tested range. No finite computation is used in place of the preceding infinite proof.

## Relationship to prior work

Guo, Qiu, Cao, Feng, and Gao prove the binary criterion \(D(k)=1\) in terms of the largest prime-power component of \(k+1\). Their Lemma 9 gives the local binary fact \(p\mid D(k)\) exactly when \(n/p^a\le p^a\); their finite-difference Lemma 4 restricts possible prime divisors to \(k+1\). Those statements do **not** determine higher exact prime powers dividing \(D(k)\). Here the new carry lower bound, high-boundary correction, and explicit valuation-attaining witness give the entire gcd for every \(k\).

OEIS A080170 records the indices at which the gcd is one, not its complete values. A prior analysis of the distribution of nontrivial gcds constrained by their prime factors estimates a counting function but does not imply the pointwise prime-power formula. The present theorem is a quantitative refinement of the same natural invariant, rather than another equivalently phrased unit test.

## Limitations

The result is specific to the full progression \(2\le q\le k+1\) and to the lower binomial index \(k\). It does not determine gcds over shortened progressions or with other lower-index sequences. No claim is made that the proof is independently audited.

## References

1. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, first publicly submitted 2026-06-22. Section 2, Lemmas 4 and 9 and Theorem 1.
2. OEIS A080170, sequence listing the indices for which this binomial progression gcd is one.
3. E. E. Kummer, classical carry theorem for prime-adic valuations of binomial coefficients.
