# Strict positivity of the five-term truncation in the two-block odd partition conjecture

## Finding
Let
\[
P(q)=\prod_{j\ge 1}\frac{1+q^{2j-1}}{1-q^{2j}},\qquad
S_5(q)=q^3-q^6-3q^{10}+3q^{15}+6q^{21}.
\]
For every integer \(n\ge 0\), let \(b(n)=[q^n]P(q)S_5(q)\). Then
\[
b(0)=b(1)=b(2)=0,\qquad b(n)>0\quad(n\ge3).
\]
Thus the complete coefficientwise nonnegativity and strict-positivity assertions of Merca's Conjecture 1 hold for its first nontrivial truncation \(N=5\).

## Assumptions and scope
All identities are in the ring \(\mathbb Z[[q]]\) of integer formal power series. Products are coefficientwise well-defined. The index \(N=5\) refers to the first five terms in the triangular correction series
\[
S_N(q)=\sum_{r=1}^{N}(-1)^{T_{r-1}}T_{\lceil r/2\rceil}q^{T_{r+1}},
\quad T_r=r(r+1)/2.
\]
The assertion is for every integer coefficient index \(n\ge0\), not a finite range of indices and not all \(N\equiv1,2\pmod4\).

## Proof
Define a finite positive-coefficient factor
\[
P_{10}(q)=\prod_{j=1}^{10}\frac{1+q^{2j-1}}{1-q^{2j}},
\qquad R(q)=P(q)/P_{10}(q).
\]
Both \(P_{10}\) and \(R\) are well-defined series with nonnegative integer coefficients. The constant term of \(R\) is one, and \([q^{21}]R(q)\ge1\), because \(1+q^{21}\) occurs as the numerator factor with \(j=11\).

Set \(L=\operatorname{lcm}(2,4,\ldots,20)=5040\) and define the polynomial
\[
H(q)=S_5(q)\prod_{j=1}^{10}(1+q^{2j-1})
\prod_{j=1}^{10}\left(\sum_{r=0}^{L/(2j)-1}q^{2jr}\right).
\]
The product identity \((1-q^{L})/(1-q^{2j})=\sum_{r=0}^{L/(2j)-1}q^{2jr}\) yields the exact rational-function identity
\[
P_{10}(q)S_5(q)=\frac{H(q)}{(1-q^L)^{10}}.
\]
The degree of \(H\) is \(21+\sum_{j=1}^{10}(2j-1)+\sum_{j=1}^{10}(L-2j)=50411\). An exhaustive, exact *finite polynomial* calculation, repeated in two independent algebraic arrangements by the attached `verify.py`, proves
\[
[q^n]H(q)\ge0\quad(0\le n\le50411),\qquad
[q^n]H(q)=0\iff n\in\{0,1,2,26,30\}.
\]
For complete reproducibility, the first arrangement multiplies the ten positive geometric-polynomial factors using the exact recurrence \(B_n=A_n+B_{n-2j}-A_{n-L}\), then the ten odd numerator factors, then \(S_5\). The second arrangement calculates coefficients of \(S_5P_{10}\) by distinct-part and even-part dynamic programming, and applies the tenth \(L\)-step difference \([q^n]H=\sum_{k=0}^{10}(-1)^k\binom{10}{k}[q^{n-kL}]S_5P_{10}\). Both output the same \(50412\) integers, with the same zero set. This exact finite certificate, rather than checking finitely many coefficients of the desired infinite series, is the essential positivity input.

Since \((1-q^L)^{-10}\) has nonnegative coefficients and constant term one, all coefficients of \(P_{10}S_5\) are nonnegative. For \(3\le n<L\), its coefficient is \([q^n]H\), and is strictly positive except at \(n=26,30\). For every \(n\ge L\), write \(n=r+kL\) with \(0\le r<L\) and \(k\ge1\). Because \(H\) has strictly positive coefficient at \(r+L\) (this index lies between \(L\) and \(2L-1\)), the coefficient of \(P_{10}S_5\) at \(n\) is strictly positive.

Finally, \(P(q)S_5(q)=R(q)P_{10}(q)S_5(q)\). Multiplying by \(R\) preserves nonnegativity and all already-positive coefficients. At the two remaining indices, the \(q^{21}\) term of \(R\) gives the explicit lower bounds
\[
b(26)\ge [q^{21}]R\,[q^5]P_{10}S_5\ge1,\quad
b(30)\ge [q^{21}]R\,[q^9]P_{10}S_5\ge3.
\]
The series starts in degree \(3\), so its first three coefficients vanish. This completes the proof for every \(n\ge0\).

## Verification
Run `python3 verify.py` using Python 3 and no external packages. The checker constructs \(H\) in two exact integer arithmetic methods, checks its full coefficient range and zero indices, checks the first coefficients by direct signed partition enumeration, and prints `CERTIFICATE_PASS`. The polynomial coefficient-vector SHA-256 in the verification output is a reproducibility fingerprint, not an external proof or an independent audit. The machine-readable certificate is exact and finite; no inference from a sampled prefix of the infinite series is used.

## Relationship to prior work
Merca (2026), Conjecture 1, proposes coefficientwise nonnegativity and strict positivity for truncation lengths \(N\equiv1,2\pmod4\). Its Theorem 1.3 derives the correction series \(S_N\), and Corollary 1.2 proves positivity for the **infinite** correction series, which does not imply positivity of the five-term *truncation*. This result proves precisely the \(N=5\) case, the first length past \(N=1,2\). The later Merca paper on dyadic structure and theta-weighted congruences addresses different coefficient identities and congruences; no truncated \(N=5\) positivity theorem was found in accessible material.

## Limitations
No assertion is made for \(N=6\) or any \(N\ge9\), for a bijective explanation, or for minimality of ten finite Euler factors. The proof rests on exhaustive deterministic integer arithmetic for an explicit polynomial of degree \(50411\), supplemented by an algebraic rational-function identity. Reproduction of the code is recommended before citing or relying on the certificate. Overlap with unindexed or inaccessible literature remains possible. No independent mathematical audit has been performed.

## References
- M. Merca, *The two-block odd partition function*, arXiv:2609.33770v1 (first posted 2026-09-27), Conjecture 1 and Theorem 1.3. https://arxiv.org/abs/2609.33770
- M. Merca, *The two-block odd partition function*, Ramanujan Journal 71, article 23 (2026), https://doi.org/10.1007/s11139-026-01426-1
- M. Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for \(\operatorname{pod}(n)\)*, arXiv:2610.05020v1 (first posted 2026-10-04). https://arxiv.org/abs/2610.05020
