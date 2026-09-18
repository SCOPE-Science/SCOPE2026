# A sharper density profile for oscillating sumsets

## Statement

For a set \(A\subseteq\mathbb N\), write \(d(A)\) for its asymptotic density when it exists, and \(d_*(A)\), \(d^*(A)\) for lower and upper asymptotic density. Paolo Leonetti proved that for every integer \(r\ge2\) and every \(\delta\in(0,1/4)\) there is a set \(A\) with
\[
d(A)=\delta^r,\qquad d^*(A+A)=1,
\]
and
\[
d_*(A+A)\le (r+1)(2\delta)^{r-1}.
\]
The same construction in fact gives the strictly sharper bound
\[
\boxed{
 d_*(A+A)\le r(2\delta)^{r-1}-(r-1)(2\delta)^r.
}
\tag{1}
\]

Define the extremal profile
\[
\Lambda(\alpha)=\inf\{d_*(A+A):d(A)=\alpha,\ d^*(A+A)=1\}.
\]
For every integer \(r\ge2\) satisfying \(\alpha^{1/r}<1/4\), (1) gives
\[
\boxed{
\Lambda(\alpha)
\le
2^{r-1}\alpha^{1-1/r}
\bigl(r-2(r-1)\alpha^{1/r}\bigr).
}
\tag{2}
\]
Consequently, if \(L=\log(1/\alpha)\), then as \(\alpha\to0^+\),
\[
\boxed{
\Lambda(\alpha)
\le
(1+o(1))\,
\frac{\sqrt L}{2\sqrt{\log2}}
\exp\!\bigl(2\sqrt{L\log2}\bigr)\,\alpha.
}
\tag{3}
\]
On the other hand, Kneser's theorem gives \(d_*(A+A)\ge\min\{2d(A),d^*(A+A)\}\); hence for \(0<\alpha<1/2\),
\[
\Lambda(\alpha)\ge2\alpha.
\tag{4}
\]
Thus
\[
\boxed{
\frac{\log \Lambda(\alpha)}{\log\alpha}\longrightarrow1
\qquad(\alpha\to0^+).
}
\tag{5}
\]
In particular, among sets of natural density \(\alpha\) whose double sumset has upper density one, the least possible lower density of the double sumset has exact logarithmic exponent one. The result does not determine \(\Lambda(\alpha)/\alpha\).

## Proof of the refined fixed-parameter bound

We retain the notation from the proof of Leonetti's Theorem 1.2. At the endpoint \(x_{m+1}\), the construction writes
\[
A\cap[0,x_{m+1})=F_m\cup G_m,
\]
with
\[
\frac{|F_m+F_m|}{x_{m+1}}\le2\varepsilon_{m+1}.
\tag{6}
\]
For pairwise distinct primes \(q_{m,1},\dots,q_{m,r}\), put
\[
D_{m,i}=\{0,1,\dots,2\lfloor\delta q_{m,i}\rfloor\},
\qquad
\eta_{m,i}=\frac{|D_{m,i}|}{q_{m,i}}.
\]
Then \(\eta_{m,i}\to2\delta\) for each \(i\), because \(q_{m,i}>r/\varepsilon_m\) and \(\varepsilon_m\to0\).

Define the periodic sets
\[
\Gamma_m=\bigcap_{i=1}^r(q_{m,i}\mathbb N+D_{m,i})
\]
and, for \(j=0,\dots,r-1\),
\[
\Gamma_{m,j}
=
\bigcap_{\substack{1\le i\le r\\ i\ne j+1}}
(q_{m,i}\mathbb N+D_{m,i}).
\]
Leonetti's proof establishes
\[
G_m+G_m\subseteq\Gamma_m,
\qquad
F_m+G_m\subseteq\Gamma_m\cup\bigcup_{j=0}^{r-1}\Gamma_{m,j}.
\tag{7}
\]
But \(\Gamma_m\subseteq\Gamma_{m,j}\) for every \(j\). Hence, setting
\[
U_m=\bigcup_{j=0}^{r-1}\Gamma_{m,j},
\]
(7) reduces to
\[
(G_m+G_m)\cup(F_m+G_m)\subseteq U_m.
\tag{8}
\]

Let \(Q_m=\prod_i q_{m,i}\). By the Chinese remainder theorem, a residue modulo \(Q_m\) lies in \(U_m\) exactly when at least \(r-1\) of its \(r\) coordinates lie in their respective sets \(D_{m,i}\). Thus one period contains exactly
\[
\prod_{i=1}^r|D_{m,i}|
+
\sum_{j=1}^r
(q_{m,j}-|D_{m,j}|)
\prod_{i\ne j}|D_{m,i}|
\tag{9}
\]
residues of \(U_m\). Dividing by \(Q_m\), its exact periodic density is
\[
u_m=
\prod_{i=1}^r\eta_{m,i}
+
\sum_{j=1}^r(1-\eta_{m,j})
\prod_{i\ne j}\eta_{m,i}.
\tag{10}
\]
For an initial interval of length \(x_{m+1}\), one incomplete period contributes an error of at most \(Q_m/x_{m+1}\), and the original construction has
\[
\frac{Q_m}{x_{m+1}}\le\varepsilon_m\varepsilon_{m+1}.
\tag{11}
\]
Combining (6), (8), (10), and (11),
\[
\frac{|(A+A)\cap[0,x_{m+1})|}{x_{m+1}}
\le
2\varepsilon_{m+1}+u_m+\varepsilon_m\varepsilon_{m+1}.
\]
Taking \(m\to\infty\) gives
\[
\begin{aligned}
d_*(A+A)
&\le (2\delta)^r+r(1-2\delta)(2\delta)^{r-1}\\
&=r(2\delta)^{r-1}-(r-1)(2\delta)^r,
\end{aligned}
\]
which proves (1). The density and upper-density conclusions are unchanged from Leonetti's construction.

## Optimization as the source density tends to zero

Set \(a=\log2\) and \(L=\log(1/\alpha)\). Substituting \(\delta=\alpha^{1/r}=e^{-L/r}\) into (2) yields
\[
\frac{\Lambda(\alpha)}{\alpha}
\le
2^{r-1}e^{L/r}
\bigl(r-2(r-1)e^{-L/r}\bigr).
\tag{12}
\]
For large \(L\), choose \(r\) to be the nearest integer to
\[
\rho(L)=\frac{\sqrt{1+4aL}-1}{2a}.
\tag{13}
\]
Then \(r\sim\sqrt{L/a}\), so \(L/r\to\infty\) and the admissibility condition \(e^{-L/r}<1/4\) holds. The logarithm of the right-hand side of (12) is
\[
(r-1)a+\frac Lr+\log r+o(1).
\tag{14}
\]
The continuous function \(ar+L/r+\log r\) is stationary at \(r=\rho(L)\), since
\[
a-\frac{L}{r^2}+\frac1r=0
\quad\Longleftrightarrow\quad
ar^2+r-L=0.
\]
Rounding \(\rho(L)\) to the nearest integer changes (14) by \(o(1)\), because the second derivative there is \(O(L^{-1/2})\). At \(r=\rho(L)\),
\[
a\rho+\frac L\rho=\sqrt{1+4aL}.
\]
Therefore
\[
\log\frac{\Lambda(\alpha)}{\alpha}
\le
2\sqrt{aL}+\frac12\log\frac La-a+o(1),
\]
which exponentiates to (3).

Finally, (4) and (3) give
\[
-L+O(1)\le\log\Lambda(\alpha)\le-L+O(\sqrt L),
\]
and (5) follows.

## Verification

`artifacts/verify_profile.py` checks two parts that are useful for detecting bookkeeping mistakes:

1. an explicit CRT example in which the union of the \(r\) one-coordinate-deleted constraint sets is counted both by exhaustive residues and by (9);
2. numerical optimization of (12), compared with the asymptotic logarithm
\[
2\sqrt{L\log2}+\frac12\log\frac{L}{\log2}-\log2.
\]

The recorded output is in `artifacts/verify-output.txt`. These computations support the algebra but are not substitutes for the proof above.

## Context and limitations

The main input is Paolo Leonetti, *On a question of Ruzsa about densities of sumsets*, arXiv:2609.20206. Its Theorem 1.2 gives the bound \((r+1)(2\delta)^{r-1}\); the refinement above comes from counting the already-present CRT union exactly instead of bounding its \(r+1\) pieces separately.

Pierre-Yves Bienvenu, *Realisability of simultaneous density constraints for sets of integers*, arXiv:2502.09438 (published in J. Number Theory 281 (2026), 596--614), studies the full quadruple of lower/upper densities of \(A\) and \(2A\), including three-dimensional projections, but the inspected results do not supply the small-\(\alpha\) profile (3)--(5).

Norbert Hegyvári, François Hennecart, and Péter Pál Pach, *On the density of sumsets and product sets*, arXiv:1902.02512, is the source of the Ruzsa question to which Leonetti responds.

Originality is asserted only to the best of our knowledge. The motivating preprint is very recent, so unindexed contemporaneous refinements remain possible. Leonetti cites an unpublished manuscript of I. Z. Ruzsa concerning the same question; no public identifier or full text was located. Leonetti reports only that this manuscript proved the necessary restriction \(\nu\ge1/2\) under a hypothetical positive answer to Ruzsa's question. Since its full contents were not inspected, it remains the main inaccessible-source risk. No claim is made that (3) is the true asymptotic order of \(\Lambda(\alpha)\); the factor between the lower bound \(2\alpha\) and the upper envelope in (3) remains open.

## References

- P. Leonetti, *On a question of Ruzsa about densities of sumsets*, arXiv:2609.20206, https://arxiv.org/abs/2609.20206.
- P.-Y. Bienvenu, *Realisability of simultaneous density constraints for sets of integers*, arXiv:2502.09438, https://arxiv.org/abs/2502.09438.
- N. Hegyvári, F. Hennecart, P. P. Pach, *On the density of sumsets and product sets*, arXiv:1902.02512, https://arxiv.org/abs/1902.02512.
- M. Kneser, *Abschätzung der asymptotischen Dichte von Summenmengen*, Math. Z. 58 (1953), 459--484.
