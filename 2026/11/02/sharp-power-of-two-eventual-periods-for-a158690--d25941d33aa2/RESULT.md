# Sharp power-of-two eventual periods for A158690

## Finding

Let \(a(n)\) be the integer sequence defined formally by
\[
\sum_{n\ge0}a(n)\frac{t^n}{n!}
=1+\sum_{m\ge1}\prod_{j=1}^{m}\bigl(1-e^{-(2j-1)t}\bigr).
\]
For each integer \(r\ge1\), the least eventual period of \(a(n)\bmod 2^r\) is exactly
\[
T_r=\begin{cases}
1,&r=1,\\
2,&2\le r\le4,\\
2^{r-3},&r\ge5.
\end{cases}
\]
Moreover, for every \(r\ge5\) and every integer \(n\ge r\), the *half-period defect* is precisely
\[
a(n+2^{r-4})-a(n)\equiv
\begin{cases}2^{r-1}\pmod{2^r},&n\text{ even},\\
0\pmod{2^r},&n\text{ odd}.
\end{cases}
\]
Thus the Carmichael-function upper bound \(2^{r-2}\) for \(r\ge3\) is never sharp for this sequence once \(r\ge4\), and the smaller period is sharp for every \(r\ge5\).

## Assumptions and scope

All generating series are formal. Define \(H(y)\in\mathbb Z[[y]]\) by
\[
H(y)=1+\sum_{m\ge1}\prod_{j=1}^{m}
\left(1-(1+y)^{-(2j-1)}\right)=\sum_{m\ge0}c_my^m.
\]
Each product has order at least \(m\), so the definition is coefficientwise finite. Substituting \(y=e^t-1\) gives the stated exponential generating series. An *eventual period* \(T>0\) modulo \(M\) means \(a(n+T)\equiv a(n)\pmod M\) for all sufficiently large integers \(n\); its least possible value is meant. The theorem applies to **every** integer exponent \(r\ge1\), not only to tested values.

## Proof

**1. Exact reduction to power sequences.** The Stirling-number identity gives
\[
a(n)=\sum_{m=0}^{n}c_m m!\left\{\begin{matrix}n\\m\end{matrix}\right\},\qquad
m!\left\{\begin{matrix}n\\m\end{matrix}\right\}
=\sum_{j=0}^m(-1)^{m-j}\binom mj j^n\quad(n\ge1).
\]
Fix \(r\ge1\). Since \(2^r\mid (2r)!\), all summands indexed by \(m\ge2r\) vanish modulo \(2^r\), for any \(n\). Consequently \(a(n)\) is congruent modulo \(2^r\) to a *fixed* integer linear combination of \(j^n\), \(0\le j<2r\). If \(n\ge r\), every even \(j\) contributes zero modulo \(2^r\), including \(j=0\). Thus all subsequent congruence calculations can be performed termwise using odd \(j\), without assuming any finite experiment proves a general statement.

**2. The necessary modulo-\(32\) base.** Expanding the finite products in \(H\) to degree seven gives, exactly modulo \(32\),
\[
(c_0,c_1,\ldots,c_7)=(1,1,2,7,1,5,11,30).
\]
For \(m\ge8\), \(32\mid m!\), so modulo \(32\) the inclusion-exclusion formula becomes
\[
a(n)\equiv\sum_{j=0}^{7}B_jj^n,\qquad
(B_0,\ldots,B_7)=(4,23,16,19,19,25,25,30),
\]
where \(B_j=\sum_{m=j}^7c_m(-1)^{m-j}\binom mj\pmod{32}\). For \(n\ge5\), even bases contribute zero. Every odd base has eighth power \(1\pmod{32}\); checking the eight residues \(n=5,\ldots,12\) gives
\[
(a(5),\ldots,a(12))\equiv(31,17,31,1,31,17,31,1)\pmod{32}.
\]
Hence, **for every** \(n\ge5\),
\[
a(n)\equiv
\begin{cases}1\pmod{32},&n\equiv0\pmod4,\\
17\pmod{32},&n\equiv2\pmod4,\\
31\pmod{32},&n\text{ odd}.
\end{cases}
\]
In particular, \(a(n+2)-a(n)\equiv16\pmod{32}\) for even \(n\ge5\) and \(0\pmod{32}\) for odd \(n\ge5\).

**3. Exact dyadic lifting.** For each odd integer \(j\) and integer \(s\ge1\), write \(j^2=1+8u\). The binomial expansion and
\(\nu_2\bigl(\binom{2^{s-1}}{k}\bigr)\ge s-1-\nu_2(k)\)
show that terms of order \(k\ge2\) are divisible by \(2^{s+4}\). Therefore
\[
j^{2^s}-1\equiv2^{s-1}(j^2-1)\pmod{2^{s+4}}.
\]
Apply this congruence termwise to the fixed odd-base representation from step 1, with \(r=s+4\) and \(n\ge r\). It follows that
\[
a(n+2^s)-a(n)\equiv
2^{s-1}\bigl(a(n+2)-a(n)\bigr)\pmod{2^{s+4}}.
\]
Step 2 then yields the asserted half-period defect with \(s=r-4\).

**4. Minimality and small powers.** For \(r\ge5\), put \(T=2^{r-4}\). The defect is nonzero modulo \(2^r\) at every even \(n\ge r\), so \(T\) is not an eventual period. But \(T\) is even, so applying the defect twice gives \(a(n+2T)\equiv a(n)\pmod{2^r}\) for every \(n\ge r\). The least eventual period divides \(2T\), a power of two, and cannot divide \(T\); hence it equals \(2T=2^{r-3}\). Finally, the modulo-\(32\) classification from step 2 reduces to the alternating distinct values \(1\) and \(-1\) modulo \(4,8,16\), and to the constant value \(1\) modulo \(2\). Their least eventual periods are respectively \(2\) and \(1\), completing every case.

## Verification

Run `python3 verify.py` (Python standard library only). It independently computes the first eight coefficients of \(H\) using binomial expansions, constructs their inclusion-exclusion weights, checks the eight modulo-\(32\) power values, and enumerates additional finite modular checks at moduli \(2^5\) through \(2^{10}\). The exact symbolic binomial argument above, rather than finite enumeration, proves all exponents.

## Relationship to prior work

A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238 (first posted September 7, 2026), proves the general eventual-period upper bound \(\lambda(M)\) using the Stirling/power-sum representation. That representation is used explicitly here. The source does not determine the least periods for all powers of two, or the half-period defect. The OEIS A158690 entry records Bala's particular example of a period-two tail modulo \(16\), which this classification includes but does not treat as a new observation. The contribution here is the exact all-exponent law and sharp half-period defect from the modulo-\(32\) base.

## Limitations

This result is specific to A158690 and moduli which are powers of two. It does not determine minimal eventual periods at arbitrary odd prime powers or general composite moduli. The starting index \(n\ge r\) for the displayed defect is sufficient; no optimal preperiod is asserted. Priority remains subject to comparison against any unindexed older 2-adic congruence results. No independent mathematical audit has been carried out.

## References

1. A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238v1, September 7, 2026, Sections 1–4. https://arxiv.org/abs/2609.07238
2. OEIS Foundation, *A158690*, including P. Bala's December 18, 2021 congruence conjectures and the explicit modulo-\(16\) example. https://oeis.org/A158690
3. R. Graham, D. Knuth, and O. Patashnik, *Concrete Mathematics*, 2nd ed., Chapter 6 (Stirling-number power-sum identity).
