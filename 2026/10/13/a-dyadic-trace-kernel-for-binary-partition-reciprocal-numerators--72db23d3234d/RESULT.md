# A dyadic trace kernel for binary partition reciprocal numerators modulo four

## Finding
For an integer \(n\ge 0\), let \(\mathcal B(n)\) denote the partitions of \(n\) into powers of two, and write \(B(n)=|\mathcal B(n)|\). With \(m_\lambda(2^k)\) the multiplicity of \(2^k\), define the **binary reciprocal subsum numerator**
\[
H_n(x)=\sum_{\lambda\in\mathcal B(n)}\prod_{k\ge0}(1+x^{2^k})^{\lfloor n/2^k\rfloor-m_\lambda(2^k)}\in\mathbb Z[x].
\]
This is the reduced numerator \(\operatorname{num}_B(n,x)\), since its common polynomial divisor is one (as established in the references). The following describes *all* its coefficients modulo four, not merely selected low-degree coefficients.

**Theorem.** For every integer \(n\ge2\), let \(e=2\lfloor n/2\rfloor\), \(t=\nu_2(e)\ge1\), and
\[
d=d(n)=\sum_{k\ge1}2^k\left\lfloor\frac{n}{2^k}\right\rfloor,\qquad
c=\frac{B(e)}2\pmod2\in\mathbb F_2.
\]
In \(\mathbb F_2[x]\) define the **dyadic trace kernel**
\[
Q_{t,c}(x)=c(1+x)^{2^t}+\sum_{j=0}^{t-1}x^{2^j}(1+x)^{2^t-2^{j+1}}.
\]
Then \(d\ge2^t\), and the following coefficientwise congruence holds in \(\mathbb Z[x]\):
\[
\boxed{H_n(x)\equiv2(1+x)^{d-2^t}Q_{t,c}(x)\pmod4.}
\]
The right-hand side uses any integral lift of \(Q_{t,c}\), because it is multiplied by two. In particular, \(H_n(x)\) has even coefficients, and \(H_n(x)/2\) is an integer polynomial with the *exact* factorization
\[
\frac{H_n(x)}2\equiv(1+x)^{d-2^t}Q_{t,c}(x)\pmod2,\qquad Q_{t,c}(1)=1.
\]
Thus the exact multiplicity of \(x+1\) in this reduction is \(d-2^t\). When \(n\equiv2\) or \(3\pmod4\), one has \(c=1\) and \(t=1\), giving the especially sparse universal formula
\[
\boxed{H_n(x)\equiv2(1+x)^{d-2}(1+x+x^2)\pmod4.}
\]
For every \(n\ge2\), the coefficient of \(x\) in \(H_n\) is \(2\pmod4\); hence the integer coefficient content of \(H_n\) is exactly two.

## Assumptions and scope
The statement concerns every \(n\ge2\), with no asymptotic or primality hypotheses. Congruences of polynomials mean coefficientwise congruences. The exact root multiplicity is over the field \(\mathbb F_2\), **not** a claim about a root of the characteristic-zero numerator. The quantity \(B(e)/2\) is integral because \(B(e)\) is even for \(e\ge2\).

## Proof
Write \(u=1+x\), \(a_k=\lfloor n/2^k\rfloor\), and \(m_k=m_\lambda(2^k)\). The binary partition identity \(\sum_k2^km_k=n\) shows that every summand in \(H_n\) has the same degree \(d=\sum_{k\ge0}2^ka_k-n\). We work briefly in the ring \((\mathbb Z/4\mathbb Z)[[x]]\), where \(u\) is a unit; the resulting equality will be between polynomials.

**Step 1: a uniform first dyadic correction.** Induction by squaring gives, for each \(k\ge1\),
\[
(1+x)^{2^k}\equiv1+x^{2^k}+2x^{2^{k-1}}\pmod4.
\]
Consequently, with \(a_k-m_k\ge0\),
\[
(1+x^{2^k})^{a_k-m_k}\equiv u^{2^k(a_k-m_k)}
\left(1+2(a_k-m_k)x^{2^{k-1}}u^{-2^k}\right)\pmod4.
\]
The factor for \(k=0\) is exactly \(u^{a_0-m_0}\). Products of two first-order corrections vanish modulo four. Summing over all binary partitions therefore yields
\[
H_n(x)\equiv u^d\left(B(n)+2\sum_{k\ge1}\bigl(a_kB(n)-C_k(n)\bigr)x^{2^{k-1}}u^{-2^k}\right)\pmod4,
\]
where \(C_k(n)=\sum_{\lambda\in\mathcal B(n)}m_\lambda(2^k)\). The minus sign is irrelevant in the coefficient of two.

**Step 2: parity of multiplicity sums.** Let \(\mathcal B(z)=\sum_{n\ge0}B(n)z^n=\prod_{j\ge0}(1-z^{2^j})^{-1}\). Removing or adjoining a part of size one gives \(B(2m+1)=B(2m)\); splitting even partitions according to whether they contain ones gives \(B(2m)=\sum_{j=0}^mB(j)\). These identities prove by induction that \(B(0)=B(1)=1\) and \(B(n)\) is even for all \(n\ge2\). Hence \(\mathcal B(z)\equiv1+z\pmod2\).

Marking occurrences of a part of size \(2^k\) gives the exact generating function
\[
\sum_{n\ge0}C_k(n)z^n=\frac{z^{2^k}}{1-z^{2^k}}\,\mathcal B(z).
\]
Therefore \(C_k(n)\equiv1\pmod2\), for even \(n\), exactly when \(2^k\mid n\); otherwise it is even. For even \(n\ge2\), the term \(a_kB(n)\) vanishes modulo two, so division of the displayed congruence by two gives
\[
\frac{H_n(x)}2\equiv u^d\left(\frac{B(n)}2+\sum_{k=1}^{\nu_2(n)}x^{2^{k-1}}u^{-2^k}\right)\pmod2.
\]
This is a polynomial identity since \(d\ge2^{\nu_2(n)}\). Extracting \(u^{d-2^t}\) proves the asserted kernel formula for even \(n\).

**Step 3: odd indices.** The bijection adding a part of size one sends \(\mathcal B(2m)\) to \(\mathcal B(2m+1)\). All exponents \(a_k-m_k\) are unchanged, because \(\lfloor(2m+1)/2^k\rfloor=\lfloor2m/2^k\rfloor\) for \(k\ge1\), while \(a_0\) and \(m_0\) each increase by one. Thus \(H_{2m+1}(x)=H_{2m}(x)\) and \(d(2m+1)=d(2m)\), establishing the theorem for odd indices as well.

**Step 4: the sharp root order and sparse case.** At \(x=1\) in characteristic two, all terms in \(Q_{t,c}\) vanish except the term \(j=t-1\), which equals one. Hence \(Q_{t,c}(1)=1\) and the \(x+1\) multiplicity is exactly \(d-2^t\). If \(e\equiv2\pmod4\), write \(e=2(2h+1)\). The identity \(B(e)=\sum_{j=0}^{2h+1}B(j)\), paired as \(B(0)+B(1)\) and \(B(2j)+B(2j+1)\), gives \(B(e)\equiv2\pmod4\), so \(c=1\) and \(Q_{1,1}(x)=1+x+x^2\). Finally, the \(x\) coefficient of the full binary congruence is \(2\pmod4\): the \(j=0\) kernel term contributes one, while all other terms and the even-degree power of \(1+x\) have zero linear coefficient in characteristic two. Since all coefficients are even, their greatest common divisor is exactly two.

The sum in the kernel can equivalently be regarded as the finite characteristic-two trace \(\sum_{j=0}^{t-1}w^{2^j}\), with \(w=x/(1+x)^2\), multiplied by \((1+x)^{2^t}\). This explains its dyadic form.

## Verification
The self-contained accompanying \(verify.py\) constructs \(H_n\) from exact integer-polynomial binary-partition sums and separately reconstructs the claimed characteristic-two kernel. It tests equality coefficient-by-coefficient for all \(2\le n\le100\), with selected degree and multiplicity diagnostics. These finite tests support the algebraic argument; they are **not** the reason the identity is asserted for arbitrarily large \(n\).

## Relationship to prior work
Ballantine, Beck, Feigon and Maurischat introduced the reciprocals of subsum polynomials and their binary restriction. Their Section 4 includes the binary numerator/denominator, the even/odd pairing, isolated linear and quadratic coefficient identities (notably Proposition 4.6), and a full characteristic-zero recurrence (Theorem 4.7). The present theorem extracts an explicit **closed coefficientwise modulo-four reduction** and a universal high-multiplicity \(x+1\) root in characteristic two; neither exact formula is stated there. Chen, Ono and Zhang subsequently proved binary coprimality and discussed open shape conjectures, but did not give this dyadic trace reduction. The previously published recurrence determines the coefficients algorithmically, and may afford a different derivation of the present formula; the present contribution is its explicit modular structure, not a new exact recurrence.

## Limitations
The root order is a characteristic-two statement about \(H_n/2\), not a complex factorization or an irreducibility claim. The reduction modulo four does not resolve the conjectured unimodality or log-concavity of the binary numerator. Although targeted comparisons found no equivalent explicit dyadic trace theorem, coverage by an unindexed formulation remains possible.

## References
1. C. Ballantine, G. Beck, B. Feigon and K. Maurischat, *Reciprocals of Subsum Polynomials*, arXiv:2605.10512 (first posted May 11, 2026), especially Section 4 and Theorem 4.7.
2. E. Chen, K. Ono and J. Zhang, *Reciprocals of Partition Polynomials*, arXiv:2605.21718 (first posted May 20, 2026), especially Sections 1 and 4.
