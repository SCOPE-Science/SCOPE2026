# A single Walsh–Hadamard family separates operator cotype for every finite q

Let \(n=2^k\), let \(H=H_n\) be the normalized Walsh–Hadamard matrix, and put
\[
s_n=\sqrt{2\log(2n)},\qquad
\|x\|_{X_n}=\max\left\{\|x\|_\infty,\frac{\|Hx\|_\infty}{s_n}\right\}.
\]
Let \(U_n:X_n\to \ell_\infty^n\) be the identity map. This is the family introduced by Xinglong Wu in arXiv:2609.19731 to disprove Talagrand's operator-cotype inequality at \(q=2\).

## Theorem

There are absolute constants \(c,C>0\) and an absolute \(n_0\) such that, for every dyadic \(n\ge n_0\) and every finite \(q\ge2\),
\[
 C_q^r(U_n)\ge \frac12 n^{1/q},
\]
\[
 C_q^g(U_n)\le C\left(\frac{n}{\log(n+1)}\right)^{1/q},
\]
and
\[
 \|U_n\|_{q,1}
 \le n^{1/(2q)}\bigl(2\log(2n)\bigr)^{1/(2q)}
 \le C\left(\frac{n}{\log(n+1)}\right)^{1/q}.
\]
Consequently,
\[
\boxed{
 C_q^r(U_n)\ge c\,\bigl(\log(n+1)\bigr)^{1/q}
 \max\{C_q^g(U_n),\|U_n\|_{q,1}\}.
}
\]
The constants \(c,C,n_0\) may be chosen independently of \(q\). In particular, for every fixed \(2\le q<\infty\), no dimension-free constant—even one allowed to depend on that fixed \(q\)—can bound \(C_q^r(U)\) by \(\max\{C_q^g(U),\|U\|_{q,1}\}\) for arbitrary Banach-space operators. The same sequence \((X_n,U_n)\) witnesses this simultaneously for all finite \(q\).

## Proof

For the standard basis \((e_i)_{i=1}^n\), Wu's subgaussian estimate gives
\[
 \mathbb E\left\|\sum_{i=1}^n\varepsilon_i e_i\right\|_{X_n}\le2.
\]
Since \(\|U_ne_i\|_\infty=1\), the definition of Rademacher cotype gives, for every \(q\ge2\),
\[
 C_q^r(U_n)\ge \frac{n^{1/q}}2.
\]

For Gaussian cotype, take any finite sequence \((x_i)\subset X_n\), set
\[
 a_i=\|U_nx_i\|_\infty=\|x_i\|_\infty,
 \qquad
 G=\mathbb E\left\|\sum_i g_i x_i\right\|_{X_n}.
\]
Wu's \(q=2\) estimate yields
\[
 \|(a_i)\|_2\le C_2\sqrt{\frac{n}{\log(n+1)}}\,G
\]
with an absolute \(C_2\). On the other hand, for each \(i\), choose a norm-one functional \(x_i^*\in X_n^*\) with \(x_i^*(x_i)=\|x_i\|_{X_n}\). Then
\[
 G\ge
 \mathbb E\left|\sum_j g_jx_i^*(x_j)\right|
 =\sqrt{\frac2\pi}\left(\sum_j|x_i^*(x_j)|^2\right)^{1/2}
 \ge\sqrt{\frac2\pi}\,a_i.
\]
Thus \(\|(a_i)\|_\infty\le\sqrt{\pi/2}\,G\). Interpolating \(\ell_2\) and \(\ell_\infty\),
\[
 \|(a_i)\|_q
 \le \|(a_i)\|_2^{2/q}\|(a_i)\|_\infty^{1-2/q}
 \le C\left(\frac{n}{\log(n+1)}\right)^{1/q}G,
\]
where \(C\) is absolute and uniform for \(q\ge2\). This proves the Gaussian estimate.

For the \((q,1)\)-summing norm, use Wu's notation. For \(A=[x_1\ \cdots\ x_m]=(a_{ji})\), write \(HA=(c_{ji})\) and set
\[
 \alpha=\max_j\sum_i|a_{ji}|,
 \qquad
 \beta=\max_j\sum_i|c_{ji}|,
 \qquad
 D=\max_{\eta_i=\pm1}\left\|\sum_i\eta_i x_i\right\|_{X_n}
   =\max\{\alpha,\beta/s_n\}.
\]
Put \(u_i=\|x_i\|_\infty\). Wu's Hadamard calculation gives
\[
 u_i\le\alpha,
 \qquad
 \sum_i u_i^2\le \sqrt n\,\alpha\beta.
\]
Hence, for every \(q\ge2\),
\[
 \sum_i u_i^q
 \le \alpha^{q-2}\sum_i u_i^2
 \le \sqrt n\,\alpha^{q-1}\beta
 \le \sqrt n\,s_n D^q.
\]
Taking \(q\)-th roots gives
\[
 \left(\sum_i\|U_nx_i\|_\infty^q\right)^{1/q}
 \le n^{1/(2q)}s_n^{1/q}D
 =n^{1/(2q)}(2\log(2n))^{1/(2q)}D.
\]
This is the asserted \((q,1)\)-summing estimate. Finally,
\[
 \frac{n^{1/(2q)}s_n^{1/q}}
 {(n/\log(n+1))^{1/q}}
 =\left(\frac{s_n\log(n+1)}{\sqrt n}\right)^{1/q}\le1
\]
for all sufficiently large \(n\), with the threshold independent of \(q\). Combining the three estimates proves the theorem.

## Context and improvement direction

Talagrand's Research Problem 19.1.2 asks whether a universal bound of the form
\[
 C_q^r(U)\le L\max\{C_q^g(U),\|U\|_{q,1}\}
\]
holds for arbitrary Banach-space operators; the same chapter proves a positive result for operators whose domain is \(\ell_\infty^N\), with a note that a corresponding \(C(K)\) result is also available. Wu's 2026 construction gives a negative answer at \(q=2\), with a \(\sqrt{\log n}\) separation. The theorem above shows that Wu's very same spaces and operators are not a phenomenon confined to the endpoint: for every finite \(q\ge2\) they give a quantitative separation of order at least \((\log n)^{1/q}\).

For \(2<q<\infty\), Marius Junge's comparison theorem gives detailed Gaussian/Rademacher cotype characterizations for operators defined on \(C(K)\). That positive-domain theory does not subsume the present construction, whose domains are the Walsh–Hadamard renormings \(X_n\).

## Limitations and originality status

The result does not address \(q=\infty\), does not assert that \((\log n)^{1/q}\) is the optimal separation for fixed \(q>2\), and does not classify domains on which Talagrand's inequality remains valid. The originality claim is restricted to the simultaneous all-finite-\(q\) extension for Wu's family, to the best of our knowledge. Targeted searches for the source paper, Walsh–Hadamard formulations, Gaussian/Rademacher operator cotype, and \((q,1)\)-summing equivalents located the classical \(C(K)\) theory but no statement of this extension. Older operator-cotype literature is extensive, so an equivalent implication under different terminology remains a residual risk.

## References

1. Xinglong Wu, *A Counterexample to Talagrand's Operator Cotype Problem*, arXiv:2609.19731v1 (2026), https://arxiv.org/abs/2609.19731.
2. Michel Talagrand, *Upper and Lower Bounds for Stochastic Processes: Decomposition Theorems*, 2nd ed. (2021), Research Problem 19.1.2 and Theorem 19.1.5, https://michel.talagrand.net/ULBSPRINGER.pdf.
3. Marius Junge, *Comparing gaussian and Rademacher cotype for operators on the space of continuous functions*, Studia Math. 118 (1996), 101–115; arXiv:math/9302206, https://arxiv.org/abs/math/9302206.
4. Michel Talagrand, *Cotype and (q,1)-summing norm in a Banach space*, Invent. Math. 110 (1992), 545–556, DOI 10.1007/BF01231344.
