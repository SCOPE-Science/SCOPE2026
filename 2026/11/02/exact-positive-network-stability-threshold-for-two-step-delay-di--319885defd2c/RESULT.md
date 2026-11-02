# Exact positive-network stability threshold for two-step delay discretizations

## Finding

For every dimension \(n\geq1\), take \(D=\operatorname{diag}(a_1,\ldots,a_n)\) with \(a_j>0\) and an entrywise nonnegative real matrix \(B\). For the constant-delay system
\[
 y'(t)=-D y(t)+B y(t-\tau),\qquad \tau=mh,\quad m\in\{1,2,\ldots\},\ h>0,
\]
apply the second-order, matched-coefficient multistep family of Rodríguez-Gutiérrez and Martín-Vaquero, with \(0<\beta<1\):
\[
\rho(E)y_k=h\sigma(E)(-D y_k+B y_{k-m}),\qquad
\rho(z)=z^2+2(\beta-1)z+1-2\beta,\quad
\sigma(z)=z^2+(\beta-1)z+\beta.
\]
Here \(Ey_k=y_{k+1}\), and the recurrence uses the prescribed discrete history.

**Exact stability theorem.** Every characteristic multiplier lies strictly in the unit disk, for *every* \(h>0\), \(m\geq1\), and \(0<\beta<1\), **if and only if**
\[
\boxed{\operatorname{spr}(D^{-1}B)<1.}
\]
More strongly, this equivalence holds for each individual admissible triple \((h,m,\beta)\). If the radius equals one, \(z=1\) is a multiplier for every triple. If it exceeds one, every triple has a **real** multiplier strictly greater than one. Here \(\operatorname{spr}\) denotes spectral radius, not the polynomial \(\rho\).

This exact condition can certify stable noncommuting matrix pairs that *every* one-exponent generalized field-of-values sufficient condition in the motivating paper fails to certify. One explicit example is
\[
D=\operatorname{diag}(1,2,4),\qquad
B=\begin{pmatrix}0&4&0\\0&0&1/4\\1&0&0\end{pmatrix}.
\]
For this example \(\operatorname{spr}(D^{-1}B)=1/2\), but the numerical radius of \(D^{p/2-1}BD^{-p/2}\) is strictly larger than one for **all** real \(p\).

## Assumptions and scope

The theorem concerns exact arithmetic, homogeneous linear delay systems, a single constant grid-aligned delay \(\tau=mh\), strictly positive diagonal damping, entrywise nonnegative coupling, and the displayed matched implicit/delayed coefficients. No irreducibility, normality, simultaneous diagonalizability, or symmetry is assumed for \(B\). Schur stability means all the finitely many characteristic roots of the autonomous augmented recurrence have modulus strictly below one. The scalar parameters satisfy \(h>0\), integer \(m\geq1\), \(0<\beta<1\). The method's quadratic \(\rho\) is distinguished from \(\operatorname{spr}\), the spectral radius.

## Proof

**1. Positive-real scalar factor.** The polynomial \(\sigma\) has both zeros strictly inside the unit disk by the quadratic Jury inequalities: \(|\beta|<1\), \(1+(\beta-1)+\beta=2\beta>0\), and \(1-(\beta-1)+\beta=2>0\). Therefore \(R(z)=\rho(z)/\sigma(z)\) is analytic on the exterior closed unit disk, including infinity, with \(R(\infty)=1\). For \(z=e^{i\theta}\), direct polynomial multiplication gives
\[
\Re R(e^{i\theta})=
\frac{8(1-\beta)\sin^4(\theta/2)}{|\sigma(e^{i\theta})|^2}\geq0.
\]
The harmonic minimum principle, applied after inversion \(z=1/w\), implies \(\Re R(z)\geq0\) for every \(|z|\geq1\). Consequently, for every \(a>0\),
\[
|\rho(z)+ha\sigma(z)|
=|\sigma(z)|\,|R(z)+ha|\geq ha|\sigma(z)|.
\]

**2. Exact matrix characteristic equation.** Substituting \(y_k=z^k v\) into the recurrence gives
\[
T(z)v=0,\qquad
T(z)=z^m[\rho(z)I+h\sigma(z)D]-h\sigma(z)B.
\]
The determinant \(\det T(z)\) is a polynomial of degree \(n(m+2)\). Its zeros, counted with multiplicity, are the characteristic multipliers of the augmented recurrence, including when the delayed and current-history blocks overlap at \(m=1\) or \(2\).

**3. Complete stable side.** For \(|z|\geq1\), every diagonal entry of \(L(z)=z^m[\rho(z)I+h\sigma(z)D]\) is nonzero by Step 1. Let \(K(z)=L(z)^{-1}h\sigma(z)B\). Entrywise,
\[
|K(z)|\leq D^{-1}B.
\]
Since \(B\geq0\), Perron–Frobenius monotonicity and the complex modulus bound give
\[
\operatorname{spr}(K(z))\leq\operatorname{spr}(|K(z)|)
\leq\operatorname{spr}(D^{-1}B)<1.
\]
Thus \(I-K(z)\) and hence \(T(z)=L(z)(I-K(z))\) are nonsingular for all \(|z|\geq1\). All characteristic multipliers are strictly interior.

**4. Sharp threshold and unstable side.** Because \(\rho(1)=0\) and \(\sigma(1)=2\beta>0\),
\[
T(1)=2h\beta(D-B).
\]
If \(\operatorname{spr}(D^{-1}B)=1\), the nonnegative matrix \(D^{-1}B\) has eigenvalue one, so \(T(1)\) is singular. If \(\operatorname{spr}(D^{-1}B)>1\), for real \(z\geq1\) define
\[
M(z)=z^{-m}\operatorname{diag}\!\left(
\frac{1}{a_j+R(z)/h}\right)_{j=1}^n B.
\]
Here \(R(z)\geq0\), all denominators are positive, and \(M(z)\geq0\). Its spectral radius is continuous, starts above one at \(z=1\), and tends to zero as \(z\to+\infty\). Hence some real \(z_*>1\) has \(\operatorname{spr}(M(z_*))=1\); Perron–Frobenius makes one an eigenvalue of \(M(z_*)\), so \(T(z_*)\) is singular. Thus instability is real and unavoidable for every admissible triple. These four steps prove the iff classification.

**5. An all-exponent numerical-range separation.** For the displayed three-node matrix, \(D^{-1}B\) is a single positive directed cycle whose three edge gains multiply to \(1/8\); therefore its spectral radius equals \((1/8)^{1/3}=1/2\), and Steps 1–4 prove unconditional stability. The motivating paper's generalized field of values is the ordinary numerical range of \(C_p=D^{p/2-1}BD^{-p/2}\). Set \(t=2^{-p/2}>0\); the three cyclic weights of \(C_p\) are \(4t\), \(t/8\), and \(1/(4t^2)\).

For an entrywise nonnegative matrix \(C\), its numerical radius equals the largest eigenvalue of \((C+C^{\mathsf T})/2\): use the absolute-value bound on \(x^*Cx\), followed by a nonnegative Perron eigenvector to attain equality. In this example the symmetric part has characteristic polynomial
\[
\lambda^3-\frac{S(t)}4\lambda-\frac1{32},\qquad
S(t)=\frac{1025}{64}t^2+\frac1{16t^4}.
\]
Calculus or weighted arithmetic–geometric mean gives
\[
S(t)\geq\frac34\left(\frac{1025}{64}\right)^{2/3}>4.
\]
The characteristic polynomial at \(\lambda=1\) is therefore \(1-S(t)/4-1/32<0\), and its largest root exceeds one. Thus the numerical radius of \(C_p\) exceeds one for every real \(p\), and no generalized field-of-values disk certificate applies. This does **not** contradict the cited sufficient criterion; it shows the criterion is not necessary.

## Verification

The included standalone `verify.py` checks the scalar positive-real polynomial identity symbolically; the exact three-node determinant factorization at three integer delays; the numerical-range cubic and strict minimization inequality by exact symbolic arithmetic; 54 finite, independently assembled stable characteristic-root instances including an irreducible cycle and a reducible graph; and 24 threshold/unstable instances. Run with `python verify.py` after installing Python 3, SymPy and NumPy. These finite computations are supplementary; the universal assertion rests on Steps 1–5.

## Relationship to prior work

Rodríguez-Gutiérrez and Martín-Vaquero (2026, arXiv:2610.33780v1) define the second-order matched-coefficient family in their equation (29), show scalar disk stability (Theorem 3.8), and obtain a **sufficient** matrix condition \(F_p(A,B)\subset D(0,1)\) for some \(p\) (Corollary 3.9). Their matrix analysis does not state the exact Perron-root criterion for arbitrary nonnegative network coupling, nor the explicit example where all their one-exponent certificates fail. Tercero-Báez and Martín-Vaquero (2024, arXiv:2412.12297v1) analyze different IMEX–BDF coefficients through scalar regions and generalized numerical ranges. Classical positive-delay-system theory gives the continuous-time Metzler/M-matrix threshold, not by itself the exact Schur-root classification of this particular multistep discretization. General earlier multistep unconditional-stability work supplies broad tools, but no identical theorem was located in the material inspected. This is a literature-based originality assessment, not a claim that all earlier publications have been exhaustively excluded.

## Limitations

Only one constant grid-aligned delay, positive diagonal damping, nonnegative delayed coupling, and \(0<\beta<1\) are covered. Stability of the stationary linear recurrence is not a positivity-preservation assertion for its iterates. Off-grid interpolation, changing delays, signed couplings, floating-point errors, nonlinear dynamics, and infinite-dimensional operators are outside the proof. The first part's condition is inherited from classical positive-system spectral geometry; the asserted contribution is its exact preservation by the specified newly analyzed numerical family and the rigorous insufficiency witness for the one-exponent numerical-range test. Earlier equivalent formulations may exist.

## References

1. J. Rodríguez-Gutiérrez and J. Martín-Vaquero, *On the stability of second-order methods for DDEs and PDDEs*, arXiv:2610.33780v1, submitted 24 October 2026. https://arxiv.org/html/2610.33780v1
2. A. Tercero-Báez and J. Martín-Vaquero, *On the stability of IMEX BDF methods for DDEs and PDDEs*, arXiv:2412.12297v1, submitted 16 December 2024. https://arxiv.org/html/2412.12297v1
3. R. R. Rosales, B. Seibold, D. Shirokoff, and D. Zhou, *Unconditional Stability for Multistep ImEx Schemes: Theory*, SIAM J. Numer. Anal. 55 (2017), 2336–2360, arXiv:1609.04130. https://arxiv.org/abs/1609.04130
4. M. Á. Castro, M. A. García, J. A. Martín, and F. Rodríguez, *Exact and Nonstandard Finite Difference Schemes for Coupled Linear Delay Differential Systems*, Mathematics 7 (2019), article 1038. https://www.mdpi.com/2227-7390/7/11/1038
5. C. Briat, *Positive Systems with Delays* (research overview), https://www.briat.info/research/positive.html
