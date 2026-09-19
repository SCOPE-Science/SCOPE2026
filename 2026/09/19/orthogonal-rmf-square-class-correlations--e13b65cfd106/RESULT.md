# Universal square-class correlations in orthogonal compact-group random multiplicative functions

## Statement

Let \(G\) be a compact group and let \(V\) be a nontrivial irreducible finite-dimensional unitary representation of \(G\), of dimension \(d\). At each prime \(p\), choose an independent Haar-distributed \(g_p\in G\). If \(\alpha_1(p),\ldots,\alpha_d(p)\) are the eigenvalues of \(g_p\) on \(V\), define the automorphic random multiplicative function \(X_V\) by
\[
X_V(p^k)=h_k(\alpha_1(p),\ldots,\alpha_d(p))
=\chi_{\operatorname{Sym}^k V}(g_p),
\]
and extend multiplicatively. Put
\[
S_V(x)=\sum_{n\le x}X_V(n).
\]
Assume that \(V\) is of orthogonal Frobenius--Schur type, equivalently that it has a nondegenerate \(G\)-invariant symmetric bilinear form.

For \(k,l\ge0\), set
\[
c(k,l)=\mathbb E\!\left[X_V(p^k)\overline{X_V(p^l)}\right].
\]
Then:

1. **Local square-parity correlation.** One always has
\[
c(k,l)=\dim\operatorname{Hom}_G(\operatorname{Sym}^lV,\operatorname{Sym}^kV)\in\mathbb Z_{\ge0}.
\]
If \(d\ge2\) and \(k\equiv l\pmod2\), then
\[
\boxed{\quad c(k,l)\ge \left\lfloor\frac{\min(k,l)}2\right\rfloor+1.\quad}
\]
If \(d=1\), then \(c(k,l)=1\) whenever \(k\equiv l\pmod2\), and \(c(k,l)=0\) otherwise.

2. **Global square-class correlation.** Write two positive integers in their common square class as
\[
m=r u^2,\qquad n=r v^2,
\]
where \(r\) is squarefree. If \(d\ge2\), then
\[
\boxed{\quad
\mathbb E\!\left[X_V(m)\overline{X_V(n)}\right]
\ge \tau(\gcd(u,v)).
\quad}
\]
For \(d=1\), the left side is exactly \(1\) for such a pair.

3. **Universal square bias.** For every \(d\ge1\),
\[
\boxed{\quad \mathbb E S_V(x)\ge \lfloor\sqrt{x}\rfloor.\quad}
\]
For \(d=1\), equality holds.

4. **Second-moment inflation.** If \(d\ge2\), then
\[
\boxed{\quad
\mathbb E|S_V(x)|^2
\ge
\sum_{t\le x}\left\lfloor\sqrt{\frac{x}{t}}\right\rfloor^2
=x\log x+O(x).
\quad}
\]
If \(d=1\), then
\[
\boxed{\quad
\mathbb E|S_V(x)|^2
=\frac{6}{\pi^2}x\log x+O(x).
\quad}
\]

5. **Low-moment obstruction.** For every fixed \(q\in[1/2,1)\),
\[
\boxed{\quad
\mathbb E|S_V(x)|^{2q}\ge x^q(1+o(1)).
\quad}
\]
At \(q=1\), the second-moment bound above gives an additional factor of order \(\log x\) over \(x\).

Consequently the prime-square cancellation hypothesis \(\mathbb E h_2=0\) in Leung's low-moment theorem is not merely violated by isolated orthogonal examples: every nontrivial irreducible orthogonal compact-group model has a square-class correlation mechanism that forces a larger scale. In particular, this applies simultaneously to every even symmetric-power Sato--Tate model
\[
V=\operatorname{Sym}^{2a}(\mathbb C^2),\qquad a\ge1,
\]
whereas the source paper computes the corresponding moment inflation explicitly only for the symmetric-square case.

## Proof

Because \(h_k=\chi_{\operatorname{Sym}^kV}\), character orthogonality gives
\[
c(k,l)=\langle\chi_{\operatorname{Sym}^kV},\chi_{\operatorname{Sym}^lV}\rangle_G
=\dim\operatorname{Hom}_G(\operatorname{Sym}^lV,\operatorname{Sym}^kV).
\]
Thus every local covariance is a nonnegative integer.

Orthogonal Frobenius--Schur type gives a nonzero invariant quadratic tensor
\[
Q\in(\operatorname{Sym}^2V)^G.
\]
Multiplication by \(Q\) in the symmetric algebra is injective:
\[
Q\cdot:\operatorname{Sym}^{j-2}V\hookrightarrow\operatorname{Sym}^jV,
\]
because the symmetric algebra is an integral domain. Compactness of \(G\) gives complete reducibility, so for each \(j\ge2\) one may choose a \(G\)-stable complement \(H_j\) and write
\[
\operatorname{Sym}^jV\cong Q\operatorname{Sym}^{j-2}V\oplus H_j
\cong\operatorname{Sym}^{j-2}V\oplus H_j.
\]
Take \(H_0=\mathbf1\) and \(H_1=V\). Iteration gives
\[
\operatorname{Sym}^jV\cong H_j\oplus H_{j-2}\oplus H_{j-4}\oplus\cdots.
\]
If \(d\ge2\), then every \(H_j\) is nonzero, since
\[
\dim H_j
=\binom{d+j-1}{j}-\binom{d+j-3}{j-2}>0.
\]
Hence if \(k\equiv l\pmod2\), the two symmetric powers contain at least
\[
\left\lfloor\frac{\min(k,l)}2\right\rfloor+1
\]
common nonzero direct summands. Projecting to each such summand in one symmetric power and including it in the other gives that many linearly independent \(G\)-maps. This proves the local lower bound.

When \(d=1\), a nontrivial irreducible orthogonal representation is a quadratic character of \(G\), so \(\operatorname{Sym}^kV=V^{\otimes k}\) depends only on the parity of \(k\), proving the stated exact local covariance.

Now suppose \(m=r u^2\) and \(n=r v^2\) with \(r\) squarefree. At every prime the exponents of \(m\) and \(n\) have the same parity. Write
\[
v_p(m)=\varepsilon_p+2a_p,\qquad
v_p(n)=\varepsilon_p+2b_p,
\qquad \varepsilon_p\in\{0,1\}.
\]
Independence over primes and the local estimate give, for \(d\ge2\),
\[
\mathbb E[X_V(m)\overline{X_V(n)}]
=\prod_p c(v_p(m),v_p(n))
\ge\prod_p(\min(a_p,b_p)+1)
=\tau(\gcd(u,v)).
\]
All covariance terms, including those outside a common square class, are nonnegative, so discarding them can only lower the second moment. Therefore
\[
\begin{aligned}
\mathbb E|S_V(x)|^2
&\ge \sum_{\substack{r\ \mathrm{squarefree}\\ru^2,rv^2\le x}}\tau(\gcd(u,v))\\
&=\sum_{\substack{r\ \mathrm{squarefree}}}\sum_{a\le\sqrt{x/r}}
\left\lfloor\frac{\sqrt{x/r}}a\right\rfloor^2.
\end{aligned}
\]
Every positive integer \(t\) has a unique decomposition \(t=ra^2\) with \(r\) squarefree. Hence the last expression is exactly
\[
\sum_{t\le x}\left\lfloor\sqrt{\frac{x}{t}}\right\rfloor^2.
\]
Since \(\lfloor y\rfloor^2=y^2+O(y)\),
\[
\sum_{t\le x}\left\lfloor\sqrt{\frac{x}{t}}\right\rfloor^2
=x\sum_{t\le x}\frac1t+O\!\left(\sqrt{x}\sum_{t\le x}t^{-1/2}\right)
=x\log x+O(x).
\]
For \(d=1\), covariance is exactly the indicator that the two integers lie in the same square class, so
\[
\mathbb E|S_V(x)|^2
=\sum_{\substack{r\le x\\r\ \mathrm{squarefree}}}
\left\lfloor\sqrt{\frac{x}{r}}\right\rfloor^2
=\frac6{\pi^2}x\log x+O(x),
\]
using the standard estimate \(\sum_{r\le x,\ r\text{ squarefree}}1/r=(6/\pi^2)\log x+O(1)\).

Finally, \(Q^a\) is a nonzero invariant vector in \(\operatorname{Sym}^{2a}V\). Thus
\[
\mathbb E h_{2a}=\dim(\operatorname{Sym}^{2a}V)^G\ge1.
\]
All such expectations are nonnegative integers, so every square \(n\) contributes at least \(1\) to \(\mathbb E X_V(n)\), and no nonsquare contributes negatively. This proves
\[
\mathbb E S_V(x)\ge\lfloor\sqrt{x}\rfloor.
\]
For \(q\ge1/2\), the exponent \(2q\ge1\), so Jensen's inequality yields
\[
\mathbb E|S_V(x)|^{2q}\ge|\mathbb E S_V(x)|^{2q}
\ge\lfloor\sqrt{x}\rfloor^{2q}=x^q(1+o(1)).
\]

## Relation to recent literature

Leung's Theorem 1.1 gives, under the prime-square cancellation condition \(\mathbb E h_2=0\),
\[
\mathbb E|S(x)|^{2q}\asymp_d
\left(\frac{x}{1+(1-q)\sqrt{\log\log x}}\right)^q,
\qquad 0\le q\le1.
\]
For a compact-group model the same paper identifies
\(\mathbb E h_2=1\) exactly in orthogonal Frobenius--Schur type, and Proposition 7.1 computes the symmetric-square Sato--Tate example, obtaining \(x\log x+O(x)\) for the second moment and \(\lfloor\sqrt x\rfloor\) for the mean. The theorem above supplies a uniform representation-theoretic mechanism for the entire orthogonal class. For fixed \(q\in[1/2,1)\), its lower bound exceeds the centered scale by a factor tending to infinity of order at least \((\log\log x)^{q/2}\); at \(q=1\) the second moment exceeds the centered scale by order \(\log x\).

Harper's 2020 low-moment theorem treats the classical Steinhaus and Rademacher random multiplicative functions. It does not state the compact-group orthogonal square-class covariance result above.

## Originality and limitations

Originality is asserted only to the best of our knowledge. The motivating preprint arXiv:2609.20460v1 was submitted on 17 September 2026 and is very recent. Its Section 7 explicitly treats orthogonal type as the failure of prime-square centering and proves an exact result for the symmetric-square Sato--Tate model, but does not state the local Hom-space lower bound, the universal square-class correlation inequality, or the resulting all-orthogonal second-moment lower bound. Searches using orthogonal compact-group random multiplicative functions, Frobenius--Schur type, square-class/squarefree-kernel covariance, and even symmetric-power Sato--Tate formulations did not identify an earlier theorem covering these claims. No inaccessible source with metadata specifically suggesting this universal result was identified; unindexed contemporaneous work remains the main residual originality risk.

The result gives lower bounds, not a full asymptotic for a general orthogonal representation. It does not determine low moments for \(q<1/2\), does not provide matching upper bounds, and does not claim that all orthogonal models have the same moment asymptotics. The classical representation-theoretic facts used in the proof are not claimed as new. No independent validation or formal proof-assistant verification is asserted.

## References

1. Sun-Kai Leung, *Low moments of automorphic random multiplicative function sums*, arXiv:2609.20460v1 (2026), https://arxiv.org/abs/2609.20460.
2. Adam J. Harper, *Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos*, Forum of Mathematics, Pi 8 (2020), e1, https://doi.org/10.1017/fmp.2019.7.
