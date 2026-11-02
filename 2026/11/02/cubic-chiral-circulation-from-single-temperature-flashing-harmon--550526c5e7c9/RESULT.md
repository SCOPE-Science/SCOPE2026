# Cubic chiral circulation from single-temperature flashing harmonic traps

## Finding

Switching randomly between **two individually conservative harmonic traps** creates a stationary signed angular-area current, even though both phases use one isotropic heat bath, and every frozen-phase Langevin diffusion is reversible. For all parameters specified below, the complete current is
\[
\boxed{\Omega=-\frac{Tc^3(a-b)\lambda(p+\lambda)}{2abQR}},
\qquad p=a+b,
\]
where \(Q=(a+\lambda)(b+\lambda)\), \(H=p/(2ab)+(p+2\lambda)/(2Q)\), and \(R=p(p+2\lambda)-c^2(p+\lambda)H>0\). Accordingly the signed circulation is **cubic rather than linear** in the off-diagonal trap coupling. It is nonzero for every finite positive switching rate precisely when \(c(a-b)\ne0\), and reverses sign when either anisotropy contrast or trap tilt reverses.

In the simple positive-definite example \((a,b,c,T)=(2,1,1,1)\),
\[
\Omega(\lambda)=-\frac{\lambda(\lambda+3)}{21\lambda^3+86\lambda^2+105\lambda+36}.
\]
Its magnitude has exactly one global maximum on \((0,\infty)\), at the unique positive root \(\lambda_*\approx0.787960172311\) of
\[
7\lambda^4+42\lambda^3+51\lambda^2-24\lambda-36=0.
\]

## Assumptions and scope

Fix \(a,b,T,\lambda>0\) and \(c\in\mathbb R\) with \(c^2<ab\). Let \(W\) be two-dimensional standard Brownian motion, independent of the continuous-time two-state chain \(\sigma\), with generator \(\lambda\begin{psmallmatrix}-1&1\\1&-1\end{psmallmatrix}\). The planar process solves
\[
dX_t=-K_{\sigma_t}X_t\,dt+\sqrt{2T}\,dW_t,
\quad K_0=\begin{pmatrix}a&0\\0&b\end{pmatrix},\quad
K_1=\begin{pmatrix}a&c\\c&b\end{pmatrix}.
\]
Both stiffness matrices are symmetric positive definite, representing equilibrium harmonic confinement when held fixed. Uniform positive definiteness and nondegenerate noise yield a unique stationary joint law with finite moments. Set \(X=(X_1,X_2)\) and define the signed **area increment per time** by
\[
\Omega=\lim_{h\downarrow0}\frac1h\mathbb E[X_1(t)(X_2(t+h)-X_2(t))-X_2(t)(X_1(t+h)-X_1(t))],
\]
with stationary initialization. This is equivalently the stationary rate of \(\int(X_1\circ dX_2-X_2\circ dX_1)\). This observable is not the mean polar-angle velocity, which requires a different definition.

## Proof

Write \(S_i=\mathbb E[X X^{\mathsf T}\mathbf1_{\{\sigma=i\}}]\). Since \(\mathbb P(\sigma=i)=1/2\), applying the joint diffusion-switch generator to the six stationary second moments gives exactly
\[
K_iS_i+S_iK_i+\lambda(S_i-S_{1-i})=T I_2,\qquad i=0,1.
\tag{1}
\]
This equation is valid without assuming a Gaussian joint stationary law. Let \(x_i=(S_i)_{11}\), \(y_i=(S_i)_{22}\), and \(z_i=(S_i)_{12}\). The off-diagonal equation at phase zero gives \(z_0=\lambda z_1/(p+\lambda)\). Inverting the two diagonal-moment \(2\times2\) linear systems gives
\[
x_1=\frac{T}{2a}-\frac{c(2a+\lambda)z_1}{2a(a+\lambda)},\qquad
y_1=\frac{T}{2b}-\frac{c(2b+\lambda)z_1}{2b(b+\lambda)}.
\tag{2}
\]
Substitution in the phase-one off-diagonal equation yields
\[
\left(\frac{p(p+2\lambda)}{p+\lambda}-c^2 H\right)z_1=-\frac{cTp}{2ab},
\qquad
z_1=-\frac{cTp(p+\lambda)}{2abR}.
\tag{3}
\]
The division is legitimate. Indeed \(H>0\), \(c^2<ab\), and direct expansion gives
\[
2Q\bigl[p(p+2\lambda)-ab(p+\lambda)H\bigr]
=\lambda\bigl[p^3+(4a^2+6ab+4b^2)\lambda+3p\lambda^2\bigr]>0.
\tag{4}
\]
Hence \(R>0\) for every allowed parameter. By the Itô drift rule, the signed area rate is
\[
\Omega=\mathbb E[X_1(-bX_2-cX_1\mathbf1_{\{\sigma=1\}})
-X_2(-aX_1-cX_2\mathbf1_{\{\sigma=1\}})]
=(a-b)(z_0+z_1)-c(x_1-y_1).
\tag{5}
\]
The quadratic-variation correction in converting to Stratonovich signed area cancels because the two noise coordinates have zero cross-variation. Substituting (2)–(3) into (5) and simplifying gives the boxed expression exactly. The numerator and \(R>0\) give the if-and-only-if criterion and sign.

For fixed positive \(a,b,T,\lambda\), with small \(c\), replacing \(R\) by \(p(p+2\lambda)+O(c^2)\) shows
\[
\Omega=-\frac{T(a-b)\lambda(p+\lambda)}{2abQp(p+2\lambda)}c^3+O(c^5).
\]
For fixed permissible \(c\), the endpoint asymptotics are
\[
\Omega\sim-\frac{Tc^3(a-b)}{2abp(ab-c^2)}\lambda\quad(\lambda\downarrow0),
\qquad
\Omega\sim-\frac{Tc^3(a-b)}{p(4ab-c^2)\lambda}\quad(\lambda\to\infty).
\]
The corresponding slow/fast switching limits both have zero area current. In the canonical case, the stated rational formula follows by direct substitution; its derivative is
\[
\frac{3(7\lambda^4+42\lambda^3+51\lambda^2-24\lambda-36)}{(21\lambda^3+86\lambda^2+105\lambda+36)^2}.
\]
The numerator polynomial has exactly one positive root by Descartes' sign rule and changes from negative at zero to positive at infinity. Since \(\Omega<0\) for \(\lambda>0\), this proves exactly one strict global maximum of \(|\Omega|\) and gives the stated rate.

## Verification

The accompanying standard-library-only `verify.py` independently solves the original six-by-six rational moment system via Gaussian elimination, reconstructs the area rate from its entries, and checks the theorem's closed form on 250 exact-rational parameter combinations (including negative couplings and equal diagonal stiffness). Five additional exact identities check the canonical rational expression. Four checks test the unique-positive-root interval and numerical location, and eight check the positive-denominator polynomial identity. Running `python verify.py` on the included file yields `PASS: 267 exact rational assertions`. These finite checks validate algebraic cases; the proof above establishes the complete parameter range.

## Relationship to prior work

Randomly switched scalar harmonic traps were treated theoretically by Biroli, Kulkarni, Majumdar and Schehr (2023), and subsequently in the experimentally validated version first made public in August 2025. Their harmonically trapped Brownian particles use randomly varying scalar stiffness and study many-particle correlations and extreme positions. Scalar confinement is rotationally symmetric; it has no tilted two-dimensional stiffness matrix with the cross moment needed for the signed area law here.

Single- and multiple-bath Brownian gyrators are established models. In particular, Dutta and Saha (2026) examine a Brownian ellipsoid with *different temperatures in distinct directions*; Chor, Godec and Raz (2026) study multiple reservoirs and a transformed curl-force representation; and the fractional Brownian gyrator literature studies direction-dependent temporal noise. These do not directly provide the two-conservative-trap, one-isotropic-bath, Poisson-switching cubic law. The elementary matrix-moment framework is standard and is not claimed as new. This report claims only the explicit cubic cancellation, strict chirality criterion, endpoint limits and canonical unique optimal switching rate for this specified model.

## Limitations

This is an exact stationary second-moment/area-current theorem, not a formula for the full probability density or entropy-production rate. The pathwise area observable is distinct from mean polar-angular velocity. No claims are made about nonlinear or time-dependent traps, state-dependent switching, or finite-time convergence rates. The result uses uniform additive noise, symmetric switching, and identical diagonal stiffnesses across phases. No novelty certificate is asserted: a broader Markov-switching diffusion theorem or an inaccessible detailed treatment of flashing gyrators might subsume the formula. Several relevant papers could only be inspected through abstracts or indexed substantial passages, and institutional the complete 2026 curl-forces paper was not accessible for comparison.

## References

- M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan and G. Schehr, *Experimental evidence for strong emergent correlations between particles in a switching trap*, arXiv:2508.07199 (first public 2025-08-10); Phys. Rev. Lett. **137**, 037102 (2026). https://arxiv.org/abs/2508.07199
- M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (2023); Phys. Rev. E **109**, L032106 (2024). https://arxiv.org/abs/2312.02570
- S. Dutta and A. Saha, *Microscopic gyration of a Brownian ellipsoid*, Proc. R. Soc. A **482**, 20250754 (2026). https://doi.org/10.1098/rspa.2025.0754
- O. Chor, A. Godec and O. Raz, *Hamiltonian curl-forces in systems coupled to multiple thermal reservoirs*, arXiv:2610.08423 (first public 2026-10-06). https://arxiv.org/abs/2610.08423
- *Fractional Brownian gyrator*, J. Phys. A (2022). https://doi.org/10.1088/1751-8121/aca4aa
- L. Arnold and P. Kloeden, *Lyapunov exponents and rotation number of two-dimensional systems with telegraphic noise*, SIAM J. Appl. Math. (1989). https://doi.org/10.1137/0149075
