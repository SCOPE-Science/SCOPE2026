# Sharp dyadic precision in a Franel divisibility sum

## Finding
Let the Franel numbers and their weighted convolution be
\[
f_m=\sum_{a=0}^{m}\binom{m}{a}^{3},\qquad
S_n=\sum_{k=0}^{n-1}(3k+1)(-16)^{n-1-k}\binom{2k}{k}f_k.
\]
For every integer \(r\ge2\), with \(n=2^r\),
\[
\boxed{\nu_2(S_{2^r})=3r+1.}
\]
Equivalently, \(S_{2^r}\equiv2^{3r+1}\pmod{2^{3r+2}}\). Defining the integer quotient
\[
Q_n=\frac{S_n}{n\binom{2n}{n}}\quad(n\ge2),
\]
the same assertion is \(\nu_2(Q_{2^r})=2r\). The smaller dyadic boundary is exceptional: \(S_2=0\).

## Assumptions and scope
The valuation \(\nu_2\) is defined on nonzero rational numbers by exponent of two; the theorem concerns integers \(r\ge2\) only. The quotient integrality for every \(n\ge2\) is Guo's 2014 result [1, Theorem 1.3]; the proof below refines its exact identity [1, equation (2.4)]. No assertion is made about odd-prime valuations, arbitrary indices, or the valuation of zero.

## Proof
Guo [1, equations (2.1)–(2.4)] obtained the exact identity
\[
Q_n=\sum_{k=0}^{n-1}\binom{n+2k}{3k}\binom{3k}{k}\binom{2k}{k}
\frac{(k-n)(-4)^{n-k}}{8(2k+1)}.
\tag{1}
\]
For completeness, its derivation substitutes Sun's Franel expansion
\[
f_m=\sum_{k=0}^{m}\binom{m+2k}{3k}\binom{3k}{k}\binom{2k}{k}(-4)^{m-k}
\]
into the definition of \(S_n\) and interchanges two finite sums. The resulting inner sum has endpoint
\[
\sum_{m=k}^{n-1}(3m+1)(-16)^{n-m-1}\binom{2m}{m}
\binom{m+2k}{3k}(-4)^{m-k}
=\binom{2n}{n}\binom{n+2k}{3k}
\frac{n(k-n)(-4)^{n-k}}{8(2k+1)}.
\]
The endpoint identity follows by induction on \(n\): writing its right side as \(E_{n,k}\), the initial value is \(E_{k,k}=0\) and both sides satisfy
\[
E_{n+1,k}=-16E_{n,k}+(3n+1)\binom{2n}{n}\binom{n+2k}{3k}(-4)^{n-k}.
\]
The recurrence reduces to the two standard consecutive-binomial ratios and an elementary cancellation. This reconstructs the nonstandard telescoping step in [1].

Substitute \(j=n-k\) in (1) and denote its \(j\)-th summand by
\[
T_{n,j}=\frac{(-1)^{j+1}j4^j}{8(2n-2j+1)}
\frac{(3n-2j)!}{j!(n-j)!^3},\qquad1\le j\le n.
\tag{2}
\]
The factorial quotient is a multinomial coefficient, hence an integer. Let \(s_2(t)\) be the number of ones in the binary expansion of the nonnegative integer \(t\). Legendre's formula gives, for every \(j\),
\[
\nu_2(T_{n,j})=2j-3+\nu_2(j)+s_2(j)+3s_2(n-j)-s_2(3n-2j).
\tag{3}
\]
Now put \(n=2^r\). If \(1\le j\le n/2\), binary complementation yields
\[
s_2(n-j)=r-s_2(j-1),\quad
s_2(3n-2j)=r-s_2(j-1).
\]
Together with \(s_2(j)=s_2(j-1)+1-\nu_2(j)\), (3) becomes the exact layer formula
\[
\boxed{\nu_2(T_{n,j})=2r+2j-2-s_2(j-1)}
\quad(1\le j\le2^{r-1}).
\tag{4}
\]
The \(j=1\) summand has valuation exactly \(2r\); every \(2\le j\le n/2\) has valuation at least \(2r+j-1>2r\), since \(s_2(j-1)\le j-1\).

If \(r\ge3\) and \(j>n/2\), (2) and the multinomial integrality imply
\[
\nu_2(T_{n,j})\ge2j-3\ge n-1\ge2r+1.
\]
For \(r=2\), the only remaining indices \(j=3,4\) have valuations \(6,7\), respectively, also greater than \(2r\). Thus \(T_{n,1}\) is the unique term with smallest two-adic valuation, so no cancellation can remove its leading binary digit. Therefore \(\nu_2(Q_n)=2r\).

Finally \(\nu_2(n)=r\), while Legendre's formula implies \(\nu_2(\binom{2^{r+1}}{2^r})=1\). Multiplying \(Q_n\) by \(n\binom{2n}{n}\) gives \(\nu_2(S_{2^r})=2r+r+1=3r+1\). The boundary \(S_2=-16+16=0\) follows directly. \(\square\)

## Verification
Run `python VERIFY.py` in the same directory as this file. The script constructs Franel numbers from their second-order recurrence and checks the binomial sum independently at small indices. It verifies the published quotient identity for every \(2\le n\le26\), checks the valuation of every transformed summand for \(2\le r\le12\), and directly computes the claimed weighted sums for \(2\le r\le10\). The required terminal output is `VERIFY_OK`. These finite checks support the calculation but do not substitute for the preceding proof for arbitrary \(r\).

## Relationship to prior work
Guo [1, Theorem 1.3] proved divisibility by \(n\binom{2n}{n}\) for all \(n>1\), which at \(n=2^r\) guarantees only \(\nu_2(S_n)\ge r+1\). Identity (2.4) of [1] is used explicitly here. The additional ingredient is the exact binary-weight stratification (4), which makes the valuation equal to \(3r+1\), an improvement of \(2r\) binary digits over the general bound. This is not a new proof of Guo's original theorem.

Sun [2] studies congruences for prime-length (odd-prime) Franel sums, including denominators involving sixteen. Mao [3] strengthens a related odd-prime Franel supercongruence modulo the fourth prime power. Neither of their inspected statements gives the present exact dyadic endpoint valuation. The Franel numbers themselves are tabulated in OEIS A000172 [4]; that table is not a table of this convolution's valuations.

## Limitations
The result is confined to powers of two with exponent at least two and relies on the established Franel expansion from [1,2]. The degree of novelty relative to unlocated later work remains uncertain. The mathematical review accompanying this result is not an independent audit or priority certification.

## References
[1] V. J. W. Guo, *Proof of a supercongruence conjectured by Z.-H. Sun*, arXiv:1404.6978v1 (public 2014-04-28), Theorem 1.3 and equations (2.1)–(2.4), https://arxiv.org/abs/1404.6978.

[2] Z.-H. Sun, *Congruences involving Franel and Catalan-Larcombe-French numbers*, arXiv:1502.02499v3 (2015), https://arxiv.org/abs/1502.02499. The Franel identity cited in [1] is attributed there to Z.-W. Sun (2013), not to this later paper.

[3] G.-S. Mao, *Proof of some congruence conjectures of Z.-H. Sun involving Apéry-like numbers*, arXiv:2111.08778 (2021), https://arxiv.org/abs/2111.08778.

[4] OEIS A000172, Franel numbers, https://oeis.org/A000172.
