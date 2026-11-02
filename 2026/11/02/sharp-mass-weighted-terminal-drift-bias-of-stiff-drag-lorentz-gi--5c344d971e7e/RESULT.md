# Sharp mass-weighted terminal-drift bias of stiff drag–Lorentz GIRK

## Finding

For the uniform, constant-coefficient charged-dust/gas relative-motion problem, the stiff two-stage GIRK source integrator, composed as source–forcing–source, has a forced fixed point whose **relative error in the physical relative-kinetic norm** is at most the universal sharp constant

\[
C_*=\left[\frac{s_*}{(1+4s_*)(4s_*^2+s_*+4)}\right]^{1/2}=0.174872575596\ldots,
\qquad 8s_*^3+2s_*^2=1,\quad s_*>0.
\]

This inequality holds with any finite number of species, arbitrary signed gyrofrequencies, and arbitrarily nonnormal drag–Lorentz coupling. Its sharp supremum is approached by a genuine one-species charged-dust system in the *stiff* step-selection regime; it is not attained with strictly positive drag.

## Assumptions and scope

Fix an integer \(m\ge1\), a gas density \(\rho_g>0\), dust-to-gas mass ratios \(\epsilon_i>0\), constant stopping-rate parameters \(\alpha_i>0\), signed gyrofrequencies \(\Omega_i\in\mathbb R\), a fixed magnetic unit direction \(\hat b\), and a constant differential external acceleration \(A_{\rm rel}\in\mathbb R^{3m}\). Set \(B_\times v=v\times\hat b\), \(T_i=-\alpha_iI_3+\Omega_iB_\times\), and for block vectors \(W=(w_i)_{i=1}^m\) let

\[
(M_{\rm rel}W)_i=T_iw_i+\sum_{j=1}^m\epsilon_jT_jw_j,
\qquad \dot W=M_{\rm rel}W+A_{\rm rel}.
\]

The terminal velocity is \(W_*=-M_{\rm rel}^{-1}A_{\rm rel}\). The positive-definite relative kinetic metric is

\[
Q=\rho_g\left(\operatorname{diag}(\epsilon_1,\ldots,\epsilon_m)-\frac{\epsilon\epsilon^{\mathsf T}}{1+\sum_i\epsilon_i}\right)\otimes I_3,
\qquad \|W\|_Q=\sqrt{W^{\mathsf T}QW}.
\]

For a full timestep \(\Delta t>0\), write \(Z=(\Delta t/2)M_{\rm rel}\). The source half-step on the stiff branch has stability function

\[
R(z)=\frac{1-z}{1-2z+2z^2}.
\]

For the exact uniform forcing part between the half-steps, the recurrence and its fixed point are

\[
W^{n+1}=R(Z)^2W^n+\Delta t\,R(Z)A_{\rm rel},\qquad
W_{\rm fp}=\Delta t\,[I-R(Z)^2]^{-1}R(Z)A_{\rm rel}.
\]

The claim concerns the algebraic fixed point for every positive timestep. When the paper's stiff branch is selected and its step-stability condition holds, that fixed point is also the attractive numerical terminal drift. No claim is made for the source integrator's resolved coefficient set.

## Proof

**Dissipativity in the physical metric.** Write \(E=\sum_i\epsilon_i\), \(D_\epsilon=\operatorname{diag}(\epsilon_i)\), and \(S=I_m+\mathbf1\epsilon^{\mathsf T}\). The identity

\[
\left(D_\epsilon-\frac{\epsilon\epsilon^{\mathsf T}}{1+E}\right)S=D_\epsilon
\]

implies, with the block-diagonal \(\operatorname{diag}(T_i)\), that

\[
\operatorname{Re}\langle W,M_{\rm rel}W\rangle_Q
=-\rho_g\sum_{i=1}^m\epsilon_i\alpha_i\|w_i\|_2^2<0\quad(W\ne0).
\]

The matrix \(Q\) is positive definite by weighted Cauchy–Schwarz because \(E/(1+E)<1\). Consequently \(M_{\rm rel}\), and hence \(Z\), is strictly dissipative in the \(Q\)-inner product; its spectrum lies in the open left half-plane.

**Exact error transfer function.** Put \(D(z)=1-2z+2z^2\), \(N(z)=1-z\). Direct multiplication gives

\[
D(z)^2-N(z)^2=z(2z-1)(2z^2-3z+2).
\]

Since \(A_{\rm rel}=-M_{\rm rel}W_*\) and \(\Delta t\,M_{\rm rel}=2Z\), the fixed-point error, as an identity of rational matrix functions, is

\[
W_{\rm fp}-W_*=f(Z)W_*,\qquad
f(z)=-\frac{z}{(2z-1)(2z^2-3z+2)}.
\]

Every pole of \(f\) lies in the open right half-plane, at \(1/2\) or \((3\pm i\sqrt7)/4\). The apparent zero cancellation at \(z=0\) is harmless because \(Z\) is invertible. In particular the fixed point exists and is unique for every \(\Delta t>0\).

**Exact scalar half-plane maximum.** For \(z=x+iy\), \(x\le0\), and \(s=|z|^2\), expansion yields

\[
|2z-1|^2=1+4s-4x,
\]
\[
|2z^2-3z+2|^2=4s^2+s+4+16x^2-12(1+s)x.
\]

Both factors are at least their values at \(x=0\). Therefore

\[
|f(z)|^2\le \frac{s}{(1+4s)(4s^2+s+4)}=:G(s),
\]

with equality for purely imaginary \(z\) of modulus \(\sqrt{s}\). The sign of \(G'(s)\) is the sign of \(1-2s^2-8s^3\). This expression decreases strictly from one to minus infinity on the positive real axis, so its unique root \(s_*\) is the unique global maximizer. Thus \(\sup_{\operatorname{Re}z\le0}|f(z)|=C_*\).

**No hidden eigenvector-condition-number factor.** Conjugate by \(Q^{1/2}\), putting \(B=Q^{1/2}ZQ^{-1/2}\). Then \(\operatorname{Re}\langle v,Bv\rangle<0\). Its Cayley transform \(T=(I+B)(I-B)^{-1}\) is a contraction, since

\[
\|(I+B)v\|_2^2-\|(I-B)v\|_2^2=4\operatorname{Re}\langle v,Bv\rangle\le0.
\]

Define \(F(t)=f((t-1)/(t+1))\), which extends analytically across \(t=-1\) and a neighborhood of the closed unit disk: the only poles of \(f\) lie in the right half-plane. Rational functional calculus gives \(f(B)=F(T)\). Von Neumann's contraction inequality (by uniform polynomial approximation of \(F\) on the closed disk) now implies

\[
\|f(Z)\|_{Q\to Q}=\|F(T)\|_2\le\max_{|t|\le1}|F(t)|
=\sup_{\operatorname{Re}z\le0}|f(z)|=C_*.
\]

Multiplying by \(W_*\) proves the theorem without assuming normality.

**Sharpness within the physical stiff branch.** Take one dust species with \(\epsilon=1/10\), a unit gyrofrequency and positive drag \(\alpha\downarrow0\), with a transverse nonzero prescribed terminal drift. For one species the perpendicular relative generator is \((1+\epsilon)(-\alpha I+ B_\times)\), normal in the physical metric. Choose the full timestep

\[
\Delta t_\alpha=\frac{2\sqrt{s_*}}{(1+\epsilon)\sqrt{1+\alpha^2}}.
\]

As \(\alpha\downarrow0\), its perpendicular half-step eigenvalues converge to \(\pm i\sqrt{s_*}\). Moreover \(2\sqrt{s_*}>1+\epsilon\), so \(\Delta t_\alpha\ge(1+\alpha^2)^{-1/2}\): these are actual stiff-branch timesteps by the paper's selection rule. Taking \(A_{\rm rel}=-M_{\rm rel}W_*\) gives

\[
\lim_{\alpha\downarrow0}\frac{\|W_{\rm fp}-W_*\|_Q}{\|W_*\|_Q}=C_*.
\]

Strict positive drag places every relevant eigenvalue strictly inside the half-plane and makes the scalar bound strict; hence finite positive-drag systems cannot attain the supremum.

## Verification

The standalone script `verify.py` performs exact Fraction-based polynomial identity checks, an exact complex-rational matrix calculation for 236 one-, two-, and three-species examples, and numerical root isolation for the scalar cubic. Its random values include positive density ratios, strictly positive drag, and signed gyrofrequencies; the kinetic norms and rational fixed-point transfer identity are independently assembled. The script reports `PASS` when all assertions hold. Finite checks are corroboration only; the proof of all dimensions and parameters is the preceding functional-calculus argument.

## Relationship to prior work

Chen, Li, He, Wibking, Krumholz and Bai (2026), Sections II.3–II.7, Equations (39)–(42), Table 1 and Appendix A, define the charged-dust source splitting, the relative generator, the stiff stability function and the forced terminal-drift fixed point. They report the large-step \(O(\Delta t^{-2})\) bias, but do not in the inspected full text derive an exact sharp uniform mass-weighted error bound for arbitrary multicomponent nonnormal matrices. Tedeschi-Prades et al. (2025) develop the aerodynamic-drag GIRK precursor; their source treatment and numerical tests do not establish the claimed charged drag–Lorentz half-plane constant. Von Neumann's contraction inequality is established standard operator theory, used here rather than claimed as new. The proposed addition is the particular exact rational error function, its sharp half-plane maximum, the physical dissipativity metric, and attainment in the stiff model class.

## Limitations

The result assumes constant drag coefficients, gyrofrequencies, densities and magnetic direction, and an exact uniform forcing substep; it is not a theorem for Picard-truncated nonlinear updates or spatial transport. It bounds the forced fixed-point bias, not the norm of transient propagation, physical time-to-equilibrium, total-velocity error or practical floating-point stability. The constant is a sharp supremum, not an attainable maximum when every drag coefficient is positive. The exact historical priority of the specialization cannot be guaranteed from the inspected literature alone.

## References

1. M. Chen, H. Li, C.-C. He, B. D. Wibking, M. R. Krumholz and X.-N. Bai, *A Nonlinear General Implicit Runge–Kutta Integrator for Multifluid Charged Dust and Gas*, arXiv:2610.18979v1 (13 October 2026), https://arxiv.org/html/2610.18979v1 .
2. G. Tedeschi-Prades, T. Birnstiel, K. Dolag, B. Ercolano and M. Hutchison, *General Implicit Runge-Kutta Integrators for Multifluid Gas-Dust Aerodynamic Drag*, arXiv:2511.07562v1 (10 November 2025), https://arxiv.org/html/2511.07562v1 .
3. J. von Neumann, *Eine Spektraltheorie für allgemeine Operatoren eines unitären Raumes*, Math. Nachr. 4 (1951), 258–281 (contraction inequality).