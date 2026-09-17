# Exact 2-adic valuations for the tenth power of the Thue--Morse generating function

Let
\[
T(x)=\prod_{j\ge 0}(1-x^{2^j}),\qquad T(x)^{10}=\sum_{n\ge0}t_{10}(n)x^n,
\]
and let \(\nu_2(a)\) denote the exponent of \(2\) in a nonzero integer \(a\).

## Theorem

For every \(n\ge0\),
\[
\boxed{\nu_2(t_{10}(n))=\nu_2\binom{n+9}{9}+2\,\mathbf 1_{n\equiv7\pmod8}.}
\]
In particular, \(t_{10}(n)\ne0\) for every \(n\ge0\).

Equivalently, if \(n=8q+r\), then
\[
\nu_2(t_{10}(8q+r))=
\begin{cases}
\nu_2(q+1),&r\in\{0,2,4,6\},\\
1+\nu_2(q+1),&r\in\{1,5\},\\
2+\nu_2(q+1),&r=3,\\
6+\nu_2(\lfloor q/2\rfloor+1),&r=7.
\end{cases}
\]

## Context

Gawron, Miska and Ulas initiated the systematic study of the coefficients \(t_m(n)\) and obtained exact positive-exponent 2-adic formulas in special cases, including powers of two and \(m=3\). Shen and Wang recently proved exact formulas for \(m=5\) and \(m=9\). Shen subsequently proved, among other results, the binomial valuation formula for the families \(m=2^r\) and \(m=3\cdot2^r\) with \(r\ge2\), together with the exceptional identity
\[
\nu_2(t_6(n))=\nu_2\binom{n+5}{5}+\mathbf1_{n\equiv3\pmod4}.
\]
The exponent \(m=10\) is not in either of the two families named in that result. The theorem above exhibits a similar but distinct exceptional correction: two extra powers of two precisely on the residue class \(7\pmod8\).

## Proof

Write \(t(n)=t_{10}(n)\), with \(t(n)=0\) for \(n<0\).

### 1. Seven residue classes modulo eight

Iterating \(T(x)=(1-x)T(x^2)\) three times gives
\[
T(x)^{10}=H(x)T(x^8)^{10},\qquad
H(x)=(1-x)^{10}(1-x^2)^{10}(1-x^4)^{10}.
\]
For \(0\le r<8\), define the section polynomial
\[
P_r(z)=\sum_j[x^{8j+r}]H(x)\,z^j.
\]
Direct binomial expansion gives, for \(0\le r\le6\),
\[
2^{b_r}\mid P_r(z)\quad\text{coefficientwise},
\qquad
2^{-b_r}P_r(z)\equiv1+z^8=(1-z)^8\pmod2,
\]
where
\[
(b_0,b_1,b_2,b_3,b_4,b_5,b_6)=(0,1,0,2,0,1,0).
\]
Taking the \(r\)-th section of the preceding functional equation yields
\[
\sum_{q\ge0}t(8q+r)z^q=P_r(z)T(z)^{10}.
\]
Over \(\mathbf F_2[[z]]\),
\[
T(z)=\prod_{j\ge0}(1+z^{2^j})=(1-z)^{-1},
\]
so for \(r\le6\)
\[
2^{-b_r}\sum_{q\ge0}t(8q+r)z^q
\equiv(1-z)^8(1-z)^{-10}=(1-z)^{-2}\pmod2.
\]
Consequently
\[
\frac{t(8q+r)}{2^{b_r}}\equiv q+1\pmod2.
\]
Thus, whenever \(q\) is even,
\[
\nu_2(t(8q+r))=b_r\qquad(0\le r\le6).
\]

### 2. A normalized dyadic recurrence

Set
\[
V_n=(t(n-1),t(n-2),\ldots,t(n-9))^T.
\]
Extracting coefficients from
\(T(x)^{10}=(1-x)^{10}T(x^2)^{10}\) gives
\[
V_{2n}=AV_n,
\qquad
A_{ij}=(-1)^i\binom{10}{2j-i}\quad(1\le i,j\le9),
\]
where the binomial coefficient is zero outside \(0\le2j-i\le10\).

Let
\[
D=\operatorname{diag}(2^6,2^1,2^2,2^1,2^3,2^1,2^2,2^1,2^6)
\]
and let \(J\) be the \(9\times9\) matrix whose every row is
\((1,0,0,0,0,0,0,0,1)\). For \(s\ge0\), put
\[
R_s=2^{-s}D^{-1}A^{s+4}.
\]
Exact integer calculation gives
\[
R_s\in M_9(\mathbf Z),\qquad R_s\equiv J\pmod2
\]
for \(0\le s\le8\). These finitely many identities propagate to every \(s\ge0\) from the annihilating identity
\[
\begin{aligned}
0={}&A^9+2A^8-19680A^7-34560A^6+76783616A^5+298975232A^4\\
&-64718110720A^3+85899345920A^2+8658654068736A
+35184372088832I.
\end{aligned}
\]
Indeed, after dividing the shifted identity by the normalization defining \(R_s\), one obtains
\[
\begin{aligned}
R_{s+5}={}&-R_{s+4}+4920R_{s+3}+4320R_{s+2}-4798976R_{s+1}
-9342976R_s\\
&+1011220480R_{s-1}-671088640R_{s-2}
-33822867456R_{s-3}-68719476736R_{s-4}.
\end{aligned}
\]
Every coefficient except the leading \(-1\) is even. Hence both integrality and the congruence \(R_s\equiv J\pmod2\) follow inductively.

Now write \(k=2^su\) with \(u\) odd. Then
\[
V_{16k}=A^{s+4}V_u=2^sDR_sV_u.
\]
Modulo two,
\[
T(x)^{10}\equiv(1-x)^{-10},
\]
so
\[
t(n)\equiv\binom{n+9}{9}\pmod2.
\]
By Lucas' theorem, this binomial coefficient is odd exactly when \(n\mathbin{\&}9=0\). For odd \(u\), exactly one of \(t(u-1)\) and \(t(u-9)\) is odd (with negative-index terms interpreted as zero). Since every row of \(J\) selects precisely those two coordinates, every coordinate of \(R_sV_u\) is odd. Therefore, with
\[
(d_1,\ldots,d_9)=(6,1,2,1,3,1,2,1,6),
\]
we have the exact formula
\[
\nu_2(t(16k-i))=\nu_2(k)+d_i\qquad(1\le i\le9).
\]

### 3. Completion

Let \(n=8q+r\).

For \(r\le6\), the section congruence handles even \(q\). If \(q\) is odd, set \(k=(q+1)/2\); then
\[
8q+r=16k-(8-r),
\]
and the dyadic recurrence gives
\[
\nu_2(t(8q+r))=b_r+\nu_2(q+1).
\]
The same formula also agrees with the even-\(q\) case because then \(\nu_2(q+1)=0\).

For \(r=7\), according as \(q=2a\) or \(q=2a+1\), one has
\[
8q+7=16(a+1)-9\quad\text{or}\quad16(a+1)-1,
\]
so the dyadic recurrence gives
\[
\nu_2(t(8q+7))=6+\nu_2(a+1)
=6+\nu_2(\lfloor q/2\rfloor+1).
\]

Finally, Legendre's formula (equivalently, Kummer's theorem) gives
\[
\nu_2\binom{8q+r+9}{9}=b_r+\nu_2(q+1)\qquad(0\le r\le6)
\]
and
\[
\nu_2\binom{8q+16}{9}=4+\nu_2(\lfloor q/2\rfloor+1).
\]
Combining these identities proves
\[
\nu_2(t_{10}(n))=\nu_2\binom{n+9}{9}+2\mathbf1_{n\equiv7\pmod8}.
\]

## Verification

The accompanying exact-integer script independently checks the section-polynomial congruences, the displayed annihilating identity for \(A\), the normalized matrix identities for the finite induction bases, the parity condition in the normalized recurrence, and the final valuation formula for \(0\le n\le100000\).

## Originality and limitations

Originality is asserted only to the best of our knowledge. Exact and synonymous searches for the tenth power, \(t_{10}(n)\), its 2-adic valuation, the binomial baseline \(\binom{n+9}{9}\), and the residue-class correction did not locate this formula. The 2018 paper treats other exact positive-exponent cases; the June 2026 paper proves the fifth- and ninth-power formulas; and the September 2026 paper's abstract states exact valuation families \(m=2^r\) and \(m=3\cdot2^r\) for \(r\ge2\), together with the special case \(m=6\), none of which includes \(m=10\).

The full text of arXiv:2609.16966 was not inspected, so an incidental tenth-power computation or remark not advertised in its abstract remains a material residual originality risk. No claim is made here about automaticity of the odd parts of \(t_{10}(n)\). The theorem concerns only the exact 2-adic valuation.

## References

1. M. Gawron, P. Miska, M. Ulas, *Arithmetic properties of coefficients of power series expansion of* \(\prod_{n=0}^{\infty}(1-x^{2^n})^t\), Monatshefte für Mathematik 185 (2018), 307--360. https://doi.org/10.1007/s00605-017-1041-2
2. Z. Shen, X. Wang, *2-adic Valuations of Coefficients of the Fifth and Ninth Powers of the Thue--Morse Generating Function*, arXiv:2606.28718 (2026). https://arxiv.org/abs/2606.28718
3. Z. Shen, *Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts*, arXiv:2609.16966 (2026). https://arxiv.org/abs/2609.16966
