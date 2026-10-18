# Sharp odd-index lifting resolves the overcubic tuple congruence conjecture

## Finding

Let \(\bar b_m(n)\) denote the number of overcubic partition \(m\)-tuples of \(n\). For all integers \(i\ge3\), \(k\ge0\), and \(n\ge0\), set \(M=2^ik+2^{i-1}-1\). Then
\[
\bar b_M(8n+5)\equiv0\pmod{2^{i+2}},\qquad
\bar b_M(8n+7)\equiv0\pmod{2^{i+3}}.
\]
Both moduli are best possible, simultaneously for every choice of \(i,k\):
\[
\nu_2\bigl(\bar b_M(5)\bigr)=i+2,\qquad
\nu_2\bigl(\bar b_M(7)\bigr)=i+3.
\]
This resolves both clauses of Conjecture 1.5 in Maity--Saikia, *Extending Recent Arithmetic Properties of Overcubic Partition Tuples* (2026). A stronger lifting statement underlies the result: put \(t=2^{i-3}(2k+1)\), define \(A(z)=\varphi(-z)\varphi(-z^2)=\sum_{n\ge0}a(n)z^n\), and let \(\bar b_3(n)\) be the triple-count. Then **for every odd positive integer \(n\)**,
\[
\boxed{\bar b_{4t-1}(n)\equiv (1-t)a(n)+t\,\bar b_3(n)\pmod{2^{i+3}}.}
\]

## Assumptions and scope

All series are formal power series over \(\mathbb Z\) in the indeterminate \(z\); no analytic-convergence assumption is needed. Write \(f_j(z)=\prod_{r\ge1}(1-z^{jr})\). The defining generating function and theta notation are
\[
F(z)=\sum_{n\ge0}\bar b_1(n)z^n=\frac{f_4(z)}{f_1(z)^2 f_2(z)},\quad
\sum_{n\ge0}\bar b_m(n)z^n=F(z)^m,\quad
\varphi(z)=\sum_{r\in\mathbb Z}z^{r^2}.
\]
The classical identities \(\varphi(-z)=f_1(z)^2/f_2(z)\) and \(\varphi(-z^2)=f_2(z)^2/f_4(z)\) imply \(A(z)=F(z)^{-1}\). The notation \(\nu_2(s)\) is the exponent of \(2\) in a nonzero integer \(s\). All stated valuation equalities concern strictly positive counts.

## Proof

**Step 1: an integral, parity-controlled fourth-power correction.** Since \(A(0)=1\) and \(A\equiv1\pmod2\), write \(A=1+2T\) with \(T\in z\mathbb Z[[z]]\). Expanding,
\[
F^4=A^{-4}=\sum_{j\ge0}(-1)^j\binom{j+3}{3}(2T)^j.
\]
Every nonconstant coefficient is divisible by \(8\): for \(j=1\) the coefficient is \(-8\), for \(j=2\) it is \(40\), and for \(j\ge3\) it is divisible by \(8\). Therefore
\[
C(z)=\frac{F(z)^4-1}{8}\in z\mathbb Z[[z]],\qquad F^4=1+8C.
\]
Modulo \(2\), the terms \(j=1,2\) in \(C\) contribute \(T\) and \(T^2\), while the terms \(j\ge3\) contribute zero, including \(j=3\) (coefficient \(-20\)) and \(j=4\) (coefficient \(70\)). Hence \(C\equiv T+T^2\pmod2\).

Let \(U=\sum_{r\ge1}(-1)^r z^{r^2}\), \(V=\sum_{r\ge1}(-1)^r z^{2r^2}\). The theta expansion gives \(A=(1+2U)(1+2V)\), so \(T=U+V+2UV\), and, in characteristic \(2\), squaring a series replaces each exponent by twice that exponent. Consequently,
\[
C\equiv T+T^2\equiv U+V+U^2+V^2
\equiv\sum_{r\ge1}z^{r^2}+\sum_{r\ge1}z^{4r^2}\pmod2.
\]
It follows that \(C^2\), and thus \(AC^2\), has only **even-indexed** nonzero coefficients modulo \(2\):
\[
[z^{2h+1}]AC^2\equiv0\pmod2\qquad(h\ge0).
\]
This is the extra parity gain needed beyond ordinary binomial lifting.

**Step 2: lift the triple series.** Put \(t=2^{i-3}(2k+1)\). Then \(\nu_2(t)=i-3\), \(M=4t-1\), and
\[
F^M=A(F^4)^t=A(1+8C)^t
=A+8tAC+64\binom t2AC^2+\sum_{j=3}^{t}8^j\binom tj AC^j.
\]
The elementary identity \(j\binom tj=t\binom{t-1}{j-1}\) implies, when \(1\le j\le t\),
\[
\nu_2\!\left(8^j\binom tj\right)\ge3j+(i-3)-\nu_2(j).
\]
For every \(j\ge3\) this is at least \(i+6\). The quadratic term has scalar coefficient divisible by \(2^{i+2}\), and the odd-index parity established in Step 1 supplies another factor \(2\). Therefore, in every odd coefficient, all terms with \(j\ge2\) vanish modulo \(2^{i+3}\). Since \(8AC=A(F^4-1)=F^3-A\), coefficient extraction yields
\[
\bar b_{4t-1}(n)\equiv (1-t)a(n)+t\bar b_3(n)\pmod{2^{i+3}}
\qquad(n\ge1\text{ odd}).
\]

**Step 3: the two progressions.** The coefficient \(a(n)\) is a signed integer sum over representations \(n=x^2+2y^2\), with \(x,y\in\mathbb Z\). Squares modulo \(8\) are \(0,1,4\), and twice a square modulo \(8\) is \(0\) or \(2\). Thus \(x^2+2y^2\) never equals \(5\) or \(7\) modulo \(8\), giving the *exact* vanishing
\[
a(8n+5)=a(8n+7)=0\quad(n\ge0).
\]
Saikia--Sarma, *Further Arithmetic Properties of Overcubic Partition Triples* (Theorem 1.1, 2024 preprint), established for every \(n\ge0\) the two base congruences
\[
\bar b_3(8n+5)\equiv0\pmod{32},\qquad
\bar b_3(8n+7)\equiv0\pmod{64}.
\]
Multiplying these by \(t\), whose \(2\)-adic valuation is \(i-3\), and applying Step 2 proves the respective moduli \(2^{i+2}\) and \(2^{i+3}\) for every \(i,k,n\) in the claimed ranges.

**Step 4: exact sharpness in each progression.** Direct truncated integer series calculations (also reproducible via the accompanying verifier) give
\[
\bar b_3(5)=1248=32\cdot39,\qquad
\bar b_3(7)=9792=64\cdot153.
\]
The Step 2 congruence immediately implies \(\nu_2(\bar b_M(5))=i+2\). At degree \(7\), an exact small-series coefficient identity is
\[
[z^7]AC^2=7424=2^8\cdot29.
\]
So the quadratic correction at degree \(7\) is divisible by at least \(2^{i+10}\). All higher corrections are divisible by at least \(2^{i+6}\). The same binomial expansion therefore yields the stronger *degree-seven-only* relation
\[
\bar b_M(7)\equiv t\bar b_3(7)\pmod{2^{i+4}},
\]
which implies \(\nu_2(\bar b_M(7))=i+3\). This proves both moduli are optimal for every permitted tuple parameter.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The independent Euler-product construction of \(F\) matches inversion of \(\varphi(-z)\varphi(-z^2)\) through degree \(191\). Exact integer calculations verify \(\bar b_3(5)=1248\), \(\bar b_3(7)=9792\), the degree-seven correction \(7424\), and the odd-index parity of \(AC^2\) through degree \(191\). The program compares both sides of the lifting congruence for each odd index through \(191\) over \(i=3,4,5,6,7\) and \(k=0,1,2,3\), checking \(1920\) modular identities; it additionally verifies both progressions and the exact sharpness at the two least indices. The finite computations corroborate, but do not replace, the universal formal-series proof.

## Relationship to prior work

Maity--Saikia (arXiv:2607.07270, first public July 8, 2026) state the two target formulas as Conjecture 1.5. Their Theorems 1.1--1.4 concern neighboring tuple-parameter classes with \(M\) shifted by \(0\) or \(-2\), not the \(-1\) class here. The exact triple congruences used in Step 3 were already proved by Saikia--Sarma (arXiv:2411.00013, Theorem 1.1), and are not claimed as new. Chacón--Sellers (arXiv:2606.21780, Section 3) develop the general theta and binomial perspective, but do not derive the odd-index lifting modulo \(2^{i+3}\) or the full conjectural family. The new ingredient is the mod-two even-support identity for \(AC^2\), which upgrades the standard parameter lifting precisely where the conjecture needs it. Established general congruences modulo smaller powers of \(2\) do not by themselves force these sharp moduli.

## Limitations

The argument establishes the stated congruences and sharpness for the specified \(4t-1\) family only. It does not classify all overcubic tuple congruences, cover arbitrary residue classes, or give asymptotics for their counts. The strongest coefficient lift stated here is restricted to odd indices. Earlier general theta/binomial identities are acknowledged, and independent external mathematical validation has not been performed. Literature searches cannot categorically exclude an implicit equivalent result in other sources.

## References

1. S. Maity and M. P. Saikia, *Extending Recent Arithmetic Properties of Overcubic Partition Tuples*, arXiv:2607.07270, submitted July 8, 2026; Conjecture 1.5 and Section 2. https://arxiv.org/abs/2607.07270
2. M. P. Saikia and M. Sarma, *Further Arithmetic Properties of Overcubic Partition Triples*, arXiv:2411.00013, first submitted October 19, 2024; Theorem 1.1. https://arxiv.org/abs/2411.00013
3. D. Chacón and J. A. Sellers, *Congruences for Overcubic Partition k-Tuples*, arXiv:2606.21780, submitted June 19, 2026; Section 3. https://arxiv.org/abs/2606.21780
