# A sixth-order transition recurrence and exact bigram law for the Padovan-automatic difference word
## Finding
Let \(a(0)=0\), \(a(1)=1\), and
\[
a(n)=n-a\!\left(n-a\!\left(n-a(n-1)\right)\right)\qquad(n\ge2),
\]
and put \(d_n=a(n+1)-a(n)\in\{0,1\}\). Let \(\rho>1\) be the real root of \(\rho^3=\rho+1\), and let \(c=\rho^{-2}\), equivalently the real root of \(c^3-c^2+2c-1=0\).

Use the explicit non-erasing morphisms \(\nu,\eta\) from Proposition 5.2 and Table 2 of Cloitre--Ma--Zhang, so that \(d_0d_1\cdots=\eta(\nu^\omega(S))\). For
\[
W_m=\eta(\nu^m(S)),\qquad Q_m=\#\{j: (W_m)_j(W_m)_{j+1}=01\},
\]
one has
\[
(Q_0,Q_1,Q_2,Q_3,Q_4,Q_5)=(0,1,1,2,2,3)
\]
and, for every \(m\ge0\),
\[
Q_{m+6}=Q_{m+4}+Q_{m+1}+Q_m.
\]

The adjacent-pair frequencies of the infinite binary word \(d\) therefore exist. If \(\pi_{uv}\) denotes the limiting frequency of \(uv\in\{00,01,10,11\}\), then
\[
\pi_{00}=\frac{4-6c+c^2}{7},\qquad
\pi_{01}=\pi_{10}=\frac{3-c-c^2}{7},\qquad
\pi_{11}=\frac{8c+c^2-3}{7}.
\]
Numerically these are approximately \(0.1293823159\), \(0.3007773931\), \(0.3007773931\), and \(0.2690628979\). In particular the nearest-neighbor covariance has the exact negative value
\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}(d_n-c)(d_{n+1}-c)
=\frac{8c-6c^2-3}{7}\approx-0.0556550594.
\]

## Assumptions and scope
The result uses the proved morphic identity in Proposition 5.2 of arXiv:2609.33421v1. No unproved conjecture about the recurrence is used. The statement concerns adjacent factors of the first-difference word, not higher-order factor frequencies or a full dynamical model.

## Proof
Write \(X_m=\nu^m(S)\). Track simultaneously the counts of the \(26\) letters in \(X_m\) and the counts of the \(68\) adjacent letter pairs that occur under iteration. This gives a \(94\)-dimensional integer linear state \(x_m=T^m x_0\). Because \(\eta\) has nonempty images of length one or two, both \(|W_m|\) and \(Q_m\) are integer linear functionals of this state.

An exact reconstruction of Table 2 gives
\[
L_m:=|W_m|:\quad L_0,L_1,L_2=2,3,4,\qquad L_{m+3}=L_{m+1}+L_m,
\]
and
\[
Q_0,\ldots,Q_5=0,1,1,2,2,3,\qquad Q_{m+6}=Q_{m+4}+Q_{m+1}+Q_m.
\]
For completeness, the finite linear certificate checks the residuals of both recurrences for \(94\) consecutive powers of \(T\). Cayley--Hamilton then makes each recurrence valid for every later power as well.

Thus the generating functions are
\[
\sum_{m\ge0}L_m z^m=\frac{2+3z+2z^2}{1-z^2-z^3}
\]
and
\[
\sum_{m\ge0}Q_m z^m=
\frac{z(1+z+z^2+z^3+z^4)}{1-z^2-z^5-z^6}
=
\frac{z(1+z+z^2+z^3+z^4)}{(1+z^3)(1-z^2-z^3)}.
\]
The common dominant singularity is \(z_0=\rho^{-1}\). Taking the ratio of the dominant coefficients gives
\[
\lim_{m\to\infty}\frac{Q_m}{L_m}
=
\frac{z_0(1+z_0+z_0^2+z_0^3+z_0^4)}{(1+z_0^3)(2+3z_0+2z_0^2)}
=
\frac{3-c-c^2}{7}.
\]
The last equality follows by reducing with \(\rho^3=\rho+1\) and \(c=\rho^{-2}=1+\rho-\rho^2\).

The restriction of \(\nu\) to the other \(25\) letters is primitive; the exact incidence computation gives a positive twentieth power. Standard Perron--Frobenius frequency theory for primitive substitutions, followed by the non-erasing output morphism \(\eta\), therefore upgrades the prefix-limit above to the frequency of \(01\) in the full infinite word.

For every finite binary word, the difference between the numbers of \(01\) and \(10\) factors is determined by its two endpoint bits, so the two limiting frequencies are equal. Cloitre--Ma--Zhang prove that the one-letter frequency of \(1\) is \(c\). Hence \(\pi_{11}=c-\pi_{10}\) and \(\pi_{00}=1-c-\pi_{01}\), which gives the displayed table. The covariance is \(\pi_{11}-c^2\).

## Verification
The standalone verifier reconstructs the substitution and output morphism from Table 2, closes the adjacent-pair state space, checks that it has \(68\) pair states and total dimension \(94\), verifies the length and transition recurrences over the Cayley--Hamilton window, and checks that the \(25\)-letter growing component becomes strictly positive at incidence-matrix power \(20\). It also independently evaluates the original nested recurrence through \(200000\) first differences as a normalization check. The finite numerical replay is not used as an infinite proof.

## Relationship to prior work
Cloitre--Ma--Zhang prove the recurrence identification, the explicit \(26\)-letter morphic presentation, the one-letter frequency \(c\), nonperiodicity, and least balance constant \(4\). Their full text does not state adjacent-pair frequencies; Section 6 instead lists the dynamical description of the difference word as an open direction. The exact bigram law here is the first local correlation invariant beyond the one-letter density, and the sixth-order recurrence explains it through the same Padovan cubic together with unit-circle factors.

The OEIS entry A076502 records the recurrence and its asymptotic slope, but does not record adjacent-pair frequencies. Targeted searches of published mathematical findings and public web sources found no equivalent formula or stronger result for this word.

## Limitations
This result does not identify the full shift-invariant measure, frequencies of factors of length at least three, or the proposed toral-rotation coding. Its proof is conditional on the correctness of the source's morphic identity, which is itself formally and computationally verified in that work. The independent direct recurrence replay here only checks normalization on a finite prefix.

## References
1. B. Cloitre, H. Ma, and W. Zhang, “A Padovan-automatic description of a nested recurrence,” arXiv:2609.33421v1, 2026.
2. B. Cloitre, H. Ma, and W. Zhang, reproducibility package for the same work, DOI:10.5281/zenodo.22979217, published 2026-09-26.
3. OEIS Foundation Inc., OEIS A076502.
