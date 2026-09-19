# A 0.553 lower bound for four-color rainbow Schur triples

Let \(c:[n]\to[4]\) be a coloring and
\[
R_n(c)=\{(x,y)\in[n]^2:x+y\le n,\ c(x),c(y),c(x+y)\ \text{are pairwise distinct}\}.
\]
Following Hegde--Kumar--Pratibha, write
\[
\Lambda_{n,4}=\binom n2^{-1}\max_c |R_n(c)|.
\]

## Result

There is an explicit sequence of four-colorings for which
\[
\frac{|R_n(c_n)|}{\binom n2}\longrightarrow \frac{553}{1000}.
\]
Consequently,
\[
\boxed{\liminf_{n\to\infty}\Lambda_{n,4}\ge \frac{553}{1000}=0.553.}
\]

Combined with the general upper bound of Hegde--Kumar--Pratibha,
\[
\frac{553}{1000}\le \liminf_{n\to\infty}\Lambda_{n,4}
\le \limsup_{n\to\infty}\Lambda_{n,4}\le \frac34.
\]

Their general lower bound gives \(10/21\approx0.476190\) when \(k=4\). Thus the construction improves the currently stated lower bound by
\[
\frac{553}{1000}-\frac{10}{21}=\frac{1613}{21000}\approx0.07681.
\]

## Construction

Put
\[
(\beta_0,\ldots,\beta_{10})
=
\frac1{100}(0,23,30,40,50,59,62,75,85,96,100)
\]
and use the color word
\[
(1,2,3,4,2,4,3,2,4,3).
\]
For \(0\le j\le 8\), color \(m\in[n]\) with the \(j\)-th color when
\[
\beta_j\le \frac mn<\beta_{j+1},
\]
and use the last color on \(\beta_9\le m/n\le1\).
Changing conventions at the finitely many interval endpoints affects only \(O(n)\) ordered Schur pairs and hence does not affect the limiting density.

## Exact area calculation

Let \(I=[a,b)\), \(J=[c,d)\), and define
\[
\Phi_t(I,J)
=
\frac12\left[
(t-a-c)_+^2-(t-b-c)_+^2-(t-a-d)_+^2+(t-b-d)_+^2
\right],
\]
where \(u_+=\max(u,0)\).
This is the area of
\[
\{(x,y)\in I\times J:x+y\le t\}.
\]

Let \(I_j=[\beta_j,\beta_{j+1})\), with the harmless endpoint convention at \(1\).
If \(A\) denotes the area in
\[
\mathcal T=\{(x,y)\in[0,1]^2:x+y\le1\}
\]
on which the colors of \(x,y,x+y\) are pairwise distinct, then
\[
A=
\sum_{\substack{0\le i,j,k\le9\\
\operatorname{col}(i),\operatorname{col}(j),\operatorname{col}(k)
\text{ pairwise distinct}}}
\left(\Phi_{\beta_{k+1}}(I_i,I_j)-\Phi_{\beta_k}(I_i,I_j)\right).
\]

Because all breakpoints have denominator \(100\), this sum is an exact rational calculation.
Grouping by the interval containing \(x+y\), the ten contributions to \(10^4(2A)\) are
\[
0,\ 0,\ 280,\ 648,\ 648,\ 220,\ 1086,\ 922,\ 1272,\ 454.
\]
They sum to \(5530\), so
\[
2A=\frac{5530}{10000}=\frac{553}{1000}.
\]

For the finite colorings above, the normalized lattice-point count is a Riemann sum for this piecewise-constant indicator. Its discontinuity set is contained in finitely many lines
\[
x=\beta_i,\qquad y=\beta_j,\qquad x+y=\beta_k,
\]
and has area zero. Hence
\[
\frac{|R_n(c_n)|}{n^2}\to A.
\]
Since
\[
\frac{\binom n2}{n^2}\to\frac12,
\]
we obtain
\[
\frac{|R_n(c_n)|}{\binom n2}\to2A=\frac{553}{1000}.
\]

## Reproducibility

`artifacts/verify.py` performs the area computation with exact rational/integer arithmetic and independently brute-counts the corresponding finite colorings at several values of \(n\).
The stored output is in `artifacts/verification_output.txt`.

The finite checks are supporting evidence only; the lower bound follows from the exact area calculation and the Riemann-sum argument.

## Context and originality

Hegde, Kumar and Pratibha, *A somewhat sure note on an un-Schur problem* (arXiv:2609.18474v1, 16 September 2026), prove for fixed \(k\ge3\)
\[
\frac{(k-2)(k+1)}{(k-1)(k+3)}
\le
\liminf_{n\to\infty}\Lambda_{n,k}
\le
\limsup_{n\to\infty}\Lambda_{n,k}
\le1-\frac1k.
\]
They state that these are, to the best of their knowledge, the first nontrivial bounds for \(k\ge4\), say that the bounds are likely not optimal, and specifically identify \(k=4\) as worth further investigation.

The earlier paper of Parczyk and Spiegel introduced the multiplicity problem for rainbow Schur triples and treated the three-color case. Searches for four-color rainbow-Schur multiplicity bounds, interval constructions, the exact density \(553/1000\), and synonymous anti-Ramsey formulations did not identify this construction or a stronger four-color lower bound.

Originality is therefore asserted only to the best of our knowledge. The motivating preprint is very recent, so unindexed contemporaneous work remains the main residual literature risk.

## Limitations

This result is only a lower bound. It does not improve the currently available upper bound \(3/4\), prove that \(\Lambda_{n,4}\) has a limit, or determine the optimal four-color density. No claim is made that the displayed interval coloring is unique or locally optimal, and no new bound for \(k\ge5\) is asserted.

## References

1. S. Hegde, H. Kumar, Pratibha, *A somewhat sure note on an un-Schur problem*, arXiv:2609.18474v1 (2026). https://arxiv.org/abs/2609.18474
2. O. Parczyk, C. Spiegel, *An Unsure Note on an Un-Schur Problem*, Electron. J. Combin. 33(1) (2026), #P1.45. https://doi.org/10.37236/13554
