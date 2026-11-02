# Exact joint Möbius-sign distribution for affine shifts of binary-field cubics

## Finding

Let \(q=2^m\) with any integer \(m\ge1\), and let \(h(T)=uT+v\in\mathbb F_q[T]\), where \(u\ne0\) and \(v\) is arbitrary. The polynomial Möbius function \(\mu\) takes the value zero on a non-squarefree polynomial and \((-1)^r\) on a squarefree polynomial with \(r\) distinct monic irreducible factors.

For \(s,t\in\{-1,0,1\}\), let
\[
N_{s,t}(h)=\#\{f\in\mathbb F_q[T]:f\text{ monic},\ \deg f=3,\ \mu(f)=s,\ \mu(f+h)=t\}.
\]
The **entire joint Möbius-sign distribution** is independent of \(u\) and \(v\). Its exact entries are
\[
\begin{aligned}
N_{0,0}(h)&=q,\\
N_{0,+1}(h)=N_{0,-1}(h)=N_{+1,0}(h)=N_{-1,0}(h)&=\frac{q(q-1)}2,\\
N_{+1,+1}(h)=N_{-1,-1}(h)&=\frac{q^2(q-2)}4,\\
N_{+1,-1}(h)=N_{-1,+1}(h)&=\frac{q(q^2-2q+2)}4.
\end{aligned}
\]
In particular, the exact two-point Chowla-type correlation is
\[
\boxed{\sum_{\substack{f\text{ monic}\\\deg f=3}}\mu(f)\mu(f+uT+v)=-q.}
\]
Both assertions hold without an asymptotic condition on \(q\), including \(q=2\).

## Assumptions and scope

All finite fields are of characteristic two. A "nonconstant affine shift" means exactly \(\deg h=1\), equivalently \(u\ne0\). No condition is placed on \(v\). The counts range over all \(q^3\) monic cubic polynomials, including nonsquarefree ones. The result is not asserted for constant shifts, polynomials of degree other than three, or fields of odd characteristic.

## Proof

**1. Depressing a cubic and separating its two constant terms.** Write an arbitrary monic cubic uniquely as
\[
f(T)=T^3+aT^2+bT+c,\qquad a,b,c\in\mathbb F_q.
\]
The change of variable \(T=Y+a\) sends this polynomial to
\[
Y^3+BY+C,\qquad B=b+a^2,\quad C=c+ab.
\]
The translated shift \(f+h\) has depressed parameters
\[
B'=B+u,\qquad C'=C+ua+v.
\]
Since \(u\ne0\), the map
\[
(a,b,c)\longmapsto (B,C,C')
\]
is a bijection \(\mathbb F_q^3\to\mathbb F_q^3\): recover \(a=(C+C'+v)/u\), then \(b=B+a^2\) and \(c=C+ab\). Translation of the indeterminate preserves factorization type. Consequently, all joint-sign counts depend only on the nonzero increment \(u\) in the depressed linear coefficient.

**2. Möbius signs of depressed cubics.** Let \(\chi(z)=(-1)^{\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(z)}\) be the nontrivial additive quadratic-phase character. Since the derivative of \(Y^3+BY+C\) is \(Y^2+B\), this polynomial has a repeated root precisely when \(C=0\). The characteristic-two Berlekamp discriminant in the explicit cubic form of Carmon [1, Section 2] is
\[
\operatorname{Berl}(Y^3+BY+C)=1+\frac{B^3}{C^2}\quad (C\ne0).
\]
The characteristic-two analogue of Pellet's formula, also given in [1], therefore yields
\[
\mu(Y^3+BY+C)=-\chi\!\left(1+\frac{B^3}{C^2}\right)
=\varepsilon\chi\!\left(\frac{B^3}{C^2}\right),
\quad \varepsilon=(-1)^{m+1},\qquad C\ne0.
\]
For \(C=0\), the Möbius value is zero.

For \(B\in\mathbb F_q\), define the signed one-parameter sum
\[
S(B)=\sum_{C\in\mathbb F_q}\mu(Y^3+BY+C).
\]
At \(B=0\), every nonzero \(C\) contributes \(\varepsilon\), giving \(S(0)=\varepsilon(q-1)\). At \(B\ne0\), the map \(C\mapsto B^3/C^2\) permutes \(\mathbb F_q^\times\) because squaring is bijective. Hence additive-character orthogonality gives
\[
S(B)=\varepsilon\sum_{z\in\mathbb F_q^\times}\chi(z)=-\varepsilon\qquad (B\ne0).
\]
Thus \(\sum_B S(B)=0\), and for every \(u\ne0\), separating \(B=0\), \(B=u\), and the other \(q-2\) values yields
\[
\sum_B S(B)S(B+u)
=2\,\varepsilon(q-1)(-\varepsilon)+(q-2)\varepsilon^2=-q.
\]

**3. The full joint table.** Put \(A_B(s)=\#\{C\in\mathbb F_q:\mu(Y^3+BY+C)=s\}\). Since precisely \(C=0\) is nonsquarefree,
\[
A_B(0)=1,\qquad A_B(s)=\frac{q-1+sS(B)}2\quad(s\in\{-1,1\}).
\]
By the bijection from Step 1,
\[
N_{s,t}(h)=\sum_{B\in\mathbb F_q}A_B(s)A_{B+u}(t).
\]
For nonzero \(s,t\), expanding the product and using \(\sum_B S(B)=0\) gives
\[
N_{s,t}(h)=\frac{q(q-1)^2+st\sum_B S(B)S(B+u)}4
=\frac{q((q-1)^2-st)}4.
\]
This is \(q^2(q-2)/4\) when \(s=t\), and \(q(q^2-2q+2)/4\) when \(s=-t\). If one sign is zero, summing \(A_B(\pm1)\) over \(B\) gives \(q(q-1)/2\). If both are zero the sum has exactly \(q\) contributions. This proves all nine entries. Multiplying the signs and summing the four nonzero-sign entries gives \(-q\), as asserted. The formulas are integers for every even \(q\); at \(q=2\), the same-sign squarefree entries are zero and all other counts remain valid.

## Verification

Run `python3 verify.py` in the directory containing the attached standalone standard-library script. It constructs polynomial-basis representations of \(\mathbb F_{2^m}\) for \(1\le m\le6\), determines each cubic's Möbius sign by directly counting rational roots and checking the derivative for repeated roots, and enumerates the joint signs under nonconstant affine shifts. This approach does not use the Berlekamp discriminant or the character-sum derivation of the proof.

All nonzero linear coefficients and all constants are checked for fields of size at most \(16\); selected nonzero coefficients and constants are checked over fields of size \(32\) and \(64\). The observed result was `VERIFY_OK degrees=6 shifts=352 cubic_pairs=3765008`. These finite tests corroborate the exact proof but do not prove its universal quantifier.

## Relationship to prior work

Carmon's 2014 article [1] provides the characteristic-two Möbius/Berlekamp identity and proves a broad upper bound for multi-shift autocorrelations (Theorem 1.1). The full text gives the cubic Berlekamp formula used here but does not state the nine-entry exact joint distribution or the uniform value \(-q\) for all nonconstant affine shifts. Those statements require the separate coefficient-coordinate bijection and exact character-orthogonality computation above; they do not follow as numerical equalities from Carmon's upper bound. Carmon and Rudnick's 2012 predecessor [2] treats odd characteristic. Sawin and Shusterman [3] study broader Chowla correlations; their publisher abstract does not establish this exact fixed-degree table, but their full manuscript was not inspected and no whole-document exclusion is asserted. An existing exact joint-squarefree count for nonconstant affine shifts already gives the unsigned total \(q(q-1)^2\); that count is not claimed as new. The new assertion is the sign-resolved nine-entry table, including its \(-q\) signed correlation. Constant-shift correlations are a distinct regime because the coefficient bijection here requires \(u\ne0\).

## Limitations

This theorem treats only monic cubics, characteristic two, and nonconstant affine shifts. The Berlekamp/Pellet identity employed in the proof is published prior work, not independently reproved here. The direct computational tests cover six finite-field sizes and are not an infinite certificate. Equivalent coverage in less readily searchable literature cannot be ruled out; no independent mathematical audit is claimed.

## References

1. D. Carmon, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field in characteristic 2*, arXiv:1409.3694v1, first posted 2014-09-12; especially Section 2 (cubic Berlekamp discriminant and characteristic-two Pellet identity), Theorem 1.1, and Section 7. https://arxiv.org/html/1409.3694v1
2. D. Carmon and Z. Rudnick, *The autocorrelation of the Mobius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599, first posted 2012-05-08. https://arxiv.org/abs/1205.1599
3. W. Sawin and M. Shusterman, *On the Chowla and twin primes conjectures over* \(\mathbb F_q[T]\), *Annals of Mathematics* 196 (2022), 457–506. https://doi.org/10.4007/annals.2022.196.2.1
