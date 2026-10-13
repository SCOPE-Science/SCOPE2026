# Exact ternary Carmichael periods for A158690

## Finding

Let \(a(n)\) be the integer sequence with exponential generating function
\[
\sum_{n\ge0}a(n)\frac{t^n}{n!}
=1+\sum_{m\ge1}\prod_{j=1}^m\left(1-e^{-(2j-1)t}\right).
\]
For every integer \(r\ge1\), the **least eventual period** of \(a(n)\) modulo \(3^r\) is exactly
\[
\boxed{2\cdot3^{r-1}}.
\]
More precisely, for every integer \(r\ge2\) and every \(n\ge3r\),
\[
a\!\left(n+2\cdot3^{r-2}\right)-a(n)\equiv
\begin{cases}
2\cdot3^{r-1}\pmod{3^r},&n\text{ even},\\
0\pmod{3^r},&n\text{ odd}.
\end{cases}
\]
For \(n\ge3\) one also has \(a(n)\equiv(-1)^{n+1}\pmod3\).

## Assumptions and scope

All indices and exponents are ordinary nonnegative integers. For \(m\ge1\), define
\[
P_m(n)=n![t^n]\prod_{j=1}^{m}\bigl(1-e^{-(2j-1)t}\bigr),
\quad P_0(n)=\mathbf 1_{n=0}.
\]
For each fixed \(n\ge1\), only \(m\le n\) contributes to \(a(n)=\sum_{m=1}^{n}P_m(n)\). The theorem determines the exact least **eventual**, not necessarily the initial, period for each power of three. No assertion is made for other prime powers.

## Proof

**1. Integral factorial divisibility.** Put \(y=e^{-t}-1\) and \(d_j=2j-1\). The polynomial
\[
F_m(y)=\prod_{j=1}^m\bigl(1-(1+y)^{d_j}\bigr)
\]
lies in \(y^m\mathbb Z[y]\). Since
\[
n![t^n](e^{-t}-1)^k=(-1)^n k!\,S(n,k),
\]
where \(S(n,k)\) is a Stirling number of the second kind, we have \(m!\mid P_m(n)\) for all \(m,n\). Thus \(3^r\mid P_m(n)\) if \(m\ge3r\), because \((3r)!\) contains at least \(r\) factors of three.

**2. An eventual Carmichael period.** Inclusion–exclusion gives, for \(n\ge1\),
\[
P_m(n)=(-1)^n\sum_{S\subseteq\{1,\ldots,m\}}(-1)^{|S|}K_S^n,
\qquad K_S=\sum_{j\in S}(2j-1).
\]
Fix \(r\ge1\) and \(n\ge3r\). The factorial divisibility just proved removes every \(m\ge3r\), both at \(n\) and at later indices. For all remaining terms, \(3\mid K_S\) implies \(K_S^n\equiv0\pmod{3^r}\), while \(3\nmid K_S\) implies \(K_S^{2\cdot3^{r-1}}\equiv1\pmod{3^r}\). Since the shift is even, it preserves the common sign \((-1)^n\). Therefore \(2\cdot3^{r-1}\) is a period modulo \(3^r\) from every \(n\ge3r\).

**3. A first-third shift and its exact leading digit.** Suppose \(r\ge2\), \(n\ge3r\), and set \(h=2\cdot3^{r-2}\). For \(3\nmid k\), write
\[
Q(k)=\frac{k^2-1}{3}\pmod3.
\]
The elementary binomial congruence
\[
\frac{k^h-1}{3^{r-1}}\equiv Q(k)\pmod3
\]
follows by expanding \((1+3c)^{3^{r-2}}\) with \(c=(k^2-1)/3\) (it also holds when \(r=2\)). For \(3\mid k\), both \(k^n\) and \(k^{n+h}\) vanish modulo \(3^r\).

Consequently, divide the difference \(a(n+h)-a(n)\) by \(3^{r-1}\) and reduce modulo three. The contribution from a fixed \(m\) equals
\[
H_m(\epsilon)=(-1)^\epsilon
\sum_{S\subseteq\{1,\ldots,m\}}(-1)^{|S|}\rho_\epsilon(K_S)Q(K_S)\pmod3,
\quad \epsilon\equiv n\pmod2,
\]
where \(\rho_0(k)=1\) and \(\rho_1(k)=k\pmod3\) for \(3\nmid k\), and we declare the entire summand zero for \(3\mid k\).

The summand depends only on \(K_S\bmod9\): indeed \(Q(k+9)\equiv Q(k)\pmod3\) on units, and both residue and parity factors are unchanged. For every \(m\ge5\), the factor with \(j=5\) has \(d_5=9\); pairing every subset not containing \(5\) with the corresponding subset containing \(5\) cancels these contributions exactly modulo three. Hence \(H_m(\epsilon)=0\) for all \(m\ge5\), independently of \(r\).

Only four explicit subset sums remain. Their values, computed by substituting \(K_S\) in the displayed finite formula, are

| \(m\) | \(H_m(0)\pmod3\) | \(H_m(1)\pmod3\) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 2 | 1 |
| 3 | 0 | 2 |
| 4 | 0 | 0 |
| **Total** | **2** | **0** |

Therefore the normalized difference is \(2\pmod3\) for even \(n\) and zero for odd \(n\), proving the displayed half-shift congruence.

**4. Minimality.** Modulo three, the first two products suffice: \(P_1(n)=(-1)^{n+1}\), while \(P_2(n)=(-1)^n(4^n-1-3^n)\equiv0\pmod3\) for \(n\ge1\); all \(P_m(n)\) with \(m\ge3\) are divisible by three. Thus \(a(n)\equiv(-1)^{n+1}\pmod3\) for all \(n\ge3\), so every eventual period modulo \(3^r\) must be even. The least eventual period divides the established eventual period \(2\cdot3^{r-1}\). If it were a proper divisor for \(r\ge2\), it would divide \(h=2\cdot3^{r-2}\), contradicting the nonzero half-shift for every even \(n\ge3r\). For \(r=1\), the alternating modulo-three residues already give least period two.

## Verification

The accompanying standalone `verify_ternary.py` independently evaluates \(a(n)\) by (i) repeated exponential-product binomial convolution and (ii) an integral polynomial expansion in \(e^{-t}-1\) followed by Stirling numbers. Both agree for \(0\le n\le110\) modulo \(3^5\), including the OEIS initial values. The verifier performs 764 full- and first-third-shift coefficient checks for \(1\le r\le5\), and independently enumerates the seven finite-difference layers \(H_m\) for each parity. Execute `python3 verify_ternary.py` from this package's directory; `replay.txt` records an actual successful run. The finite tests are not substituted for the proof of the infinite family.

## Relationship to prior work

The public OEIS record A158690 defines this sequence and records Bala's eventual-periodicity conjecture. Ahaan Kallat proved in 2026 that the Carmichael exponent \(\lambda(q)\) is an eventual period modulo every positive integer \(q\). For \(q=3^r\), that establishes the **upper** period \(2\cdot3^{r-1}\); it does not, by itself, determine whether the period is minimal. The additional first-third-shift congruence above proves sharpness for the entire ternary tower and explains the parity-dependent obstruction. The comparison is based on the accessible OEIS entry and the source's bibliographic abstract; the full 2026 manuscript could not be inspected here.

## Limitations

The theorem does not determine the **least preperiod** for any \(r\), nor sharpness for primes other than three. The full text of the motivating seven-page manuscript was unavailable during literature comparison, so possible stronger statements in its body or in unindexed literature remain an originality risk. The result has not been independently audited.

## References

1. OEIS Foundation, "A158690," https://oeis.org/A158690 (entry including comments by Peter Bala, 2021, and update pointing to Kallat, September 2026).
2. A. Kallat, "A Proof of Bala's Congruence Conjectures for A158690," arXiv:2609.07238v1, originally posted 2026-09-07, https://arxiv.org/abs/2609.07238 (bibliographic abstract accessible; full PDF unavailable here).
3. MSC2020, class 11B50, sequences modulo an integer.

