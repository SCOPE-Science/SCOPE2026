# Eventual strict growth of sixfold evil and odious representation counts

## Finding

For \(m\geq0\), write \(s_2(m)\) for the number of ones in its binary expansion. Put \(E=\{m\geq0:s_2(m)\equiv0\pmod2\}\) and \(O=\{m\geq0:s_2(m)\equiv1\pmod2\}\). Let \(r_6(n)\), respectively \(s_6(n)\), count **ordered** six-tuples of elements of \(E\), respectively \(O\), summing to \(n\). Then both counts are eventually strictly increasing. More precisely, with \(\beta=\log_2 15<4\), as \(n\to\infty\), **independently for either count**,

\[
r_6(n)-r_6(n-1)=\frac1{64}\binom{n+4}{4}+O(n^\beta),\qquad
s_6(n)-s_6(n-1)=\frac1{64}\binom{n+4}{4}+O(n^\beta).
\]

Thus the eventual-monotonicity part of Conjecture 12(a) of Allouche and Shallit holds. No explicit threshold or assertion that their proposed sharp thresholds are correct is made.

## Assumptions and scope

The integers and summands are **nonnegative**, and each tuple is ordered; repetition is allowed. Coefficients are ordinary generating-function coefficients over \(\mathbb Z\). The asymptotics and implied constants are absolute, with \(n\ge1\). The sign convention is \(t_m=(-1)^{s_2(m)}\), so \(t_0=1\) and \(E\) includes zero. The two error terms need not be equal.

## Proof

**Sixth-moment lemma.** Define the truncated Thue–Morse polynomial
\[
T_h(z)=\sum_{j=0}^{2^h-1}t_jz^j=\prod_{i=0}^{h-1}(1-z^{2^i}),\quad h\ge0.
\]
There is an absolute constant \(C\) such that
\[
\frac1{2\pi}\int_0^{2\pi}|T_h(e^{i\theta})|^6\,d\theta\le C15^h.
\]
Indeed, on the unit circle,
\[
P(z)=|1-z|^6=20-15(z+z^{-1})+6(z^2+z^{-2})-(z^3+z^{-3}).
\]
Let \(L_h(z)=\prod_{i=0}^{h-1}P(z^{2^i})=\sum_{k\in\mathbb Z}c_h(k)z^k\), and put \(a_h=c_h(0)\), \(b_h=c_h(1)\), \(d_h=c_h(2)\). Since \(L_h(z)=L_h(z^{-1})\) and \(L_{h+1}(z)=P(z)L_h(z^2)\), direct coefficient comparison yields
\[
\begin{pmatrix}a_{h+1}\\b_{h+1}\\d_{h+1}\end{pmatrix}=
\begin{pmatrix}20&12&0\\-15&-16&-1\\6&20&6\end{pmatrix}
\begin{pmatrix}a_h\\b_h\\d_h\end{pmatrix},\quad
(a_0,b_0,d_0)=(1,0,0).
\]
The characteristic polynomial of the displayed matrix is \(f(X)=X^3-10X^2-96X+512\), with three distinct real roots in \((-9,-8)\), \((4,5)\), and \((14,15)\). To verify the root brackets exactly, the values of \(f\) at \(-9,-8,4,5,14,15\), respectively, are \(-163,128,32,-93,-48,197\). The matrix is therefore diagonalizable over \(\mathbb R\) and has spectral radius strictly less than \(15\), whence \(a_h\le C15^h\). Since \(a_h\) is the constant Laurent coefficient of \(L_h\), it equals the sixth moment above.

**Arbitrary prefixes and the disk.** Put \(Q_N(z)=\sum_{0\le j<N}t_jz^j\). Every integer interval \([0,N)\) decomposes into disjoint aligned dyadic blocks, at most one of each length \(2^h\). For such a block beginning at a multiple \(u2^h\), the identity \(t_{u2^h+j}=t_ut_j\) for \(0\le j<2^h\) shows its polynomial is a unimodular rotation and signed multiple of \(T_h\) on the unit circle. The triangle inequality in \(L^6\), combined with the sixth-moment lemma, gives
\[
\|Q_N(e^{i\theta})\|_{L^6(d\theta/2\pi)}
\le C\sum_{0\le h\le\lfloor\log_2N\rfloor}15^{h/6}
\le C N^{\beta/6},\quad \beta=\log_2 15.
\]
Write \(T(z)=\sum_{j\ge0}t_jz^j\) for \(|z|<1\). Abel summation gives
\[
T(re^{i\theta})=(1-r)\sum_{N\ge1}r^{N-1}Q_N(e^{i\theta}),\quad 0<r<1.
\]
Minkowski's inequality and the standard geometric-power sum bound \(\sum_{N\ge1}r^{N-1}N^u=O((1-r)^{-u-1})\), valid for fixed \(u>0\) as \(r\uparrow1\), imply
\[
\|T(re^{i\theta})\|_{L^6(d\theta/2\pi)}
=O((1-r)^{-\beta/6}).
\]

**Coefficient estimate.** Put \(A(z)=(1-z)^{-1}\) and \(F_\pm(z)=(A(z)\pm T(z))/2\). These are the generating series of \(E\) and \(O\). Therefore
\[
(1-z)F_\pm(z)^6=\frac1{64}\sum_{j=0}^{6}\binom6j(\pm1)^j(1-z)^{j-5}T(z)^j.
\]
The \(j=0\) coefficient at \(z^n\) equals \(\binom{n+4}{4}/64\). For the remaining terms, take \(r=e^{-1/n}\) for \(n\ge2\) and \(\delta=1-r\asymp1/n\). Cauchy's coefficient formula costs at most the bounded factor \(r^{-n}=e\). For \(1\le j\le4\), Hölder's inequality with exponents \(6/j\) and \(6/(6-j)\) gives
\[
\left|[z^n](1-z)^{j-5}T(z)^j\right|
\le C\|T(re^{i\theta})\|_6^j
\big\||1-re^{i\theta}|^{-(5-j)}\big\|_{6/(6-j)}.
\]
Using \(|1-re^{i\theta}|\asymp\delta+|\theta|\) on \(-\pi\le\theta\le\pi\) and \((5-j)6/(6-j)>1\), the latter norm is
\[
O\!\left(\delta^{-(5-j)+(6-j)/6}\right).
\]
Hence, for \(1\le j\le4\),
\[
[z^n](1-z)^{j-5}T(z)^j
=O\!\left(n^{4-j(5-\beta)/6}\right)=O(n^\beta),
\]
where the last inequality follows from \(\beta=\log_2 15>3\) and \(\beta<4\) (indeed the exponent decreases with \(j\) and at \(j=1\) is less than \(\beta\) because \(19<5\beta\), as \(2^{19}=524288<759375=15^5\)). For \(j=5\), the same \(L^6\) bound and Hölder yield \(O(n^{5\beta/6})=O(n^\beta)\). For \(j=6\), \(|1-z|\le2\) on the chosen circle and Hölder gives \(O(n^\beta)\). Summing the finitely many terms proves both announced asymptotics.

Finally \(\binom{n+4}{4}/64\sim n^4/1536\), while \(\beta<4\). Both successive differences are therefore eventually positive, as claimed.

## Verification

The standalone `verify.py` reproduces the integral's constant term for each \(0\le h\le7\) independently by squaring the coefficients of the cubed dyadic polynomial and compares it with the matrix recurrence; it checks the six integer root signs and computes exact ordered sixfold representation functions through \(n=200\). It reports the finite nonincreasing points \(\{1,2,4,7,10,13,16,19,22,25,28,31,34,37\}\) for \(r_6\) and \(\{1,2,3,4,5\}\) for \(s_6\) within that range. These are finite tests, **not** proofs of the conjectured sharp cutoffs; the unbounded theorem uses the symbolic estimates above.

## Relationship to prior work

Allouche and Shallit, arXiv:2112.13627v3, Section 4, Theorem 10 and Corollary 11, prove eventual growth for ten summands using a pointwise Fourier bound, while Conjecture 12(a) explicitly asks for eventual growth at six summands. Their Theorem 13 establishes an obstruction for five summands. The present proof uses a **sixth-moment integral bound** instead of their pointwise bound, making the sixfold error smaller than its order-four main term. The source's original preprint was publicly posted on 2021-12-27; its inspected Conjecture 12 is in version 3 posted on 2022-12-20. Known Thue–Morse coefficient-congruence results and unrelated sharp finite-frequency sixth-moment inequalities do not yield the monotonicity statement.

## Limitations

No effective global monotonicity threshold is established; the finite experiments do not prove the specific thresholds proposed in Conjecture 12. No analogous assertion is made for five summands, nor an optimal spectral constant claimed. The originality assessment is literature-based and remains subject to independently discovering unindexed or differently formulated prior results. Independent mathematical audit has not been performed.

## References

1. J.-P. Allouche and J. Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, arXiv:2112.13627, first posted 2021-12-27, version 3 posted 2022-12-20, especially Section 4, Conjecture 12 and Corollary 11. https://arxiv.org/pdf/2112.13627
2. OEIS A001969 (evil numbers) and A000069 (odious numbers), as referenced in [1]. https://oeis.org/A001969 ; https://oeis.org/A000069
