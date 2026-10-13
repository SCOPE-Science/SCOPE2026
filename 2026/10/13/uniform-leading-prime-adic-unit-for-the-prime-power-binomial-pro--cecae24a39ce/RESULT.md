# Uniform leading prime-adic unit for the prime-power binomial progression

## Finding

For every prime \(p\), positive integer \(a\), and every integer \(q\) with \(2\le q\le p^a\), one has
\[
\boxed{\binom{q(p^a-1)}{p^a-1}\equiv -p^a\pmod{p^{a+1}}.}
\]
In particular, the exact \(p\)-adic valuation of *every* member of this progression is \(a\), and the first nonzero \(p\)-adic digit of each member is the same, namely \(-1\). The modulus \(p^{a+1}\) is sharp because the common residue is not zero modulo this modulus. As a previously known consequence of related gcd results, the complete progression gcd equals \(p^a\).

## Assumptions and scope

The prime \(p\) may be \(2\), and \(a\ge1\) is arbitrary. Set \(A=p^a\). The variable \(q\) ranges over *all* integers in \([2,A]\), not merely primes. Binomial coefficients are ordinary positive integers; \(\nu_p(p)=1\). The boundary \(q=1\) is excluded, since its binomial coefficient is \(1\). No assertion is made for \(q>A\).

## Proof

Write \(m=q-1\), so \(1\le m<A\), and put \(K=A-1\), \(R=m(A-1)\), and \(N=(m+1)(A-1)=K+R\). Let \(s_p(t)\) be the sum of the base-\(p\) digits of \(t\). The identities
\[
K=A-1,\qquad R=(m-1)A+(A-m),\qquad N=mA+(A-1-m)
\]
are disjoint base-\(p\) block decompositions. If \(0\le t<A\), complementing its \(a\) base-\(p\) digits gives \(s_p(A-1-t)=a(p-1)-s_p(t)\). Applying this to \(m-1\) and \(m\) shows
\[
s_p(K)=s_p(R)=s_p(N)=a(p-1).
\]
By Legendre's factorial formula (equivalently Kummer's digit-sum formula),
\[
\nu_p\binom NK=\frac{s_p(K)+s_p(R)-s_p(N)}{p-1}=a.
\]
This proves the exact valuation; it remains to compute its leading unit.

For any nonnegative integer \(T\), let \(U_p(T!)=T!/p^{\nu_p(T!)}\), a unit modulo \(p\), and write the base-\(p\) digits as \(T=\sum_{j\ge0}T_jp^j\). Separating multiples of \(p\) from the factorial and applying Wilson's theorem in every complete block gives
\[
U_p(T!)\equiv(-1)^{\nu_p(T!)}\prod_{j\ge0}T_j!\pmod p.
\]
The identity also holds for \(p=2\) (where signs coincide). Consequently,
\[
\frac1A\binom NK\equiv (-1)^a\prod_{j\ge0}\frac{N_j!}{K_j!R_j!}\pmod p.
\]
Every denominator here is invertible modulo \(p\).

First assume that \(p\) is odd. For each of the lower \(a\) digits, write \(r_j\) for the \(j\)-th digit of \(m\), and \(t_j\) for that of \(m-1\). The corresponding digits of \(N,K,R\) are, respectively, \(p-1-r_j,p-1,p-1-t_j\). The digits at positions \(a+j\) are \(r_j,0,t_j\). Wilson's theorem yields
\[
(p-1-u)!\equiv\frac{(-1)^{u+1}}{u!}\pmod p\qquad(0\le u<p).
\]
Thus, multiplying the factorial ratios from these two positions cancels all \(r_j!\) and \(t_j!\), and leaves \((-1)^{r_j-t_j+1}\). The full factorial-ratio product therefore equals
\[
(-1)^{a+s_p(m)-s_p(m-1)}.
\]
Since \(m\ge1\), subtracting one in base \(p\) gives
\[
s_p(m)-s_p(m-1)=1-(p-1)\nu_p(m).
\]
The exponent \(a+s_p(m)-s_p(m-1)\) consequently has the parity of \(a+1\). Inserting the prefactor \((-1)^a\) proves \(\binom NK/A\equiv -1\pmod p\). For \(p=2\), every digit factorial is \(1\pmod2\), so the displayed unit-factorial formula immediately gives \(\binom NK/A\equiv1=-1\pmod2\). This completes the proof for all primes and all stated parameters.

## Verification

Run the standalone file `artifacts/verify.py` with Python 3. It independently computes exact integer binomial coefficients and factorial valuations, and separately reconstructs the normalized residue using base-\(p\) factorial products. It checked \(825\) triples with primes \(p\le31\) and \(p^a\le150\), exhaustively over \(2\le q\le p^a\), with no failures. The finite checks are illustrative; the infinite assertion follows from the preceding proof.

## Relationship to prior work

Guo, Qiu, Cao, Feng, and Gao (2026), in their proof of OEIS A080170, determine when the progression gcd is \(1\), and give the local criterion for whether a prime divides that gcd. Other work has already determined exact \(p\)-adic valuations of this gcd; in particular, the gcd for a prime-power parameter equals \(p^a\). Neither a gcd criterion nor its exact valuation specifies the first nonzero residue of *each* individual binomial coefficient. The new statement is the uniform unit congruence for the entire interval of \(q\). OEIS A080170 records the gcd-one indices rather than these normalized units.

## Limitations

The congruence concerns the prime-power parameter \(p^a-1\), not the full composite-parameter gcd problem. The leading unit is determined only modulo \(p\), not to higher \(p\)-adic precision. The available literature search cannot exclude an equivalent unindexed classical congruence. Independent validation has not been performed.

## References

1. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, and Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (first submitted 2026-06-22), especially Theorem 1 and Lemma 9, https://arxiv.org/pdf/2606.22997.
2. *OEIS A080170: Numbers \(k\) such that the complete binomial progression gcd is one*, https://oeis.org/A080170.
3. Standard classical identities: Wilson's theorem; Legendre's formula for factorial prime-adic valuations.
