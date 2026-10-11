# Exact fourth moment and all extremizers for four consecutive Fourier characters
## Finding
For every integer \(N\ge7\), let \(\zeta_N=e^{2\pi i/N}\) and
\[
F_N(k)=\sum_{j=0}^3 a_j\zeta_N^{jk},\qquad k=0,\ldots,N-1.
\]
With \(S=\sum_{j=0}^3|a_j|^2\), the **sharp fourth-moment inequality** is
\[
\frac1N\sum_{k=0}^{N-1}|F_N(k)|^4\le C S^2,
\qquad
C=\frac{3t^4+4t^3+12t^2+3}{2(1+t^2)^2}=2.808840165474\ldots,
\]
where \(t\) is the unique positive root of
\[
t^3+3t^2-3t-3=0,\qquad 1.261802<t<1.261803.
\]
Every nonzero equality case, and no other, has coefficients
\[
(a_0,a_1,a_2,a_3)=\lambda(1,t e^{i\theta},t e^{2i\theta},e^{3i\theta}),
\quad \lambda\in\mathbb C\setminus\{0\},\ \theta\in\mathbb R.
\]
The identical sharp inequality and equality characterization hold for the integral of \(|F(e^{ix})|^4\) over normalized Haar measure on the circle.

## Assumptions and scope
The coefficients are arbitrary complex numbers; no reality or phase-only restriction is imposed. The input norm uses counting measure on four coefficients; the output uses probability measure on the cyclic grid, or probability Haar measure on the circle. Frequencies are consecutive and unweighted. The lower bound \(N\ge7\) ensures that distinct harmonics of the degree-six trigonometric polynomial \(|F_N|^4\) do not alias. The theorem does not treat shorter grids, different frequency sets, or other moments.

## Proof
Put \(a_j=x_j e^{i\phi_j}\) with \(x_j=|a_j|\ge0\). Define the three aperiodic correlations
\[
R_1=a_1\overline {a_0}+a_2\overline {a_1}+a_3\overline {a_2},\quad
R_2=a_2\overline {a_0}+a_3\overline {a_1},\quad
R_3=a_3\overline {a_0}.
\]
Since the Fourier frequencies in \(|F|^2\) are between \(-3\) and \(3\), orthogonality for \(N\ge7\), and likewise on \(\mathbb T\), gives exactly
\[
\langle |F|^4\rangle=S^2+2(|R_1|^2+|R_2|^2+|R_3|^2).
\tag{1}
\]
Introduce mirror-pair root mean squares
\[
A=\sqrt{\frac{x_0^2+x_3^2}{2}},\qquad
B=\sqrt{\frac{x_1^2+x_2^2}{2}},\qquad S=2(A^2+B^2).
\]
Triangle inequality, Cauchy–Schwarz, and arithmetic–geometric mean give
\[
\begin{aligned}
|R_1|&\le x_0x_1+x_1x_2+x_2x_3\le 2AB+B^2,\\
|R_2|&\le x_0x_2+x_1x_3\le2AB,\\
|R_3|&\le x_0x_3\le A^2.
\end{aligned}
\tag{2}
\]
For \((a_0,a_1,a_2,a_3)=(A,B,B,A)\), all three inequalities in (2) are equalities simultaneously, so mirror-pair reduction does not sacrifice a possible maximizer. For \(A>0\), set \(t=B/A\) and substitute (2) into (1):
\[
\frac{\langle|F|^4\rangle}{S^2}\le
1+\frac{2[(2AB+B^2)^2+(2AB)^2+A^4]}{4(A^2+B^2)^2}
= M(t)=\frac{3t^4+4t^3+12t^2+3}{2(1+t^2)^2}.
\]
A direct differentiation gives
\[
M'(t)=-\frac{2t(t^3+3t^2-3t-3)}{(1+t^2)^3}.
\]
The cubic \(g(t)=t^3+3t^2-3t-3\) has exactly one positive zero: the coefficient signs have one variation, and \(g(0)<0<\lim_{t\to\infty}g(t)\). Therefore \(M\) increases strictly until its unique positive root \(t_*\), then strictly decreases. At the boundary \(B=0\) or \(A=0\), the value is at most \(3/2\), strictly below \(M(t_*)\). Thus \(C=M(t_*)\) is the global sharp value.

To recover all equality cases, \(A,B>0\). Equality in \(x_0x_3\le A^2\) forces \(x_0=x_3=A\). Equality in \(x_1x_2\le B^2\) then forces \(x_1=x_2=B\). Equality in the triangle inequality for \(R_1\) forces the three adjacent phase differences \(\phi_1-\phi_0\), \(\phi_2-\phi_1\), and \(\phi_3-\phi_2\) to coincide modulo \(2\pi\). Hence \(\phi_j=\phi_0+j\theta\), and the coefficients have exactly the stated form. Conversely, these coefficients make (1)–(2) and the one-variable maximum exact.

## Verification
The standalone standard-library program `check.py` verifies the rational polynomial identity underlying \(M'\), a rational isolating bracket for the unique positive root, exact convolution–correlation equality and each Cauchy–Schwarz/AM–GM scalar inequality on 624 integer coefficient vectors, and independent complex-coefficient quadrature at five cyclic grid orders \(7,8,9,11,15\). It prints `VERIFY_OK`. This finite verification is supplemental: (1)–(2), the cubic sign analysis and equality proof establish the theorem for **all** \(N\ge7\).

## Relationship to prior work
Finite Fourier restriction and extension problems have a broad literature; Christ–Shao study a continuous spherical extension problem, whose geometry and exponent setting do not imply this exact four-frequency packet value. Osgood–Siripuram–Wu study cyclic Fourier interpolation and universal sampling, not sharp complex-coefficient fourth moments. Related published work on phase-only four-point *lower* moments and on three-frequency projection norms likewise does not entail the unrestricted *upper* fourth moment and equality family obtained here. An equivalent formulation in historical sharp trigonometric-polynomial tables is a residual priority possibility.

## Limitations
No result is asserted for \(N\le6\), where fourth-moment aliasing may occur. No claim is made for arbitrary Fourier support sets or exponents other than four. The algebraic proof does not certify absolute historical novelty or independent review.

## References
- M. Christ and S. Shao, *On the extremizers of an adjoint Fourier restriction inequality*, arXiv:1006.4318, originally posted 2010-06-22, https://arxiv.org/abs/1006.4318.
- B. Osgood, V. Siripuram and H. Wu, *Discrete sampling and interpolation: universal sampling sets*, arXiv:1204.0992, originally posted 2012-04-04, https://arxiv.org/abs/1204.0992.
