# Monomial rigidity for polynomial-symbol Hankel operators obeying the strong reproducing kernel thesis

## Finding

Let
\[
\psi(z)=\sum_{k=1}^{N}c_kz^k
\]
be a nonzero analytic polynomial with \(\psi(0)=0\). For the Hardy-space Hankel operator
\[
H_{\overline\psi}f=P_-(\overline\psi f),
\]
the strong reproducing kernel thesis
\[
\|H_{\overline\psi}\|
=
\sup_{a\in\mathbb D}\|H_{\overline\psi}k_a\|_2
\]
holds if and only if
\[
\psi(z)=cz^m
\]
for some \(c\neq0\) and \(m\ge1\).

Using the standard identities
\[
\|H_{\overline\psi}\|=\|\psi\|_*,
\qquad
\sup_{a\in\mathbb D}\|H_{\overline\psi}k_a\|_2=\|\psi\|_G,
\]
this says that a nonzero polynomial symbol satisfies
\[
\|\psi\|_*=\|\psi\|_G
\]
exactly when it is a monomial.

## Assumptions and scope

The Hardy space \(H^2\) has orthonormal basis
\[
1,z,z^2,\ldots,
\]
and
\[
k_a(w)=\frac{\sqrt{1-|a|^2}}{1-\overline a w}
\]
is the normalized reproducing kernel. The symbol is normalized by \(\psi(0)=0\), which is natural because an analytic constant does not affect the antianalytic Hankel operator.

The statement classifies polynomial symbols only. It makes no assertion for general \(H^\infty_0\) or \({\rm BMOA}_0\) symbols.

## Proof

Put
\[
E_N=\operatorname{span}\{1,z,\ldots,z^{N-1}\}.
\]
Direct multiplication gives
\[
H_{\overline\psi}z^j
=
\sum_{m=1}^{N-j}\overline{c_{m+j}}z^{-m}
\quad(0\le j<N),
\]
and
\[
H_{\overline\psi}z^j=0
\quad(j\ge N).
\]
Hence \(H_{\overline\psi}\) has finite rank and
\[
H_{\overline\psi}=H_{\overline\psi}P_{E_N}.
\]
Therefore
\[
A:=H_{\overline\psi}^*H_{\overline\psi}
\]
has range contained in \(E_N\).

As \(|a|\to1\), the normalized kernels \(k_a\) converge weakly to zero in \(H^2\). This follows first for polynomials and then for arbitrary \(H^2\) functions by norm approximation and the fact that \(\|k_a\|_2=1\). Since \(H_{\overline\psi}\) is compact,
\[
\|H_{\overline\psi}k_a\|_2\to0
\qquad(|a|\to1).
\]
The kernel-norm function is continuous. Thus, if the strong thesis holds, its positive supremum is attained at an interior point \(a_0\).

For a unit vector, equality in the Rayleigh quotient of the positive operator \(A\) implies
\[
Ak_{a_0}=\|H_{\overline\psi}\|^2k_{a_0}.
\]
The left side belongs to \(E_N\). If \(a_0\neq0\), then
\[
k_{a_0}(w)
=
\sqrt{1-|a_0|^2}\sum_{j\ge0}\overline{a_0}^{\,j}w^j
\]
has infinitely many nonzero coefficients and cannot lie in \(E_N\). Hence
\[
a_0=0,
\qquad
k_{a_0}=1.
\]
Therefore the strong thesis holds exactly when \(1\) is an operator-norming vector.

If \(1\) is norming, then
\[
A1=\|H_{\overline\psi}\|^2\,1.
\]
Taking inner products with \(z^j\), for \(1\le j<N\), gives
\[
0
=
\langle H_{\overline\psi}1,H_{\overline\psi}z^j\rangle
=
\sum_{m=1}^{N-j}c_{m+j}\overline{c_m},
\]
up to the harmless global conjugation determined by the inner-product convention. Thus every positive-lag aperiodic autocorrelation of \((c_1,\ldots,c_N)\) vanishes.

Assume that at least two coefficients are nonzero. Let
\[
r=\min\{k:c_k\neq0\},
\qquad
s=\max\{k:c_k\neq0\},
\]
with \(r<s\), and choose
\[
j=s-r.
\]
For a nonzero summand in
\[
\sum_{m=1}^{N-j}c_{m+j}\overline{c_m},
\]
one needs simultaneously \(m\ge r\) and \(m+j\le s\). With \(j=s-r\), these inequalities force \(m=r\). Hence the whole correlation equals
\[
c_s\overline{c_r}\neq0,
\]
a contradiction. Thus exactly one coefficient is nonzero.

Conversely, if
\[
\psi(z)=cz^m,
\]
then
\[
H_{\overline\psi}z^j
=
\begin{cases}
\overline c\,z^{j-m},&0\le j<m,\\
0,&j\ge m.
\end{cases}
\]
So \(H_{\overline\psi}\) is \(|c|\) times an isometry on
\[
\operatorname{span}\{1,\ldots,z^{m-1}\}
\]
and vanishes on its orthogonal complement. Consequently
\[
\|H_{\overline\psi}\|
=
|c|
=
\|H_{\overline\psi}k_0\|_2,
\]
which proves the converse.

## Verification

No numerical experiment is used. The proof reduces the question to five exact checks:

1. polynomial degree gives finite rank and
\[
\operatorname{Ran}(H_{\overline\psi}^*H_{\overline\psi})\subset E_N;
\]
2. normalized Hardy kernels are weakly null at the boundary;
3. compactness therefore forces any kernel norm saturation to occur in the disk;
4. finite-dimensional range forces the norming kernel to be \(k_0\);
5. the maximal occupied lag isolates one nonzero autocorrelation term unless the coefficient support is a singleton.

The monomial converse is checked directly on the Hardy basis.

## Relationship to prior work

Dyakonov's recent paper formulates the problem of characterizing Hankel operators obeying the strong reproducing kernel thesis. It recalls
\[
\|H_{\overline\psi}\|=\|\psi\|_*,
\qquad
\sup_{a\in\mathbb D}\|H_{\overline\psi}k_a\|_2=\|\psi\|_G,
\]
so the problem is exactly to classify equality in
\[
\|\psi\|_G\le\|\psi\|_*.
\]
The paper gives sufficient examples through \(G\)-extremal functions and records that a suitable quadratic symbol of the form
\[
az+z^2
\]
can fail the strong thesis. It does not classify polynomial symbols.

Brevig and Seip study a different equality condition,
\[
\|H_{\overline\psi}\|=\|\psi\|_\infty,
\]
called maximal norm. Their norm-attainment rigidity does not imply equality between the Garsia and Nehari quotient norms when both are strictly smaller than the supremum norm.

Dyakonov's earlier Garsia-norm work studies the stronger equality
\[
\|\psi\|_G=\|\psi\|_\infty.
\]
That produces sufficient strong-thesis examples, but it does not classify the intermediate equality
\[
\|\psi\|_G=\|\psi\|_*.
\]
The polynomial theorem above rules out such intermediate equality for every nonmonomial polynomial.

## Limitations

The proof uses finite rank essentially. For nonpolynomial symbols, a norming kernel need not be forced into a finite-dimensional range, so the argument does not extend directly.

The theorem therefore settles only the polynomial-symbol subclass of the broader open problem. It does not decide whether there are nonpolynomial symbols satisfying
\[
\|\psi\|_*=\|\psi\|_G<\|\psi\|_\infty
\]
or unbounded \({\rm BMOA}_0\) examples.

An equivalent finite-rank observation could conceivably occur in older Hankel-matrix literature under different terminology; targeted searches did not locate such a statement.

## References

1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v1, 2026.
2. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, J. Math. Anal. Appl. 529 (2024), 127221; arXiv:2301.07937.
3. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, J. Funct. Anal. 288 (2025), 110833; arXiv:2404.05565.
4. F. F. Bonsall, *Boundedness of Hankel matrices*, J. London Math. Soc. 29 (1984), 289--300.
5. S. Treil, *A remark on the reproducing kernel thesis for Hankel operators*, St. Petersburg Math. J. 26 (2015), 479--485.
