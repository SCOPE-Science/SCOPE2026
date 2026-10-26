# Sharp fourth moments and phase locking for the centered hexagonal Fourier packet

## Finding

Let \(\mathbb T^2\) carry Haar probability measure. The centered nearest-neighbor shell of the triangular (\(A_2\)) frequency lattice is
\[
\Lambda=\{(0,0),\pm A,\pm B,\pm C\},\quad
A=(1,0),\quad B=(0,1),\quad C=A-B.
\]
For arbitrary complex coefficients, set \(P(t)=\sum_{\lambda\in\Lambda}c_\lambda e^{i\langle\lambda,t\rangle}\) and \(S=\sum_{\lambda\in\Lambda}|c_\lambda|^2\). Then
\[
\int_{\mathbb T^2}|P|^4\,dm\le K_*S^2,
\quad
K_*=\frac{t_*^4+36t_*^2+48t_*+90}{(t_*^2+6)^2}
=3.6562899693108\ldots,
\]
where \(t_*=1.35801094267399\ldots\) is the unique positive zero of \(2t^3+6t^2-3t-12\).

For \(S>0\), equality holds **if and only if** there are \(\rho\in\mathbb C\setminus\{0\}\) and \(\theta\in\mathbb R^2\) such that
\[
c_0=\rho t_*,\qquad c_\lambda=\rho e^{i\langle\lambda,\theta\rangle}\quad(\lambda\in\Lambda\setminus\{0\}).
\]
The identical sharp constant and **the same complete continuous two-angle equality family** hold on \((\mathbb Z/q\mathbb Z)^2\), for every integer \(q\ge5\). The angles remain arbitrary real numbers even on a finite torus; coefficient phases need not be characters of the sampling group. The zero polynomial also gives equality trivially.

## Assumptions and scope

All Fourier frequencies are distinct elements of \(\mathbb Z^2\); the integral is normalized to make the total mass one. The fourth moment means the fourth power of the \(L^4\) norm, not the norm itself. On a finite product cyclic group, the mean is normalized counting measure and the character indexed by \((a,b)\) is \((j,k)\mapsto e^{2\pi i(aj+bk)/q}\). We assert finite-group transfer only for \(q\ge5\). No value for smaller orders is asserted.

## Proof

**1. Parseval and the six-root shell.** Write \(P=a+R\), and rotate all coefficients by a scalar of modulus one so that \(a\ge0\). Put \(B_0=\int|R|^2\,dm=\sum_{\lambda\ne0}|c_\lambda|^2\). For \(R=\sum_{\lambda\ne0}c_\lambda e^{i\langle\lambda,t\rangle}\), Parseval for the square gives \(\int|R|^4=\sum_{\gamma}|(c*c)(\gamma)|^2\), where the sum is over the 19 possible pair-sums.

Write \(x_{+i}=|c_{+i}|\) and \(x_{-i}=|c_{-i}|\) for the three opposite pairs of roots, \(s_i=x_{+i}^2+x_{-i}^2\), and \(p_i=x_{+i}x_{-i}\). Replacing coefficients in the convolution by their moduli cannot decrease any absolute convolution coefficient. For nonnegative coefficients the zero sum has convolution coefficient \(2\sum_i p_i\), the six doubled roots contribute \(\sum_i(x_{+i}^4+x_{-i}^4)\), and the 12 remaining nonzero pair-sums have one unordered two-root representation each. Exact enumeration therefore gives
\[
\int|R|^4\,dm\le
2B_0^2-\sum_i(x_{+i}^4+x_{-i}^4)+8\sum_{i<j}p_ip_j.
\]
Now \(\sum_i(x_{+i}^4+x_{-i}^4)\ge B_0^2/6\), while \(p_i\le s_i/2\) and \(\sum_{i<j}s_is_j\le B_0^2/3\). Consequently
\[
\int|R|^4\,dm\le\frac52 B_0^2.
\]
If \(B_0>0\), equality in the preceding coefficient-modulus estimate forces all six \(|c_\lambda|\) equal, because equality in the six-variable fourth-power Cauchy inequality forces equal magnitudes.

**2. The three-root interaction.** The only nonzero summands of \(\int R^2\overline R\,dm\) correspond to two nonzero roots summing to a third. Taking absolute values yields twice the sum of six products, each taking one amplitude from each opposite pair. Among the eight corners of a \(2\times2\times2\) array, precisely an antipodal pair of corners is omitted. For vectors \(u,v,w\in\mathbb R_{\ge0}^2\), this six-corner form is, up to permuting and reversing coordinates,
\[
T(u,v,w)=u^{\mathsf T}M(v)w,
\qquad
M(v)=\begin{pmatrix}v_++v_-&v_+\\v_-&v_++v_-\end{pmatrix}.
\]
Let \(s=v_+^2+v_-^2\), \(h=v_+v_-\), so \(0\le h\le s/2\). The top eigenvalue of \(M(v)^{\mathsf T}M(v)\) is
\[
\frac{3s+4h+\sqrt{5s^2+16sh+12h^2}}2\le\frac92s.
\]
Both terms in the numerator are increasing in \(h\ge0\), and equality in the last inequality requires \(v_+=v_-\). Hence
\[
T(u,v,w)\le\frac3{\sqrt2}\|u\|_2\|v\|_2\|w\|_2.
\]
Taking the opposite-pair masses \(s_1,s_2,s_3\), with \(s_1+s_2+s_3=B_0\), gives
\[
\left|\int R^2\overline R\,dm\right|
\le 3\sqrt2\sqrt{s_1s_2s_3}
\le\sqrt{\frac23}\,B_0^{3/2}.
\]
Both bounds are attained when all six shell magnitudes are identical and their phases are additive-character phases.

**3. Reduction to one variable.** Orthogonality and expansion of the square of \(|a+R|^2\) give the exact identity
\[
\int|a+R|^4\,dm
=a^4+4a^2B_0+2a^2\operatorname{Re}\int R^2\,dm
+4a\operatorname{Re}\int R^2\overline R\,dm
+\int|R|^4\,dm.
\]
Since \(|\int R^2|\le B_0\), steps 1–2 imply
\[
\int|P|^4\,dm
\le a^4+6a^2B_0+\frac8{\sqrt6}aB_0^{3/2}+\frac52B_0^2.
\]
For \(B_0>0\), write \(B_0=6b^2\) and \(t=a/b\ge0\). Dividing by \((a^2+B_0)^2\) gives
\[
F(t)=\frac{t^4+36t^2+48t+90}{(t^2+6)^2}.
\]
Direct differentiation yields
\[
F'(t)=-\frac{24(2t^3+6t^2-3t-12)}{(t^2+6)^3}.
\]
The cubic has precisely one positive real root: its nonzero coefficient signs have one variation, its value at zero is negative, and it grows to positive infinity. Hence \(F\) increases to that root and decreases thereafter. Since \(F(0)=5/2\) and \(\lim_{t\to\infty}F(t)=1\), the global optimum is exactly \(K_*=F(t_*)\). If \(B_0=0\), the ratio is only one, so no additional nonzero extremizer occurs.

**4. Equality phases.** Attaining \(K_*\) forces \(a>0\), \(B_0>0\), and equality at every sharp intermediate inequality, because all terms carry nonnegative multipliers. Step 1 gives a common positive shell magnitude \(b\). Equality in \(\operatorname{Re}\int R^2\le B_0\) forces each opposite-root coefficient product to equal \(b^2\) after the common phase is removed. Thus \(c_{-A}=\overline{c_A}\), \(c_{-B}=\overline{c_B}\), and \(c_{-C}=\overline{c_C}\). Then \(R\) is real-valued on the torus and, using \(A=B+C\),
\[
\int R^2\overline R\,dm
=12b^3\cos(\arg c_A-\arg c_B-\arg c_C).
\]
Its sharp upper bound requires \(\arg c_A=\arg c_B+\arg c_C\pmod{2\pi}\), exactly the additive-character condition. This proves the displayed equality family, including its sufficiency. Reinstating the global scalar gives the statement for complex \(a\).

**5. Finite products.** Each coordinate of every pair-sum in \(\Lambda+\Lambda\) lies between \(-2\) and \(2\). For \(q\ge5\), reduction modulo \(q\) is injective on this pair-sum set. Thus exactly the same convolution identities and proof hold on the finite product. The same continuous two-angle coefficient family gives every equality case; no restriction of the angles to discrete character phases is needed because the full pair-sum relation structure is unchanged.

## Verification

The standalone `checker.py` computes the entire fourth moment by 7-by-7 pair-sum convolution, independently verifies the explicit shell identity and center/arm polynomial, tests arbitrary complex coefficients against the sharp inequality, tests the phase-character equality family, and checks exact convolution-to-finite-grid agreement for orders 5–7. It also tests the six-corner tensor estimate. Its deterministic verification suite reports 3,589 passed assertions. Its finite samples corroborate the identities and do not replace the all-coefficient analytical proof.

## Relationship to prior work

Additive energy and discrete restriction estimates motivate determining the exact fourth moment on highly symmetric finite Fourier supports. Mudgal's work treats asymptotic energy bounds for lattice points on higher-dimensional spheres, not the present seven-coefficient sharp optimization. De Dios Pont, Greenfeld, Ivanisvili and Madrid treat uniform higher-energy inequalities for cube subsets, not the centered triangular lattice packet. A previously available six-root (center-free) sharp fourth moment gives the shell benchmark \(5/2\) but does not resolve the new center–shell cubic interactions or the sharp mixed constant. Closely related five-point cross and six-point triangular-aperture results concern different frequency supports and do not imply the seven-point optimum. See the separate review document for the status and remaining priority limitations.

## Limitations

No assertion is made for finite cyclic orders below five, for nonuniform Fourier weights, or for other root systems. The result is self-contained but has not undergone an independent mathematical audit. Searches cannot rule out older, differently phrased equivalent sharp estimates, especially those obtained through general multilinear tensor inequalities.

## References

1. Akshat Mudgal, *Additive energies on spheres*, arXiv:2105.06925, first posted 14 May 2021; Journal of the London Mathematical Society 106 (2022), 2927–2958. https://arxiv.org/abs/2105.06925
2. Jaume de Dios Pont, Rachel Greenfeld, Paata Ivanisvili, José Madrid, *Additive energies on discrete cubes*, arXiv:2112.09352, first posted 17 December 2021; Discrete Analysis 2023:13. https://arxiv.org/abs/2112.09352
