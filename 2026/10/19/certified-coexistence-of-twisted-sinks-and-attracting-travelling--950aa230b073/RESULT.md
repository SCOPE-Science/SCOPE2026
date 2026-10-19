# Certified coexistence of twisted sinks and attracting travelling three-cycles in a discrete Huygens triangle

## Finding

On the equal-weight repulsive three-oscillator discrete Huygens triangle, **there exist at least four distinct hyperbolically attracting phase classes at the same interaction strength**: the two uniform twisted fixed points and two orientation-reflected prime-period-three travelling orbits. This occurs at the **exact rational strength** \(h=57/50\) and persists throughout some open interval about that value. Thus the twisted sinks do not have an almost-global basin throughout their local-stability range.

More precisely, with \(P(a,b,c)=(c,a,b)\), there is a point \(z=(a,b,-a-b)\) with

\[
|a-1.514991066322|\le 10^{-8},\qquad
|b-0.512312470864|\le 10^{-8}
\]

such that \(F_h(z)=Pz\) modulo \(2\pi\). Both \(z,Pz,P^2z\) and their negatives are prime-period-three attracting orbits. Both \(\pm(2\pi/3)\mathbf1\) remain attracting fixed points. Every assertion concerns the full two-dimensional relative-phase torus; no global cycle census is claimed.

## Assumptions and scope

Three equally coupled identical oscillators interact reciprocally with \(\sin\) phase-difference response in discrete time. Their edge differences live in

\[
\mathcal Z=\{(z_1,z_2,z_3)\in(\mathbb R/2\pi\mathbb Z)^3:\ z_1+z_2+z_3\equiv0\pmod{2\pi}\}.
\]

The induced quotient map is

\[
F_h(z)=z+hK\sin z\pmod{2\pi},\quad
K=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix},\quad h>0.
\]

Here sine is componentwise. On the tangent plane \(E=\mathbf1^\perp\), \(K=3I\); the spectral potential-descent bound is \(0<h<2/3\). The two uniform twisted fixed points are attracting for \(0<h<4/3\), since each tangent multiplier equals \(1-3h/2\).

## Proof

**1. Reduce a travelling three-cycle to two equations.** Write \(c=-a-b\). For the cyclic permutation \(P(a,b,c)=(c,a,b)\), the condition \(F_h(a,b,c)=P(a,b,c)\pmod{2\pi}\), using the branch where the first coordinate advances by \(2\pi\), is equivalent to

\[
R_1(a,b)=2a+b+h(2\sin a-\sin b-\sin c)-2\pi=0,
\]
\[
R_2(a,b)=b-a+h(2\sin b-\sin a-\sin c)=0.
\]

The third equation follows from the preserved sum. Set \(h=57/50\), \(q=(1.514991066322,0.512312470864)\), and \(r=10^{-8}\). Use the fixed rational matrix

\[
M=\begin{pmatrix}
0.762247899&0.152210095\\
0.480438085&0.498391907
\end{pmatrix}.
\]

**2. Certify an actual zero.** All entries of \(q,M,h,r\) are interpreted as exact rational numbers. The companion verifier bounds \(\sin\), \(\cos\), and \(\pi\) by rational intervals using Taylor's theorem and Machin's identity. It proves at the center, for the max norm,

\[
\|MR(q)\|_\infty<10^{-9},\qquad
\|I-MDR(q)\|_\infty+7h r\|M\|_\infty<10^{-5}.
\]

Indeed, since cosine is globally \(1\)-Lipschitz, each row sum of \(DR(x)-DR(q)\) on the closed box \(\|x-q\|_\infty\le r\) is at most \(7hr\). The rational interval upper bounds imply that \(x\mapsto x-MR(x)\) contracts that box strictly into itself. The Banach fixed-point theorem yields a unique **genuine** zero of \(R\) inside the box. The inverse matrix is non-singular, so a fixed point of the contraction is a zero of \(R\).

**3. Certify stability in both quotient directions.** Define the co-rotating map \(T=P^{-1}F_h\). Since \(P\) commutes with \(F_h\), \(F_h^3=T^3\). The point from step 2 is fixed by \(T\). In coordinates \(a,b\), its derivative is

\[
B=DT=\begin{pmatrix}
h(-\cos a+\cos c)&1+h(2\cos b+\cos c)\\
-1+h(-2\cos c-\cos a)&-1+h(-2\cos c-\cos b)
\end{pmatrix}.
\]

Exact interval evaluation on the entire validated root box gives

\[
-1.56<\operatorname{tr}B<-1.55,\qquad
0.70<\det B<0.71.
\]

Consequently \(1+\operatorname{tr}B+\det B>0\), \(1-\operatorname{tr}B+\det B>0\), and \(1-\det B>0\). These strict second-order Schur inequalities put both eigenvalues of \(B\) inside the open unit disk. The two eigenvalues of the period-three return \(DF_h^3=B^3\) also lie there. The certified coordinates are pairwise distinct modulo \(2\pi\), so the orbit is genuinely of prime period three.

**4. Distinguish all four sinks and make them robust.** Oddness \(F_h(-z)=-F_h(z)\) supplies another attracting three-cycle with the opposite orientation. The two cycles are disjoint because the three coordinates in the certified box are nonzero and unequal in magnitude, so their multiset is not invariant under negation. At each uniform twist \(z=\pm(2\pi/3)\mathbf1\), the two tangent multipliers are \(1-3h/2=-71/100\), strictly inside the unit disk. A hyperbolic attractor has an open basin of positive two-dimensional torus measure. Since all four are hyperbolic and since \(I-DT\) is invertible, the implicit-function theorem and continuity of eigenvalues continue both travelling cycles and both fixed sinks under sufficiently small changes in \(h\).

## Verification

Run the **complete embedded standalone file** `verify_triangle_cycle.py` with Python 3.10 or later. It uses exact integer/fraction arithmetic for every logical comparison, interval enclosures for transcendental constants and trigonometric evaluations, and checks the contraction, inclusion, root separation, and all three strict Schur inequalities. The code does not infer existence from floating-point iterations; the finite computation supplies rational inequalities used in the analytic Banach fixed-point argument. The verified inequalities, combined with the stated algebraic equivariance identities, establish the claim.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (arXiv:2610.10993v1, publicly posted October 7, 2026) establish the discrete Huygens graph-gradient framework, classify equilibrium geometry including the frustrated all-to-all triangle, and prove strict Lyapunov decrease below the graph spectral limit. Their results do not assert the existence of attracting prime-period-three cycles above that limit.

Buescu and Oliveira (arXiv:2610.19953v1, publicly posted October 14, 2026) establish almost-global convergence to twisted minima on the strict-descent interval for rings and explicitly identify the open question beyond that interval. This later paper is cited as scientific context alongside the earlier motivating work.

Kalmár-Nagy, Horváth and Vincze (2025) analyze fixed points, periodic dynamics and chaos in small fully coupled discrete-time Kuramoto systems; only the publisher's short preview could be inspected here. Its complete paper may contain closely related numerics or results, and priority remains uncertain. Maistrenko et al. (2008) study phase chaos and periodic multistability, chiefly in a four-oscillator model, providing further context.

## Limitations

The result asserts **at least** four distinct attractors, not that no others exist. The open parameter interval is not numerically optimized. It proves a mathematically certified finite-step coexistence example, not a complete bifurcation diagram or a statement about arbitrary networks. The exact-parameter certificate is self-contained; bibliographic priority against the inaccessible full 2025 article is not independently settled.

## References

1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public October 7, 2026), https://arxiv.org/html/2610.10993v1.
2. J. Buescu, H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (first public October 14, 2026), https://arxiv.org/html/2610.19953v1.
3. T. Kalmár-Nagy, D. A. Horváth, B. Vincze, *Synchronization in Small, Fully Coupled Systems of Discrete-Time Kuramoto Oscillators*, Int. J. Bifurcation Chaos 35 (2025), 2530032, https://doi.org/10.1142/S0218127425300320.
4. V. L. Maistrenko, A. A. Vasylenko, Y. L. Maistrenko, E. Mosekilde, *Phase Chaos and Multistability in the Discrete Kuramoto Model*, Nonlinear Oscillations 11 (2008), 229–241, https://doi.org/10.1007/s11072-008-0026-4.
