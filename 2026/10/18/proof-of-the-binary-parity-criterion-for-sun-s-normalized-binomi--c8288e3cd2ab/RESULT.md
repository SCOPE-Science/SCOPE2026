# Proof of the binary-parity criterion for Sun's normalized binomial convolution

## Finding

For every integer \(n\geq1\), define
\[
F(k)=\binom{6k}{3k}\binom{3k}{k},\qquad
s_n=\frac{1}{(2n-1)\binom{3n}{n}}\sum_{k=0}^{n}F(k)F(n-k).
\]
Then \(s_n\) is an integer and
\[
\boxed{s_n\equiv\begin{cases}
8\pmod{16},&n\text{ is a power of }2,\\
0\pmod{16},&\text{otherwise}.
\end{cases}}
\]
Equivalently, \(s_n/8\) is odd exactly when \(n\) is a power of two. This establishes the binary-parity clause attributed to Zhi-Wei Sun in OEIS A189286. The following stronger bounds also hold, with \(s_2(m)\) denoting the number of ones in the binary expansion of the nonnegative integer \(m\):
\[
\nu_2(s_n)\ge s_2(3n)+1\qquad(n\ge1),
\]
\[
\nu_2(s_n)\ge s_2(3n)+2\qquad(n\ge1\text{ not a power of }2),
\]
\[
\nu_2(s_{2^r})=3\qquad(r\ge0).
\]
The integrality assertion is a previously published theorem of Guo; the new statement is the exact binary-parity criterion and the accompanying digit-sum bounds.

## Assumptions and scope

All binomial coefficients have ordinary nonnegative integer arguments; \(n\) ranges over every positive integer, and \(k\) over \(0\le k\le n\). We write \(\nu_2(x)\) for the exponent of two dividing a nonzero integer or nonzero rational number. Here all summands and \(s_n\) are positive. The zero index is excluded: the source records \(s_0=-1\), so the divisible-by-eight statement concerns \(n\ge1\) only. Guo's 2013 Theorem 1.2 establishes integer normalization term by term; our valuation computation is independently meaningful in the two-adic rationals.

## Proof

Define the individual normalized summands
\[
Q_{n,k}:=\frac{F(k)F(n-k)}{(2n-1)\binom{3n}{n}}.
\]
By Guo's Theorem 1.2 [2], every \(Q_{n,k}\) is an integer, and \(Q_{n,k}=Q_{n,n-k}\). This prior theorem supplies ordinary integrality, not the parity conclusion.

Legendre's formula gives \(\nu_2(m!)=m-s_2(m)\). Because multiplying by two does not change binary digit sum, we calculate
\[
\begin{aligned}
\nu_2(F(j))
&=\nu_2\!\left(\frac{(6j)!}{(3j)!(2j)!j!}\right)
=s_2(3j)+s_2(2j)+s_2(j)-s_2(6j)\\
&=2s_2(j),\\
\nu_2\!\binom{3n}{n}&=2s_2(n)-s_2(3n).
\end{aligned}
\]
Since \(2n-1\) is odd, it follows **exactly**, including the endpoints \(k=0,n\), that
\[
\nu_2(Q_{n,k})=t+2c_n(k),\quad
t=s_2(3n),\quad
c_n(k)=s_2(k)+s_2(n-k)-s_2(n).
\tag{1}
\]
For nonnegative integers \(a,b\), the digit-sum difference \(s_2(a)+s_2(b)-s_2(a+b)\) equals the total number of carries in binary addition (counting every carry entering a new position). Hence \(c_n(k)\ge0\). Moreover \(c_n(k)=0\) exactly when the one-bits of \(k\) form a subset of the one-bits of \(n\). There are \(2^{s_2(n)}\) such values of \(k\), including zero and \(n\).

Split the defining sum into pairs \(\{k,n-k\}\) and, when \(n\) is even, the singleton \(k=n/2\). Each noncentral pair contributes \(2Q_{n,k}\). By (1), a pair with \(c_n(k)=0\) has exact valuation \(t+1\), so
\[
\frac{2Q_{n,k}}{2^{t+1}}\equiv1\pmod2.
\]
A pair with \(c_n(k)\ge1\) has valuation at least \(t+3\). For even \(n\), the central term has
\[
 c_n(n/2)=2s_2(n/2)-s_2(n)=s_2(n)\ge1,
\]
so its valuation is at least \(t+2\). In particular **no central zero-carry term exists**. The \(2^{s_2(n)}\) zero-carry values therefore form exactly \(2^{s_2(n)-1}\) disjoint two-element pairs.

Consequently the entire quotient \(s_n/2^{t+1}\) is an integer, and reduction modulo two yields
\[
\boxed{\frac{s_n}{2^{s_2(3n)+1}}\equiv2^{s_2(n)-1}\pmod2.}\tag{2}
\]
This establishes the first valuation lower bound. If \(n\) is a power of two, then \(s_2(n)=1\) and \(s_2(3n)=2\), so (2) gives \(\nu_2(s_n)=3\). If \(n\) is not a power of two, then \(s_2(n)\ge2\), hence (2) gives \(\nu_2(s_n)\ge s_2(3n)+2\). Finally \(s_2(3n)\ge2\) for every positive integer \(n\): if \(3n\) had exactly one binary one, then \(3n\) would equal a power of two, impossible since \(3\mid3n\). Thus \(s_n\equiv0\pmod{16}\) off the powers of two, whereas \(s_n\equiv8\pmod{16}\) at powers of two. This proves the theorem for all \(n\ge1\).

## Verification

A self-contained Python 3 standard-library script, `verify.py`, checks exact integer normalizations and the valuation formula against factorial valuations for all \(1\le n\le512\), together with the mod-16 dichotomy and zero-carry parity. It prints `VERIFY_OK` if every check succeeds. This finite verification is supplementary; equation (1), binary carry counting, and reflection pairing provide the infinite proof.

Run with `python3 verify.py` from the directory containing the extracted files. The script has no external dependencies.

## Relationship to prior work

Zhi-Wei Sun's 2011 sequence and conjectural parity criterion are documented in [1] and [3]. In 2013 Guo proved the stronger **integrality of every individual normalized summand** [2], and his introduction notes that Sun had already proved eight-divisibility of the full sum. Neither Guo's stated theorems nor the inspected material in Sun's published-version paper supplies the exact oddness-of-\(s_n/8\) characterization. The subsequently published A189286 entry in [4] reports a new proof of integrality, but its stated theorem and derivation do not treat the parity clause. Equation (2) connects the missing parity criterion to the zero-carry pairs in Kummer's binary-addition framework. This is a claim of coverage relative to the cited and searched materials, not a claim of independently certified research priority.

## Limitations

The theorem gives the parity of \(s_n/8\) and some general lower bounds, not the exact valuation of \(s_n\) at every non-power-of-two index or odd-prime valuations. It uses Guo's established integrality theorem for the integer nature of the normalized summands; the two-adic valuation identities themselves follow directly from Legendre's formula. A broad prior theorem not located in the inspected literature could conceivably imply the same parity statement. Independent mathematical assessment has not been performed.

## References

[1] Zhi-Wei Sun, *Some new series for \(1/\pi\) and related congruences*, arXiv:1104.3856, first public version 2011-04-19, https://arxiv.org/abs/1104.3856 (see the original recorded conjecture; the accessible 2017 revision records the same sequence).

[2] Victor J. W. Guo, *Proof of Sun's conjecture on the divisibility of certain binomial sums*, arXiv:1301.4877v1 (2013-01-21), Theorem 1.2 and its proof, https://arxiv.org/html/1301.4877v1 .

[3] OEIS Foundation, *A189286*: normalized binomial convolution and Sun's parity conjecture, https://oeis.org/A189286 (accessed 2026-10-17; entry attributes the conjecture to 2011-04-19).

[4] *OEIS Open*, arXiv:2608.11941v2 (2026), Appendix A.1, A189286 entry: the stated resolved conjecture concerns termwise integrality, https://arxiv.org/html/2608.11941v2 .
