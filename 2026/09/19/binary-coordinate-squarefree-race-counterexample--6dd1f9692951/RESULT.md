# A binary-coordinate obstruction to universal oscillation in squarefree congruence races

## Statement

Fix an integer \(M\ge 3\), put \(m=\varphi(M)\), and enumerate the reduced residue classes modulo \(M\) by \(m_1,\ldots,m_m\). For a squarefree integer \(N\) coprime to \(M\), let \(n_i(N)\) be the number of prime divisors of \(N\) congruent to \(m_i\pmod M\). Given positive integers \(l_1,\ldots,l_m\) and an admissible vector \(a=(a_1,\ldots,a_m)\), define
\[
 A_a(x)=\{N\le x:N\text{ squarefree},\ (N,M)=1,\ n_i(N)\equiv a_i\pmod{l_i}\ \forall i\}.
\]
Write \(L=\prod_i l_i\).

Tang's recent paper proves equidistribution of the sets \(A_a(x)\) and, in the regime where at least one \(l_i\ge3\), conjectures that \(|A_a(x)|-|A_{a'}(x)|\) changes sign infinitely often for every distinct pair \(a,a'\). The following one-coordinate dichotomy shows that the conjecture, as stated, is false.

**Theorem (one-coordinate race dichotomy).** Assume \(m>2\), and suppose \(a,a'\) differ in exactly one coordinate \(c\).

1. If \(l_c=2\), then there is a constant \(C_c>0\) such that
   \[
   |A_a(x)|-|A_{a'}(x)|
   \sim
   \frac{(-1)^{a_c}-(-1)^{a'_c}}{L}\,C_c\,x(\log x)^{-2/m}.
   \]
   In particular the sign is eventually constant, regardless of the values of the other moduli \(l_i\).

2. If \(l_c=\ell\ge3\), put \(\omega=e^{2\pi i/\ell}\),
   \[
   z_c=1+\frac{\omega-1}{m},\qquad
   \alpha=\frac{\cos(2\pi/\ell)-1}{m},\qquad
   \beta=\frac{\sin(2\pi/\ell)}{m}>0.
   \]
   Then there is a nonzero complex constant \(K_c\) such that
   \[
   |A_a(x)|-|A_{a'}(x)|
   =\frac{2x(\log x)^\alpha}{L}
   \operatorname{Re}\!\left(
     (\omega^{-a_c}-\omega^{-a'_c})K_c
     e^{i\beta\log\log x}
   \right)
   +o\!\left(x(\log x)^\alpha\right).
   \]
   Hence the sign changes infinitely often. Moreover the positive and negative sides each have log-log density \(1/2\), in the usual weight \(1/(n\log n)\).

Thus, for a Hamming-distance-one comparison, the relevant modulus is the modulus on the coordinate that actually changes; a larger modulus on an unchanged coordinate does not force oscillation.

## Explicit counterexample to the universal sign-change conjecture

Take
\[
M=5,\qquad (m_1,m_2,m_3,m_4)=(1,2,3,4),\qquad
(l_1,l_2,l_3,l_4)=(3,2,1,1),
\]
and compare
\[
a=(0,0,0,0),\qquad a'=(0,1,0,0).
\]
Here \(l_1=3\), so the system lies in Tang's regime "\(l_i\ge3\) for some \(i\)". Nevertheless the two vectors differ only in the binary coordinate \(c=2\). The theorem gives
\[
|A_{(0,0,0,0)}(x)|-|A_{(0,1,0,0)}(x)|
\sim \frac{C_2}{3}\frac{x}{\sqrt{\log x}},\qquad C_2>0.
\]
Consequently this difference is eventually positive and does not change sign infinitely often.

More precisely, the three Fourier modes surviving in the difference have pole orders
\[
\frac12,\qquad \frac18+\frac{\sqrt3}{8}i,\qquad
\frac18-\frac{\sqrt3}{8}i.
\]
Therefore
\[
|A_{(0,0,0,0)}(x)|-|A_{(0,1,0,0)}(x)|
=
\frac{C_2}{3}x(\log x)^{-1/2}
+O\!\left(x(\log x)^{-7/8}\right),
\]
with \(C_2>0\).

## Proof

For \(e_i=e^{2\pi i/l_i}\) and
\[
J=\prod_i\{0,1,\ldots,l_i-1\},
\]
Tang uses the root-of-unity decomposition
\[
L_j(s)=\prod_{i=1}^m\prod_{p\equiv m_i\, (M)}
\left(1+e_i^{j_i}p^{-s}\right),\qquad j\in J,
\]
whose pole order at \(s=1\) is
\[
z_j=\frac1m\sum_{i=1}^m e_i^{j_i}.
\]
Fourier inversion gives
\[
|A_a(x)|
=\frac1L\sum_{j\in J}
\left(\prod_i e_i^{-a_i j_i}\right)\widetilde A_j(x),
\]
where \(\widetilde A_j(x)\) is the partial sum of the Dirichlet coefficients of \(L_j\).

Suppose \(a,a'\) differ only in coordinate \(c\). Their Fourier coefficient difference factors as
\[
\left(\prod_{i\ne c}e_i^{-a_i j_i}\right)
\left(e_c^{-a_cj_c}-e_c^{-a'_cj_c}\right).
\]
It vanishes whenever \(j_c=0\). Among the surviving modes, the real part
\[
\Re z_j=\frac1m\sum_i\cos(2\pi j_i/l_i)
\]
is maximized by setting every \(j_i=0\) for \(i\ne c\). Thus unrelated coordinates cannot supply the leading term.

If \(l_c=2\), the unique dominant surviving index is \(j=e_c\), where now \(e_c=-1\), and
\[
z_{e_c}=1-\frac2m.
\]
Since \(m>2\), this is positive. Write
\[
L_{e_c}(s)=\zeta(s)^{1-2/m}G_c(s).
\]
The standard Selberg--Delange factorization makes \(G_c\) holomorphic and nonzero at \(1\). For real \(s>1\), both the normalized Euler product and its limit are real and positive, hence
\[
C_c:=\frac{G_c(1)}{\Gamma(1-2/m)}>0.
\]
All other surviving modes have strictly smaller real pole order, so Selberg--Delange gives
\[
|A_a(x)|-|A_{a'}(x)|
\sim
\frac{(-1)^{a_c}-(-1)^{a'_c}}{L}
C_c x(\log x)^{-2/m}.
\]

If \(l_c=\ell\ge3\), the two dominant surviving indices are \(j_c=1\) and \(j_c=\ell-1\), with every other coordinate zero. Their pole orders are \(z_c\) and \(\overline{z_c}\). Writing
\[
L_{e_c}(s)=\zeta(s)^{z_c}G_c(s),\qquad
K_c=\frac{G_c(1)}{\Gamma(z_c)},
\]
the same factorization shows \(K_c\ne0\), and the conjugate mode has constant \(\overline{K_c}\). The two Selberg--Delange main terms combine to the displayed cosine law. Every other surviving Fourier mode has a strictly smaller real pole order, yielding the stated little-oh remainder.

Because the amplitude is nonzero and \(\beta>0\), the leading cosine takes both signs infinitely often. Away from arbitrarily small neighborhoods of its zeros, the little-oh term cannot alter the sign. The standard change of variable \(t=\log\log x\) then gives log-log density \(1/2\) for each sign, exactly as in the classical scalar residue race for \(\omega(n)\).

For the explicit \(M=5\) example, Fourier cancellation removes every mode with \(j_2=0\). The remaining indices are \((j_1,j_2)=(0,1),(1,1),(2,1)\). Their pole orders are respectively \(1/2\) and \((1+e^{\pm2\pi i/3})/4=1/8\pm i\sqrt3/8\), proving the sharper displayed error term.

## Verification

`artifacts/verify_example.py` separately enumerates squarefree integers up to \(10^6\) for the explicit \(M=5\) example. The exact differences
\[
|A_{(0,0,0,0)}(10^4)|-|A_{(0,1,0,0)}(10^4)|=197,
\]
\[
|A_{(0,0,0,0)}(10^5)|-|A_{(0,1,0,0)}(10^5)|=1673,
\]
\[
|A_{(0,0,0,0)}(10^6)|-|A_{(0,1,0,0)}(10^6)|=15160
\]
are positive and consistent with an \(x/\sqrt{\log x}\) main term. These finite computations are only a check; the counterexample is proved by the pole-order argument above.

## Relation to prior literature

Tang's 2026 preprint establishes the underlying equidistribution and Fourier/Selberg--Delange framework. Its Section 4.2, headed by the case where some \(l_i\ge3\), gives one oscillatory example and conjectures infinite sign changes for every distinct pair. The counterexample above shows that a modulus \(\ge3\) on a coordinate where the two vectors agree is irrelevant to the leading race.

Porritt's 2018 work proves log-log oscillation laws for the scalar race \(\omega(n)\bmod q\), and notes analogous squarefree variants. That work does not impose a vector of separate congruence conditions on prime-factor counts in each reduced residue class modulo \(M\), and it does not cover Tang's mixed-modulus conjecture. The cosine/log-log-density step used here is consistent with that classical scalar mechanism.

To the best of our knowledge, searches of the source title/arXiv identifier, synonymous descriptions of squarefree prime-factor congruence races, and the specific mixed modulus \((3,2,1,1)\) did not locate an earlier correction or counterexample to Tang's conjecture. The source is very recent, so unindexed concurrent comments remain a material originality risk.

## Limitations

The result does not classify every pair \(a,a'\) in the mixed-modulus problem. When several changed coordinates share the largest relevant modulus, their leading Selberg--Delange constants can interact and may cancel; this requires additional analysis. The theorem gives a complete classification only for pairs differing in one coordinate, plus an explicit infinite family of counterexamples to the blanket oscillation claim. No independent validation or formal proof-assistant verification is asserted.

## References

1. W. Tang, *Distribution of squarefree integers with double congruence conditions*, arXiv:2609.16716 (2026). https://arxiv.org/abs/2609.16716
2. S. Porritt, *Residue races of the number of prime divisors function*, Journal of Number Theory 192 (2018), 1--14; arXiv:1806.01585. https://arxiv.org/abs/1806.01585
3. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, third edition, AMS, 2015 (Selberg--Delange method).
