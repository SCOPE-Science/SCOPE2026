# An all-exponent Hardy--Dirichlet gap in Baernstein's quasi-norm comparison

## Finding

Let \(p\) be a degree-\(n\) polynomial with **simple** zeros on the unit circle, and put \(Q_n(z)=1+z^n\). Up to rotation of the argument and nonzero scalar multiplication, write
\[
p(z)=1+a_1z+\cdots+a_{n-1}z^{n-1}+z^n.
\]
For \(r>0\), set \(M_f(r)=\int_{\mathbb T}|f|^r\,dm\), with normalized Haar measure \(m\), and
\[
F_p(r)=\log\bigl(\|p\|_r/\|Q_n\|_r\bigr).
\]
The polar factor \(q=p-zp'/n\) is zero-free on the closed disk. Hence the analytic branch \(q^{r/2}\) normalized by its constant term \(1\) has Taylor series
\[
q(z)^{r/2}=\sum_{k=0}^{\infty}c_k(r)z^k.
\]
**For every positive exponent, including \(r>2\),** one has the explicit weighted Hardy--Dirichlet derivative bound
\[
\boxed{\frac{M_p(r)}{M_{Q_n}(r)}F_p'(r)
\ge \frac{2}{n r^2(r+2)}\sum_{k\ge1}\frac{k}{2k+1}|c_k(r)|^2.}\tag{1}
\]
If \(n\ge2\), \(p\ne 1+z^n\), and \(m_0=\min\{1\le j\le n-1:a_j\ne0\}\), this yields a coefficient-visible inequality valid, in particular, over the **previously untreated range \(r>2\)**:
\[
\boxed{\frac{M_p(r)}{M_{Q_n}(r)}F_p'(r)
\ge \frac{m_0(n-m_0)^2}{2n^3(2m_0+1)(r+2)}|a_{m_0}|^2>0.}\tag{2}
\]
The proof of (1)--(2) in fact works for every \(r>0\), but the separate published result *Strict Baernstein monotonicity and quantitative binomial rigidity* already provides strictness at every exponent and a sharper first-coefficient estimate on \(0<r\le2\). **The new quantitative range claimed here is \(r>2\)**; global equality rigidity is background, not a new contribution.

## Proof

The argument uses only the fully specified analytic identities in Teng Zhang's *Baernstein's Quasi-Norm Monotonicity Conjecture for Polynomials with Unimodular Zeros*, arXiv:2610.02009v1. Its Lemma 2.1 gives the normalization above. Proposition 2.2 proves that, when all unit-circle roots are simple, \(q\) has no zeros in \(\overline{\mathbb D}\) and \(B=q^*/q\) is a finite Blaschke product with \(B(0)=0\). Schwarz's lemma therefore gives \(|B(z)|\le|z|\).

Write \(a=r/2\) and \(g=q^a\). The source's Proposition 3.4 gives
\[
\mathcal P_{2a}(q,B)=\frac{M_{Q_n}(2a)}{an}
\int_{\mathbb D}\operatorname{Re}H_a(B(z))|g'(z)|^2\,dA(z),
\quad dA=dx\,dy/\pi.
\]
Its Theorem 3.5 gives \(\operatorname{Re}H_a(w)>0\) for \(|w|<1\), and its kernel expansion (equation (4.2)) gives \(\operatorname{Re}H_a(0)=1/(a+1)\). Applying the disk Harnack inequality to this positive harmonic function and then Schwarz's estimate yields
\[
\operatorname{Re}H_a(B(z))
\ge\frac{1}{a+1}\frac{1-|B(z)|}{1+|B(z)|}
\ge\frac{1-|z|}{(a+1)(1+|z|)}
\ge\frac{1-|z|}{2(a+1)}.
\]
Proposition 2.4 writes the difference of the normalized relative entropies as a nonnegative entropy term plus \(r\mathcal P_r(q,B)/M_p(r)\); Lemma 2.3 identifies that difference as \(r^2F_p'(r)\). Thus
\[
F_p'(r)\ge \frac{M_{Q_n}(r)}{M_p(r)}\,
\frac{1}{anr}\frac{1}{2(a+1)}
\int_{\mathbb D}(1-|z|)|g'(z)|^2\,dA(z).
\]
Equivalently, inserting \(a=r/2\) gives the prefactor \(2/[nr^2(r+2)]\) multiplying the weighted area integral. Indeed, directly before substituting \(a\), the prefactor from the identities is \((anr)^{-1}[2(a+1)]^{-1}\), which is \(2/[nr^2(r+2)]\).

With \(g(z)=\sum_{k\ge0}c_k(r)z^k\), orthogonality on circles and nonnegativity allow termwise radial integration:
\[
\int_{\mathbb D}(1-|z|)|g'(z)|^2\,dA(z)
=2\sum_{k\ge1}k^2|c_k(r)|^2
\int_0^1(1-\rho)\rho^{2k-1}\,d\rho
=\sum_{k\ge1}\frac{k}{2k+1}|c_k(r)|^2.
\]
This proves (1). If \(m_0\) is the first nonzero intermediate coefficient, then
\[
q(z)=1+\left(1-\frac{m_0}{n}\right)a_{m_0}z^{m_0}+O(z^{m_0+1}),
\]
so \(c_{m_0}(r)=(r/2)(1-m_0/n)a_{m_0}\). Retaining only the corresponding positive summand in (1) proves (2). For a non-binomial polynomial the right side is strictly positive; the binomial has \(q=1\) and vanishing energy.

## Scope, comparisons and use

The inequality is **not** asserted for multiple unit-circle zeros; the source's clean zero-free polar factor on the closed disk is used. For \(n=1\), every allowed polynomial is binomial and the bound is zero. No optimality of the coefficient is claimed. The quantity in (2) is invariant under the permitted normalizing rotations because \(|a_{m_0}|\) is unchanged. Integrating (2) over any compact \(2<s<t<\infty\) gives a nonzero quantitative lower bound on the normalized log-ratio increment, weighted by the computable positive moment ratio \(M_{Q_n}(r)/M_p(r)\).

Zhang (arXiv:2610.02009v1) already proves nondecreasing comparison and the kernel/entropy identities above. Lei and Zhang (arXiv:2605.03949v2) classify the exponent-two entropy equality cases. The published *Strict Baernstein monotonicity and quantitative binomial rigidity* (2026) already proves \(F_p'(r)>0\) for all allowed unimodular-root polynomials and a sharper coefficient-dependent gap for \(0<r\le2\). No originality is assigned here to either strictness or the all-exponent equality cases. What survives is the explicit Hardy--Dirichlet coercivity estimate (1) and its coefficient form (2) for \(r>2\).

A sample numerical integration for the simple-root polynomial \(p=1+z+z^2+z^3\) at \(r=4\) yields \(F_p'(4)\approx0.0457382662\), while the lower bound from (2), after undoing the moment ratio, is \(0.0005611672\). This is only a sanity check: the infinite-family result follows from the analytical proof above.

## References

1. T. Zhang, *Baernstein's Quasi-Norm Monotonicity Conjecture for Polynomials with Unimodular Zeros*, arXiv:2610.02009v1 (2026), Lemma 2.1, Propositions 2.2, 2.4, 3.4, Theorem 3.5, and equation (4.2).
2. J. Lei and T. Zhang, *Proof of the Agler--McCarthy Entropy Conjecture*, arXiv:2605.03949v2 (2026), Theorem 1.3.
3. *Strict Baernstein monotonicity and quantitative binomial rigidity* (published 2026), all-exponent strictness and coefficient gap for \(0<r\le2\).
