# Exact dyadic valuations for two-color quaternary partitions

## Finding

Let \(h_n=S_{4,2}(n)\) be the coefficients of the two-color quaternary partition series
\[
H(x)=\sum_{n\ge0}h_nx^n=(1-x)^{-2}\prod_{j\ge0}(1-x^{4^j})^{-6}
=(1-x)^{-8}\prod_{j\ge1}(1-x^{4^j})^{-6}.
\]
For every integer \(n\ge1\),
\[
\nu_2(h_n)=\begin{cases}
3,&n\text{ odd},\\
2,&\nu_2(n)\text{ odd},\\
4,&\nu_2(n)\ge2\text{ even}.
\end{cases}
\tag{1}
\]
In fact, \(h_n\equiv8n\pmod{32}\) when \(n\) is odd; \(h_n\equiv4\pmod8\) when \(\nu_2(n)\) is odd; and \(h_n\equiv16\pmod{32}\) when \(\nu_2(n)\ge2\) is even.

Set \(b_j=\varphi_4(h_{j+1})=\lfloor\nu_2(h_{j+1})/2\rfloor\). Then \(b_0=b_1=1\), \(b_3=2\) and, for all integers \(j\ge0\),
\[
 b_{4j+2}=b_{4j+1}=b_{4j}=1,\qquad
 b_{8j+7}=b_{2j+1},\qquad
 b_{16j+11}=b_{16j+3}=b_{8j+3}=2.
\tag{2}
\]
Thus Conjecture 6.6(4) of Ulas and Żmija holds; its component of Conjecture 6.6(2), asserting \(4\)-automaticity at the parameter \(m=2\), also holds. The levels \(\nu_2(h_n)=3,2,4\) have natural densities \(1/2,1/3,1/6\), respectively.

## Assumptions and scope

All power series identities are identities in \(\mathbb Z[[x]]\). The coefficient \(h_n\) counts partitions using eight colors for parts of size one and six colors for each larger part of size \(4^j\) with \(j\ge1\). This is the definition of \(S_{4,2}(n)\) in the cited paper, where in general the part of size one has \(km\) colors and each other allowed size has \(m(k-1)\) colors. The special coefficient \(h_0=1\) has valuation zero and is excluded from (1). For a positive integer \(z\), \(\nu_2(z)\) denotes its binary valuation; \(\varphi_4(z)=\lfloor\nu_2(z)/2\rfloor\).

## Proof

Define
\[
R(x)=\frac{(1-x^4)^2}{(1-x)^8}=\sum_{n\ge0}r_nx^n.
\]
Splitting off the first power-of-four factor in \(H(x)\) gives the exact Mahler equation \(H(x)=R(x)H(x^4)\). Introduce the explicit integer polynomial
\[
\begin{aligned}
P(x)={}&8x+4x^2+24x^3+8x^4+8x^5+12x^6+24x^7\\
&+16x^8+8x^9+20x^{10}+24x^{11}+24x^{12}\\
&+8x^{13}+28x^{14}+24x^{15}.
\end{aligned}
\]
The following is a finite polynomial identity modulo \(32\), verified simply by multiplication: every coefficient of
\[
(1-x^{16})(1-x^4)^2-(1-x)^8(1-x^{16}+P(x))
\tag{3}
\]
is divisible by \(32\). Since both denominators have unit constant terms, (3) implies
\[
R(x)\equiv1+\frac{P(x)}{1-x^{16}}\pmod{32}.
\tag{4}
\]
Consequently \(r_0=1\); every \(r_n\) with \(n\ge1\) is divisible by \(4\); and the following more precise statements hold:
\[
\begin{aligned}
r_n&\equiv8n\pmod{32}&&\text{if }n\text{ is odd},\\
r_n&\equiv4\pmod8&&\text{if }n\equiv2\pmod4,\\
r_{4t}&\equiv8t\pmod{32}&&\text{for }t\ge1.
\end{aligned}
\tag{5}
\]
The coefficients of \(H(x)=R(x)H(x^4)\) satisfy
\[
h_n=\sum_{0\le j\le\lfloor n/4\rfloor}r_{n-4j}h_j.
\tag{6}
\]
We first prove by strong induction on \(n\ge1\) that \(4\mid h_n\). For \(4\nmid n\), every index \(n-4j\) in (6) is positive, so (5) applies. For \(n=4t\), the term \(j=t\) is \(h_t\), divisible by four by induction, and all other terms have a positive \(r\)-index. This proves the claim.

If \(n\) is odd, the terms of (6) with \(j\ge1\) are multiples of \(8\cdot4=32\): their \(r\)-indices are odd and positive, so (5) applies, and \(4\mid h_j\). The initial term therefore gives \(h_n\equiv r_n\equiv8n\pmod{32}\). If \(n\equiv2\pmod4\), all terms in (6) with \(j\ge1\) vanish modulo \(8\) because \(4\mid r_{n-4j}\) and \(4\mid h_j\). Thus \(h_n\equiv r_n\equiv4\pmod8\).

For \(t\ge1\), separate the final summand \(h_t\) in (6) at \(n=4t\). Every intermediate summand (where \(1\le j<t\)) is divisible by \(8\cdot4=32\), by the last congruence in (5) and the proven divisibility of \(h_j\). Hence
\[
h_{4t}\equiv h_t+8t\pmod{32}.
\tag{7}
\]
Write \(n=4^q u\), where \(q\ge1\) and \(4\nmid u\). Repeated application of (7) gives
\[
h_n\equiv h_u+8u\bigl(1+4+\cdots+4^{q-1}\bigr)
\equiv h_u+8u\pmod{32}.
\tag{8}
\]
If \(u\) is odd, (8) is \(h_n\equiv16u\equiv16\pmod{32}\), so the valuation is four. If \(u\equiv2\pmod4\), (8) implies \(h_n\equiv h_u\equiv4\pmod8\), so the valuation is two. Together with the odd case this proves (1) for every positive \(n\).

For (2), the value of \(b_j\) is two precisely when \(\nu_2(j+1)\) is a **positive even** integer; otherwise it is one. The three constant-index strings in (2) are immediate. For the remaining equality, \(\nu_2(8j+8)=3+\nu_2(j+1)\), while \(\nu_2(2j+2)=1+\nu_2(j+1)\); these are simultaneously positive and even. This proves all relations. The output two occurs exactly when the base-four expansion of \(n\) has at least one trailing zero digit and the first digit to its left is odd (one or three). A finite automaton can track whether the number of trailing binary zeros is a positive even integer (equivalently, the base-four condition); this proves \(4\)-automaticity for positive indices. The exceptional output \(\varphi_4(h_0)=0\) can be assigned to the base-four input zero using a separate automaton state, so the full sequence indexed from zero is also \(4\)-automatic.

Finally, among positive integers \(n\), the density of \(\nu_2(n)=t\) is \(2^{-(t+1)}\). Summing the convergent geometric series for odd \(t\ge1\) gives \(1/3\); summing for positive even \(t\ge2\) gives \(1/6\); odd integers have density \(1/2\). This proves the stated valuation frequencies.

## Verification

The standalone \(\texttt{verify.py}\) included alongside this document independently multiplies the finite polynomials in (3) and checks every coefficient modulo \(32\). It also constructs coefficients of \(H(x)\) modulo \(32\) directly from the colored partition product up to a stated cutoff, compares them with (1), and tests the relations (2) on the available range. The finite checks detect implementation and transcription errors; the unrestricted result is proved by (3)--(8).

## Relationship to prior work

Ulas and Żmija formulated the exact relations (2) in their Conjecture 6.6(4), alongside a general \(4\)-automaticity conjecture in part (2). Their main proved valuation theorems concern prime bases; the parameter \((k,m)=(4,2)\) is composite-base and is presented as conjectural in their Section 6. The present statement gives a stronger exact binary-valuation formula and all three natural densities for this specific case. Results for composite bases under the different restriction \(\nu_2(m)\ge2\) do not imply the case \(m=2\). Other work on uniformly colored prime-ary partitions studies different generating functions. The finite polynomial certificate (3) is an elementary, complete way to check the nonstandard input to this proof.

## Limitations

This establishes the case \(k=4,m=2\), not the full conjectures for every color parameter or every composite base. The claimed novelty is relative to the sources and equivalences inspected, not a certificate of universal literature priority. The derivation concerns valuations only; it does not characterize higher binary digits of normalized coefficients. No independent scientific validation has been performed.

## References

1. M. Ulas and B. Żmija, *On p-adic valuations of certain m colored p-ary partition functions*, arXiv:1904.03398 (first public version 6 April 2019), *Ramanujan Journal* 55 (2021), 623–660, DOI: 10.1007/s11139-020-00256-z; especially Section 6, Conjecture 6.6.
2. M. Ulas and B. Żmija, *On p-adic valuations of colored p-ary partitions*, arXiv:1809.04628, *Monatshefte für Mathematik* 188 (2019), 351–368, DOI: 10.1007/s00605-018-1227-2.
3. B. Żmija, *Arithmetic properties of colored p-ary partitions*, DOI: 10.1007/s10474-023-01382-y (2023); its accessible description concerns prime-ary partition functions rather than the precise quaternary series here. Full text was not inspected, which remains a bibliographic limitation.
